#!/usr/bin/env python3

import cgi

from util import Util

form = cgi.FieldStorage()
action = form.getfirst("action")

login = form.getfirst("login")
password = form.getfirst("password")
publish = form.getfirst("text")

util = Util()

online = util.get_data(util.ONLINE)
user = online[0] if len(online) else None

error = False
message = ''

if action == "login":
    if util.login(login, password):
        user = login
        posts = util.get_posts(user)
        string = '<h2>Ваши посты:</h2><br>'
        for post in posts:
            string += f'<p>{post}</p>'
        message = string
    else:
        error = True
        message = '<p>Такой пользователь не зарегистрирован</p>'
elif action == "publisher":
    util.set_posts(user, publish)
    posts = util.get_posts(user)
    string = '<h2>Ваши посты:</h2><br>'
    for post in posts:
        string += f'<p>{post}</p>'
    message = string
elif action == "register":
    util.register(login, password)
    message = '<p>Вы зарегистрированы и уже авторизованы</p>'
elif action == "logout":
    util.logout(user)
    message = "<p>Вы вышли из системы</p>"
elif not action:
    if not util.is_online(user):
        action = "logout"


if action == "logout" or error:
    form = '''
        <h1>Авторизуйтесь</h1>
        <form method="post" action="wall.py">
            Логин: <input type="text" name="login">
            Пароль: <input type="password" name="password">
            <input type="hidden" name="action" value="login">
            <input type="submit">
        </form>
        <h1>Еще не зарегистрированы?</h1>
        <form method="post" action="wall.py">
            Логин: <input type="text" name="login">
            Пароль: <input type="password" name="password">
            <input type="hidden" name="action" value="register">
            <input type="submit">
        </form>
    '''
else:
    form = f'''
        <form action="wall.py">
            <textarea name="text"></textarea><br>
            <input type="hidden" name="action" value="publisher">
            <input type="submit">
        </form><br>
        <form action="wall.py">
            <input type="hidden" name="action" value="logout"
            <p>
            <input type="submit" value="Выйти"><br><br><br>
        </form>
    '''

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Wall</title>
</head>
<body>
    {message}
    {form}
</body>
</html>
'''

print('Content-type: text/html\n')
print(pattern.format(form=form, message=message, action='publisher'))