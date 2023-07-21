
# builtin library
import qrcode
def generate_qr_code(data, output_file):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to the output file
    img.save(output_file)

if __name__ == "__main__":
    data = input("Enter the data for the QR code: ")
    output_file = input("Enter the output file path (e.g., qr_code.png): ")

    try:
        generate_qr_code(data, output_file)
        print("QR code generated successfully.")
    except Exception as e:
        print(f"Error generating QR code: {e}")
