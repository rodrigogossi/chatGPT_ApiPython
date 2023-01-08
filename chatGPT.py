import openai

openai.api_key = ""

#response = openai.Completion.create(
# model="text-davinci-003",
# prompt="fale sobre como criar um blog",
# temperature=0,
# max_tokens=1000,
# top_p=1,
# frequency_penalty=0.5,
# presence_penalty=0
#)


response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

print(image_url)