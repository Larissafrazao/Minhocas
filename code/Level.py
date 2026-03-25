#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from pygame import font, Surface, Rect, Font

from code. Entity import Entity
import pygame
from code.EntityFactory import EntityFactory
from code.const import COLOR_BLACK, WIN_HEIGHT


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000


    def run(self, ):
        pygame.mixer_music.load('./asset/Trilha Sonora.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout/ 1000 : .1f}s', COLOR_BLACK, (10,5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_BLACK, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_BLACK, (10, WIN_HEIGHT - 20))
            pygame.display.flip()



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)



