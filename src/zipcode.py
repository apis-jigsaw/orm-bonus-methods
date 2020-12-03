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

