from django import forms
from .models import Comments, Post, TaskList

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description', 'pic', 'tags']

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']


class DateInput(forms.DateInput):
    input_type = 'date'

class NewTaskForm(forms.ModelForm):
	class Meta:
		model = TaskList
		fields = '__all__'
		widgets = {
            'dueDate': DateInput(),
        }