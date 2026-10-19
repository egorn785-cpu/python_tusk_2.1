from data import library_archive, crew_members, ship_systems
from solution_loops import get_sciense_book, get_name_book, get_short_old_books, average_lenth, well_paid, number_of_systems, all_information_list
import solution_comprehensions as comp

def cool_print(title:str):
	print(f"\n{'-'*10} {title} {'-'*10}")

cool_print("А1 фантастика:")
for b in get_sciense_book(library_archive):
    print(b)

cool_print("А2 список названий")
for name in get_name_book(library_archive):
    print(name)

cool_print("А3 старые книги")
for name in get_short_old_books(library_archive):
    print(name)

cool_print("В1 cредний стаж")
for role, avg in average_lenth(crew_members).items():
    print(f"{role}: {avg:.2f}")

cool_print("В2 зарплата 5000+0")
for line in well_paid(crew_members):
    print(line)

cool_print("В3 число систем")
for surname, count in number_of_systems(crew_members, ship_systems).items():
    print(f"{surname}: {count}")

cool_print("В6 информация")
for emp in comp.all_information_list(crew_members, ship_systems):
    for key, value in emp.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}") # Красиво выводим премию
        else:
            print(f"  {key}: {value}")
    print("  " + "-"*20)