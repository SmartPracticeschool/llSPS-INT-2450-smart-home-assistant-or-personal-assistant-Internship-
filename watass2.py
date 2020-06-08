import json
import time
import urllib.request
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('M2ljxzuy3oyk4t19gYgThAOfLnKQOaDQqnlNx7ybRJ9n')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/919ffb9a-8a06-4a80-ad16-aad032b9231a')
while True:
    val = input("Hello there!!! How can i help you,\n Enter your message: ") 
    print("USER:",val) 
    
    response = assistant.message(
        assistant_id='2ef0a873-6266-490b-ac3e-93f0203ea5c3',
        session_id='433e3128-4541-4ceb-aba4-31d7a0c42f3d',
        input={
            'message_type': 'text',
            'text': val
        }
        
    ).get_result()

    value1=json.dumps(response, indent=2)
##    print("value1")
##    print(value1)
    val2=response['output']['generic'][0]['text']
    print("BOT:",val2) 
##    print('val2')
##    print(val2)
    time.sleep(2)
    
   
    
    
       
       
    
