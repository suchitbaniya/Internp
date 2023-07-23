import requests
from requests.auth import HTTPBasicAuth
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json 
from .models import api_data

#fetching data from api
def fetch_data_from_api():
    url = 'https://horizon.subisu.net.np/api/corporateOnu/'
    username = 'ems'
    password = 'Subisu#321'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))
#mapping the conditions by creating dictionary
    status_mapping ={
         "1":"up",
         "2":"down",
         'True':'up',
         'False':'down'
    }

    customer_type_mapping ={
         "1" :"SME",
         "2" : "Co-orporate"
    }


  #checking response

    if response.status_code == 200:
        data = response.json() #saving data in json 
        

       

        #iterating data in api and getting data in variable for saving in database
        for item in data:
                customer_type=item.get('Customer Type', None)
                OLT=item.get('OLT HostName', None)
                Branch=item.get('Branch Name', None)
                
                Serial_number=item.get('ONU Serial', None)
                Description=item.get('User Descr', None)
                Admin_s=item.get('Admin Status', None)
                Operational_S=item.get('Operational Status', None)
                admin_Status=item.get('PON Admin Status', None)
                pon_Opertional_Status=item.get('PON Operational Status', None)
                last_update=item.get('Last Update', None)
                host_Status=item.get('Host Status', None)
                
                Pon_port = item.get('Pon Interface',None)
                Onu_id =item.get('Onu Interface',None)
                downtime = str(last_update)[11:19]
               
                exitising_data = api_data.objects.filter(
                     OLT_Hostname=OLT,
                     Pon_port=Pon_port,
                     Onu_id= Onu_id,
                     ONU_Serial_number=Serial_number,
                     Operational_Status=status_mapping.get(Operational_S,None),

                ).first()

                print(OLT)

                if exitising_data:
                     if exitising_data.Operational_Status != status_mapping.get(Operational_S,None) :
                          exitising_data.Operational_Status = status_mapping.get(Operational_S,None)
                          exitising_data.acknowledged_status = "open" if status_mapping.get(Operational_S,None)=="down" else None
                          exitising_data.save()
                else:
                #saving in the database
                    my_data =api_data(
                        Customer_type=customer_type_mapping.get(customer_type,None),
                        OLT_Hostname=OLT,
                        Branch_name=Branch,
                        
                        Pon_port=Pon_port , #joining the value of ponport and onu id
                        Onu_id =Onu_id,
                        ONU_Serial_number=Serial_number,
                        User_Description=Description,
                        Admin_Status=status_mapping.get(Admin_s,None), #mapping with status id
                        Operational_Status=status_mapping.get(Operational_S,None),
                        PON_Admin_Status=status_mapping.get(admin_Status,None),
                        PON_Opertional_Status=status_mapping.get(pon_Opertional_Status,None),
                        Last_Update=last_update,
                        Host_Status= host_Status,
                        Downtime=downtime,

                )
               
                    #acknowledged status will be open while operational data will be down
                    if my_data.Operational_Status == "down":
                        my_data.acknowledged_status = "Open"
                        
                
                    #saving the data
                    my_data.save()
            

    else:
        return HttpResponse("error in retrival")


def check_data():
     
     status_mapping ={
         "1":"up",
         "2":"down",}
     
     customer_type_mapping ={
         "1" :"SME",
         "2" : "Co-orporate"
    }
    
     #retreiving hostname and serial no from model to check 
     sending_data_to_check= list(api_data.objects.filter(acknowledged_status= 'Open').values('OLT_Hostname','ONU_Serial_number','Pon_port','Onu_id'))
     
   
     #preparing data to send
     

     username = 'ems'
     password = 'Subisu#321'

     api_to_check = "https://horizon.subisu.net.np/api/corporateUpdateStatus/?hostname={}&serial={}&ponInterface={}&onuId={}"
    #passing the data to the api
     for item in sending_data_to_check:
          hostname= item['OLT_Hostname']
          serialno= item['ONU_Serial_number']
          ponport= item ['Pon_port']
          onuid= item['Onu_id']


          url = api_to_check.format(hostname,serialno,ponport,onuid)

          response = requests.get(url, auth= HTTPBasicAuth(username,password))
          returned_data =response.json()

          for item in returned_data:
               if not isinstance(item,dict):
                    continue
               
               r_c_type = item.get('Customer Type',None)
               r_hostname = item.get('OLT HostName',None)
               r_branch= item .get('Branch Name',None)
               r_pon_port = item.get('Pon Interface',None)
               r_onu_id = item.get('Onu Interface',None)
               r_serial = item.get('ONU Serial',None)
               r_desc = item.get('User Descr',None)
               r_admin_status = item.get('Admin Status',None)
               r_ONU_status = item.get('Operational Status', None)
               r_p_admin_status = item.get('PON Admin Status',None)
               r_p_o_status = item.get('PON Operational Status',None)
               r_l_update=item.get('Last Update',None)
               r_H_status =item.get('Host Status',None)


               data_in_db = api_data.objects.filter(
                    OLT_Hostname= r_hostname,
                    Pon_port= r_pon_port,
                    Onu_id= r_onu_id,
                    ONU_Serial_number= r_serial).first()
               
               if data_in_db:
                     if data_in_db.Operational_Status != status_mapping.get(r_ONU_status, None):
                    # Update the existing record
                        data_in_db.Customer_type = customer_type_mapping.get(r_c_type, None)
                        data_in_db.Branch_name = r_branch
                        data_in_db.User_Description = r_desc
                        data_in_db.Admin_Status = status_mapping.get(r_admin_status, None)
                        data_in_db.Operational_Status = status_mapping.get(r_ONU_status, None)
                        data_in_db.PON_Admin_Status = status_mapping.get(r_p_admin_status, None)
                        data_in_db.PON_Opertional_Status = status_mapping.get(r_p_o_status, None)
                        data_in_db.Last_Update = r_l_update
                        data_in_db.Host_Status = r_H_status

                        if data_in_db.Operational_Status == 'up':
                            data_in_db.Uptime = data_in_db.Last_Update[11:19]
                            data_in_db.acknowledged_status = data_in_db.acknowledged_status
                        elif data_in_db.Operational_Status == 'down':
                            data_in_db.Downtime = data_in_db.Last_Update[11:19]
                            data_in_db.acknowledged_status = data_in_db.acknowledged_status

                        data_in_db.save()
               else:
                    my_data =api_data(
                    Customer_type=customer_type_mapping.get(r_c_type,None),
                    OLT_Hostname=r_hostname,
                    Branch_name=r_branch,
                    Pon_port=r_pon_port ,
                    Onu_id =r_onu_id,
                    ONU_Serial_number=r_serial,
                    User_Description=r_desc,
                    Admin_Status=status_mapping.get(r_admin_status,None), #mapping with status id
                    Operational_Status=status_mapping.get(r_ONU_status,None),
                    PON_Admin_Status=status_mapping.get(r_p_admin_status,None),
                    PON_Opertional_Status=status_mapping.get(r_p_o_status,None),
                    Last_Update=r_l_update,
                    Host_Status= r_H_status,
                    
                    )

                    if my_data.Operational_Status == 'up':
                        my_data.Uptime = my_data.Last_Update[11:19]
                   
                    elif my_data.Operational_Status == 'down'  :
                        my_data.Downtime= my_data.Last_Update[11:19]
                      

                    my_data.save()

               

               

    
          


     
    
   




     

    

   
     
    
     
     