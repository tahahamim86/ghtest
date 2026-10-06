cars = ["Toyota", "Honda", "Ford", "BMW"]
series = ["Corolla", "Civic", "Mustang", "X5"]
#loop through both lists simultaneously using zip
for car, serie in zip(cars, series):
    print(f"{car} - {serie}")