# Generated by Django 3.2 on 2021-09-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0004_alter_students_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='courses',
            field=models.ManyToManyField(related_name='student', to='st.Students'),
        ),
    ]
