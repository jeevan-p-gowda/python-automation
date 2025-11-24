import pyotp

from src.common.log_utils import log


@log
def totp(mfa: str) -> pyotp.TOTP:
    return pyotp.TOTP(s=mfa, digits=6, digest="sha1", interval=30, name="AzureDiamond", issuer="CISCO")
