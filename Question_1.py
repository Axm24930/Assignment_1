import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("ages : ", ages)
#sort_age
ages.sort()
#After sorting ages
print("Ages_Sorted : ", ages)
#finding the min and max of Ages
min = min(ages)
max = max(ages)
print ("Minimum age: ",min, "and maximum age: ", max)
#Adding Min_age and Max_age
ages.append(min)
ages.append(max)
print("Ages: ",ages)
#Median of given ages
median = statistics.median(ages)
print("Median Age:", median)
#Average of ages
sum_ages = sum(ages)
leng = len(ages)
avg = sum_ages/leng
print("Average age: ",avg)
#Range of ages
range = max - min
print("Range of the ages: ",range)
