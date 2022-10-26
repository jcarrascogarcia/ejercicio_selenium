from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://micgr.contraloria.cl")

input_box_username = driver.find_element(By.ID, "tusername")

input_box_password = driver.find_element(By.ID, "tpassword")

input_box_username.send_keys("jcarrascog")

input_box_password.send_keys("1234")


botonIngresar = driver.find_element(By.CLASS_NAME, "IngresarBoton")
botonIngresar.send_keys(Keys.ENTER)

#import time

#print('esperaremos 5 segundos' )
#time.sleep(5)

#driver.get("https://micgr.contraloria.cl/cgrsica/SicaInf/")

#print('esperaremos 5 segundos' )
#time.sleep(3)

#driver.get("https://micgr.contraloria.cl/SicaProd/SICAv3-AuditoriaCumplimiento/faces/buscarAuditoriaCumByUsuario?_adf.ctrl-asign=Qd2hjZDQqP1K2NSPH6XyyX6HxgPTKd9GFk2fGphV266pbFnMZC9P!1010413882!1666794256842")
