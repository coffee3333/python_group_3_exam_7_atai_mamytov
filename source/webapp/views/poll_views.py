from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Poll
from webapp.forms import PollForm, ChoiceForm


class PollView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/poll_ls.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollDetailView(DetailView):
    context_object_name = 'poll'
    model = Poll
    template_name = 'poll/poll_detail.html'
    key_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChoiceForm()
        return context


class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('poll_ls')