from django.urls import path

from . import views
urlpatterns=[
    path("uploads/video",views.SubjectVideoView.as_view(),name="upload_video"),
    path("uploads/image",views.SubjectImageView.as_view(),name="upload_image"),
    path("uploads/link",views.LinkView.as_view(),name="upload_link"),
    path("uploads/file",views.DocxView.as_view(),name="upload_file"),
]