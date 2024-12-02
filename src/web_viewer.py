from flask import Flask, send_file
from io import BytesIO
from qr_generator import QRCodeGenerator

app = Flask(__name__)

@app.route('/')
def show_qr():
    """
    Display QR code in web browser
    Benefits: Accessible via web browser, sharable via URL
    """
    # Create generator
    generator = QRCodeGenerator()
    
    # Generate QR code
    qr_image = generator.generate_qr_code("Hello, World!")
    
    # Save to memory buffer
    img_buffer = BytesIO()
    qr_image.save(img_buffer, 'PNG')
    img_buffer.seek(0)
    
    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
