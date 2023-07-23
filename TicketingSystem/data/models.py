
from django.db import models

# Create your models here.

        

        
class api_data(models.Model):
    #model fields
    E_ID =models.AutoField(primary_key=True)
    OLT_Hostname = models.CharField(max_length=50,null=True,blank=True)
    Branch_name = models.CharField(max_length=100,null=True,blank=True)
    
    Pon_port = models.CharField(max_length =50,null=True,blank=True)
    Onu_id = models.CharField(max_length =10,null=True,blank=True)
    ONU_Serial_number =models.CharField(max_length=50,null=True,blank=True)
    User_Description =models.CharField(max_length=50,null=True,blank=True)
    Admin_Status= models.CharField(max_length=50,null=True,blank=True)
    Operational_Status=models.CharField(max_length=50,null=True,blank=True)
    PON_Admin_Status=models.CharField(max_length=50,null=True,blank=True)
    PON_Opertional_Status=models.CharField(max_length=50,null=True,blank=True)

    Customer_type = models.CharField(max_length=50,null= True, blank = True)
    
    Last_Update=models.CharField(max_length=50,null=True,blank=True)
    Host_Status=models.CharField(max_length=50,null=True,blank=True)
    Uptime= models.TimeField(max_length=50,null=True,blank=True)
    Downtime = models.TimeField(max_length=50,null=True,blank=True)
    acknowledged_status = models.CharField(max_length=50,null=True,blank=True)
    Remarks = models.CharField(max_length=255,null=True,blank=True)

   
   
    #displaying in terms of table
    class Meta:
        verbose_name_plural ="API Data"
        ordering = ['E_ID',
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
                    'Last_Update',
                    'Host_Status',
                    'Uptime',
                    'Downtime',
                    'acknowledged_status',
                    'Remarks']
    
   
      

