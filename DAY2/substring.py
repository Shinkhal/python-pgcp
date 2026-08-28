def manual_substring():
  word = input("Enter the word : ")
    
  sub = input("Enter Substring : ")
  count = 0
  start =0
  while True:
    pos = word.find(sub, start)
    if pos == -1:
      break
    count+=1
    start = pos +1
     
  print(count)
    
manual_substring()