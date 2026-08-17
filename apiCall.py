import json

class InvalidOperationResponse:
    @staticmethod
    def InvalidResponse( code: int=400, message: str="Bad Request", detail: str="Server cannot process the request"):
        return json.dumps({
            "code": code,
            "message": message,
            "detail": detail
        })
    
    @staticmethod
    def usrDisplay(code: int, message: str, detail: str):
        print(f"Error: {code} {message}\nMessage: {detail}")

class ValidOperationResponse:
    @staticmethod
    def ValidResponse(code: int=200, message: str="OK", detail: str="The request was successful"):
        return json.dumps({
            "code": code,
            "message": message,
            "detail": detail
        })
    
    @staticmethod
    def usrDisplay(code: int, message: str, detail: str):
        print(f"Success: {code} {message}\nMessage: {detail}")

