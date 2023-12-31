# Generated by Django 4.2.3 on 2023-07-19 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_api_data_options_api_data_onu_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api_data',
            options={'ordering': ['E_ID', 'OLT_Hostname', 'Branch_name', 'Pon_port', 'Onu_id', 'ONU_Serial_number', 'User_Description', 'Admin_Status', 'Operational_Status', 'PON_Admin_Status', 'PON_Opertional_Status', 'Last_Update', 'Host_Status', 'Uptime', 'Downtime', 'acknowledged_status', 'Remarks'], 'verbose_name_plural': 'API Data'},
        ),
        migrations.RemoveField(
            model_name='api_data',
            name='Interface',
        ),
    ]
