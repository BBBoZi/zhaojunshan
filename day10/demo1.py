try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

captcha1 = Image.open("captcha1.png")
result = pytesseract.image_to_string(captcha1)
print(result)

captcha2 = Image.open("captcha2.png")
result = pytesseract.image_to_string(captcha2)
print(result)


