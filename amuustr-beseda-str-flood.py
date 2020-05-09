print ("""
Working.
@muuT3ra$$uu-kick-my-str-v.1
#FuckAllEverything. 
by Tripl_color vk.com/Tripl_color""")
import vk_requests
import time
import random
token = "твой айди"
cid = str(input('Айди беседы = '))

photo = "photo472165736_457244077"
audio = "audio472165736_456239668"
msg = "fuck all. by Tripl_Color. @muuT3ra$$uu-kick-my-str-v.1 "


while True:
 api = vk_requests.create_api(service_token=token)  
 print(api.messages.send(chat_id= cid, message= msg, random_id= random.randint(1, 2147483647)))
 print(api.messages.send(chat_id= cid, attachment= photo, random_id= random.randint(1, 2147483647)))
 print(api.messages.send(chat_id= cid, attachment= audio, random_id= random.randint(1, 2147483647)))
 print(api.messages.send(chat_id= cid, message= random.randint(1, 2147483647), random_id= random.randint(1, 2147483647)))

 print('Круг сообщений сделан')
 time.sleep(5)
