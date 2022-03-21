from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from hashlib import md5

# Create your models here.
class Url(models.Model):
    full_url = models.CharField(unique=True,max_length=400)
    short_url = models.CharField(unique=True, max_length=20)


    def __str__(self):
        return self.full_url


    @classmethod
    def create(self, full_url):
        temp_url = md5(full_url.encode()).hexdigest()[:5]
        try:
            obj = self.objects.create(full_url= full_url, short_url=temp_url)
        except:
            obj = self.objects.get(full_url=full_url)
        return obj

    def routeToURL(req, key):
        print(key)


class Website(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


