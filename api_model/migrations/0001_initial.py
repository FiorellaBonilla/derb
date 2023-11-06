# Generated by Django 4.2.5 on 2023-11-03 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_model', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameFields', models.CharField(max_length=100)),
                ('field_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModelTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Fish', 'Fish')], max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_address', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=50)),
                ('occupants_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tinyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.TextField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_model.modelfields')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_model.formmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseF', models.TextField(blank=True, null=True)),
                ('fieldsRes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_model.modelfields')),
            ],
        ),
        migrations.AddField(
            model_name='modelfields',
            name='model_inicial',
            field=models.ManyToManyField(to='api_model.modeltemplate'),
        ),
        migrations.AddField(
            model_name='formmodel',
            name='model_pre',
            field=models.ManyToManyField(to='api_model.modeltemplate'),
        ),
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('persons', models.ManyToManyField(to='api_model.person')),
                ('pets', models.ManyToManyField(to='api_model.pet')),
                ('rooms', models.ManyToManyField(to='api_model.room')),
            ],
        ),
    ]