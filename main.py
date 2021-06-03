def SplitTheBill(ppl,bill,tip):
  share = (1+ tip)* bill/ppl
  share = round(share,2)
  return share
  
print(SplitTheBill(5,100.13))

print(f" I went to dinner last night with 4 friends and I spent ${SplitTheBill(5,61.61,0.15)}.")

animal = input("What is your Favorite animal?")

print(animal)
