merget_file_list = []
with open('txt/1.txt', encoding='utf-8') as file:
    merget_file_list.append([0, '1.txt', []])
    for line in file:
        merget_file_list[-1][2].append(line.strip())  
        merget_file_list[-1][0] += 1  

with open('txt/2.txt', encoding='utf-8') as file:
    merget_file_list.append([0, '2.txt', []])
    for line in file:
        merget_file_list[-1][2].append(line.strip())  
        merget_file_list[-1][0] += 1 

with open('txt/3.txt', encoding='utf-8') as file:
    merget_file_list.append([0, '3.txt', []])
    for line in file:
        merget_file_list[-1][2].append(line.strip())  
        merget_file_list[-1][0] += 1

sort_merge = sorted(merget_file_list)

with open('merge.txt', 'w+', encoding='utf-8') as merget_file:
    for file in sort_merge:
        merget_file.write(f'{file[1]}\n')  
        merget_file.write(f'{file[0]}\n')
        count = 1
        for string in file[2]:
            merget_file.write('Строка номер  ' + str(count) + ' файла номер ' + file[1][0] + ' ' + string + '\n')
            count += 1
        merget_file.write('\n')
