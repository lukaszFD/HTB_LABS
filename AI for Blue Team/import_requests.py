import web_scraper

resp = requests.get('http://httpbin.org/ip')
print(resp.content.decode())
