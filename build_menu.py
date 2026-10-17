from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import cv2
import html

ROOT=Path('regaloo-menu'); A=ROOT/'assets'
for d in ['logo','food','drinks','icons','backgrounds']: (A/d).mkdir(parents=True,exist_ok=True)
im=Image.open(r'C:\Users\hp\Downloads\Menu Regaloo _ Fast-Food & Pizzas.png').convert('RGB')
S=im.width/576
def extract(name,box,poly=None,clean=True):
    box=tuple(round(v*S) for v in box); pic=im.crop(box).convert('RGBA'); w,h=pic.size
    mask=Image.new('L',(w,h),0)
    if poly: ImageDraw.Draw(mask).polygon([(round(x*S),round(y*S)) for x,y in poly],fill=255)
    else: ImageDraw.Draw(mask).ellipse((1,1,w-2,h-2),fill=255)
    if clean:
        rgb=np.array(pic)[:,:,:3]; dark=(rgb.max(2)<96).astype('uint8')
        outside=(np.array(mask)==0); candidates=(dark|outside).astype('uint8')
        n,lab=cv2.connectedComponents(candidates)
        edge=np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1],lab[outside]])); edge=edge[edge!=0]
        m=np.array(mask); m[np.isin(lab,edge)]=0; mask=Image.fromarray(m)
    pic.putalpha(mask.filter(ImageFilter.GaussianBlur(.45))); pic.save(A/(name+'.png'))

extract('logo/regaloo',(43,10,247,207),clean=False)
assets=[
('salad',(35,210,257,302),[(2,50),(30,18),(91,0),(159,10),(220,43),(211,73),(169,91),(63,88),(9,70)]),
('pizza',(275,178,560,319),[(0,80),(20,31),(88,0),(179,5),(243,37),(280,77),(284,123),(255,140),(177,128),(58,120)]),
('tacos',(25,414,265,510),[(0,70),(18,24),(49,0),(135,9),(207,30),(239,66),(228,94),(95,88)]),
('burger',(20,626,164,730),[(2,91),(16,56),(24,15),(70,0),(115,11),(127,52),(142,86),(119,103),(29,103)]),
('baguetto',(327,610,557,690),[(0,54),(15,23),(52,0),(145,3),(211,22),(230,55),(220,77),(30,79)]),
('crispy-chicken',(17,810,148,891),[(0,49),(20,21),(56,0),(99,5),(127,28),(130,59),(111,79),(34,80)]),
('sandwich',(28,980,259,1054),[(0,48),(14,12),(91,0),(195,8),(226,28),(230,55),(207,71),(24,73)]),
('chicken-platter',(333,801,555,885),[(0,55),(22,9),(72,0),(115,8),(165,17),(199,18),(219,44),(220,73),(184,83),(50,82)]),
('pasta',(309,961,535,1057),[(0,57),(25,23),(76,0),(146,6),(202,33),(225,60),(211,82),(158,95),(57,91)]),
('crousty',(22,1208,144,1310),[(0,63),(15,27),(40,0),(79,8),(115,35),(121,73),(103,95),(48,101),(13,85)]),
('fries',(312,1211,404,1294),[(0,36),(10,9),(32,0),(65,9),(90,39),(84,68),(66,81),(29,80),(7,67)])]
for name,box,poly in assets: extract('food/'+name,box,poly)
for name,box,poly in [
('beetroot',(425,1385,566,1520),[(0,100),(8,61),(32,7),(76,0),(112,22),(123,67),(140,111),(115,134),(28,132)]),
('lemon',(306,1512,413,1633),[(0,91),(13,46),(27,0),(82,5),(88,64),(106,95),(84,120),(20,115)]),
('carrot',(421,1657,566,1783),[(0,111),(45,84),(52,8),(105,0),(119,63),(144,97),(140,119),(81,125)]),
('orange',(20,1637,160,1757),[(0,84),(37,39),(54,0),(96,3),(99,83),(139,107),(109,119),(38,115)]),
('avocado',(121,1638,220,1758),[(0,91),(33,58),(39,0),(80,9),(92,107),(60,120),(8,112)]),
('strawberry',(201,1645,340,1773),[(0,88),(21,45),(25,12),(59,0),(84,48),(138,92),(128,121),(72,127),(16,117)]),
('pepsi',(300,1794,354,1910),None),('oulmes',(351,1801,406,1912),None),('orange-soda',(402,1810,452,1912),None),('water',(456,1785,505,1912),None),('small-water',(505,1832,542,1912),None)]: extract('drinks/'+name,box,poly)
extract('icons/scooter',(406,1914,563,2034),[(0,68),(23,55),(58,8),(82,0),(99,17),(94,45),(113,69),(155,101),(144,119),(21,118),(0,98)])
im.crop(tuple(round(v*S) for v in (267,340,282,604))).save(A/'backgrounds/wood.jpg')
(A/'icons/brush.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 60" preserveAspectRatio="none"><path fill="#ff7900" d="M18 5 74 2 65 0 243 3 280 7 266 12 296 16 280 20 300 24 280 28 292 32 278 37 292 41 269 45 280 50 221 54 231 58 92 57 56 60 62 55 4 54 20 49 0 45 19 39 7 35 25 31 1 26 24 22 8 18 27 13 14 10Z"/></svg>''')
(A/'icons/phone.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="none" stroke="#111" stroke-width="3"/><path fill="#111" d="m9 7 5 6-3 3 5 5 3-3 6 4c-4 9-21-5-16-15Z"/><path d="M18 7q7 0 7 8m-7-4q3 0 3 4" fill="none" stroke="#111" stroke-width="2"/></svg>''')

cats={
'Salade':[('Salade Marocaine',15),('Salade Pate',20),('Mexicaine',20)],
'Tacos':[('Crispy',30),('Poulet',30),('Viande hachée',32),('Mixte',32)],
'Burger':[('Cheese Burger',25),('Chicken Burger',25),('Spécial Burger',30)],
'Pactic cio':[('Crispy',30),('Viande hachée',35),('Poulet',30),('Mixte',35)],
'Sandwich':[('Thon',13),('Omlette',13),('Crispy Frite',17),('Viande hachée',20),('Poulet',18)],
'Crousty':[('Crispy Frite',30),('Viande hachée',35),('Poulet',30)],
'Pizza':[('Pizza Margherita',20),('Pizza Thon',25),('Pizza Poulet',25),('Pizza Viande Hachée',30),('Pizza Fruits de Mer',40),('Pizza 4 Saison',40),('Pizza REGALOO',40),('Pizza pipironi',30),('Pizza charcuterie',30),('Pizza 4 fromage',40),('Pizza Crispy',30)],
'Baguetto':[('Crispy',30),('Viande Hachée',35),('Poulet',30)],
'Plats':[('Crispy',30)],
'Pate':[('Poulet',30),('Bolognaise',35),('Carbonara',35),('Fruit de mer',40)],
'Supplément':[('Frite',6),('Thon',8),('Fromage',10)],
'Jus':[('Orange',15),('Pomme',13),('Banane orange',15),('Banane au lait',13),('Avocat',20),('Avocat fruit sec',25),('Panmaché orange',18),('Panaché au lait',15),('Mangue',20),('Fraise',18)],
'Boisson':[('Pepsi',6),('Oulmes Tropical',10),('Oulmes',7),('Eau petit',3),('Eau grand',6)]}
def rows(name):
    return '<ul>'+''.join(f'<li><span>{html.escape(n)}</span><i aria-hidden="true"></i><strong>{p:02d} dh</strong></li>' for n,p in cats[name])+'</ul>'
def section(name,photo,side=False):
    return f'<section class="category {"side-photo" if side else ""}"><div class="category-top"><img src="assets/food/{photo}.png" alt="{name}" width="300" height="150"><h2>{name}</h2></div>{rows(name)}</section>'
left=''.join(section(*v) for v in [('Salade','salad'),('Tacos','tacos'),('Burger','burger',True),('Pactic cio','crispy-chicken',True),('Sandwich','sandwich'),('Crousty','crousty',True)])
right=''.join(section(*v) for v in [('Pizza','pizza'),('Baguetto','baguetto'),('Plats','chicken-platter'),('Pate','pasta'),('Supplément','fries',True)])
special=''.join(f'<div class="special {n}"><div class="bubble">Jus de<br>{label}</div><img src="assets/drinks/{n}.png" alt="Jus de {label}">{"<strong>8dh</strong>" if n=="lemon" else ""}</div>' for n,label in [('beetroot','betterave'),('lemon','citron'),('carrot','carotte')])
drinkimgs=''.join(f'<img src="assets/drinks/{n}.png" alt="{n}" width="100" height="200">' for n in ['pepsi','oulmes','orange-soda','water','small-water'])
(ROOT/'index.html').write_text(f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#ff7900"><meta name="description" content="Le menu REGALOO : pizzas, tacos, burgers, plats et jus. Livraison au 07 87 14 26 24."><title>Menu Regaloo | Fast-Food &amp; Pizzas</title><link rel="stylesheet" href="style.css"></head>
<body><main class="menu"><header><img class="logo" src="assets/logo/regaloo.png" alt="REGALOO — Fast Food & Pizza" width="235" height="227"><div class="heading"><h1>Menu</h1><span class="underline"></span><p>FAST<br>FOOD<br><em>GOOD<br>MOOD !</em></p></div></header>
<div class="food-grid"><div class="column">{left}</div><div class="column">{right}</div></div>
<div class="drinks-grid"><div class="juice"><section class="category"><h2>Jus</h2>{rows('Jus')}</section><div class="juice-photos"><img src="assets/drinks/orange.png" alt="Jus d’orange"><img src="assets/drinks/avocado.png" alt="Jus d’avocat"><img src="assets/drinks/strawberry.png" alt="Jus de fraise"></div></div><aside class="specials" aria-label="Jus frais">{special}</aside></div>
<div class="beverages"><section class="category"><h2>Boisson</h2>{rows('Boisson')}</section><div class="bottles">{drinkimgs}</div></div>
<footer><p class="delivery">Livraison<br>disponible</p><span class="arrow" aria-hidden="true">⤳</span><a href="tel:+212787142624"><img src="assets/icons/phone.svg" alt="Téléphone">07 87 14 26 24</a><img class="scooter" src="assets/icons/scooter.png" alt="Livraison en scooter"></footer></main></body></html>''',encoding='utf-8')
