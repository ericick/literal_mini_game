#-*-coding:utf-8-*-
from jiiu import uuju, xrze, ifnew
from game import iuuihw, ybxijxmm
from sys import exit
#���ȶ���������Ϸ����������
class Engine(object):
	def __init__(self, game_map):
		self.game_map = game_map
		
	def play(self):
		current_game = self.game_map.start_game()
		last_game = self.game_map.next_game('mine')
		
		while current_game != last_game:
			next_game_name = current_game.enter()
			current_game = self.game_map.next_game(next_game_name)
		
		current_game.enter()
		
class Game(object):
	def enter(self):
		print '������һ����Ϸ'
		return 'ybxijxmm'
		
class Mine(Game):
	def enter(self):
		print '�ڿ�'
		return 'ybxijxmm'
		
class Tviu(Game):
	def enter(self):
		print '�˳�'
		exit(1)
		
class Plant(Game):
	def enter(self):
		print "�������"
		raw_input(" >")
		print '�ֵ�'
		return 'ybxijxmm'

class Map(object):
	
	games = {'�ڿ�': Mine(),
			'��ֲ': Plant(),
			'iuuihw': iuuihw.Iuuihw(),
			'ybxijxmm': ybxijxmm.Ybxijxmm(),
			'�˳�': Tviu()}
	
	def __init__(self, start_map):
		self.start_map = start_map
	
	def next_game(self, map_name):
		game = Map.games.get(map_name)
		return game
		
	def start_game(self):
		return self.next_game(self.start_map)
		
if ifnew.new():
	map = Map('iuuihw')
else:
	map = Map('ybxijxmm')

game = Engine(map)
game.play()