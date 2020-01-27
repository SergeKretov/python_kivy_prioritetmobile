from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.config import Config

scrWidth = 640
scrHeight = 650

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', scrWidth)
Config.set('graphics', 'height', scrHeight)

class MyApp(App):
    def build(self):
        fl = FloatLayout(size = (scrWidth,scrHeight))
        fl.add_widget(Button(
            text = 'Главная',
            font_size = 16,
            size_hint = (.2 , .1),
            background_normal = '',
            background_color = [.61,.61,.61,1],
            pos = (0,0),
            on_press = self.btn_main_press));

        fl.add_widget(Button(
            text = 'О нас',
            font_size = 16,
            size_hint = (.2 , .1),
            background_normal = '',
            background_color = [.92,.92,.92,1],
            pos = (scrWidth/5,0),
            on_press = self.btn_about_press));
        
        fl.add_widget(Button(
            text = 'Услуги',
            font_size = 16,
            size_hint = (.2 , .1),
            background_normal = '',
            background_color = [.61,.61,.61,1],
            pos = (scrWidth/5*2,0),
            on_press = self.btn_uslugi_press));
        
        fl.add_widget(Button(
            text = 'Запись',
            font_size = 16,
            size_hint = (.2 , .1),
            background_normal = '',
            background_color = [.92,.92,.92,1],
            pos = (scrWidth/5*3,0),
            on_press = self.btn_zapis_press));

        fl.add_widget(Button(
            text = 'Контакты',
            font_size = 16,
            size_hint = (.2 , .1),
            background_normal = '',
            background_color = [.61,.61,.61,1],
            pos = (scrWidth/5*4,0),
            on_press = self.btn_contact_press));

        fl.add_widget(Button(
            text = 'Центр правовой помощи ПРИОРИТЕТ',
            font_size = 16,
            size_hint = (1, .05),
            background_normal = '',
            background_color = [.61,.61,.61,1],
            pos = (0,scrHeight - scrHeight / 20),
            on_press = self.btn_cpp_press));
        
        fl.add_widget(Image(
            source='logo.png'));

        return fl

    def btn_main_press(self, instance):
        instance.text = 'VVV'
    
    def btn_about_press(self, instance):
        fl_about = FloatLayout(size = (scrWidth,scrHeight))
        instance.text = 'VVV'

    def btn_uslugi_press(self, instance):
        instance.text = 'VVV'

    def btn_zapis_press(self, instance):
        instance.text = 'VVV'

    def btn_contact_press(self, instance):
        instance.text = 'VVV'
    
    def btn_cpp_press(self, instance):
        instance.text = 'VVV'



MyApp().run()
