def final_rate(price,q):
    total=price*q
    return total

def calc_discount(dis):
    discount=(dis/100)*total
    return discount

def total_bill(total,discount,tax):
    discounted_bill=total-discount
    final=discounted_bill+((tax/100)*discounted_bill)
    return final

item_price=float(input("Enter Item Price: "))
qty=float(input("Enter Quantity: "))
discount=float(input("Enter Discount %. if any: "))
tax=float(input("Enter tax %: "))

total=final_rate(item_price,qty)
discount=round(calc_discount(discount),2)
final_bill= round(total_bill(total,discount,tax),2)
print("\n")
print(f"Total: {total}")
print(f"Discount: {discount}")
print(f"Tax%: {tax}%")
print(f"Final Bill: Rs {final_bill}")