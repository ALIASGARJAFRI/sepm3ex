def encrypt(plaintext, key):
  result = ""
  for char in plaintext:
      if char.isalpha():
        if char.isupper(): 
          result += chr((ord(char)+ key - 65) % 26 + 65)

        else :
           result += chr((ord(char)+ key - 97) % 26 + 97)
      else:
        char += result

  return result

def decrypt (plaintext, key):
         result = ""
         for char in plaintext:
            if char.isalpha():
              if char.isupper(): 
               result += chr((ord(char)- key - 65) % 26 - 65)
              else :
                result +=  chr((ord(char)- key - 97) % 26 + 97)
            else:
                char +=result

         return result






def main():
           plaintext = input("please enter your text")
           key = int(input("please enter your key"))

           encrypted_text = encrypt(plaintext, key)
           decrypted_text = decrypt(encrypted_text, key)

           print("emcrpted text is" + (encrypted_text))
           print("decrypted text is" + (decrypted_text))

if __name__ == '__main__':
    main()






