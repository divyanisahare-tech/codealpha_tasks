import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Get script folder
current_folder = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_folder, "books.csv")

# Website link
url = "http://books.toscrape.com/"

# Fetch webpage
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# Extract books
books = soup.find_all('article', class_='product_pod')

data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    data.append([title, price])

# Save CSV
df = pd.DataFrame(data, columns=["Book Name", "Price"])
df.to_csv(output_path, index=False)

print("CSV saved at:", output_path)
