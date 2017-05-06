from bs4 import BeautifulSoup
from urllib import request

def main():
    soup = get_parsed_page("http://www.notabug.fr")
    print_post_titles(soup)
    print('')
    print_post_categories(soup)

def get_parsed_page(url):
    with request.urlopen(url) as page:
        html = page.read()
    return BeautifulSoup(html, 'html.parser')

def print_post_titles(soup):
    print('Titles:')
    post_titles = soup.find_all('p', class_='article-headline-p')
    print_html_elements_text(post_titles)

def print_post_categories(soup):
    print('Categories:')
    post_categories = set(soup.find_all('a', class_='post_category-link'))
    print_html_elements_text(post_categories)

def print_html_elements_text(html_elements):
    for html_element in html_elements:
        print(html_element.getText())

main()
