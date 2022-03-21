from http.server import HTTPServer, SimpleHTTPRequestHandler


PORT = 8000


if __name__ == '__main__':
    try:
        with HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        pass
