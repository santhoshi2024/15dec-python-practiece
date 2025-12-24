gold_rate = 12,300 
earings=6
ring=4
bangles=40
chain=20
necklace=24

print('welcome')

gold=input("DO U WANT TO BUY GOLD yes/no")
if gold == "no":
    print("ok, no purchase")

year = int(input('enter the year 2026,2027,2028'))
if gold == "yes":
  if year == 2026:
    print("gold rate is 12,300")
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
  elif year == 2027:
    gold_rate= 12,300
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
  elif year == 2028:
    gold_rate == 12,300
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
else: 
  print("ok, no purchase")           
   
ACCORING_TO_WEIGHT= str(input("please enter ornaments weight"))
gold_cost1=earings*gold_rate
gold_cost2=necklace*gold_rate
gold_cost3=chain*gold_rate
gold_cost4=ring*gold_rate
gold_cost5=bangles*gold_rate
gold_cost = gold_cost1 + gold_cost2 + gold_cost3 + gold_cost4 + gold_cost5

print(f"only net costof gold{gold_cost}Rs.")
#increases  by 6% every year 
increase_value=gold_rate*6 /100

print("Would you like me calculate with GST")

GST=int(gold_cost*2/100)
total_value=gold_cost + increase_value + GST



