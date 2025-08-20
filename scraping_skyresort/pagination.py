import requests 
from parsel import Selector
from urllib.parse import urljoin

url = "https://www.skiresort.info/ski-resorts/"
base_url = "https://www.skiresort.info/"

all_url = []

while True:
    print(f"Scraping: {url}")
    response = requests.get(url)
    response.raise_for_status()
    sel = Selector(text=response.text)
    elements = sel.xpath('//div[@id="resortList"]//div[@class="h3"]/a')
    
    for element in elements:
        link = element.xpath('./@href').get()
        if link:
            all_url.append(link)
    
    print(f"Found {len(all_url)} resort links so far…")
    
    
    
    next_page = sel.xpath('//ul[@id="pagebrowser2"]//li/a[contains(text(), "›")]/@href').get()
    if not  next_page:
        break
    url = urljoin(base_url, next_page)
    

#print(f"Total unique resorts scraped: {len(all_url)}")

for link in all_url:
    response = requests.get(link)
    if response.status_code == 200:
        print("Successfuly fetched")
        sel = Selector(text=response.text)
        
        resort_name = sel.xpath('//span[@class = "fn"]/text()').get()
        elevation = sel.xpath('//div[@id="selAlti"]/text()').getall()
        oprerating_time = sel.xpath('//div[@class="description"]//table[@class = "info-table"]//tr//td/text()').getall()
        resort_website = sel.xpath('//div[@id="selLinkCustomer"]/a/@href').get()
        reviews = sel.xpath('//span[@class="text-default altitude"]/text()').get()

        #print(f"Resort name is : {resort_name}")
        print("***************************")
        print(f"Elevation info is {",".join((elevation))}")
        print(".************************")
        print(f"operating time is {",".join(oprerating_time)}")
        print(f"reviews = {reviews}")
        print(f"resort website:  {resort_website}")
        
        contact_page_link = sel.xpath('//a[@class="shaded detail-links link-img"]/@href').get()
        response = requests.get(contact_page_link)
            
        if response.status_code == 200:
            print(f"Successfult fetched!")
            sel = Selector(text=response.text)
            contact_information =sel.xpath('//div[@class="row"]//div[@class = "col-sm-9"]/p/text()').getall()
            phone_number = sel.xpath('//div[@class="col-sm-9"]/p/a[@class = "phonenumber"]/text()').get()
            Email = sel.xpath('//div[@class="col-sm-9"]//p/a[2]/text()').get()
            
            print(f"Contact information is =  {" ".join(contact_information)}")
            print(f'Phone Number : {phone_number}')
            print(f"Email is : {Email}")
            
        else:
            print("Error while fetching Html!")
            
        
        
    else:
        print("Error: can not fetched the page")
