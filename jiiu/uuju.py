#-*-coding:utf-8-*-
import pickle
#========================================================================
#数据存储
def data_dump(data):
	with open('data.pkl', 'wb') as output:
		pickle.dump(data, output)
	print "您的数据已保存"
#========================================================================
#========================================================================
#数据读取
def data_load():
	with open('data.pkl', 'rb') as input:
		data = pickle.load(input)
	return data
#========================================================================