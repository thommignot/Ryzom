# Generated by Django 2.1.7 on 2019-02-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_subscriptions_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='template_class',
            field=models.CharField(default='Task', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='template_module',
            field=models.CharField(default='todos.components.base', max_length=255),
            preserve_default=False,
        ),
    ]