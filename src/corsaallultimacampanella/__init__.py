def main() -> None:
    print("Hello from corsaallultimacampanella!")

# importa ed inizializza la libreria pygame
import pygame

pygame.init()

# lo screen (con titolo)
screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption("Il mio primo gioco con PyGame!")

# facile...
running = True

while running:
    # serve a gestire la X di chiusura in alto
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # colora lo schermo di verde
    screen.fill("green")

    # aggiorna il contenuto dello schermo
    pygame.display.flip()

# Chiude pygame
pygame.quit()
