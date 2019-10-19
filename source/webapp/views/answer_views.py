from django.shortcuts import redirect, get_object_or_404, render
from django.views import View

from webapp.models import Poll, Answer, Choice


class QuestionnaireCreateView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choice = poll.choice.all()
        context = {
            'poll': poll,
            'choices': choice
        }
        return render(request, 'answer/answer_create.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['value']
        answer = get_object_or_404(Choice, pk=pk)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(choice=answer, poll=poll)
        return redirect('poll_ls')