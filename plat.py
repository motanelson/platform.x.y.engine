import pygame
from pygame.locals import *

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coordenadas: (0, 0)")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Carregar a imagem
image_path = "robot_image.png"  # Substitua pelo caminho do arquivo da imagem
robot_image = pygame.image.load(image_path).convert_alpha()
image_size = robot_image.get_width()  # Considera a imagem como 32x32 px

# Posição inicial da imagem
x, y = 0, 50

# Velocidade de movimento
speed = 5

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Obter teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        y -= speed
    if keys[K_DOWN]:
        y += speed
    if keys[K_LEFT]:
        x -= speed
    if keys[K_RIGHT]:
        x += speed

    # Limitar a movimentação dentro da tela
    x = max(0, min(x, screen_width - image_size))
    y = max(50, min(y, screen_height - image_size))  # y mínimo é 50 devido à borda

    # Atualizar o título da janela
    pygame.display.set_caption(f"Coordenadas: ({x}, {y - 50})")

    # Desenhar o fundo e os elementos
    screen.fill(BLACK)  # Preencher a janela com preto
    pygame.draw.line(screen, WHITE, (0, 50), (screen_width, 50), 2)  # Linha branca na borda
    screen.blit(robot_image, (x, y))  # Desenhar a imagem

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()
