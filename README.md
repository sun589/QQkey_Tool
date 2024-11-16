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
[![联系我](https://img.shields.io/badge/%E8%81%94%E7%B3%BB%E6%88%91-goodluck1787@outlook.com-grey?labelColor=white&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA0UlEQVR4nO3UwWkCQRSH8R96E5ICBLEFIZAalBDwYgu2YAu2kBZyySFVBARbCKsWEMGbsrIwC0vY1cmqwcN+8GDY9/h/zOwwNNwTL1gjvbBWGJUJVlcIT0MlZYK8eSlpVU7e+ES/RnAX7zGCrHaYoR0R3MIU218ZlYJXfIf1Es8nwgf4CrMbTGIEGR3MsccBb3gszJb1H0pyKgU5T1gUbsY4VBK+LcLMuZyTjVY445/If/RnQU4PH6GydRW1BbE0gvpHdPPHbnQlSYLh+Y02/BdHOA2bqc6k+4oAAAAASUVORK5CYII=)](mailto:goodluck1787@outlook.com)
> QQ远程控号&盗号/生成木马/突破空间&邮箱&QQ群/扫码控号/QQkey直取/Clientkey直取/发说说……

可能是你见过唯一还在持续更新的QQKey工具箱:)  
<font size=5>我是尺寸</font>  
<details><summary>免责声明【必读】</summary>

### **本工具仅供学习和技术研究使用，不得用于任何非法行为，否则后果自负。**

**本工具的作者不对本工具的安全性、完整性、可靠性、有效性、正确性或适用性做任何明示或暗示的保证，也不对本工具的使用或滥用造成的任何直接或间接的损失、责任、索赔、要求或诉讼承担任何责任。**

**本工具的作者保留随时修改、更新、删除或终止本工具的权利，无需事先通知或承担任何义务。**

**本工具的使用者应遵守相关法律法规，尊重QQ的版权和隐私，不得侵犯QQ或其他第三方的合法权益，不得从事任何违法或不道德的行为。**

## **本工具的使用者在下载、安装、运行或使用本工具时，即表示已阅读并同意本免责声明。如有异议，请立即停止使用本工具，并删除所有相关文件。**

</details>  

***再次声明:本软件仅用于学习用途,请勿用于违法行为 后果自负!***  
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
![程序截图](https://github.com/user-attachments/assets/ae4742ab-3c7e-40c5-b9d1-5ee44e15cf5d)  
****
# 仓库访问数量(从2024-10-14计起)
![Visitor count](https://profile-counter.glitch.me/sun589-QQkey_Tool/count.svg)  
如果路过了不放给个star:))))))))))))))))))))))))))))))))))))))))))
****
# 制作不易,如果喜欢,请给作者打个Star,谢谢:)))))))))))  
[![Star History Chart](https://api.star-history.com/svg?repos=sun589/QQkey_Tool&type=Date)](https://star-history.com/#sun589/QQkey_Tool&Date)  
****
