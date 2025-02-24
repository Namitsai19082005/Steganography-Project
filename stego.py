import encrypt
import decrypt

image_path = "Image.png"
msg = input("Enter secret message: ")
password = input("Set a passcode: ")

encrypt.encrypt_image(image_path, msg, password)

user_password = input("Enter passcode for decryption: ")
decrypt.decrypt_image("encryptedimg.png", password, user_password)
