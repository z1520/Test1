# 2019/8/2

# 什么是单元测试unittest
#    简介：unittest框架和使用
# 1.用import语句引入unittest模块
#
# 2.测试的类都继承于TestCase类
#
# 3.setUP() 测试前的初始化工作； tearDown 测试后的清除工作 （在每个测试方法运行时被调用）
#
# 注意：
#   1.所有类中的入参为self，定义方法的变量也要"self.变量"
#   2.定义测试用例，以"test" 开头的命名方法，方法的入参为self
#   3.unittest.main()方法会搜索该模块下所有以test开头的测试用例，并自动执行他们
#   4.自己写的.py文件不能用，用unittest.py命名，不然会找不到TestCase
#
#   成功时输出 ， 失败是 F
#

# -*- coding:UTF-8 -*-
# import unittest
#
# class UserTestCase(unittest.TestCase):
#     def setUp(self):
#         print("==setUP==")
#         self.name = "小D课堂"
#         self.age = 24
#
#     def tearDown(self):
#         print("==tearDown")
#
#
#     def test_name(self):
#         print("调用test_name")
#         # 断言是否相同
#         self.assertEqual(self.name,"小D课堂",msg="名字不对")
#
#
#     def test_isupper(self):
#         print("调用test_isupper")
#         # 断言是否为 true，msg是断言错误的提示信息
#         self.assertFalse('xdclass'.isupper(),msg="不是大写")
#
#
#     def test_age(self):
#         print("调用test_age")
#         self.assertEqual(self.age,24)
#
#
# if __name__ == '__main__':
#     unittest.main()


# 测试套件testSuite介绍
#   简介：TestSuite的基本介绍和使用场景
#   需求：
#       1.利用unittest执行流程测试而非单元测试
#       2.控制unittest的执行顺序
#
#   1.nuittest.TestSuite() 类来表示一个测试用例集
#       1.用来确定测试用例的顺序，哪个先执行哪个后执行
#       2.如果一个class中有四个 test开头的方法，则加载到suite中时则有四个测试用例
#       3.有TestLoder加载TestCase到TestSuite
#       4.verbosity参数可以控制执行结果输出，0 简单报告，1 时一般报告，2 是详细报告    默认 1 会在每个成功的用例前面有个“.”，每个失败的用例前面有个“F”
#
#   2.TextTestRunner()  文本测试用例运行器
#
#   3.run() 方法是运行测试套件的测试用例，入参为suite测试套件


# -*- coding:UTF-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class XdclassTestCase(unittest.TestCase):
    def setUp(self):
        self.age = 24
        self.name = "小D课堂"
        print(" setUP   method====")

    def tearDown(self):
        print(" tearDown method====")
        # 断言是否相同
        self.assertEqual("FOO".upper(),"FOO")

    def test_one(self):
        u"""这是登陆窗口"""
        print(" test_one 二当家小D 来了")
        # 断言是否相同
        self.assertEqual(self.name,"小D课堂",msg="名字不对")

    def test_two(self):
        u"""这是首页面"""
        print(" test_two 前端 来了")


    def test_three(self):
        u"""测试方法3"""
        print(" test_three 后端 来了")
        self.assertEqual(self.age,24)

    def test_four(self):
        u"""这是网址"""
        print(" test_four 小D课堂官网上线啦  https：//xdclass.net")
        self.assertEqual(self.age,24)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(XdclassTestCase("test_one"))
    suite.addTest(XdclassTestCase("test_four"))
    suite.addTest(XdclassTestCase("test_three"))
    suite.addTest(XdclassTestCase("test_two"))

    # verbosity参数可以控制执行结果的输出
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    file_prefix = time.strftime("%Y-%m-%d %H_%m_%S",time.localtime())
    print(file_prefix)
    fp = open("./"+file_prefix+"_result.html","wb")
    runner = HTMLTestRunner(stream=fp,title=u"小D课堂 测试报告",description=u"测试用例执行情况")
    runner.run(suite)
    fp.close()



# unittest中HTML测试报告优化
#    简介：为每一个测试用例添加说明，那么将会是报告更加通俗易懂，工作中汇报数据的技巧
#   u"""test_one方法"""