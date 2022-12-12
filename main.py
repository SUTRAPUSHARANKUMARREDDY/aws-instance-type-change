import json
import boto3
import requests

region = input()
privtip = input()
instanceid = input()
newinstancetype = input()

slack_webhook_url ='https://hooks.slack.com/services/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'


c4_large	  = (", vCPU = 2, Memory (GiB) = 3.75")
c5_2xlarge	  = (", vCPU = 8, Memory (GiB) = 16")
c5_4xlarge	  = (", vCPU = 16, Memory (GiB) = 32")
c5_9xlarge	  = (", vCPU = 36, Memory (GiB) = 72")
c5a_4xlarge  = (", vCPU = 16, Memory (GiB) = 32")
m5_2xlarge	  = (", vCPU = 8, Memory (GiB) = 32")
m5_4xlarge	  = (", vCPU = 16, Memory (GiB) = 64")
m5_large	  = (", vCPU = 2, Memory (GiB) = 8")
m5_xlarge	  = (", vCPU = 4, Memory (GiB) = 16")
m5a_2xlarge  = (", vCPU = 8, Memory (GiB) = 32")
m5a_4xlarge  = (", vCPU = 16, Memory (GiB) = 64")
m5a_8xlarge  = (", vCPU = 32, Memory (GiB) = 128")
m5a_large	  = (", vCPU = 2, Memory (GiB) = 8")
m5a_xlarge	  = (", vCPU = 4, Memory (GiB) = 16")
p3_2xlarge	  = (", vCPU = 8, Memory (GiB) = 61")
t2_2xlarge	  = (", vCPU = 8, Memory (GiB) = 32")
t2_large	  = (", vCPU = 2, Memory (GiB) = 8")
t2_medium	  = (", vCPU = 2, Memory (GiB) = 4")
t2_micro	  = (", vCPU = 1, Memory (GiB) = 1")
t2_small	  = (", vCPU = 1, Memory (GiB) = 2")
t2_xlarge	  = (", vCPU = 4, Memory (GiB) = 16")
t3_2xlarge	  = (", vCPU = 8, Memory (GiB) = 32")
t3_large	  = (", vCPU = 2, Memory (GiB) = 8")
t3a_medium	  = (", vCPU = 2, Memory (GiB) = 4")

def send_slack_message(slack_webhook_url, slack_message):
  print('>send_slack_message:slack_message:'+slack_message)
  slack_payload = {'text': slack_message}
  print('>send_slack_message:posting message to slack channel')
  response = requests.post(slack_webhook_url, json.dumps(slack_payload))
  response_json = response.text  # convert to json for easy handling
  print('>send_slack_message:response after posting to slack:'+str(response_json))

def change_instance_type():

  notification_message = 'The Below EC2 instance type is changed: \n'

  INSTANCE_ID = instanceid
  EC2_RESOURCE = boto3.resource('ec2', region_name=region)
  
  instances = EC2_RESOURCE.instances.filter(
    InstanceIds=[
        INSTANCE_ID,
    ],
  )

  for instance in instances:
    for tag in instance.tags:
                if 'Name'in tag['Key']:
                    name = tag['Value']
    state= instance.state["Name"]
    type=instance.instance_type
    privateip=instance.private_ip_address
    InstanceName = name
    
    if state == 'running':
      if newinstancetype != type:
        if privateip == privtip:
          client = boto3.client("ec2", region_name=region)
          client.stop_instances(InstanceIds=[instanceid])
          waiter=client.get_waiter('instance_stopped')
          waiter.wait(InstanceIds=[instanceid])
          client.modify_instance_attribute(InstanceId=instanceid, Attribute='instanceType', Value=newinstancetype)
          client.start_instances(InstanceIds=[instanceid])
          
          ec2_info = "Instance Name: " + InstanceName + '\n'
          ec2_info = ec2_info + "Region: " + region + '\n'
          ec2_info = ec2_info + "InstanceId: " + instanceid + '\n'
          
          if type == 'c4.large':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + c4_large + '\n'
          elif type == 'c5.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + c5_2xlarge + '\n'
          elif type == 'c5.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + c5_4xlarge + '\n'
          elif type == 'c5.9xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + c5_9xlarge + '\n'
          elif type == 'c5a.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + c5a_4xlarge + '\n'
          elif type == 'm5.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5_2xlarge + '\n'
          elif type == 'm5.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5_4xlarge + '\n'
          elif type == 'm5.large':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5_large + '\n'
          elif type == 'm5.xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5_xlarge + '\n'
          elif type == 'm5a.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5a_2xlarge + '\n'
          elif type == 'm5a.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5a_4xlarge + '\n'
          elif type == 'm5a.8xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5a_8xlarge + '\n'
          elif type == 'm5a.large':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5a_large + '\n'
          elif type == 'm5a.xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + m5a_xlarge + '\n'
          elif type == 'p3.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + p3_2xlarge + '\n'
          elif type == 't2.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t2_2xlarge + '\n'
          elif type == 't2.large':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t2_large + '\n'
          elif type == 't2.medium':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t2_medium + '\n'
          elif type == 't2.micro':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t2_micro + '\n'
          elif type == 't2.small':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t2_small + '\n'
          elif type == 't2.xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t2_xlarge + '\n'
          elif type == 't3.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t3_2xlarge + '\n'
          elif type == 't3.large':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t3_large + '\n'
          elif type == 't3a.medium':
            ec2_info = ec2_info + "Instance Type Changed from: " + type + t3a_medium + '\n'
          else:
            ec2_info = ec2_info + "Instance Type Changed from: " + type + ", Hardware Not Decleared" + '\n'
          
          
          if newinstancetype == 'c4.large':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + c4_large + '\n'
          elif newinstancetype == 'c5.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + c5_2xlarge + '\n'
          elif newinstancetype == 'c5.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + c5_4xlarge + '\n'
          elif newinstancetype == 'c5.9xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + c5_9xlarge + '\n'
          elif newinstancetype == 'c5a.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + c5a_4xlarge + '\n'
          elif newinstancetype == 'm5.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5_2xlarge + '\n'
          elif newinstancetype == 'm5.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5_4xlarge + '\n'
          elif newinstancetype == 'm5.large':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5_large + '\n'
          elif newinstancetype == 'm5.xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5_xlarge + '\n'
          elif newinstancetype == 'm5a.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5a_2xlarge + '\n'
          elif newinstancetype == 'm5a.4xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5a_4xlarge + '\n'
          elif newinstancetype == 'm5a.8xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5a_8xlarge + '\n'
          elif newinstancetype == 'm5a.large':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5a_large + '\n'
          elif newinstancetype == 'm5a.xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + m5a_xlarge + '\n'
          elif newinstancetype == 'p3.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + p3_2xlarge + '\n'
          elif newinstancetype == 't2.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t2_2xlarge + '\n'
          elif newinstancetype == 't2.large':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t2_large + '\n'
          elif newinstancetype == 't2.medium':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t2_medium + '\n'
          elif newinstancetype == 't2.micro':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t2_micro + '\n'
          elif newinstancetype == 't2.small':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t2_small + '\n'
          elif newinstancetype == 't2.xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t2_xlarge + '\n'
          elif newinstancetype == 't3.2xlarge':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t3_2xlarge + '\n'
          elif newinstancetype == 't3.large':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t3_large + '\n'
          elif newinstancetype == 't3a.medium':
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + t3a_medium + '\n'
          else:
            ec2_info = ec2_info + "Instance Type Changed to: " + newinstancetype + ", Hardware Not Decleared" + '\n'
      
          notification_message += ec2_info + '\n'
          send_slack_message(slack_webhook_url, notification_message)
        else:
          print("The Private IP is Not Matching")
      else:
        print("The Requested Instance Type is same as Present Instance Type")
    else:
      print("The Instance is in STOP State")
    
def lambda_handler(event, context):
    change_instance_type()
    return {
      'statusCode': 200,
      'body': json.dumps('The Instance type change Process is completed.')
    }