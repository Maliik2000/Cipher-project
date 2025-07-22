#Malik Windham
#Caesar Decypher for 10 letter shift
def decypher(message):
  hold = []
  for letter in message:
    if letter == " " or letter == "!" or letter == "." or letter == "?" or letter == "," or letter == "\n":
      hold.append(letter)
    elif ord(letter) + 10 > 122:
      hold.append(chr(ord(letter) - 16))
    else:
      hold.append(chr(ord(letter) + 10))
  decoded = "".join(hold)
  return decoded

#Ceasar Decypher for 14 letter shift
def decypher_special(message):
  hold = []
  for letter in message:
    if letter == " " or letter == "!" or letter == "." or letter == "?" or letter == "," or letter == "\n" or letter == "'":
      hold.append(letter)
    elif ord(letter) + 14 > 122:
      hold.append(chr(ord(letter) - 12 ))
    else:
      hold.append(chr(ord(letter) + 14))
  decoded = "".join(hold)
  return decoded
#Breaks all caesar ciphers
def trial_by_fire(message):
  offset = 26
  trial = 0
  
  while(offset >= 1):
    hold = []
    print("OFFSET NUMBER: ", offset)
    for letter in message:
      if letter == " " or letter == "!" or letter == "." or letter == "?" or letter == "," or letter == "\n" or letter == "'":
        hold.append(letter)
      elif ord(letter) + offset > 122:
        hold.append(chr(ord(letter) - trial ))
      else:
        hold.append(chr(ord(letter) + offset))
    verify = "".join(hold)
    print(verify, "\n")
    trial += 1
    offset -= 1
  
#Ceasar encyrption 10 letter shift
def encryption(message):
  hold = []
  for letter in message:
    if letter == " " or letter == "!" or letter == "." or letter == "?" or letter == "," or letter == "\n":
      hold.append(letter)
    elif ord(letter) - 10 < 97:
      hold.append(chr(ord(letter) - 16))
    else:
      hold.append(chr(ord(letter) - 10))
  decoded = "".join(hold)
  return decoded.lower()

coded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj! "
check = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
To_Vishal ="i figured out how to send you messages back and uncoded your message!!"

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

decoded_message = decypher(coded_message)
sent_to = encryption(To_Vishal)


print(decoded_message, "\n")
print(decypher(first_message), "\n")
print(decypher_special(second_message), "\n")

third_message ="vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

trial_by_fire(third_message)
#Vigenere break
def vigenere_cipher(keyword, message):
  length_message = len(message)
  key_size = len(keyword)
  i = 0
  hold = []
  while( length_message >= 1):
    for letter in message:
      if letter == " " or letter == "!" or letter == "." or letter == "?" or letter == "," or letter == "\n" or letter == "'":
        hold.append(letter)
        length_message -= 1
      else:
        hold.append(keyword[i])
        i += 1
        length_message -= 1
        if i >= key_size:
          i = 0
    
  cipher_message = "".join(hold)
  print(cipher_message)
  length_message = len(message)
  i = 0
  send = []
  for letter in message:
    if letter == " " or letter == "!" or  letter == "." or letter == "?" or letter == "," or letter == "\n":
      send.append(letter)
      i += 1 
    elif abs(ord(cipher_message[i]) - 97) + ord(letter) > 122:
      send.append(chr(abs(ord(cipher_message[i]) - 97) + ord(letter) - 26 ))
      i += 1
    else:
      send.append(chr(abs(ord(cipher_message[i]) -97) + ord(letter)))
      i += 1
  decoded = "".join(send)
  print(decoded)
  
 #vigenere encrypt
def vigenere_encryption(keyword, message):
  length_message = len(message)
  key_size = len(keyword)
  i = 0
  hold = []
  while( length_message >= 1):
    for letter in message:
      if letter == " " or letter == "!" or letter == "." or letter == "?" or letter == "," or letter == "\n" or letter == "'":
        hold.append(letter)
        length_message -= 1
      else:
        hold.append(keyword[i])
        i += 1
        length_message -= 1
        if i >= key_size:
          i = 0
    
  cipher_message = "".join(hold)
  #print(cipher_message)
  length_message = len(message)
  i = 0
  send = []
  for letter in message:
    if letter == " " or letter == "!" or  letter == "." or letter == "?" or letter == "," or letter == "\n":
      send.append(letter)
      i += 1 
    elif abs(ord(letter) - (ord(cipher_message[i]) - 97)) < 97:
      send.append(chr(abs(ord(letter) - (ord(cipher_message[i]) - 97) + 26 )))
      i += 1
    else:
      send.append(chr(abs(ord(letter) - (ord(cipher_message[i]) - 97))))
      i += 1
  decoded = "".join(send)
  return decoded

key_1st = "friends"
vigenere_cipher_1st = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
vigenere_cipher(keyword = key_1st, message = vigenere_cipher_1st)

key_2nd = "mcdonalds"
my_message = "we did it we did it we did it yea!"

my_message_encrypt = vigenere_encryption(keyword = key_2nd, message = my_message)

print(my_message_encrypt)

vigenere_cipher(keyword = key_2nd, message = my_message_encrypt)
