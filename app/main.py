import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Configurações da tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Zona de Guerra Eterna")

# Fonte
font = pygame.font.Font(None, 36)

# Função para criar botões
def draw_button(x, y, width, height, text, button_color, text_color):
    pygame.draw.rect(screen, button_color, (x, y, width, height))
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 250 <= event.pos[0] <= 550 and 200 <= event.pos[1] <= 250:
                print("Iniciar o jogo")
            elif 250 <= event.pos[0] <= 550 and 300 <= event.pos[1] <= 350:
                print("Acessar configurações")
            elif 250 <= event.pos[0] <= 550 and 400 <= event.pos[1] <= 450:
                running = False

    screen.fill(WHITE)
    draw_button(250, 200, 300, 50, "Iniciar Jogo", BLACK, WHITE)
    draw_button(250, 300, 300, 50, "Configurações", BLACK, WHITE)
    draw_button(250, 400, 300, 50, "Sair", BLACK, WHITE)

    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
