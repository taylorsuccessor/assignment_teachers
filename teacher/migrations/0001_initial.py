# Generated by Django 2.1 on 2020-07-07 13:07

from django.db import migrations, models
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=17)),
                ('room_number', models.CharField(blank=True, max_length=2, null=True)),
                ('subjects_taught', models.CharField(max_length=200)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to=teacher.models.get_upload_path)),
            ],
        ),
    ]