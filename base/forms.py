from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['image', 'name', 'want', 'where']
        widgets ={
            'image' : forms.FileInput(attrs={'id':'upload', 'onchange':'previewImage(), imgur()'}),
            'name': forms.TextInput(attrs={'placeholder':'Your name'}),
            'want' : forms.TextInput(attrs={'class':'wanttext','placeholder':'요청사항', 'style' : 'word-wrap:break-word'}),
            'where' :  forms.TextInput(attrs={'placeholder':'완성본 받을 곳'}),
        }
        labels ={
            'image' : 'Upload',
        }
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False