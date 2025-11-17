import qrcode,base64
from io import BytesIO
def generate_qr_base64(t):
 q=qrcode.QRCode(box_size=8,border=2);q.add_data(t);q.make(fit=True)
 img=q.make_image(fill_color="black",back_color="white")
 b=BytesIO();img.save(b,format="PNG")
 return base64.b64encode(b.getvalue()).decode()