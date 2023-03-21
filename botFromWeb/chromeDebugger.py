import csv
import random
from time import sleep

from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_driver = "/Users/imadecandragirinata/Downloads/chromedriver"
chrome_options=Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")


driver = webdriver.Chrome(chrome_driver,chrome_options=chrome_options)
# driver.get('http://www.instagram.com/');

####################### Grab related hashtag  #############################

isiList = list()
hashtag = raw_input("Enter hashtag : ")

# hashtag = [x for x in raw_input("Enter hashtag:")]

driver.get('https://www.instagram.com/explore/tags/' +hashtag+ '/')
isi = driver.find_elements_by_css_selector('a.LFGs8.xil3i')

noTagsURL = list()
for x in isi:
    isiList.append(x.text)

x = len(isiList)#rows
print(x)
y=2#columns
a=[]#create an empty list first
for i in range(x):
    a.append([0]*y)

isiDataH = -1
for data in isiList:
    isiDataH += 1
    a[isiDataH][1] = data
    noTags = (data.replace('#', ''))
    # for j in range(1):
    noTagsURL.append(noTags)
    # print(noTags)


with open('dataarray.txt', mode='a') as write_file:
    write_data = csv.writer(write_file)
    write_data.writerow(isiList)

print(noTagsURL)




# username = driver.find_element_by_name('username')
# username.send_keys('gohankuluk@gmail.com')
# password = driver.find_element_by_name('password')
# password.send_keys('4Lay1708')
#
# button_login = driver.find_element_by_tag_name('form')
# button_login.submit()
#

####################### Input hashtag , distinct # from hashtag , get webpage of hashtag #############################

# # noTagsURL = list()
#
# int_list = [x for x in raw_input("Enter hashtag:").split()]
# print(int_list)
# for data in int_list:
#     noTags = (data.replace('#', ''))
#     noTagsURL.append(noTags)
#
# print(noTagsURL)
#
pArray = -1
# i = 0


angkaKiriman = list()
fixNumber = list ()
for i in noTagsURL:
    # print(i)
    pArray += 1
    driver.get('https://www.instagram.com/explore/tags/' + noTagsURL[pArray] +'/')


    ####################### Grab number of hashtag post #############################


    nPosts = driver.find_elements_by_xpath("//span[@class='g47SY ']")
    for nPost in nPosts:
        angkaKiriman.append(nPost.text)
    sleep(random.uniform(8, 15))



isiDataN = -1
print('\nPrint Biasa')
for data in angkaKiriman:
    noComma = (data.replace(',', ''))
    fixNumber.append(noComma)
    isiDataN += 1
    # for j in range(y):
    a[isiDataN][0]= fixNumber
    print(a[isiDataN][0])

with open('dataarray.txt', mode='a') as write_file:
    write_data = csv.writer(write_file)
    write_data.writerow(fixNumber)



print('\n Tes sort')
a.sort(key=lambda x:[1] , reverse=True)



isi = -1
for i in a :
    isi += 1
    print(a[isi][1])

    print(a[isi][0])

print(" \n Selesai")






#
# for isi1 in a:
#     for isi2 in range(2):
#         print(a[isi1][1])


# fixNumber.sort(reverse=True)
# print(fixNumber)


# sleep (8)
# driver.quit()


