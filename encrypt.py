import cv2
import numpy as np

def encrypt_image(image_path, msg, password, output_path="encryptedimg.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read the image.")
        return

    msg += "~"  # Add delimiter to mark the end of the message
    d = {chr(i): i for i in range(256)}

    rows, cols, _ = img.shape
    index = 0

    for i in range(rows):
        for j in range(cols):
            if index < len(msg):
                img[i, j, 0] = d[msg[index]]  # Store ASCII values in Blue channel
                index += 1
            else:
                break

    cv2.imwrite(output_path, img)  # Save as PNG to prevent data loss
    print(f"Image saved as {output_path}")
