import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import cv2


# 이미지 검색을 통해서 원하는 키위 위치를 동적으로 얻고 이를 반환
def search_location(search):
    small_image = cv2.imread(f'img_{search}.png')
    large_image = cv2.imread('password.png')

    result = cv2.matchTemplate(small_image, large_image, cv2.TM_SQDIFF_NORMED)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc
    trows, tcols = small_image.shape[:2]
    position_x = (2 * MPx + tcols) / 2
    position_y = (2 * MPy + trows) / 2
    print(f'{search}, x: {position_x}, y:{position_y}')
    return position_x, position_y


# 지정한 이미지의 위치를 클릭하는 모듈
def pass_click(driver, element,  search):
    act = ActionChains(driver)
    x, y = search_location(search)
    target_x = element.location['x'] + x
    target_y = element.location['y'] + y
    print(f'click : {search}, x: {target_x}, y: {target_y}')
    act.move_by_offset(target_x, target_y).click().perform()
    act.reset_actions()


driver = webdriver.Chrome()
driver.get('https://ui.vpay.co.kr/web2/login/view')

# wait time for loading
time.sleep(5)
python_button = driver.find_elements_by_xpath("//button[@class='btn-input-mouse']")[0]
python_button.click()
time.sleep(3)

# 원하는 이미지를 찾는지 테스트
# search_location(1)
# search_location(2)
# search_location(3)
# search_location(4)
# search_location(5)
# search_location(6)
# search_location(7)
# search_location(8)
# search_location(9)
# search_location(0)
# search_location('remove_all')
# search_location('remove')
# search_location('complete')

pass_buttons = driver.find_elements_by_xpath('//div[@id="pwd_layoutSingle"]')[0]
pass_buttons.screenshot('password.png')

# 테스트수행
pass_click(driver, pass_buttons, '1')
pass_click(driver, pass_buttons, '3')
pass_click(driver, pass_buttons, '5')
pass_click(driver, pass_buttons, '7')
pass_click(driver, pass_buttons, 'remove_all')
pass_click(driver, pass_buttons, '2')
pass_click(driver, pass_buttons, '4')
pass_click(driver, pass_buttons, '6')
pass_click(driver, pass_buttons, 'remove')
pass_click(driver, pass_buttons, '8')
pass_click(driver, pass_buttons, '9')
pass_click(driver, pass_buttons, 'complete')




