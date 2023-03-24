from django.db import models
from django.core.validators import MinValueValidator

class Task(models.Model):
    title=models.CharField("Ім'я та фамілія", max_length=50)
    number=models.IntegerField("Номер телефону",validators=[MinValueValidator(1)])
    task=models.TextField('Що зацікавило')


    def str(self):
        return self.title

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'