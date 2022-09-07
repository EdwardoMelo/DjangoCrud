# Generated by Django 3.2.15 on 2022-09-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=256)),
                ('ativa', models.BooleanField(default=True)),
                ('data_nascimento', models.DateField(null=True)),
            ],
        ),
    ]
