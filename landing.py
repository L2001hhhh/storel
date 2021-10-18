from selenium import webdriver
import time

chromeDriver = webdriver.Chrome()
chromeDriver.get(r'http://8.129.91.152:8765/ ')
chromeDriver.maximize_window()
# 注册
chromeDriver.find_element_by_xpath('//*[@class="no-border special-color"]').click()
#手机号
chromeDriver.find_element_by_xpath('//*[@class="form-control reg-mobile phoneNum"]').send_keys("17952265888")
time.sleep(10)
# 输入图片验证码
B = chromeDriver.find_element_by_xpath('//*[@class="btn btn-success left reget-mobileCode"]').click()
time.sleep(2)
# 输入短信验证码
text = chromeDriver.find_element_by_xpath('//*[@class="layui-layer-content"]')
str = text.text
aaa = str[len(str)-4:]
chromeDriver.find_element_by_xpath('//*[@name="code"]').send_keys(aaa)

# 输入密码
chromeDriver.find_element_by_xpath('//*[@type="password"]').send_keys("qwer123456")
# # 勾选服务协议
chromeDriver.find_element_by_xpath('//*[@name="agree"]').click()
# # 下一步
chromeDriver.find_element_by_xpath('//*[@class="btn btn-special"]').click()
time.sleep(5)
# 分配蜂群
chromeDriver.find_element_by_xpath('/html/body/div[4]/div[3]/a[2]').click()
# a = chromeDriver.window_handles
# chromeDriver.switch_to.window(a[1])
time.sleep(5)

# 身份认证
chromeDriver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a/img').click()

chromeDriver.find_element_by_xpath("//*[@class='link-color fs-12 right realname-check']").click()


time.sleep(3)
# 姓名
chromeDriver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/div[1]/div/input").send_keys("张三")
# 身份证号
chromeDriver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/div[2]/div/input").send_keys("130425198708092057")
# 点击
chromeDriver.find_element_by_xpath("/html/body/div[3]/div[2]/div/form/div[3]/div/button").click()
