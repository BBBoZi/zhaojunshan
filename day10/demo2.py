try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

captcha3 = Image.open("captcha3.png")


def convert_img(img,threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

convert_img(captcha3,150)
print(convert_img(captcha3,150))

result = pytesseract.image_to_string(captcha3)
print(result)
