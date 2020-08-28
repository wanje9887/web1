# Generated by Django 3.0.8 on 2020-08-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='odh562@naver.com', max_length=256, verbose_name='이메일'),
            preserve_default=False,
        ),
    ]
