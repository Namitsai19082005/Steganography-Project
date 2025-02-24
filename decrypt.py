import cv2

def decrypt_image(image_path, password, user_password):
    if password != user_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read the image.")
        return

    c = {i: chr(i) for i in range(256)}

    rows, cols, _ = img.shape
    decrypted_msg = ""
    stop = False  # Flag to stop both loops

    for i in range(rows):
        for j in range(cols):
            char = c[img[i, j, 0]]  # Read from Blue channel
            if char == "~":  # Stop when delimiter is found
                stop = True
                break
            decrypted_msg += char
        if stop:
            break  # Break outer loop too

    print("Decrypted Message:", decrypted_msg)
