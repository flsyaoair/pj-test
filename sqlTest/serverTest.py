# -*- coding: UTF-8 -*- 
import logging

from sqlTest import  database
from datetime import datetime
from sqlalchemyTest import *
def taskCreate():

    session = database.get_session()
#     user = User(name='first', username=u'新的')
#     session.add(user)
#     session.flush()
#     blog = Blog(title=u'第一个', user=user.id)
#     session.add(blog)
#     session.commit()
            
 
    print session.query(Blog).get(1).user_obj
    print session.query(User).get(1).blog_list

if __name__ == '__main__':
     
      taskCreate()  