# galaxia_2d.py
# import do kivy para a interface grafica

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.clock import Clock
from math import cos, sin, radians

# tela para visualização do modelo 2D
class Galaxia2DWidget(Widget):
    def __init__(self, **kwargs):
        super(Galaxia2DWidget, self).__init__(**kwargs)
        
        # define os planetas, velocidade, distancia, raio e cor
        self.planets = {
            'Tatooine': {'radius': 5, 'distance': 30, 'color': (1, 0.8, 0), 'angle': 5, 'orbit_speed': 10},
            'Coruscant': {'radius': 25, 'distance': 120, 'color': (0, 0.5, 1), 'angle': 0, 'orbit_speed': 6},
            'Endor': {'radius': 18, 'distance': 180, 'color': (0, 0.8, 0), 'angle': 0, 'orbit_speed': 8},
            'Hoth': {'radius': 22, 'distance': 250, 'color': (1, 1, 1), 'angle': 0, 'orbit_speed': 7},
        }

        for planet, info in self.planets.items():
            with self.canvas:
                Color(*info['color'])
                info['ellipse'] = Ellipse(pos=self.calculate_position(planet), size=(info['radius'] * 2, info['radius'] * 2))

        Clock.schedule_interval(self.update, 1 / 60.0)

    # posisão do planeta
    def calculate_position(self, planet):
        info = self.planets[planet]
        angle_rad = radians(info['angle'])
        x = self.width / 2 + info['distance'] * cos(angle_rad)
        y = self.height / 2 + info['distance'] * sin(angle_rad)
        return (x - info['radius'], y - info['radius'])

    # animação dos planetas, atualizando a posição da elipse
    def update(self, dt):
        for planet, info in self.planets.items():
            info['angle'] += dt * info['orbit_speed']  # ajuste velocidade do movimento orbital
            info['ellipse'].pos = self.calculate_position(planet)

# chama a tela para abrir o aplicativo de visualização
class Galaxia2DApp(App):
    def build(self):
        return Galaxia2DWidget()
    
if __name__ == "__main__":
    galaxia_app = Galaxia2DApp()
    galaxia_app.run()