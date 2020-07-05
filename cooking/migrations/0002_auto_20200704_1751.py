# Generated by Django 3.0.8 on 2020-07-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='recent',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]