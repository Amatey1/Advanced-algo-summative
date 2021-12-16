import itertools

def encrypt(text,key): 
    # Vals is used to store the values of the encryption
    vals=[]
    # The text is converted to a list for easier manipulation
    l = list(text)
    i=0
    # The code below goes through the list of values and skips indexes by the number"key"
    # to form an encrypted value by adding the values it iterates through .
    while i < key:
            vals.append(l[i:len(text):key])
            i+=1
    s = "".join(itertools.chain(*vals))                
    return s
print(encrypt("plain text",2))


#To decrypt the input we divide the 'total number of characters in text' by the value "key" and set it as the new "key" 
#this reverses the progression that created the encryption.
# Then repeat the encrypt process but with the new key 
def decrpyt(text,key):
    key = int(len(text)/key)
    vals=[]
    l = list(text)
    i=0
    while i < key:
            vals.append(l[i: len(text):key])
            i+=1
    s = "".join(itertools.chain(*vals))           
    return s

print(decrpyt(encrypt("plain text",2),2))
