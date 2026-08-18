import datetime
import socket
import json
import os
from typing import Dict, Any, Optional

class SystemLogger:
    def __init__(self, log_file: str = "syslog.log"):
        self.log_file = log_file
        self.private_ip = self.get_private_ip()

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Get the local/private IP address                                ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def get_private_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            try:
                hostname = socket.gethostname()
                return socket.gethostbyname(hostname)
            except:
                return "127.0.0.1"

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Create a structured log entry                                   ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def create_log_entry(self, message: str, detail: str, status: str = "INFO") -> Dict[str, Any]:
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "ip": self.private_ip,
            "status": status,
            "message": message,
            "detail": detail
        }
    
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Write log entry to file                                         ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def write_log(self, log_entry: Dict[str, Any]):
        try:
            os.makedirs(os.path.dirname(self.log_file) or '.', exist_ok=True)
            with open(self.log_file, "a") as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            print(f"failed to write log: {e}")

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Log a success event                                             ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_success(self, message: str="OK", detail: str="The request was successful"):
        entry = self.create_success_log(message, detail)
        self.write_log(entry)
        return entry

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Log an error event                                              ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_error(self, message: str="Bad Request", detail: str="Server cannot process the request"):
        entry = self.create_error_log(message, detail)
        self.write_log(entry)
        return entry

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Log an info event                                               ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_info(self, messageL str, detail: str=""):
        entry = self.create_log_entry(message, detail, status="INFO")
        self.write_log(entry)
        return entry

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          Log a warning event                                             ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_warning(self, message: str, detail: str=""):
        entry = self.create_log_entry(message, detail, status="WARNING")
        self.write_log(entry)
        return entry

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
##              create logger instance                                          ##
##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
logger = SystemLogger()

if __name__ == "__main__":
    logger.log_success()
    logger.log_error()`
