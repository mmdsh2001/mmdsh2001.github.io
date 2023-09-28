from django.forms import Form ,CharField , ValidationError ,TextInput


class MyForm(Form):
    word = CharField(max_length=45,widget=TextInput(attrs={'placeholder': 'eg: Hello'}))

    def clean(self):
        cleaned_data =super().clean()
        word = cleaned_data['word']
        if len(word) < 2:
            raise ValidationError('Name must be at least 3 characters long.')
        return cleaned_data
       