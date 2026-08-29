import time
import urllib.request
import urllib.error


def check_website(url):
    """Check the health of a website."""

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    start_time = time.perf_counter()

    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "WebsiteHealthMonitor/1.0"
            }
        )

        with urllib.request.urlopen(
            request,
            timeout=10
        ) as response:

            response_time = (
                time.perf_counter() - start_time
            ) * 1000

            return {
                "url": url,
                "status": "UP",
                "status_code": response.status,
                "response_time": round(
                    response_time,
                    2
                )
            }

    except urllib.error.HTTPError as error:

        response_time = (
            time.perf_counter() - start_time
        ) * 1000

        return {
            "url": url,
            "status": "DOWN",
            "status_code": error.code,
            "response_time": round(
                response_time,
                2
            )
        }

    except (
        urllib.error.URLError,
        TimeoutError,
        ValueError
    ) as error:

        response_time = (
            time.perf_counter() - start_time
        ) * 1000

        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "response_time": round(
                response_time,
                2
            ),
            "error": str(error)
        }


if __name__ == "__main__":

    website_url = input(
        "Enter website URL: "
    )

    result = check_website(website_url)

    print("\nMonitoring Result:")
    print(result)