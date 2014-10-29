from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.image import ImageLoader
from kivy.uix.widget import Widget


class SnakeLogo(Widget):
    texture = ObjectProperty()

    def __init__(self, **kwargs):
        self.texture = ImageLoader.load('snake.png').texture
        super(SnakeLogo, self).__init__(**kwargs)

class MenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class Settings(Screen):
    def __init__(self, *args, **kwargs):
		super(Settings, self).__init__(*args, **kwargs)
		
		self.onLabel = self.ids["on_or_off"]
		
		
    def on_off(self):
        if(self.onLabel.text == 'on'):
           self.onLabel.text = "off"
            
        else:
            self.onLabel.text = "on"

class HighScores(Screen):
    pass


class SnakeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(GameScreen(name = 'game'))
        sm.add_widget(Settings(name = 'settings'))
        sm.add_widget(HighScores(name = 'high_scores'))
        return sm

if __name__ == '__main__':
    SnakeApp().run()
