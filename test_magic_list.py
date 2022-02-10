import pytest

from MagicList import MagicList

from Person import Person


def test_skipping_boundary():
    # Valid Case
    # Expecting to add value successfully
    magic_list = MagicList()
    magic_list[0] = 5
    assert magic_list[0] == 5


def test_skipping_boundary_with_object():
    # Valid case
    # Magic List with object
    # Expecting to add value successfully
    magic_list_person = MagicList(Person)
    magic_list_person[0].age = 5
    assert magic_list_person[0].age == 5


@pytest.mark.parametrize("index", range(1, 11))
def test_indexes_continuity(index):
    #Expecting to raise error .
    magic_list = MagicList()
    with pytest.raises(IndexError):
        magic_list[index] = index


@pytest.mark.parametrize("index", range(1, 11))
def test_negative_indexes(index: int):
    #Expecting to raise error.
    magic_list = MagicList()
    with pytest.raises(IndexError):
        magic_list[-index] = index


def test_update_boundary():
    #Valid Case.
    #Check if update successfully
    magic_list = MagicList()
    for i in range(100):
        magic_list[i] = i
        assert list(magic_list) == list(range(i + 1))


def test_compare_magiclistofperson_with_person():
    magic_list_person = MagicList(Person)
    for i in range(10):
        person = Person()
        person.age = i
        magic_list_person[i].age = i
        assert person == magic_list_person[i]


if __name__ == '__main__':
    pytest.main()
