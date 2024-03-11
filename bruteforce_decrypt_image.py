from pwn import xor

# Read the encrypted image
enc_image = open("magic.png.enc", "rb").read()

# Initialize the test variable
test = b'\xb1]\xecQ\xac\x18H4'

# Brute-force decryption loop
for char in range(1, 13):  # Range adjusted to start from 1 and include 12
    key = test + bytes([char])
    decrypted_image = xor(enc_image, key)
    
    # Save the decrypted image to a separate file for each iteration
    output_image_path = f"kdecrypted_image{char}.png"
    with open(output_image_path, "wb") as output_image:
        output_image.write(decrypted_image)

    print(f"Decrypted image saved to {output_image_path}")
