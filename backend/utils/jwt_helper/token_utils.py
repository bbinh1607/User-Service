import jwt
from datetime import datetime, timedelta
from backend.config import ACCESS_TOKEN_EXPIRES, REFRESH_TOKEN_EXPIRES, SECRET_KEY, ALGORITHM
from backend.error.business_errors import TokenExpired, InvalidToken
from flask import g

def generate_token(user):
    now = datetime.utcnow()

    access_token_payload = {
        "sub": str(user.id),
        "role": user.role.name,
        "rank": user.role.rank,
        "type": "access",
        "iat": now,
        "exp": now + timedelta(hours=ACCESS_TOKEN_EXPIRES)
    }
    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    refresh_token_expires = now + timedelta(days=REFRESH_TOKEN_EXPIRES)
    refresh_token_payload = {
        "sub": str(user.id),
        "type": "refresh",
        "iat": now,
        "exp": refresh_token_expires
    }
    refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm=ALGORITHM)

    return access_token, refresh_token, refresh_token_expires

def decode_token(token, type=None):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if type is not None:
            if payload.get("type") != type:
                raise InvalidToken()
        return payload
    except jwt.ExpiredSignatureError:
        raise TokenExpired()
    except jwt.InvalidTokenError:
        raise InvalidToken()
    except Exception as e:
        raise InvalidToken()

def verify_token(type=None):
    try:
        payload = jwt.decode(g.token, SECRET_KEY, algorithms=[ALGORITHM])
        if not isinstance(payload, dict):
            return False
        if type is not None:
            if payload.get("type") != type:
                return False
        return True
    except Exception as e:
        return False
