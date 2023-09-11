"""该脚本意在帮助同学们更好的抢课，请勿使用此脚本进行违纪违法行为，出现后果作者概不负责
   请选课前2-5min运行该脚本"""

from datetime import timedelta
from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建一个特定时间
specific_time = datetime(2023, 9, 11, 20, 26, 59, 400000)  # 设置选课时间，提前600000微秒
formatted_time = specific_time.strftime("%Y-%m-%d %H:%M:%S.%f")
print("设置时间:",formatted_time)
minimum_time_difference = timedelta(seconds=10)  # 若距离选课时间10s以上，程序每5s校验一下时间，若10s以内，每0.1s校验以下时间

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'd:\Google\chromedriver.exe'))
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://icourses.jlu.edu.cn/')
time.sleep(15)#等待打开选课网站

input_element = wd.find_element(By.XPATH,'//*[@id="loginNameDiv"]/div/input').send_keys("账号")#此处输入账号，也可不填，在登录页面手动输入
input_element = wd.find_element(By.XPATH,'//*[@id="loginPwdDiv"]/div/input').send_keys("密码")#此处输入密码，也可不填，在登录页面手动输入

time.sleep(30)#等待输入账号，密码，验证码，进入收藏界面

current_time = datetime.now()# 获取当前时间
print("当前时间:",current_time)

# 比较时间
while True:
    current_time = datetime.now()
    time_difference = specific_time - current_time
    if current_time >= specific_time:
        print("当前时间达到或超过特定时间，跳出循环")
        print(current_time)
        break
    elif time_difference >= minimum_time_difference:
        print("当前时间还早于特定时间前10秒，继续循环")
        print(current_time)
        time.sleep(5)  # 暂停5秒后继续循环
    else:
        print("当前时间还未达到特定时间，继续循环")
        print(current_time)
        time.sleep(0.1)  # 暂停0.1秒后继续循环

# 记录开始刷新的时间
start_time = time.time()
wd.refresh()#刷新出新数据，才能抢课，否则即使时间到了，还是会显示选课时间未到

# 等待页面刷新完成
wait = WebDriverWait(wd, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="xsxkapp"]/div/div[3]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/div/a[1]/span')))


for i in range(1, 9):#后面数字9可改动，具体取决于你收藏夹里的课程＋1，该数字不要超过11
    button_element = wd.find_element(By.XPATH, f'//*[@id="xsxkapp"]/div/div[3]/div/div/div/div[3]/table/tbody/tr[{i}]/td[9]/div/a[1]/span').click()# 模拟点击选课按钮
    button_element2 = wd.find_element(By.CSS_SELECTOR, 'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span').click()#模拟点击二次确认
    time.sleep(0.03)#歇30ms，让浏览器反应以下

end_time2 = time.time()
select_time = end_time2 - start_time
print(f"抢课总用时：{select_time:.6f} 秒")