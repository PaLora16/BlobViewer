from app.exceptions import (
    TestApiExcpetion,
    InvalidFormatException,
    InvalidResponseException,
    NotFoundException,
)
from typing import Any


def normalize(r: Any) -> Any:
    """
    Check raw HTTP response for formal response validity
    :param r: Any - the response from the API
    :return: response payload
    """

    if r is None:
        raise TestApiExcpetion("No response from TestApi")
    try:
        # API returns no valid json format for example in case invalid article id
        # IMHO API should return responses in the same shape always
        response = r.json()
    except Exception as e:
        raise NotFoundException(f"Item not found, {r}") from e
    else:
        _status = response.get("message", "N/A")
        if _status.upper() != "OK":
            raise InvalidFormatException("Invalid response from API")
        _payload = response.get("result", "N/A")
        if _payload == "N/A":
            raise InvalidResponseException("No result key in ressponse")
        return _payload
