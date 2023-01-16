from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.snackbar import Snackbar


# In order to run this program you should have kivy and kivymd modules installed
# Created for study project 
class MenuScreen(Screen):
    pass


class RulesScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class PlayersScreen1(Screen):
    pass


class ProfileScreen1(Screen):
    pass


class PlayersScreen2(Screen):
    pass


class PlayersScreen3(Screen):
    pass


class PlayersScreen4(Screen):
    pass


class PlayersScreen5(Screen):
    pass


class ProfileScreen2(Screen):
    pass


class ProfileScreen3(Screen):
    pass


class ProfileScreen4(Screen):
    pass


class ProfileScreen5(Screen):
    pass


class Sentence(Screen):
    pass


# Create the screen manager


sm = ScreenManager()

sm.add_widget(ProfileScreen1(name='profile1'))
sm.add_widget(ProfileScreen2(name='profile2'))
sm.add_widget(ProfileScreen3(name='profile3'))
sm.add_widget(ProfileScreen4(name='profile4'))
sm.add_widget(ProfileScreen5(name='profile5'))

sm.add_widget(PlayersScreen1(name='players1'))
sm.add_widget(PlayersScreen2(name='players2'))
sm.add_widget(PlayersScreen3(name='players3'))
sm.add_widget(PlayersScreen4(name='players4'))
sm.add_widget(PlayersScreen5(name='players5'))

sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(RulesScreen(name='rules'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(Sentence(name='sentence'))
sm.add_widget(AboutScreen(name='about'))


class MainApp(MDApp):
    def build(self):
        self.title = "Sentence Game"
        self.icon = 'question-mark.png'

        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('fortext.kv')

    def on_switch_active(self, value):
        if value:
            self.theme_cls.theme_style = "Dark"

        else:
            self.theme_cls.theme_style = "Light"

    def disable(self, text, root, page):
        if text and len(text) < 13:
            root.manager.current = page
            root.manager.transition.direction = 'left'
        elif not text:
            Snackbar(text="Enter your name").show()
            self.disabled = True
        elif not len(text) < 13:
            Snackbar(text="Maximum 12 characters allowed").show()
            self.disabled = True

    def disable_layout(self, root, page, text1, text2, text3, text4, text5):
        if text1 and text2 and text3 and text4 and text5:
            root.manager.current = page
            root.manager.transition.direction = 'left'
        else:
            self.disabled = True
            Snackbar(text="Enter your words!").show()


#   #fc4e77 #ffa41c  #bc20c7  #32a858 #c94208
if __name__ == "__main__":
    MainApp().run()
