import requests
# 获取短信验证码
url = 'https://api-test.weifengqi18.com/wuneng-platform-web/platform/user/sendcaptchacode'
data = {
    'mobile': '17682313802'
    }
headers = {
            'host': 'api-test.weifengqi18.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Origin': 'https://www-test.weifengqi18.com',
            'Referer': 'https://www-test.weifengqi18.com/',
            'Accept-Encoding': 'gzip, deflate, br'
        }

session = requests.session()
res = session.post(url, data, headers=headers)
res_data = eval(res.text)
code = res_data['data']['captcha']  # 短信验证码


#  登录
login_url = 'https://api-test.weifengqi18.com/wuneng-platform-web/platform/user/loginByCaptcha'
login_data = {
    'mobile': '17682313802',
    'captcha': code + 20
}
login_header = {
            'host': 'api-test.weifengqi18.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Origin': 'https://www-test.weifengqi18.com',
            'Referer': 'https://www-test.weifengqi18.com/',
            'Accept-Encoding': 'gzip, deflate, br'
        }

re = session.post(login_url, login_data, headers=login_header)
res_data = eval(re.text)['data']
# print(res_data)
ticketid = res_data['ticketid']
key = res_data['login-secret-key']
# print(ticketid, key)


# 用户管理
user_url = 'https://api-test.weifengqi18.com/wuneng-platform-web/platform/user/list'
user_data = {
                'currentPage': 1,
                'showCount': 10,
                'user_name': '',
                'mobile': '',
                'state': '',
}
user_header = {
            'host': 'api-test.weifengqi18.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'Origin': 'https://www-test.weifengqi18.com',
            'Referer': 'https://www-test.weifengqi18.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'PWEB-TICKETID': ticketid,
            'pweb-login-secret-key': key
        }


res = session.post(user_url, user_data, headers=user_header)
print(res.json())