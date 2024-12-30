from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView,
    IssueCreateView, IssueUpdateView, IssueDeleteView
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:project_id>/issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_edit'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
]
