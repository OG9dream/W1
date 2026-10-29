import requests

url = "https://api.github.com/users/OG9dream"
r=requests.get(url,timeout=8)

print("状态码:",r.status_code)
print("r是什么:",type(r))
print("--- 服务器返回的原文(前 300 个字符)---")
print(r.text[:300])
