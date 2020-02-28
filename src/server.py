import os, random, sys
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler as CGIHandler

def display_server_info(port):
    main_module_dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f"Server's root directory: {main_module_dirname}")
    print(f"Server's CGI directories: {CGIHandler.cgi_directories}")
    print(f"Starting HTTP Server on port: {port}")

def configure_server():
    port = 8000 + random.randint(1000,5000)
    return HTTPServer(('localhost', port), CGIHandler)

def main():
    try:
        try:
            server = configure_server()
        except Exception as e:
            print(f"Unable to start server: Exception = {e}")
            return
        try:
            display_server_info(server.server_port)
            server.serve_forever()
        except Exception as base:
            print()
            print(f"Exception: {base}\nShutting Down Server")
            server.shutdown()
    except KeyboardInterrupt:
        print("Keyboard interrupt, exiting gracefully")
if __name__ == "__main__":
    main()