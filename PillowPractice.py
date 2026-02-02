from PIL import Image ,ImageDraw,ImageFont,ImageFilter

# for opening an image
img = Image.open("photo.jpg")
# img.show()
# print(img.size)   # (width, height)
# print(img.mode)   # RGB, RGBA, L, etc
# print(img.format) # JPEG, PNG


# from PIL import Image

# img = Image.new("RGB", (3000, 500), color="white")

# for daving an image
# img.save("output.png")
# img.save("output.jpg", quality=95)

# for drawing shapes
draw = ImageDraw.Draw(img)
# draw.line((1000, 400, 1001, -123), fill="black", width=3)
# draw.rectangle((50, 50, 200, 150), fill="black",outline="blue", width=3)
# draw.ellipse((1000, 100, 1100, 200), outline="red", width=2)


# font = ImageFont.truetype("fonts/IndieFlower-Regular.ttf", 40)
# draw.text((50, 50), "Hello World", fill="black", font=font)

# font = ImageFont.truetype("fonts/Handlee-Regular.ttf", 40)
# draw.text((2000, 50), "Hello World", fill="black", font=font)

# text = "This is a long sentence"
# x, y = 20, 20

# for line in text.split():
#     draw.text((x, y), line, font=font, fill="black")
#     y += 45

# img = img.resize((300, 300))
# img.thumbnail((300, 300))
# img = img.crop((20, 100, 400, 200))
# crop follow a rule right > left    bottom > top

# img.rotate(45)
# img.transpose(Image.FLIP_LEFT_RIGHT)
# img.transpose(Image.FLIP_TOP_BOTTOM)

# img.filter(ImageFilter.BLUR)
# img.filter(ImageFilter.SHARPEN)
# img.filter(ImageFilter.EDGE_ENHANCE)




img.show()
