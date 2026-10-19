def get_sciense_book(books: list[tuple])->list[tuple]:
	result=[]
	result =[book for book in books if book[-1]=="Научная фантастика"]
	return result

def get_name_book(books: list[tuple])->list[str]:
	result=[]
	result=[book[0] for book in books ]
	return result

def get_short_old_books(books: list[tuple])->list[str]:
	result=[]
	result=[book[0] for book in books if book[2]<=1950 and book[3]<= 300]
	return result

def average_lenth(crew: list[tuple])->dict:
	result=dict()
	result={role: sum(p[2] for p in crew if p[1]==role)/len([p for p in crew if p[1]==role]) for role in set(p[1] for p in crew)}
	return result

def well_paid(crew: list[tuple])->list[str]:
	result=list()
	result=[f"{p[0]}: {p[-1]}" for p in crew if p[3]>5000 and p[2]<10]
	return result

def number_of_systems(crew: list[tuple], system: dict)->dict:
	result=dict()
	result = {p[0]: sum(1 for workers in system.values() if p[0] in workers) for p in crew}
	return result

def all_information_list(crew: list[tuple], system: dict)->list[dict]:
	result=list()
	result = [
		{
			"name": p[0],
			"role": p[1],
			"exp": p[2],
			"paid": p[3],
			"systems": sum(1 for workers in system.values() if p[0] in workers),
			"bonus": p[3] * (0.15 if p[2] > 5 else 0.10)
		}
		for p in crew
	]
	return result