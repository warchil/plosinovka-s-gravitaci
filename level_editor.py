import pygame
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

# herni okno
velikostDilku = 50
pocetSloupcu = 20
velikostOkraje = 100
sirkaObrazovky = velikostDilku * pocetSloupcu
vyskaObrazovky = (velikostDilku * pocetSloupcu) + velikostOkraje

herniOkno = pygame.display.set_mode((sirkaObrazovky, vyskaObrazovky))
pygame.display.set_caption('Level Editor')

# Nacteni obrazku
sun_img = pygame.image.load('obrazky/slunce.png')
sun_img = pygame.transform.scale(sun_img, (velikostDilku, velikostDilku))
bg_img = pygame.image.load('obrazky/obloha.png')
bg_img = pygame.transform.scale(bg_img, (sirkaObrazovky, vyskaObrazovky - velikostOkraje))
dirt_img = pygame.image.load('obrazky/dirt.png')
grass_img = pygame.image.load('obrazky/grass.png')
blob_img = pygame.image.load('img/blob.png')
# platform_x_img = pygame.image.load('img/platform_x.png')
# platform_y_img = pygame.image.load('img/platform_y.png')
lava_img = pygame.image.load('obrazky/lava.png')
coin_img = pygame.image.load('img/coin.png')
# exit_img = pygame.image.load('img/exit.png')
# save_img = pygame.image.load('img/save_btn.png')
# load_img = pygame.image.load('img/load_btn.png')

# Herni promenne
clicked = False
level = 1

# Definice barev
BILA = (255, 255, 255)
ZELENA = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

# Vytvoreni prazdneho levelu
world_data = []
for row in range(20):
	r = [0] * 20
	world_data.append(r)

# Vytvoreni okraje levelu
for tile in range(0, 20):
	world_data[19][tile] = 2
	world_data[0][tile] = 1
	world_data[tile][0] = 1
	world_data[tile][19] = 1

def vypisText(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	herniOkno.blit(img, (x, y))

def nakresliMrizku():
	for c in range(21):
		# vertikalni linky
		pygame.draw.line(herniOkno, BILA, (c * velikostDilku, 0), (c * velikostDilku, vyskaObrazovky - velikostOkraje))
		# vodorovne linky
		pygame.draw.line(herniOkno, BILA, (0, c * velikostDilku), (sirkaObrazovky, c * velikostDilku))

def vykresliSvet():
	for radek in range(20):
		for sloupec in range(20):
			if world_data[radek][sloupec] > 0:
				if world_data[radek][sloupec] == 1:
					# hlina
					img = pygame.transform.scale(dirt_img, (velikostDilku, velikostDilku))
					herniOkno.blit(img, (sloupec * velikostDilku, radek * velikostDilku))
				if world_data[radek][sloupec] == 2:
					# trava
					img = pygame.transform.scale(grass_img, (velikostDilku, velikostDilku))
					herniOkno.blit(img, (sloupec * velikostDilku, radek * velikostDilku))
				if world_data[radek][sloupec] == 3:
					# nepritel
					img = pygame.transform.scale(blob_img, (velikostDilku, int(velikostDilku * 0.75)))
					herniOkno.blit(img, (sloupec * velikostDilku, radek * velikostDilku + (velikostDilku * 0.25)))
				if world_data[radek][sloupec] == 4:
					# lava
					img = pygame.transform.scale(lava_img, (velikostDilku, velikostDilku // 2))
					herniOkno.blit(img, (sloupec * velikostDilku, radek * velikostDilku + (velikostDilku // 2)))
				if world_data[radek][sloupec] == 5:
					# mince
					img = pygame.transform.scale(coin_img, (velikostDilku // 2, velikostDilku // 2))
					herniOkno.blit(img, (sloupec * velikostDilku + (velikostDilku // 4), radek * velikostDilku + (velikostDilku // 4)))

# class Button():
# 	def __init__(self, x, y, image):
# 		self.image = image
# 		self.rect = self.image.get_rect()
# 		self.rect.topleft = (x, y)
# 		self.clicked = False
#
# 	def draw(self):
# 		action = False
#
# 		#get mouse position
# 		pos = pygame.mouse.get_pos()
#
# 		#check mouseover and clicked conditions
# 		if self.rect.collidepoint(pos):
# 			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
# 				action = True
# 				self.clicked = True
#
# 		if pygame.mouse.get_pressed()[0] == 0:
# 			self.clicked = False
#
# 		#draw button
# 		herniOkno.blit(self.image, (self.rect.x, self.rect.y))
#
# 		return action

#create load and save buttons
# save_button = Button(sirkaObrazovky // 2 - 150, vyskaObrazovky - 80, save_img)
# load_button = Button(sirkaObrazovky // 2 + 50, vyskaObrazovky - 80, load_img)

# hlavni herni smycka
run = True
while run:

	clock.tick(fps)

	#draw background
	herniOkno.fill(ZELENA)
	herniOkno.blit(bg_img, (0, 0))
	herniOkno.blit(sun_img, (velikostDilku * 2, velikostDilku * 2))

	#load and save level
	# if save_button.draw():
	# 	#save level data
	# 	pickle_out = open(f'level{level}_data', 'wb')
	# 	pickle.dump(world_data, pickle_out)
	# 	pickle_out.close()
	# if load_button.draw():
	# 	#load in level data
	# 	if path.exists(f'level{level}_data'):
	# 		pickle_in = open(f'level{level}_data', 'rb')
	# 		world_data = pickle.load(pickle_in)


	#show the grid and draw the level tiles
	nakresliMrizku()
	vykresliSvet()

	#text showing current level
	# vypisText(f'Level: {level}', font, BILA, velikostDilku, vyskaObrazovky - 60)
	# vypisText('Press UP or DOWN to change level', font, BILA, velikostDilku, vyskaObrazovky - 40)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks to change tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // velikostDilku
			y = pos[1] // velikostDilku
			#check that the coordinates are within the tile area
			if x < 20 and y < 20:
				#update tile value
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 5:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 8
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#up and down key presses to change level number
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			elif event.key == pygame.K_DOWN and level > 1:
				level -= 1

	#update game display window
	pygame.display.update()

pygame.quit()