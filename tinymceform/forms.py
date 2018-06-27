from django.forms import ModelForm
from .models import MyModel
class ArticleForm(ModelForm):
     class Meta:
        model = MyModel
        fields = ['content']