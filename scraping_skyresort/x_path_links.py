import requests
from parsel import Selector
total_pages = 32
all_link = []
#loop through over the pages
for page in range(1,total_pages+1):

    if page == 1:
        url = "https://www.skiresort.info/ski-resorts"
    else:
        url = f"https://www.skiresort.info/ski-resorts/page/{page}/"
        
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully fetched:" ,response)
        sel = Selector(text=response.text)
        
        #Define the path
        elements = sel.xpath('//div[@id= "resortList"]//div[@class="h3"]/a')
        for element in elements:
            text = element.xpath("./text()").getall()
            urls = element.xpath("./@href").getall()
            all_link.append(url)
            #print(f'Text is: {text} | Url: {urls}')
            #print(len(urls))
print(len(all_link))
     
    
            
