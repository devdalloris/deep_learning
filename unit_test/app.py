def calculate_area(width, height):
    if width < 0 or height <0:
        raise ValueError("Ширина и высота должны быть неотрицательными.")
    return width * height

def is_palindrome(text):
    clean_text = ''.join(filter(str.isalnum, text)).lower()
    return clean_text == clean_text[::-1]
