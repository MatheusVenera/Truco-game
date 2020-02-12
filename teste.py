import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Truco"


class Sorteador():

    def __init__(self):
        self.naipes = ["ouros","espadas","copas","paus"]
        self.numeros = ["4","5","6","7","10","11","12","1","2","3"]
        self.mao_minha = ["algo","teste","algoteste"]
        self.mao_computador = []
        self.total_de_cartas = 0
        self.carta = None

    def sorteador(self):
        i = 0
        while self.total_de_cartas != 6:
            if i%2 == 0:
                self.carta = random.choice(self.numeros) + " de " + random.choice(self.naipes)
                self.carta = str(self.carta)
                if not(self.carta in self.mao_minha) and not(self.carta in self.mao_computador):
                    self.mao_minha.append(self.carta)
                    self.total_de_cartas += 1
            else:
                self.carta = random.choice(self.numeros) + " de " + random.choice(self.naipes)
                self.carta = str(self.carta)
                if not(self.carta in self.mao_computador) and not(self.carta in self.mao_minha):
                    self.mao_computador.append(self.carta)
                    self.total_de_cartas += 1
            i += 1
        print(self.mao_minha)
        print(self.mao_computador)
        print("--------------------------------")

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.sorteou = False
        self.teste = Sorteador()

    def setup(self):
        self.teste = Sorteador()
        
    def on_draw(self):
        arcade.start_render()
        posicao_x = 100
        for i in range(3):
            arcade.draw_text(self.teste.sorteador.mao_minha[i], posicao_x, 100, arcade.color.WHITE)
            posicao_x += 150

    def on_update(self, delta_time):
        if self.sorteou == False:
            self.teste.sorteador()
            self.sorteou = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.teste.sorteador()

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()