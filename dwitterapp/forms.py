import arrow
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 
            'text',
        )

    def save(self, commit=True):
        post = self.save(commit=False)
        post.author = self.request.user
        post.published_date = arrow.now().datetime        
        return super(PostForm, self).save(commit)
