import random
import arcade
import os

LARGURA_TELA = 926
ALTURA_TELA = 427
TITULO = "Truco"

class Carta(arcade.Sprite):

    def carta(self):
        self.center_x = None
        self.center_y = None 


class Sorteador():

    def __init__(self):
        self.naipes = ["ouro","espada","copa","pau"]
        self.numeros = ["quatro","cinco","seis","sete","dez","onze","doze","um","dois","tres"]
        self.mao_minha = []
        self.mao_computador = []
        self.carta = None
        self.manilha = None
        self.carta_manilha = None
        self.valor_dos_naipes = [('ouros', 1), ('espadas', 2), ('copas', 3), ('paus', 4)]
        self.valor_dos_naipes = dict(self.valor_dos_naipes)
        self.valor_das_cartas = [('quatro', 1), ('cinco', 2), ('seis', 3), ('sete', 4), ('dez', 5), ('onze', 6), ('doze', 7), ('um', 8), ('dois', 9), ('tres', 10)]
        self.valor_das_cartas = dict(self.valor_das_cartas)
        self.valor_das_cartas_reverso = [(1, 'quatro'), (2, 'cinco'), (3, 'seis'), (4, 'sete'), (5, 'dez'), (6, 'onze'), (7, 'doze'), (8, 'um'), (9, 'dois'), (10, 'tres')]
        self.valor_das_cartas_reverso = dict(self.valor_das_cartas_reverso)

    def sortear(self):
        self.mao_minha = []
        self.mao_computador = []
        self.carta = None
        self.manilha = None
        self.carta_manilha = None
        if sum((len(self.mao_minha),len(self.mao_computador))) == 0:
            while len(self.mao_minha) != 3:
                self.carta = random.choice(self.numeros) + "_" + random.choice(self.naipes) + ".png"
                self.carta = str(self.carta)
                if not(self.carta in self.mao_minha) and not(self.carta in self.mao_computador):
                    self.mao_minha.append(self.carta)
            while len(self.mao_computador) != 3:
                self.carta = random.choice(self.numeros) + "_" + random.choice(self.naipes) + ".png"
                self.carta = str(self.carta)
                if not(self.carta in self.mao_computador) and not(self.carta in self.mao_minha):
                    self.mao_computador.append(self.carta)
        while True:
            self.manilha = random.choice(self.numeros) + "_" + random.choice(self.naipes) + ".png"
            self.manilha = str(self.manilha)
            if not(self.manilha in self.mao_computador) and not(self.manilha in self.mao_minha):
                self.carta_manilha = self.manilha
                self.manilha = self.manilha.split("_")
                self.manilha = self.manilha[0]
                self.manilha = self.valor_das_cartas[self.manilha]
                if self.manilha == 10:
                    self.manilha = 1
                    break
                elif self.manilha < 10:
                    self.manilha += 1
                    break
        self.manilha = self.carta_manilha
        self.sorteou = False


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(arcade.color.AMAZON)
        self.fundo = None
        self.lista_minhas_cartas = None
        self.lista_cartas_adversario = None
        self.minha_carta = None
        self.carta_adversario = None
        self.contagem_regressiva = None
        self.tempo = None
        self.vez = None
        self.sortear = None
        self.baralho = None

    def setup(self):
        self.fundo = arcade.load_texture("images/fundo.png")
        self.sorteou = False
        self.sortear = Sorteador()
        self.valor_dos_naipes = [('ouro', 1), ('espada', 2), ('copa', 3), ('pau', 4)]
        self.valor_dos_naipes = dict(self.valor_dos_naipes)
        self.valor_das_cartas = [('quatro', 1), ('cinco', 2), ('seis', 3), ('sete', 4), ('dez', 5), ('onze', 6), ('doze', 7), ('um', 8), ('dois', 9), ('tres', 10)]
        self.valor_das_cartas = dict(self.valor_das_cartas)

        self.lista_minhas_cartas = arcade.SpriteList()
        self.lista_cartas_adversario = arcade.SpriteList()

        self.tempo = 0
        posicao_x = 400
        for i in range(3):
            self.carta_adversario = arcade.Sprite("images/carta_costas.png", 1/3)
            self.carta_adversario.center_x = posicao_x
            self.carta_adversario.center_y = 275
            self.lista_cartas_adversario.append(self.carta_adversario)
            posicao_x += 50

        self.contagem_regressiva = 30
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(LARGURA_TELA // 2, ALTURA_TELA // 2,LARGURA_TELA, ALTURA_TELA, self.fundo)
        arcade.draw_text(("Tempo: " + str(self.contagem_regressiva) + " seg"), 805, 5, arcade.color.WHITE, 14, bold=True)
        arcade.draw_text("Você", 40, 35, arcade.color.WHITE, 14, bold=True)
        arcade.draw_text("Adversário", 40, 10, arcade.color.WHITE, 14, bold=True)
        if self.sortear.mao_minha != []:
            self.minha_carta = arcade.Sprite(("images/" + self.sortear.mao_minha[0]), 1/2)
            self.minha_carta.center_x = 375
            self.minha_carta.center_y = 100
            self.lista_minhas_cartas.append(self.minha_carta)

            self.minha_carta = arcade.Sprite(("images/" + self.sortear.mao_minha[1]), 1/2)
            self.minha_carta.center_x = 455
            self.minha_carta.center_y = 100
            self.lista_minhas_cartas.append(self.minha_carta)

            self.minha_carta = arcade.Sprite(("images/" + self.sortear.mao_minha[2]), 1/2)
            self.minha_carta.center_x = 535
            self.minha_carta.center_y = 100
            self.lista_minhas_cartas.append(self.minha_carta)
            self.lista_minhas_cartas.draw()
        if self.sortear.mao_computador != []:
            self.lista_cartas_adversario.draw()
        if self.sortear.carta_manilha != None:
            self.sortear.carta_manilha = arcade.Sprite(("images/" + self.sortear.manilha), 0.7)
            self.sortear.carta_manilha.center_x = 250
            self.sortear.carta_manilha.center_y = 200
            self.sortear.carta_manilha.angle = -90
            self.sortear.carta_manilha.draw()

        self.baralho = arcade.Sprite("images/baralho.png", 0.65)
        self.baralho.center_x = 225
        self.baralho.center_y = 200
        self.baralho.draw()
            
        if self.vez == None:
            arcade.draw_circle_filled(25, 42, 6, arcade.color.GRAY)
            arcade.draw_circle_filled(25, 17, 6, arcade.color.GRAY)
        if self.vez == "Jogador":
            arcade.draw_circle_filled(25, 42, 6, arcade.color.GREEN)
            arcade.draw_circle_filled(25, 17, 6, arcade.color.GRAY)
        if self.vez == "Adversário":
            arcade.draw_circle_filled(25, 42, 6, arcade.color.GRAY)
            arcade.draw_circle_filled(25, 17, 6, arcade.color.GREEN)

    def on_update(self, delta_time):
        self.tempo += 1
        if self.tempo == 60:
            self.tempo = 0
            if self.contagem_regressiva > 0 and self.vez == "Jogador":
                self.contagem_regressiva -= 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.vez = random.choice(["Jogador", "Adversário"])
            self.sortear.sortear()
            self.sorteou = True

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if (x > self.lista_minhas_cartas[0].left) and (x < self.lista_minhas_cartas[0].right) and (y > self.lista_minhas_cartas[0].bottom) and (y < self.lista_minhas_cartas[0].top):
                print("batata")

def main():
    game = MyGame(LARGURA_TELA, ALTURA_TELA, TITULO)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()