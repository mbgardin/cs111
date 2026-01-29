import requests
from bs4 import BeautifulSoup

# Q1: Downloading a Web Page
def download(url, output_filename):
    """
    Downloads the HTML content of the given URL and saves it to the specified output file.
    """
    # Send a GET request to the URL and get the HTML content
    response = requests.get(url)
    # Open the output file in write mode and save the content
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

# Q2: Prettify
def make_pretty(url, output_filename):
    """
    Downloads the HTML content of the URL, formats it with .prettify(),
    and saves it to the specified output file.
    """
    # Send a GET request and get HTML content
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    # Open the output file and save the formatted HTML content
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

# Q3: Finding Paragraphs
def find_paragraphs(url, output_filename):
    """
    Finds all paragraphs in the HTML content of the URL and writes them (with <p> tags) to the output file.
    """
    # Send a GET request and get HTML content
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all paragraph tags
    paragraphs = soup.find_all('p')
    # Write each paragraph content, including the <p> tags, to the output file
    with open(output_filename, 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(str(paragraph) + '\n')  # Write the entire <p> tag, including the content

# Q4: Finding Links
def find_links(url, output_filename):
    """
    Finds all href links in the HTML content of the URL and writes each one to the output file.
    """
    # Send a GET request and get HTML content
    response = requests.get(url)
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all anchor tags with href attributes
    links = soup.find_all('a', href=True)
    # Write each link to the output file
    with open(output_filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link.get('href') + '\n')
