from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static





urlpatterns =[

    path('register/',RegistrationAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    # path('logout/', LogoutAPIView.as_view(), name='logout'),

    path('department/', DepartmentView.as_view({'get': 'list', 'post': 'create'})),
    path('department/<int:pk>', DepartmentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('user/', User_ProfileView.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>', User_ProfileView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('categoty/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('categoty/<int:pk>', CategoryView.as_view({'get': 'retrieve' , 'put': 'update', 'delete': 'destroy'})),

    path('file/', FileView.as_view({'get': 'list', 'post': 'create'})),
    path('file/<int:pk>', FileView.as_view({'get': 'retrieve', 'put' : 'update', 'delete': 'destroy'})),

    path('audit_log/', Audit_LogView.as_view({'get': 'list', 'post': 'create'})),
    path('audit_log/<int:pk>', Audit_LogView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('request/', Access_RequestView.as_view({'get': 'list', 'post': 'create'})),
    path('request/<int:pk>', Access_RequestView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('backup/', File_BackupView.as_view({'get': 'list', 'post': 'create'})),
    path('backup/<int:pk>', File_BackupView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('recovery/', File_RecoveryView.as_view({'get': 'list', 'post': 'create'})),
    path('recovery/<int:pk>', File_RecoveryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # path('workflow/', WorkflowView.as_view({'get': 'list', 'post': 'create'})),
    # path('workflow/<int:pk>', WorkflowView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # path('workflow_responsibility/', Worlflow_ResponsibilityView.as_view({'get': 'list', 'post': 'create'})),
    # path('workflow_responsibility/<int:pk>', Worlflow_ResponsibilityView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('notification_token/', Notification_TokenView.as_view({'get': 'list', 'post': 'create'})),
    path('notification_token/<int:pk>', Notification_TokenView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('notification/', NotificationView.as_view({'get': 'list', 'post': 'create'})),
    path('notification/<int:pk>', NotificationView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('feedback/', FeedbackView.as_view({'get': 'list', 'post': 'create'})),
    path('feedback/<int:pk>', FeedbackView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)