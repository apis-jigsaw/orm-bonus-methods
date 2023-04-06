def has_one_builder(cls):
    return f"SELECT {cls.__table__}.* FROM {cls.__table__} WHERE id = %s"

def has_many_builder(src_cls, has_many_cls):
    src_name = src_cls.__name__.lower()
    has_many_table = has_many_cls.__table__
    return f"SELECT {has_many_table}.* FROM {has_many_table} WHERE {src_name}_id = %s"