import qrcode

def main():
    data = input("Enter the text or URL to encode in the QR code: ")
    if not data.strip():
        print("Input cannot be empty.")
        return
    img = qrcode.make(data)
    filename = input("Enter the filename to save the QR code image (e.g., 'qrcode.png'): ")
    if not filename.strip():
        filename = "qrcode.png"
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')):
        filename += ".png"
    # Ensure filename is a string
    filename = str(filename)
    img.save(filename)  # type: ignore
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    main() 