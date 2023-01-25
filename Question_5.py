import math
rad_cir=30
#finding the area of circle with radius value 30
_area_of_circle_=math.pi*pow(rad_cir,2)
print("Area of circle :""{:.2f}".format(_area_of_circle_))
#finding the circumference of circle with given Radius
_circum_of_circle_=2*math.pi*rad_cir
print("circumference of circle is:""{:.2f}".format(_circum_of_circle_))
#Taking radius as user input and calculating the area
rad_cir=int(input("Enter the radius:"))
area_circle=math.pi*pow(rad_cir,2)
print("area of circle is:""{:.2f}".format(area_circle))
