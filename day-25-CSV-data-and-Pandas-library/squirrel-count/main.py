import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census_Squirrel_Data.csv")
data_dict = data["Primary Fur Color"].value_counts().to_dict()
print(data_dict)
new_dict = {
    "Fur Color": [],
    "Count": []
}
for key in data_dict:
    new_dict["Fur Color"].append(key)
    new_dict["Count"].append(data_dict[key])

pandas.DataFrame(new_dict).to_csv("squirrel_count.csv")

