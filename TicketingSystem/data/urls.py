from django.urls import path
from . import views

urlpatterns = [
    # path('',views.search_view,),
    path('',views.display_data_from_db),
    # path('send_data/',views.checking_data),
    path ('mail/',views.email, name= 'compose_mail'),
    path('report/',views.report, name = 'report'),
    path ('comment/', views.comment, name='comment'),
    path ('status/', views.status, name = 'status'),
]


