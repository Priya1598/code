import os
from playwright.sync_api import Playwright, sync_playwright
import time
import keyboard
cd = os.getcwd()
 
 
with open(rf'{cd}\input_location.txt', 'r') as file:
    lines = file.readlines()
    filter_conditions = eval(lines[0].strip())
 
def wait_for_element(page, element_id: str):
    page.wait_for_selector(f'#{element_id}')
 
def wait_for_element_xpath(page, xpath: str):
    page.wait_for_selector(f'xpath={xpath}')
download_path = os.path.join(os.getcwd(),'downloads')
os.makedirs(download_path,exist_ok=True)
            
def run(playwright: Playwright):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Update with your path
    browser = playwright.chromium.launch(headless=False, executable_path=chrome_path)
    # # context = browser.new_context()
    # user_data = "C:\\Users\\180100\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default"
    # browser = playwright.chromium.launch_persistent_context(user_data, headless=False, channel='msedge')
    page = browser.new_page()
    page.goto("https://saa.portal.nttdataservices.com/powerbireports/powerbi/PROD/LMS/Courses/Catalys_Home")
    # time.sleep(10)
    # page.keyboard.press('Enter')
    # login_box = frame.locator('//*[@id="tilesHolder"]/div[1]/div/div/div/div[2]/div[2]/small')
    # login_box.wait_for()
    # login_box.click()
    
    time.sleep(50)
    while True:
        try:
            frame = page.frame_locator("iframe").first
            # Interact with the checkbox
            # page.wait_for_selector('xpath=/html/body/div[1]/ui-view/div/div/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/span')
            check_box_frame = 'xpath=//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/span'
            check_box = frame.locator(check_box_frame)
            check_box.wait_for()
            check_box.click()
            break
        except:
            time.sleep(2)
    time.sleep(20)
    for key, values in filter_conditions.items():
        # Search for the key
        # search_box = frame.locator('xpath=/html/body/div[1]/ui-view/div/div/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[1]/input')
        search_box = frame.locator('xpath=//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[1]/input')
        # search_box = frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div/1/input')
        search_box.wait_for()
        search_box.click()
        search_box.fill("")
        page.keyboard.type(f'{key}')
        time.sleep(10)
        # page.keyboard.press('enter')
        # page.wait_for_timeout(10000)  # 10 seconds
        # print(key)
        try:
            try:
                check_box_selector = frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/span')
                check_box_selector.click()
                page.wait_for_timeout(15000)  #15 seconds
            except:
                scheck_box_selector=frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/span')
                scheck_box_selector.click()
                page.wait_for_timeout(15000) 
        except Exception as e:
            print("Please use xpath after declaring frame\nframe->xpath\nSuppressing this error as this element is not visually restricted to us")
            pass
        # # Search for courses and download
        course_search_box = frame.locator('xpath=/html/body/div[1]/ui-view/div/div/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[1]/input')
        course_search_box.wait_for()
        # course_search_box = frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[1]/input')
        for value in values:
            course_search_box.click()
            course_search_box.fill("")
            page.keyboard.type(f'{value}')
            # course_search_box.fill(value)
            page.wait_for_timeout(10000)  # 10 seconds
            print(value)
            try:
                fstcourse_selector = frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/span')
                fstcourse_selector.click()
                page.wait_for_timeout(10000)  # 10 seconds
            except:
                course_selector = frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[26]/transform/div/div[2]/div/div/visual-modern/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/span')
                course_selector.click()
                page.wait_for_timeout(10000)  # 10 seconds
            with page.expect_download() as download_info:
                download = frame.locator('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[10]/transform/div/div[2]/div/div')
                download.click()
            time.sleep(15)
            # downloads=download_info.value
            # file_path=os.path.join(download_path,downloads.dummy.csv)
            # downloads.save_as(file_path)
            # page.keyboard.press('Enter')
            page.wait_for_timeout(40000)  #  30 seconds
            # browser.close()
 
playwright = sync_playwright().start()
try:
    run(playwright)
finally:
    print('pass')