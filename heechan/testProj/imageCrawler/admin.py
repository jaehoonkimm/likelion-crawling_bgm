from django.contrib import admin
# models에서 class import
from .models import ImageData

# admin page를 통해 import 했던 class의 data 관리토록 등록
admin.site.register(ImageData)