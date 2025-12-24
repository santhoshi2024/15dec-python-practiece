gold_rate = 12300 


print('welcome')

gold=input("DO U WANT TO BUY GOLD yes/no")

if gold == "no":
    print("ok, no purchase")

year = int(input('enter the year 2026,2027,2028'))
if gold == "yes":
  if year == 2026:
    print("gold rate is 12,300")
  
  elif year == 2027:
    gold_rate= 12,300
  
  elif year == 2028:
    gold_rate == 12,300
 
else: 
  print("ok, no purchase")           
   
ACCORING_TO_WEIGHT= str(input("please enter ornaments weight"))
gold_cost = int((ACCORING_TO_WEIGHT)*gold_rate)


print(f"only net costof gold{gold_cost}Rs.")
#increases  by 6% every year 
increase_value=gold_rate*6 /100

print("Would you like me calculate with GST")

GST=int(gold_cost*2/100)
total_value=gold_cost + increase_value + GST



