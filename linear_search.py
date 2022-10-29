r1 = int(input('enter start of range: '))
r2 = int(input('enter end of range: '))
numbers = list(range(r1,r2))
req_num = int(input("enter target: "))
def linear_search(list, target):
  for i in range(0,len(list)):
    if list[i] == target:
      return i
  return None

def verify(index):
  if index is not None:
    print(f"Value found at {index}")
  else:
    print("value not found")

result = linear_search(numbers, req_num)
verify(result)