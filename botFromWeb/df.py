from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_driver = "/Users/imadecandragirinata/Downloads/chromedriver"
chrome_options=Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")


driver = webdriver.Chrome(chrome_driver,chrome_options=chrome_options)