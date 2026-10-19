import pytest
import solution_loops as loops
import solution_comprehensions as comp


def test_empty_collections():
	assert loops.average_lenth([]) == {}
	assert comp.average_lenth([]) == {}

	assert loops.get_sciense_book([]) == []
	assert comp.get_sciense_book([]) == []
	assert loops.well_paid([]) == []
	assert comp.well_paid([]) == []

#для проверки, что вернет, если список есть, но нет научной фантастики
def test_no_matches_filtering():
	fake_books = [("ааакппи", "пппав", 2020, 100, "роман")]
	assert loops.get_sciense_book(fake_books) == []
	assert comp.get_sciense_book(fake_books) == []

#сравниваем среднее через approx
def test_average_approx():
	test_crew = [("А", "штурман", 5, 100), ("Б", "штурман", 10, 100)]
	expected = {"штурман": 7.5}
	assert loops.average_lenth(test_crew) == pytest.approx(expected)
	assert comp.average_lenth(test_crew) == pytest.approx(expected)

#тест с посчитанным вручную ответом
def test_manual_hardcoded():
	test_crew = [("Иванов", "штурман", 5, 6000)]
	expected = ["Иванов: 6000"]
	assert loops.well_paid(test_crew) == expected
	assert comp.well_paid(test_crew) == expected