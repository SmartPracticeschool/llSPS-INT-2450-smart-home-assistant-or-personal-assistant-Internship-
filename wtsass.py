import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('M2ljxzuy3oyk4t19gYgThAOfLnKQOaDQqnlNx7ybRJ9n')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/919ffb9a-8a06-4a80-ad16-aad032b9231a')

response = assistant.create_session(
    assistant_id='2ef0a873-6266-490b-ac3e-93f0203ea5c3'
).get_result()

print(json.dumps(response, indent=2))
