from django.contrib import admin
from .models import api_data
# Register your models here.

#displaying in tabular form 
class Adminmodel(admin.ModelAdmin):
    list_display = ('E_ID',
                    'OLT_Hostname',
                    'Branch_name',
                    'Pon_port',
                    'Onu_id',
                    'ONU_Serial_number',
                    'User_Description',
                    'Admin_Status',
                    'Operational_Status',
                    'PON_Admin_Status',
                    'PON_Opertional_Status',
                    'Customer_type',
                    'Last_Update',
                    'Host_Status',
                    'Uptime',
                    'Downtime',
                    'acknowledged_status',
                    'Remarks'
      )
    
    
   

admin.site.register(api_data,Adminmodel)
