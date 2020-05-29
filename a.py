# Sergio Patrick Hirayama Trautmann
# João Pedro Almeida de Oliveira
from graphics import *

zbufer = []
def matriz():
    b = []
    zbufer = []
    a = 0

    for l in range(800):
        a +=1
        b.append(a)
        for i in range(10):
            for i in range(8):
                zbufer.append(b)
    print(b)
    print(zbufer)


def ponto(x,y,cor,tam):

    num1 = 400 + x
    num2 = -y + 400

    if tam == 1:
        win.plotPixel(num1,num2,cor)
    elif tam == 2:
        win.plotPixel(num1,   num2,   cor)
        win.plotPixel(num1+1, num2,   cor)
        win.plotPixel(num1,   num2-1, cor)
        win.plotPixel(num1+1, num2-1, cor)
    elif tam == 3:
        win.plotPixel(num1,   num2,   cor)
        win.plotPixel(num1+1, num2,   cor)
        win.plotPixel(num1-1, num2,   cor)
        win.plotPixel(num1, num2+1,   cor)
        win.plotPixel(num1, num2-1,   cor)
    elif tam == 4:
        win.plotPixel(num1,   num2,   cor)
        win.plotPixel(num1+1, num2,   cor)
        win.plotPixel(num1+2, num2,   cor)
        win.plotPixel(num1-1, num2,   cor)
        win.plotPixel(num1, num2-1,   cor)
        win.plotPixel(num1, num2-2,   cor)
        win.plotPixel(num1, num2+1,   cor)
        win.plotPixel(num1+1, num2+1,   cor)
        win.plotPixel(num1+1,  num2-1, cor)
        win.plotPixel(num1+1, num2-2, cor)
        win.plotPixel(num1-1, num2-1, cor)
        win.plotPixel(num1+2, num2-1, cor)
    return

def reta (x1, y1, x2, y2, cor, tam):
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
            p = dx/2
            while x != x2:
                ponto(x, y, cor, tam)
                p = p - dy
                if p < 0:
                    y = y + yInc
                    p = p + dx
                x = x + xInc
                continue
        else:
            p = dy/2
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

def tracejada (x1, y1, x2, y2, cor, tam):
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
    p = 5/4 - r
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


def texto( x, y, palavra, cor, tamanho, estilo):
    # ==escreve o texto em “palavra” na coordenada (x,y) da tela
    # === obs. Todos os textos estarão na horizontal
    # === use tamanha=10 e estilo= ‘bold’
    t = Text(Point(x, y), palavra)

    t.setOutline(cor)
    t.setSize(tamanho)
    t.setStyle(estilo)
    t.draw(win)
    return

def Projetar(x,y,z,f, F,cor, tam):
    # == calcula a (x ́,y ́) da tela relativa ao ponto (x,y,z) do avião
    #no espaço 3D com o observador à distância F da origem do sistema
    #de coordenadas e o plano projetivo à distância f do observador
    X = x * f/(F-z)
    Y = y * f/(F-z)
    ponto(X, Y, cor, tam)
    return

def Tela_Fundo(win):
    win.close()
    win = GraphWin("Tela Radar", 800, 800)
    win.setBackground("black")
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
    return
def clear(win):
    texto.undraw(win)
    win.update()
    return
matriz()

win = GraphWin("Tela Radar", 800, 800, autoflush=False)
win.setBackground("black")
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




reta(-310,-180,-330,-191,'gray',2)
reta(-310,180,-330,191,'gray',2)
reta(310,-180,330,-191,'gray',2)
reta(310,180,330,191,'gray',2)

reta(350,90,370,97,'gray',2)
reta(350,-90,370,-97,'gray',2)
reta(-350,90,-370,97,'gray',2)
reta(-350,-90,-370,-97,'gray',2)

reta(170,320,179,337,'gray',2)
reta(-170,320,-179,337,'gray',2)
reta(170,-320,179,-337,'gray',2)
reta(-170,-320,-179,-337,'gray',2)

reta(100,347,105,363,'gray',2)
reta(-100,347,-105,363,'gray',2)
reta(100,-347,105,-363,'gray',2)
reta(-100,-347,-105,-363,'gray',2)
texto(665, 300, "90o", 'red', 10, 'bold')
Projetar(100,200,300,10,500,3,'red')

print(zbufer[0][0])

win.getMouse()
