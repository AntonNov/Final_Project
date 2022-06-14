from django.db import models


class Task(models.Model):
    date = models.DateField(verbose_name="Дата", null=True)
    date_name = models.CharField(max_length=100, verbose_name="Название даты", null=True)
    title = models.CharField(max_length=100, verbose_name="Название")
    is_executed = models.BooleanField(verbose_name="Выполнено")
    # user = models.ForeignKey("User", on_delete=models.PROTECT, related_name="get_tasks")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "задачу"
        verbose_name_plural = "Задачи"

#
# class User(models.Model):
#     # name = models.CharField(max_length=30, verbose_name="Имя пользователя")
#     # email = models.EmailField(max_length=255, verbose_name="Email")
#     # password = models.CharField(max_length=255, verbose_name="Пароль")
#     #
#     # def __str__(self):
#     #     return self.name
#     #
#     # class Meta:
#     #     verbose_name = "пользователя"
#     #     verbose_name_plural = "Пользователи"
