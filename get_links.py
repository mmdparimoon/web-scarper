import requests
from bs4 import BeautifulSoup

class Get_Data():
    def __init__(self):
        self.prd_page_links= {'sensors': ['https://electropeak.com/sensors?product_list_limit=60',
                                          'https://electropeak.com/sensors?p=2&product_list_limit=60',
                                          'https://electropeak.com/sensors?p=3&product_list_limit=60',
                                          'https://electropeak.com/sensors?p=4&product_list_limit=60',
                                          'https://electropeak.com/sensors?p=5&product_list_limit=60',
                                          'https://electropeak.com/sensors?p=6&product_list_limit=60',
                                          'https://electropeak.com/sensors?p=7&product_list_limit=60',
                                          'https://electropeak.com/sensors?p=8&product_list_limit=60' ],
                              'development-boards': ['https://electropeak.com/development-boards?product_list_limit=60',
                                                     'https://electropeak.com/development-boards?p=2&product_list_limit=60',
                                                     'https://electropeak.com/development-boards?p=3&product_list_limit=60',
                                                     'https://electropeak.com/development-boards?p=4&product_list_limit=60',
                                                     'https://electropeak.com/development-boards?p=5&product_list_limit=60',
                                                     'https://electropeak.com/development-boards?p=6&product_list_limit=60',
                                                     'https://electropeak.com/development-boards?p=7&product_list_limit=60', ],
                              'displays': ['https://electropeak.com/displays?product_list_limit=60',
                                           'https://electropeak.com/displays?p=2&product_list_limit=60',
                                           'https://electropeak.com/displays?p=3&product_list_limit=60',
                                           'https://electropeak.com/displays?p=4&product_list_limit=60',
                                           'https://electropeak.com/displays?p=5&product_list_limit=60'
                                           ],
                              'wireless-iot': ['https://electropeak.com/wireless-iot?product_list_limit=60',
                                               'https://electropeak.com/wireless-iot?p=2&product_list_limit=60',
                                               'https://electropeak.com/wireless-iot?p=3&product_list_limit=60',
                                               'https://electropeak.com/wireless-iot?p=4&product_list_limit=60',
                                               'https://electropeak.com/wireless-iot?p=5&product_list_limit=60'],
                              'robotics': ['https://electropeak.com/robotics?product_list_limit=60',
                                           'https://electropeak.com/robotics?p=2&product_list_limit=60',
                                           'https://electropeak.com/robotics?p=3&product_list_limit=60',
                                           'https://electropeak.com/robotics?p=4&product_list_limit=60',
                                           'https://electropeak.com/robotics?p=5&product_list_limit=60',
                                           'https://electropeak.com/robotics?p=6&product_list_limit=60',
                                           'https://electropeak.com/robotics?p=7&product_list_limit=60']}
        self.items_image=[]
        self.items_price=[]
        self.items_name_and_link=[]




    def making_soup(self):
        for key,value in self.prd_page_links.items():
            for items in range(len(value)):
                self.webpage = requests.get(self.prd_page_links[key][items])
                self.soup = BeautifulSoup(self.webpage.content, 'html.parser')

                self.items_name_and_link.append(self.soup.find_all('a', attrs={"class": "product-item-link"}) )
                self.items_price.append(self.soup.find_all('span', attrs={"class": "price"}))
                self.items_image.append(self.soup.find_all('img', attrs={"class": "product-image-photo"}))


