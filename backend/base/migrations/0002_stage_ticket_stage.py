# Generated by Django 4.1.6 on 2023-02-11 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='base.stage'),
        ),
    ]