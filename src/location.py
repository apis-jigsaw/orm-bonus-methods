from src import *
class Location:
    __table__ = 'locations'
    attributes = ['id', 'longitude', 'latitude', 'address', 
            'zipcode_id', 'venue_id', 'created_at']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def venue(self, cursor):
        query_str = "SELECT * FROM venues WHERE id = %s"
        cursor.execute(query_str, (self.venue_id,))
        record = cursor.fetchone()
        return build_from_record(Venue, record)

    def zipcode(self, cursor):
        query_str = "SELECT * FROM zipcodes WHERE id = %s"
        cursor.execute(query_str, (self.zipcode_id,))
        record = cursor.fetchone()
        return build_from_record(Zipcode, record)
