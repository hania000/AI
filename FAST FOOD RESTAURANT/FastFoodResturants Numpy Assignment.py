#ASSIGNMENT 

import numpy as np

address,city,country,keys,latitude,longitude=np.genfromtxt('FastFoodResturants.csv', delimiter=',', usecols=(0,1,2,3,4,5), unpack=True, dtype=None,skip_header=1)
print(address)
print(city)
print(country)
print(keys)
print(latitude)
print(longitude)

#FastFoodResturants.csv - statistics operations
print("FastFoodResturants.csv mean:",np.mean(longitude))
print("FastFoodResturants.csv average:",np.average(longitude))
print("FastFoocResturants.csv std:",np.std(longitude))
print("FastFoodResturants.csv mod:",np.median(longitude))
print("FastFoodResturants.csv percentile-45:",np.percentile(longitude,45))
print("FastFoodResturants.csv min:",np.min(longitude))
print("FastFoodResturants.csv max:",np.max(longitude))

#statics price of latitude
print("FastFoodResturants.csv mean:",np.mean(latitude))
print("FastFoodResturants.csv max:",np.max(latitude))
print("FastFoodResturants.csv average:",np.average(latitude))
print("FastFoodResturants.csv std:",np.std(latitude))
print("FastFoodResturants.csv mod:",np.mod(latitude,10))
print("FastFoodResturants.csv percentile-50:",np.mod(latitude,10))
print("FastFoodResturants.csv min:",np.min(latitude))
print("FastFoodResturants.csv max:",np.max(latitude))

#maths opeartion on arrays
addition = latitude+longitude
subtraction=latitude-longitude
multiplication=latitude*longitude
division=latitude/longitude

print("FastFoodResturants.csv latitude-longitude-addition",addition)
print("FastFoodResturants.csv latitude-longitude-subtraction",subtraction)
print("FastFoodResturants.csv latittude-longitude-division",division)
print("FastFoodResturants.csv latitude-longitude-multiplication",multiplication)

#2 dimentional arrary
D2_array = np.array([latitude,longitude])
print ("FastFoodResturants latitude plus longitude - 2 dimentional arrary - " ,D2_array)

#3 dimentional array
D3_array= np.array([[longitude,latitude]])
print ("FastFoodResturants latitude plus longitude - 3 dimentional arrary - " ,D3_array)

#using np.nditer()
for item in np.nditer(D2_array):
    print(item)

#using np,ndenumerate()
for index, elem in np.ndenumerate(D2_array):
    print(index, elem) 

#common prperties of array
#ndim
print("ndim",D2_array.ndim)
#shape
print("shape",D2_array.shape)
#size
print("size",D2_array.size)
#dtype
print("dtye",D2_array.dtype)
#itemsize
print("itemsize",D2_array.itemsize)
#nbytes
print("nbytes",D2_array.nbytes)
#tranpose
print("T",D2_array.T)

#slicing array
D2_arraySlice= D2_array[1:3, 2:4]
print(D2_arraySlice)

D2_arraySlice2= D2_array[2:8, 3:5]
print(D2_arraySlice2)

#geometric operations
pricePie = (latitude/np.pi)+1
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)
print(sine_values)
print(cosine_values)
print(tangent_values)

sinh_values = np.sinh(pricePie)
print(sinh_values)
cosh_values = np.cosh(pricePie)
print(cosh_values)
tanh_values = np.tanh(pricePie)
print(tanh_values)
