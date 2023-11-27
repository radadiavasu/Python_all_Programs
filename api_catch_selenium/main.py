from seleniumwire import webdriver
from seleniumwire.utils import decode as decode_vasu

import json

def show_request_urls(driver, target_url):
    driver.get(target_url)
    urls = []
    for request in driver.requests:
        urls.append({"Url": request.url})
    return urls

def show_response(driver, target_url):
    driver.get(target_url)
    resps = []
    for request in driver.requests:
        try:
            data = decode_vasu(
                request.response.body,
                request.response.headers.get("Content Encoding", "identity")
            )
            resp = json.loads(data.decode("utf-8"))
            resps.append(resp)
        except:
            pass
    return resps

def main():
    keywords = ["api", "v1"]
    driver = webdriver.Firefox(seleniumwire_options={"disable_encoding": True})
    target_url = "https://www.adidas.co.uk/terrex"
    
    request_urls = show_request_urls(driver, target_url)
    request_resps = show_response(driver, target_url)
    for url in request_urls:
        for kw in keywords:
            if kw in url['Url']:
                print(url)
    with open('urls.json', 'w') as f:
        json.dump(request_resps, f)
    driver.close()
    
    
    
if __name__ == '__main__':
    main()
    