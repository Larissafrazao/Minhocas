#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.transform

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        novo_tamanho=(120,80)
        self.surf= pygame.transform.scale(self.surf, novo_tamanho)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def update(self, ):
        pass

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
          self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass
