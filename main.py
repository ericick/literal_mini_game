#-*-coding:utf-8-*-
from jiiu import uuju, xrze, ifnew
from game import iuuihw, ybxijxmm
from sys import exit
#首先定义整个游戏的运行引擎
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
		print '进入了一个游戏'
		return 'ybxijxmm'
		
class Mine(Game):
	def enter(self):
		print '挖矿'
		return 'ybxijxmm'
		
class Tviu(Game):
	def enter(self):
		print '退出'
		exit(1)
		
class Plant(Game):
	def enter(self):
		print "你想干嘛"
		raw_input(" >")
		print '种地'
		return 'ybxijxmm'

class Map(object):
	
	games = {'挖矿': Mine(),
			'种植': Plant(),
			'iuuihw': iuuihw.Iuuihw(),
			'ybxijxmm': ybxijxmm.Ybxijxmm(),
			'退出': Tviu()}
	
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