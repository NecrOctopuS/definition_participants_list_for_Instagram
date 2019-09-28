# Definition of the list of participants of the action for a post on Instagram
Defines a list of participants for an Instagram post that meet the following conditions:
- the participant marked an existing user
- like
- subscribed

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

### Script run examples

On input send full link to the post on Instagram and the nickname of the author of the post
```
py definition_participants_list_for_Instagram.py https://www.instagram.com/p/BtON034lPhu/ beautybar.rus
```
After the script is executed, a list of participants is displayed.