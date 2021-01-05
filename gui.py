import pygame
from settings import WIDTH, HEIGHT, FPS, LOGO
from boardGUI import BoardGUI
import time

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Chess AI")
pygame.display.set_icon(pygame.image.load(LOGO))

def main():
    running = True
    clock = pygame.time.Clock()
    x1, y1 = 0, 0
    board_gui = BoardGUI()
    while running:
        clock.tick(FPS)
        if not board_gui.get_turn():
            board_gui.ai_move()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x1, y1 = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    x2, y2 = pygame.mouse.get_pos()
                    board_gui.move(x1, y1, x2, y2)
                    x1 = -1
                    y1 = -1
        board_gui.draw_squares(WIN)
        board_gui.draw_state(WIN)
        pygame.display.update()

        if board_gui.check_game_over():
            font = pygame.font.Font("./media/arial.ttf", 64)
            text = font.render("Game Over!", True, (0, 255, 255))
            WIN.blit(text, (WIDTH / 2 - 175, HEIGHT / 2 - 48))
            pygame.display.update()
            time.sleep(7)
            board_gui.reset()
    pygame.quit()


if __name__ == "__main__":
    main()