import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scavenger_hunt(url, element, attribute, output_filename):
    """
    Recursively finds the next URL, HTML element, and attribute in the scavenger hunt
    and stops when it encounters an attribute labeled "final". Writes the final result to output.
    """
    # Loop until we find the 'final' attribute
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            return

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specified HTML element with the given attribute
        tag = soup.find(element, attrs={attribute: True})
        if not tag:
            print(f"No element <{element}> with attribute '{attribute}' found on {url}")
            return

        # Retrieve the attribute value and check if it's the final result
        next_step = tag[attribute]
        if attribute == "final":
            # Write the final result to the output file
            with open(output_filename, 'w') as file:
                file.write(next_step)
            print(f"Scavenger hunt completed. Result saved to {output_filename}")
            return

        # Extract the next URL, element, and attribute from the attribute value
        try:
            next_url, next_element, next_attribute = next_step.split(',')
            url = urljoin(url, next_url.strip())  # Resolve relative URLs
            element = next_element.strip()
            attribute = next_attribute.strip()
        except ValueError:
            print(f"Error parsing the next step from '{next_step}'. Expected format: '<URL>,<tag>,<attribute>'")
            return

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 lab21.py <URL> <HTML element> <attribute> <output file>")
        sys.exit(1)

    start_url = sys.argv[1]
    start_element = sys.argv[2]
    start_attribute = sys.argv[3]
    output_file = sys.argv[4]

    scavenger_hunt(start_url, start_element, start_attribute, output_file)
