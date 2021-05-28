import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
#The library that will turn a weird string library that we'll scrap from Google into one that we can read
import ast

from selenium import webdriver

chromePath=r'D:\\Mridul\\Internship\\Python_files\\chromedriver.exe'

driver = webdriver.Chrome(chromePath)

URL = 'https://www.google.com/search?q=bikes&safe=active&rlz=1C1GCEA_enIN830IN831&sxsrf=ACYBGNSOw73uJMJ0V0jUGfaRBgEsuHzUeg:1580365723665&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvxMuM2arnAhWDUn0KHeJQCncQ_AUoAXoECBAQAw&biw=736&bih=635'
directory = 'Bikes'


def getURLs(URL):

    driver.get(URL)
    
    page = driver.page_source
    print(page)

    soup = Soup(page, 'lxml')

    desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})

    ourURLs = []

    for url in desiredURLs:
        theURL = url.text
        theURL = ast.literal_eval(theURL)['ou']

        ourURLs.append(theURL)

    return ourURLs




def save_images(URLs, directory):

    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, url in enumerate(URLs):
        savePath = os.path.join(directory, '{:06}.jpg'.format(i))

        try:
            ulib.urlretrieve(url, savePath)

        except:
            print('I failed with', url)









URLs = getURLs(URL)


for url in URLs:
    print(url)

save_images(URLs, directory)