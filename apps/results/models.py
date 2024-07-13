from django.db import models
from apps.quiz.models import Quiz
from apps.authentication.models import User


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Result for {self.user_id} in {self.quiz_id}'
