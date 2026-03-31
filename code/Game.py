#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect

from code.Level import Level
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # 1. Verifica se o usuário escolheu jogar (1P, 2P Co-op ou 2P Comp)
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                fases = ['Fase 1', 'Fase 2']
                fase_atual = 0

                while fase_atual < len(fases):
                    # Criamos a fase atual baseada na lista
                    level = Level(self.window, fases[fase_atual], menu_return)

                    # Rodamos a fase e guardamos o retorno (NEXT_LEVEL ou GAME_OVER)
                    status = level.run()

                    if status == "NEXT_LEVEL":
                        fase_atual += 1  # Vai para a próxima fase da lista
                    else:
                        break  # Se perdeu ou saiu, volta para o Menu principal

            # 2. Verifica se o usuário escolheu sair
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
