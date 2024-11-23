from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import os


#ascii_map = [" ","`",".","'",",","~",":",";","•","^","!","*","-","_",">","<","i","l","(",")","[","]","f","j","e","r","u","b","c","s","{","}","/","|","I","J","p","?","÷","π","§","A","C","7","V","X","D","Q","2","E","R","6","Z","5","K","&","3","8","%","$","#","@","W","M"]
ascii_map = list(reversed([
    " ", ".", "`", "'", ",", ":", ";", "-", "_", "^", "~", "<", ">", "(", ")", 
    "[", "]", "{", "}", "/", "|", "°","≪", "≡", "i", "l", "!", "?", "f", "j", "r", "t", "z", "o", 
    "q", "y", "w", "u", "v", "x", "a", "s", "c", "k", "d", "g", "*", "+", "n","m", 
    "b", "e", "T", "F", "Y", "L", "I", "J", "P", "U", "O", "X", "V", "C", "A", "K", 
    "H", "E", "Z", "Q", "R", "2", "4", "5", "6", "7", "9", "&", "%",  
    "∞", "€", "£","§", "√", "∆", "∑", "≅", "∫",  "⊂", "⊃", "∩", 
    "⊥", "∃", "∀", "λ", "π", "μ", "η", "θ", "χ", "ξ", "ψ", "ϕ", "β", "δ", "ζ", 
    "τ", "φ", "ω", "Δ", "Π", "Ω", "Θ", "Φ", "Ξ", "Σ", "Λ", "Γ", "X", "W", "M", 
    "B", "G", "0","#","$","@","¶", 
]))
def ascii_gen(filepath):
    MAX_SIZE = (90,90)
    img = Image.open(filepath)
    processed_img = ImageEnhance.Contrast(img).enhance(1.7)
    resized = processed_img.resize(MAX_SIZE) 
    img_array = np.asarray(resized)
    img_lst = img_array.tolist()
    bw_img_array = convert_to_greyscale(img_lst)
    
    for line in bw_img_array:
        ascii_line = []
        for pixel in line:
            item = ascii_map[ pixel[0]//2]
            ascii_line.append(item)
        print(*ascii_line)

def convert_to_greyscale(img_array):
    result = []
    for line in img_array:
        result.append([[sum(x)//3]*3 for x in line])
    return result


    

if __name__ == "__main__":
    dir_path = "./test_images"
    for file in os.listdir(dir_path):
        full_path = os.path.join(dir_path, file)
        ascii_gen(full_path)
        print(*[" "]*90)
        print(*[" "]*90)
