from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas as pd
from datetime import datetime
cd=os.getcwd()
import warnings
import logging
# import fitz
import re
import shutil
import numpy as np
import time
from datetime import datetime,timedelta
import warnings
import configparser
import sys
from pathlib import Path
print('###################################################################Automation Started for Mercy-Lozier SLA raw data-DBA ##########################################################################')
import os
import pandas as pd
import datetime
import time
from win32api import MessageBox
import ctypes
import socket
global Start_Time
from sqlalchemy import create_engine
import urllib
# conn = engine.connect()
Start_Time = time.strftime("%m/%d/%y %H:%M:%S")
today=datetime.datetime.today()
Portal_Id = os.getlogin()
 
#User Name:
GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
NameDisplay = 3
size = ctypes.pointer(ctypes.c_ulong(0))
GetUserNameEx(NameDisplay, None, size)
 
nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
GetUserNameEx(NameDisplay, nameBuffer, size)
 
full_name = nameBuffer.value
 
#Domain:
domain_name = socket.getfqdn(socket.gethostbyname(socket.gethostname())).lower()
domain = ('YES' if ('nttdata' in domain_name) or ('keane.com' in domain_name) else 'NO')
 
#Code to Capture Domain Name:
Dname = socket.getfqdn(socket.gethostbyname(socket.gethostname())).lower()
 
#SQL Config:
try:
    params = urllib.parse.quote_plus('Driver={ODBC Driver 17 for SQL Server};'
                                     'Server=10.235.21.137;'
                                     'Database=ATI_LogCapture;'
                                     'UID=ATILogDB;'
                                     'PWD=[]Y&@`@j&U7W!F_H;')
 
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params), fast_executemany=True)
except:
    MessageBox(0,'Connect to VPN and Zscalar properly','Error')
    exit()
 
 
#BotVersion Check
 
bot_name = 'ATI_BOT_Catalys'
version = '1.0'
key = (pd.read_sql_query(f"select * from tbl_ATI_BOT_Owner_Details Where Bot_File_Name ='{bot_name}' and Bot_Version = '{version}'", engine)['BOT_Updated_Key'][0])
 
if key == 'ATI_BOT_Catalys_1.0_6_Jan_2025':
    pass
else:
    MessageBox(0,'Please use the Updated Version or Contact Developer','Error')
    exit()
 
current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
config_path = os.path.join(current_directory, 'Source', 'config.ini')
downloads_path=f'{current_directory}/Downloads'
chrome_driver_path = f"{cd}/Source/chromedriver.exe"
filestobedownloaded=str(Path.home()/"Downloads")
chrome_options=Options()
chrome_options.add_experimental_option("prefs",{
    "credentials_enable_service": False,
    "profile.password_manager_enabled":False,
    # "download.default_directory":filestobedownloaded,
    "download.prompt_for_download":False,
    "profile.default_content_settings.popups":0,
    "download.prompt_for_download":False,
    "safebrowsing.enabled":False
})
 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
 
# chrome_options.add_argument("disable-infobars")
 
chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://saa.portal.nttdataservices.com/powerbireports/powerbi/PROD/LMS/Courses/Catalys_Home")
 
chrome_options.add_argument("--disable-extensions")
 
chrome_options.add_argument("--disable-plugins-discovery")
 
chrome_options.add_argument("--start-maximized")
 
# chrome_options.add_argument("--safebrowsing-disable-download-protection")
 
service = Service(executable_path=chrome_driver_path)
 
service.start()
 
driver = webdriver.Chrome(service=service,options=chrome_options)
 
# driver.delete_all_cookies()
driver.get("https://saa.portal.nttdataservices.com/powerbireports/powerbi/PROD/LMS/Courses/Catalys_Home")
def waitelement(driver, element_id):
    entr = False
    while not entr:
        try:
            driver.find_element(By.ID, element_id)
            entr = True
            break
        except:
            pass
def waitelemen_xpath(driver, xpath):
    entr = False
    while not entr:
        try:
            driver.find_element(By.XPATH, xpath)
            entr = True
            break
        except:
            pass
def waitelement_class(driver, class_name):
    entr = False
    while not entr:
        try:
            driver.find_element(By.CLASS_NAME, class_name)
            entr = True
            break
        except:
            pass
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]','_',name).strip()
with open(rf'{current_directory}\input_location.txt', 'r') as file:
 
    lines = file.readlines()
 
    filter_conditions = eval(lines[0].strip())
 
config = configparser.ConfigParser()
config.read(config_path)
 
# Get credentials from config file
username = config.get('Credentials', 'username')
password = config.get('Credentials', 'password')
 
 
waitelement(driver,"i0116")
login=driver.find_element(By.ID,'i0116')
login.send_keys(f"{username}")
login.send_keys(Keys.ENTER)
 
 
waitelement(driver,"passwordInput")
passwords=driver.find_element(By.ID,'passwordInput')
passwords.send_keys(f"{password}")
passwords.send_keys(Keys.ENTER)
 
while True:
    ready_state=driver.execute_script("return document.readyState")
    if ready_state=="complete":
        break
    time.sleep(2)
driver.switch_to.frame(0)
while True:
    waitelemen_xpath(driver,'/html/body/div[2]/div/main/div[2]/div/div/form[1]/div[2]/input')
    confirm=driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div[2]/div/div/form[1]/div[2]/input')
    break
time.sleep(2)
confirm.send_keys(Keys.ENTER)
 
time.sleep(50)
driver.switch_to.frame(0)
waitelemen_xpath(driver,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/span')
check_box=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/span')
check_box.click()
counts=0
for key, values in filter_conditions.items():
    counts+=1
    search_box=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[1]/input')
    search_box.click()
    search_box.clear()
    search_box.send_keys(key)
    time.sleep(10)
    print(key)
    check_box_selector=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/span')
    check_box_selector.click()
    time.sleep(10)
    course_search_box=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[1]/input')
    course_search_box.click()
    for value in values:
        course_search_box.clear()
        course_search_box.send_keys(value)
        time.sleep(10)
        print(value)
        try:
            fstcourse_selector=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/span')
            fstcourse_selector.click()
            time.sleep(10)
        except:
            course_selector=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/span')
            course_selector.click()
            time.sleep(10)
        download=driver.find_element(By.XPATH,'//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[10]/transform/div/div[2]/div/div')
        download.click()
        files_before=set(os.listdir(filestobedownloaded))
        while True:
            time.sleep(1)
            files_after=set(os.listdir(filestobedownloaded))
            new_files=files_after-files_before
            if new_files:
                downloaded_file=os.path.join(filestobedownloaded,new_files.pop())            
                break
        # time.sleep(10)
        while True:
            try:
                with open(downloaded_file,'rb'):
                    break
            except PermissionError:
                time.sleep(2)
        sanitized_key=sanitize_filename(key)
        sanitized_value=sanitize_filename(value)
        new_file_name=f"{sanitized_key}_{sanitized_value}.xlsx"
        new_file_path=os.path.join(filestobedownloaded,f"{sanitized_key}_{sanitized_value}.xlsx")
        os.rename(downloaded_file,new_file_path)
        final_path=os.path.join(downloads_path,new_file_name)
        shutil.move(new_file_path,final_path)
 
count=counts
global End_Time
End_Time = time.strftime("%b/%d/%Y %H:%M:%S")
 
BOT_LOG = pd.DataFrame({'Bot_File_Name':['ATI_BOT_Catalys'],'BoT_Type':['1.0'],'BoT_StartDateTimeStamp':[Start_Time],
          'BoT_EndDateTimeStamp':[pd.to_datetime(time.strftime("%m/%d/%y %H:%M:%S"))],'No_ofTransaction_Count':[count],'UserPortalID':[Portal_Id],
         'UserName':[full_name],'ISNTTDomain':[domain],'Remarks':["Success"],'TransactionDate':[today.strftime('%Y-%m-%d')],'BoTStatus':['Completed'],
         'DomainName':[socket.getfqdn(socket.gethostbyname(socket.gethostname())).lower()]})
 
BOT_LOG.to_sql('tbl_ATI_BOT_Log_Capture',if_exists='append',con=engine,index=False)
print('###################################################################Automation Completed for Mercy-Lozier SLA raw data-DBA ##########################################################################')
 