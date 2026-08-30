import sys
from pathlib import Path


BACKEND_DIR = (
    Path(__file__).resolve().parent.parent
)

sys.path.insert(
    0,
    str(BACKEND_DIR)
)


from monitor import check_website


def test_valid_website():

    result = check_website(
        "https://example.com"
    )

    assert result["status"] == "UP"

    assert result["status_code"] is not None


def test_invalid_website():

    result = check_website(
        "https://this-websites-"
        "does-not-exist-123456.com"
    )

    assert result["status"] == "DOWN"


if __name__ == "__main__":

    test_valid_website()
    test_invalid_website()

    print(
        "All tests passed successfully."
    )
    