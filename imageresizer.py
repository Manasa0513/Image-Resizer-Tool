import os
from PIL import Image
def resize_and_convert_images(input_folder, output_folder, width, height, output_format="JPEG"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")):
            input_path = os.path.join(input_folder, filename)
            with Image.open(input_path) as img:
                resized_img = img.resize((width, height))
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{base_name}.{output_format.lower()}"
                output_path = os.path.join(output_folder, output_filename)
                resized_img.save(output_path, output_format)
                print(f"Saved: {output_path}")
if __name__ == "__main__":
    input_folder = r"c:\Users\Manasa\OneDrive\Desktop\images"      
    output_folder = r"c:\Users\Manasa\OneDrive\Desktop\resized"   
    w = int(input("Enter new width: "))
    h = int(input("Enter new height: "))
    fmt = input("Enter output format (JPEG/PNG): ").upper()
    resize_and_convert_images(input_folder, output_folder, w, h, fmt)