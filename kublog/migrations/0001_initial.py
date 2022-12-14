# Generated by Django 3.2.5 on 2022-11-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_message', models.CharField(max_length=2200)),
            ],
        ),
        migrations.CreateModel(
            name='PostOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.CharField(max_length=2200)),
                ('place', models.CharField(choices=[('食堂', '食堂'), ('500号館', '500号館'), ('600号館', '600号館'), ('700号館', '700号館'), ('800号館', '800号館'), ('900号館', '900号館'), ('1000号館', '1000号館'), ('御井本館', '御井本館'), ('御井図書館', '御井図書館'), ('第1学生部室棟', '第1学生部室棟'), ('第2学生部室棟', '第2学生部室棟'), ('御井学館', '御井学館'), ('御井学生会館', '御井学生会館'), ('千歳会館', '千歳会館'), ('第2体育館', '第2体育館'), ('第3学生部室棟', '第3学生部室棟'), ('テニスコート', 'テニスコート'), ('インターナショナル・ハウス', 'インターナショナル・ハウス'), ('みいアリーナ', 'みいアリーナ'), ('学生寮', '学生寮'), ('駐輪場', '駐輪場'), ('グラウンド', 'グラウンド'), ('弓道場', '弓道場'), ('茶室', '茶室'), ('器楽室', '器楽室')], max_length=30)),
                ('created_by', models.CharField(max_length=30)),
            ],
        ),
    ]
