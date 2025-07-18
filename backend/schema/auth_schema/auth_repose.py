from dataclasses import dataclass

@dataclass
class AuthResponse:
    access_token: str
    refresh_token: str