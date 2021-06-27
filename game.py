import pygame
from gameObject import gameObject
from player import player
from enemy import enemy

class Game:

    def __init__(self):

        self.width = 1000
        self.height = 500
        self.white_color = (255,255,255)

        self.clock = pygame.time.Clock()

        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.background = gameObject(0,0, self.width, self.height, 'assets/background.png')

        self.treasure = gameObject(465, 20, 50, 50,'assets/treasure.png')

        self.level = 1.0

        self.reset_map()

    def reset_map(self):
        self.player = player(450, 430, 50, 50, 'assets/player.png', .25)

        speed = .15 + (self.level * .05)

        if self.level >= 4.0:
            self.enemies = [
                enemy(0, 100, 50, 50, 'assets/enemy.png', speed),
                enemy(0, 350, 50, 50, 'assets/enemy.png', speed),
                enemy(800, 250, 50, 50, 'assets/enemy.png', speed), 
            ]

        elif self.level >= 2.0:
            self.enemies = [
                enemy(0, 350, 50, 50, 'assets/enemy.png', speed),
                enemy(800, 250, 50, 50, 'assets/enemy.png', speed), 
            ]

        else:
             self.enemies = [
                enemy(800, 250, 50, 50, 'assets/enemy.png', speed), 
            ]


            
       

    def draw_objects(self):

        self.game_window.fill(self.white_color)
        self.game_window.blit(self.background.image,(self.background.x,self.background.y))
        self.game_window.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
        self.game_window.blit(self.player.image,(self.player.x,self.player.y))

        for enemy in self.enemies: 
            self.game_window.blit(enemy.image,(enemy.x,enemy.y))
        
        pygame.display.update()

    def move_objects(self, player_direction):
         self.player.move(player_direction, self.height)
         for self.enemy in self.enemies:
            self.enemy.move(self.width)

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
                self.level += .5
                return True
        return False     

    def run_game_loop(self):
        player_direction = 0

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            player_direction = 0

            self.move_objects(player_direction)

            self.draw_objects()

            #if self.detect_collision(self.player, self.enemy):
               ### return 
            if self.check_if_collided():
                self.reset_map()

        self.clock.tick(60)



