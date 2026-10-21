from PIL import Image
im=Image.open('siripay_4k.png').convert('RGB')
print(im.size)
