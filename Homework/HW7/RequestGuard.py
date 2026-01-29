import requests
import re
from urllib.parse import urlparse

class RequestGuard:
    def __init__(self, url):
        """
        Initializes the RequestGuard object.
        Strips the domain and parses robots.txt to determine forbidden paths.
        """
        parsed_url = urlparse(url)
        self.domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
        self.forbidden = self.parse_robots()

    def parse_robots(self):
        """
        Parses the robots.txt file of the domain and returns a list of disallowed paths.
        """
        robots_url = f"{self.domain}/robots.txt"
        try:
            response = requests.get(robots_url)
            if response.status_code == 200:
                disallowed_paths = []
                lines = response.text.splitlines()
                for line in lines:
                    match = re.match(r"Disallow: (.*)", line)
                    if match:
                        disallowed_paths.append(match.group(1).strip())
                return disallowed_paths
            else:
                return []
        except requests.RequestException:
            return []

    def can_follow_link(self, url):
        """
        Checks if a given URL can be followed based on the domain and forbidden paths.
        """
        parsed_url = urlparse(url)
        url_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # Check if the domain matches
        if url_domain != self.domain:
            return False

        # Check if the path matches any forbidden paths
        for path in self.forbidden:
            if parsed_url.path.startswith(path):
                return False

        return True

    def make_get_request(self, url, use_stream=False):
        """
        Makes a get request if the URL is allowed. If not, returns None.
        """
        if self.can_follow_link(url):
            return requests.get(url, stream=use_stream)
        return None

# Main section for testing (optional)
if __name__ == "__main__":
    # Example usage and test cases
    guard = RequestGuard("https://cs111.byu.edu")

    # Test parse_robots()
    print("Forbidden paths:", guard.forbidden)

    # Test can_follow_link()
    print(guard.can_follow_link("https://cs111.byu.edu/staff"))  # Example, should return True
    print(guard.can_follow_link("https://cs111.byu.edu/data"))   # Example, based on robots.txt

    # Test make_get_request()
    response = guard.make_get_request("https://cs111.byu.edu/staff")
    if response:
        print(response.status_code)
    else:
        print("Request not allowed")
