#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.logged = False

  def login(self, password):
    if self.password == password:
      self.logged = True
      return True
    else:
      self.logged = False
      return False


