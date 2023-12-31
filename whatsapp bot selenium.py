import sys
import time
from selenium import webdriver

def user_chat(name_user):
    chat_new = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
    chat_new.click()
    
    user_chat=browser.find_element_by_xpath('//div[@class="_3u328 copyable-text-selectable-text')
    user_chat.send_keys(name_user)

    time.sleep(2)

    try:
        user =browser.find_element_by_xpath('//span[@title="{}"]',format(name_user))
        user.click()

    except Exception as e:
          print(f"user {name_user} is not in the contacts")

    except Exception as e:
         browser.close()
         print(e)
         sys.exit()

if __name__=='__main__':
    my_options=webdriver.ChromeOptions()
    browser =webdriver.Chrome('chromedriver.exe',options='')
    browser.get('https://web.whatsapp.com')

    time.sleep(20)

    name_list=['rudra']

    for name_user in name_list:


         try:
              user=browser.find_element_by_xpath('//span[@title="{}"]'.format(name_user))
              user.click() 

            except Exception as e:
            print(e)

    
    box_message=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    box_message.send_keys("hello")

    time.sleep(10)
    box_message=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/')
    box_message.click()
    
    time.sleep(20)


browser.close()