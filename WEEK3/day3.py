import requests
import re
import string
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Walter_Robertson_(artist)")


soup = BeautifulSoup(response.text, "html.parser")


with open("index.html", "w", encoding="utf-8") as article:
    article.write(soup.prettify())

container = soup.find("div", class_="mw-content-container")

paragraphs = container.find_all("p")

cleaned_paragraphs = []

for paragraph in paragraphs:
    cleaned_paragraphs.append(paragraph.text)


final_text = ' '.join(cleaned_paragraphs)

with open("article.txt", "w", encoding="utf-8") as article_text:
    article_text.write(final_text)

pattern = r'\b[A-Za-z]+'

words = re.findall(pattern, final_text)

occurences = {}


for word in words:
    converted_words = word.lower().strip(string.punctuation)
    if converted_words not in occurences:
        occurences[converted_words] =  1
    else:
        occurences[converted_words] += 1

print(occurences)