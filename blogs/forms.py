from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
  class Meta:
    model = Blog
    fields = [
      "title",
      "content",
      "created_at",
      "updated_at",
      "published",
    ]

    label = {
      "title": 文章標題,
      "content": 內容,
      "created_at": 新增日期,
      "updated_at": 更新日期,
      "published": 是否發佈,
    }