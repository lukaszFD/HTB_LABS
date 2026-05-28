import requests # Musi być requests, a nie web_scraper
import re
from bs4 import BeautifulSoup

PAGE_URL = 'http://154.57.164.64:30832'

def get_html_of(url):
    # Ta linia wymaga zaimportowanej biblioteki requests
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()

def count_occurrences_in(word_list):
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count

def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    # Tutaj możesz też dodać print(raw_text), żeby zobaczyć treść i cenę!
    return re.findall(r'\w+', raw_text)

def get_top_words_from(all_words):
    occurrences = count_occurrences_in(all_words)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

# GŁÓWNA LOGIKA
all_words = get_all_words_from(PAGE_URL)
top_words = get_top_words_from(all_words)

# Wyświetlamy top 10 słów
for i in range(10):
    print(top_words[i][0])

    # Dodaj to na końcu swojego skryptu:
    html = get_html_of(PAGE_URL)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()

    # Szukamy fragmentu o koncie rodzinnym
    if "family" in text.lower():
        start_index = text.lower().find("family")
        # Wyświetlamy 100 znaków po słowie "family", żeby zobaczyć cenę
        print(text[start_index:start_index + 100])