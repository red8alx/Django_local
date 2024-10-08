# Generated by Django 5.1 on 2024-09-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_product_productdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='companyCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('student', models.ManyToManyField(related_name='courses', to='company.companystudent')),
            ],
        ),
    ]
