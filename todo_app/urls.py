from django.urls import include, path

# import todo_app.views
from todo_app.views import TodoView

urlpatterns = [

     path('abc/',TodoView.as_view(),name="abc"),
    
]
