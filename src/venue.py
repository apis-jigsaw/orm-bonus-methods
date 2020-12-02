import src
class Venue():
    __table__ = 'venues'
    attributes = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_foursquare_id(self, foursquare_id, cursor):
        foursquare_query = """SELECT * FROM venues WHERE foursquare_id = %s"""
        cursor.execute(foursquare_query, (foursquare_id,))
        record =  cursor.fetchone()
        return src.build_from_record(src.Venue, record)

    def location(self, cursor):
        location_query = """SELECT * FROM locations WHERE locations.venue_id = %s"""
        cursor.execute(location_query, (self.id,))
        record = cursor.fetchone()
        return src.build_from_record(src.Location, record)

    def categories(self, cursor):
        categories_query = """SELECT categories.* FROM venue_categories 
        JOIN categories ON venue_categories.category_id = categories.id WHERE venue_categories.venue_id = %s"""
        cursor.execute(categories_query, (self.id,))
        venue_records = cursor.fetchall()
        return src.build_from_records(src.Category, venue_records)




