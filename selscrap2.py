from selenium import webdriver
import urllib.request
import json

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.metacritic.com/browse/tv/score/metascore/all/filtered?sort=desc")

from datetime import datetime
time = datetime.now()


tvshowlist = []
i = 1
while i<=100:
    for tvshow in driver.find_elements_by_tag_name("tr"):
        print(tvshow.text)
        for tag in tvshow.find_elements_by_tag_name("a"):
            for img in tag.find_elements_by_tag_name("img"):
                print(img.get_attribute("src"))
                urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
                i = i+1
                
                tvshowlist.append(
                    {"NO": tvshow.text.split("\n")[1],
                     "TITLE": tvshow.text.split("\n")[2],
                     "RELEASE": tvshow.text.split("\n")[3],
                     "DESCRIPTION" : tvshow.text.split("\n")[4],
                     "Image": img.get_attribute("src"),
                     "RATE": tvshow.text.split("\n")[0],
                     "waktu_scraping":time.strftime("%H:%M:%S  %d-%m-%y"),
                     }
                )


hasil = open('D:\scraping\Lib\site-packages\hasilscrap2.json','w')

json.dump(tvshowlist, hasil,  indent=5)

hasil.close()

driver.quit()