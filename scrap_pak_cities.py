import pandas as pd
from bs4 import BeautifulSoup
import requests
# from csv import writer

url="https://en.wikipedia.org/wiki/List_of_cities_in_Pakistan_by_population"
city_page=requests.get(url).content
# print(city_page)
soup = BeautifulSoup(city_page, 'html.parser')
# print(soup.title.text)
city_page_table=soup.find("table", attrs={"class","sortable wikitable"})
# print(city_page_table.text)

city_table_tr=city_page_table.find_all("tr")
# print(city_table_tr)

# print(city_table_tr[0].text)

city_table_td=city_table_tr[1].find_all("td")
# print(city_table_td[2].text)

pakistani_cities_dataframe=pd.DataFrame()
# print(pakistani_cities_dataframe)

#loop

for i in range(1,len(city_table_tr)):

    city_table_td=city_table_tr[i].find_all("td")
    # rank=city_table_td[0].get_text().strip()
    city_name=city_table_td[1].get_text().strip()
    population_2017=city_table_td[2].get_text().strip()
    population_1998=city_table_td[3].get_text().strip()
    change_in_population=city_table_td[4].get_text().strip()
    province=city_table_td[5].get_text().strip()

    pakistani_cities_dataframe=pakistani_cities_dataframe.append({"City_name":city_name,
                                                                 "Population_2017":population_2017,
                                                                 "Population_1998":population_1998,
                                                                 "Change_in_population":change_in_population,
                                                                 "Province":province},ignore_index=True)
    pakistani_cities_dataframe.to_csv("pakistani_cities.csv")

