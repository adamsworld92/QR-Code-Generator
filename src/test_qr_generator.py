import pytest # noqa
import qrcode
from qrcode.image.pil import PilImage
from pathlib import Path
from io import BytesIO
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qr_generator import QRCodeGenerator  # Use absolute import 

class TestQRCodeGenerator:
    """
    Test suite for QRCodeGenerator class
    Benefits: Organizes related tests and shares setup/teardown
    """
    
    def test_qr_generator_initialization(self):
        """
        Test if QRCodeGenerator initializes with default parameters
        Benefits: Ensures class can be instantiated correctly
        """
        generator = QRCodeGenerator()
        assert isinstance(generator, QRCodeGenerator)
        assert generator.version == 1  # Default version
        assert generator.box_size == 10  # Default box size
        assert generator.border == 4  # Default border

    def test_generate_qr_code_with_custom_parameters(self):

        generator = QRCodeGenerator(version=2, box_size=15, border=5)
        assert generator.version == 2
        assert generator.box_size == 15
        assert generator.border == 5

    def test_generate_qr_code_returns_image(self):
        generator = QRCodeGenerator()
        result = generator.generate_qr_code("Test Text")
        assert isinstance(result, PilImage)

    def test_qr_code_contains_correct_data(self):
        test_text = "Hello, World!!"
        generator = QRCodeGenerator()
        qr_code = generator.generate_qr_code(test_text)
        img_buffer = BytesIO()
        qr_code.save(img_buffer, 'PNG')
        


