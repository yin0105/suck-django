# Generated by Django 3.1.7 on 2021-02-22 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformations',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profiles', serialize=False, to='auth.user')),
                ('company', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('role', models.IntegerField(default=2)),
                ('email_verify', models.BooleanField(default=False)),
                ('email_token', models.CharField(blank=True, max_length=255, null=True)),
                ('email_image', models.CharField(blank=True, max_length=255, null=True)),
                ('google_auth_verify', models.BooleanField(default=False)),
                ('google_auth_provide_id', models.CharField(blank=True, max_length=255, null=True)),
                ('google_auth_email', models.CharField(blank=True, max_length=255, null=True)),
                ('google_auth_name', models.CharField(blank=True, max_length=255, null=True)),
                ('google_auth_image', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_auth_verify', models.BooleanField(default=False)),
                ('linkedin_auth_provide_id', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_auth_email', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_auth_name', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_auth_image', models.CharField(blank=True, max_length=255, null=True)),
                ('outlook_auth_verify', models.BooleanField(default=False)),
                ('outlook_auth_provide_id', models.CharField(blank=True, max_length=255, null=True)),
                ('outlook_auth_email', models.CharField(blank=True, max_length=255, null=True)),
                ('outlook_auth_name', models.CharField(blank=True, max_length=255, null=True)),
                ('outlook_auth_image', models.CharField(blank=True, max_length=255, null=True)),
                ('real_password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user_profiles',
            },
        ),
    ]
