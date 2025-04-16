import pygame

pygame.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PingPong')


paddle_width, paddle_height = 10,100

ball_radius = 10

paddle1 = pygame.Rect(30,(HEIGHT-paddle_height)//2,paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH-paddle_width - 30,(HEIGHT-paddle_height)//2,paddle_width, paddle_height)

paddle_speed = 7

ball_x,ball_y = WIDTH//2,HEIGHT//2
speed_ball_x,speed_ball_y = 5,5



while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()


    ball_x += speed_ball_x
    ball_y += speed_ball_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.move_ip(0,-paddle_speed)
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.move_ip(0,paddle_speed)
    # todo add moving for paddle2 


    
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        speed_ball_y *= -1 

    # переробити під гол
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        speed_ball_x *= -1 

    if paddle1.collidepoint(ball_x -ball_radius,ball_y):
        speed_ball_x *= -1 
    # зробити для другої палетки


    screen.fill("black")
    pygame.draw.rect(screen,"white",paddle1)
    pygame.draw.rect(screen,"white",paddle2)
    pygame.draw.circle(screen,"white",(ball_x,ball_y),ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)