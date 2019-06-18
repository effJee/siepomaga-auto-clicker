from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options=options)
browser.get('https://www.siepomaga.pl/s/klikaj')
main_window = browser.current_window_handle

clickers = browser.find_elements_by_link_text('Klik')

# https://www.pajacyk.pl/#index
clickers[0].click()
browser.switch_to.window(browser.window_handles[-1])
pajacyk = browser.find_element_by_class_name('paj-click')
button = browser.find_element_by_class_name('paj-click2')
ActionChains(browser).move_to_element(pajacyk).click(button).perform()
browser.close()
browser.switch_to.window(main_window)

# http://www.okruszek.org.pl/
clickers[1].click()
browser.switch_to.window(browser.window_handles[-1])
browser.close()
browser.switch_to.window(main_window)

# http://www.pmiska.pl/
clickers[2].click()
browser.switch_to.window(browser.window_handles[-1])
browser.close()
browser.switch_to.window(main_window)
# print(browser.current_url)
