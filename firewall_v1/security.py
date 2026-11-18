import hashlib
import secrets
import hmac


class Security:

    @staticmethod
    def hash_text(value):
        return hashlib.sha256(
            str(value).encode("utf-8")
        ).hexdigest()

    @staticmethod
    def hash_password(password, iterations=600000):
        salt = secrets.token_bytes(16)
        result = hashlib.pbkdf2_hmac(
            "sha256",
            str(password).encode("utf-8"),
            salt,
            iterations
        )
        return (
            f"pbkdf2_sha256${iterations}$"
            f"{salt.hex()}${result.hex()}"
        )

    @staticmethod
    def verify_password(password, stored):
        try:
            algorithm, iterations, salt, expected = stored.split("$")
            if algorithm != "pbkdf2_sha256":
                return False

            result = hashlib.pbkdf2_hmac(
                "sha256",
                str(password).encode("utf-8"),
                bytes.fromhex(salt),
                int(iterations)
            ).hex()

            return hmac.compare_digest(result, expected)
        except (ValueError, TypeError):
            return False
