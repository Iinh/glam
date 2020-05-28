# Generated by Django 3.0.6 on 2020-05-22 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_compress_json'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FenixAggregation',
        ),

        migrations.CreateModel(
            name='FenixAggregation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('channel', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('ping_type', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('build_id', models.CharField(max_length=100)),
                ('metric', models.CharField(max_length=200)),
                ('metric_type', models.CharField(max_length=100)),
                ('metric_key', models.CharField(blank=True, max_length=200)),
                ('client_agg_type', models.CharField(blank=True, max_length=100)),
                ('total_users', models.IntegerField()),
                ('histogram', models.TextField(blank=True, null=True)),
                ('percentiles', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'glam_fenix_aggregation',
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='fenixaggregation',
            constraint=models.UniqueConstraint(fields=('channel', 'version', 'ping_type', 'os', 'build_id', 'metric', 'metric_type', 'metric_key', 'client_agg_type'), name='fenix_unique_dimensions'),
        ),
        migrations.CreateModel(
            name='FenixAggregationView',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('channel', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('ping_type', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('build_id', models.CharField(max_length=100)),
                ('metric', models.CharField(max_length=200)),
                ('metric_type', models.CharField(max_length=100)),
                ('metric_key', models.CharField(blank=True, max_length=200)),
                ('client_agg_type', models.CharField(blank=True, max_length=100)),
                ('total_users', models.IntegerField()),
                ('histogram', models.TextField(blank=True, null=True)),
                ('percentiles', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'view_glam_fenix_aggregation',
                'managed': False,
            },
        ),
    ]