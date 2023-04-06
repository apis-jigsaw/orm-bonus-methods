import pytest
from src import State, City, Zipcode, Venue, Location, save, test_conn, test_cursor, drop_all_tables, Category, VenueCategory
from src.query_builder import has_one_builder, has_many_builder
def test_has_one_builder():
    query_str = has_one_builder(State)
    assert query_str == "SELECT states.* FROM states WHERE id = %s"

    query_str = has_one_builder(City)
    assert query_str == "SELECT cities.* FROM cities WHERE id = %s"


def test_has_many_builder():
    # zipcode.locations() query
    query_str = has_many_builder(Zipcode, Location)
    assert query_str == "SELECT locations.* FROM locations WHERE zipcode_id = %s"
    #  state.cities() query
    # query_str = has_many_builder(State, City)
    # assert query_str == "SELECT cities.* FROM cities WHERE state_id = %s"

    