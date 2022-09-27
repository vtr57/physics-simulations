from vpython import *
#GlowScript 3.0 VPython

cena1 = canvas(width=1200, height=600, title='Tela 1')
cena1.range = 35

partícula1 = sphere(pos=vector(-50,0,0), color=color.blue, opacity = 0.3, radius = 2, make_trail=True, retain=10, trail_type="points")
partícula2 = sphere(pos=vector(-50,0,0), color=color.red, radius = 2, make_trail=True, retain=10, trail_type="points")
mybox = box(pos=vector(55,0,0), length=0.1, height=50, width=50, color=vector(1.000, 0.926, 0.000))

Início = text(text='Início', align='center', color=color.green, pos=vector(-50,-5,0.5), height = 2)
Final = text(text='Final', align='center', color=color.green, pos=vector(0,-5,0.5), height = 2)

while True:
    sleep(1)
    partícula1.pos = vector(-50,0,0)
    partícula2.pos = vector(-50,0,0)
    a=0
    while a < 10:
        rate(20)
        if a < 5:
            partícula2.pos.x += 1.99
        else:
            partícula2.pos.x += -0.999
        a+=0.1

    sleep(0.5)

    b = 0   
    while b < 10:
        rate(20)
        partícula1.pos.x += 0.51
        b+=0.1

    sleep(0.5)

    c=0
    partícula2.pos=vector(-50,0,0)
    "partícula2.make_trail = False"
    partícula1.pos=vector(-50,0,0)
    while c < 10:
        rate(20)
        if c < 5:
            partícula2.pos.x += 1.99
        else:
            partícula2.pos.x += -0.999
        partícula1.pos.x += 0.51
        c+=0.1
    sleep(1)