# Generated by Django 2.2.13 on 2020-09-30 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='lesson_purchased',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased', to='lessons.Lesson'),
        ),
    ]