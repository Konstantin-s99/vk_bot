import sqlite3

def doc(nume):
	curs.execute("SELECT text FROM docs WHERE name='"+nume+"'")
	nume=str(curs.fetchone())
	nume=nume[2:-3]
	return nume	
def cou(nume):
	nume=str(nume)
	curs.execute("SELECT descr FROM courses WHERE id="+nume+"")
	nume=str(curs.fetchone())
	nume=nume[2:-3]
	return nume
	
while True:
	conn = sqlite3.connect('db.sqlite')
	curs=conn.cursor()
	
	print("Редактор SQL by Hitreno")
	print(" ")
	print("Выберите файл:")
	print("(1)Список направлений")
	print("(2)Начало подачи док-ов")
	print("(3)Конец подачи док-ов")
	print("(4)Очное зачисление")
	print("(5)Заочное зачисление")
	print("(6)Платное поступление")
	print("(7)ФВО и УВЦ")
	print("(8)Зачисление ст-ов 1 курса")
	print("(9)Льготники")
	print("(10)Нельготники")
	print("(11)Общежитие не предост.")
	print("(12)Адреса общежитий")
	print("")
	print("Направления:")
	print("")
	print("(13)Информатика и выч. техника")
	print("(14)Прикладная иформатика")
	print("(15)Программная инженерия")
	print("(16)Информационная безопасность")
	print("(17)Радиотехника")
	print("(18)Инфокоммун. техн")
	print("(19)Констр. и тех. электр.")
	print("(20)Упр. в техн. системах")
	print("(21)Полиг. и упак. технологии")
	print("(22)Техносферная безопасность")
	print("(23)ИБ телекомуниц. систем")
	print("(24)Информ.-аналит. системы безоп.")
	print("(25)Радиоэлектр. системы и комплексы")
	print("(26)Пожарная безопасность")
	print(" ")
	try:
		inp=int(input(">>>"))
	except ValueError:
		print("Только Числа!")
		break
	if inp==  1:
		inp=("all_d" )
		old=doc(inp)
	elif inp==  2:
		inp=("str_d"  )
		old=doc(inp)
	elif inp==  3:
		inp=("fin_d")
		old=doc(inp)
	elif inp== 4 :
		inp=("ochno")
		old=doc(  inp)
	elif inp==  5:
		inp=("zaochno")
		old=doc(inp  )
	elif inp== 6 :
		inp=("pay")
		old=doc( inp )
	elif inp== 7 :
		inp=("mlt_dep")
		old=doc(inp  )
	elif inp== 8 :
		inp=("l1")
		old=doc(  inp)
	elif inp== 9 :
		inp=("l2")
		old=doc(  inp)
	elif inp== 10 :
		inp=("l3")
		old=doc( inp )
	elif inp== 11 :
		inp=("l4")
		old=doc( inp )
	elif inp== 12 :
		inp=("l5")
		old=doc( inp )
	elif inp>12 and inp<27:
		inp=inp-12
		old=cou(inp)
	else:
		print("Принимаются только целые числа от 1 до 26")
		break
	print("")
	print("Старый текст:")
	print("")
	print(old)
	print("")
	print("Для сохранения нажмите Enter. Для сноса строки \\n БЕЗ пробелов. Для выхода без сохранения Ctrl+C")
	print("Новый текст:")
	new=input(">>>")
	print("")
	if type(inp)==int:
		inp=str(inp)
		curs.execute("UPDATE courses SET descr='"+new+"' WHERE id="+inp)
		conn.commit()
		print("Новый текст успешно сохранён")
	else:
		inp=str(inp)
		curs.execute("UPDATE docs SET text='"+new+"' WHERE name='"+inp+"'")
		conn.commit()
		print("Новый текст успешно сохранён")
	print("Хотите продолжить? да/нет")
	sogl=input(">>>")
	if sogl=="да":
		continue
	elif sogl=="нет":
		print("Всего хорошего!")
		break
	else:
		print("Неверный ввод")
		break
conn.close()