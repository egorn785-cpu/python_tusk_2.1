
def get_sciense_book(books: list[tuple])->list[tuple]:
	result=[]
	for book in books:
		if book[-1] == "Научная фантастика":
			result.append(book)
	return result

def get_name_book(books: list[tuple])->list[str]:
	result=[]
	for book in books:
		result.append(book[0])
	return result

def get_short_old_books(books: list[tuple])->list[str]:
	result=[]
	for book in books:
		if book[2]<= 1950 and book[3]<= 300:
			result.append(book[0])
	return result

def average_lenth(crew: list[tuple])->dict:
	temp = {}
	result={}
	for p in crew:
		role=p[1]
		exp=p[2]
		if role not in temp:
			temp[role]=[]
		temp[role].append(exp)
	for role in temp:
		result[role]=sum(temp[role])/len(temp[role])
	return result

def well_paid(crew: list[tuple])->list[str]:
	result=[]
	for p in crew:
		if p[3]>5000 and p[2]< 10:
			result.append(f"{p[0]}: {p[-1]}")
	return result

def number_of_systems(crew: list[tuple], system: dict)->dict:
	result={}
	for p in crew:
		name = p[0]
		count=0
		for workers in system.values():
			if name in workers:
				count+=1
		result[name]=count
	return result

def all_information_list(crew: list[tuple], system: dict)->list[dict]:
	result=[]
	for p in crew:
		count=sum(1 for workers in system.values() if p[0] in workers)
		bonus= p[3]*0.15 if p[2]>5 else p[3]*0.10
		worker_dict={ "name": p[0], "role": p[1], "exp": p[2], "paid": p[3], "systems": count, "bonus": bonus}
		result.append(worker_dict)
	return result