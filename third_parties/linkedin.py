import os
from dotenv import load_dotenv
import requests

load_dotenv()

def scrape_linkedin_profile(url : str, mode :bool = False):
    """
    scrape information from linkedin profiles,
    """
    if mode:
        url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(url,timeout=10,)

    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params={
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedinUrl" :url,
        }
        response = requests.get(
            api_endpoint, params= params, timeout = 10,
        )

    data = response.json().get("person")

    data = { k:v for k,v in data.items() if v not in ([],"","",None) and k not in ["certifications"]}
    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(url = "https://in.linkedin.com/in/contact-nitish-kumar", mode = True)
    )