from django.urls import path
from .views import CRUDView

urlpatterns = [
    path('', CRUDView.as_view(), name='student_crud'),
    path('<int:pk>/', CRUDView.as_view(), name='student_detail'),
]
