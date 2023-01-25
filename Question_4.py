it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Findthe length of the set it_companies
print("Length of it_companies:",len(it_companies))
#Add'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to it_companies
multiple_it=['T.C.S','cognizant','Cisco','Infosys']
it_companies.update(multiple_it)
print(" it_companies list",it_companies)
#Removing one of the companies
it_companies.remove('Cisco')
print(it_companies)
#Join A and B
print("Union of A and B:",A.union(B))
# A intersection B
print("Intersection of A and B",A.intersection(B))
#Is A subset of B
print("Checkinf If A is Subset of B:",A.issubset(B))
#Are A and B disjoint sets
print("Checking If A and B are Disjoints:",A.isdisjoint(B))
#Join A and B with Both
print("join A with B ",A.union(B))
print("join B with A",B.union(A))
# symmetric difference between A and B
print("symmetric difference ",A.symmetric_difference(B))
#Delete the sets completely
A.clear()
B.clear()
print(A)
print(B)
#Converting the ages to a set and compare the length of the list and the set
print("length of  list :",len(age))
print("Length of  set is:", len(set(age)))
if(len(age)>len(set(age))):
    print("The length of List is Greater")
else:
    print("The length of Age is Greater")
