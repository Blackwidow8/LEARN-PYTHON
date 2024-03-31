import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.zinduaschool.com/blog/")

soup =BeautifulSoup(response.text, "html.parser")

website_text = response.text

with open("index.html", "w") as blogs_page:
    blogs_page.write(soup.prettify())

    container = soup.find("div", id="archive-container")
    articles =  container.find_all("article")

with open ("blogs.txt", "a") as blogs:
    for article in articles:
        title= article.find("h2",class_="entry-title")
        author = article.find("span", class_="author")
        footer = article.find("footer", class_="entry-footer")
        link = footer.find("a", class_="post-more-link")
        path = link.get("href")


    blogs.write(f"Title:{title.text}\n Author:{author.text}\n Link: {path}\n\n")

def