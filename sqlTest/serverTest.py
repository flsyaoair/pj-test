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
            
#  
#     print session.query(Blog).get(1).user_obj
    data=session.query(User).filter(User.blog_list.any(Blog.title == '哈哈fls')).first()
    print "12312377777777777777777777777777" ,data
#     print  session.query(User).filter(User.blog_list.any(Blog.title == '第一个')).first()
#     blog = session.query(Blog).first()
#     print blog.user_obj.name



#     user = User(name=u'heb哈哈')
#     blog = Blog(title=u'一个')
#     user.blog_list = [blog]
#     #user.blog_list_auto = [blog]
#     session.add(user)
#     print blog in session
#     session.commit()
    


#     user = User(name='2',username=u'新的fls')
#     session.add(user)
#     session.commit()
#   
#     user = User(id=2, blog_list=[Blog(title='哈哈l4431',id=31),Blog(title='l444')])
#     session.merge(user)
#   
#     session.commit()


#     user = User(name=u'1')
#     blog = Blog(title=u'第一个')
#     user.blog_list = [blog]

#     session.add(user)
#     session.add(blog)

#     session.expunge(user)

#     print session.query(User).get(1).blog_list

if __name__ == '__main__':
     
      taskCreate()  