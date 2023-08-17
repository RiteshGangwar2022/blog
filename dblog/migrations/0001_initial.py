# Generated by Django 4.2.4 on 2023-08-15 08:49

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
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post/')),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dblog.category')),
            ],
        ),
    ]