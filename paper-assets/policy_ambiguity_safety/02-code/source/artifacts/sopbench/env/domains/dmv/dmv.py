"""
file for dmv functionality implmentations
database dependencies assume chatbot dependencies are followed perfectly
assumes previous steps in the dependency chain were called
"""

from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none

import copy
from datetime import datetime, timedelta

# default correct database values
default_data = {
  "accounts": {
    "23_Super": {
      "identification": "jsdbvsjvb7Q3",
      "admin_password": "[REDACTED]",
      "birthday": "1990-06-15",
      "vehicles": {
        "86XY120": {
          "model": "Toyota Camry",
          "vin": "brxousayo7",
          "reg_date": "2023-01-01",
          "address": "123 Elm Street",
          "insurance_status": "valid"
        }
      },
      "address": "123 Elm Street",
      "driver_license": {
        "dl_number": "D9678420081",
        "legal_name": "Anjali",
        "exp_date": "2028-06-15",
        "address": "123 Elm Street"
      },
      "tests": {
        "knowledge": {"status": "passed", "scheduled_time": None, "attempts": 1},
        "drive": {"status": "passed", "scheduled_time": None, "attempts": 1}
      }
    },
    "frustrated_coder": {
      "identification": "xgdyfh6346pacd",
      "admin_password": "[REDACTED]",
      "birthday": "1992-03-22",
      "vehicles": {
        "0YST653": {
          "model": "Honda Civic",
          "vin": "7ha4xm4qx1",
          "reg_date": "2023-02-15",
          "address": "456 Oak Street",
          "insurance_status": "valid"
        },
        "L023012": {
          "model": "Tesla Model 3",
          "vin": "txostm4rkx",
          "reg_date": "2023-03-20",
          "address": "456 Oak Street",
          "insurance_status": "expired"
        }
      },
      "address": "456 Oak Street",
      "driver_license": {
        "dl_number": "D0886546234",
        "legal_name": "Henry Yang",
        "exp_date": "2027-03-22",
        "address": "456 Oak Street"
      },
      "tests": {
        "knowledge": {"status": "passed", "scheduled_time": None, "attempts": 1},
        "drive": {"status": "passed", "scheduled_time": None, "attempts": 1}
      }
    },
    "HIGH666": {
      "identification": "aosdvvau8e2dscsx",
      "admin_password": "[REDACTED]",
      "birthday": "2000-07-07",
      "vehicles": {},
      "address": "789 Pine Street",
      "driver_license": None,
      "tests": {
        "knowledge": {"status": "passed", "scheduled_time": None, "attempts": 1},
        "drive": {"status": "scheduled", "scheduled_time": "2024-12-10T10:30:00", "attempts": 2}
      }
    }
  },
  "test_slots": {
    "knowledge": [
      "2024-12-11T09:00:00",
      "2024-12-11T09:30:00",
      "2024-12-11T10:00:00",
      "2024-12-11T10:30:00",
      "2024-12-12T10:30:00",
      "2024-12-12T12:00:00"
    ],
    "drive": [
      "2024-12-11T14:00:00",
      "2024-12-13T14:30:00",
      "2024-12-13T15:00:00",
      "2024-12-14T14:00:00"
    ]
  },
  "interaction_time": "2024-11-21T16:25:31"
}

default_data_descriptions = {
    "accounts":                 "accounts in the database with information for each account",
    "test_slots":               "a dictionary where the keys are valid test types in the database and values are available time slots for the corresponding test type.",
    "interaction_time":         "the time when the user is interacting with the database. It is the reference time for all time-related functionalities.",
    "identification":           "the identification to the user's account",
    "admin_password":           "[REDACTED] password to enable administrative functionalities for the user's account",
    "birthday":                 "user's birthday, formatted as YYYY-MM-DD.",
    "vehicles":                 "a dictionary of the vehicles owned by the user, where each key is the plate number of the vehicle, "\
                                + "and the value is another dictionary with detailed information of the vehicle, including"\
                                + "\n'model': make and model,"\
                                + "\n'vin': Vehicle Identification Number,"\
                                + "\n'reg_date': registration date, formatted as YYYY-MM-DD,"\
                                + "\n'address':registration address of this vehicle,"
                                + "\n'insurance_status': insurance status of the vehicle, valid or expired",
    "address":                  "the address associated with the user's account",
    "driver_license":           "a dictionary containing details of the user's driver license, including "
                                 + "\n'dl_number': the driver license number,"
                                 + "\n'legal_name': the full legal name of the user (license holder),"
                                 + "\n'exp_date': the expiration date of the license, formatted as YYYY-MM-DD,"
                                 + "\n'address': the address associated with the license",
    "tests":                    "a dictionary of the user's test history, where each key is the type of test ('knowledge' or 'drive'), "
                                 + "and the value is another dictionary with details of that test, including "
                                 + "\n'status': the current status of the test ('not scheduled', 'scheduled', or 'passed'),"
                                 + "\n'scheduled_time': the scheduled time for the test, or None if not scheduled,"
                                 + "\n'attempts': the number of attempts the user has made for this test"                   
}

ddp = default_dependency_parameters = {
    "vehicle_renewal_window": 90,
    "dl_renewal_window": 180,
    "attempt_limit": 3,
    "min_age": 16,
}

# describes the common functions of an online DMV service
class DMV:
    # initialization of DMV functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("DMV"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.data = data
        self.accounts = self.data["accounts"] if data else {}
        self.test_slots = self.data["test_slots"] if data else {}
        self.interaction_time = self.data["interaction_time"]
        self.innate_state_tracker = DMV_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full) # no state tracker constraints yet
        self.data_descriptions = data_descriptions
    # root functions, base functions of this domain
    def login_user(self, username:str, identification:str|dict[str:str|int])->bool:
        if not self.domain_dep.process(method_str="login_user", username=username, identification=identification): return False
        return self.accounts[username]["identification"] == identification
    def logout_user(self, username:str)->bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        return True
    def authenticate_admin_password(self, username:str, admin_password:[REDACTED]
        if not self.domain_dep.process(method_str="authenticate_admin_password",
            username=username, admin_password=[REDACTED] return False
        return self.accounts[username]["admin_password"] == admin_password
    def set_admin_password(self, username:str, admin_password_new:str)->bool:
        if not self.domain_dep.process(method_str="set_admin_password",
            username=username, admin_password_new=admin_password_new): return False
        self.accounts[username]["admin_password"] = admin_password_new
        return True
    # domain functions, functions that outline specific services in this domain
    ## vehicle functions
    def register_vehicle(self, username:str, plate_num:str, model:str, vin:str) -> bool:
        if not self.domain_dep.process(method_str="register_vehicle",
            username=username, plate_num=plate_num, model=model, vin=vin): return False 
        reg_date = self.interaction_time.split("T")[0]
        address = self.accounts[username]["address"]
        vehicle = {
                    "model": model,
                    "vin": vin,
                    "reg_date": reg_date,
                    "address": address,
                    "insurance_status": "expired"
        }
        self.accounts[username]["vehicles"][plate_num] = vehicle
        return True
    def get_reg_status(self, username:str, plate_num:str)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="get_reg_status",
            username=username, plate_num=plate_num): return False
        vehicle = self.accounts[username]["vehicles"][plate_num]
        return True, vehicle["reg_date"] 
    def change_vehicle_address(self, username:str, plate_num:str, address_new:str)->bool:
        if not self.domain_dep.process(method_str="change_vehicle_address",
            username=username, plate_num=plate_num, address_new=address_new): return False 
        self.accounts[username]["vehicles"][plate_num]["address"] = address_new
        return True
    def validate_vehicle_insurance(self, username:str, plate_num:str)->bool:
        if not self.domain_dep.process(method_str="validate_vehicle_insurance",
            username=username, plate_num=plate_num): return False 
        self.accounts[username]["vehicles"][plate_num]["insurance_status"] = "valid"
        return True
    def renew_vehicle(self, username:str, plate_num:str)->tuple[bool,str]:
        if not self.domain_dep.process(method_str="renew_vehicle",
            username=username, plate_num=plate_num): return False 
        vehicle = self.accounts[username]["vehicles"][plate_num]
        current_renewal_date = datetime.strptime(vehicle["reg_date"], "%Y-%m-%d")
        new_renewal_date = current_renewal_date + timedelta(days=365)
        vehicle["reg_date"] = new_renewal_date.strftime("%Y-%m-%d")
        return True, vehicle["reg_date"]
    ## DL functions
    def get_dl_status(self, username: str)->tuple[bool,str]:
        if not self.domain_dep.process(method_str="get_dl_status", username=username): return False 
        exp_date = self.accounts[username]["driver_license"]["exp_date"]
        return True, exp_date
    def update_dl_legal_name(self, username:str, new_name:str)->bool:
        if not self.domain_dep.process(method_str="update_dl_legal_name", username=username, new_name=new_name): return False 
        self.accounts[username]["driver_license"]["legal_name"] = new_name
        return True
    def change_dl_address(self, username:str, address_new:str)->bool:
        if not self.domain_dep.process(method_str="change_dl_address", username=username, address_new=address_new): return False 
        self.accounts[username]["driver_license"]["address"] = address_new
        return True
    def renew_dl(self, username:str)->tuple[bool,str]:
        if not self.domain_dep.process(method_str="renew_dl", username=username): return False 
        # extends the driver’s license expiration date by five years
        acc = self.accounts[username]
        dl = acc["driver_license"]
        current_exp_date = datetime.strptime(dl["exp_date"], "%Y-%m-%d")
        new_exp_date = current_exp_date.replace(year=current_exp_date.year + 5)
        dl["exp_date"] = new_exp_date.strftime("%Y-%m-%d")
        return True, dl["exp_date"]
    ## test scheduling functions
    def show_available_test_slots(self, username:str, test_type:str)->bool|tuple[bool,list]:
        if not self.domain_dep.process(method_str="show_available_test_slots", username=username, test_type=test_type): return False
        return True, self.test_slots[test_type]
    def schedule_test(self, username:str, test_type:str, schedule_time:str)->bool:
        if not self.domain_dep.process(method_str="schedule_test", 
                username=username, test_type=test_type, schedule_time=schedule_time): return False 
        test_info = self.accounts[username]["tests"][test_type]
        test_info["status"] = "scheduled"
        test_info["scheduled_time"] = schedule_time
        test_info["attempts"] += 1
        return True
    def cancel_test(self, username:str, test_type:str)->bool:
        if not self.domain_dep.process(method_str="cancel_test", 
                username=username, test_type=test_type): return False 
        test_info = self.accounts[username]["tests"][test_type]
        test_info["status"] = "not scheduled"
        test_info["scheduled_time"] = None
        test_info["attempts"] -= 1
        return True
    def update_test_status(self, username:str, test_type:str, passed:bool, legal_name:str=None)->bool:
        if not self.domain_dep.process(method_str="update_test_status", 
                username=username, test_type=test_type, passed=passed, legal_name=legal_name): return False 
        test_info = self.accounts[username]["tests"][test_type]
        test_info["status"] = "passed" if passed else "not scheduled"
        test_info["scheduled_time"] = None
        if test_type == "drive" and passed:  # issue a driver's license
            current_time = datetime.strptime(self.interaction_time, "%Y-%m-%dT%H:%M:%S")
            acc = self.accounts[username]
            bday = datetime.strptime(acc["birthday"], "%Y-%m-%d").date()
            current_year_birthday = bday.replace(year=current_time.year)
            # exp_date is set to five years from the birthday this year
            exp_date = current_year_birthday.replace(year=current_time.year + 5)
            unique_hash = abs(hash(username)) % (10**10)
            dl_number = f"D{unique_hash:10d}"
            self.accounts[username]["driver_license"] = {
                "dl_number": dl_number,
                "legal_name": legal_name if legal_name else username,
                "exp_date": exp_date.strftime("%Y-%m-%d"),
                "address": self.accounts[username]["address"]
            }
        return True
    def transfer_title(self, username:str, target_owner:str, plate_num:str) -> bool:
        if not self.domain_dep.process(method_str="transfer_title", 
                username=username, target_owner=target_owner, plate_num=plate_num): return False 
        vehicle = self.accounts[username]["vehicles"].pop(plate_num)
        self.accounts[target_owner]["vehicles"][plate_num] = vehicle
        return True
    #----------------------------------------------------------------------------------------------------------
    # internal functions, functions used to aid the assistant
    def internal_get_database(self)->dict:
        if not self.domain_dep.process(method_str="internal_get_database"): return False
        return True, self.data
    def internal_check_username_exist(self, username:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_username_exist", username=username): return False
        return True, username in self.accounts
    def internal_get_user_birthday(self, username:str)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_user_birthday", username=username): return False
        return True, self.accounts[username]["birthday"]
        # return datetime.strptime(self.accounts[username]["birthday"], "%Y-%m-%d").date()
    def internal_has_vehicle(self, username:str, plate_num:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_has_vehicle", 
                username=username, plate_num=plate_num): return False
        return True, plate_num in self.accounts.get(username, {}).get("vehicles", {})
    def internal_vehicle_registered(self, plate_num:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_vehicle_registered", plate_num=plate_num): return False
        for username, _ in self.accounts.items():
            if self.internal_has_vehicle(username, plate_num)[1]: return True, True
        return True, False
    def internal_get_vehicle_details(self, username:str, plate_num:str)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_vehicle_details", 
                username=username, plate_num=plate_num): return False
        return True, self.accounts[username]["vehicles"][plate_num]
    def internal_has_dl(self, username:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_has_dl", username=username): return False
        return True, self.accounts.get(username, {}).get("driver_license") is not None
    def internal_get_dl_details(self, username:str)->bool|tuple[dict,bool]:
        if not self.domain_dep.process(method_str="internal_get_dl_details", username=username): return False
        return True, self.accounts[username]["driver_license"]
    def internal_valid_test_type(self, test_type:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_valid_test_type", test_type=test_type): return False
        return True, test_type in self.test_slots
    def internal_check_test_slot_available(self, test_type:str, schedule_time:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_test_slot_available", 
                test_type=test_type, schedule_time=schedule_time): return False
        return True, schedule_time in self.test_slots.get(test_type, [])
    def internal_get_test_details(self, username:str, test_type:str)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_test_details", 
                username=username, test_type=test_type): return False
        return True, self.accounts[username]["tests"][test_type]
    def internal_get_interaction_time(self)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_interaction_time"): return False
        return True, self.interaction_time
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.data
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions
    def evaluation_get_innate_state_tracker(self):
        return self.innate_state_tracker
    
# contains the dynamic dependencies of each function, predeinfes possible conditions for each condition
class DMV_State_Tracker:
    # initialization
    def __init__(self, domain_system:DMV, vehicle_renewal_window:int, dl_renewal_window:int, attempt_limit:int, min_age:int):
        # dependencies and the data it depends on
        self.domain_system = domain_system
        # customizable values
        self.vehicle_renewal_window = int(vehicle_renewal_window)
        self.dl_renewal_window = int(dl_renewal_window)
        self.attempt_limit = int(attempt_limit)
        self.min_age = int(min_age)
        # tracked states
        self.set_logged_in_usernames:set = set() # set of usernames of the logged in users
        self.prev_auth_admin_pass:bool = False # boolean if the current user entered in an admin password
    # dependencies based on the dmv state, alternative terms: conditions, constraints, restrictions
    def logged_in_user(self, username:str)->bool: return username in self.set_logged_in_usernames
    def authenticated_admin_password(self, username:str)->bool: return self.prev_auth_admin_pass
    def is_vehicle_address_different(self, username:str, plate_num:str, address_new:str)->bool:
        return self.domain_system.internal_get_vehicle_details(username, plate_num)[1]["address"] != address_new
    def valid_vehicle_insurance(self, username:str, plate_num:str)->bool:
        return self.domain_system.internal_get_vehicle_details(username, plate_num)[1]["insurance_status"] == "valid"
    def within_vehicle_renewal_period(self, username:str, plate_num:str)->bool:
        interaction_time = self.domain_system.internal_get_interaction_time()[1]
        current_date = datetime.strptime(interaction_time, "%Y-%m-%dT%H:%M:%S").date()
        reg_date = self.domain_system.internal_get_vehicle_details(username, plate_num)[1]["reg_date"]
        expiration_date = datetime.strptime(reg_date, "%Y-%m-%d").date()
        earliest_renewal_date = expiration_date - timedelta(days=self.vehicle_renewal_window)
        return earliest_renewal_date <= current_date <= expiration_date
    def is_dl_address_different(self, username:str, address_new:str)->bool:
        return self.domain_system.internal_get_dl_details(username)[1]['address'] != address_new
    def within_dl_renewal_period(self, username:str)->bool:
        interaction_time = self.domain_system.internal_get_interaction_time()[1]
        current_date = datetime.strptime(interaction_time, "%Y-%m-%dT%H:%M:%S").date()
        exp_date = self.domain_system.internal_get_dl_details(username)[1]['exp_date']
        expiration_date = datetime.strptime(exp_date, "%Y-%m-%d").date()
        earliest_renewal_date = expiration_date - timedelta(days=self.dl_renewal_window)
        return earliest_renewal_date <= current_date <= expiration_date 
    def above_minimum_age(self, username:str)->bool:
        interaction_time = self.domain_system.internal_get_interaction_time()[1]
        current_date = datetime.strptime(interaction_time, "%Y-%m-%dT%H:%M:%S")
        user_birthday_str = self.domain_system.internal_get_user_birthday(username)[1]
        user_birthday = datetime.strptime(user_birthday_str, "%Y-%m-%d")
        age = current_date.year - user_birthday.year
        if (current_date.month, current_date.day) < (user_birthday.month, user_birthday.day):
            age -= 1  # adjust if the birthday has not occurred yet this year
        return age >= self.min_age
    def test_type_is_drive(self, test_type:str)->bool:
        return test_type == "drive"
    def drive_test_ready(self, username:str)->bool:
        return ((self.domain_system.internal_get_test_details(username, "knowledge")[1]["status"] == "passed")
                and (self.domain_system.internal_get_test_details(username, "drive")[1]["status"] == "not scheduled"))
    def test_scheduled(self, username:str, test_type:str)->bool:
        return (self.domain_system.internal_get_test_details(username, test_type)[1]["status"] == "scheduled" 
                and (self.domain_system.internal_get_test_details(username, test_type)[1]["scheduled_time"] is not None))
    def within_attempt_limit(self, username:str, test_type:str)->bool:
        return self.domain_system.internal_get_test_details(username, test_type)[1]["attempts"] < self.attempt_limit
    def before_test_date(self, username:str, test_type:str)->bool:
        interaction_time = self.domain_system.internal_get_interaction_time()[1]
        current_date = datetime.strptime(interaction_time, "%Y-%m-%dT%H:%M:%S")
        scheduled_time = self.domain_system.internal_get_test_details(username, test_type)[1]["scheduled_time"]
        scheduled_date = datetime.strptime(scheduled_time, "%Y-%m-%dT%H:%M:%S")
        return current_date < scheduled_date
    # # functions that change the state of the dmv
    def add_logged_in_user(self, username:str): self.set_logged_in_usernames.add(username)
    def remove_logged_in_user(self, username:str): self.set_logged_in_usernames.remove(username)
    def set_authenticate_admin_password(self): self.prev_auth_admin_pass = True

# required and customizable dependencies are separated
class DMV_Strict:
    # initialization of dmv functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("DMV"),
        dep_full:dict=get_domain_dependency_none("DMV_Strict"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.dep_params = dep_params
        self.domain_system:DMV= DMV(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker:DMV_State_Tracker = DMV_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep:Dependency_Evaluator = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)
    # root functions
    def login_user(self, username:str, identification:str=None)->bool:
        # check dependencies
        if not self.domain_dep.process(method_str="login_user", username=username, identification=identification): return False
        # perform action
        self.state_tracker.add_logged_in_user(username) # update state if necessary
        return self.domain_system.login_user(username, identification)
    def logout_user(self, username:str)->bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        self.state_tracker.remove_logged_in_user(username)
        return self.domain_system.logout_user(username)
    # account functions, functions that manage the account
    def authenticate_admin_password(self, username:str, admin_password:[REDACTED]
        if not self.domain_dep.process(method_str="authenticate_admin_password", username=username, admin_password=[REDACTED] return False
        self.state_tracker.set_authenticate_admin_password()
        return self.domain_system.authenticate_admin_password(username, admin_password)
    def set_admin_password(self, **kwargs)->bool:
        return self._check_dep_and_do("set_admin_password", **kwargs)
    # domain functions, functions that outline specific services in this domain
    ## vehicle functions
    def register_vehicle(self, **kwargs)->bool:   
        return self._check_dep_and_do("register_vehicle", **kwargs)
    def get_reg_status(self, **kwargs)->tuple[bool,str]:
        return self._check_dep_and_do("get_reg_status", **kwargs)
    def change_vehicle_address(self, **kwargs)->bool:
        return self._check_dep_and_do("change_vehicle_address", **kwargs)
    def validate_vehicle_insurance(self, **kwargs)->bool:
        return self._check_dep_and_do("validate_vehicle_insurance", **kwargs)
    def renew_vehicle(self, **kwargs)->tuple[bool,str]:
        return self._check_dep_and_do("renew_vehicle", **kwargs)
    ## DL functions
    def get_dl_status(self, **kwargs)->tuple[bool,str]:
        return self._check_dep_and_do("get_dl_status", **kwargs)
    def update_dl_legal_name(self, **kwargs)->bool:
        return self._check_dep_and_do("update_dl_legal_name", **kwargs)
    def change_dl_address(self, **kwargs)  -> bool:
        return self._check_dep_and_do("change_dl_address", **kwargs)
    def renew_dl(self, **kwargs)->tuple[bool,str]:
        return self._check_dep_and_do("renew_dl", **kwargs)
    ## test scheduling functions
    def show_available_test_slots(self, **kwargs)->bool:
        return self._check_dep_and_do("show_available_test_slots", **kwargs)
    def schedule_test(self, **kwargs)->bool:
        return self._check_dep_and_do("schedule_test", **kwargs)
    def cancel_test(self, **kwargs)->bool:
        return self._check_dep_and_do("cancel_test", **kwargs)
    def update_test_status(self, **kwargs)->bool:
        return self._check_dep_and_do("update_test_status", **kwargs)
    def transfer_title(self, **kwargs)-> bool:
        return self._check_dep_and_do("transfer_title", **kwargs)
    # internal domain functions
    def internal_get_database(self)->dict:
        return self._check_dep_and_do("internal_get_database")
    def internal_check_username_exist(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_check_username_exist", **kwargs)
    def internal_get_user_birthday(self, **kwargs)->bool|str:
        return self._check_dep_and_do("internal_get_user_birthday", **kwargs)
    def internal_has_vehicle(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_has_vehicle", **kwargs)
    def internal_vehicle_registered(self, **kwargs)->bool|tuple[bool,bool]:
        return self._check_dep_and_do("internal_vehicle_registered", **kwargs)
    def internal_get_vehicle_details(self, **kwargs)->bool|dict:
        return self._check_dep_and_do("internal_get_vehicle_details", **kwargs)
    def internal_has_dl(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_has_dl", **kwargs)
    def internal_get_dl_details(self, **kwargs)->bool|dict:
        return self._check_dep_and_do("internal_get_dl_details", **kwargs)
    def internal_valid_test_type(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_valid_test_type", **kwargs)
    def internal_check_test_slot_available(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_check_test_slot_available", **kwargs)
    def internal_get_test_details(self, **kwargs)->bool|str:
        return self._check_dep_and_do("internal_get_test_details", **kwargs)
    def internal_get_interaction_time(self)->bool|str:
        return self._check_dep_and_do("internal_get_interaction_time")
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_innate_state_tracker(self)->DMV_State_Tracker:
        return self.domain_system.evaluation_get_innate_state_tracker()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->DMV:
        return self.domain_system
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->DMV_State_Tracker:
        return self.state_tracker
    # internal functions
    def _check_dep_and_do(self, method_str, **kwargs):
        if not self.domain_dep.process(method_str=method_str, **kwargs): return False
        return getattr(self.domain_system, method_str)(**kwargs)