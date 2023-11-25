# quiz.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class QuizScreen(Screen):
    def __init__(self, cadastro_planetas, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.quiz = Quiz(cadastro_planetas)

        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        label_question = Label(text=self.quiz.get_current_question()["pergunta"])
        layout.add_widget(label_question)

        options = ["A", "B", "C"]
        for option in options:
            button = ToggleButton(group='options', text=f'Option {option}', on_press=self.select_option)
            layout.add_widget(button)

        button_next_question = Button(text='Next Question', on_press=self.next_question)
        layout.add_widget(button_next_question)

    def select_option(self, instance):
        selected_option = instance.text[-1].lower()
        self.check_answer(selected_option)

    def check_answer(self, selected_option):
        self.quiz.answer_question(selected_option)

    def next_question(self, instance):
        self.quiz.next_question()
        current_question = self.quiz.get_current_question()
        if current_question:
            label_question = self.children[0].children[0]  # Assuming label is the first child of the first child
            label_question.text = current_question["pergunta"]
        else:
            print(f"Quiz completed! Final score: {self.quiz.get_score()}")


class Quiz:
    def __init__(self, cadastro_planetas):
        self.cadastro_planetas = cadastro_planetas
        self.current_planet = None
        self.current_question_index = 0
        self.score = 0

    def start_quiz(self, planet_name):
        if planet_name in self.cadastro_planetas:
            self.current_planet = planet_name
            self.current_question_index = 0
            self.score = 0
            return True
        else:
            print(f"The planet {planet_name} is not registered.")
            return False

    def get_current_question(self):
        if self.current_planet:
            questions = self.cadastro_planetas[self.current_planet]["perguntas"]
            if 0 <= self.current_question_index < len(questions):
                return questions[self.current_question_index]
        return None

    def answer_question(self, selected_option):
        current_question = self.get_current_question()
        if current_question and selected_option == current_question["resposta_correta"].lower():
            print("Correct! You earned a point.")
            self.score += 1
        else:
            print("Wrong. The correct answer is:", current_question["resposta_correta"])
            print(current_question["explicacao"])

    def next_question(self):
        self.current_question_index += 1

    def get_score(self):
        return self.score
