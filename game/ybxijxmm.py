#-*-coding:utf-8-*-
from jiiu import uuju, xrze
#========================================================================
class Game(object):
	def enter(self):
		print '������һ����Ϸ'
		return 'mine'
#========================================================================
def ybximmbj():
	print '=' * 79
	data = uuju.data_load()
	print '����: %s' % data['����']
	print '�Ա�: %s' % data['�Ա�']
	print '����: %s' % data['����']
	print 'ְҵ: %s' % data['ְҵ']
	print '�ȼ�: %s' % data['�ȼ�']
	print '=' * 79
#========================================================================
def xrzexdmu():
	dict = {
			1: '�ڿ�',
			2: '��ֲ',
			3: '�˳�'}
	choice = xrze.qrtk(dict, "������������ʲô��")
	return choice
#========================================================================
class Ybxijxmm(Game):
	def enter(self):
		ybximmbj()
		choice = xrzexdmu()
		return choice
#========================================================================