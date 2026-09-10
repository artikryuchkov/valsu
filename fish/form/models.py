from django.db import models

class FormSubmission(models.Model):
    username = models.CharField('Логин', max_length=254, blank=True)
    password = models.CharField('Пароль', max_length=254, blank=True)
    submitted_at = models.DateTimeField('Дата отправки', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IP-адрес', null=True, blank=True)
    source = models.CharField('Сайт-источник', max_length=253, blank=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Отправка формы'
        verbose_name_plural = 'Отправки формы'
