import creds
import openai
import os

os.environ["OPENAI_KEY"] = creds.API_KEY
openai.api_key = os.environ["OPENAI_KEY"]


# keep_prompting = True
# while keep_prompting:
#     prompt = input("Please enter your image prompt. Type exit if done. ")
#     n = int(input("Please enter the number of images you want to generate. "))
#     if prompt == "exit":
#         keep_prompting = False
#     else:
#         image_gen = openai.Image.create(prompt=prompt,
#                                         n=n,
#                                         size="1024x1024")
#
#         for img in range(0,n):
#             print(image_gen["data"][img]["url"])
#

# for editing image with dall-e
# image_edit = openai.Image.create_edit(
#     image=open("Arm.png","rb"),
#     mask=open("noArm.png","rb"),
#     prompt="A woman wearing an arm prosthesis.",
#     n=1,
#     size="1024x1024",
#
# )
# print(image_edit)


# for image variation
image_variation = openai.Image.create_variation(
    image=open("prosthesis.png","rb"),
    n=3,
    size="1024x1024"

)
print(image_variation)

