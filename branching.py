kw_used=float(input("How much KW did you used\n"))
main=1000
base=0.07633
overage=0.09259
base_cost=(main*base)
if kw_used<=main:
    print("the total cost is $",round(kw_used*base))
else:
    excess=kw_used-main
    overage_cost=overage*excess
    total=base_cost+overage_cost
    (round(total))
    print("the total cost is $",round(total))

