from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
  class Meta:
    model = Blog
    fields = [
      "title",
      "author",
      "content",
      # "created_at",
      # "updated_at",
      "published",
    ]

    labels = {
      "title": "標題",
      "author": "作者",
      "content": "內容",
      # "created_at": "新增日期",
      # "updated_at": "更新日期",
      "published": "是否發佈",
    }