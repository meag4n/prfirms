# New York City Public Relations Firms Scrape

## What does this repo do?

This is a web scraper I built to scrape PR firms in New York City from the website clutch.co. I wanted to see how the marketing of a firm -- including its name and slogan -- related to its average hourly rate.

## What steps did I take to make this?

First, I created a CSV file and wrote its headers with

```
csvfile = open("firms.csv", "w", newline='', encoding="utf-8")
c = csv.writer(csvfile)

c.writerow(["name","url","slogan", "rate"])
```

Next, using the get_firm_details function, I individually scraped:

The entire block each firm is in:
```
li_list = soup.findAll("li", class_="provider-row")
```

Its name and clutch.co profile url, which are both located under the same h3:
```
h3_list = li.find('h3', class_='company-name')
a_list = h3_list.find("a")
firm_details_list.append(a_list.text)
firm_details_list.append(a_list.attrs["href"])
```

Its slogan:
```
p_list = li.find("p", class_="tagline")
firm_details_list.append(p_list.text)
```

And its rate:
```
try:
      div_list = li.find("div", class_="module-list")
      children = div_list.findAll("div", class_="list-item")
      firm_details_list.append(children[1].text)
      print(children[1])
except:
      print("Undisclosed")
```

For the second function, I used the for i range function to repeat the process for each page. The function has an integer range to add a page=number part of each URL, allowing me to scrape all 19 pages.

```
for i in range(19):
    url = "https://clutch.co/us/pr-firms?page=" + str(i) + "&sort_by=&location%5Bcountry%5D=US&location%5Bcity%5D=US%23NY%23New%20York&op=Apply&form_id=spm_exposed_form&form_build_id=form-rpwCWWuWTyuryfIbFDIhe1edxFa8UrA7FxS2vHa1G8s"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    csv_list = get_firm_details(soup, csv_list)
```

## Problems I encountered

For the average hourly rate of the PR firm, there were two classes used by the website. "list-item" and "list-item undisclosed" were both used for undisclosed price amounts, so I had to use a try/except function to print "Undisclosed" when the "list-item" class wasn't found. I also didn't anticipate how many firms had undisclosed amounts, which made it a bit harder to analyze how more expensive firms market themselves compared to lower-end firms.
