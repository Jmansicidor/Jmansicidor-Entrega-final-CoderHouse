# Generated by Django 4.0.4 on 2022-06-17 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_user_userinfo'),
        ('blog', '0002_create_nombre_completo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create',
            name='nombre_completo',
        ),
        migrations.AlterField(
            model_name='create',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.userinfo'),
        ),
    ]