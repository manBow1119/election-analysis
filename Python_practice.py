#lists- mutable collections
counties = ["Arapahoe", "Denver", "Jefferson"]
counties
print(counties[1])
print(counties[-1])

#length
len(counties)

#appending to end
counties.append("Index 3")

print(counties[3])

#slicing
first_two = counties[0:2]
print(first_two)

last_two = counties[2:]
print(last_two)

print(type(last_two))

#insert
counties.insert(2, "Travis")
print(counties)

#remove- removes value
counties.remove("Travis")
counties

#pop- removes at index
counties.pop(-1)
counties

#mutate value at index
counties[2] = "El Paso"
counties 

#tuples-immutable collections
counties2 = ("Arapahoe", "Denver", "Jefferson")
counties2 
counties2[:2] 

#dictionaries- key:value

counties3 = {}
counties3["Arapahoe"] = 422829
counties3["Denver"] = 463353
counties3["Jefferson"] = 432438
counties3

#view object to see all keys and values
counties3.items()

#view object for keys only
counties3.keys()

#view object for values only
counties3.values()

#use get to find the value for specific key
counties3.get("Arapahoe")
#or
counties3["Arapahoe"]
#or
print(counties3.get("Arapahoe"))
#or
print(counties3["Arapahoe"])

#list of dictionaries
# list_of_dict_example = [{"key1: value1, "key2": value2}, {"key1": value3, "key2": value4}]
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

voting_data
len(voting_data)

#practice shuffling
voting_data.insert(1,{"county": "El Paso", "registered_voters": 461149})
arap = voting_data[0]
voting_data.remove(arap)
voting_data

pop = voting_data.pop(1)

voting_data.append(pop)

voting_data 

voting_data.append(arap)

voting_data

###Python conditionals practice
counties4 = ["Arapahoe", "Denver","Jefferson"]
if counties4[1]=="Denver":
    print(counties4[1])

#if-else chain
score = int(input("What is your test score?"))

if score >= 90:
    print("Your score is an A")
elif score >= 80:
    print("Your score is a B")
elif score >= 70:
    print("Your score is a C")
elif score >= 60:
    print("Your score is a D")
else: 
    print("Your score is an F")

#membership conditionals
if "El Paso" in counties4:
    print("El paso is in the list of counties")
else:
    print("El paso is not in the list of counties")

#compound comparators
if "El Paso" in counties4 and "Arapahoe" in counties4:
    print("El paso and Arapahoe is in the list of counties")
else:
    print("El paso or Arapahoe is not in the list of counties")

if "El Paso" in counties4 or "Arapahoe" in counties4:
    print("El paso or Arapahoe is in the list of counties")
else:
    print("El paso and Arapahoe is not in the list of counties")

if "El Paso"  not in counties4 and "Arapahoe" in counties4:
    print("Only Arapahoe is in the list of counties")
else:
    print("El paso and Arapahoe is not in the list of counties")

#print all keys
for key in counties3.keys():
    print(key)    

#print all values    
for voters in counties3.values():
    print(voters)

#same using key as index
for county in counties3:
    print(counties3[county])

#same using get
for county in counties3:
    print(counties3.get(county))

# list enumerated- use items()
for county, voters in counties3.items():
    print(county, voters)

for county, voters in counties3.items():
    print(county + " county has " + str(voters)+ " registered voters")

#iterate list of dictionaries
for i in range(len(voting_data)):
    print(voting_data[i])

#Use nested loop to get dictionary, then value from dictionary
for dict in voting_data:
    for value in dict.values():
        print(value)


for dict in voting_data:
    for value in dict.keys():
        print(value)


for dict in voting_data:
    print(dict["registered_voters"])

# formatted string output
for dict in voting_data:
    voters = dict["registered_voters"] 
    print(f"Registered Voters: {voters}")

#format printing dictionaries
for county, voters in counties3.items():
    print(f"{county} county has {voters} registered voters")

#formatting floats
first = 17
second = 89
print(f"first divided by second is {first/second: .3f}")
