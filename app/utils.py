import requests
import re
from bs4 import BeautifulSoup


def calculate_linkedin_followers():

    linkedin_url = "https://in.linkedin.com/in/afaque-umer"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    response = requests.get(linkedin_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    linkedin_profile_content = soup.find(
        "div", class_="profile-info-subheader"
    ).get_text(strip=True)

    linkedin_match = re.search(
        r"(\d+(?:\.\d+)?K?) followers", linkedin_profile_content, re.IGNORECASE
    )
    linkedin_followers = linkedin_match.groups()[0]
    return linkedin_followers


def calculate_medium_followers():
    url = "https://afaqueumer.medium.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    medium_soup = BeautifulSoup(response.content, "html.parser")
    medium_profile_content = medium_soup.find(class_="bf b ge gh ds").get_text(
        strip=True
    )
    medium_match = re.search(
        r"(\d+(?:\.\d+)?K?) followers", medium_profile_content, re.IGNORECASE
    )
    medium_followers = medium_match.groups()[0]
    return medium_followers
