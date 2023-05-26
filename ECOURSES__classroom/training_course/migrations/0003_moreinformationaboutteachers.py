# Generated by Django 4.1.7 on 2023-05-23 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training_course', '0002_reviewcourse_moreinformationaboutcourses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInformationAboutTeachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=150, verbose_name='Профессия')),
                ('education', models.TextField(blank=True, verbose_name='Образование')),
                ('experience', models.TextField(blank=True, verbose_name='Опыт работы')),
                ('completed_courses', models.TextField(blank=True, help_text='Курсы, необходимо указать, которые не были пройдены в рамках данной платформы', verbose_name='Пройденные курсы')),
                ('previously_supervised_courses', models.TextField(blank=True, verbose_name='Курсы, которые уже преподовали')),
                ('category', models.ForeignKey(help_text='Категория, по которой учителя преподают', on_delete=django.db.models.deletion.PROTECT, to='training_course.category', verbose_name='Категория')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Дополнительные данные для преподователей',
                'verbose_name_plural': 'Дополнительные данные для преподователей',
            },
        ),
    ]