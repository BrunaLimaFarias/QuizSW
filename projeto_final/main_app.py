# main_app.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label 
from kivy.uix.button import Button
from quiz import QuizScreen
from projeto_star_wars import cadastrar_planeta, cadastro_planetas
from galaxia_2d import Galaxia2DWidget




class MenuScreen(BoxLayout):
    pass

class CadastroPlanetaScreen(BoxLayout):

    def cadastrar_planeta(self):
        nome_planeta = self.nome_planeta_input.text.strip()
        personagens = self.personagens_input.text.strip()
        eventos = self.eventos_input.text.strip()

        cadastrar_planeta(nome_planeta, personagens, eventos)

        # limpa apos cadastrar o planeta
        self.nome_planeta_input.text = ''
        self.personagens_input.text = ''
        self.eventos_input.text = ''

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.quiz = QuizScreen(cadastro_planetas={})

        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.label_question = Label(text="")
        self.layout.add_widget(self.label_question)

        self.option_a = "Opção A"
        self.option_b = "Opção B"
        self.option_c = "Opção C"

        self.layout.add_widget(ToggleButton(group='options', text=self.option_a, on_press=self.select_option))
        self.layout.add_widget(ToggleButton(group='options', text=self.option_b, on_press=self.select_option))
        self.layout.add_widget(ToggleButton(group='options', text=self.option_c, on_press=self.select_option))

        self.button_next_question = Button(text='Próxima Pergunta', on_press=self.next_question)
        self.layout.add_widget(self.button_next_question)

    def select_option(self, instance):
        selected_option = instance.text[-1].lower()
        self.check_answer(selected_option)

    def check_answer(self, selected_option):
        self.quiz.answer_question(selected_option)

    def next_question(self, instance):
        self.quiz.next_question()
        current_question = self.quiz.get_current_question()
        if current_question:
            self.label_question.text = current_question["pergunta"]
        else:
            print(f"Quiz concluído! Pontuação final: {self.quiz.get_score()}")


class Galaxia2DScreen(BoxLayout):
    def build(self):
        return Galaxia2DWidget().run
    

class StarWarsQuizApp(App):
    def build(self):
        sm = ScreenManager()

        menu_screen = Screen(name='menu')
        menu_screen.add_widget(MenuScreen())
        sm.add_widget(menu_screen)

        cadastro_planeta_screen = Screen(name='cadastro_planeta')
        cadastro_planeta_screen.add_widget(CadastroPlanetaScreen())
        sm.add_widget(cadastro_planeta_screen)


        
        

        galaxia_2d_screen = Screen(name='galaxia_2d')
        galaxia_2d_screen.add_widget(Galaxia2DScreen())
        sm.add_widget(galaxia_2d_screen)

        return sm


if __name__ == "__main__":
    StarWarsQuizApp().run()