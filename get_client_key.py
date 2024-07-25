import sys
from urlextract import URLExtract
import requests
import re
import json
import os
os.system("title QQ Clientkey 获取器")
print("[Info] 欢迎使用 QQ Clientkey 获取器!")
print("\033[31m[Warning] 请勿将本窗口任何信息透露给他人,否则后果自行承担!\033[0m")
print("[Tip] 在刚登录QQ时获取可能会出现如无法获取skey的情况,这时请重启工具获取!")
session = requests.session()
try:
    print("[Info] 正在获取pt_local_token...")
    login_htm = session.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?s_url=https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone")
    q_cookies = requests.utils.dict_from_cookiejar(login_htm.cookies)
    pt_local_token = q_cookies.get("pt_local_token")
    pt_login_sig = q_cookies.get("pt_login_sig")
    print(f"[+] pt_local_token={pt_local_token}\n[+] pt_local_sig={pt_login_sig}")
    params = {"callback":"ptui_getuins_CB",
              "r":"0.8987470931280881",
              "pt_local_tk":pt_local_token}
    cookies = {"pt_local_token":pt_local_token,
               "pt_login_sig":pt_login_sig}
    headers = {"Referer":"https://xui.ptlogin2.qq.com/",
               "Host":"localhost.ptlogin2.qq.com:4301",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
except Exception as e:
    print(f"[ERROR] 获取pt_local_token时发生错误,原因:{e}")
    input()
    sys.exit(0)
try:
    print("[Info] 正在获取本机登录QQ号..")
    get_uin = session.get("https://localhost.ptlogin2.qq.com:4301/pt_get_uins",params=params,cookies=cookies,headers=headers).text
    uin_list = re.findall(r'\[([^\[\]]*)\]', get_uin)[0]
    uin = json.loads(uin_list).get('uin')
    nickname = json.loads(uin_list).get('nickname')
    print(f"[+] uin={uin}\n[+] nickname={nickname}")
    clientkey_params = {"clientuin":uin,
                        "r":"0.14246048393632815",
                        "pt_local_tk":pt_local_token,
                        "callback":"__jp0"}
    print("[Info] 正在获取clientkey...")
    clientkey_get = session.get("https://localhost.ptlogin2.qq.com:4301/pt_get_st",cookies=cookies,headers=headers,params=clientkey_params)
    clientkey_cookies = requests.utils.dict_from_cookiejar(clientkey_get.cookies)
    clientkey = clientkey_cookies.get("clientkey")
    if not clientkey:
        print("\033[33m[Warning]未获取到clientkey,请尝试稍后重启工具获取!\033[0m")
    else:
        print(f"[+] clientkey={clientkey}")
except Exception as e:
    print(f"[ERROR] 获取clientkey发生错误,请检查是否开启QQ!")
    input()
    sys.exit(0)
try:
    print("[Info] 正在获取QQ空间&QQ邮箱登录地址&Skey...")
    qzone_params = {
        "u1":"https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone",
        "clientuin":uin,
        "pt_aid":"549000912",
        "keyindex":"19",
        "pt_local_tk":pt_local_token,
        "pt_3rd_aid":"0",
        "ptopt":"1",
        "style":"40",
        "daid":"5"
    }
    qzone_jump_cookies = {
        "clientkey":clientkey,
        "clientuin":uin,
        "pt_local_token":pt_local_token
    }
    headers = {"Referer": "https://xui.ptlogin2.qq.com/",
               "Host": "ssl.ptlogin2.qq.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
    qzone_url = session.get("https://ssl.ptlogin2.qq.com/jump",params=qzone_params,cookies=cookies,headers=headers)
    qzone_cookies = requests.utils.dict_from_cookiejar(qzone_url.cookies)
    qzone_skey = qzone_cookies.get("skey")
    extractor = URLExtract()
    qzone_url = extractor.find_urls(qzone_url.text)[0]
    pskey = session.get(qzone_url,allow_redirects=False)
    pskey_cookies = requests.utils.dict_from_cookiejar(pskey.cookies)
    qzone_pskey = pskey_cookies.get("p_skey")
    qzone_url = f"https://ssl.ptlogin2.qq.com/jump?ptlang=1033&clientuin={uin}&clientkey={clientkey}&u1=https://user.qzone.qq.com/{uin}/infocenter&keyindex=19"
    print(f"[+] qzone_skey={qzone_skey}")
    print(f"[+] qzone_pskey={qzone_pskey}")
    print(f"[+] qzone_url={qzone_url}")
    mail_params = {
        "u1":"https://graph.qq.com/oauth2.0/login_jump",
        "clientuin":uin,
        "pt_aid":"716027609",
        "keyindex":"19",
        "pt_local_tk":pt_local_token,
        "pt_3rd_aid":"102013353",
        "ptopt":"1",
        "style":"40",
        "daid":"383"
    }
    mail_cookies = {
        "clientkey":str(clientkey),
        "clientuin":str(uin),
        "pt_local_token":str(pt_local_token),
        "pt_login_sig":str(pt_login_sig)
    }
    mail_url = session.get("https://ssl.ptlogin2.qq.com/jump",params=mail_params,cookies=mail_cookies,headers=headers)
    mail_cookies = requests.utils.dict_from_cookiejar(mail_url.cookies)
    mail_url = extractor.find_urls(mail_url.text)[0]
    pskey = session.get(mail_url,allow_redirects=False)
    pskey_cookies = requests.utils.dict_from_cookiejar(pskey.cookies)
    mail_pskey = pskey_cookies.get("p_skey")
    mail_url = f"https://ssl.ptlogin2.qq.com/jump?ptlang=1033&clientuin={uin}&clientkey={clientkey}&u1=https://wx.mail.qq.com/list/readtemplate?name=login_page.html&keyindex=19"
    print(f"[+] mail_pskey={mail_pskey}")
    print(f"[+] mail_url={mail_url}")
except Exception as e:
    print(f"[ERROR] 获取QQ空间&QQ邮箱地址时出现错误,原因:{e}")
    input()
    sys.exit(0)
print("******************信息整理******************")
print(f"uin={uin}")
print(f"nickname={nickname}")
print(f"clientkey={clientkey}")
print(f"qzone_skey={qzone_skey}")
print(f"qzone_pskey={qzone_pskey}")
print(f"mail_pskey={mail_pskey}")
print(f"qzone_url={qzone_url}")
print(f"mail_url={mail_url}")
print("******************感谢使用******************")
while True:
    pass