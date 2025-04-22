import pygame
pygame.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PingPong')

font = pygame.font.Font(None, 48)
score1 = 0
score2 = 0
paddle_width, paddle_height = 10,100

ball_radius = 10

paddle1 = pygame.Rect(30,(HEIGHT-paddle_height)//2,paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH-paddle_width - 30,(HEIGHT-paddle_height)//2,paddle_width, paddle_height)

paddle_speed = 7

ball_x,ball_y = WIDTH//2,HEIGHT//2
speed_ball_x,speed_ball_y = 5,5

max_score = 4
game_over = False

def draw_score():
    score_text = font.render(f"{score1} : {score2}", True, "white")
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

def goal(player1):
    global score1, score2
    if player1:
        score1 += 1
    else:
        score2 += 1
    reset_ball()

def reset_ball():
    global ball_x,ball_y,speed_ball_x,speed_ball_y
    ball_x,ball_y = WIDTH//2,HEIGHT//2
    speed_ball_x *= -1
    speed_ball_y *= -1
    # pygame.time.delay(1000)

def reset_game():
    global score1, score2, game_over
    game_over = False
    reset_ball()
    score1 = 0
    score2 = 0
    paddle1.y = (HEIGHT-paddle_height)//2
    paddle2.y = (HEIGHT-paddle_height)//2


def finish_game():
    global game_over, score1, score2
    if score1 == max_score or score2 == max_score:
        game_over = True
        if score1 > score2:
            winner = "Player 1 wins!"
        elif score1 < score2:
            winner = "Player 2 wins!"
        else:
            return True

        
        text_surface = font.render(winner, True, "white")
        screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, HEIGHT//3 - text_surface.get_height()//2))
        pygame.display.flip()
        # pygame.time.delay(3000)
        # reset_game()
    return False

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
       elif game_over and event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            reset_game()
           

    if game_over:
        continue
    ball_x += speed_ball_x
    ball_y += speed_ball_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0,-paddle_speed)
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.move_ip(0,paddle_speed)
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.move_ip(0,-paddle_speed)
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.move_ip(0,paddle_speed)

    
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        speed_ball_y *= -1 

    # переробити під гол
    if ball_x - ball_radius < 0:
        goal(False)
    if ball_x + ball_radius > WIDTH:
        goal(True)

    if paddle1.collidepoint(ball_x -ball_radius,ball_y):
        speed_ball_x *= -1 
    if paddle2.collidepoint(ball_x +ball_radius,ball_y):
        speed_ball_x *= -1 


    screen.fill("black")
    pygame.draw.rect(screen,"white",paddle1)
    pygame.draw.rect(screen,"white",paddle2)
    pygame.draw.circle(screen,"white",(ball_x,ball_y),ball_radius)
    
    draw_score()

    if finish_game():
        continue
    pygame.display.flip()
    pygame.time.Clock().tick(60)