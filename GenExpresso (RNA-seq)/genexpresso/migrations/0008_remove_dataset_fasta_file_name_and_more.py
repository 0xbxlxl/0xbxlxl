# Generated by Django 5.1.4 on 2025-01-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genexpresso', '0007_dataset_fasta_file_name_dataset_gene_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='fasta_file_name',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='gene_information',
        ),
        migrations.AddField(
            model_name='dataset',
            name='fasta_file',
            field=models.FileField(blank=True, null=True, upload_to='fasta_files/'),
        ),
    ]
