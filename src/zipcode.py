import src
class Zipcode:
    __table__ = 'zipcodes'
    attributes = ['id', 'code', 'city_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def locations(self, cursor):
        query_str = "SELECT locations.* FROM locations WHERE zipcode_id = %s"
        cursor.execute(query_str, (self.id,))
        records = cursor.fetchall()
        return src.build_from_records(src.Location, records)

    def city(self, cursor):
        query_str = "SELECT cities.* FROM cities WHERE id = %s"
        cursor.execute(query_str, (self.city_id,))
        record = cursor.fetchone()
        return src.build_from_record(src.City, record)


