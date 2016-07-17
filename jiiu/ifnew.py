#-*-coding:utf-8-*-
import os.path
#判断是否为新玩家
def new():
	if not os.path.exists('data.pkl'):
		return True
	else:
		return False
