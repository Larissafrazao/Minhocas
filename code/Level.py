#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame
from pygame import Surface, Rect, Font
from code.Entity import Entity
from code.EntityFactory import EntityFactory
# Certifique-se de importar WIN_WIDTH para o nascimento dos inimigos
from code.const import COLOR_BLACK, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.Player import Player
from code.Enemy import Enemy


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        # Timeout agora funciona como sua "pontuação/vida"
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load('./asset/Trilha Sonora.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        player_lives = 3
        invisibility_timer = 0

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()

            # 1. MOVIMENTAÇÃO E DESENHO
            for ent in self.entity_list:
                if isinstance(ent, Player) and current_time < invisibility_timer:
                    if (current_time // 100) % 2 == 0:
                        continue
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # 2. LÓGICA DE COLISÃO (O que você queria adicionar)
            # Vamos pegar os jogadores e inimigos da lista
            players = [ent for ent in self.entity_list if isinstance(ent, Player)]
            enemies = [ent for ent in self.entity_list if isinstance(ent, Enemy)]

            for p in players:
                for e in enemies:
                    if p.rect.colliderect(e.rect):
                        if current_time > invisibility_timer:
                            player_lives -= 1
                            invisibility_timer = current_time + 2000
                            if player_lives > 0:
                                # ALERTA: Flash vermelho na tela e remove o inimigo
                                self.window.fill((255, 0, 0))
                                if e in self.entity_list:
                                    self.entity_list.remove(e)
                                print(f"Alerta! Vidas restantes: {player_lives}")
                            else:
                                # TERCEIRA VEZ: Jogador desaparece e perde
                                if p in self.entity_list:
                                    self.entity_list.remove(p)
                                print("Game Over: A tartaruga sumiu!")
                                return


            # 3. TRATAMENTO DE EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3', 'Enemy4'))
                    novo_inimigo = EntityFactory.get_entity(choice)

                    # CORREÇÃO: Faz nascer em altura aleatória e na borda direita
                    y_pos = random.randint(0, WIN_HEIGHT - 80)
                    novo_inimigo.rect.topleft = (WIN_WIDTH, y_pos)

                    self.entity_list.append(novo_inimigo)

            # 4. LIMPEZA E UI
            # Remove quem saiu da tela
            self.entity_list = [ent for ent in self.entity_list if ent.rect.right > 0]

            # Texto na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', COLOR_BLACK, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_BLACK, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_BLACK, (10, WIN_HEIGHT - 20))

            # Se o tempo acabar, Game Over
            if self.timeout <= 0:
                return  # Encerra o level

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)