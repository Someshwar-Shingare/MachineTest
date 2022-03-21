from django import forms

class WebsiteForm(forms.Form):
    name = forms.CharField(max_length=200)
    qr_code = forms.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)