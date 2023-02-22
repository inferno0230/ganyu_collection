import os
import magic

# Set the path to the directory containing the images
path = "decrypted_nsfw"

# Create a new directory to store the renamed images
new_dir = os.path.join(path, "new")
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

# Get a list of all files in the directory
files = os.listdir(path)

# Initialize the magic library to detect file types
mime = magic.Magic(mime=True)

# Loop through each file in the directory
for file in files:
    # Check if the current item is a file and an image
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path) and "image" in mime.from_file(file_path):
        # Determine the file type based on the file header
        file_type = mime.from_file(file_path).split("/")[1]
        # Rename the file with the appropriate file extension
        new_name = f"{os.path.splitext(file)[0]}.{file_type}"
        os.rename(file_path, os.path.join(new_dir, new_name))

