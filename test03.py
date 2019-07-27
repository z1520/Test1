# -*- coding: utf-8
# from selenium import webdriver
# # 拿到driver
# driver = webdriver.Firefox()
#
# # 跳转网页
# driver.get("http://www.baidu.com")
#
# print(driver.title)

# # 选中输入框，输入关键词
# driver.find_element_by_id("kw").send_keys("林俊杰")
# # 选中按钮，触发事件
# driver.find_element_by_id("su").click()

# 定位元素的八种方法，一定要唯一
# id name class_name



# from selenium import webdriver
# # 拿到driver
# driver = webdriver.Firefox()
#
# # 跳转网页
# driver.get("http://www.baidu.com")
#
# print(driver.title)
#
# # 选中输入框，输入关键词
# driver.find_element_by_name("wd").send_keys("林俊杰  邓紫棋")
# # 选中按钮，触发事件
# driver.find_element_by_id("su").click()

# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# print(driver.title)
# driver.find_element_by_class_name("s_ipt").send_keys("许嵩")
# driver.find_element_by_id('su').click()

"""
clear()  清空
send_keys()  输入
back()  后退页面
maximize_window()  窗口最大化
click()  点击事件
sunmit()  提交表单

"""



""""""
# # tag name  通过标签去定位（div）
# # find_element_by_link_text
#
# from selenium import webdriver
# import selenium.webdriver.support.ui as ui
# from time import sleep
#
# driver = webdriver.Firefox()
#
# #跳转网页
# driver_item = webdriver.Firefox()
# wait = ui.WebDriverWait(driver_item,10)
# driver.get("https://xdclass.net")
# wait.until(lambda driver: driver.find_element_by_partial_link_text("视频学习").click())
# print(driver.title)

# # 睡眠时间3s
# sleep(3)
#
# wait = ui.webdriverwait(driver_item,10)
# driver.find_element_by_partial_link_text("视频学习").click()

""""""


# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.get("https://www.xdclass.net")
# print(driver.title)
# sleep(3)
# # driver.find_element_by_partial_link_text("视频学习").click()
# # driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)")
#
# # 路径：通过firebug的拷贝css路径
# # 审查元素--右键--复制--css选择器
#
# # Xpath语法：
# # 注意： // 全部的意思，即全文扫描   /相邻的意思   *是所有元素   ..是元素的父节点   .是当前节点
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/ul/li[2]").click()
# print(driver.title)


# 8种选择器注意问题：如果定位元素报错，原因如下
# 1.根据定位取不到
# 2.多个元素根据下标超出范围，没有0，从1开始
# 解决办法：换其他方式定位元素
