class House():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def house_hold_type(self):
        print(f"{self.name}\n{self.area}м2\n")

    def furniture(self, bed, wardrobe, table):
        self.bed = bed
        self.wardrobe = wardrobe
        self.table = table
        self.bed_area = 4
        self.wardrobe_area = 2
        self.table_area = 1.5
        print(f"{self.bed}: {self.bed_area}m2")
        print(f"{self.wardrobe}: {self.wardrobe_area}m2")
        print(f"{self.table}: {self.table_area}m2")

    def remaining_area(self):
        print(self.area - (self.bed_area+self.wardrobe_area+self.table_area))
    
obj1 = House("Трeшка", 300)
obj1.house_hold_type()
obj1.furniture("bed", "wardrobe", "table")
obj1.remaining_area()