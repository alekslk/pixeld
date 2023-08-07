from tkinter import Tk, filedialog
from PIL import Image

root = Tk()
root.withdraw()

# GUI to select an image file
file_path = filedialog.askopenfilename(title="Choose an image file", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])

# If selected...
if file_path:
    # Open the image
    img = Image.open(file_path)
    
    # Convert to pixels
    pixels = list(img.getdata())
    # Black pixels only
    black_pixels = [pixel for pixel in pixels if pixel == (0, 0, 0)]   
    # Total pixels
    total_pixels = len(pixels)
    
    print(f"Perforation ration is: {len(black_pixels)/total_pixels}")

else:
    print("File was not selected.")
