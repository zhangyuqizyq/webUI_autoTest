import unittest
import HTMLTestRunner
import os
from testsuits.test_discuz01 import Discuz01Test
from testsuits.test_discuz02 import Discuz02Test
from testsuits.test_discuz03 import Discuz03Test
from testsuits.test_discuz04 import Discuz04Test

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Discuz01Test))
suite.addTest(unittest.makeSuite(Discuz02Test))
suite.addTest(unittest.makeSuite(Discuz03Test))
suite.addTest(unittest.makeSuite(Discuz04Test))

if __name__ == '__main__':
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="论坛单元测试报告",description="用例执行情况")
    runner.run(suite)
