import requests
from parsel import Selector

url = "https://www.skiresort.info/ski-resort/carezza/"
response = requests.get(url)
if response.status_code == 200:
    print("Successfuly fetched")
    sel = Selector(text=response.text)
    
    resort_name = sel.xpath('//span[@class = "fn"]/text()').get()
    elevation = sel.xpath('//div[@id="selAlti"]/text()[2]').get()
    oprerating_time = sel.xpath('//table[@class = "info-table"]//tr/td/text()').get()
    resort_website = sel.xpath('//div[@id="selLinkCustomer"]/a/@href').get()
    
    print(f"Resort name is : {(resort_name)}")
    print("***************************")
    print(f"Elevation info is {elevation}")
    print(".************************")
    print(f"operating time is {oprerating_time}")
    
    print(f"resort website:  {resort_website}")
    
    contact_page_link = sel.xpath('//a[@class="shaded detail-links link-img"]/@href').get()
    response = requests.get(contact_page_link)
        
    if response.status_code == 200:
        print(f"Successfult fetched!")
        sel = Selector(text=response.text)
        contact_information =sel.xpath('//div[@class="col-sm-9"]/p/text()').get()
        phone_number = sel.xpath('//div[@class="col-sm-9"]/p/a/@href').get()
        Email = sel.xpath('//div[@class="col-sm-9"]//p/a[2]/text()').get()
        reviews = sel.xpath('//*[@id="c50"]/div/div[3]/div[2]/div/div[1]/span/text()').get()
        
        print(f"Contact information is {contact_information}")
        print(f'Phone Number : {phone_number}')
        print(f"Email is : {Email}")
        print(f"reviews : {reviews}")
    else:
        print("Error while fetching Html!")
        
    
    
else:
    print("Error: can not fetched the page")