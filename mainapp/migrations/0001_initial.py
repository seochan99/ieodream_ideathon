# Generated by Django 3.2 on 2021-08-13 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogI',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogI/')),
                ('final', models.ImageField(blank=True, null=True, upload_to='blogI/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogM/')),
                ('final', models.ImageField(blank=True, null=True, upload_to='blogM/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogS/')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LikeI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LikeM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='postS/')),
                ('like_user_set', models.ManyToManyField(blank=True, related_name='likes_user_setS', through='mainapp.Like', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='postM/')),
                ('like_user_set', models.ManyToManyField(blank=True, related_name='likes_user_setM', through='mainapp.LikeM', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostI',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='postI/')),
                ('like_user_set', models.ManyToManyField(blank=True, related_name='likes_user_setI', through='mainapp.LikeI', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='postD/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeSL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.blogs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.CreateModel(
            name='LikeML',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.blogm')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.AddField(
            model_name='likem',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.postm'),
        ),
        migrations.AddField(
            model_name='likem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='LikeIL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.blogi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.AddField(
            model_name='likei',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.posti'),
        ),
        migrations.AddField(
            model_name='likei',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.posts'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CommentS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='commentS/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainapp.posts')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='commentM/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainapp.postm')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='commentI/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainapp.posti')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_sh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_sh', to='mainapp.shop')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blogs',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='likes_user_setSL', through='mainapp.LikeSL', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogs',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogm',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='likes_user_setML', through='mainapp.LikeML', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogm',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogi',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='likes_user_setIL', through='mainapp.LikeIL', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogi',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='likem',
            unique_together={('user', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='likei',
            unique_together={('user', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
    ]
