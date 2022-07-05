acounts = [

    {"acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
     },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]
payments_sum={}
print("heil")
all_transactions=[ac["transactions"] for ac in acounts]
for trans_list in all_transactions:
    for trans in trans_list:
      amount=trans["amount"]
      method=trans["method"]
      if method in payments_sum:
          payments_sum[method]+=amount
      else:
          payments_sum[method]=amount

print(payments_sum)

# print details of 1002
# for ac in acounts:
#     if ac["acno"]==1002:
#         print(ac.pop("transactions"))

ac_details = [ac for ac in acounts if ac["acno"] == 1002]
# print(f"ac details are{ac_details}")


# print savings type acount details
# savings_details=[ac["transactions"] for ac in acounts ]
# print(savings_details)
# sort acounts based on balance order by desc
# balance_order=sorted(acounts,key=lambda ac:ac["balance"],reverse=True)
# print(balance_order)

# acounts.sort(reverse=True,key=lambda ac:ac["balance"])
# print(acounts)

# ac_det=sorted([ac["balance"] for ac in acounts ],reverse=True)
# print(ac_det)


# list of acounts with phonepe transaction
# for ac in acounts:
#      transaction=ac["transactions"]
#      for transaction in ac:
#          for single_tract in transaction:
#              if single_tract["method"]=="phone-pay":
#                  print(transaction)


# all_transactions=[ac["transactions"] for ac in acounts]
# mini_trans=[trans for trans_list in all_transactions for trans in trans_list if trans["method"]=="phone-pay"]
# print(mini_trans)
#


# print all transactions where transaction amount > 500
# all_transactions=[ac["transactions"] for ac in acounts]
# print(all_transactions)
# amount_gt_500=[trans for trans_list in all_transactions for trans in trans_list if trans["amount"]>500 ]
# print(amount_gt_500)


# credit transactions of 1002
# all_transactions=[ac["transactions"] for ac in acounts]
# credit_1002=[credit for trans in all_transactions for credit in trans if credit["to"]==1002]
# print(credit_1002)

# agregate transaction based on payment method

# all_transactions=[ac["transactions"] for ac in acounts]
# g_pay_trans=[gpay["amount"] for trans in all_transactions for gpay in trans if gpay["method"]=="g-pay"]
# neft_trans=[neft["amount"] for trans in all_transactions for neft in trans if neft["method"]=="neft"]
# phonepe_trans=[phonepe["amount"] for trans in all_transactions for phonepe in trans if phonepe["method"]=="phone-pay"]
# print("Total gpay transaction is ",sum(g_pay_trans))
# print("Total phonepay transaction is ",sum(phonepe_trans))
# print("Total neft transactions is ",sum(neft_trans))




#
