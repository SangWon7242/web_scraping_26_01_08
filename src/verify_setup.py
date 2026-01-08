import requests # 웹사이트에 요청을 보내고 응답을 받는 라이브러리

# 1. requests : 원하는 웹사이트에 요청
try:
  response = requests.get("https://www.naver.com", timeout=5)
  print(f"1. Requests: SUCCESS (Status Code: {response.status_code})")
except Exception as e:
  print(f"1. Requests: FAILED ({e})")

'''
# 2. BeautifulSoup & lxml Test
html_doc = "<html><body><h1>Hello, Scraper!</h1></body></html>"
try:
  soup = BeautifulSoup(html_doc, "lxml")
  h1_text = soup.select_one("h1").text
  if h1_text == "Hello, Scraper!":
    print("2. BeautifulSoup & lxml: SUCCESS")
  else:
    print("2. BeautifulSoup & lxml: FAILED (Wrong text)")
except Exception as e:
  print(f"2. BeautifulSoup & lxml: FAILED ({e})")

# 3. Pandas Test
data = {"Name": ["Test"], "Value": [100]}
try:
  df = pd.DataFrame(data)
    if not df.empty:
      print("3. Pandas: SUCCESS")
    else:
      print("3. Pandas: FAILED (Empty DataFrame)")
except Exception as e:
    print(f"3. Pandas: FAILED ({e})")

print("-----------------------------------------")
'''