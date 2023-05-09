from PIL import Image
import re

def txt2img3(txt,ename):
    bits=''
    for i in txt:
        c=str(bin(ord(i))[2:])
        padding=''
        if len(c)%8!=0:
            for i in range(0,8-len(c)%8):
                padding=padding+"0"
        #print((c,padding))
        bits=bits+padding+c
    #print(bits)

    img=Image.open(ename)
    #print(bits)
    img_width, img_height = img.size   
    bit_index = 0
    # iterate over the pixels and set the color based on the bit value
    for y in range(img_height):
        for x in range(img_width):
            try:
                bit_value = int(bits[bit_index])
                current=img.getpixel((x, y))
                nz=bin(current[2])
                nz=nz[2:len(nz)-1]
                nz=nz+str(bit_value)
                newz=int(nz,2)
                bit_index = bit_index+1

                bit_value = int(bits[bit_index])
                ny=bin(current[1])
                ny=ny[2:len(nz)-1]
                ny=ny+str(bit_value)
                newy=int(ny,2)
                bit_index = bit_index+1

                bit_value = int(bits[bit_index])
                nx=bin(current[0])
                nx=ny[2:len(nz)-1]
                nx=nx+str(bit_value)
                newx=int(nx,2)
                bit_index = bit_index+1

                #print(nh,current[2])
                img.putpixel((x, y), (newx,newy,newz))
            except:
                bit_value = 0
                current=img.getpixel((x, y))
                nz=bin(current[2])
                nz=nz[2:len(nz)-1]
                nz=nz+str(bit_value)
                newz=int(nz,2)
                bit_index = bit_index+1

                bit_value = 0
                ny=bin(current[1])
                ny=ny[2:len(nz)-1]
                ny=ny+str(bit_value)
                newy=int(ny,2)
                bit_index = bit_index+1

                bit_value = 0
                nx=bin(current[0])
                nx=ny[2:len(nz)-1]
                nx=nx+str(bit_value)
                newx=int(nx,2)
                bit_index = bit_index+1
                #print(nh,current[2])
                img.putpixel((x, y), (newx,newy,newz))

    return img

def decode3(sname):
    img=Image.open(sname)
    #print(bits)
    img_width, img_height = img.size   
    bit_index = 0
    bits=''
    for y in range(img_height):
        for x in range(img_width):
            current=img.getpixel((x, y))
            nz=bin(current[2])
            bits=bits+nz[-1]
            ny=bin(current[1])
            bits=bits+ny[-1]
            nx=bin(current[0])
            bits=bits+nx[-1]
    return bits

def bits2ascii3(bits):
    s=''
    l=re.findall('........',bits)
    for i in l:
        s=s+chr(int(i,2))
    return s
