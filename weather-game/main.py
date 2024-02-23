import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_gray = data[data['Primary Fur Color'] == "Gray"]
total_gray = color_gray['Primary Fur Color'].count()

color_cinnamon = data[data['Primary Fur Color'] == "Cinnamon"]
total_cinnamon = color_cinnamon['Primary Fur Color'].count()

color_black = data[data['Primary Fur Color'] == "Black"]
total_black = color_black['Primary Fur Color'].count()


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [total_gray, total_cinnamon, total_black]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_marco_count.csv")
