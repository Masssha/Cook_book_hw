# 1 задание:
cook_book = {}
ingredients_list = []
with open('test_file.py', 'rt') as f:
    # for line in f: - не поняла, как сделать цикл про всем блюдам. не понимаю, почему цикл перескакивает через строку, если писать вот так
        dish_name = f.readline().strip()
        cook_book[dish_name] = ingredients_list
        quantity = int(f.readline().strip())
        for grocery in range(quantity):
            grocery = f.readline().strip()
            ingredients = {}
            ingredients['ingredient_name'] = grocery.split(' | ')[0]
            ingredients['quantity'] = grocery.split(' | ')[1]
            ingredients['measure'] = grocery.split(' | ')[2]
            ingredients_list.append(ingredients)

print(f"cook_book = {cook_book}")

# 2 задание:
def get_shop_list_by_dishes(dishes, person_count):
    all_dish_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                all_dish_dict[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': (int(ing['quantity']) * person_count)}
        else:
            print(f'Блюда “{dish}” нет в книге рецептов')
    return all_dish_dict

print(get_shop_list_by_dishes(['Scrambled eggs'], 2))

# третью пока не понимаю вообще, как начинать делать, хех...

