from django.forms import ModelForm
class BloogForm(ModelForm):
    class Meta:
        fields='__all__'

