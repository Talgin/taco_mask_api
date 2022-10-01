from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette import status

X_API_KEY = APIKeyHeader(name='X-API-Key', auto_error=True)


def check_authentication_header(api_key_header: str = Security(X_API_KEY)):
    """Matches X-API-Key header with that from Database
    
    Parameters
    ----------
    api_key_header : str
        X-API-Key obtained from user

    Returns
    -------
    result : dict
        Info about the authorization
    """
    # this is where the SQL query for converting the API key into a user_id will go
    value_from_db = dict()
    if api_key_header != value_from_db:
        # if passes validation check, return user data for API Key
        # future DB query will go here
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
        )
    print(value_from_db)