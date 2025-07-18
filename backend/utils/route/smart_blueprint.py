# backend/utils/route/smart_blueprint.py
from flask import Blueprint

def has_authentication_decorator(view_func):
    return getattr(view_func, "_auth_required", False)

class SmartBlueprint(Blueprint):
    def route(self, rule, **options):
        def decorator(f):
            is_protected = has_authentication_decorator(f)

            if is_protected:
                final_rule = rule
            else:
                prefix = self.url_prefix or ""
                prefix = prefix.strip("/")
                final_rule = f"/public{prefix}{rule}"

            # Đăng ký route
            super(SmartBlueprint, self).route(final_rule, **options)(f)
            return f
        return decorator
