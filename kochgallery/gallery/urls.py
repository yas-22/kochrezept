from django.urls import path


from .views import overview, upload
urlpatterns = [
    path('', overview, name='overview'),
    path('upload/', upload, name='upload'),
]
