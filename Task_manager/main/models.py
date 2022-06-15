from django.db import models


class Task(models.Model):
    date = models.DateField(verbose_name="Дата", null=True)
    title = models.CharField(max_length=100, verbose_name="Название")
    is_executed = models.BooleanField(verbose_name="Выполнено", default=False)
    date_name = models.CharField(max_length=100, verbose_name="Название даты", null=True, default="завтра")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "задачу"
        verbose_name_plural = "Задачи"
