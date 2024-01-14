from django.contrib import admin
from django.urls import path
import hello_app.views as gj 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', gj.hello_world, name='hello_world'),
    path('mercedes/', gj.mercedes),
    path('current_datetime/', gj.current_datetime, name='current_datetime'),
    path('time_after_10_hours/<int:hours>/', gj.time_after_10_hours, name='time_after_10_hours'),
    path('hellokushal/', gj.hello, name='hello'),
    path('books/', gj.author_list, name='book_list'),
    path('emp', gj.emp),  
    path('show',gj.show),  
    path('edit/<int:id>', gj.edit),  
    path('update/<int:id>', gj.update),  
    path('delete/<int:id>', gj.destroy),  
    
]

