import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor

def simulate_download(link):
    print(f"Downloading {link}...")
    time.sleep(3)  # Simulating download delay
    print(f"Completed {link}")


def main(url):
    print(f"Fetching {url}...")
    time.sleep(2)  # Simulating fetching delay
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [ a['href'] for a in soup.find_all('a', href=True)]
        print(f"Found {len(links)} links.")

        with ThreadPoolExecutor() as executor:
            executor.map(simulate_download, links)
            
if __name__ == "__main__":
    main("https://www.covasant.com")