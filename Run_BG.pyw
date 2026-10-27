from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import socket
from Files import Write

Port = 7777
Dir = Path(__file__).resolve().parent / "Files" / "Web"

class Server_Handler(SimpleHTTPRequestHandler):
    def __init__(self, *Args, **Kwargs):
        super().__init__(*Args, directory=str(Dir), **Kwargs)

    def log_message(self, Format, *Args):
        pass

    def Send_Response(self, Status_Code, Message):
        Response_Data = Message.encode("utf-8")
        self.send_response(Status_Code)
        self.send_header("Content-Type", "text/plain; charset=UTF-8")
        self.send_header("Content-Length", str(len(Response_Data)))
        self.end_headers()
        self.wfile.write(Response_Data)

    def do_POST(self):
        if self.path not in ("/upload", "/write"):
            self.Send_Response(404, "Route Not Found")
            return

        try:
            Content_Length = int(self.headers.get("Content-Length", 0))

            if not 0 < Content_Length <= 10_000_000:
                self.Send_Response(400, "Invalid Data Size")
                return

            Data = self.rfile.read(Content_Length).decode("utf-8")

            if self.path == "/upload":
                print(Data)
                Message = "Data Received Successfully!"
            else:
                Write.Write_Text(Data)
                Message = "Write Function Executed!"

            self.Send_Response(200, Message)

        except (UnicodeDecodeError, ValueError):
            self.Send_Response(400, "Invalid Text Data")
        except Exception:
            self.Send_Response(500, "Server Error")

def Get_Network_Ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as Socket:
        try:
            Socket.connect(("192.0.2.1", 80))
            return Socket.getsockname()[0]
        except OSError:
            return "127.0.0.1"

if __name__ == "__main__":
    if not (Dir / "index.html").is_file():
        raise FileNotFoundError(f"HTML File Not Found: {Dir / 'index.html'}")

    Network_Ip = Get_Network_Ip()
    print(f"Website: http://{Network_Ip}:{Port}")

    with ThreadingHTTPServer(("0.0.0.0", Port), Server_Handler) as Server:
        try:
            Server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer Stopped.")