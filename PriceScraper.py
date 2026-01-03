import requests
from bs4 import BeautifulSoup
url="https://books.toscrape.com/"
final_output=requests.get(url)
final_output.encoding = 'utf-8'
organised_data=BeautifulSoup(final_output.text, "html.parser")
price_tag=organised_data.find('p', class_='price_color')
just_the_price=price_tag.text
print("I finished the job")
print(f"The price of the first book is: {just_the_price}")

