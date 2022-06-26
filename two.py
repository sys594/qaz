from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入 ActionChains 类
import time




driver = webdriver.Chrome()
# "https://access-cn1.statestreet.com.cn/logon/LogonPoint/tmindex.html"
url='https://access-cn1.statestreet.com.cn/logon/LogonPoint/tmindex.html'
driver.get(url)

#隐式等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def xswait(address,t,frequency,method=By.ID):
    wait = WebDriverWait(driver,t,frequency)
    wait.until(EC.presence_of_element_located((method,address)),message="")

#隐式等待后操作：click,或者send key
# def click_sendkey(address,t,frequency,value,find=find_element_by_id,action=click,method=By.ID):
#     xswait(address,t,frequency,method=By.ID)
#     driver.find('address').action(value)

# 定位到要右击的元素
# right_click = driver.find_element_by_id("xx")
# time.sleep(2)
# 对定位到的元素执行鼠标右键操作
# ActionChains(driver).context_click(right_click).click(right_click).drag_and_drop("1","2").perform()
# sleep(2)
# username  id=login
xswait('login',10,0.5)
driver.find_element_by_id('login').send_keys('a848139')
# password passwd
xswait('passwd',10,0.5)
driver.find_element_by_id('passwd').send_keys('Hl594329936!!')
# domain id=domain  //*[@id="domain"]/option[2]
xswait('domain',10,0.5)
driver.find_element_by_id('domain').click()
# sleep(1)
xswait('//*[@id="domain"]/option[2]',10,0.5,method=By.XPATH)
driver.find_element_by_xpath('//*[@id="domain"]/option[2]').click()
# securlid  passwd1
xswait('passwd1',10,0.5)
driver.find_element_by_id('passwd1').send_keys('594329')