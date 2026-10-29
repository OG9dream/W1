import requests

# ===== 1. 状态码:存在的用户 vs 不存在的用户 =====
ok = requests.get("https://api.github.com/users/OG9dream", timeout=10)
print("存在的用户 →", ok.status_code)

no = requests.get("https://api.github.com/users/this-user-does-not-exist-xyz123", timeout=10)
print("不存在的用户 →", no.status_code)

# ===== 2. .text 和 .json() 的区别 =====
print("r.text 的类型:", type(ok.text))
data = ok.json()
print("r.json() 的类型:", type(data))
print("login 字段:", data["login"])
print("公开仓库数:", data["public_repos"])

# ===== 3. 响应头 & 编码 =====
print("Content-Type:", ok.headers["Content-Type"])
print("编码:", ok.encoding)
print("404 时它其实回了我:", no.json())