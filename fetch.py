import json
import requests

# ============ ① 配置区 ============
USERNAME = "OG9dream"
DATA_FILE = "data.json"


# ============ ② 取数据(带防弹衣)============
def get_user(username):
    url = "https://api.github.com/users/" + username
    try:
        r = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print("网络出问题了:", type(e).__name__)
        return None

    if r.status_code == 404:
        print("没有这个用户:", username)
        return None
    if r.status_code != 200:
        print("请求失败,状态码:", r.status_code)
        return None

    return r.json()


def get_repos(username):
    url = "https://api.github.com/users/" + username + "/repos"
    try:
        r = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print("网络出问题了:", type(e).__name__)
        return None

    if r.status_code != 200:
        print("请求失败,状态码:", r.status_code)
        return None

    return r.json()


# ============ ③ 展示 ============
def show_report(user, repos):
    print("=" * 44)
    print("GitHub 用户报告:", user["login"])
    print("=" * 44)
    print("公开仓库数:", user["public_repos"])
    print("粉丝数:", user["followers"])
    print("注册时间:", user["created_at"][:10])
    print()
    print("--- 仓库清单 ---")
    for i, repo in enumerate(repos, 1):
        lang = repo.get("language")
        if lang is None:
            lang = "未标注"
        print(i, repo["name"], "| 星标", repo["stargazers_count"], "| 语言", lang)


# ============ ④ 存盘 ============
def save_data(user, repos):
    data = {"user": user, "repos": repos}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("已保存到", DATA_FILE)


# ============ ⑤ 组装 ============
def main():
    user = get_user(USERNAME)
    if user is None:
        return

    repos = get_repos(USERNAME)
    if repos is None:
        return

    show_report(user, repos)
    save_data(user, repos)


main()