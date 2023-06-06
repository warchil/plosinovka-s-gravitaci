import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Herni promenne
velikost_dlazdice = 50
sirka_obrazovky = 1600
vyska_obrazovky = 900
BILA_BARVA = (255, 255, 255)

herniObrazovka = pygame.display.set_mode((sirka_obrazovky, vyska_obrazovky))
pygame.display.set_caption('Plošinovka')

# Nacteni obrazku
obrazekSlunce = pygame.image.load('obrazky/slunce.png')
obrazekPozadi = pygame.image.load('obrazky/obloha-1600-900.png')



class Hrac():

	def __init__(self, x, y):
		self.obrazky_napravo = []
		self.obrazky_nalevo = []
		self.index = 0
		self.pocitadlo = 0
		for cislo in range(1, 5):
			obrazek_napravo = pygame.image.load(f'obrazky/guy{cislo}.png')
			obrazek_napravo = pygame.transform.scale(obrazek_napravo, (40, 80))
			obrazek_nalevo = pygame.transform.flip(obrazek_napravo, True, False)
			self.obrazky_napravo.append(obrazek_napravo)
			self.obrazky_nalevo.append(obrazek_nalevo)
		self.aktualniObrazek = self.obrazky_napravo[self.index]
		self.rect = self.aktualniObrazek.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.sirka = self.aktualniObrazek.get_width()
		self.vyska = self.aktualniObrazek.get_height()
		self.rychlost_y = 0
		self.vyskocil = False
		self.smer = 0

	def aktualizuj(self):
		dx = 0
		dy = 0
		odpocet_chuze = 5

		# reakce na klavesy
		klavesa = pygame.key.get_pressed()
		if klavesa[pygame.K_SPACE] and self.vyskocil == False:
			self.rychlost_y = -15
			self.vyskocil = True
		if klavesa[pygame.K_SPACE] == False:
			self.vyskocil = False
		if klavesa[pygame.K_LEFT]:
			dx -= 5
			self.pocitadlo += 1
			self.smer = -1
		if klavesa[pygame.K_RIGHT]:
			dx += 5
			self.pocitadlo += 1
			self.smer = 1
		if klavesa[pygame.K_LEFT] == False and klavesa[pygame.K_RIGHT] == False:
			self.pocitadlo = 0
			self.index = 0
			if self.smer == 1:
				self.aktualniObrazek = self.obrazky_napravo[self.index]
			if self.smer == -1:
				self.aktualniObrazek = self.obrazky_nalevo[self.index]


		# reseni animace
		if self.pocitadlo > odpocet_chuze:
			self.pocitadlo = 0
			self.index += 1
			if self.index >= len(self.obrazky_napravo):
				self.index = 0
			if self.smer == 1:
				self.aktualniObrazek = self.obrazky_napravo[self.index]
			if self.smer == -1:
				self.aktualniObrazek = self.obrazky_nalevo[self.index]


		# Pridani gravitace
		self.rychlost_y += 1
		if self.rychlost_y > 10:
			self.rychlost_y = 10
		dy += self.rychlost_y

		# Kontrola kolizi
		for dlazdice in svet.seznam_dlazdic:
			# Zkontroluj kolize ve smeru x
			if dlazdice[1].colliderect(self.rect.x + dx, self.rect.y, self.sirka, self.vyska):
				dx = 0
			# Zkontroluj kolize ve smeru y
			if dlazdice[1].colliderect(self.rect.x, self.rect.y + dy, self.sirka, self.vyska):
				# Zkontroluj, jestli je hrac nad zemi (ve skoku - stoupa)
				if self.rychlost_y < 0:
					dy = dlazdice[1].bottom - self.rect.top
					self.rychlost_y = 0
				# Zkontroluj, jestli je hrad nad zemi (pada)
				elif self.rychlost_y >= 0:
					dy = dlazdice[1].top - self.rect.bottom
					self.rychlost_y = 0

		# Aktualizace souradnic hrace
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > vyska_obrazovky:
			self.rect.bottom = vyska_obrazovky
			dy = 0

		# Nakresleni hrace na obrazovku
		herniObrazovka.blit(self.aktualniObrazek, self.rect)
		pygame.draw.rect(herniObrazovka, BILA_BARVA, self.rect, 2)



class Svet():
	def __init__(self, definice_sveta):
		self.seznam_dlazdic = []

		# nacteni obrazku
		obrazekHliny = pygame.image.load('obrazky/dirt.png')
		obrazekTravy = pygame.image.load('obrazky/grass.png')

		cislo_radku = 0
		for radek in definice_sveta:
			cislo_sloupce = 0
			for dlazdice in radek:
				if dlazdice == 1:
					obrazek = pygame.transform.scale(obrazekHliny, (velikost_dlazdice, velikost_dlazdice))
					obrazek_rect = obrazek.get_rect()
					obrazek_rect.x = cislo_sloupce * velikost_dlazdice
					obrazek_rect.y = cislo_radku * velikost_dlazdice
					dlazdice = (obrazek, obrazek_rect)
					self.seznam_dlazdic.append(dlazdice)
				if dlazdice == 2:
					obrazek = pygame.transform.scale(obrazekTravy, (velikost_dlazdice, velikost_dlazdice))
					obrazek_rect = obrazek.get_rect()
					obrazek_rect.x = cislo_sloupce * velikost_dlazdice
					obrazek_rect.y = cislo_radku * velikost_dlazdice
					dlazdice = (obrazek, obrazek_rect)
					self.seznam_dlazdic.append(dlazdice)
				cislo_sloupce += 1
			cislo_radku += 1

	def nakresli(self):
		for tile in self.seznam_dlazdic:
			herniObrazovka.blit(tile[0], tile[1])
			pygame.draw.rect(herniObrazovka, BILA_BARVA, tile[1], 2)

definice_level_1 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

hrac = Hrac(100, vyska_obrazovky - 130)
svet = Svet(definice_level_1)

run = True
while run:

	clock.tick(fps)

	herniObrazovka.blit(obrazekPozadi, (0, 0))
	herniObrazovka.blit(obrazekSlunce, (100, 100))

	svet.nakresli()

	hrac.aktualizuj()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()