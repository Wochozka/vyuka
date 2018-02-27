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

  @staticmethod                             # this is static method (by class, not by instance)
  def passwordValidation(password):         # static method does not need "self" (there is no selfable instance)
    if len(password) >= User.minPassLength:
      return True
    else:
      return False

  @classmethod
  def passwordValidation(cls, password):    # this is class-methon (by class too, but with class-name)
    if len(password) >= cls.minPassLength:  # class-name is like parameter; useful for inheritance
      return True
    else:
      return False

  def returnID(self):                       # access directly to the ID is not nice
    return self.ID                          # in practice should be private with "__" prefix


user1 = User("john.doe", "BestPassword")
print("User 1: ID: {0}".format(user1.returnID()))
user2 = User("jane.doe", "betterPassword")
print("User 2: ID: {0}".format(user2.returnID()))
print("Min pass length: {0}".format(User.minPassLength))
