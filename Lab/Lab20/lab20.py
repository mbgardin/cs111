import urllib.parse
import requests


# Q1: Get Domain
def get_domain(url):
    """
    Given a URL, returns the full domain of the URL (including the scheme),
    or an empty string if the scheme is not valid or no domain is present.
    """
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme in ['http', 'https'] and parsed_url.netloc:
        return f"{parsed_url.scheme}://{parsed_url.netloc}"
    return ''


# Q2: Combine Paths
def combine_paths(url, path):
    """
    Given a base URL and a path to another page, combines them to return the full URL to the other page.
    """
    return urllib.parse.urljoin(url, path)


# Q3: Combine URLs
def combine_urls(base_url, url_to_join):
    """
    Combines the base URL and the URL to join, returning the full URL.
    """
    return urllib.parse.urljoin(base_url, url_to_join)


# Q4: Print Pages
def print_pages(url, paths, output_filename):
    """
    Given a base URL and a list of paths or pages, this function combines them,
    retrieves their content, and writes them to the specified output file.
    Each page's content should start on its own line.
    """
    current_url = url  # Start with the base URL
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for path in paths:
            # If the path starts with a '/', treat it as an absolute path and join it with the domain
            if path.startswith('/'):
                current_url = urllib.parse.urljoin(url, path)
            # Otherwise, join it as a relative page to the current URL
            else:
                current_url = urllib.parse.urljoin(current_url, path)

            # Fetch the content of the current URL and write it to the file
            response = requests.get(current_url)
            if response.status_code == 200:
                output_file.write(response.text + '\n')
            else:
                output_file.write(f"Failed to retrieve {current_url}\n")


# Main section for testing
if __name__ == "__main__":
    # Test Q1: Get Domain
    print(get_domain('https://cs111.byu.edu/lab/lab20/'))  # Output: https://cs111.byu.edu
    print(get_domain('http://en.wikipedia.org/w/index.php'))  # Output: http://en.wikipedia.org
    print(get_domain('proj/proj4/'))  # Output: ''

    # Test Q2: Combine Paths
    print(combine_paths('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/'))  # Output: https://cs111.byu.edu/lab/lab20/
    print(combine_paths('https://cs111.byu.edu/hw/hw03/#part-2',
                        '/articles/about/'))  # Output: https://cs111.byu.edu/articles/about/

    # Test Q3: Combine URLs
    print(combine_urls('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/'))  # Output: https://cs111.byu.edu/lab/lab20/
    print(combine_urls('https://cs111.byu.edu/lab/lab08', 'lab20/'))  # Output: https://cs111.byu.edu/lab/lab20/
    print(combine_urls('https://cs111.byu.edu/hw/hw05/',
                       'https://www.wikipedia.org'))  # Output: https://www.wikipedia.org
    print(combine_urls('https://cs111.byu.edu/lab/lab20/assets/page1.html',
                       'page2.html'))  # Output: https://cs111.byu.edu/lab/lab20/assets/page2.html

    # Test Q4: Print Pages
    # This will write the content of two example pages to 'pages.output.txt'
    print_pages('https://cs111.byu.edu', ['/lab/lab20/assets/page1.html', 'page2.html'], 'pages.output.txt')
