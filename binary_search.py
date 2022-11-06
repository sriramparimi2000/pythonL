r1 = int(input('enter start of range: '))
r2 = int(input('enter end of range: '))
numbers = list(range(r1,r2))
req_num = int(input("enter target: "))
def binary_search(list,target):
  first = 0
  last = len(list) - 1
  while first <= last:
    middle = (first+last) // 2
    if list[middle] == target:
      return middle
    elif list[middle] < target:
      first = middle + 1
    else:
      last = middle - 1
  return None

def verify(index):
  if index is not None:
    print(f"Value found at {index}")
  else:
    print("value not found")

result = binary_search(numbers, req_num)
verify(result)