from vpython import *
#GlowScript 3.0 VPython

cena1 = canvas(width=1200, height=600, title='Tela 1')
cena1.range = 7

partícula1 = sphere(pos=vector(-10,0,0), color=color.blue, opacity = 0.3, radius = 0.5, make_trail=True, retain=10, trail_type="points")
partícula2 = sphere(pos=vector(-10,0,0), color=color.red, radius = 0.5, make_trail=True, retain=10, trail_type="points")

Início = text(text='Início', align='center', color=color.green, pos=vector(-10,-1,0.5), height = 0.5)
Final = text(text='Final', align='center', color=color.green, pos=vector(10,-1,0.5), height = 0.5)

grafico1 = gcurve(color = color.blue)

while True:
    sleep(1)
    partícula1.pos=vector(-10,0,0)
    partícula2.pos=vector(-10,0,0)
    a=0
    while a < 40:
        rate(20)
        if a <= 10:
            partícula2.pos += vector(0.3, 0.4, 0)
        elif a > 10 and a <= 30:
            partícula2.pos += vector(0.5, -0.4, 0)
        if a > 30:
            partícula2.pos += vector(0.7, 0.4, 0)
        "partícula1.pos.x += 0.49"
        a+=1
    sleep(0.5)
    b = 0   
    while b < 40:
        rate(20)
        partícula1.pos.x += 0.49
        b+=1
    sleep(0.5)
    c=0
    partícula2.pos=vector(-10,0,0)
    partícula1.pos=vector(-10,0,0)
    while c < 40:
        rate(20)
        if c <= 10:
            partícula2.pos += vector(0.3, 0.4, 0)
        elif c > 10 and c <= 30:
            partícula2.pos += vector(0.5, -0.4, 0)
        if c > 30:
            partícula2.pos += vector(0.7, 0.4, 0)
        partícula1.pos.x += 0.49
        c+=1
    sleep(1)