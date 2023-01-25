#creating an empty dog dictionary
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog = {"name":"Pit bull","color":"black","breed":"Terrior4","age":4}
print("Dog_dict: ",dog)
#create a student dictionary
student = {"First_name":"ashlesh", "Last_name":"Marneni", "Gender":"male", "Age":"22",
           "Marital status":"single", "Skills":["C","DBMS","python"], "country": "United States",
           "city":"Kansas","address":"12526 Hardy Street Overland Park"}
print("Student_Details: ",student)
#length of student dictonary:
leng = len(student)
print("length of student dictonary: ",leng)
#get the values of skills and check Data Type
print("Student skills: ",student["Skills"])
print("datatype : ", type(student["Skills"]))
#modifying skills by adding one more
student["Skills"].append("R")
print("Skills: ", student["Skills"])
#getting the dictionary keys as list
print("Dictionary_Keys: ",list(student.keys()) )
#getting the dictionary values as list
print("Dictionary_Values: ",list(student.values()) )
