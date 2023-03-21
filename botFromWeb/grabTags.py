import csv
from selenium import webdriver

driver = webdriver.Firefox()

isiList = list()
driver.get('https://www.instagram.com/explore/tags/followandfollow/')
isi = driver.find_elements_by_css_selector('a.LFGs8.xil3i')

noTagsURL = list()
for x in isi:
    isiList.append(x.text)
for data in isiList:
    noTags = (data.replace('#', ''))
    noTagsURL.append(noTags)
    print(noTags)

with open('dataarray.txt', mode='a') as write_file:
    write_data = csv.writer(write_file)
    write_data.writerow(isiList)

# # BACA CSV
# with open('dataarray.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     # for row in csv_reader:
#     #     if line_count == 0:
#     #         print(f'Column names are {", ".join(row)}')
#     #         line_count += 1
#     #     else:
#     #         # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#     #         line_count += 1
#     #         break
#     while True:
#
#     print(f'Processed {line_count} lines.')

# ### baca 2
# from typing import OrderedDict
#
# bacaIsi = []
# with open('dataarray.txt', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         bacaIsi.append(row)
#     # print(row.replace('#', ''))
#
# print(bacaIsi[0])
#
#
# # print([s.replace('#', '') for s in bacaIsi])

# inte = 0
# for i in bacaIsi:
#     inte += 1
#     bacaIsi[inte].remove('#')


# fruits = ['apple', 'banana', 'cherry']
#
#
#
# print([s.replace('a', '') for s in fruits])
