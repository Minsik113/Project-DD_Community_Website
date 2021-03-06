# Generated by Django 3.2.5 on 2021-07-07 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardAllContentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('seenum', models.PositiveIntegerField(default=0)),
                ('board_kind', models.CharField(max_length=20)),
                ('like', models.ManyToManyField(default=0, related_name='likes', to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boardapp.boardallcontentlist')),
            ],
        ),
        migrations.CreateModel(
            name='Board_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_writer', models.CharField(max_length=20)),
                ('comment_content', models.TextField(null=True)),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='boardapp.boardallcontentlist')),
            ],
        ),
    ]
