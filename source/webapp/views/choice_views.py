from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.models import Poll, Choice
from webapp.forms import PollForm, ChoiceForm, AnswerForPollForm


class AnswerForPollCreateView(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = AnswerForPollForm

    def form_valid(self, form):
        self.poll = self.get_poll()
        self.poll.choice.create(**form.cleaned_data)
        return redirect('poll_detail', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)


class AnswerUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = AnswerForPollForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})



class AnswerDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})
