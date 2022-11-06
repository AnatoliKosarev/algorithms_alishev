class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f'<w: {self.weight}, v: {self.value}>'

    def value_per_unit_of_weight(self):
        return self.value / self.weight

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value


item_1 = Item(4, 20)
item_2 = Item(3, 18)
item_3 = Item(2, 14)

items_list = [item_1, item_2, item_3]

items_list.sort(key=lambda x: x.value_per_unit_of_weight(), reverse=True)

current_item_index = 0
current_weight = 0
current_value = 0
weight_capacity = 7

while current_item_index < len(items_list) and current_weight < weight_capacity:
    current_item = items_list[current_item_index]

    # if item weight fits into knapsack - add the whole item
    if current_weight + current_item.get_weight() <= weight_capacity:
        current_weight += current_item.get_weight()
        current_value += current_item.get_value()
    # if item weight > than available space - add item fraction that fits
    else:
        current_value += (weight_capacity - current_weight) / current_item.get_weight() * current_item.get_value()
        current_weight = weight_capacity

    current_item_index += 1

print(current_value)
