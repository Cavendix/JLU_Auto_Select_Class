"""本脚本为选课捡漏脚本，原理为不断刷新抢课系统，一旦有其他人退课就可以立即选上
   截至2023.9.11，该脚本无被系统屏蔽风险
   各位同学请勿在选课系统已经崩溃时使用此脚本，否则会事与愿违
   请勿使用该脚本恶意选课，造成后果作者概不负责"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\Google\chromedriver.exe'))
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://icourses.jlu.edu.cn/')
time.sleep(15)#等待打开选课网站

input_element = wd.find_element(By.XPATH,'//*[@id="loginNameDiv"]/div/input').send_keys("账号")#此处输入账号，也可不填，在登录页面手动输入
input_element = wd.find_element(By.XPATH,'//*[@id="loginPwdDiv"]/div/input').send_keys("密码")#此处输入密码，也可不填，在登录页面手动输入

time.sleep(30)#等待输入账号，密码，验证码，进入收藏界面

while(True):
    n = 0
    time.sleep(20)#程序休息20S，防止崩溃

    while(n<1000):#连续刷新超过1300次程序有崩溃可能，所以需要休息20s

        wd.refresh()
        # 等待页面刷新完成
        wait = WebDriverWait(wd, 100)#如果选课界面100s都没有刷新出来，程序自动结束
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="xsxkapp"]/div/div[3]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/div/a[1]/span')))

        for i in range(1,9):
            button_element = wd.find_element(By.XPATH, f'//*[@id="xsxkapp"]/div/div[3]/div/div/div/div[3]/table/tbody/tr[{i}]/td[9]/div/a[1]/span').click()# 模拟点击选课按钮
            button_element2 = wd.find_element(By.CSS_SELECTOR,'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span').click()#模拟点击二次确认
            time.sleep(0.03)

        n=n+1
        print(n)#展示程序运行状态