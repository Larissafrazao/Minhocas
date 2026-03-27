#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity

from code.const import ENTITY_SPEED, WIN_WIDTH


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        # Use o mesmo valor que você usou para a tartaruga (ex: 120, 80).
        novo_tamanho = (80, 80)

        # Redimensiona a imagem (surf)
        self.surf = pygame.transform.scale(self.surf, novo_tamanho)

        # Recria o retângulo (rect) com o novo tamanho, mantendo a posição original
        self.rect = self.surf.get_rect(left=position[0], top=position[1])


    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
