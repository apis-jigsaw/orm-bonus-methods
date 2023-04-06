import pytest
from src import State, City, Zipcode, Venue, Location, save, test_conn, test_cursor, drop_all_tables, Category, VenueCategory
from src.orm import filter_by, paginate_by

@pytest.fixture()
def build_venue_records():
    drop_all_tables(test_conn, test_cursor)
    build_venues()
    yield
    drop_all_tables(test_conn, test_cursor)

@pytest.fixture()
def build_taco_records():
    drop_all_tables(test_conn, test_cursor)
    build_taco_venues()
    yield
    drop_all_tables(test_conn, test_cursor)

def build_venues():
    venue = save(Venue(name='Los Tacos Al Pastor', price = 1, foursquare_id = '4bf58dd8d48988d151941735'), test_conn, test_cursor)
    grimaldis = save(Venue(name='Grimaldis', price = 2), test_conn, test_cursor)
    pizza = save(Category(name='Pizza'), test_conn, test_cursor)
    for i in range(1, 20):
        venue = save(Venue(name='Los Tacos Numero {i}'), test_conn, test_cursor)

def build_taco_venues():
    for i in range(1, 28):
        venue = save(Venue(name='Los Tacos Numero {i}'), test_conn, test_cursor)


def test_filter_by_filters_by_specified_attrs(build_venue_records):
    venues = filter_by(test_cursor, Venue, {'name': 'Los Tacos Al Pastor', 'price': 1})
    first_venue = venues[0]
    assert first_venue.name == "Los Tacos Al Pastor"
    assert first_venue.price == 1

    venues = filter_by(test_cursor, Venue, {'foursquare_id': '4bf58dd8d48988d151941735'})
    first_venue = venues[0]
    assert first_venue.name == "Los Tacos Al Pastor"
    assert first_venue.price == 1

def test_filter_by_returns_first_ten_records_if_no_attrs(build_venue_records):
    venues = filter_by(test_cursor, Venue)
    assert len(venues) == 10
    first_venue = venues[0]
    assert first_venue.name == "Los Tacos Al Pastor"

def test_paginate_by(build_taco_records):
    venues = paginate_by(test_cursor, Venue, page_number = 2, per_page = 10)
    
    assert len(venues) == 10
    first_venue = venues[0]
    first_venue.name = "Los Tacos Numero 11"

def test_paginate_by_changes_based_on_per_page(build_taco_records):
    venues = paginate_by(test_cursor, Venue, page_number = 2, per_page = 5)
    
    assert len(venues) == 5
    first_venue = venues[0]
    first_venue.name = "Los Tacos Numero 6"
