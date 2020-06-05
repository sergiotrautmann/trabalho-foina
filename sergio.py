# Sergio Patrick Hirayama Trautmann
# João Pedro Almeida de Oliveira
from graphics import *
import math
a = math.cos(30)
b = math.sin(30)

def ponto(x, y, cor, tam):
    num1 = 400 + x
    num2 = -y + 400

    if tam == 1:
        win.plotPixel(num1, num2, cor)
    elif tam == 2:
        win.plotPixel(num1, num2, cor)
        win.plotPixel(num1 + 1, num2, cor)
        win.plotPixel(num1, num2 - 1, cor)
        win.plotPixel(num1 + 1, num2 - 1, cor)
    elif tam == 3:
        win.plotPixel(num1, num2, cor)
        win.plotPixel(num1 + 1, num2, cor)
        win.plotPixel(num1 - 1, num2, cor)
        win.plotPixel(num1, num2 + 1, cor)
        win.plotPixel(num1, num2 - 1, cor)
    elif tam == 4:
        win.plotPixel(num1, num2, cor)
        win.plotPixel(num1 + 1, num2, cor)
        win.plotPixel(num1 + 2, num2, cor)
        win.plotPixel(num1 - 1, num2, cor)
        win.plotPixel(num1, num2 - 1, cor)
        win.plotPixel(num1, num2 - 2, cor)
        win.plotPixel(num1, num2 + 1, cor)
        win.plotPixel(num1 + 1, num2 + 1, cor)
        win.plotPixel(num1 + 1, num2 - 1, cor)
        win.plotPixel(num1 + 1, num2 - 2, cor)
        win.plotPixel(num1 - 1, num2 - 1, cor)
        win.plotPixel(num1 + 2, num2 - 1, cor)
    return


def reta(x1, y1, x2, y2, cor, tam):
    x = x1
    y = y1
    p = 0
    dx = x2 - x1
    dy = y2 - y1
    xInc = 1
    yInc = 1
    if dx < 0:
        xInc = -1
        dx = -dx
    if dy < 0:
        yInc = -1
        dy = -dy
    if dy <= dx:
        p = dx / 2
        while x != x2:
            ponto(x, y, cor, tam)
            p = p - dy
            if p < 0:
                y = y + yInc
                p = p + dx
            x = x + xInc
            continue
    else:
        p = dy / 2
        while y != y2:
            ponto(x, y, cor, tam)
            p = p - dx
            if p < 0:
                x = x + xInc
                p = p + dy
            y = y + yInc
            continue


def pontilhada(x1, y1, x2, y2, cor, tam):
    x = x1
    y = y1
    p = 0
    contador = 0
    dx = x2 - x1
    dy = y2 - y1
    xInc = 1
    yInc = 1
    if dx < 0:
        xInc = -1
        dx = -dx
    if dy < 0:
        yInc = -1
        dy = -dy
    if dy <= dx:
        p = dx / 2
        while x != x2:
            if contador % 10 == 0:
                ponto(x, y, cor, tam)
            contador = contador + 1
            p = p - dy
            if p < 0:
                y = y + yInc
                p = p + dx
            x = x + xInc
            continue
    else:
        p = dy / 2
        while y != y2:
            if contador % 10 == 0:
                ponto(x, y, cor, tam)
            contador = contador + 1
            p = p - dx
            if p < 0:
                x = x + xInc
                p = p + dy
            y = y + yInc
            continue


def tracejada(x1, y1, x2, y2, cor, tam):
    x = x1
    y = y1
    p = 0
    contador = 0
    dx = x2 - x1
    dy = y2 - y1
    xInc = 1
    yInc = 1
    if dx < 0:
        xInc = -1
        dx = -dx
    if dy < 0:
        yInc = -1
        dy = -dy
    if dy <= dx:
        p = dx / 2
        while x != x2:
            if contador < 5:
                ponto(x, y, cor, tam)
            contador = contador + 1

            if contador == 10:
                contador = contador * 0
            p = p - dy
            if p < 0:
                y = y + yInc
                p = p + dx
            x = x + xInc
            continue
    else:
        p = dy / 2
        while y != y2:
            if contador < 5:
                ponto(x, y, cor, tam)
            contador = contador + 1

            if contador == 10:
                contador = contador * 0
            p = p - dx
            if p < 0:
                x = x + xInc
                p = p + dy
            y = y + yInc
            continue


def circulo(xc, yc, r, cor, tam):
    x = 0
    y = r
    p = 5 / 4 - r
    ponto(x, y, cor, tam)
    while x < y:
        x = x + 1
        if p < 0:
            p = (p + (2 * x) + 1)
        else:
            y = y - 1
            p = (p + (2 * x)) + (1 - (2 * y))
            x = x + xc
            y = y + yc

        ponto(x, y, cor, tam)
        ponto(y, x, cor, tam)
        ponto(y, -x, cor, tam)
        ponto(-x, y, cor, tam)
        ponto(-x, -y, cor, tam)
        ponto(-y, -x, cor, tam)
        ponto(-y, x, cor, tam)
        ponto(x, -y, cor, tam)
    return


def texto(x, y, palavra, cor, tamanho, estilo):
    # ==escreve o texto em “palavra” na coordenada (x,y) da tela
    # === obs. Todos os textos estarão na horizontal
    # === use tamanha=10 e estilo= ‘bold’
    num1 = 400 + x
    num2 = -y + 400
    t = Text(Point(num1, num2), palavra)

    t.setOutline(cor)
    t.setSize(tamanho)
    t.setStyle(estilo)
    t.draw(win)
    return


def ProjetarX(X, z, f, F):
    # == calcula a (x ́,y ́) da tela relativa ao ponto (x,y,z) do avião
    # no espaço 3D com o observador à distância F da origem do sistema
    # de coordenadas e o plano projetivo à distância f do observador
    x = X * f / (F - z)
    #   print(X,Y)
    #   ponto(X,Y,'red', 4)
    return x
def ProjetarY( Y, z, f, F):
    # == calcula a (x ́,y ́) da tela relativa ao ponto (x,y,z) do avião
    # no espaço 3D com o observador à distância F da origem do sistema
    # de coordenadas e o plano projetivo à distância f do observador
    y = Y * f / (F - z)
    #   print(X,Y)
    #   ponto(X,Y,'red', 4)
    return  y

def angulacao(x, y):
    m = y / x
    print(m)
    return m


def aviao(X, Y,z,f,F, direcao,palavra):
    x =ProjetarX(X,z,f,F)
    y = ProjetarY(Y,z,f,F)

    if direcao == 'd':
        cor = 'green'
    elif direcao == 'p':
        cor = 'red'
    else:
        cor = 'white'
    if x == 0 and y ==0:
        reta(x, y, x - 20, y, cor, 2)
        ponto(x, y, 'red', 2)
        reta(x - 6, y + 8, x - 6, y - 8, cor, 2)
        reta(x - 16, y + 4, x - 16, y - 4, cor, 2)

    if x == 0:
        dire = 4
        print(dire)
    else:
        dire = angulacao(x,y)
        print(dire)
    if dire >= 3.73:
        if y > 0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x , y -20, cor, 2)
                ponto(x , y , 'red', 2)
                reta(x + 4, y - 15, x - 4, y - 15, cor, 2)
                reta(x + 8, y - 5, x - 8, y - 5, cor, 2)
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x, y - 20, cor, 2)
                ponto(x, y - 20, 'red', 2)
                reta(x + 4, y - 3, x - 4, y - 3, cor, 2)
                reta(x + 8, y - 13, x - 8, y - 13, cor, 2)
        if y < 0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x , y -20, cor, 2)
                ponto(x , y - 20, 'red', 2)
                reta(x + 4, y - 3, x - 4, y - 3, cor, 2)
                reta(x + 8, y - 13, x - 8, y - 13, cor, 2)
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x, y - 20, cor, 2)
                ponto(x, y, 'red', 2)
                reta(x + 4, y - 15, x - 4, y - 15, cor, 2)
                reta(x + 8, y - 5, x - 8, y - 5, cor, 2)
        return
    if 0.28 >= dire >= -0.27:
        if x > 0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 20, y, cor, 2)
                ponto(x, y, 'red', 2)
                reta(x - 6, y + 8, x - 6, y - 8, cor, 2)
                reta(x - 16, y + 4, x - 16, y - 4, cor, 2)
            if  direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 20, y, cor, 2)
                ponto(x - 20, y, 'red', 2)
                reta(x - 3, y + 4, x - 3, y - 4, cor, 2)
                reta(x - 13, y + 8, x - 13, y - 8, cor, 2)
        if x < 0:
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 20, y, cor, 2)
                ponto(x, y, 'red', 2)
                reta(x - 6, y + 8, x - 6, y - 8, cor, 2)
                reta(x - 16, y + 4, x - 16, y - 4, cor, 2)
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 20, y, cor, 2)
                ponto(x - 20, y, 'red', 2)
                reta(x - 3, y + 4, x - 3, y - 4, cor, 2)
                reta(x - 13, y + 8, x - 13, y - 8, cor, 2)
        return
    if 3.73> dire > 0.28:
        if x > 0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x -12, y -12, cor, 2)
                ponto(x , y , 'red', 2)
                reta(x - 12, y -5, x - 3, y - 14, cor, 2)
                reta(x + 3, y - 10, x - 10, y + 4, cor, 2)
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 12, y - 12, cor, 2)
                ponto(x - 12, y - 12, 'red', 2)
                reta(x - 15, y - 2, x - 1, y - 15, cor, 2)
                reta(x + 1, y - 5, x - 5, y + 2, cor, 2)
        if x < 0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x -12, y -12, cor, 2)
                ponto(x-12 , y-12 , 'red', 2)
                reta(x - 15, y -2, x - 1, y - 15, cor, 2)
                reta(x + 1, y - 5, x - 5, y + 2, cor, 2)
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 12, y - 12, cor, 2)
                ponto(x, y, 'red', 2)
                reta(x - 12, y - 5, x - 3, y - 14, cor, 2)
                reta(x + 3, y - 10, x - 10, y + 4, cor, 2)
        return
    if -0.27> dire >-3.73:
        if x >0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x -12, y +12, cor, 2)
                ponto(x , y , 'red', 2)
                reta(x - 12, y + 5, x - 3, y + 14, cor, 2)
                reta(x + 3, y + 10, x - 10, y - 4, cor, 2)
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 12, y + 12, cor, 2)
                ponto(x - 12, y + 12, 'red', 2)
                reta(x - 12, y + 2, x - 1, y + 14, cor, 2)
                reta(x, y + 5, x - 6, y - 1, cor, 2)
        if x <0:
            if direcao == 'd':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x -12, y +12, cor, 2)
                ponto(x -12, y + 12, 'red', 2)
                reta(x - 12, y + 2, x - 1, y + 14, cor, 2)
                reta(x , y + 5, x - 6, y - 1, cor, 2)
            if direcao == 'p':
                texto(x + 20, y + 5, palavra,cor, 10, 'bold')
                reta(x, y, x - 12, y + 12, cor, 2)
                ponto(x, y, 'red', 2)
                reta(x - 12, y + 5, x - 3, y + 14, cor, 2)
                reta(x + 3, y + 10, x - 10, y - 4, cor, 2)
        return



win = GraphWin("Tela Radar", 800, 800, autoflush=False)
win.setBackground("black")
ponto(519, -300, 'red', 4)
pontilhada(360, 0, -360, 0, "gray", 2)
pontilhada(0, 360, 0, -360, "gray", 2)
circulo(0, 0, 90, "gray", 1)
circulo(0, 0, 180, "gray", 1)
circulo(0, 0, 270, "gray", 1)
circulo(0, 0, 360, "gray", 1)
tracejada(-260, -260, 260, 260, "gray", 1)
tracejada(260, -260, -260, 260, "gray", 1)
reta(360, 0, 380, 0, "gray", 2)
reta(-360, 0, -380, 0, "gray", 2)
reta(0, 360, 0, 380, 'gray', 2)
reta(0, -360, 0, -380, 'gray', 2)
reta(-255, -255, -270, -270, 'gray', 2)
reta(-255, 255, -270, 270, 'gray', 2)
reta(255, 255, 270, 270, 'gray', 2)
reta(255, -255, 270, -270, 'gray', 2)

ponto(0, 360, 'blue', 4)


reta(-310, -180, -330, -191, 'gray', 2)
reta(-310, 180, -330, 191, 'gray', 2)
reta(310, -180, 330, -191, 'gray', 2)
reta(310, 180, 330, 191, 'gray', 2)

reta(350, 90, 370, 97, 'gray', 2)
reta(350, -90, 370, -97, 'gray', 2)
reta(-350, 90, -370, 97, 'gray', 2)
reta(-350, -90, -370, -97, 'gray', 2)

reta(170, 320, 179, 337, 'gray', 2)
reta(-170, 320, -179, 337, 'gray', 2)
reta(170, -320, 179, -337, 'gray', 2)
reta(-170, -320, -179, -337, 'gray', 2)

reta(100, 347, 105, 363, 'gray', 2)
reta(-100, 347, -105, 363, 'gray', 2)
reta(100, -347, 105, -363, 'gray', 2)
reta(-100, -347, -105, -363, 'gray', 2)

texto(340, 0, "90o", 'gray', 10, 'bold')
texto(0, 340, "0o", 'gray', 10, 'bold')
texto(-340, 0, "270o", 'gray', 10, 'bold')
texto(0, -340, "180o", 'gray', 10, 'bold')

texto(-290, -180, "240o", 'gray', 10, 'bold')
texto(-290, 180, "300o", 'gray', 10, 'bold')
texto(290, -180, "120o", 'gray', 10, 'bold')
texto(290, 180, "60o", 'gray', 10, 'bold')

texto(330, 90, "75o", 'gray', 10, 'bold')
texto(-330, 90, "285o", 'gray', 10, 'bold')
texto(330, -90, "105o", 'gray', 10, 'bold')
texto(-330, -90, "255o", 'gray', 10, 'bold')

texto(170, 300, "30o", 'gray', 10, 'bold')
texto(-170, 300, "330o", 'gray', 10, 'bold')
texto(170, -300, "150o", 'gray', 10, 'bold')
texto(-170, -300, "210o", 'gray', 10, 'bold')

texto(100, 327, "15o", 'gray', 10, 'bold')
texto(-100, 327, "345o", 'gray', 10, 'bold')
texto(100, -327, "165o", 'gray', 10, 'bold')
texto(-100, -327, "195o", 'gray', 10, 'bold')

texto(240, 240, "45o", 'gray', 10, 'bold')
texto(-240, 240, "315o", 'gray', 10, 'bold')
texto(240, -240, "135o", 'gray', 10, 'bold')
texto(-240, -240, "225o", 'gray', 10, 'bold')




aviao(-12990, 7500, 7500, 100, 15000,'d','oi')





win.getMouse()

