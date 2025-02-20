from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("draft/", views.DraftPostListView.as_view(), name="drafts"),
    path("archived/", views.ArchivedPostListView.as_view(), name="archive"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post"),
    path("new/", views.PostCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    

]