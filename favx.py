import requests

# === 🔧 THÔNG TIN CẦN THAY THẾ ===
tweet_id = "1939872914129789015"  # ← ID tweet cần thả tim

cookie = (
    'guest_id_marketing=v1%3A175133298690740175; '
    'guest_id_ads=v1%3A175133298690740175; '
    'guest_id=v1%3A175133298690740175; '
    'personalization_id="v1_Gtjt6MG2rTwB+y7Olviacw=="; '
    'gt=1939857303072907604; '
    'kdt=piEVKzZmJLYuXFqwgayRBCGZN3KCEU2i9TcG94R6; '
    'auth_token=147f8e0c862256324bab5ca1dcea5748a0f30841; '
    'ct0=1395e728c8e2f68080912e043d918c63f85b31dbe2a58dd2532653a081e65b4fdfb2eba42d5dd6656e0a586c24d9ff3c866788a3bf07be65f7e5a34d2205304826a5bb2e9976b2d3119dc569b9226993; '
    'lang=en; '
    'twid=u%3D1939258265780809729; '
    'att=1-BIvE3SXwIB1XisdJfkCIGaTSp63BLMxFeHO5vI3h; '
    '__cf_bm=1uz.EOxxLTMdOmbktewdKoWokUVqrd_M5GYj8B1r8Ho-1751336699-1.0.1.1-Rh.3BJAMd.Br6twpyJGXag3q7NRYmh0OcOEISZajmkNsJgUtV8fbgCSfg2aXLZsN37z0bE1NCOo9ViRCfpvXL5rfu4fJABpN054IJh2dNiY'
)

# === 🔍 TỰ ĐỘNG LẤY ct0 (CSRF token) TỪ COOKIE ===
ct0 = cookie.split("ct0=")[1].split(";")[0]

# === 🛰️ GỬI REQUEST ===
url = "https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet"

headers = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "x-csrf-token": ct0,
    "x-twitter-auth-type": "OAuth2Session",
    "x-twitter-active-user": "yes",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Referer": "https://x.com/",
    "Origin": "https://x.com",
    "Cookie": cookie
}

payload = {
    "variables": {
        "tweet_id": tweet_id
    },
    "queryId": "lI07N6Otwv1PhnEgXILM7A"
}

response = requests.post(url, headers=headers, json=payload)

print("Status code:", response.status_code)
print("Response:", response.text)
