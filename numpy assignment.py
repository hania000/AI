import numpy as np

brokered_by , price,acre_lot,city,house_size =np.genfromtxt('RealEstate-USA1.csv',delimiter=',',usecols=(0,4,5,8,9),unpack=True,dtype=None,skip_header=1)

print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

#RealEstate-USA1.csv - statistics operations
print("RealEstate-USA.csv mean:",np.mean(price))
print("RealEstate-USA.csv average:",np.average(price))
print("RealEstate-USA.csv std:",np.std(price))
print("RealEstate-USA.csv mod:",np.median(price))
print("RealEstate-USV.csv percentile-50:",np.percentile(price,50))
print("Realestate-USA.csv min:",np.min(price))
print("RealEstate-USA.csv max:",np.max(price))

#statics price on house_size
print("RealEstate-USA.csv mean:",np.mean(house_size))
print("RealEstate-USA.csv average:",np.average(house_size))
print("RealEstate-USA.csv std:",np.std(house_size))
print("RealEstate-USA.csv mod:",np.mod(house_size))
print("RealEstate-USA.csv percentile-50:",np.mod(house_size,50))
print("RealEstate-USA.csv min:",np.min(house_size))
print("RealEstate-USA.csv max:",np.max(house_size))

#maths opeartion on arrays
addition = price+house_size
subtraction=price-house_size
multiplication=price*house_size
division=price/house_size

print("RealEstate-USA.csv price-house_size-addition",addition)
print("RealEstate-USA.csv price-house_size-subtraction",subtraction)
print("RealEstate-USA.csv price-house_size-division",division)
print("RealEstate-USA.csv price-house_size-multiplication",multiplication)
