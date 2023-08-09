from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.pdfgen import canvas
from tkinter import Tk, filedialog
from PIL import Image
import os

###############################
# GUI to select an image file #
###############################
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Choose an image file", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
###############################

# If selected...
if file_path:
    # Open the image
    original_img = Image.open(file_path)
    
    # Convert to pixels
    pixels = list(original_img.getdata())
    # Black pixels only
    black_pixels = [pixel for pixel in pixels if pixel == (0, 0, 0)]   
    # Total pixels
    total_pixels = len(pixels)
    
    # Text information
    text_info = [
        f"Number of black pixels {len(black_pixels)}",
        f"Number of all pixels: {total_pixels}",
        f"Perforation ratio: {len(black_pixels)/total_pixels:.5f}"        
    ]


    # Save the image temporarily
    temp_image_path = "temp_img.png"
    original_img.save(temp_image_path)   

##################
# PDF Operations #
##################

    # Create PDF
    page_size = landscape(A4)

    output_path_pdf = os.path.join(os.path.dirname(file_path), "combined_" + os.path.splitext(os.path.basename(file_path))[0] + ".pdf")
    c = canvas.Canvas(output_path_pdf, pagesize=page_size)
    page_width, page_height = page_size
    
    # Scale factor to resize an image
    if original_img.width < page_width:
        scale_factor = 1
    else:
        scale_factor = (page_width-10) / original_img.width
    
    resized_img_width = int(original_img.width * scale_factor)
    resized_img_height = int(original_img.height * scale_factor)
    resized_img = original_img.resize((resized_img_width, resized_img_height))
    
    # Insert the image into the PDF
    x_draw = (page_width - resized_img_width) / 2 # centered
    y_draw = page_height - resized_img_height

    c.drawImage(temp_image_path, x_draw, y_draw - 5, width=resized_img.width, height=resized_img.height)

    # Insert text_info into the PDF as actual text
    text_object = c.beginText(10, y_draw - 30)  # Adjusting coordinates
    text_object.setFont("Times-Roman", 14)
    for line in text_info:
        text_object.textLine(line)
    c.drawText(text_object)

    # Save the PDF
    c.save()

    # Cleanup
    os.remove(temp_image_path)

    print(f"PDF saved to {output_path_pdf}")
    for line in text_info:
        print(line)

else:
    print("File was not selected.")
