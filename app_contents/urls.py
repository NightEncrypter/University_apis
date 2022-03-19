from django.urls import path

from . import views
urlpatterns=[
    # VIDEOS
    path("video",views.SubjectVideoView.as_view(),name="upload_video"),
    path("uploads/video/<int:pk>",views.Video_Update_Delete.as_view(),name="subvideo_update_delete"),
    
    
    # IMAGE
    path("image",views.SubjectImageView.as_view(),name="sub_upload_image"),
    path("uploads/image/<int:pk>",views.Image_Update_Delete.as_view(), 
         name="image_update_delete"),
    
    # LINKS
    path("link",views.LinkView.as_view(),name="links"),
    path("uploads/link/<int:pk>",views.Link_Update_Delete.as_view(), 
         name="link_update_delete"),
    
    # DOCX
    path("docx",views.DocxView.as_view(),name="sub_docx")  ,
    path("uploads/docx/<int:pk>",views.Docx_Update_Delete.as_view(), 
         name="subdocx_update_delete"),
    
#     # TOPIC
    path("topics",views.TopicView.as_view(),name="topics"), 
    path("uploads/topics/<int:pk>",views.Topic_Update_Delete.as_view(), 
         name="topic_update_delete"),
    
    # UNIT
    path("units",views.UnitView.as_view(),name="units"),
    path("uploads/units/<int:pk>",views.Unit_Update_Delete.as_view(), name="unit_update_delete"),
    
    # SUB
    path("subjects",views.SubjectView.as_view(),name="subject"),
    path("uploads/subjects/<int:pk>",views.Subject_Update_Delete.as_view(), name="sub_update_delete"),
    
    
    path("unitfilter",views.FilterOfUnit.as_view(),name="filter_unit"),
    
    # path("uploads/file",views.DocxView.as_view(),name="upload_file"),
]