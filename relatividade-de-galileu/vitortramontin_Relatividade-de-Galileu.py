from vpython import *
#GlowScript 2.9 VPython

cena1 = canvas(width=800, height=300, title='Tela 1')
cena2 = canvas(width=800, height=300, title='Tela 2')
cena1.range = 4
cena2.range = 4

partícula1 = sphere(pos=vector(0,0,0), color=color.blue, radius = 0.1, canvas = cena1)
parede1 = box(pos = vector(0,0,-1), size=vector(4, 2, 0.4),  color = color.red, canvas = cena1)
partícula2 = sphere(pos=vector(0,0,0), color=color.blue, radius = 0.1, canvas=cena2)
parede2 = box(pos = vector(0,0,-1), size=vector(4, 2, 0.4),  color = color.red, canvas=cena2)


a=0
while a < 10:
    rate(10)
    partícula1.pos.x += 0.1
    partícula2.pos.x += 0.1
    a+=0.1
    cena1.center = partícula1.pos #a câmera se movimenta junto com a bolinha
    
    
    
    
    
    
    
    