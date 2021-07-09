from django.urls import path
from core import views

urlpatterns =[
  path('obras',views.LibList, name='listagem'),
  path('obras/',views.LibPost, name='envio'),
  path('obras/<str:pk>/',views.LibPut, name='atualizar'),
  path('obras/<str:pk>', views.LibDelete,name='deletar')
]