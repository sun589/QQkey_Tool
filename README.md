****
# QQkey_Tool  
![Author-sun589](https://img.shields.io/badge/Author-sun589-yellow.svg)
![License-MIT](https://img.shields.io/badge/license-MIT-green)
![Language-python](https://img.shields.io/badge/Language-python-blue?logo=python)
![Github stars](https://img.shields.io/github/stars/sun589/QQkey_Tool?style=flat&logo=github&color=46cdcf)  
![GitHub Release](https://img.shields.io/github/v/release/sun589/QQkey_Tool?display_name=tag&style=flat&label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC&logo=github)
![Github downloads](https://img.shields.io/github/downloads/sun589/QQkey_Tool/total?style=flat&color=red&label=%E6%80%BB%E4%B8%8B%E8%BD%BD%E9%87%8F&logo=github)
![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/sun589/QQkey_Tool/latest/total?style=flat&label=%E6%9C%80%E6%96%B0%E4%B8%8B%E8%BD%BD%E9%87%8F&color=orange&logo=github)  
> QQ远程控号&盗号/生成木马/突破空间&邮箱&QQ群/扫码控号/QQkey直取/Clientkey直取/发说说……

可能是你见过唯一还在持续更新的QQKey工具箱:)  
***声明:本软件仅用于学习用途,请勿用于违法行为 后果自负!***  
****
#  使用说明
  下载[Release](https://github.com/sun589/QQkey_Tool/releases)里最新的版本打开QQKey_Tool.exe食用  
  or  
  下载[源代码](https://github.com/sun589/QQkey_Tool/)运行
****
#  常见问题 Q&A
## Q:如何预防盗号病毒?
### A:详见 [预防盗号木马的方法](#预防盗号木马的方法)  

## Q:已经被对方获取QQKey控号了怎么办?  
A:请第一时间打开QQ[找回密码](https://accounts.qq.com/find/password)界面进行更改密码,由于tx对账号安全所顾虑在更改完后将立刻将此账号所登录的所有业务立即下线,即QQKey也将随同失效  
  
## Q:可以获取密码吗?  
A:So actually...此工具只能获取QQ的clientkey以及各种信息,不过可以通过clientkey突破空间与邮箱,也算间接获取密码了  

## Q:为什么我打不开?  
A:检查你的系统是否为32位,本工具仅支持64位系统,如果你是32位的话建议直接换一个64位系统(毕竟目前大部分软件也仅支持64位)
****
# 预防盗号木马的方法
## 关于shellcode注入获取的clientkey
这种的请自行到网上搜索qqkey预防获取工具,本工具通过网页快捷登录协议获取clientkey  
## 关于使用网页快捷登录获取的clientkey(本工具的原理)
***若觉得麻烦/不会操作可使用QQKey_Tool的3.2或者以上版本的防QQKey木马器进行一键修复/恢复**  
找到`C:\Windows\System32\drivers\etc\hosts`文件,打开它,换行后添加以下内容:  
```
0.0.0.0 localhost.ptlogin2.qq.com
```
注意:添加该行代码后请到cmd里执行`ipconfig /flushdns`以立即生效,  
在生效后虽然防住了盗号病毒但也不能使用登录页面的快捷登录了  
****
# 程序截图
![程序截图](https://github.com/user-attachments/assets/61bf4c50-a5b9-4ffd-bff1-7f13af45173a)
****
# 仓库访问数量(从2024-10-14计起)
![Visitor count](https://profile-counter.glitch.me/sun589-QQkey_Tool/count.svg)  
如果路过了不放给个star:))))))))))))))))))))))))))))))))))))))))))
****
# 制作不易,如果喜欢,请给作者打个Star,谢谢:)))))))))))  
[![Star History Chart](https://api.star-history.com/svg?repos=sun589/QQkey_Tool&type=Date)](https://star-history.com/#sun589/QQkey_Tool&Date)  
****
