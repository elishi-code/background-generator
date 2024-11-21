from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save("sharpen.png", 'png')
# filtered_img = img.convert('L')
# filtered_img.save("grey.png", 'png')
# filtered_img.show()
# filtered_img = img.rotate(90)
# filtered_img.save("rotate.png", 'png')
# filtered_img = img.resize((300, 300))
# filtered_img.save("resize.png", 'png')
# box = (0, 0, 300, 300)
# region = img.crop(box)
# region.save("crop.png", 'png')

img = Image.open('./Pokedex/astro.jpg')
img.thumbnail((400, 400))
img.save("thumbnail.jpg")

