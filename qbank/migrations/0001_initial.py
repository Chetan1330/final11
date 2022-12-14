# Generated by Django 4.1 on 2022-11-28 12:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExamHeader',
            fields=[
                ('exam_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('keywords', models.CharField(blank=True, max_length=300, null=True)),
                ('slug', models.CharField(blank=True, max_length=300, null=True)),
                ('duration_m', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('pass_score', models.IntegerField(blank=True, null=True)),
                ('category_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qbank.category')),
            ],
            options={
                'db_table': 'ExamHeader',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('bachelor_degree', models.CharField(blank=True, max_length=50, null=True)),
                ('bachelor_yop', models.IntegerField(blank=True, null=True)),
                ('master_degree', models.CharField(blank=True, max_length=50, null=True)),
                ('master_yop', models.IntegerField(blank=True, null=True)),
                ('specialization', models.CharField(blank=True, max_length=50, null=True)),
                ('auth_user_id', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('tech_stack', models.CharField(blank=True, max_length=100, null=True)),
                ('project_description', models.CharField(blank=True, max_length=400, null=True)),
                ('auth_user_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Project',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('question_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question_num', models.IntegerField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('option_a', models.TextField(blank=True, null=True)),
                ('option_b', models.TextField(blank=True, null=True)),
                ('option_c', models.TextField(blank=True, null=True)),
                ('option_d', models.TextField(blank=True, null=True)),
                ('option_e', models.TextField(blank=True, null=True)),
                ('option_f', models.TextField(blank=True, null=True)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('referrence', models.CharField(blank=True, max_length=1000, null=True)),
                ('explanation', models.CharField(blank=True, max_length=1000, null=True)),
                ('page_num', models.IntegerField(blank=True, null=True)),
                ('exam_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qbank.examheader')),
            ],
            options={
                'db_table': 'ExamQuestion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('dashboard_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('auth_user_id', models.IntegerField(blank=True, null=True)),
                ('score_taken', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qbank.examheader')),
            ],
            options={
                'db_table': 'Dashboard',
                'managed': True,
            },
        ),
    ]
