from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Loading extension
EXTENSION_PATH = '/Users/dinoland/Library/Application Support/Google/Chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.17.0_0.crx'
# EXTENSION_PATH = '/Users/dinoland/Desktop/auto test/10.15.1_0.crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(12)

#Select get started button
driver.switch_to.window(driver.window_handles[0])
mainWindows = driver.current_window_handle
start_btn = driver.find_element(By.XPATH, '//button[text()="Get Started"]')
start_btn.click()

#Select import wallet button
import_btn = driver.find_element(By.XPATH, '//button[text()="Import wallet"]')
import_btn.click()

#Select Agree button
agree_btn = driver.find_element(By.XPATH, '//button[text()="I Agree"]')
agree_btn.click()

#Input 12-word phrase
input1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input')
input1.send_keys("attract")

input2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[1]/div/input')
input2.send_keys("mean")

input3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div[1]/div/input')
input3.send_keys("shuffle")

input4 = driver.find_element(By.XPATH, ' /html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[4]/div[1]/div/input')
input4.send_keys("cross")

input5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[5]/div[1]/div/input')
input5.send_keys("wing")

input6 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[6]/div[1]/div/input')
input6.send_keys("donor")

input7 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[7]/div[1]/div/input')
input7.send_keys("future")

input8 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[8]/div[1]/div/input')
input8.send_keys("amateur")

input9 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[9]/div[1]/div/input')
input9.send_keys("infant")

input10 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[10]/div[1]/div/input')
input10.send_keys("fix")

input11 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[11]/div[1]/div/input')
input11.send_keys("grace")

input12 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[12]/div[1]/div/input')
input12.send_keys("sea")

#input password
new_pwd = driver.find_element(By.ID, 'password')
new_pwd.send_keys("Bcda54321@")

confirm_pwd = driver.find_element(By.ID, 'confirm-password')
confirm_pwd.send_keys("Bcda54321@")

#Select agree checkbox
check_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input')
check_box.click()

#Select import button
import_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/form/button')
import_btn.click()

#Select all done button
done = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/button')
done.click()

#Disable pop-up
# print(driver.find_element(By.XPATH, '//body').text)
element1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/button')))
element1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@title="Close"]')))
# element1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div/button')
element1.click()


driver.get("https://appdev.luz.monster/")
driver.switch_to.window(driver.window_handles[2])

element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Approve"]')))
element2.click()

element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Switch network"]')))
element2.click()


driver.switch_to.window(mainWindows)
# driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.XPATH, '//body').text)

element3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/button[1]')))
element3.click()

element3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button')))
element3.click()

element3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'connect-wallet')))
element3.click()


WebDriverWait(driver, 20).until(EC.new_window_is_opened(driver.window_handles))

# driver.implicitly_wait(12)
driver.switch_to.window(driver.window_handles[2])

element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Next"]')))
element2.click()

element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Connect"]')))
element2.click()



driver.switch_to.window(mainWindows)
print(driver.find_element(By.XPATH, '//body').text)

element3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button')))
element3.click()

element3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'connect-wallet')))
element3.click()


WebDriverWait(driver, 20).until(EC.new_window_is_opened(driver.window_handles))

driver.switch_to.window(driver.window_handles[2])

element2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign"]')))
element2.click()
