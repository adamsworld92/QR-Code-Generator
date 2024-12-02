import qrcode
from qrcode import QRCode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image
from pathlib import Path

class QRCodeGenerator:

    def __init__(self, version=1, box_size=10, border=4):

        self.version = version
        self.box_size = box_size
        self.border = border

        self.qr = qrcode.QRCode(
            version=version,
            box_size=box_size,
            border=border
        )

    def generate_qr_code(self, data):
        qr = QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        return qr.make_image(fill_color="black", back_color="white")


    def generate_qr_code(self, text: str) -> Image.Image:
   
        # Clear any existing data
        self.qr.clear()
        # Add the text data to the QR code
        self.qr.add_data(text)
        # Generate the QR code matrix
        self.qr.make(fit=True)
        # Create and return the image
        return self.qr.make_image(fill_color="black", back_color="white")
     # Return the QRCode object instead of the image
    
