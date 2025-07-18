# backend/utils/route_helper.py
import inspect
from functools import wraps

def has_authentication_decorator(func):
    return hasattr(func, "_auth_required")

def auto_route(blueprint, path, methods=["GET"]):
    def decorator(func):
        is_protected = has_authentication_decorator(func)
        final_path = path if is_protected else "/public" + path
        blueprint.route(final_path, methods=methods)(func)
        return func
    return decorator
