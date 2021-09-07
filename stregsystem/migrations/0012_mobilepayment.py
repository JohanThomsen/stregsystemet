# Generated by Django 2.2.13 on 2020-11-18 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0011_dangling_migration_20201024_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=64)),
                ('timestamp', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('transaction_id', models.CharField(max_length=32, unique=True)),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('U', 'Unset'), ('A', 'Approved'), ('I', 'Ignored')], default='U', max_length=1)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stregsystem.Member')),
                ('payment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stregsystem.Payment')),
            ],
        ),
    ]