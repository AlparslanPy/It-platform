# Generated by Django 3.2 on 2021-09-29 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0003_alter_students_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='project',
            field=models.ForeignKey(blank=True, default='-', null=True, on_delete=django.db.models.deletion.CASCADE, to='st.project'),
        ),
    ]
