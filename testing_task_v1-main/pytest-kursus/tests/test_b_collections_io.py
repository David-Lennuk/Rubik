import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    assert unique_sorted([3, 1, 2, 2, 3]) == [1, 2, 3]
    assert unique_sorted([]) == []
    assert unique_sorted([5, 5, 5]) == [5]
    assert unique_sorted([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert unique_sorted([10, 5, 7, 5, 1, 1]) == [1, 5, 7, 10]

def test_count_words_basic():
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

    text2 = "Tere tere Tere"
    out2 = count_words(text2)
    assert out2 == {"tere": 3}

    text3 = ""
    out3 = count_words(text3)
    assert out3 == {}

def test_merge_dicts_basic():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    assert merge_dicts(d1, d2) == {"a": 1, "b": 3, "c": 4}

    d1_empty = {}
    d2 = {"a": 1}
    assert merge_dicts(d1_empty, d2) == {"a": 1}

def test_find_max_pair_basic():
    assert find_max_pair([3, 1, 2, 2, 3]) == (3, 2)
    assert find_max_pair([5, 5, 5]) == (5, 3)
    try:
        find_max_pair([])
    except ValueError as e:
        assert str(e) == "Tühja loendi maksimum ei ole defineeritud"

def test_flatten_basic():
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[]]) == []
    assert flatten([["a"], ["b", "c"], ["d"]]) == ["a", "b", "c", "d"]

def test_read_write_file_basic():
    test_path = "test_file.txt"
    text = "Tere tulemast!"
    write_file(test_path, text)
    
    assert read_file(test_path) == text

    import os
    os.remove(test_path)

def test_safe_get_basic():
    d = {"a": 1, "b": 2}
    assert safe_get(d, "a") == 1
    assert safe_get(d, "c", 10) == 10
    assert safe_get(d, "b") == 2
    assert safe_get(d, "d", "default") == "default"

def test_top_n_basic():
    assert top_n([1, 2, 3, 4, 5], 3) == [5, 4, 3]
    assert top_n([10, 5, 20, 1], 2) == [20, 10]
    try:
        top_n([1, 2, 3], 0)
    except ValueError as e:
        assert str(e) == "n peab olema positiivne"
    try:
        top_n([1, 2, 3], 5)
    except ValueError as e:
        assert str(e) == "n ei tohi olla suurem kui loendi pikkus"

def test_chunk_list_basic():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [4, 5]]
    assert chunk_list([1, 2], 5) == [[1, 2]]
    try:
        chunk_list([1, 2, 3], 0)
    except ValueError as e:
        assert str(e) == "Suurus peab olema positiivne"
        
# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
