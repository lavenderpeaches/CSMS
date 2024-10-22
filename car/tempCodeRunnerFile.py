# Fetch all categories
categories = Category.objects.all()
print(categories)

# Fetch specific car by id
car = AddCar.objects.get(id=1)
print(car.carname)