# Generated by Django 3.2.9 on 2022-12-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20221201_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='dificult',
            field=models.CharField(blank=True, max_length=19, null=True, verbose_name='Легкость'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text_6',
            field=models.TextField(blank=True, null=True, verbose_name='статья-6'),
        ),
    ]
