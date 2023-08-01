from django.urls import path
from . import views
urlpatterns = [path('',views.main,name='main'),
               path('details/',views.details,name='details'),
               path('details/add/',views.add,name='add'),
               path('details/add/addrecord/',views.addrecord,name='addrecord'),
               path('details/update/<int:id>',views.update,name='update'),
               path('details/update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
               path('details/deleteIt/<int:id>',views.deleteIt,name='deleteIt'),
               path('details/moreInfo/<int:id>',views.moreInfo,name='moreInfo'),
               ]