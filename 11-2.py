# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
try:
    driver.get(sbis_site)
    sleep(1)
    user_login, user_password = 'Фонарь123', 'Фонарь1234'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(3)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(3)
    btn1 = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]') #кнопка Контакты в аккордеоне
    btn1.click()
    sleep(3)
    btn2 = driver.find_element(By.CSS_SELECTOR, '[class="NavigationPanels-SubMenu__head  NavigationPanels-SubMenu__head_default ws-flex-shrink-0"]')
    btn2.click() #еще раз клик по "Контакты" для перехода в реестр
    sleep(2)
    btn3 = driver.find_element(By.CSS_SELECTOR,'[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]')
    btn3.click() # + сообщение
    sleep(3)
    btn4 = driver.find_element(By.CSS_SELECTOR, '[class="controls-Field js-controls-Field controls-InputBase__nativeField controls-Search__nativeField_caretEmpty controls-Search__nativeField_caretEmpty_theme_default   controls-InputBase__nativeField_hideCustomPlaceholder"]')
    person = "Фонарев Дима"
    btn4.send_keys(person, Keys.ENTER) # ввели адресата, появилось автодополнение
    sleep(3)
    btn5 = driver.find_element(By.CSS_SELECTOR, '[class="controls-ListView__itemContent  controls-ListView__item_default-topPadding_s controls-ListView__item_default-bottomPadding_s controls-ListView__item-rightPadding_s controls-ListView__item-leftPadding_l "]')
    btn5.click() #выбрали адресата, открылось поле сообщения
    sleep(3)
    btn6 = driver.find_element(By.CSS_SELECTOR, '[class="textEditor_Viewer__Paragraph"]')
    btn6.click()
    sleep(2)
    text = "Наташа, ты молодец"
    btn6.send_keys(text, Keys.ENTER)  # ввели текст сообщения
    sleep(2)
    btn7 = driver.find_element(By.CSS_SELECTOR, '[class="msg-send-editor-send ws-flexbox ws-flex-shrink-0 msg-send-editor__send ws-justify-content-end"]')
    btn7.click() # отправили сообщение
    sleep(2)
    # проверяем сообщение в реестре
    message = driver.find_element(By.CSS_SELECTOR, '[class="msg-entity-text msg-entity_font_croppless richEditor_richContentRender_fontSize-m_theme-default controls_RichEditor_theme-default richEditor_richContentRender_theme-default richEditor_richContentRender richEditor_richContentRender_lineHeight-s richEditor_richContentRender_colorPalette-first richEditor_richContentRender_readOnly msg-dialogs-item__message-text msg-entity-text_normalized controls-List_DragNDrop__notDraggable ws-flex-shrink-1 msg-entity-expander__content ws-flex-grow-1 ws-flex-shrink-1"]')
    assert message.text == "Наташа, ты молодец"
    btn8 = driver.find_element(By.CSS_SELECTOR,'[class="controls-ListView__itemContent  controls-ListView__item_default-topPadding_s controls-ListView__item_default-bottomPadding_s controls-ListView__item-rightPadding_null controls-ListView__itemContent_withCheckboxes controls-ListView__itemContent_withCheckboxes_default "]')
    btn8.click()  # открыли сообщение
    sleep(2)
    btn9 = driver.find_element(By.CSS_SELECTOR,'[title="Удалить"]')
    btn9.click()  # удаляем сообщение
    sleep(3)
    mes1 = driver.find_element(By.CSS_SELECTOR, '[class="msg-entity-text msg-entity_font_croppless richEditor_richContentRender_fontSize-m_theme-default controls_RichEditor_theme-default richEditor_richContentRender_theme-default richEditor_richContentRender richEditor_richContentRender_lineHeight-s richEditor_richContentRender_colorPalette-first richEditor_richContentRender_readOnly msg-dialogs-item__message-text msg-entity-text_normalized controls-List_DragNDrop__notDraggable ws-flex-shrink-1 msg-entity-expander__content ws-flex-grow-1 ws-flex-shrink-1"]')
    assert mes1.text != "Наташа, ты молодец"
finally:
    driver.quit()
