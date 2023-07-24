
from django.urls import path
from message_app import views
urlpatterns = [
   path('create',views.create),
   path('dashboard',views.dashboard),
   path('delete/<rid>',views.delete),
   path('edit/<rid>',views.edit)
]