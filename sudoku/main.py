from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class SudGridLayout(GridLayout):
    pass


class SudokuApp(App):
    
    def build(self):
        return SudGridLayout()

glApp = SudokuApp()
glApp.run()
