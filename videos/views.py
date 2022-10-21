from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):

    return render(request, 'videos/index.html')


class CreateVideo(LoginRequiredMixin, CreateView):
	model = Video
	fields = ['title', 'description', 'video_file', 'thumbnail']
	template_name = 'videos/create_video.html'

	def form_valid(self, form):
		form.instance.uploader = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('video-detail', kwargs={'pk': self.object.pk})


class DetailVideo(DetailView):
	model = Video
	template_name = 'videos/detail_video.html'


class UpdateVideo(LoginRequiredMixin, UpdateView):
	model = Video
	fields = ['title', 'description']
	template_name = 'videos/create_video.html'

	def get_success_url(self):
		return reverse('video-detail', kwargs={'pk': self.object.pk})


class DeleteVideo(LoginRequiredMixin, DeleteView):
	model = Video
	template_name = 'videos/delete_video.html'

	def get_success_url(self):
		return reverse('index')