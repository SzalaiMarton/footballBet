import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.football-data.co.uk/englandm.php"

def getData() -> bool:
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    premLeague = soup.find('a', string = ["Premier League"])
    print(premLeague["href"])
    fileUrl = f"https://www.football-data.co.uk/{premLeague["href"]}"
    fileName = os.path.basename(premLeague['href'])
    return download_file(fileUrl, fileName)

def download_file(url, fileName) -> bool:
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        return False

    with open(fileName, 'w') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    print(f"Downloaded: {fileName}")
    return True

getData()