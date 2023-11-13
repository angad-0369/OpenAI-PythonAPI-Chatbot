import creds
import os
import openai

os.environ["OPENAI_KEY"] = creds.API_KEY
openai.api_key = os.environ["OPENAI_KEY"]

prompt = "Please rate the sentiment of this tweet as positive , negative , or neutral : Impressed with @SwiftDeliver's service once again! Fast delivery, secure packaging, and excellent customer support. 👍🚚 #HappyCustomer ->"
response = openai.Completion.create(model="davinci:ft-personal-2023-08-24-15-27-39",
                                    prompt=prompt,
                                    max_tokens=1)
print(response["choices"][0]["text"])















