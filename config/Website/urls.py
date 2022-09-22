from django.urls import path

from Website.views import index, new_announce, delete_announce, announce_detail, delete_comment, edit_announce, \
    edit_comment

urlpatterns = [
    path('', index, name="Website-index"),
    path('new/announce/', new_announce, name='Website-new_post'),
    path('delete/announce/<int:identifier>/', delete_announce, name='Website-delete_announce'),
    path('delete/comment/<int:identifier>/', delete_comment, name='Website-delete_comment'),
    path('announce/<int:identifier>/', announce_detail, name='Website-announce'),
    path('edit/announce/<int:identifier>/', edit_announce, name='Website-edit_announce'),
    # path('edit/comment/<int:identifier/>', edit_comment, name='Website-edit_comment')
]
