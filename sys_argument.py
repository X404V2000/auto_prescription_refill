import datetime

class user:
    def __init__(self, prescription: str, serial_number: str):
        self.prescription = prescription        ##patient diagnosis
        self.serial_number = serial_number      ##number for meds corresponding diagnosis
        
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##          user interface                                                      ##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def usr_interface():
        ##argument
    def request_prescription():
        ##argument
    def receives_outstock__instock_notification():
        ##argument
    def receive_time_or_date_to_pick_up():
        ##argument
    def picks_up_prescription():
        ##argument
    def receive_request_to_contact_physician():

class pharmacist:
    def __init__(self):
        #argument
    def determine_status_of_prescription():
        ##argument
    def checks_inventory_for_refill_or_alternative():
        ##argument
    def fills_prescription():
        ##argument

class physician:
    def __init__(self):
        ##argument
    def check_patient_records():
        ##argument
    def evaluate_alternative_medication():
        ##argument
