import os
import shutil
source_folder = '/path/to/your/folder'  
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
text_extensions = ['.txt', '.md', '.csv']
pdf_extensions = ['.pdf']
other_extensions = []
def create_directories():
    directories = ['Images', 'Text Files', 'PDFs', 'Others']
    for dir_name in directories:
        dir_path = os.path.join(source_folder, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
def organize_files():
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        if os.path.isdir(file_path):
            continue
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension in image_extensions:
            dest_folder = 'Images'
        elif file_extension in text_extensions:
            dest_folder = 'Text Files'
        elif file_extension in pdf_extensions:
            dest_folder = 'PDFs'
        else:
            dest_folder = 'Others'
        dest_path = os.path.join(source_folder, dest_folder, file_name)
        shutil.move(file_path, dest_path)
        print(f"Moved: {file_name} to {dest_folder}")
if __name__ == '__main__':
    create_directories()
    organize_files()
    print("File organization complete!")
