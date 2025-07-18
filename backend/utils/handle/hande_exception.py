def handle_exceptions_class(cls):
    """
    Decorator cho class: tự động bọc tất cả method public bằng handle_exception.
    """
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, handle_exception(attr_value))
    return cls

def handle_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise e
    return wrapper



def handle_exceptions_repository_class(cls):
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith("__"):
            setattr(cls, attr_name, handle_exception_repository(attr_value))
    return cls


def handle_exception_repository(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self = args[0] 
            if hasattr(self, 'db'):
                self.db.rollback()
            raise e
    return wrapper