from bs4 import BeautifulSoup
import requests

url = 'https://clutch.co/us/pr-firms?&sort_by=&location%5Bcountry%5D=US&location%5Bcity%5D=US%23NY%23New%20York&op=Apply&form_id=spm_exposed_form&form_build_id=form-rpwCWWuWTyuryfIbFDIhe1edxFa8UrA7FxS2vHa1G8s'

import csv

csvfile = open("firms.csv", "w", newline='', encoding="utf-8")
c = csv.writer(csvfile)

c.writerow(["name","url","slogan", "rate"])

csv_list = []

def get_firm_details(soup, csv_list):
    li_list = soup.findAll("li", class_="provider-row")
    for li in li_list:
        firm_details_list = []
        h3_list = li.find('h3', class_='company-name')
        a_list = h3_list.find("a")
        firm_details_list.append(a_list.text)
        firm_details_list.append(a_list.attrs["href"])
        p_list = li.find("p", class_="tagline")
        firm_details_list.append(p_list.text)
        try:
            div_list = li.find("div", class_="module-list")
            children = div_list.findAll("div", class_="list-item")
            firm_details_list.append(children[1].text)
            print(children[1])
        except:
            print("Undisclosed")

        c.writerow(firm_details_list)

    return firm_details_list

for i in range(19):
    url = "https://clutch.co/us/pr-firms?page=" + str(i) + "&sort_by=&location%5Bcountry%5D=US&location%5Bcity%5D=US%23NY%23New%20York&op=Apply&form_id=spm_exposed_form&form_build_id=form-rpwCWWuWTyuryfIbFDIhe1edxFa8UrA7FxS2vHa1G8s"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    csv_list = get_firm_details(soup, csv_list)

for index, item in enumerate(csv_list):
    print(index, item)

csvfile.close()
