from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.image import ImageLoader
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

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
    
    def button_press(self, *args):
        popup.close()

    def color_popup(*args):
        button1 = Button(text = 'red', size_hint = (1, .33), background_color = [1, 0, 0, 1])
        button2 = Button(text = 'green', size_hint = (1, .33), background_color = [0, 1, 0, 1])
        button3 = Button(text = 'blue', size_hint = (1, .33), background_color = [0, 0, 1, 1])
        
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(button1)
        box.add_widget(button2)
        box.add_widget(button3)
        
        popup = Popup(title='Background Color', content = box, size_hint = (.5, .5), background_color = [0, 0, 0, 1])
        popup.open()
  
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
