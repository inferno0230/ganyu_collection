from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os

# Get the passcode from the user
passcode = input("Enter the passcode used to encrypt the images: ")

# Define the folder containing the encrypted images to be decrypted
folder_path = "encrypted_nsfw"

# Define the output folder for the decrypted images
output_folder_path = "decrypted_nsfw"

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an encrypted image
    if not filename.lower().endswith(".ganyu"):
        continue

    # Open the encrypted image file
    with open(os.path.join(folder_path, filename), "rb") as f:
        encrypted_data = f.read()

    # Extract the IV from the encrypted data
    iv = encrypted_data[:16]

    # Create the cipher object using AES in CBC mode with the passcode and IV
    cipher = AES.new(pad(passcode.encode("utf-8"), 32), AES.MODE_CBC, iv)

    # Decrypt the encrypted data using the cipher object and the IV
    decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), 16)

    # Save the decrypted data to a file with the original extension in the output folder
    output_filename = os.path.splitext(filename)[0] + os.path.splitext(filename)[1].replace(".ganyu", "")
    output_path = os.path.join(output_folder_path, output_filename)
    with open(output_path, "wb") as f:
        f.write(decrypted_data)

