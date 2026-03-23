#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from code.const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        # 1. Carrega a imagem original
        self.surf = pygame.image.load("asset/1_game_background.png").convert()

        # 2. Pega as dimensões da SUA janela
        largura_janela = self.window.get_width()
        altura_janela = self.window.get_height()

        # 3. REDIMENSIONA a imagem para caber na janela
        self.surf = pygame.transform.scale(self.surf, (largura_janela, altura_janela))

        # 4. Cria o retângulo baseado na imagem já redimensionada
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.init()
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
             self.window.blit(source=self.surf, dest=self.rect)
             self.menu_text(80, 'OCEAN COLLEAGUES',(COLOR_BLACK), ((WIN_WIDTH/2), 100))

             for i in range(len(MENU_OPTION)):
              self.menu_text(30, (MENU_OPTION[i]), (COLOR_BLACK), ((WIN_WIDTH / 2), 200 + 30 * i ))


             pygame.display.flip()
             # check for all events
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit() #Close window
                     quit() #and pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.SysFont('Lucida Sans Typewhiter', size=text_size)
        text_surf: Surface = font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)



