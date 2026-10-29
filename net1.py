import requests

sites = [
    "https://api.github.com",
    "https://www.baidu.com",
    "https://raw.githubusercontent.com",
]

for url in sites:
    try:
        r = requests.get(url, timeout=8)
        print(url, "→ 通了,状态码", r.status_code)
    except Exception as e:
        print(url, "→ 失败:", type(e).__name__)