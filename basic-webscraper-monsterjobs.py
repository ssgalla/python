# import the requests modules
import requests
# import beautifulsoup for html parsing
from bs4 import BeautifulSoup

# insert URL for site that is to be scraped then requesting the requests module to get the URL page and finally call BS4 to parse HTML
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=India'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# using BS4 to find specific HTML ID from site then find all results matching in a section with the HTML class card-content
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')

# for each card-content locate title_elem, company_elem and location_elem once found find the HTML tag they are in print all of them
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()