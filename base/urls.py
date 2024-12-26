from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', UserView.as_view({'get':'list', 'post':'create'})),
    path('users/<int:pk>', UserView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('department/', DepartmentView.as_view({'get':'list', 'post':'create'})),
    path('department/<int:pk>', DepartmentView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('user_profile/', User_ProfileView.as_view({'get':'list', 'post':'create'})),
    path('user_profile/<int:pk>', User_ProfileView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('file/', FileView.as_view({'grt':'list', 'post':'create'})),
    path('file/<int:pk>', FileView.as_view({'get':'retrive', 'put':'update', 'delete':'destroy'})),
    path('metadata/', MetadataView.as_view({'get':'list', 'post': 'create'})),
    path('metadata/<int:pk>', MetadataView.as_view({'get':'retrive', 'put':'update', 'delete':'destroy'})),
    path('auto_log/', Auto_LogView.as_view({'get':'list', 'post': 'create'})),
    path('auto_log/<int:pk>', Auto_LogView.as_view({'get':'retrive', 'put':'update', 'delete':'destroy'})),
    path('feedback/', FeedbackView.as_view({'get':'list', 'post': 'create'})),
    path('feedback/<int:pk>', FeedbackView.as_view({'get':'retrive', 'put':'update', 'delete':'destroy'})),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
