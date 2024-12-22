# Generated by Django 5.0.6 on 2024-08-31 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBapp', '0002_login_delete_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=100)),
                ('L_name', models.CharField(max_length=100)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Mob_num', models.CharField(max_length=15)),
                ('Password', models.BigIntegerField()),
                ('Conf_password', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]