import settings
import pygame
import area 
import dicts
import os 
import bullet
import music
import random
# from bullet import blit_bullet_count
list_letters = ["q", "w", "e", "r", "t", "y", "u","x", "c", "f"]
list_cor_x = [150, 200, 220, 300, 350, 370]
list_cor_y = [300, 350, 440, 580, 620, 700]
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
flag_bullet_die = False
flag_level_3 = False
letter = ""
# font = pygame.font.SysFont("kokila", 20)
# follow = font.render("", 1, (0,0,0))

# flag_pistol_shoot = False
# flag_gravity_animation = False
bullet1 = bullet.Bullet(
                    x = 0,
                    y = 0,
                    width= 0,
                    height= 0,
                    name_image= None
                )
        
class Sprite(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.FLAG_GRAVITY_ANIMATION = False
        self.COUNT_BULLET = 0
        self.LIST_BULLET = []
        self.STEP = 2
        self.GRAVITY = 6
        self.ACTIVE_GRAVITY = True
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.COUNT_JUMP = 0
        self.JUMP = False
        self.KEY_PRESSED = False
        self.OPEN_DOOR = False
        self.MASK_ON = False
        self.INJURED = False
        self.EXIT_DOOR = False
        self.MEDIC_MOVE_RIGHT = False
        self.MEDIC_MOVE_LEFT = False
        self.MOVE_BULLET = False
        self.DIRECTION = "R"
        self.SPEED_ANIMATION = 0
        self.COUNT_IMG = 3
        self.COUNT_FIRE_POSITION = 0
        self.EXTING_ON = False
        self.BLIT_FIRE_1 = True
        self.BLIT_FIRE_2 = True
        self.BLIT_FIRE_3 = True
        self.BLIT_FIRE_4 = True
        self.BLIT_FIRE_5 = True
        self.BLIT_FIRE_6 = True
        self.BLIT_FIRE_7 = True
        self.SCENE4 = False
        self.COUNT_FIRE_POSITION = 0
        self.EXTING_ON = False
        self.BLIT_FIRE_1 = True
        self.BLIT_FIRE_2 = True
        self.BLIT_FIRE_3 = True
        self.BLIT_FIRE_4 = True
        self.BLIT_FIRE_5 = True
        self.BLIT_FIRE_6 = True
        self.BLIT_FIRE_7 = True
        self.HOLE_COUNT = True
        self.TIME_HOLE_BLIT
    def move_sprite(self):
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                self.DIRECTION = 'R'
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                    # walk_sound.WALK_SOUND.play()
                    # self.RECT.x = self.RECT.x + self.STEP
                    # self.RECT.x = self.RECT.x + self.STEP
                # print(self.ACTIVE_GRAVITY, self.JUMP)
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    # print(1111111)
                    # print("anim_right")
                    self.animation(folder= "player",count_while=5,last_img= 5, first_img=1) 
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
               
                self.DIRECTION = 'L'
                if self.CAN_MOVE_LEFT == True:      
                    self.X -= self.STEP      
                    # self.can_move_left(list_rect)
                    # self.RECT.x = self.RECT.x - self.STEP
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    # print("anim_left")
                    self.animation(folder= "player",count_while=5,last_img= 5, first_img=1)
                    # walk_sound.WALK_SOUND.play()
                    # self.RECT.x = self.RECT.x - self.STEP 
            elif self.ACTIVE_GRAVITY == False:
                self.NAME_IMAGE = "game2/images/player/1.png"
                self.direction()
            
     #
    def jump(self, list_rect):
        # print(self.JUMP)
        event = pygame.key.get_pressed()
        #
        if event[pygame.K_UP] and self.KEY_PRESSED == False:
            self.KEY_PRESSED = True
            # print(1111111111)
        # if self.KEY_PRESSED == False:
        #     print(self.COUNT_JUMP)
        # if self.COUNT_JUMP > 30:
        #     print(1111111111)
        # print(self.COUNT_JUMP)
    
        if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
            if self.COUNT_JUMP <= 25:
                self.NAME_IMAGE = "game2/images/player/6.png"
            else: 
                self.NAME_IMAGE = "game2/images/player/8.png"
            # self.animation(folder= "player",count_while=1,last_img= 6, first_img=4)
            self.direction()
            # print(self.COUNT_JUMP)
            # print(self.KEY_PRESSED)
            self.JUMP = True
            self.COUNT_JUMP += 1
            # self.RECT.y -= 11
            self.Y -= 11
            self.can_move_up(list_rect)
            # print(self.COUNT_JUMP)
        if self.COUNT_JUMP > 30 and self.COUNT_JUMP <= 35:
            # print(1111111111)
            # print(1111111111111111111111111111111)
            self.COUNT_JUMP += 1
            # print(self.COUNT_JUMP)
            self.JUMP = False 
            # if self.FLAG_GRAVITY_ANIMATION == True:
            self.NAME_IMAGE = "game2/images/player/8.png"
            self.direction()
        # if self.COUNT_JUMP > 35:
        #     # self.JUMP = False 
        #     self.NAME_IMAGE = "game2/images/player/6.png"
        #     self.direction()
            
            # self.KEY_PRESSED = False
            # self.COUNT_JUMP = 0
            
    def medic_move(self):
        if self.MEDIC_MOVE_LEFT == True:
                self.DIRECTION = 'L'
                self.X -= 2
                self.DIRECTION = 'R'
                self.animation(folder= "medic",count_while=5,last_img= 5, first_img=1) 
        if self.MEDIC_MOVE_RIGHT == True:
            # print(1111111111)
                self.DIRECTION = 'R'
                self.X += 2
                self.DIRECTION = 'L'
                self.animation(folder= "medic",count_while=5,last_img= 5, first_img=1) 
        if self.X + self.WIDTH < 0:
            self.MEDIC_MOVE_LEFT = False
        if self.X > 800:
            self.MEDIC_MOVE_RIGHT = False
    def medic_move_screen(self):
        if self.X < 0:
            # print(1)
            self.X += 5
            self.DIRECTION = 'L'
        if self.X > 800:
            # print(1111111111)
            self.MEDIC_MOVE_LEFT = True
            self.DIRECTION = 'R'
            
        

    def gravity(self, list_rect, sprite = None):
        # global flag_gravity_animation
       
        self.can_move_down(list_rect, sprite)
        if self.ACTIVE_GRAVITY:
            self.Y += self.GRAVITY
            if sprite != None and self.JUMP == False and (self.COUNT_JUMP > 35 or self.COUNT_JUMP == 0):

                # print(11111111111)
                self.NAME_IMAGE = "game2/images/player/6.png"
                # self.load_image()
                self.direction()
                # flag_gravity_animation = True
            # flag_gravity_animation = False
            # self.animation(folder= "player",count_while=3,last_img= 3, first_img=1)
            
        
    def can_move_right(self, list_rect):
        for block in list_rect:
            if self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                # print(block.HEIGHT, "23e43ed3sede")
                if self.X + self.WIDTH <= block.X + self.STEP and self.X + self.WIDTH >= block.X:
                    self.CAN_MOVE_RIGHT = False
                    self.X -= self.STEP
                    # self.RECT.x -= 3
                    break         
                else:
                    self.CAN_MOVE_RIGHT = True
            else:
                    self.CAN_MOVE_RIGHT = True
    def can_move_left(self, list_rect):
        for block in list_rect:
            if  self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                # print(block.HEIGHT, "23e43ed3sede")
                if self.X >= block.X - self.STEP and self.X <= block.X + block.WIDTH:
                        self.CAN_MOVE_LEFT = False
                        self.X += self.STEP
                        # self.RECT.x += 3
                        break
                else:
                    self.CAN_MOVE_LEFT = True
            else:
                self.CAN_MOVE_LEFT = True
    def can_move_down(self, list_rect, sprite = None):
        
        for block in list_rect:
            if self.X <= block.X + block.WIDTH and self.X + self.WIDTH >= block.X:
                # print(self.Y + self.HEIGHT, block.Y, self.Y)
                if self.Y + self.HEIGHT >= block.Y and self.Y + self.HEIGHT <= block.Y + self.GRAVITY:
                    
                    # print(self.Y + self.HEIGHT, block.Y, self.Y)
                    # print(self.Y + self.HEIGHT, block.Y)
                    # self.RECT.Y = block.Y - self.RECT.height - 1
                # if block.Y + block.height > self.RECT.Y:
                    # block.NAME_IMAGE = "game2/images/1.jpg"
                    # block.load_image()
                    # if sprite:
                    #     print(99999999999999)
                    self.ACTIVE_GRAVITY = False
                    self.COUNT_JUMP = 0
                    self.KEY_PRESSED = False
                    self.JUMP = False
                    self.Y = block.Y - self.HEIGHT
                      
                    break
                else:
                    self.ACTIVE_GRAVITY = True
            else:
                    self.ACTIVE_GRAVITY = True
                

    def can_move_up(self, list_rect):
        for block in list_rect:
            if self.Y <= block.Y + block.HEIGHT and self.Y + self.HEIGHT >= block.Y + block.HEIGHT:
                if self.X + 50>= block.X and self.X + self.WIDTH - 50 <= block.X + block.WIDTH:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
                    self.JUMP = False
            # if block.x <= self.X + self.WIDTH and block.x + block.width >= self.X + self.WIDTH:
            #     if block.Y + block.height > self.Y:
            #         self.COUNT_JUMP = 41
            #         self.ACTIVE_GRAVITY = True
    def draw_text(self, win, key):
        font = pygame.font.SysFont("kokila", 20)
        follow = font.render(f"Натисніть {key} щоб взаємодіяти з предметами!", 1, (0,0,0))
        win.blit(follow, (100, 200))

    def lever_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X <= settings.lever.X + settings.lever.WIDTH and self.X + self.WIDTH >= settings.lever.X:
           # print(222222222222222)
           if self.Y + 30 >= settings.lever.Y and self.Y + self.HEIGHT <= settings.lever.Y + settings.lever.HEIGHT + 30:
               self.draw_text(win, "E")
               if event[pygame.K_e]:
               #    print(22222)
                  self.OPEN_DOOR = True

    def mask_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= mask.X + mask.WIDTH + 20 and self.X + 20 >= mask.X:
            # print(5555)
            # print(self.RECT.y  + 21 >= mask.RECT.y, self.RECT.y + 21, mask.RECT.y)
            if self.Y + 21 >= mask.Y and self.Y + self.HEIGHT <= mask.Y + mask.HEIGHT + 20:
                self.draw_text(win, "R")
                # print(2222223333)
                if event[pygame.K_r]:
                    # print(222222)'
                    self.MASK_ON = True
                    self.NAME_IMAGE = "game2/images/sprite_with_injured.png"
                    mask.NAME_IMAGE = None
                    self.load_image()

    def injured_collide(self):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= settings.injured.X + settings.injured.WIDTH + 20 and self.X + 20 >= settings.injured.X:
            if self.Y + 21 >= settings.injured.Y and self.Y + self.HEIGHT <= settings.injured.Y + settings.injured.HEIGHT + 20:
                self.draw_text(win, "F")
                if event[pygame.K_f]:
                    self.NAME_IMAGE = "game2/images/sprite_with_injured.png"
                    self.load_image()
                    self.INJURED = True
    def position(self):
        event = pygame.key.get_pressed()
        if event[pygame.K_t]:
            print(self.X)
    def door_collide(self, door):
        if not self.OPEN_DOOR:
            if self.Y >= door.Y and self.Y + self.HEIGHT - 10 <= door.Y + door.HEIGHT:
                # print(11111)
                if self.X + self.WIDTH >= door.X:
                    # print(5555)
                    self.CAN_MOVE_RIGHT = False
                    self.X -= 3
                    self.X -= 3
        if self.OPEN_DOOR:
            # print(1111)
            door.NAME_IMAGE = None
            door.IMAGE = None
    # def open_door(self):
    #     if self.OPEN_DOOR:
    #         print(1111)
    #         self.NAME_IMAGE = None
    # def bullet(self):
    #     global flag_bullet_die
    #     global flag_pistol_shoot
    #     global move_bullet
    #     for block in area.list_rect:
    #         if block.X <= bullet.X + bullet.WIDTH and block.X + block.WIDTH > bullet.X + bullet.WIDTH:
    #             if bullet.HEIGHT > block.Y - bullet.HEIGHT and bullet.Y + bullet.HEIGHT < block.y + bullet.HEIGHT + block.HEIGHT:
    #                 self.MOVE_BULLET = False
    #                 break
    #             else:
    #                 self.MOVE_BULLET = True
    #         else:
    #             self.MOVE_BULLET = True
    #     if self.MOVE_BULLET:
    #         # print("erhbhUIWRHOIQHOUE")
    #         if self.X <= bullet.X + bullet.WIDTH and self.X + self.WIDTH >= bullet.X:
    #         # print(222222222222222)
    #             if self.Y + 30 >= bullet.Y and self.Y + self.HEIGHT <= bullet.Y + bullet.HEIGHT + 30:
    #                 # print("ulygiguoviuo")
    #                     die_bullet_version.DIE_BULLET_VERSION.play()
    #                     self.MOVE_BULLET = False
    #                     flag_bullet_die = True
    #     if bullet.X <= 0:
    #         self.MOVE_BULLET = False
    #     if bullet.X >= 800:
    #         self.MOVE_BULLET = False
        
        
    #     if self.MOVE_BULLET:
    #         # for i in range(1):
    #         if move_bullet == 0:
    #             pistol_shoot.PISTOL_SHOOT.play()
    #             move_bullet += 1
    #         if bullet.X >= 800 or bullet.X <= 0:
    #             move_bullet = 0
    #         # print(111111)
    #         bullet.X += self.STEP
            

    def medic_bot_collide(self):
        # print(self.X)
        # print(medic_bot.X)
        global flag_level_3
        if self.X <= medic_bot.X + medic_bot.WIDTH and self.X + self.WIDTH >= medic_bot.X:
            # print(222222222222222)
            if self.Y + 30 >= medic_bot.Y and self.Y + self.HEIGHT <= medic_bot.Y + medic_bot.HEIGHT + 30:
                flag_level_3 = True
                
                # list_create_world, list_rect = area.create_world(area.list_world_2)
                # print(medic_bot.X)

    def door_exit_collide(self):
        if self.INJURED:
            if self.Y >= door_exit.Y and self.Y + self.HEIGHT - 10 <= door_exit.Y + door_exit.HEIGHT:
                # print(11111)
                if self.X + self.WIDTH >= door_exit.X:
                    event = pygame.key.get_pressed()
                    self.draw_text(win, "E")
                    if event[pygame.K_e]:
                        # self.OPEN_DOOR = False
                        self.EXIT_DOOR = True
    def animation(self,folder= None, count_while= None, last_img= None, first_img= None):
        self.SPEED_ANIMATION += 1
        if self.SPEED_ANIMATION % count_while == 0:
            if self.COUNT_IMG == last_img:
                self.COUNT_IMG = first_img
            self.NAME_IMAGE = f"game2/images/{folder}/{self.COUNT_IMG}.png"
            self.direction() # задаємо напрямок по горизонталі зображення 
            self.COUNT_IMG += 1 # задаємо наступний номер зображення
    def direction(self):
        # print(self.DIRECTION)
        if self.DIRECTION == 'R':
            self.load_image()
        elif self.DIRECTION == 'L':
            self.load_image(direction=True)
    def fire(self, fire, num_fire):
        global fire1
        global fire2
        global fire3
        global fire4
        global fire5
        global fire6
        global fire7
        self.COUNT_FIRE_POSITION += 1
        if self.X <= fire.X + fire.WIDTH and self.X + self.WIDTH >= fire.X:
            # print(222222222222222)
            if self.Y + 30 >= fire.Y and self.Y + self.HEIGHT <= fire.Y + fire.HEIGHT + 30:
                # print("012398")
                pass
                # pass
        if (self.Y + 10 <= fire.Y + fire.HEIGHT and self.Y + self.HEIGHT - 10 >= fire.Y) or (self.Y + 10 <= fire.Y + fire.HEIGHT and self.Y + self.HEIGHT - 10 >= fire.Y):
                # print(block.HEIGHT, "23e43ed3sede")
            if (self.X + self.WIDTH <= fire.X + self.STEP and self.X + self.WIDTH >= fire.X + 100) or (self.X >= fire.X - self.STEP - 30 and self.X <= fire.X + fire.WIDTH + 30):
                if self.EXTING_ON:
                    event = pygame.key.get_pressed()
                    self.draw_text(win, "E")
                    if event[pygame.K_e]:
                        if num_fire == 1:
                            # print(1)
                            self.BLIT_FIRE_1 = False
                        if num_fire == 2:
                            # print(2)
                            self.BLIT_FIRE_2 = False
                        if num_fire == 3:
                            # print(3)
                            self.BLIT_FIRE_3 = False
                        if num_fire == 4:
                            # print(4)
                            self.BLIT_FIRE_4 = False
                        if num_fire == 5:
                            # print(5)
                            self.BLIT_FIRE_5 = False
                        if num_fire == 6:
                            # print(6)
                            self.BLIT_FIRE_6 = False
                        if num_fire == 7:
                    
                            self.BLIT_FIRE_7 = False
                            # print(self.BLIT_FIRE_7)
        if self.COUNT_FIRE_POSITION == 350:
            fire1 = Sprite(x = 400, y = 70, width = 80, height = 50, name_image = "game2/images/fire.png")
        if self.COUNT_FIRE_POSITION == 700:
            fire2 = Sprite(x = 720, y = 670, width = 80, height = 50, name_image = "game2/images/fire.png")
        if self.COUNT_FIRE_POSITION == 1050:
            fire3 = Sprite(x = 0, y = 670, width = 80, height = 50, name_image = "game2/images/fire.png")
        if self.COUNT_FIRE_POSITION == 1400:
            fire4 = Sprite(x = 100, y = 490, width = 80, height = 50, name_image = "game2/images/fire.png")
        if self.COUNT_FIRE_POSITION == 1750:
            fire5 = Sprite(x = 100, y = 250, width = 80, height = 50, name_image = "game2/images/fire.png")
        if self.COUNT_FIRE_POSITION == 2100:
            fire6 = Sprite(x = 720, y = 490, width = 80, height = 50, name_image = "game2/images/fire.png")
        if self.COUNT_FIRE_POSITION == 2450:
            fire7 = Sprite(x = 400, y = 670, width = 80, height = 50, name_image = "game2/images/fire.png")
    def panel_collide(self):
    #    if self.X <= panel.X + panel.WIDTH and self.X + self.WIDTH >= panel.X:
    #        print("123")
    #        if self.Y + 30 >= panel.Y and self.Y + self.HEIGHT <= panel.Y + panel.HEIGHT + 30:
    #            #print("123")
    #            pass
        event = pygame.key.get_pressed()
        if (self.X + self.WIDTH <= panel.X + self.STEP + 60 and self.X + self.WIDTH >= panel.X - 60) or (self.X >= panel.X - self.STEP - 60 and self.X <= panel.X + panel.WIDTH + 60):
            if (self.Y + 10 <= panel.Y + panel.HEIGHT and self.Y + self.HEIGHT - 10 >= panel.Y) or (self.Y + 10 <= panel.Y + panel.HEIGHT and self.Y + self.HEIGHT - 10 >= panel.Y):
                self.draw_text(win, "E")
                if event[pygame.K_e]:
                   print(1111111111)
                   self.SCENE4 = True
                #    door_3 = Sprite(x = 520, y = 600, width = 120, height = 120, name_image = "game2/images/fire.png")
    def extinguisher_collide(self):
        #if self.X <= extinguisher.X + extinguisher.WIDTH and self.X + self.WIDTH >= extinguisher.X:
        #    print("123")
        #    if self.Y + 30 >= extinguisher.Y and self.Y + self.HEIGHT <= extinguisher.Y + extinguisher.HEIGHT + 30:
        #        print("321")
        #        pass
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= extinguisher.X + extinguisher.WIDTH + 20 and self.X + 20 >= extinguisher.X:
            if self.Y + 21 >= extinguisher.Y and self.Y + self.HEIGHT <= extinguisher.Y + extinguisher.HEIGHT + 20:
                self.draw_text(win, "E")
                if event[pygame.K_e]:
                  self.EXTING_ON = True
    def shoot(self, win, count_while, sprite, list_rect):
            # global blit_bullet_count
            global bullet1
            # blit_bullet_count += 1
            # if blit_bullet_count == 100:
            #     blit_bullet_count = 0
            #     bullet.flag_blit_bullet = True
            self.COUNT_BULLET += 1
            # derection = 1
            # if self.DIRECTION == "L":
            #     derection = -1
            #     width = 0
            # if bullet.flag_blit_bullet:
            
            if self.COUNT_BULLET % count_while == 2 and len(self.LIST_BULLET) < 1:
                # print(1)
                
                if medic_bot.X < -2:
                    bullet1 = bullet.Bullet(
                        x = self.X - 20,
                        y = self.Y,
                        width= 50,
                        height= 50,
                        name_image= "game2/images/bullet.png"
                    )
                
                    
                else:
                    if medic_bot.X > 400:          
                        bullet1 = bullet.Bullet(
                            x = self.X + 20,
                            y = self.Y,
                            width= 50,
                            height= 50,
                            name_image= "game2/images/bullet_2.png"
                        )
                    else:
                        bullet1 = bullet.Bullet(
                            x = self.X + 20,
                            y = self.Y,
                            width= 50,
                            height= 50,
                            name_image= "game2/images/bullet.png"
                        )

                bullet1.load_image()
                
                self.LIST_BULLET.append(bullet1)
            if self.LIST_BULLET:
                # print(1111)
                for bullet1 in self.LIST_BULLET:
                    # print(self.LIST_BULLET)
                    bullet1.blit_sprite(win)
                    bullet1.bullet(sprite,list_rect = list_rect, medic = medic_bot)
                    
                    # print(bullet1.MOVE_BULLET)
                    if bullet1.MOVE_BULLET == False:
                        # print(22222222222)
                        self.LIST_BULLET.remove(bullet1)   
    def hole(self):
        global letter
        # list_letters = ["q", "w", "e", "r", "t", "y", "u","x", "c", "f"]
        if self.HOLE_COUNT:
            # print(111)
            self.X = random.choice(list_cor_x) 
            self.Y = random.choice(list_cor_y)  
            letter = random.choice(list_letters)
            self.HOLE_COUNT = False
        event = pygame.key.get_pressed()
        font = pygame.font.SysFont("kokila", 20)
        follow = font.render(f"{letter}", 1, (0,0,0))
        # print(letter)
        if letter == "q":
            if event[pygame.K_q]:
                self.HOLE_COUNT = True
        if letter == "w":
            if event[pygame.K_w]:
                self.HOLE_COUNT = True
        if letter == "e":
            if event[pygame.K_e]:
                self.HOLE_COUNT = True
        if letter == "r":
            if event[pygame.K_r]:
                self.HOLE_COUNT = True
        if letter == "t":
            if event[pygame.K_t]:
                self.HOLE_COUNT = True
        if letter == "y":
            if event[pygame.K_y]:
                self.HOLE_COUNT = True
        if letter == "u":
            if event[pygame.K_u]:
                self.HOLE_COUNT = True
        if letter == "x":
            if event[pygame.K_x]:
                self.HOLE_COUNT = True
        if letter == "c":
            if event[pygame.K_c]:
                self.HOLE_COUNT = True
        if letter == "f":
            if event[pygame.K_f]:
                self.HOLE_COUNT = True
        win.blit(follow, (self.X, self.Y))

                


sprite = Sprite(color = (0,0,0), x = 330, y = 600, width = 50, height = 60, name_image = "game2/images/player/1.png")
smoke = Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
mask = Sprite(x = 5, y = 5, width = 30, height = 40, name_image = "game2/images/mask.png")
door = Sprite(x = 520, y = 600, width = 120, height = 120, name_image = "game2/images/door.png")
door_exit = Sprite(x = 600, y = 0, width = 120, height = 120, name_image = "game2/images/door.png")
medic_bot = Sprite(x = 20, y = 660, width = 50, height = 50, name_image = "game2/images/medic/1.png")
sprite_2 = Sprite(color = (0,0,0), x = 300, y = 660, width = 50, height = 60, name_image = "game2/images/sprite.png")
sprite_3 = Sprite(color = (0,0,0), x = 300, y = 660, width = 50, height = 60, name_image = "game2/images/sprite.png")
# bullet = Sprite(x = 100, y = 660, width = 50, height = 50, name_image = "game2/images/bullet.png")
medic_escape = Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/medic_escape.png")
arrow1 = Sprite(x = 700, y = 700, width = 100, height = 150, name_image = "game2/images/comix/arrow_1.png")
arrow2 = Sprite(x = 50, y = 700, width = 100, height = 150, name_image = "game2/images/comix/arrow_2.png")
page = Sprite(x = 50, y = 50, width = 700, height = 700, name_image = "game2/images/comix/page_1.png")
black = Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/comix/black.png")
#3 лвл. Вогонь
fire1 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")
fire2 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")
fire3 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")
fire4 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")
fire5 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")
fire6 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")
fire7 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire.png")

door_3 = Sprite(x = 520, y = 600, width = 120, height = 120, name_image = "game2/images/door.png")
extinguisher = Sprite(x = 730, y = 490, width = 50, height = 50, name_image = "game2/images/extinguisher.png")
panel = Sprite(x = 535, y = 66, width = 50, height = 50, name_image = "game2/images/panel.png")
# pipe_1 = Sprite(x = 200, y = 400, width = 75, height = 75, name_image = "game2/images/pipes/pipe1.png")
# pipe_2 = Sprite(x = 50, y = 400, width = 75, height = 75, name_image = "game2/images/pipes/pipe2.png")
# pipe_3 = Sprite(x = 100, y = 100, width = 75, height = 75, name_image = "game2/images/pipes/pipe5.png")
# pipe_4 = Sprite(x = 200, y = 200, width = 75, height = 75, name_image = "game2/images/pipes/pipe5.png")
pump = Sprite(x = 550, y = 550, width = 200, height = 200, name_image = "game2/images/panel.png")
pump_scale = Sprite(x = 580, y = 250, width = 60, height = 100, name_image = "game2/images/panel.png")
boat = Sprite(x = 100, y = 250, width = 300, height = 500, name_image = "game2/images/panel.png")

hole1 = Sprite(x = 0, y = 0, width = 50, height = 50, name_image = "game2/images/panel.png")
hole2 = Sprite(x = 0, y = 0, width = 50, height = 50, name_image = "game2/images/panel.png")
hole3 = Sprite(x = 0, y = 0, width = 50, height = 50, name_image = "game2/images/panel.png")
hole4 = Sprite(x = 0, y = 0, width = 50, height = 50, name_image = "game2/images/panel.png")