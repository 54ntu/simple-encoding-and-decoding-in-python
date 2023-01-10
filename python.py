
# code to convert the text to encryted text
# write a python program to translate a message into secret code language. #Use the rules below to translate normal english into secret code language.

# coding
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now apend three random characters at the starting and the end
# else:
# simply reverse the string

# decoding:
# if the word contains less than 3 charactes, reverse it

# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning


# your program should ask whether you want to code or decode..
import random

verify= input(" hello users, please be certain whether to  encode or decode : ")
if(verify == 'encode'):
  text= input("enter the text to encrypt : ")
  if (len(text)>=3):
    random_char1= chr(random.randint(97,122))
    random_char2= chr(random.randint(97,122))
    random_char3= chr(random.randint(97,122))
    random_char4= chr(random.randint(97,122))
    random_char5 = chr(random.randint(97, 122))
    random_char6 = chr(random.randint(97, 122))


    first_char= text[0]
    rem_char = text[1:]
    reversed_text= rem_char+first_char
    final_text = random_char1+random_char2+random_char3 +reversed_text+random_char4+random_char5+random_char6
    print('___________________________________________________ \n')
    print('the reversed text is : ', final_text)
    print('___________________________________________________\n')

  else:
    new_reverse_text = text[::-1]
    print("your entered string has less than 3 characters : \n")
    print('___________________________________________________\n')
    print('the reverse of a string is : ', new_reverse_text)
    print('___________________________________________________\n')

elif(verify == 'decode'):
  text= input("enter the text for decoding : ")
  if(len(text)>=3):
    new_text= text[3:-3]
    last_char= new_text[-1]
    rem_char= new_text[:-1]
    final_decoded_text= last_char+rem_char
    print('___________________________________________________ \n')
    print('The decrypted text is : ', final_decoded_text)
    print('___________________________________________________ \n')

  else:
    reversed_decoded_text = text[::-1]
    print("your entered string has less than 3 characters : \n")
    print('___________________________________________________\n')
    print('the decrypted string is : ', reversed_decoded_text)
    print('___________________________________________________\n')

else:
  print('___________________________________________________ \n')
  print("Ooooooooooooooops! you have entered wrong option.")
  print('___________________________________________________ \n')


