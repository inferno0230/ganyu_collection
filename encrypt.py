from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os

# Get the passcode from the user
passcode = input("Enter a passcode to encrypt the images: ")

# Define the folder containing the images to be encrypted
folder_path = "decrypted_nsfw"

# Define the output folder for the encrypted images
output_folder_path = "encrypted_nsfw"

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if not any(filename.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".bmp"]):
        continue

    # Open the image file
    with open(os.path.join(folder_path, filename), "rb") as f:
        image_data = f.read()

    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create the cipher object using AES in CBC mode with the passcode and IV
    cipher = AES.new(pad(passcode.encode("utf-8"), 32), AES.MODE_CBC, iv)

    # Pad the image data to a multiple of 16 bytes
    padded_image_data = pad(image_data, 16)

    # Encrypt the padded image data using the cipher object and the IV
    encrypted_data = iv + cipher.encrypt(padded_image_data)

    # Save the encrypted data to a file with a ".ganyu" extension in the output folder
    output_filename = os.path.splitext(filename)[0] + ".ganyu"
    output_path = os.path.join(output_folder_path, output_filename)
    with open(output_path, "wb") as f:
        f.write(encrypted_data)

