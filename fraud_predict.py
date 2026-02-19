import pickle
model=pickle.load(open("payments.pkl","rb"))
print("Fraud Detection Ready")
amount=float(input("Enter transaction amount:"))
old_balance=float(input("Enter old Balance:"))
new_balance=float(input("Enter new balance:"))
data=[[amount,old_balance,new_balance]]
result=model.predict(data)
if result[0]==1:
    print("Fraud transcation ")
else:
    print("Safe Transaction")
    