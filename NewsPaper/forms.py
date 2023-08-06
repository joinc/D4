from django import forms
from NewsPaper.models import Post

######################################################################################################################


class FormCreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'type_post',
            'title',
            'text',
        ]
        labels = {
            'author': 'Автор записи',
            'type_post': 'Тип записи',
            'title': 'Заголовок записи',
            'text': 'Текст записи',
        }
        widgets = {
            'author': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'type_post': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Укажите заголовок записи',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Напишите текст записи',
                }
            ),
        }


######################################################################################################################


class FormSearchPost(forms.Form):
    search = forms.CharField(
        label='Поиск',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите запрос для поиска в заголовке или тексте записи',
                'type': 'text',
                'class': 'form-control',
            }
        ),
        required=False,
    )
    ordering = forms.ChoiceField(
        label='Сортировка',
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-check-input',
            }
        ),
        choices=(
            ('-create_date', 'Новые сверху'),
            ('create_date', 'Старые сверху'),
            ('author', 'Авторы от А до Я'),
            ('-author', 'Авторы от Я до А'),
        ),
        initial='-create_date',
        required=False,
    )

