from vpython import *
#GlowScript 2.9 VPython

scene.center = vector(0,0,2.5)
scene.width = 1300
scene.height = 650
scene.forward = vector(-0.5,-0.5,-1)
scene.range = 30

#botões
running = True
def Run(b):
    global running
    running = not running
    if running: b.text = "Pausar"
    else: b.text = "Ligar" 
b = button(text="Liga / Pausar", pos=scene.caption_anchor, bind=Run)

#medidas da fenda e esfera
L = 5
L5 = 5*L
e = 0.1 #espessura da fenda
r = L/50 #raio da esfera

#eixos cartesianos
pointerx = arrow(pos=vector(0,0,0), axis=vector(L5,0,0), shaftwidth=0.1, 
                    headwidth = 0.1, headlength = 0.1, color=color.red)
pointery = arrow(pos=vector(0,0,0), axis=vector(0,L5,0), shaftwidth=0.1, 
                    headwidth = 0.1, headlength = 0.1, color=color.green)
pointerz = arrow(pos=vector(0,0,0), axis=vector(0,0,L5), shaftwidth=0.1, 
                    headwidth = 0.1, headlength = 0.1, color=color.blue)

#fenda
parede1 = box(pos=vector(L,L/2,L/6), length=e, height=L, width=L/3)
parede3 = box(pos=vector(L,L/2,L/2), length=e, height=L, width=L/9)
parede5 = box(pos=vector(L,L/2,5*L/6), length=e, height=L, width=L/3)
muro = box(pos=vector(L5,L/2,L/2), length=e, height=L, width=10*L5, color=color.blue)

#propriedades das partículas
dt = 0.1
x0, y0, z0 = 0,0,0
ri = vector(x0, y0, z0)
n = 50 #raiz quadrada do número de partículas
partículas = []
for i in range(0, n):
    for j in range(0, n):
        partículas.append(sphere(pos=vector(ri), radius=r, color=color.green)) #make_trail=True, retain=100, trail_radius=0.3*r))
        ri += vector(0,0,L/10)
        if ri.z > L:
            ri = vector(0,0,0)
    ri += vector(0,L/10,0)
    ri.z = 0
    
for i in range(n**2):
    partículas[i].mass = 1
    partículas[i].p = vector(random(),random() , random())

#looping de animação
while True:
    rate(300) # Number of frames/loops per second.
    if running: #botão para pausar        
        #partícula1
        #condições de colisão com a parede
        for i in range(n**2):
            partículas[i].pos = partículas[i].pos + (partículas[i].p/partículas[i].mass)*dt
            if partículas[i].pos.x < L + e/2:
                if (partículas[i].pos.x < 0):
                    partículas[i].p.x = -partículas[i].p.x
                if ((partículas[i].pos.z < 0) or (partículas[i].pos.z > L)):
                    partículas[i].p.z = -partículas[i].p.z             
            if ((partículas[i].pos.y < 0) or (partículas[i].pos.y > L)):
                    partículas[i].p.y = -partículas[i].p.y
            if (partículas[i].pos.x > L5):  
                 partículas[i].p = vector(0,0,0)
            if (partículas[i].pos.x > L and partículas[i].pos.x < L + e/2):
                #condições de colisão com a fenda
                if ( ((partículas[i].pos.z < 2*L/3) and (partículas[i].pos.z > 5*L/9) or ((partículas[i].pos.z < 4*L/9) and (partículas[i].pos.z > L/3)))):
                    partículas[i].p = partículas[i].p
                else:
                    partículas[i].p.x = -partículas[i].p.x
#                    partículas[i].p = vector(random(), random(), random()) #a colisão com a fenda é aleatória
                    
                    
                    
                    
                    
                    
                    
                    
                    