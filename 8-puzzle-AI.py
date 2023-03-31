from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme
from aigyminsper.search.SearchAlgorithms import BuscaGananciosa
from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import AEstrela
from aigyminsper.search.Graph import State
import time
import csv

class Puzzle8(State):

    def __init__(self, tabuleiro, op):
        self.operator = op  
        self.tabuleiro = tabuleiro
        self.heuristica = 0

    def check_board(self):
        pass

    def sucessors(self):
        sucessores = []
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == 0:
                    if i > 0:
                        tabuleiro = [row[:] for row in self.tabuleiro]
                        tabuleiro[i][j] = tabuleiro[i-1][j]
                        tabuleiro[i-1][j] = 0
                        sucessores.append(Puzzle8(tabuleiro, 'cima'))
                    if i < 2:
                        tabuleiro = [row[:] for row in self.tabuleiro]
                        tabuleiro[i][j] = tabuleiro[i+1][j]
                        tabuleiro[i+1][j] = 0
                        sucessores.append(Puzzle8(tabuleiro, 'baixo'))
                    if j > 0:
                        tabuleiro = [row[:] for row in self.tabuleiro]
                        tabuleiro[i][j] = tabuleiro[i][j-1]
                        tabuleiro[i][j-1] = 0
                        sucessores.append(Puzzle8(tabuleiro, 'esquerda'))
                    if j < 2:
                        tabuleiro = [row[:] for row in self.tabuleiro]
                        tabuleiro[i][j] = tabuleiro[i][j+1]
                        tabuleiro[i][j+1] = 0
                        sucessores.append(Puzzle8(tabuleiro, 'direita'))
        return sucessores

    
    def is_goal(self):
        if self.tabuleiro == [[1, 2, 3],[8, 0, 4],[7, 6, 5]]:
            return True
        else:
            return False
    
    def description(self):
        return 'Puzzle8'
    
    def cost(self):
        return 1
    
    def print(self):
        print(self.tabuleiro)

    def env(self):
        return str(self.tabuleiro) + ' ' + self.operator
    
    def h(self):
        # pega a distancia de manhattan
        distancia = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != 0:
                    if self.tabuleiro[i][j] == 1:
                        distancia += abs(i - 0) + abs(j - 0)
                    elif self.tabuleiro[i][j] == 2:
                        distancia += abs(i - 0) + abs(j - 1)
                    elif self.tabuleiro[i][j] == 3:
                        distancia += abs(i - 0) + abs(j - 2)
                    elif self.tabuleiro[i][j] == 4:
                        distancia += abs(i - 1) + abs(j - 2)
                    elif self.tabuleiro[i][j] == 5:
                        distancia += abs(i - 2) + abs(j - 2)
                    elif self.tabuleiro[i][j] == 6:
                        distancia += abs(i - 2) + abs(j - 1)
                    elif self.tabuleiro[i][j] == 7:
                        distancia += abs(i - 2) + abs(j - 0)
                    elif self.tabuleiro[i][j] == 8:
                        distancia += abs(i - 1) + abs(j - 0)
        return distancia
    
        # heuristica = 0
        # meta = [[1, 2, 3],[8, 0, 4],[7, 6, 5]]
        # for i in range(3):
        #     for j in range(3):
        #         if self.tabuleiro[i][j] != meta[i][j]:
        #             heuristica += 1
        # return heuristica
    

    def acha_posicao_0(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == 0:
                    return i, j


    def verifica_possivel(self):
        if self.acha_posicao_0() == None:
            return False
        contador = 0
        sequencia = []
        for i in range(3):
            sequencia.append(self.tabuleiro[0][i])
        for i in range(1,3):
            sequencia.append(self.tabuleiro[i][2])
        for i in range(1,3):
            sequencia.append(self.tabuleiro[2][2-i])
        sequencia.append(self.tabuleiro[1][0])
        sequencia.append(self.tabuleiro[1][1])
        sequencia_copia = sequencia[:]
        for i in sequencia:
            sequencia_copia.remove(i)
            for j in sequencia_copia:
                if i > j and j != 0 and i != 0:
                    contador += 1
        if contador % 2 == 0:
            return True
        else:
            return False
        
    def show_path(self):
        algorithm = AEstrela()
        if self.is_goal() == True:
            return ""
        if self.verifica_possivel() == False or self.is_goal() == True:
            return 'Nao tem solucao'
        result = algorithm.search(self, trace=True)
        if result != None:
            return result.show_path()
        else:
            return 'Nao tem solucao'

    
import pygame
import sys
import numpy as np

pygame.init()

# Definindo cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
cinza = (128, 128, 128)

# Definindo tamanho da tela
tela_largura = 600
tela_altura = 600

# Definindo tamanho do tabuleiro
tabuleiro_largura = 300
tabuleiro_altura = 300

# Definindo tamanho dos quadrados
quadrado_largura = 100
quadrado_altura = 100

# Definindo tamanho dos botoes
botao_largura = 100
botao_altura = 50

# Definindo tamanho da fonte
fonte = pygame.font.SysFont('Calibri', 25, True, False)

# o codigo tem o intuito de representar a solucao do puzzle 8

# Definindo a tela
tela = pygame.display.set_mode([tela_largura, tela_altura])
pygame.display.set_caption('Puzzle 8')

# Definindo o tabuleiro
tabuleiro = pygame.Surface([tabuleiro_largura, tabuleiro_altura])
tabuleiro.fill(branco)
tabuleiro_pos = [150, 150]

# Definindo os botoes
botao = pygame.Surface([botao_largura, botao_altura])
botao.fill(cinza)
botao_pos = [50, 50]

# Definindo o texto do botao
texto = fonte.render('Iniciar', True, preto)
texto_pos = [botao_pos[0] + 10, botao_pos[1] + 10]

# vamos pegar as instrucoes do puzzle 8 dps de solucionado

# tabuleiro = [[3, 0, 2],[1, 8, 4],[7, 6, 5]]
# tabuleiro = [[8,3,6],[7,5,4],[1,0,2]]

run = True
tabuleiro = [[0,3,2],[1,8,4],[5,6,7]]
state = Puzzle8(tabuleiro, 'inicio')
if state.verifica_possivel() == False:
    print('Estado impossivel')
    run = False

if run == True:
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state, trace=True)
    tf = time.time()
    if result != None:
        print(result.show_path())
        lista_instrucoes = result.show_path().split(';')
        # remove os espaços em branco
        lista_instrucoes = [x.strip() for x in lista_instrucoes]
        lista_instrucoes.pop(0)

        # exemplo de lista de instrucoes: inicio ; direita ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+ str(result.g))


# Depois de pegar as instrucoes, vamos criar uma lista com as posicoes dos quadrados
# para que possamos fazer a animacao
def cria_lista_posicoes():
    lista_posicoes = []
    for i in range(3):
        for j in range(3):
            lista_posicoes.append([i, j])
    return lista_posicoes

# vamos desenhar nosso tabuleiro
def desenha_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            quadrado = pygame.Surface([quadrado_largura, quadrado_altura])
            quadrado.fill(branco)
            quadrado_pos = [152 + i * quadrado_largura, 115 + j * quadrado_altura]
            tela.blit(quadrado, quadrado_pos)
            if tabuleiro[j][i] != 0:
                texto = fonte.render(str(tabuleiro[j][i]), True, preto)
                texto_pos = [quadrado_pos[0] + 30, quadrado_pos[1] + 30]
                tela.blit(texto, texto_pos)

# vamos desenhar nosso botao
def desenha_botao():
    tela.blit(botao, botao_pos)
    tela.blit(texto, texto_pos)

def pega_posicao_zero():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return [i, j]

# vamos desenhar nosso tabuleiro dps de solucionado
def desenha_tabuleiro_movendo():
    # Lembrando temos que ver qual instrucao vamos fazer
    # e depois fazer a animacao
    posicao_zero = pega_posicao_zero()
    if lista_instrucoes[0] == 'cima':
        # troca o zero com o de cima
        tabuleiro[posicao_zero[0]][posicao_zero[1]] = tabuleiro[posicao_zero[0] - 1][posicao_zero[1]]
        tabuleiro[posicao_zero[0] - 1][posicao_zero[1]] = 0
        # vamos desenhar o tabuleiro
        desenha_tabuleiro(tabuleiro)
        # vamos desenhar o botao
        lista_instrucoes.pop(0)
    elif lista_instrucoes[0] == 'baixo':
        # troca o zero com o de baixo
        tabuleiro[posicao_zero[0]][posicao_zero[1]] = tabuleiro[posicao_zero[0] + 1][posicao_zero[1]]
        tabuleiro[posicao_zero[0] + 1][posicao_zero[1]] = 0
        # vamos desenhar o tabuleiro
        desenha_tabuleiro(tabuleiro)
        # vamos desenhar o botao
        lista_instrucoes.pop(0)
    elif lista_instrucoes[0] == 'esquerda':
        # troca o zero com o da esquerda
        tabuleiro[posicao_zero[0]][posicao_zero[1]] = tabuleiro[posicao_zero[0]][posicao_zero[1] - 1]
        tabuleiro[posicao_zero[0]][posicao_zero[1] - 1] = 0
        # vamos desenhar o tabuleiro
        desenha_tabuleiro(tabuleiro)
        # vamos desenhar o botao
        lista_instrucoes.pop(0)
    elif lista_instrucoes[0] == 'direita':
        # troca o zero com o da direita
        tabuleiro[posicao_zero[0]][posicao_zero[1]] = tabuleiro[posicao_zero[0]][posicao_zero[1] + 1]
        tabuleiro[posicao_zero[0]][posicao_zero[1] + 1] = 0
        # vamos desenhar o tabuleiro
        desenha_tabuleiro(tabuleiro)
        # vamos desenhar o botao
        lista_instrucoes.pop(0)

# botao_gerar
botao_gerar = pygame.Rect(0, 0, 200, 50)
largura_tela = 600
altura_tela = 600
botao_gerar.center = (largura_tela/2, altura_tela - 50)
desenha_tabuleiro(tabuleiro)
# vamos fazer nosso loop principal
while True:
    # vamos fazer um loop para verificar os eventos
    for event in pygame.event.get():
        # vamos verificar se o usuario clicou no botao de fechar
        if event.type == pygame.QUIT:
            # vamos fechar o jogo
            pygame.quit()
            sys.exit()
        # vamos verificar se o usuario clicou no botao de gerar instrucoes
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vamos verificar se o usuario clicou no botao
            if botao_gerar.collidepoint(event.pos):
                while True:
                    desenha_tabuleiro_movendo()
                    if len(lista_instrucoes) == 0:
                        break
                    pygame.display.flip()
                    pygame.time.wait(600)

    # vamos desenhar o botao de gerar instrucoes
    pygame.draw.rect(tela, azul, botao_gerar)
    # vamos desenhar o texto do botao
    texto_botao_gerar = fonte.render('Gerar instruções', True, branco)
    texto_botao_gerar_rect = texto_botao_gerar.get_rect()
    texto_botao_gerar_rect.center = botao_gerar.center
    tela.blit(texto_botao_gerar, texto_botao_gerar_rect)
    # vamos atualizar a tela
    pygame.display.flip()


                