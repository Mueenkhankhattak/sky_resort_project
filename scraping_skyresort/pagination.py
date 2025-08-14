import requests 
from parsel import Selector

url = "https://www.skiresort.info/ski-resorts/"
base_url = "https://www.skiresort.info/"
all_url = []

while True:
    print(f"Scraping: {url}")
    response = requests.get(url)
    response.raise_for_status()
    sel = Selector(text=response.text)
    elements = sel.xpath('//div[@id= "resortList"]//div[@class="h3"]/a')
    
    for element in elements:
        text = element.xpath('./text()').get()
        link = element.xpath('./@href').get()
        if link :
            all_url.append(link)
        
    
    next_page = sel.xpath('//ul[@id="pagebrowser2"]//li/a[contains(text(), "›")]/@href').get()
    #if not next_page:
        #break
    if next_page == 32:
        break
    url = base_url + next_page

print(len(all_url))