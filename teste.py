import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Truco"


class Sorteador():

    def __init__(self):
        self.naipes = ["ouros","espadas","copas","paus"]
        self.numeros = ["quatro","cinco","seis","sete","dez","onze","doze","um","dois","tres"]
        self.mao_minha = []
        self.mao_computador = []
        self.carta = None

    def sortear(self):
        self.mao_minha = []
        self.mao_computador = []
        self.carta = None
        if sum((len(self.mao_minha),len(self.mao_computador))) == 0:
            while len(self.mao_minha) != 3:
                self.carta = random.choice(self.numeros) + " de " + random.choice(self.naipes)
                self.carta = str(self.carta)
                if not(self.carta in self.mao_minha) and not(self.carta in self.mao_computador):
                    self.mao_minha.append(self.carta)
            while len(self.mao_computador) != 3:
                self.carta = random.choice(self.numeros) + " de " + random.choice(self.naipes)
                self.carta = str(self.carta)
                if not(self.carta in self.mao_computador) and not(self.carta in self.mao_minha):
                    self.mao_computador.append(self.carta)
        self.sorteou = False


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.sorteou = False
        self.sortear = Sorteador()
        self.valor_das_cartas = [('quatro', 1), ('cinco', 2), ('seis', 3), ('sete', 4), ('dez', 5), ('onze', 6), ('doze', 7), ('um', 8), ('dois', 9), ('tres', 10)]
        self.valor_das_cartas = dict(self.valor_das_cartas)
        self.minha_carta = None
        self.carta_computador = None
        
    def on_draw(self):
        arcade.start_render()
        posicao_x = 100
        for i in range(3):
            arcade.draw_text(self.sortear.mao_minha[i], posicao_x, 100, arcade.color.WHITE)
            arcade.draw_text(self.sortear.mao_computador[i], posicao_x, 500, arcade.color.RED)
            posicao_x += 250

    def on_update(self, delta_time):
        if self.sorteou == False:
            self.sortear.sortear()
            self.sorteou = True

    def verificar_maior(self):
        for i in range(len(self.sortear.mao_minha)):
            self.minha_carta = self.sortear.mao_minha[i]
            self.carta_computador = self.sortear.mao_computador[i]

            self.minha_carta = self.minha_carta.split(" ")
            self.minha_carta = self.minha_carta[0]

            self.carta_computador = self.carta_computador.split(" ")
            self.carta_computador = self.carta_computador[0]

            self.minha_escolha = self.valor_das_cartas[self.minha_carta]
            self.escolha_computador = self.valor_das_cartas[self.carta_computador]

            if self.minha_escolha > self.escolha_computador:
                print("Sua carta é maior: ", self.minha_carta)
            elif self.escolha_computador > self.minha_escolha:
                print("A carta do computador é maior: ", self.carta_computador)
            elif self.minha_escolha == self.escolha_computador:
                print("Empachou!")
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.sortear.sortear()
        if key == arcade.key.BACKSPACE:
            MyGame.verificar_maior(self)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()