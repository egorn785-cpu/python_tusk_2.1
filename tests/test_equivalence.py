from data import library_archive, crew_members, ship_systems
import solution_loops as loops
import solution_comprehensions as comp

def test_books_equivalence():
    assert loops.get_sciense_book(library_archive) == comp.get_sciense_book(library_archive)
    assert loops.get_name_book(library_archive) == comp.get_name_book(library_archive)
    assert loops.get_short_old_books(library_archive) == comp.get_short_old_books(library_archive)

def test_crew_equivalence():
    assert loops.average_lenth(crew_members) == comp.average_lenth(crew_members)
    assert loops.well_paid(crew_members) == comp.well_paid(crew_members)
    assert loops.number_of_systems(crew_members, ship_systems) == comp.number_of_systems(crew_members, ship_systems)
    assert loops.all_information_list(crew_members, ship_systems) == comp.all_information_list(crew_members, ship_systems)