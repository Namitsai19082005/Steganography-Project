//Made by Namitsai Vaddempudi

Image-Based Text Encryption and Decryption
This project implements steganography by hiding secret messages inside images using OpenCV (cv2). It encrypts a message into an image by modifying pixel values and retrieves it upon decryption.

🚀 Features
Encrypt a secret message into an image.
Decrypt the hidden message using a passcode.
Uses Blue channel for storing ASCII values.
Saves the encrypted image as PNG to prevent data loss.
Uses password authentication for decryption.

🛠 Tech Stack
Python
OpenCV (cv2)
NumPy

📂 Project Structure
pgsql
Copy
Edit
📦 Image-Stegano
│── encrypt.py        # Encrypts a message into an image
│── decrypt.py        # Decrypts a message from an image
│── main.py           # Runs the encryption & decryption process
│── Image.jpg         # Input image
│── encryptedimg.png  # Output encrypted image
│── README.md         # Project documentation


🔧 Installation & Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-repo/image-stegano.git
cd image-stegano
Install dependencies

bash
Copy
Edit
pip install opencv-python numpy
Run the program

bash
Copy
Edit
python main.py


📌 How It Works
🔒 Encryption Process
Loads an image.
Converts the secret message into ASCII values.
Stores ASCII values in the Blue channel of pixels.
Saves the modified image as encryptedimg.png.

🔑 Decryption Process
Reads the encryptedimg.png.
Extracts ASCII values from the Blue channel.
Converts them back into characters.
Prints the original message (only if the correct passcode is entered).
📝 Usage

1️⃣ Encrypt a Message
bash
Copy
Edit
python main.py
Enter a secret message.
Set a passcode.
The encrypted image (encryptedimg.png) is created.

2️⃣ Decrypt a Message
Run the script again.
Enter the correct passcode.
The hidden message will be displayed.

💡 Example
mathematica
Copy
Edit
Enter secret message: HelloWorld123
Set a passcode: MySecret123
Image saved as encryptedimg.png
Enter passcode for decryption: MySecret123
Decrypted Message: HelloWorld123

⚠️ Notes
Use PNG format for better accuracy.
Avoid long messages as they require larger images.
Only users with the correct passcode can decrypt the message.

📜 License
This project is open-source under the MIT License.

