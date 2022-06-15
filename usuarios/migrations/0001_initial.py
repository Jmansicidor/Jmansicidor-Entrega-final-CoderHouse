# Generated by Django 4.0.4 on 2022-06-15 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user_sex', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Otro')])),
                ('mailbox', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='avatar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.user')),
            ],
        ),
    ]
