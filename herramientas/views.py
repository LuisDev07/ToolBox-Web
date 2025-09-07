from django.shortcuts import render
import qrcode
from PIL import Image
import io
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import base64


def home(request):
    return render(request, "Home.html")




# Logos por defecto
LOGOS = {
    "google": "static/img/logos/google.png",
    "youtube": "static/img/logos/youtube.png",
    "facebook": "static/img/logos/facebook.png",
    "twitter": "static/img/logos/twitter.png",
    "tiktok": "static/img/logos/tiktok.png",
    "instagram": "static/img/logos/instagram.png",
    "linkedin": "static/img/logos/linkedin.png",
    "whatsapp": "static/img/logos/whatsapp.png",
    "telegram": "static/img/logos/telegram.png",
    "pinterest": "static/img/logos/pinterest.png",
    "reddit": "static/img/logos/reddit.png",
   
}



def QRgenerator(request):
    qr_img_base64 = None
    url = ""
    logo_name = ""

    # Siempre preparamos logos para el template
    logos_data = [
        {
            "key": key,
            "src": f"img/logos/{key}.png",   # ruta relativa a static/
            "checked": False  # por defecto ninguno seleccionado
        }
        for key in LOGOS.keys()
    ]

    if request.method == "POST":
        url = request.POST.get("url")
        logo_name = request.POST.get("logo")
        action = request.POST.get("action")

        if url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

            # Logo
            if logo_name in LOGOS:
                logo_img = Image.open(LOGOS[logo_name])
                max_logo_size = int(img_qr.size[0] * 0.2)
                ratio = min(max_logo_size / logo_img.width, max_logo_size / logo_img.height)
                logo_new_size = (int(logo_img.width * ratio), int(logo_img.height * ratio))
                logo_img = logo_img.resize(logo_new_size)
                pos = ((img_qr.size[0] - logo_new_size[0]) // 2, (img_qr.size[1] - logo_new_size[1]) // 2)
                img_qr.paste(logo_img, pos, mask=logo_img if logo_img.mode == "RGBA" else None)

            # Actualizar logos_data para marcar el seleccionado
            for l in logos_data:
                l["checked"] = (l["key"] == logo_name)

            # Descargar
            if action == "download":
                if not url:  # si no hay URL, no se puede generar
                  return HttpResponse("Primero genera un QR antes de descargarlo.")
                buffer = io.BytesIO()
                img_qr.save(buffer, format="PNG")
                buffer.seek(0)
                return FileResponse(buffer, as_attachment=True, filename="qr.png")

            # Vista previa
            buffer = io.BytesIO()
            img_qr.save(buffer, format="PNG")
            qr_img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render(request, "QR.html", {
        "qr_img": qr_img_base64,
        "logos_data": logos_data,
        "url": url,
        "logo_name": logo_name,
    })


def generatorpassword(request):
    return render(request, "pasword.html")



def handler404(request, exception):
    return render(request, "404.html", status=404)

def handler500(request):
    return render(request, "500.html", status=500)