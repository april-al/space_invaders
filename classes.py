# class House():
#     def __init__(self, st, n):
#         self.street = st
#         self.number = n
#         self.age = 0
#
#     def __str__(self):
#         return "House: " + self.street + " " + self.number
#
#     def build(self):
#         print("House on the " + self.street + " № " + self.number)
#
#     def age_of_house(self, year):
#         self.age += year
#
#
# class ProspectHouse(House):
#     def __init__(self, prospect, number):
#         super().__init__(self, number)
#         self.prospect = prospect
#
#
# PrHouse = ProspectHouse("Мира", "777")
# print(PrHouse.prospect)
#
# # h1 = House("Spring str.", "45")
# # h2 = House("April str.", "85")
# # h1.build()
# # h2.age_of_house(1934)
# #
# # print(h2.age)
# # print(h1.street)
# # print(h2.number)
