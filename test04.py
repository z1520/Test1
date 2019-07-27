# coding : utf-8

# 自动化测试实战之ActionChains模拟用户行为

# 需求：需要使用模拟鼠操作才能进行的情况，比如单机，双击，点击鼠标右键，拖拽

# 解决：selenium提供了一个类来处理这类事件
# selenium.webdriver.commom.action_chains import ActionChains(driver)

# 脚本
# from selenium.webdriver.common.action_chains import ActionChains

# 执行原理：
# 调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列中，当调用perform()方法时，队列中的事件会一次执行

# 支持链式或分布式写法
# ActionChains（driver）。click（ele）。perform（）

# 键盘和鼠标方法列表：
# perform() 执行链中所有操作
# click(on_element=None) 单击鼠标左键
# context_click(on_element-None) 点击鼠标右键
# double_click(on_element=None) 双击鼠标左键
# move_to_element(to_element) 鼠标移到某个元素
# ele.send_keys(keys_to_send) 发送某个词到当前焦点元素

#*****不常用*****
# click_and_hold(on_element_None) 点击鼠标左键不松开
# release(on_element=None) 在某个元素位置松开鼠标左键
# key_down(value,element=None) 松开某个键盘上的键
# key_up(valus,element-None) 松开某个键
# drag_and_drop(source,target) 拖拽到某个元素然后松开
# drag_and_drop_by_offset(source,xoffset,yoffset) 拖拽到某个坐标然后松开
# move_by_offset(xoffset,yoffset) 鼠标从当前位置移动到某个坐标
# move_to_element_with_offset(to_element,xoffset,yoffset) 移动到距某个元素（左上角坐标）多少距离的位置


# 鼠标事件实战之hover菜单栏弹出



# # coding : utf-8
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
#
# # 拿到driver
# driver = webdriver.Firefox()
#
# # 跳转网页
# driver.get("https://xdclass.net")
# driver.maximize_window()
#
# # 睡眠时间
# sleep(10)
#
# # # 定位鼠标移动到上面的元素
# # menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
# # ActionChains(driver).move_to_element(menu_ele).perform()
# #
# # # 选中子菜单
# # sub_menu_ele = driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(1)")
# # sleep(3)
#
# # sub_menu_ele.click()
#
# # 获取登陆框
# login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
#
# # 触发点击事件
# ActionChains(driver).click(login_ele).perform()
# sleep(5)
#
# # 去掉保存密码checkbox勾选
# login_box_ele = driver.find_element_by_css_selector(".login_btn > span:nth-child(1) > input:nth-child(1)")
# ActionChains(driver).click(login_box_ele).perform()

# # 查找输入框，输入账号密码，输入框需要提前清理
# driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
# driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("13636026394")
#
# driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
# driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("zql12345+")
#
# # 查找登陆按钮
# login_btn_ele = driver.find_element_by_css_selector(".btn")
#
# # 触发点击事件
# ActionChains(driver).click(login_btn_ele).perform()
# sleep(3)
#
# # 判断是否登陆成功,鼠标移动到上面，判断弹窗字符
# user_info_ele = driver.find_element_by_css_selector(".avatar_img")
# sleep(3)
#
# # 触发hover事件
# ActionChains(driver).move_to_element(user_info_ele).perform()
# sleep(5)
#
# # 获取用户名的元素
# user_name_ele = driver.find_element_by_css_selector(".username")
# print("***测试结果***")
# print(user_name_ele.text)
# name = user_name_ele.text
# # sleep(5)
#
# if name == u"不语":
#     print("登陆成功！")
# else:
#     print("登陆失败！")

# driver.quit()





# 自动化测试实战之网页等待时间

# 1.为什么需要等待时间----等待系统稳定
#    网页需要加载对应的资源文件，页面渲染，窗口处理等等

# 2.自动化测试常用的等待时间
#    强制等待：
#       from time import sleep
#       sleep(5)  # 强制等待5秒再执行下一步，缺点时不管资源是不是完成，都必须等待
#   隐性等待：
#       driver.implicitly_wait(10)  # 隐性等待，最长10秒
#       #设置一个最长的等待时间，如果再规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步，弊端说就是程序会一直等待整个页面加载完成，到浏览器标签栏那个圆圈不再转
#
#       注意：对driver起作用，所以只需要设置一次，不需要到处设置
#
#   显性等待：
#       WebDriverWait  需要配合
#       until和until not，程序每隔N秒检查一次，如果成功，则执行下一步，否则继续等待，直到超过设置的最长时间
#       from selenium.webdriver.support.wait import WebDriverWait
#
#       语法：WebDriver(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
#
#       from selenium.webdriver.commom.by impory By
#       from selenium.webdriver.support.ui import WebDriverWait
#       from selenium.webdriver.support import expected_conditions as EC
#
# 结论：隐性等待和显性等待可以同时使用，等待最长时间取两者之中的较大者

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 拿到driver
driver = webdriver.Firefox()
# driver.implicitly_wait(10)  # 隐性等待

# 跳转网页
driver.get("https://baidu.com")

try:
    # 显性等待
    ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    # driver.implicitly_wait(4)
    ele.send_keys("林俊杰")
    sleep(3)
    print("资源加载成功.")

    print(driver.title)

except:
    print("资源加载失败,发送报警邮件或者短信.")

finally:
    print("不管有没有成功，都打印，用于资源管理.")
# 退出浏览器
driver.quit()



