import requests
import random
import json

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org/messages",
        auth=("api", "a0a8e747fefc0b76d54e2ca06d624adf-c8c889c9-690a34bf"),
        data={"from": "postmaster@sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org",
              "to": ["milagorobchenko@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

def send_other_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org/messages",
        auth=("api", "a0a8e747fefc0b76d54e2ca06d624adf-c8c889c9-690a34bf"),
        data={"from": "postmaster@sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org",
              "to": ["milagorobchenko@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
            
send_other_message()
#calling the function
#send_simple_message()

emails = ["Heyyyyy Jan", "This is not (yes it is) spam from Mila", "Yo Jan! What's up dawg??", "Why do you call yourself the 'unsocial blobfish', why not call yourself the 'unsocial blubberbutt"]

email = random.choice(emails)

def send_complex_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org/messages",
        auth=("api", "a0a8e747fefc0b76d54e2ca06d624adf-c8c889c9-690a34bf"),
        data={"from": "postmaster@sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org",
              "to": "markjansorenson@gmail.com", "milagorobchenko@gmail.com"
              "subject": "Spam from the best sister:)",
              "text": email})

send_complex_message()

def jan_email_route():
  return requests.post(
    "https://api.mailgun.net/v3/routes",
        auth=("api", "a0a8e747fefc0b76d54e2ca06d624adf-c8c889c9-690a34bf"),
        data={"priority": 0,
              "description": "Jan Email Route",
              "expression": "match_recipient('markjansorenson@gmail.com')",
              "action": ["store(notify='http://mydomain.com/callback')", "stop()"]})

def get_jan_email():
  return requests.get(
    "https://api.mailgun.net/v3/sandbox5f30fe6fccef44338a09f3817cd74e1b.mailgun.org/events",
      auth=("api", "a0a8e747fefc0b76d54e2ca06d624adf-c8c889c9-690a34bf"),
      params={
        "recipient" : "markjansorenson@gmail.com",
        "limit" : 3,
      }
  )

def get_simple_message(link):
  return requests.get(
    link,
    auth=("api", "a0a8e747fefc0b76d54e2ca06d624adf-c8c889c9-690a34bf"),
  )

#empty array to add recipient urls using for loop function
links = []

recipient = get_jan_email().json()

#people_to_send_to = []

#links.append adds info abt the recipient's urls to empty links array
#for loop to display each hit of recipient urls
for i in range(len(recipient["items"])):
  links.append(recipient["items"][i]["storage"]["url"])

for urls in links:
  #print(urls)
  #print("It worked!")
  if "unsocial" in get_simple_message(urls).json()["stripped-text"]:
    #print(get_simple_message(urls).json()["stripped-text"])
    send_complex_message()
    print("I sent a complex message!")


#type tells what kind of data it is
#print(json.dumps(recipient, indent=4)[111])
