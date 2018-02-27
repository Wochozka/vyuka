#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class User:

  minPassLength = 6   # this is static variable
  nextID = 1          # this is static variable too :-)

  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.logged = False
    self.ID = User.nextID
    User.nextID += 1

  def login(self, password):
    if self.password == password:
      self.logged = True
      return True
    else:
      self.logged = False
      return False


