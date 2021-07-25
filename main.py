from PIL import Image
import sys

chars = ('.', ',', ';', '!', 'v', 'l', 'L', 'F', 'E', '$', '#', '@')

if len(sys.argv) < 2:
    print('ascii-generator on!')
    exit(1)
img = Image.open(sys.argv[1])
img = img.convert('L')
(x_size, y_size) = img.size

if x_size < 100 or y_size < 100:
    print('Size is too small.')
    print('Must each side length is bigger than 100px')
    exit(1)

r = open('result.txt', 'w')

im_s = img.resize((x_size//5, y_size//10), Image.BICUBIC)
for y in range(im_s.size[1]):
    for x in range(im_s.size[0]):
        gs = im_s.getpixel((x,y))
        print(chars[int(gs/256*len(chars))], end="")
        r.write(chars[int(gs/256*len(chars))])
    print('\n', end="")
    r.write('\n')