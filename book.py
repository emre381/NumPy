import numpy as np 
# book prices 
book_prices = np.array([25,45,20,35,50,40,30])

#  satın alınan kitap adetleri 

num_of_sales=np.array([100,150,200,120,130,80,110])

# book category
category=np.array(["Novel","Science","Kids","History","Novel","Science","Kids"])

# total_sales = book_prices*num_of_sales

# print("Total :",category ,'\n' , total_sales)
# avarage_price=np.mean(book_prices)
# max_price=np.max(book_prices)
# min_price=np.min(book_prices)
# print("avarage price ",avarage_price)
# print("maximum price ",max_price)
# print("minimum price ",min_price)
# novels=book_prices[category=="Novel"]
# print("Novel prices : ",novels)  #Novel price
# novel_sales=  num_of_sales[category=="Novel"]
# print("Novel sales : ",novel_sales) #Novel sales
# total_novel_sales=np.sum(novels*novel_sales)
# print("Total Novel sales : ",total_novel_sales," TL") #Total Novel sales

data=np.array([book_prices,num_of_sales])
data_reshaped= np.reshape(data,(2,7))
print(data_reshaped)