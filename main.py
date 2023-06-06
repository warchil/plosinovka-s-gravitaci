import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

sirkaObrazovky = 1600
vyskaObrazovky = 900

screen = pygame.display.set_mode((sirkaObrazovky, vyskaObrazovky))
pygame.display.set_caption('Adrenalinová plošinovka')

# nacteni zvuku
pygame.mixer.init()
hudbaMenu = pygame.mixer.Sound('zvuky/hudba-menu.mp3')
zvukKliknuti = pygame.mixer.Sound('zvuky/zvuk-kliknuti.wav')

# hrani hudby
pygame.mixer.Channel(0).play(hudbaMenu)

# nacteni obrazku
obrazekSlunce = pygame.image.load('obrazky/slunce.png')
obrazekOblohy = pygame.image.load('obrazky/obloha.png')
obrazekTlacitkaStart = pygame.image.load('obrazky/tlacitko-start.png')
obrazekTlacitkaExit = pygame.image.load('obrazky/tlacitko-exit.png')

class Tlacitko():

    # Tato funkce vytvori novy objekt pro tridu "Tlacitko"
    # Pro vytvoreni je potreba zadat 3 parametry:
    #     1) souradnici "x", kde se tlacitko nachazi
    #     2) souradnici "y", kde se tlacitko nachazi
    #     3) obrazek tlacitka, ktery se vykresli
    def __init__(self, x, y, obrazekTlacitka):
        self.obrazekTlacitka = obrazekTlacitka
        self.rect = self.obrazekTlacitka.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.zakliknute = False

    def nakresliSe(self):
        hracKliknul = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # Zjisti, jestli je mys nad tlacitkem a jestli hrac kliknul
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.zakliknute == False:
                pygame.mixer.Channel(1).play(zvukKliknuti)
                hracKliknul = True
                self.zakliknute = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.zakliknute = False

        # vzkresli tlacitko
        screen.blit(self.obrazekTlacitka, self.rect)

        return hracKliknul

# Vytvoreni tlacitek
tlacitkoStart = Tlacitko(sirkaObrazovky // 2 - 350, vyskaObrazovky // 2, obrazekTlacitkaStart)
tlacitkoExit = Tlacitko(sirkaObrazovky // 2 + 150, vyskaObrazovky // 2, obrazekTlacitkaExit)

# herni promenne
hracJeVHlavnimMenu = True
hraBezi = True

while hraBezi:

    clock.tick(fps)

    screen.blit(obrazekOblohy, (0, 0))
    screen.blit(obrazekSlunce, (100, 100))

    if hracJeVHlavnimMenu == True:
        # Tady patri kod pro hlavni menu
        if tlacitkoStart.nakresliSe() == True:
            hracJeVHlavnimMenu = False
        if tlacitkoExit.nakresliSe() == True:
            hraBezi = False
    else:
        # Tady patri kod pro samotnou hru
        print("Hra zacina")
        hraBezi = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

print("Hra skoncila")
pygame.quit()