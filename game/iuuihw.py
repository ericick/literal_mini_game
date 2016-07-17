#-*-coding:utf-8-*-
from jiiu import uuju, xrze
#========================================================================

#========================================================================
class Game(object):
	def enter(self):
		return 'mine'		
#========================================================================
def welcome():
	print '=' * 79
	print '欢迎来到这个新世界我的朋友!'
	print '希望你能够有一段愉快的冒险经历!'
	print '=' * 79
	raw_input("> ")
#========================================================================
def choice():
	#以下是各种选项 包括种族 职业和性别
	dict = {'种族': {1: '人类',
					2: '暗夜精灵',
					3: '矮人',
					4: '侏儒',
					5: '德莱尼',
					6: '兽人',
					7: '巨魔',
					8: '亡灵',
					9: '牛头人',
					10: '血精灵',
					11: '狼人',
					12: '熊猫人',},
			'职业': {1: '猎人',
					2: '法师',
					3: '术士',
					4: '德鲁伊',
					5: '牧师',
					6: '盗贼',
					7: '萨满',
					8: '圣骑士',
					9: '战士',
					10: '武僧'},
			'性别': {1: '男',
					2: '女'}}
	#最终的选择就要输出到这个字典里面 这是初始化
	choices = {'种族': 'null',
				'职业': 'null',
				'性别': 'null',
				'姓名': 'null',
				'等级': 1,
				'红': 100,
				'蓝': 100,
				'任务开始': 'null',
				'任务时长': 'null'}
	#遍历字典 这是前面的字典 提供选项
	for i, item in enumerate(dict):
		choice = xrze.qrtk(dict[item], '请选择你的%s:' % item)
		choices[item] = choice
	#请求输入名字
	print '给你的角色一个名字吧~'
	choices['姓名'] = raw_input("> ")
	print '你现在是一个%s性%s%s了，%s这个名字必将响彻大陆' % (choices['性别'], choices['种族'], choices['职业'], choices['姓名'])
	uuju.data_dump(choices)
	return choices
#========================================================================
class Iuuihw(Game):
	def enter(self):
		print '初始化第一步'
		welcome()
		choices = choice()
		data = uuju.data_load()
		print data['姓名']
		return 'ybxijxmm'
