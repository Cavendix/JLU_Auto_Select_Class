吉林大学半自动选课脚本（验证码不会解决）  
本代码分别为两部分，auto_selectClass_1.0为抢课脚本，pick_up为捡漏脚本（捡别人推掉的课）  

利用py中selenium库，编译环境py3.9，使用Google浏览器  

调试好后，请在选课前2-5min运行该脚本

代码多注释，帮助你更好使用，一定要仔细阅读

浏览器界面打开可能是小窗，一定要立即变成全屏，否则程序会崩溃

下面开启教程：（下载地址不要有中文）  
1.python的安装及pycharm的安装和编译环境的添加，可以看这个教程  https://blog.csdn.net/h123456789999999/article/details/112753496  
2.安装google浏览器（务必使用默认地址，否则会有奇奇怪怪的报错）及google浏览器驱动（选一个你能记住的地址，一会有用），地址分别为：  
https://www.google.cn/intl/zh-CN/chrome/ 和 https://googlechromelabs.github.io/chrome-for-testing/（务必版本一致）  
3.打开pycharm创建第一个项目，将文件夹中main.py的内容复制粘贴到你的项目，编译器自动生成的请全部删除  

![image](https://github.com/Cavendix/JLU_Auto_Select_Class/assets/103408407/8815a424-44df-42e9-82c2-dd2977b80396)  

4.如图所示，光标放在selenium上，点击安装软件包selenium即可安装，如失败可以在命令提示符中输入  
pip install selenium -i https://pypi.douban.com/simple/或者多试几次（网络问题）   
5.运行脚本，手动输入验证码，使电脑显示收藏页面，等待即可  （提前将要选且难抢的课放入收藏夹，越难选放在越上面）  

![image](https://github.com/Cavendix/JLU_Auto_Select_Class/assets/103408407/5278921a-0c61-499f-b538-62f64c490ad9)  




