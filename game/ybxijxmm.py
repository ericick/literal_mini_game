#-*-coding:utf-8-*-
from jiiu import uuju, xrze
#========================================================================
class Game(object):
	def enter(self):
		print '进入了一个游戏'
		return 'mine'
#========================================================================
def ybximmbj():
	print '=' * 79
	data = uuju.data_load()
	print '姓名: %s' % data['姓名']
	print '性别: %s' % data['性别']
	print '种族: %s' % data['种族']
	print '职业: %s' % data['职业']
	print '等级: %s' % data['等级']
	print '=' * 79
#========================================================================
def xrzexdmu():
	dict = {
			1: '挖矿',
			2: '种植',
			3: '退出'}
	choice = xrze.qrtk(dict, "接下来你想做什么？")
	return choice
#========================================================================
class Ybxijxmm(Game):
	def enter(self):
		ybximmbj()
		choice = xrzexdmu()
		return choice
#========================================================================