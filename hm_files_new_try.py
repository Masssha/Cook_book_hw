with open('recipes.txt', "rt", encoding= "utf-8") as f:
    data = f.read()
cook_book = {}
for line in data.split("\n\n"):
    dish_name = line.split("\n")[0]
    dish_food_list = []
    for food in line.split("\n")[2:]:
        ingredients = {}
        ingredients['ingredient_name'] = food.split(" | ")[0]
        ingredients['quantity'] = food.split(" | ")[1]
        ingredients['measure'] = food.split(" | ")[2]
        dish_food_list.append(ingredients)
    cook_book[dish_name] = dish_food_list


def get_shop_list_by_dishes(dishes, person_count):
    all_dish_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                all_dish_dict[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': (int(ing['quantity']) * person_count)}
        else:
            print(f'Блюда “{dish}” нет в книге рецептов')
    return all_dish_dict

get_shop_list_by_dishes(['Каша'], 2)
print(get_shop_list_by_dishes(['Омлет'], 2))



def open_file(some_files):
    all_file_dict = {}
    for some_file in some_files:
        with open(some_file, "rt", encoding= "utf-8") as f:
            count = 0
            for line in f:
                count += 1
        with open(some_file, "rt", encoding="utf-8") as f:
            text_1 = f.read()
            name = f.name
        all_file_dict[count] = name.strip(), count, str(text_1.strip().split("\n"))
    file_to_write = sorted(all_file_dict.items())
    for ind, some_file in enumerate(some_files):
        ok_list = file_to_write[ind][1]
        for ok in str(ok_list).split(','):
            result = ok.strip("""]']"[(' ']']']")""")
            with open("ok_file.txt", "at", newline="\n", encoding="utf-8") as f:
                f.writelines(result)
                print(result)


open_file(['1.txt', '2.txt', '3.txt'])