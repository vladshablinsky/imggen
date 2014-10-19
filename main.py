import random
from PIL import Image, ImageDraw  

image = Image.new("RGB", (1000, 1000))
draw = ImageDraw.Draw(image)  
height = image.size[0]
width = image.size[1]

x = int(input("give sum delta\n"))
k = int(input("give k\n"))
r = int(input("give r\n"))
g = int(input("give g\n"))
b = int(input("give b\n"))

# TODO : read from file

for i in range(0, width, k):
    for j in range(0, height, k):
        sumdelta = 0
        if r >= x:
            mn = -x
        else:
            mn = -r
        if r <= 255 - x:
            mx = x
        else:
            mx = 255 - r
        rr = r + random.randint(mn, mx)
        sumdelta += abs(r - rr)
        #red component is ready
        if g >= x - sumdelta:
            mn = x - sumdelta
        else:
            mn = -g
        if r <= 255 - (x - sumdelta):
            mx = x - sumdelta
        else:
            mx = 255 - g
        gg = g + random.randint(mn, mx)
        sumdelta += abs(g - gg)
        #green component is ready
        if b >= x - sumdelta:
            mn = x - sumdelta
        else:
            mn = -b
        if b <= 255 - (x - sumdelta):
            mx = x - sumdelta
        else:
            mx = 255 - b
        bb = b + random.randint(mn, mx)
        draw.polygon([(i, j), (i + k, j), (i + k, j + k), (i, j + k)], fill = (rr, gg, bb))
    draw.polygon([(800, 800), (800, 1000), (1000, 1000), (1000,800)], fill = (r, g, b))
    
image.save("ans.png", "PNG")
del draw
