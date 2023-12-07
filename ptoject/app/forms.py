from django import forms

class UserForm(forms.Form):
    name = forms.CharField(lable="name",initial='Noname',required=False,widget=forms.TextInput(attrs={'class':'order__input'}))
    Email = forms.CharField(lable='Email',initial='Email@gbg.com',help_text='Заполните верный email')
    phone = forms.CharField(label='Phone number')
    service = forms.CharField(label='Select service')
    comment = forms.CharField(label='Tell us about service',widget=forms.Textarea)
    field_order = ['email','service','comment']

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название',widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Текст',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_published = forms.BooleanField()