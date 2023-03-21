import random
from random import randint
from time import sleep
from login2 import *
from selenium import webdriver

# driver = webdriver.Firefox()


hashtag_list = ['travelblog', 'travelblogger', 'traveler']

prev_user_list = []

# - if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,
#                  1:2]  # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    driver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(random.uniform(1, 5))

    first_thumbnail = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(random.uniform(1, 5))
    try:
        for x in range(1, 200):
            username = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text

            if username not in prev_user_list:
                # If we already follow, do not unfollow
                if driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Ikuti':

                    driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

                    button_like.click()
                    likes += 1
                    sleep(random.uniform(18, 25))

                    # Comments and tracker
                    comm_prob = randint(1, 10)
                    print('{}_{}: {}'.format(hashtag, x, comm_prob))
                    if comm_prob > 7:
                        comments += 1
                        driver.find_element_by_xpath(
                            '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                        comment_box = driver.find_element_by_xpath(
                            '/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')

                        if (comm_prob < 7):
                            comment_box.send_keys('Really cool!')
                            sleep(random.uniform(1, 5))
                        elif (comm_prob > 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :)')
                            sleep(random.uniform(1, 5))
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!!')
                            sleep(random.uniform(1, 5))
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :)')
                            sleep(random.uniform(1, 5))
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        sleep(random.uniform(22, 30))

                # Next picture
                driver.find_element_by_link_text('Next').click()
                sleep(random.uniform(22, 30))
            else:
                driver.find_element_by_link_text('Next').click()
                sleep(random.uniform(22, 30))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

# updated_user_df = pd.DataFrame(prev_user_list)
# updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
