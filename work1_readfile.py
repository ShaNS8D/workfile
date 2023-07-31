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
