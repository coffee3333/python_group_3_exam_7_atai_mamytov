"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import PollView, PollDetailView, PollCreateView, PollUpdateView, PollDeleteView, AnswerForPollCreateView, \
    AnswerUpdateView, AnswerDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollView.as_view(), name='poll_ls'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('poll/add/', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/edit/',PollUpdateView.as_view(), name='poll_edit'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('answer/<int:pk>/add_answer/', AnswerForPollCreateView.as_view(), name='answ_create'),
    path('answer/<int:pk>/edit_answer/', AnswerUpdateView.as_view(), name='answ_edit'),
    path('answer/<int:pk>/delete_answer', AnswerDeleteView.as_view(), name='answ_delete')
]
