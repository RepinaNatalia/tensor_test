# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста



from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    driver.get(sbis_site)
    sleep(2)
    btn1 = driver.find_element(By.LINK_TEXT, "Контакты")
    btn1.click()   # клик по Контактам
    sleep(2)
    btn2 = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    btn2.click()   # клик по логотипу
    driver.switch_to.window(driver.window_handles[1])  # переход на другую вкладку
    sleep(2)
    btn3 = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]')
    sleep(2)
    assert btn3.text.split('\n')[0] == "Сила в людях"   #  проверка текста
    actions = ActionChains(driver)
    actions.move_to_element(btn3)
    actions.perform()  # Скролл до кнопки "Подробнее"
    sleep(2)
    btn4 = driver.find_elements(By.CSS_SELECTOR, '[class="tensor_ru-link tensor_ru-Index__link"]')[1]  #ищем второй элемент из списка 
    btn4.click()  # клик по "Подробнее"
    assert driver.current_url == 'https://tensor.ru/about'   # проверка текущей вкладки
    sleep(2)

finally:
    driver.quit()