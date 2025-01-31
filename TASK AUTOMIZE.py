
"""
This program automates the process of sorting your files into different folders based on their extensions,
making it easier for you to organize your data. It handles the following tasks:

1. Loops through all the files in the specified source folder.
2. Identifies the file extension (e.g., .txt, .jpg, .pdf).
3. Creates corresponding folders (e.g., "Text_Files", "Images", etc.) if they don't already exist.
4. Moves the files to the appropriate folders based on their extension.
5. Prints messages to inform you of the files being moved and when the process is complete.

The program saves time and effort by automatically organizing files, ensuring that your folder structure remains neat and well-ordered.
"""

import os
import shutil

# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to organize files by extension
def organize_files_by_extension(source_folder):
    # Define the extension to folder mapping
    extensions_folders = {
        ".txt": "Text_Files",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".pdf": "PDF_Files",
        ".docx": "Word_Files",
        ".xlsx": "Excel_Files",
        ".mp3": "Audio_Files",
    }

    # Loop through all files in the folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # If it's a file and not a directory
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()

            # Check if the extension is in our mapping
            if file_extension in extensions_folders:
                # Get the folder name corresponding to the extension
                folder_name = extensions_folders[file_extension]

                # Create the folder if it doesn't exist
                folder_path = os.path.join(source_folder, folder_name)
                create_folder(folder_path)

                # Move the file to the appropriate folder
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder_name}")

# Main function to execute the task
def main():
    # Specify the folder where your files are located
    source_folder = "C:/Users/Shahzaib/Downloads" # change it to your designated folder


    print("Organizing files by extension...")
    organize_files_by_extension(source_folder)
    print("File organization complete!")

if __name__ == "__main__":
    main()

