from Stack import Stack

def convert_int_to_bin(dec_num):
  
  s = Stack()
  while(dec_num > 0):

    s.push(dec_num%2)
    dec_num = dec_num // 2

  fin = ""
  while not s.isEmpty():
    fin += str(s.pop())

  return fin
  
    
  

print(convert_int_to_bin(100))