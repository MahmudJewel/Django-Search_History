def get_prefix_arr(pattern, b):
    prefix_arr = [0] * b
    n = 0
    m = 1
    while m != b:
        if pattern[m] == pattern[n]:
            n += 1
            prefix_arr[m] = n
            m += 1
        elif n != 0:
                n = prefix_arr[n-1]
        else:
            prefix_arr[m] = 0
            m += 1
    return prefix_arr

def Search(pattern, text):
    a = len(text)
    b = len(pattern)
    prefix_arr = get_prefix_arr(pattern, b)
  
    found = []
    m = 0
    n = 0
  
    while m != a:
       
        if text[m] == pattern[n]:
            m += 1
            n += 1
      
        else:
            n = prefix_arr[n-1]
       
        if n == b:
            found.append(m-n)
            n = prefix_arr[n-1]
        elif n == 0:
            m += 1
   
    return found

text = input("Enter text: ")
pat = input('Enter pattern : ')
result = Search(pat, text)
print(f"{pat} founds {len(result)} times in {text}")
