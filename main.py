import requests
import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import request
import pandas as pd
import numpy as np

# links= {'sensors': ['https://electropeak.com/sensors?product_list_limit=60',
#                     'https://electropeak.com/sensors?p=2&product_list_limit=60',
#                     'https://electropeak.com/sensors?p=3&product_list_limit=60',
#                     'https://electropeak.com/sensors?p=4&product_list_limit=60',
#                     'https://electropeak.com/sensors?p=5&product_list_limit=60',
#                     'https://electropeak.com/sensors?p=6&product_list_limit=60',
#                     'https://electropeak.com/sensors?p=7&product_list_limit=60',
#                     'https://electropeak.com/sensors?p=8&product_list_limit=60',],
#         'development-boards':'https://electropeak.com/development-boards',
#         'displays':'https://electropeak.com/displays',
#         'wireless-iot':'https://electropeak.com/wireless-iot',
#         'robotics':'https://electropeak.com/robotics'}
# Chrome_options=webdriver.ChromeOptions()
# Chrome_options.add_experimental_option('detach',True)
#
# browser=webdriver.Chrome(options=Chrome_options)
#
# browser.get('https://electropeak.com/sensors')


# webpage = requests.get(links['sensors'])
#
# soup=BeautifulSoup(webpage.content,'html.parser')
#
#
# items_name_and_link=soup.find_all('a',attrs={ "class" : "product-item-link" })
# items_price=soup.find_all('span',attrs={ "class" : "price" })
# items_image=soup.find_all('img',attrs={ "class" : "product-image-photo" })

from get_links import Get_Data

getting=Get_Data()
getting.making_soup()


def get_product_names(pages):
    final = []
    for page in pages:
        batch = []
        for item in page:
            batch.append(str(item.getText().strip()))
        final.append(batch)
    return final

def get_product_links(pages):
    final=[]
    for page in pages:
        batch = []
        for item in page:
            batch.append(str(item.get('href')))
        final.append(batch)
    return final

def get_product_prices(pages):
    final = []
    for page in pages:
        batch=[]
        for item in page[:-4]:
            batch.append(str(item.getText()))
        final.append(batch)
    return final

def get_product_images(pages):
    final = []
    for page in pages:
        batch = []
        for item in page:
            batch.append(str(item.get('src')))
        final.append(batch)
    return final


# ass=get_product_prices(getting.items_price)
# print(len(ass))
# pprint.pprint(len(str(getting.items_name_and_link)))
# pprint.pprint(get_product_prices(getting.items_price))
topics=['sensors',
        'development-boards',
        'displays',
        'wireless-iot',
        'robotics']

all_names=get_product_names(getting.items_name_and_link)
all_links=get_product_links(getting.items_name_and_link)
all_prices=get_product_prices(getting.items_price)
all_images=get_product_images(getting.items_image)

# pprint.pprint(getting.items_image)
# pprint.pprint(f'lenghth: \\n {len(getting.items_image)}')

# pprint.pprint(all_images)

output= {'sensors': 8,
         'development-boards': 15,
         'displays': 20,
         'wireless-iot': 25,
         'robotics': 32}
def saving(output,path,index):
    df=pd.DataFrame(output,columns=['Product names','links','prices','images'])
    csv_file_path = f'{path}_data.csv'
    df.to_csv(csv_file_path)
    d=index
    print(f'CSV file &quot;{csv_file_path}&quot; has been created successfully.')



for key in topics:
        if key == 'sensors':
            output = {'Product names':
                all_names[0] + all_names[1] + all_names[2] + all_names[3] + all_names[4] + all_names[5] + all_names[6] +
                all_names[7],
                'links':
                    all_links[0] + all_links[1] + all_links[2] + all_links[3] + all_links[4] + all_links[5] + all_links[
                        6] + all_links[7],
                'prices': all_prices[0] + all_prices[1] + all_prices[2] + all_prices[3] + all_prices[4] + all_prices[5] +
                           all_prices[6] + all_prices[7],
                'images': all_images[0] + all_images[1] + all_images[2] + all_images[3] + all_images[4] + all_images[5] +
                           all_images[6] + all_images[7]}
            index = np.arange(len(str(all_names[:8])))
            saving(output, key, index)
            # for key,value in output.items():
            #     print(key,len(value),'\\n')

        if key == 'development-boards':
            output = {'Product names':
                all_names[8] + all_names[9] + all_names[10] + all_names[11] + all_names[12] + all_names[13] + all_names[
                    14],
                'links':
                    all_links[8] + all_links[9] + all_links[10] + all_links[11] + all_links[12] + all_links[13] + all_links[
                        14],
                'prices':
                    all_prices[8] + all_prices[9] + all_prices[10] + all_prices[11] + all_prices[12] + all_prices[13] +
                    all_prices[14],
                'images':
                    all_images[8] + all_images[9] + all_images[10] + all_images[11] + all_images[12] + all_images[13] +
                    all_images[14]}
            index = np.arange(len(str(all_names[:15])))
            saving(output, key, index)

        if key == 'displays':
            output = {'Product names':
                all_names[15] + all_names[16] + all_names[17] + all_names[18] + all_names[19],
                'links':
                    all_links[15] + all_links[16] + all_links[17] + all_links[18] + all_links[19],
                'prices': all_prices[15] + all_prices[16] + all_prices[17] + all_prices[18] + all_prices[19],
                'images': all_images[15] + all_images[16] + all_images[17] + all_images[18] + all_images[19]}
            index = np.arange(len(str(all_names[:20])))
            saving(output, key, index)

        if key == 'wireless-iot':
            output = {'Product names':
                all_names[20] + all_names[21] + all_names[22] + all_names[23] + all_names[24],
                'links':
                    all_links[20] + all_links[21] + all_links[22] + all_links[23] + all_links[24],
                'prices': all_prices[20] + all_prices[21] + all_prices[22] + all_prices[23] + all_prices[24],
                'images': all_images[20] + all_images[21] + all_images[22] + all_images[23] + all_images[24]}
            index = np.arange(len(str(all_names[:25])))
            saving(output, key, index)

        if key == 'robotics':
            output = {'Product names':
                all_names[25] + all_names[26] + all_names[27] + all_names[28] + all_names[29] + all_names[30] + all_names[
                    31],
                'links':
                    all_links[25] + all_links[26] + all_links[27] + all_links[28] + all_links[29] + all_links[30] +
                    all_links[31],
                'prices':
                    all_prices[25] + all_prices[26] + all_prices[27] + all_prices[28] + all_prices[29] + all_prices[30] +
                    all_prices[31],
                'images':
                    all_images[25] + all_images[26] + all_images[27] + all_images[28] + all_images[29] + all_images[30] +
                    all_images[31]}
            index = np.arange(len(str(all_names[:32])))
            saving(output, key, index)







