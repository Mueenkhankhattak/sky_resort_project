import requests
from parsel import Selector

url = "https://www.skiresort.info/ski-resort/carezza/"
response = requests.get(url)
if response.status_code == 200:
    print("Successfuly fetched")
    sel = Selector(text=response.text)
    
    resort_name = sel.xpath('//span[@class = "fn"]/text()').get()
    elevation = sel.xpath('//div[@id="selAlti"]/text()').getall()
    oprerating_time = sel.xpath('//table[@class = "info-table"]//tr/td/text()').getall()
    
    print(f"Resort name is : {resort_name}")
    print("***************************")
    print(f"Elevation info is {elevation}")
    print(".************************")
    print(f"operating time is {oprerating_time}")
    
    contact_page_link = sel.xpath('//a[@class="shaded detail-links link-img"]/@href').get()
    response = requests.get(contact_page_link)
    if response.status_code == 200:
        print(f"Successfult fetched!")
        sel = Selector(text=response.text)
        contact_information =sel.xpath('//div[@class="col-sm-9"]//p//br//following-sibling::text()').getall()
        contact_information_website = [text.strip() for text in contact_information if text!=" "]
        print(f"Contact information is {contact_information_website}")
    else:
        print("Error while fetching Html!")
        
    
    
else:
    print("Error: can not fetched the page")