from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.siepomaga.pl/s/klikaj')
