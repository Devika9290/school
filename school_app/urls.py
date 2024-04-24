from django.urls import path
from school_app.views import *

urlpatterns = [
   path('school/list',school_list,name='school-list'),
   path('batch/list',batch_list,name='batch-list'),
   path('student/list',student_list,name='student-list'),
   path('school/add',school_add,name='school-add'),
   path('school/<int:school_id>/view',school_view,name='school-view'),
   path('school/<int:school_id>/delete',school_delete,name='school-delete'),
   path('batch/add',batch_add,name='school-add'),
   path('batch/<int:batch_id>/view',batch_view,name='batch-view'),
   path('batch/<int:batch_id>/delete',batch_delete ,name='batch-delete'),
   path('student/add',student_add,name='student-add'),
   path('student/<int:student_id>/view',student_view,name='student-view'),
   path('student/<int:student_id>/delete',student_delete ,name='student-delete'),
   path('school/<int:school_id>/edit1',school_edit1,name='school-edit1'),
   path('school/<int:school_id>/edit2',school_edit2,name='school-edit2'),
   path('batch/<int:batch_id>/edit1',batch_edit1,name='batch-edit1'),
   path('batch/<int:batch_id>/edit2',batch_edit2,name='batch-edit2'),
   path('student/<int:student_id>/edit1/', StudentEdit1.as_view(), name='student-edit1'),
   path('student/<int:student_id>/edit2/', StudentEdit2.as_view(), name='student-edit2'),
   path('student/<int:student_id>/batch/',StudentWithBatch.as_view(),name='Student-With-Batch'),
   path('school/<int:school_id>/batch/',SchoolWithBatch.as_view(), name='School-With-Batch')
]
