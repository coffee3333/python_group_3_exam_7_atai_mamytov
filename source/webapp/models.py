from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=True, verbose_name='Question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = None

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='choice', on_delete=models.CASCADE, verbose_name='poll')
    answer_option = models.TextField(max_length=3000, null=False, blank=True, verbose_name='Answer option')

    def __str__(self):
        return self.answer_option

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answer', on_delete=models.CASCADE, verbose_name='poll')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created time')
    choice = models.ForeignKey('webapp.Choice', related_name='answer', on_delete=models.CASCADE, verbose_name='choice')

