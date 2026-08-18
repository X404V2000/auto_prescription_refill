import datetime
import socket
import json
import os
from typing import Optional, Dict, Any
from enum import Enum

class Loglevel(Enum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARNING = "WARNING"
    SUCCESS = "SUCCESS"

class Syslogger:
    def __init__(self, log_file: str="syslog.log"):
        self.log_file = log_file
        self.private_ip = self.get_private_ip()

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def get_private_ip():
        try:
            ##connect to a public DNS server to get the local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            ##fallback method
            try:
                hostname = socket.gethostname()
                return socket.gethostbyname(hostname)
            except:
                return "127.0.0.1"      ##will change in the future

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def logStructure(self, level: Loglevel, message: str, menu_arg: Optional[int]=None, details: Optional[Dict]=None) -> Dict[str, Any]:
        return {
                "timestamp": datetime.datetime.now().isoformat(),
                "ip": self.private_ip,
                "level": level.value,
                "message": message,
                "menu_option": menu_arg,
                "details": details or {}
            }

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def write_toFilesys(self, log_entry: Dict[str, Any]):
        try:
            ##mkdir if not exist
            os.makedirs(os.path.dirname(self.log_file) or '.', exist_ok=True)       ##get back to this

            ##appand to log file
            with open(self.log_file, "a") as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            print(f"failed to write log: {e}")      ##will change in the future
       
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_success(self, message; str, menu_arg: Optional[int]=None, details: Optional[Dict]=None):
        entry = self.create_log_entry(Loglevel.Success, message, menu-arg, details)
        self.write_log(entry)
        return entry

    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_error(self, message: str, menu_arg: Optional[int]=None, details: Optional[Dict]=None):
        entry = self.create_log_entry(Loglevel.ERROR, message, menu_arg, details)
        self.write_log(entry)
        return entry
    
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_info(self, message: str, menu_arg: Optional[int] = None, details: Optional[Dict] = None):
        ##Log an info event
        entry = self.create_log_entry(Loglevel.INFO, message, menu_arg, details)
        self.write_log(entry)
        return entry
    
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def log_warning(self, message: str, menu_arg: Optional[int] = None, details: Optional[Dict] = None):
        ##Log a warning event
        entry = self.create_log_entry(Loglevel.WARNING, message, menu_arg, details)
        self.write_log(entry)
        return entry
    
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def handle_validation_error(self, menu_arg: int):
        ##Handle invalid menu input
        details = {
            "received_value": menu_arg,
            "valid_options": [1, 2, 3, 4]
        }
        self.log_error(
            f"Invalid menu option: {menu_arg}",
            menu_arg=menu_arg,
            details=details
        )
    
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def handle_successful_input(self, menu_arg: int):
        ##Handle valid menu input
        self.log_success(
            f"Valid menu selection: {menu_arg}",
            menu_arg=menu_arg
        )
    
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def handle_exception(self, exception: Exception, menu_arg: Optional[int] = None):
        ##Handle and log exceptions
        self.log_error(
            f"Exception occurred: {str(exception)}",
            menu_arg=menu_arg,
            details={"exception_type": type(exception).__name__}
        )

# Initialize global logger instance
logger = SystemLogger()

# Convenience functions for backward compatibility
def log_success(message: str, menu_arg: Optional[int] = None):
    return logger.log_success(message, menu_arg)

def log_error(message: str, menu_arg: Optional[int] = None):
    return logger.log_error(message, menu_arg)

def log_info(message: str, menu_arg: Optional[int] = None):
    return logger.log_info(message, menu_arg)

def log_warning(message: str, menu_arg: Optional[int] = None):
    return logger.log_warning(message, menu_arg)

def write_toFilesys(menu_arg: int, is_valid: bool = True):
    """Main function to log system events"""
    if is_valid:
        logger.handle_successful_input(menu_arg)
    else:
        logger.handle_validation_error(menu_arg)
