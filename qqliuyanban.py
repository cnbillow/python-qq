# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:24:27 2020

@author: lgz
"""

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

def work(browser):

    qq=1534645821
    browser.get('https://user.qzone.qq.com/{}/infocenter?via=toolbar'.format(qq))
    #手机扫码登陆
    time.sleep(5)
    
    for page in range(2):
        #执行JaveScript隐藏网页上边栏
        js = "document.getElementsByClassName('top-fix-bar')[0].style.display='none'"
        browser.execute_script(js)
        time.sleep(1)
        
        #进入留言板
        browser.find_element_by_link_text('留言板').click()
        time.sleep(1)
        
        #切换iframe
        browser.switch_to.frame('tgb')
        time.sleep(1)
        
        #点击批量管理
        mouse = browser.find_element_by_id("btnToSet")
        ActionChains(browser).move_to_element(mouse).perform()
        browser.find_element_by_link_text("批量管理").click()
        time.sleep(1)
        
        #选中复选框
        target = browser.find_element_by_id("chkSelectAll") #全选
        #target = browser.find_element_by_xpath("//input[@name='batchItem' and @value='1000050005']") #选某一条
        browser.execute_script("arguments[0].scrollIntoView();", target) #滚动网页到可见区域
        time.sleep(1)
        target.click()
        time.sleep(1)
        
        #点击"删除选中的"，会弹出对话框
        browser.find_element_by_id('btnDeleteBatchBottom').click()
        time.sleep(1)
        
        browser.switch_to.parent_frame()
        
        #点击确定
        browser.find_element_by_id("qz_dialog_instance_qzDialog1") #定位到弹出对话框的div
        time.sleep(1)
        browser.find_element_by_link_text("确定").click()
        time.sleep(1)
        print("林国政成功删除一页")
        
        browser.refresh()
        time.sleep(2)
        
    
if __name__ == "__main__":
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=chrome_options)  # Chrome界面
    #browser.maximize_window()
    #browser = webdriver.PhantomJS()  # 无界面
    work(browser)
    browser.quit()