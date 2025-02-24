import os
import shutil
import time

def file_sorter():
    # Ask user for the target directory
    directory = input("Enter the directory path: ")

    # Ensure the directory exists
    if not os.path.exists(directory):
        print("Directory does not exist.")
        exit()

    # Loop through files in the directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1][1:].lower()  # Get extension without dot

            if ext:  # Ensure it's not an empty extension (e.g., hidden files)
                # Define the "images" directory
                images_folder = os.path.join(directory, "images")
                os.makedirs(images_folder, exist_ok=True)

                # Check if it's an image file
                image_formats = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "heic", "webp"]
                if ext in image_formats:
                    ext_folder = os.path.join(images_folder, ext)  # Subfolder for each format
                    if not os.path.exists(ext_folder):
                        os.makedirs(ext_folder)
                    shutil.move(file_path, os.path.join(ext_folder, file))
                else:
                    # Organize non-image files based on their extension
                    ext_folder = os.path.join(directory, ext)
                    if not os.path.exists(ext_folder):
                        os.makedirs(ext_folder)
                    shutil.move(file_path, os.path.join(ext_folder, file))

                print(f"Moved {file} to {ext_folder}/")
                time.sleep(10)

    print("File sorting complete.")

file_sorter()
