import pygame, sys
import time
# def anime_slide():
def animate_moves(peg, over, land,images,board_state,bttn_pos):
    steps = 30
    pygame.init()
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((1200, 600))
    img_cord_dict ={1:[520,480],2:[480,400],3:[560,400],4:[440,320],5:[520,320],6:[600,320],7:[400,240],
               8:[480,240],9:[560,240],10:[640,240],11:[360,160],12:[440,160],13:[520,160],14:[600,160],
               15:[680,160]}
    move_x = (img_cord_dict[land][0] - img_cord_dict[peg][0]) / steps
    move_y = (img_cord_dict[land][1] - img_cord_dict[peg][1]) / steps
    peg_x=img_cord_dict[peg][0]
    peg_y=img_cord_dict[peg][1]
    #over_y=img_cord_dict[over][1]

    barbie_size = 80
    PINK = (255, 192, 203)
    WHITE = (255, 255, 255)
    GREY = (251,191,0)
    RED = (165,42,42)
    x_offset = WINDOW_WIDTH // 2
    y_offset = WINDOW_HEIGHT - barbie_size // 2
       
    
    if bttn_pos == 150:
                screen.fill(PINK)
    elif bttn_pos == 300:
            screen.fill(GREY)
    elif bttn_pos == 500:
        screen.fill(RED)
    if bttn_pos == 150:
            image = pygame.image.load("BARBIE_STANDING_PIC.jpg").convert_alpha()
    elif bttn_pos == 300:
        image = pygame.image.load("ANIMIE2.jpg").convert_alpha()
    elif bttn_pos == 500:
        image = pygame.image.load("IRON.jpg").convert_alpha()
    for row in range(0, 6):
        x = x_offset - (row + 1) * barbie_size // 2
            
        for col in range(row):
            
                pygame.draw.circle(screen, (255, 255, 255), (x + barbie_size // 2, y_offset + barbie_size // 2), barbie_size // 2)
                print(x,y_offset)
                image = pygame.transform.scale(image, (barbie_size, barbie_size))
                screen.blit(image,(x ,y_offset))
                
                x += barbie_size
        y_offset -= barbie_size
        
    for step in range(steps):
        
        for n in range(1, 16):
            if n in board_state:
                image = pygame.transform.scale(images[peg-1], (barbie_size, barbie_size))
                screen.blit(image, (img_cord_dict[peg][0] + move_x * step, img_cord_dict[peg][1] + move_y * step))
                pygame.draw.circle(screen, (255, 255, 255), ( peg_x+40,peg_y+40 ), barbie_size // 2)

        pygame.display.flip()
        pygame.time.delay(50)


def third_slide():
    pygame.init()
    
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Thank you slide")

    # Load the background image
    background_image = pygame.image.load("THANKYOU.png").convert()
    background_image = pygame.transform.scale(background_image, (1200, 600))

    font = pygame.font.Font(None, 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                background_image=None            
                pygame.quit()
                sys.exit()
            # Handle any events specific to the third slide here

        # Blit the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw other elements on the third slide here
        text_surface = font.render("This is the third slide!", True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()


def display_result(last_land, bttn_pos):
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Result Slide")
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 600
    PINK = (255, 192, 203)
    WHITE = (255, 255, 255)
    GREY = (251,191,0)
    RED = (165,42,42)
    barbie_size = 80
    
    
    img_cord_dict ={1:[520,480],2:[480,400],3:[560,400],4:[440,320],5:[520,320],6:[600,320],7:[400,240],
               8:[480,240],9:[560,240],10:[640,240],11:[360,160],12:[440,160],13:[520,160],14:[600,160],
               15:[680,160]}
    img_cord= img_cord_dict[last_land]
    print(img_cord[0],img_cord[1])
    font = pygame.font.Font(None, 30)

    
    while True:
        if bttn_pos == 150:
                screen.fill(PINK)
        elif bttn_pos == 300:
                screen.fill(GREY)
        elif bttn_pos == 500:
            screen.fill(RED)       
        text_surface = font.render('CONGRATULATIONS!!', True, (0,0,0))
        screen.blit(text_surface, (100,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                image = None
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                 third_slide()

        x_offset = WINDOW_WIDTH // 2
        y_offset = WINDOW_HEIGHT - barbie_size // 2
        x_cord=img_cord[0]
        y_cord=img_cord[1]
        if bttn_pos == 150:
                image = pygame.image.load("BARBIE_STANDING_PIC.jpg").convert_alpha()
        elif bttn_pos == 300:
            image = pygame.image.load("ANIMIE2.jpg").convert_alpha()
        elif bttn_pos == 500:
            image = pygame.image.load("IRON.jpg").convert_alpha()
        for row in range(0, 6):
            x = x_offset - (row + 1) * barbie_size // 2
            
            for col in range(row):
                    pygame.draw.circle(screen, (255, 255, 255), (x + barbie_size // 2, y_offset + barbie_size // 2), barbie_size // 2)
                    print(x,y_offset)
                    image = pygame.transform.scale(image, (barbie_size, barbie_size))
                    screen.blit(image,(x_cord ,y_cord))

                    x += barbie_size
            y_offset -= barbie_size

        pygame.display.flip()    
    

def display_output(output_text,land,bttn_pos,solution,images,boards,rem_list):
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Output Slide")

    font = pygame.font.Font(None, 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                i=0
                for peg, over, land in solution:
                    board_state = boards[i]
                    animate_moves(peg, over, land,images,board_state,bttn_pos)
                    i=i+1
                display_result(land,bttn_pos)

        screen.fill((185,226,163))
        for i, line in enumerate(output_text):
             text_surface = font.render(line, True, (0,0,0))
             screen.blit(text_surface, (10, 10 + i * 40))

        pygame.display.flip()

def game_logic(binary_config):
    last_land = 0
    def DrawBoard(board):
            peg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for n in range(1,16):
                peg[n] = '.'
                if n in board:
                            peg[n] = "%X" % n
            print ("%s %s %s %s %s" % (peg[11],peg[12],peg[13],peg[14],peg[15]))
            print ("  %s %s %s %s" % (peg[7],peg[8],peg[9],peg[10]))
            print ("   %s %s %s" % (peg[4],peg[5],peg[6]))
            print ("    %s %s" % (peg[2],peg[3]))
            print ("     %s" % peg[1])

# remove peg n from board
    def RemovePeg(board,n):
        board.remove(n)
    def AddPeg(board,n):
        board.append(n)
    def IsPeg(board,n):
        return n in board
    JumpMoves = { 1: [ (2,4),(3,6) ], 
                2: [ (4,7),(5,9)  ],
                3: [ (5,8),(6,10) ],
                4: [ (2,1),(5,6),(7,11),(8,13) ],
                5: [ (8,12),(9,14) ],
                6: [ (3,1),(5,4),(9,13),(10,15) ],
                7: [ (4,2),(8,9)  ],
                8: [ (5,3),(9,10) ],
                9: [ (5,2),(8,7)  ],
                10: [ (9,8) ],
                11: [ (12,13) ],
                12: [ (8,5),(13,14) ],
                13: [ (8,4),(9,6),(12,11),(14,15) ],
                14: [ (9,5),(13,12)  ],
                15: [ (10,6),(14,13) ]
                }

    Solution = []
#
# Recursively solve the problem
#
    def Solve(board):
        if len(board) == 1:
            return board
        for peg in range(1,16): 
            if IsPeg(board,peg):
                movelist = JumpMoves[peg]
                for over,land in movelist:
                            if IsPeg(board,over) and not IsPeg(board,land):
                                saveboard = board[:] 
                                RemovePeg(board,peg)
                                RemovePeg(board,over)
                                AddPeg(board,land) 
                                Solution.append((peg,over,land))
                                board = Solve(board)
                                if len(board) == 1:
                                    return board
                                board = saveboard[:] 
                                del Solution[-1]
        return board
    def InitSolve(empty):
            board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            RemovePeg(board,empty_start)
            Solve(board)
    print("enter the binary digit of length 15 such that there is only one zero in it and remaining all should be one\n")
    input_bin_str = binary_config
    input_bin_str = input_bin_str[:16]
    empty_start = input_bin_str.index('0')+1
    print("starts with ",empty_start," place on board\n")
    InitSolve(empty_start)
    board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    RemovePeg(board,empty_start)
    output_text=[]
    board_state=[]
    b1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    board_state.append(b1)
    b2=b1.copy()
    rem_list=[[0]]
    for peg,over,land in Solution:
            RemovePeg(board,peg)
            RemovePeg(board,over)
            AddPeg(board,land) # board order changes!
            print ("Peg",peg,"jumped over",over,"to land on",land,end = "\n")
            output_str=f"Peg {peg} jumped over {over} to land on {land}"
            output_text.append(output_str)
            rem_list.append([peg,over])
            b2 = b2.copy()
            while peg in b2:
                b2.remove(peg)
            while over in b2:
                b2.remove(over)
            if land in b2:
                b2.remove(land)
            b2.append(land)
            rm=[]
            for p in b1:
                 if p not in b2:
                      rm.append(p)
            rem_list.append(rm)
            print(b2,rm)
            board_state.append(b2.copy())
            last_land=land
    output_text.append('Press Enter to see the Result...............')
    print(board_state,rem_list)
    return output_text,last_land,Solution,board_state,rem_list
def game_slide(bttn_pos):
    pygame.init()
    WINDOW_WIDTH =    1200
    WINDOW_HEIGHT =   600
    TRIANGLE_HEIGHT = 5 
    BARBIE_SIZE =     80
    PINK = (255, 192, 203)
    WHITE = (255, 255, 255)
    GREY = (251,191,0)
    RED = (165,42,42)
    def display_barbie_triangular_board(binary_config):
        if bttn_pos == 150:
                screen.fill(PINK)
        elif bttn_pos == 300:
                screen.fill(GREY)
        elif bttn_pos == 500:
            screen.fill(RED)
        x_offset = WINDOW_WIDTH // 2
        y_offset = WINDOW_HEIGHT - BARBIE_SIZE // 2
        current_barbie = 1
        for row in range(0, TRIANGLE_HEIGHT + 1):
            x = x_offset - (row + 1) * BARBIE_SIZE // 2
            for col in range(row):
                if bttn_pos == 150:
                    barbie_image = pygame.image.load("BARBIE_STANDING_PIC.jpg").convert_alpha()
                elif bttn_pos == 300:
                    barbie_image = pygame.image.load("ANIMIE2.jpg").convert_alpha()
                elif bttn_pos == 500:
                    barbie_image = pygame.image.load("IRON.jpg").convert_alpha()
                barbie_image = pygame.transform.scale(barbie_image, (BARBIE_SIZE, BARBIE_SIZE))
                screen.blit(barbie_image, (x, y_offset))
                x += BARBIE_SIZE
                current_barbie += 1
            y_offset -= BARBIE_SIZE
        font =pygame.font.Font(None, 30)
        text_surface = font.render("Enter the Binary configuration: ", True, WHITE)
        screen.blit(text_surface, (10, 10))
        input_text = font.render(binary_config, True, WHITE)
        screen.blit(input_text, (10, 40))
        pygame.display.flip()
        return barbie_image
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    if bttn_pos ==150:
        pygame.display.set_caption("Barbie Triangular Board")
    elif bttn_pos ==300:
        pygame.display.set_caption("Anime Triangular Board")
    elif bttn_pos == 500:
        pygame.display.set_caption("Avenger Triangular Board")
    binary_config = ""
    while True:
        image = display_barbie_triangular_board(binary_config)
        images = []
        for i in range(1, 16):
            images.append(image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                image =None
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Binary configuration entered:", binary_config)
                    output_text,land,solution,board_state,rem_list =game_logic(binary_config)
                    print(land)
                    display_output(output_text,land,bttn_pos,solution,images,board_state,rem_list)
                    binary_config = ""  
                elif event.unicode.isdigit():
                    binary_config = binary_config + event.unicode        
        pygame.display.flip()
def second_slide():
        buttons = []
        class Button:
            def _init_(self,text,width,height,pos,elevation):
                self.pressed = False
                self.elevation = elevation
                self.dynamic_elecation = elevation
                self.original_y_pos = pos[1]
                self.top_rect = pygame.Rect(pos,(width,height))
                self.top_color = '#FFFF00'
                self.bottom_rect = pygame.Rect(pos,(width,height))
                self.bottom_color = '#FFFF00'
                self.text = text
                self.text_surf = gui_font.render(text,True,'#FFFFFF')
                self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
                buttons.append(self)
            def change_text(self, newtext):
                self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
                self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
            def draw(self):
                self.top_rect.y = self.original_y_pos - self.dynamic_elecation
                self.text_rect.center = self.top_rect.center 
                self.bottom_rect.midtop = self.top_rect.midtop
                self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
                pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
                pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
                screen.blit(self.text_surf, self.text_rect)
                self.check_click()
            def check_click(self):
                mouse_pos = pygame.mouse.get_pos()
                if self.top_rect.collidepoint(mouse_pos):
                    self.top_color = '#FFFF00'
                    if pygame.mouse.get_pressed()[0]:
                        self.dynamic_elecation = 0
                        self.pressed = True
                        self.change_text(f"{self.text}")
                        bttn_pos=self.original_y_pos
                        game_slide(bttn_pos)
                    else:
                        self.dynamic_elecation = self.elevation
                        if self.pressed == True:
                            print('click')
                            self.pressed = False
                            self.change_text(self.text)
                else:
                    self.dynamic_elecation = self.elevation
                    self.top_color =  (255, 0, 0)
        pygame.init()
        screen_width = 1100
        screen_height = 600
        screen = pygame.display.set_mode((screen_width,screen_height))
        background_image = pygame.image.load("BACKGROUND4.png") 
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        pygame.display.set_caption('SELECT YOUR OWN THEME')
        def buttons_draw():
            for b in buttons:
                b.draw()
        clock = pygame.time.Clock()
        gui_font = pygame.font.Font(None,30)
        button1 = Button('BARBIE',200,40,(50,150),5)
        button2 = Button('ANIME',200,40,(50,300),5)
        button3 = Button('AVENGERS',200,40,(50,500),5)
        while True:
            screen.blit(background_image,(0,0))
            buttons_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    background_image = None
                    pygame.image.unload()
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock.tick(60)
def first_slide():
        pygame.mixer.init()
        pygame.mixer.music.load("LOKIVERSE.mp3")  # Replace "background_music.mp3" with your music file
        pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)
        buttons = []
        class Button:
            def _init_(self,text,width,height,pos,elevation):
                self.pressed = False
                self.elevation = elevation
                self.dynamic_elecation = elevation
                self.original_y_pos = pos[1]
                self.original_x_pos = pos[0]
                self.top_rect = pygame.Rect(pos,(width,height))
                self.top_color = '#475F77'
                self.bottom_rect = pygame.Rect(pos,(width,height))
                self.bottom_color = '#D74B4B'
                self.text = text
                self.text_surf = gui_font.render(text,True,'#FFFFFF')
                self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
                buttons.append(self)
            def change_text(self, newtext):
                self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
                self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
            def draw(self): 
                self.top_rect.y = self.original_y_pos - self.dynamic_elecation
                self.text_rect.center = self.top_rect.center 
                self.bottom_rect.midtop = self.top_rect.midtop
                self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
                pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
                pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
                screen.blit(self.text_surf, self.text_rect)
                self.check_click()
            def check_click(self):
                mouse_pos = pygame.mouse.get_pos()
                if self.top_rect.collidepoint(mouse_pos):
                    self.top_color = '#D74B4B'
                    if pygame.mouse.get_pressed()[0]:
                        self.dynamic_elecation = 0
                        self.pressed = True
                        self.change_text(f"{self.text}")
                        if self.original_x_pos == 100 :
                               second_slide()
                        if self.original_x_pos == 900 :
                              pygame.quit()
                              sys.exit()
                    else:
                        self.dynamic_elecation = self.elevation
                        if self.pressed == True:
                            print('click')
                            self.pressed = False
                            self.change_text(self.text)                                                                                    
                else:
                    self.dynamic_elecation = self.elevation
                    self.top_color = '#475F77'
        def buttons_draw():
            for b in buttons:
                b.draw()
        pygame.init()
        screen_width = 1200
        screen_height = 600
        screen = pygame.display.set_mode((screen_width,screen_height))
        background_image = pygame.image.load("THE_SPARTAN_ATHLETES.png")  # Replace "background.jpg" with the filename of your background image
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        pygame.display.set_caption('THE SPARTAN ATHELETS')
        clock = pygame.time.Clock()
        gui_font = pygame.font.Font(None,30)
        button1 = Button('START!',200,40,(100,400),5)
        button2 = Button('QUIT',200,40,(900,400),5)
        while True:
            screen.blit(background_image,(0,0))
            buttons_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    background_image= None
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            clock.tick(60)
first_slide()
