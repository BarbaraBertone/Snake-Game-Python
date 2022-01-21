import pygame
import random  #para la comida

class cuerpo:
    def __init__(self, cuadrado):
        self.x = 0
        self.y = 0
        self.dir = 0 #dirección que indica dónde se mueve el cuerpo
        self.cuadrado= cuadrado

    def dibujar(self):
        pygame.draw.rect(self.cuadrado, (255, 255, 255), (self.x, self.y, 10, 10)) #primero el color y luego el tamaño

    def moverse(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10

class manzanas:
    def __init__(self, cuadrado):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.cuadrado = cuadrado

    def dibujar(self):
        pygame.draw.rect(self.cuadrado, (255, 0, 0), (self.x, self.y, 10, 10))

    def nueva_manzana(self):
        self.x = random.randrange(40) * 10  #la manzana aparece en un lugar aleatorio
        self.y = random.randrange(40) * 10

def actualizar(cuadrado):
    cuadrado.fill((0, 0, 0))
    comida.dibujar()
    for i in range(len(serpiente)):  
        serpiente[i].dibujar()

def seguir_cabeza():
    for i in range(len(serpiente) - 1):
        serpiente[len(serpiente) - i - 1].x = serpiente[len(serpiente) - i - 2].x
        serpiente[len(serpiente) - i - 1].y = serpiente[len(serpiente) - i - 2]. y
def main():
    global serpiente, comida
    cuadrado = pygame.display.set_mode((400, 400))
    cuadrado.fill((0, 0, 0))
    comida = manzanas(cuadrado)
    serpiente = [cuerpo(cuadrado)]
    run = True
    while run:  #tomo las teclas de pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: #le asigno las direcciones
                if event.key == pygame.K_RIGHT:
                    serpiente[0].dir = 0
                if event.key == pygame.K_LEFT:
                    serpiente[0].dir = 1
                if event.key == pygame.K_DOWN:
                    serpiente[0].dir = 2
                if event.key == pygame.K_UP:
                    serpiente[0].dir = 3

        serpiente[0].moverse()
        actualizar(cuadrado)
        pygame.display.update() #actualiza el juego
        pygame.time.delay(100)  #tiempo en el que se mueve
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(cuadrado)) #crece la serpiente al comer
        seguir_cabeza()
        # atravesar la pantalla para que aparezca del otro lado sin perder
        if serpiente[0].x >= 400:
            serpiente[0].x = 0
        elif serpiente[0].x < 0:
            serpiente[0].x = 390
        if serpiente[0].y >= 400:
            serpiente[0].y = 0
        elif serpiente[0].y < 0:
            serpiente[0].y = 390

if __name__ == '__main__':
    main()
    pygame.quit()


