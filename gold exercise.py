gold_rate_2026= 12,300


earings=6
ring=4
bangles=40
chain=20
necklace=24

print('welcome')

gold=input("DO U REALLY WANT TO BUY GOLD")
if gold == "yes":
   year=input("which year do u want to buy gold")
elif year == "2026":
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
elif year == "2027":
     print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
elif year == "2028":
    print("earings-6, ring-4, bangles-40, chain-20, necklace-24")
else:
   print('TRY NEXT YEAR')
   
ACCORING_TO_WEIGHT=input("please enter ornaments weight")



gold_cost1=earings*gold_rate_2026
gold_cost2=necklace*gold_rate_2026 
gold_cost3=chain*gold_rate_2026
gold_cost4=ring*gold_rate_2026
gold_cost5=bangles*gold_rate_2026

print(f("only net costof gold{gold_cost}Rs.")) 

#increases  by 6% every year 
increase_value=12,300*6 /100

print("Would you like me calculate with GST")

GST=int(gold_cost1*2/100)
total_value=gold_cost1 + increase_value + GST



