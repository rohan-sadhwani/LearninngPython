# Create a dictionary and take input from the user and return the meaning of the word from the dict

d1 = {"action": "something that is done for a particular purpose.",
      "anger": "a strong emotion brought on by a person or thing that causes one great pain or trouble.",
      "fear": "a strong feeling one gets when one expects danger or pain.",
      "hate": "to dislike very strongly.",
      "love": "strong feelings of affection for another person or thing."
      }

key = input("Enter key to find there meaning : ")

if key in d1.keys():
    print(key, ":", d1[key])
else:
    print("Key not available in dict")
