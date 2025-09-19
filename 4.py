user_line = input()	
user_line = user_line.lower()
#1 ==========================================================
print('1 Задание','=========================================')
line_without_space = user_line.replace(' ','')
work_list = line_without_space.split(',')
print(work_list)
#2 ==========================================================
print('2 Задание','=========================================')
line_lowercase = user_line.lower()
print(line_lowercase)
#3 ==========================================================
print('3 Задание','=========================================')
line_without_space = user_line.replace(' ','')
line_without_space_comma = line_without_space.replace(',','')
list_word = set()
for i in line_without_space_comma:
	list_word.add(i)
print(len(list_word))
#4 ==========================================================
print('4 Задание','=========================================')
line_without_space = user_line.replace(' ','')
work_list = line_without_space.split(',')
max_count_o = 0
word_max_o = ''
for i in work_list:
	if i.count('o')>max_count_o:
		max_count_o=i.count('o')
		word_max_o = i
print(word_max_o)
#5 and 6 ==========================================================
print('5 и 6 Задание','=====================================')
line_without_space = user_line.replace(' ','')
work_list = line_without_space.split(',')

dictionary = {

}
for i in work_list:
	dictionary.update({i: i.count('o')+i.count('a')+i.count('i')+i.count('e')+i.count('u')+i.count('y')})
print(dictionary)
print(max(dictionary, key = dictionary.get))
#7 ==========================================================
print('7 Задание','=========================================')
line_without_space = user_line.replace(' ','')
line_without_space_comma = line_without_space.replace(',','')
work_list = line_without_space.split(',')
average_length = len(line_without_space_comma)/len(work_list)
list_average_word = []
for i in work_list:
	if len(i)>=average_length:
		list_average_word.append(i)
print(list_average_word)
#8 ==========================================================
print('8 Задание','=========================================')
line_without_space = user_line.replace(' ','')
line_without_space_comma = line_without_space.replace(',','')
work_list = line_without_space.split(',')
tuple_list = tuple(work_list[::-1])
print(tuple_list)
#9 ==========================================================
print('9 Задание','=========================================')
line_without_space = user_line.replace(' ','')
line_without_space_comma = line_without_space.replace(',','')
work_list = line_without_space.split(',')
list_word_beggin_c_k = []
for i in work_list:
	if i[0] == 'c' or i[0] =='k':
		list_word_beggin_c_k.append(i)
if len(list_word_beggin_c_k)>0:
	print(list_word_beggin_c_k)
else:
	print('Нет таких овощей')
#10 =========================================================
print('10 Задание','========================================')
line_without_space = user_line.replace(' ','')
line_without_space_comma = line_without_space.replace(',','')
work_list = line_without_space.split(',')
user_count_letter = int(input())
word_more_letter = []
for i in work_list:
	if len(i)>user_count_letter:
		word_more_letter.append(i)
print(word_more_letter)