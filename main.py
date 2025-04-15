import pygame

pygame.init()

WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('PingPong')


while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
    screen.fill((255,255,255))
    pygame.display.flip()
    pygame.time.Clock().tick(60)