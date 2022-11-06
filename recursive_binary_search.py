r1 = int(input('enter start of range: '))
r2 = int(input('enter end of range: '))
numbers = list(range(r1,r2))
req_num = int(input("enter target: "))
def recursive_binary_search(list,target):
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list))//2
    if list[midpoint]==target:
      return True
    else:
      if list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:],target)
      else:
        return recursive_binary_search(list[:midpoint],target)
def verify(result):
  print('target found: ', result)

result = recursive_binary_search(numbers,req_num)
verify(result)