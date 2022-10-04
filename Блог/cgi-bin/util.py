#!/usr/bin/env python3

import json
import os


class Util:
    USERS = "cgi-bin/users.json"
    ONLINE = "cgi-bin/online.json"
    POSTS = "cgi-bin/posts.json"

    def __init__(self):
        def create_file(path, content):
            if not os.path.exists(path) or not os.stat(path).st_size:
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(content, f)

        create_file(self.USERS, {})
        create_file(self.ONLINE, [])
        create_file(self.POSTS, {})

    def get_data(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return data

    def set_data(self, path, content):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f)

    def is_online(self, user):
        return user in self.get_data(self.ONLINE)

    def find(self, user):
        return user in self.get_data(self.USERS)

    def login(self, login, password):
        if self.find(login) and self.check_password(login, password):
            self.set_online(login)
            return True

        return False

    def register(self, login, password):
        if not self.find(login):
            users = self.get_data(self.USERS)
            users[login] = password
            self.set_data(self.USERS, users)
            self.set_online(login)
            posts = self.get_data(self.POSTS)
            posts[login] = []
            self.set_data(self.POSTS, posts)

    def logout(self, user):
        online = self.get_data(self.ONLINE)
        if user in online:
            online.remove(user)
        self.set_data(self.ONLINE, online)

    def set_online(self, user):
        online = self.get_data(self.ONLINE)
        if user not in online:
            online += [user]
            self.set_data(self.ONLINE, online)

    def check_password(self, login, password):
        users = self.get_data(self.USERS)
        return users[login] == password

    def get_posts(self, user):
        posts = self.get_data(self.POSTS)
        return posts[user]

    def set_posts(self, user, text):
        posts = self.get_data(self.POSTS)
        posts[user].append(text)
        self.set_data(self.POSTS, posts)
