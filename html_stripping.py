from bs4 import BeautifulSoup
from cleantext import clean

def stripping_html(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    clean(stripped_text)
    return stripped_text
