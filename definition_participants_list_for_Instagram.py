from instabot import Bot
import re
import argparse
import os
from dotenv import load_dotenv


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('post_link', help='Ваша ссылка на пост' )
    parser.add_argument('post_username', help='Никнейм автора поста')
    return parser

def get_user_from_comment(comment):
    return re.findall(r'(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)', comment)

def is_user_exist(username):
    if bot.get_user_id_from_username(username) == None:
        return False
    else:
        return True

if __name__ == "__main__":
    load_dotenv()
    LOGIN = os.getenv('LOGIN_INSTAGRAM')
    PASSWORD = os.getenv('PASSWORD_INSTAGRAM')
    parser = createParser()
    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    post_link = parser.parse_args().post_link
    post_username = parser.parse_args().post_username
    post_id = bot.get_media_id_from_link(post_link)
    comments = bot.get_media_comments_all(post_id)
    users_with_real_friend = []
    for comment in comments:
        usernames = get_user_from_comment(comment['text'])
        for username in usernames:
            if is_user_exist(username):
                friend_not_fake = True
                break
            else:
                friend_not_fake = False
        if friend_not_fake:
            users_with_real_friend.append((comment['user']['pk'], comment['user']['username']))
    users_id_who_like_post = bot.get_media_likers(post_id)
    user_followers = bot.get_user_followers(bot.get_user_id_from_username(post_username))
    users_who_meet_conditions = []
    for user_id, username in users_with_real_friend:
        if str(user_id) in users_id_who_like_post and str(user_id) in user_followers:
            users_who_meet_conditions.append((user_id,username))

    print('Список участников: ', )
    for user_id, username in set(users_who_meet_conditions):
        print(username, end=' ')
