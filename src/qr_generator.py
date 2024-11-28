import qrcode
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