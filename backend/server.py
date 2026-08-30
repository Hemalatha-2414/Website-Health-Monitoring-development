import json
from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer
)

from database import (
    initialize_database,
    add_website,
    get_websites,
    save_monitoring_result,
    get_latest_result
    create_user
)

from monitor import check_website


HOST = "localhost"
PORT = 8000


class WebsiteMonitorHandler(
    BaseHTTPRequestHandler
):

    def send_json_response(
        self,
        data,
        status_code=200
    ):

        response = json.dumps(data).encode(
            "utf-8"
        )

        self.send_response(status_code)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.end_headers()

        self.wfile.write(response)


    def do_GET(self):

        if self.path == "/api/websites":

            websites = get_websites()

            for website in websites:

                latest_result = get_latest_result(
                    website["id"]
                )

                website["latest_result"] = (
                    latest_result
                )

            self.send_json_response(websites)

        else:

            self.send_json_response(
                {
                    "error": "Route not found"
                },
                404
            )

    def do_OPTIONS(self):
        self.send_response(200)

        self.send_header(
            "Access-Control-Allow-Origin",
        "*"
        )

        self.send_header(
            "Access-Control-Allow-Methods",
        "GET, POST, OPTIONS"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
        "Content-Type"
        )

        self.end_headers()


    

    def do_POST(self):
        if self.path == "/api/signup":

    content_length = int(
        self.headers.get(
            "Content-Length",
            0
        )
    )

    body = self.rfile.read(
        content_length
    )

    try:

        data = json.loads(
            body.decode("utf-8")
        )

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:

            self.send_json_response(
                {
                    "error": "All fields are required"
                },
                400
            )

            return

        user = create_user(
            name,
            email,
            password
        )

        if user is None:

            self.send_json_response(
                {
                    "error": "Email already registered"
                },
                409
            )

            return

        self.send_json_response(
            {
                "message": "Account created successfully",
                "user": user
            },
            201
        )

    except json.JSONDecodeError:

        self.send_json_response(
            {
                "error": "Invalid JSON"
            },
            400
        )

elif self.path == "/api/websites":

        if self.path == "/api/websites":

            content_length = int(
                self.headers.get(
                    "Content-Length",
                    0
                )
            )

            body = self.rfile.read(
                content_length
            )

            try:

                data = json.loads(
                    body.decode("utf-8")
                )

                url = data.get("url")

                if not url:

                    self.send_json_response(
                        {
                            "error": (
                                "Website URL is required"
                            )
                        },
                        400
                    )

                    return

                website = add_website(url)

                if website is None:

                    self.send_json_response(
                        {
                            "error": (
                                "Website already exists"
                            )
                        },
                        409
                    )

                    return

                self.send_json_response(
                    website,
                    201
                )

            except json.JSONDecodeError:

                self.send_json_response(
                    {
                        "error": "Invalid JSON"
                    },
                    400
                )


        elif self.path.startswith(
            "/api/check/"
        ):

            try:

                website_id = int(
                    self.path.split("/")[-1]
                )

                websites = get_websites()

                website = next(
                    (
                        item
                        for item in websites
                        if item["id"] == website_id
                    ),
                    None
                )

                if website is None:

                    self.send_json_response(
                        {
                            "error": (
                                "Website not found"
                            )
                        },
                        404
                    )

                    return

                result = check_website(
                    website["url"]
                )

                save_monitoring_result(
                    website_id,
                    result["status"],
                    result["status_code"],
                    result["response_time"]
                )

                self.send_json_response(
                    result
                )

            except ValueError:

                self.send_json_response(
                    {
                        "error": "Invalid website ID"
                    },
                    400
                )

        else:

            self.send_json_response(
                {
                    "error": "Route not found"
                },
                404
            )


def run_server():

    initialize_database()

    server = HTTPServer(
        (HOST, PORT),
        WebsiteMonitorHandler
    )

    print(
        f"Server running at "
        f"http://{HOST}:{PORT}"
    )

    server.serve_forever()


if __name__ == "__main__":
    run_server()