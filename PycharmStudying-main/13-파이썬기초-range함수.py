menu = ["짜장면", "짬뽕", "탕수육"]
price = [5000, 6000, 12000]
for i in range(len(menu)):
    print(f"{menu[i]} : {price[i]}원")

for i,j in zip(menu, price):
    print(f"{i} : {j}원")