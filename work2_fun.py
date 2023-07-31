cook_book = {}
cook = []
with open('recipes.txt', encoding='utf-8') as f:
    data = f.read()
    
list_recipes =  data.split('\n\n')

for st in list_recipes:
    cook.append(st.split('\n'))
for srt in cook:
    srt.pop(1)    
    for i in range(1,len(srt)):
        pr = srt[i].split(' | ')
        srt[i] = {'ingredient_name': pr[0], 'quantity': pr[1], 'measure': pr[2]}

for sar in cook:
    cook_book[sar[0]] = sar[1:]

def get_shop_list_by_dishes(list, person):
    ingredients = {}
    for ls in list:
        for ingredient in cook_book.get(ls):
            x = ingredient["ingredient_name"]
            copy_ingred = ingredient.copy() 
            if x not in ingredients:                
                del copy_ingred["ingredient_name"]
                y = copy_ingred["measure"]
                copy_ingred["measure"] = y
                z = copy_ingred["quantity"]
                del copy_ingred["quantity"]                
                copy_ingred["quantity"] = int(z) * person
                ingredients[x] = copy_ingred
            else:
                ingredients[x]["quantity"] = int(ingredients[x]["quantity"]) + int(ingredient["quantity"]) * person
    return ingredients
