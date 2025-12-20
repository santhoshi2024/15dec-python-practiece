gold_rate_2026= 12,300


earings=6
ring=4
bangles=40
chain=20
necklace=24


print('welcome')

gold=input("DO U REALLY WANT TO BUY GOLD")

year=input("which year do u want to buy gold")
if 2026:
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
if 2027:
     print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
if 2028:
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
else:
   print('TRY NEXT YEAR')
   
ACCORING_TO_WEIGHT=input("please enter ornaments weight")

weight=6,4,40,20,24

gold_cost1=earings*gold_rate_2026
gold_cost2=necklace*gold_rate_2026 
gold_cost3=chain*gold_rate_2026
gold_cost4=ring*gold_rate_2026

#increases  by 6% every year 
increase_value=12,300*6 /100
GST=int(gold_cost1*2/100)
total_value=gold_cost + increase_value + GST


print(f("only net costof gold{gold_cost}Rs.")) 
print("Would you like me calculate with GST")