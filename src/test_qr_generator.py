import pytest # noqa
import qrcode
from pathlib import Path
from io import BytesIO
from PIL import Image
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