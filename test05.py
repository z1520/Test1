# 2019/7/29
# coding : utf-8

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
#
# # 拿到driver
# driver = webdriver.Firefox()
#
# # 跳转网页
# driver.get("file:///C:/Users/%E9%83%91%E5%BC%BA%E6%9E%97/Desktop/demo01.html")
#
# print(driver.title)
#
# print("默认选中male，3s后选中female")
#
# # 睡眠时间3s
# sleep(3)
#
# driver.find_element_by_id("female").click()


# 自动化测试页面之常见弹窗处理
#   简介：讲解使selenium处理页面弹窗，alert和confirm
#   弹窗常用方法（需要先切换窗口 switch_to_alert()）
#       accept()  表示接受
#       dismiss()  表示取消

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
#
# # 拿到driver
# driver = webdriver.Firefox()
#
# # 跳转网页
# driver.get("file:///C:/Users/%E9%83%91%E5%BC%BA%E6%9E%97/Desktop/demo_alert.html")
#
# print(driver.title)
#
# # 睡眠时间3s
# sleep(3)
#
# driver.find_element_by_id("alert").click()
#
# # 切换到弹窗
# win = driver.switch_to_alert()
# sleep(2)
# win.accept()
#
# sleep(3)
# driver.find_element_by_id("confirm").click()
# # 切换到弹窗
# comfirm_ele = driver.switch_to_alert()
# sleep(2)
# comfirm_ele.dismiss()


# 自动化测试之验证码常见解决方案
#    1.破解验证码
#       OCR识别： tesseract-acr
#       AI机器学习
#    2.绕过
#       让开发人员临时关闭验证码
#       提供一个万能的验证码（安全性需要保密，一般在开发测试环境使用）
#       使用cookie（登陆主要是为了拿cookie，获取登陆凭证）

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# # 拿到driver
# driver = webdriver.Firefox()
#
# # 跳转到页面
# driver.get("https://xdclass.net")
# driver.maximize_window()
#
# print(driver.title)
#
# #  睡眠时间
# sleep(3)
#
# driver.add_cookie({"name":"name","value":"zz"})
# driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMjEuanBlZyIsImlkIjoxMTcwOCwibmFtZSI6IuS4jeivrSIsImlhdCI6MTU2NDU3NjY2OCwiZXhwIjoxNTY1MTgxNDY4fQ.2ikhDGzE9OmJly3rTU6ylzx-8eJRggUgCOz3TWVje0w"})
#
# video_ele = driver.find_element_by_css_selector(".l_content > a:nth-child(3) > div:nth-child(1) > img:nth-child(2)")
# video_ele.click()
# sleep(3)
#
# # 点击购买
#
# driver.switch_to.window(driver.window_handles[1])
#
# buy_btn_ele = driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)")
# buy_btn_ele.click()
# sleep(3)
# print("进入下单页面")
# #
# # btn_ele = driver.find_element_by_css_selector(".tags > a:nth-child(2)")
# # btn_ele.click()


# 自动化测试错误截图
#    讲解使用webdriver自动截图
#      driver.get_screenshot_as_file("./error_png.png")


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 拿到driver
driver = webdriver.Firefox()
# 跳转网页
driver.get("https://xdclass.net")
driver.maximize_window()
print(driver.title)
# 睡眠3秒
sleep(3)

# # 查找登陆框
# login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
#
# # 触发事件
# ActionChains(driver).click(login_ele).perform()
# sleep(5)
#
# # 捕捉抓不到元素异常
# try:
#     driver.find_element_by_id("shell").click()
# except:
#     driver.get_screenshot_as_file("./error0.png")



# login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
# ActionChains(driver).click(login_ele).perform()
# sleep(5)
# driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
# driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("13636026395")
#
# driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
# driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("***12345*")
#
# login_btn_ele = driver.find_element_by_css_selector(".btn")
# ActionChains(driver).click(login_btn_ele).perform()
# sleep(5)
#
# try:
#
#     driver.find_element_by_css_selector(".loginin > span:nth-child(4) > a:nth-child(1)").click()
#
# except:
#     driver.get_screenshot_as_file("./error1.png")