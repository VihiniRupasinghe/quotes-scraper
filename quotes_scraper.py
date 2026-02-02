import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Set the URL
url = "http://quotes.toscrape.com/"

# Step 2: Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract quotes
quotes_data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]
    
    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)  # join tags into one string
    })

# Step 4: Save to CSV
df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)

print("Scraping complete! Saved quotes.csv")
print(df.head())  # shows first 5 rows in IDLE # Count quotes per author
author_counts = df['Author'].value_counts()
print("Quotes per author:")
print(author_counts)

# Count how many times each tag appears
all_tags = df['Tags'].str.split(", ").explode()
tag_counts = all_tags.value_counts()
print("\nMost common tags:")
print(tag_counts)

