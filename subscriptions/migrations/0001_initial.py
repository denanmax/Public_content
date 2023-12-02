# Generated by Django 4.2.7 on 2023-12-02 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255, verbose_name='stripe id')),
                ('url_pay', models.TextField(verbose_name='Ссылка на оплату')),
                ('payment_status', models.CharField(max_length=100, verbose_name='Статус оплаты')),
                ('pay_status', models.CharField(max_length=100, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
    ]
