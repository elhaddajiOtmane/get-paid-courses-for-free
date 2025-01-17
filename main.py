import requests
from bs4 import BeautifulSoup

def get_date_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    time_element = soup.find('time', class_='post-published updated')
    if time_element:
        return time_element['datetime']
    return None

# Example usage
url = input("Enter the URL: ")
date = get_date_from_url(url)
if date:
    print("Extracted date:", date)
else:
    print("Date not found.")
