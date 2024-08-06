import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://cricblog.net/#google_vignette"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract all text from the webpage
    text = soup.get_text()
    print("Text from the webpage:")
    print(text)
    
    # Extract all links (anchor tags) from the webpage
    links = soup.find_all('a')
    print("\nLinks from the webpage:")
    for link in links:
        href = link.get('href')
        text = link.text
        print(f"Link: {href}, Text: {text}")
    
    # Extract all images (img tags) from the webpage
    images = soup.find_all('img')
    print("\nImages from the webpage:")
    for img in images:
        src = img.get('src')
        alt = img.get('alt', 'No alt text provided')
        print(f"Image Source: {src}, Alt Text: {alt}")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
