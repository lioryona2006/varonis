from Person import Person
import pytest
from MagicList import MagicList


def test_magic_list_enforce_index_continuity():
    # add age value to person in index of out of range and expect to get index error.
    a = MagicList(cls_type=Person)
    with pytest.raises(IndexError):
        a[1].age = 5


def test_magic_list_support_initialized_assigned_types():
    # check if adding new person to magic list equal to person object.
    person_list = MagicList(cls_type=Person)
    person_list[0].age = 5
    assert person_list[0] == Person(age=5), 'The Magic list should support initializing assigned type'
