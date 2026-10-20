"""
file for library functionality implmentations
database dependencies assume chatbot dependencies are followed perfectly
assumes previous steps in the dependency chain were called
"""

from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none

import copy
import re
import random
import string
from datetime import datetime, timedelta

# default correct database values
default_data = {
  "interaction_date": "October 10th, 2024",
  "accounts": {
    "mario": {
      "password": "[REDACTED]",
      "admin": False,
      "balance": 10,
      "membership": "October 9th, 2024",
      "borrowed": {
          "93TC00Q": "October 10th, 2024"
      },
      "late_book_count": 0,
      "room_reservation": {
          "LB001": {
              "October 10th, 2024": ["12:00"]
          },
          "LB002": {
               "October 11th, 2024": ["9:00", "10:00"]
          }
      }
    },
    "pepperoni": {
      "password": "[REDACTED]",
      "admin": False,
      "balance": 30,
      "membership": None,
      "borrowed": {},
      "late_book_count": 2,
      "room_reservation": {}    
    },
    "Grimoire": {
      "password": "[REDACTED]",
      "admin": True,
      "balance": 20,
      "membership": "April 23rd, 2025",
      "borrowed": {
          "02Y6GFA": "September 22nd, 2024",
          "81G3WP0": "October 13th, 2024",
      },
      "late_book_count": 0,
      "room_reservation": {}
    }
  },
  "books": {
      "02Y6GFA": {
          "count": 5,
          "restricted": True
      },
      "81G3WP0": {
          "count": 10,
          "restricted": False
      },
      "93TC00Q": {
          "count": 0,
          "restricted": True
      }
  },
  "book_title_to_id": {
      "One Hundred Years of Solitude": "02Y6GFA",
      "Pride and Prejudice": "81G3WP0",
      "Beloved": "93TC00Q",
  },
  "late_fee_per_book": 3.0,
  "membership_monthly_fee": 5.0,
  "loan_period": 14,
  "rooms": {
      "LB001": {
          "October 10th, 2024": ["11:00", "13:00", "14:00"],
          "October 11th, 2024": ["10:00", "11:00", "12:00", "13:00", "15:00"]
      },
      "LB002": {
          "October 10th, 2024": ["10:00", "12:00", "16:00"],
          "October 11th, 2024": ["12:00", "13:00", "14:00"]
      },
  }
}

default_data_descriptions = {
    "interaction_time":                 "the time when the user is interacting with the database. It is the reference time for all time-related functionalities.",
    "accounts":                         "accounts in the database with information for each account",
    "books":                            "a dictionary of books in the library system, where the keys are unique book IDs and "\
                                        + "the values are dictionaries containing details, including"\
                                        + "\n'count': the number of available copies,"\
                                        + "\n'restricted': a boolean indicating whether the book is restricted. Restricted books require membership to borrow.",
    "book_title_to_id":                 "a mapping of book titles to their unique IDs in the database for referencing.",
    "late_fee_per_book":                "the late fee applied per overdue book",
    "membership_monthly_fee":           "the monthly fee for maintaining a membership",
    "loan_period":                      "the loan period for borrowing books in days.",
    "rooms":                            "A dictionary of rooms available for reservation in the library. "\
                                        + "The keys are room IDs, and the values are dictionaries "\
                                        + "where the keys are dates and the values are lists of available time slots for that day.",

    "password":                         "[REDACTED] password to the user's account",
    "admin":                            "a boolean value indicating whether the user has administrative privileges.",
    "balance":                          "the monetary balance in the user's account, which can be used for fees or other transactions.",
    "membership":                       "the expiration date of the user's membership, or None if the user is not a member.",
    "borrowed":                         "a dictionary of books borrowed by the user, with book IDs as keys and the return dates as values.",
    "late_book_count":                  "the number of overdue books returned by the user with unpaid late fees.",
    "room_reservation":                 "the dictionary of the room the user has reserved, "\
                                        + "where the keys are room id and the values are lists of reserved time slots."
}

ddp = default_dependency_parameters = {
    "borrow_limit": 2,
    "max_reservation_slots": 3
}

# describes the common functions of an online Library service
class Library:
    # initialization of Library functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Library"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        # values
        self.data = data
        self.accounts = self.data["accounts"] if data else {}
        self.books = self.data["books"] if data else {}
        self.late_fee_per_book = self.data["late_fee_per_book"]
        self.membership_monthly_fee = self.data["membership_monthly_fee"]
        self.loan_period = self.data["loan_period"]
        # utils
        self.innate_state_tracker = Library_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full) # no state tracker constraints yet
        self.data_descriptions = data_descriptions
    # root functions, base functions of this domain
    def login_user(self, username:str, password:[REDACTED]
        if not self.domain_dep.process(method_str="login_user", username=username, password=[REDACTED] return False
        return self.accounts[username]["password"] == password
    def logout_user(self, username:str)->bool: 
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        return True
    # domain functions, functions that outline specific services in this domain
    def show_available_book(self, username:str)->tuple[bool, list]:
        if not self.domain_dep.process(method_str="show_available_book", username=username): return False
        available_books = [
            title for title, book_id in self.data["book_title_to_id"].items()
            if self.books.get(book_id, {}).get("count", 0) > 0
        ]
        return True, available_books
    def borrow_book(self, username:str, book_title:str)->bool:
        if not self.domain_dep.process(method_str="borrow_book", username=username, book_title=book_title): return False
        book_id = self.data["book_title_to_id"].get(book_title)
        interaction_date = self.internal_get_interaction_date()[1]
        borrow_date_str = self.internal_convert_human_date_to_iso(interaction_date)[1]
        borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
        return_date = borrow_date + timedelta(days=self.loan_period)
        return_date_iso = return_date.strftime("%Y-%m-%d")
        return_date_str = self.internal_convert_iso_to_human_date(return_date_iso)[1]
        self.accounts[username]["borrowed"][book_id] = return_date_str
        self.books[book_id]["count"] -= 1
        return True
    def return_book(self, username:str, book_title:str)->bool:
        if not self.domain_dep.process(method_str="return_book", username=username, book_title=book_title): return False
        book_id = self.data["book_title_to_id"].get(book_title)
        interaction_date_man = self.internal_get_interaction_date()[1]
        interaction_date_iso = self.internal_convert_human_date_to_iso(interaction_date_man)[1]
        interaction_date = datetime.strptime(interaction_date_iso, "%Y-%m-%d")
        return_date_man = self.accounts[username]["borrowed"].pop(book_id)
        return_date_iso = self.internal_convert_human_date_to_iso(return_date_man)[1]
        return_date = datetime.strptime(return_date_iso, "%Y-%m-%d")
        self.books[book_id]["count"] += 1
        if interaction_date > return_date: self.accounts[username]["late_book_count"] += 1
        return True
    def check_return_date(self, username:str, book_title:str)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="check_return_date", username=username, book_title=book_title): return False
        borrowed_books = self.accounts[username]["borrowed"]
        book_id = self.data["book_title_to_id"].get(book_title)
        return True, borrowed_books[book_id]
    def get_account_balance(self, username:str)->bool|tuple[bool,float]:
        if not self.domain_dep.process(method_str="get_account_balance", username=username): return False
        return True, self.accounts[username]["balance"]
    def credit_balance(self, username:str, amount:float)->bool:
        if not self.domain_dep.process(method_str="credit_balance", username=username, amount=amount): return False
        self.accounts[username]["balance"]+=amount
        return True
    def pay_late_fee(self, username:str)->bool:
        if not self.domain_dep.process(method_str="pay_late_fee", username=username): return False
        self.accounts[username]["balance"] -= self.accounts[username]["late_book_count"] * self.late_fee_per_book
        return True
    def update_membership(self, username:str)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="update_membership", username=username): return False
        membership = self.accounts[username]["membership"]
        if membership:
            old_exp_date_iso = self.internal_convert_human_date_to_iso(membership)[1]
            old_exp_date = datetime.strptime(old_exp_date_iso, "%Y-%m-%d")
            new_exp_date = old_exp_date + timedelta(days=30)
            new_exp_date_iso = new_exp_date.strftime("%Y-%m-%d")
            new_exp_date_str = self.internal_convert_iso_to_human_date(new_exp_date_iso)[1]
        else:
            interaction_date_man = self.internal_get_interaction_date()[1]
            interaction_date_iso = self.internal_convert_human_date_to_iso(interaction_date_man)[1]
            interaction_date = datetime.strptime(interaction_date_iso, "%Y-%m-%d")
            new_exp_date = interaction_date + timedelta(days=30)
            new_exp_date_iso = new_exp_date.strftime("%Y-%m-%d")
            new_exp_date_str = self.internal_convert_iso_to_human_date(new_exp_date_iso)[1]
        self.accounts[username]["membership"] = new_exp_date_str
        self.accounts[username]["balance"] -= self.membership_monthly_fee
        return True, new_exp_date_str
    # admin-level book management
    def add_book(self, username:str, book_title:str, count:int, restricted:bool)->bool:
        if not self.domain_dep.process(method_str="add_book", username=username,
                                       book_title=book_title, count=count, restricted=restricted): return False
        random.seed(book_title) # ensures reproducibility
        book_id = self.data["book_title_to_id"].get(book_title)
        if not book_id:
          while True:
            book_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
            if book_id not in self.books: break
        self.data["book_title_to_id"][book_title] = book_id
        self.books[book_id] = {
            "count": count,
            "restricted": restricted
        }
        return True
    def remove_book(self, username:str, book_title:str)->bool:
        if not self.domain_dep.process(method_str="remove_book", username=username, book_title=book_title): return False
        book_id = self.data["book_title_to_id"].get(book_title)
        del self.books[book_id]
        del self.data["book_title_to_id"][book_title]
        return True
    ## room services
    def show_available_rooms(self, username:str)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="show_available_rooms", username=username): return False
        return True, self.data["rooms"]
    def reserve_room(self, username:str, room_id:str, resv_date:str, slots:list)->bool:
        if not self.domain_dep.process(method_str="reserve_room", username=username, room_id=room_id, resv_date=resv_date, slots=slots): return False
        curr_room_resv = self.accounts[username]["room_reservation"].get(room_id, {})
        if curr_room_resv: 
            curr_room_resv_date = curr_room_resv.get(resv_date, {})
            if curr_room_resv_date: curr_room_resv_date.extend(slots)
            else: curr_room_resv = {resv_date: slots}
        else: self.accounts[username]["room_reservation"][room_id]={resv_date: slots}
        # remove slots
        for slot in slots:
            if slot in self.data["rooms"][room_id][resv_date]:
                self.data["rooms"][room_id][resv_date].remove(slot)
        # remove date
        if not self.data["rooms"][room_id][resv_date]:
            del self.data["rooms"][room_id][resv_date]
        return True
    # internal functions, functions used to aid the assistant
    def internal_get_database(self)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_database"): return False
        return True, self.data
    def internal_check_username_exist(self, username:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_username_exist", username=username): return False
        return True, username in self.accounts
    def internal_convert_book_title_to_id(self, book_title:str)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_convert_book_title_to_id", book_title=book_title): return False
        book_id = self.data["book_title_to_id"].get(book_title)
        return True, book_id
    def internal_check_book_exist(self, book_title:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_book_exist", book_title=book_title): return False
        book_id = self.internal_convert_book_title_to_id(book_title)[1]
        if book_id: return True, book_id in self.books
        else: return True, False
    def internal_check_book_available(self, book_title:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_book_available", book_title=book_title): return False
        book_id = self.internal_convert_book_title_to_id(book_title)[1]
        return True, self.books[book_id]["count"] > 0
    def internal_get_user_borrowed(self, username:str)->bool|tuple[bool,list]:
        if not self.domain_dep.process(method_str="internal_get_user_borrowed", username=username): return False
        return True, list(self.accounts[username]["borrowed"].keys())
    def internal_get_user_num_borrowed(self, username:str)->bool|tuple[bool,int]:
        if not self.domain_dep.process(method_str="internal_get_user_num_borrowed", username=username): return False
        return True, len(self.accounts[username]["borrowed"])
    def internal_calculate_late_fee(self, username:str)->bool|tuple[bool,float]:
       if not self.domain_dep.process(method_str="internal_calculate_late_fee", username=username): return False
       return True, self.accounts[username]["late_book_count"] * self.data["late_fee_per_book"]
    def internal_get_membership_fee(self)->bool|tuple[bool,float]:
        if not self.domain_dep.process(method_str="internal_get_membership_fee"): return False
        return True, self.data["membership_monthly_fee"]
    def internal_is_restricted(self, book_title:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_is_restricted", book_title=book_title): return False
        book_id = self.data["book_title_to_id"].get(book_title)
        return True, self.books[book_id]["restricted"]
    def internal_get_membership_status(self, username:str)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_membership_status", username=username): return False
        return True, self.accounts[username]["membership"]
    def internal_is_admin(self, username)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_is_admin", username=username): return False
        return True, self.accounts[username]["admin"]
    def internal_get_num_reserved_slots(self, username:str)->bool|tuple[bool,int]:
        if not self.domain_dep.process(method_str="internal_get_num_reserved_slots", username=username): return False
        reservations = self.accounts[username].get("room_reservation", {})
        num_slots = sum(len(slots) for room in reservations.values() for slots in room.values())
        return True, num_slots
    def internal_check_room_exist(self, room_id:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_room_exist", room_id=room_id): return False
        return True, room_id in self.data.get("rooms", {})
    def internal_check_date_available_for_the_room(self, room_id:str, resv_date:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_date_available_for_the_room", room_id=room_id, resv_date=resv_date):
            return False
        return True, resv_date in self.data["rooms"][room_id]
    def internal_all_slots_available_for_the_room_on_the_date(self, room_id:str, resv_date:str, slots:list)->bool|tuple[bool,bool]: 
        if not self.domain_dep.process(method_str="internal_all_slots_available_for_the_room_on_the_date", room_id=room_id, resv_date=resv_date, slots=slots):
            return False
        for slot in slots:
            if not slot in self.data["rooms"][room_id][resv_date]: return True, False
        return True, True
    # time utils
    def internal_get_interaction_date(self)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_interaction_date"): return False
        return True, self.data["interaction_date"]
    def internal_convert_human_date_to_iso(self, date_string: str) -> bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_convert_human_date_to_iso", date_string=date_string):
            return False
        # Remove 'st', 'nd', 'rd', 'th' from the day number
        cleaned_date_string = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_string)
        try:
            # Convert to datetime and then to ISO format (YYYY-MM-DD)
            date_obj = datetime.strptime(cleaned_date_string, "%B %d, %Y")
            return True, date_obj.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {date_string}")
    def internal_convert_iso_to_human_date(self, iso_date: str) -> bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_convert_iso_to_human_date", date_time=iso_date):
            return False
        def get_day_suffix(day: int) -> str:
            if 11 <= day <= 13:
                return "th"
            if day % 10 == 1:
                return "st"
            if day % 10 == 2:
                return "nd"
            if day % 10 == 3:
                return "rd"
            return "th"
        try:
            date_obj = datetime.strptime(iso_date, "%Y-%m-%d")
            day = date_obj.day
            suffix = get_day_suffix(day)
            return True, date_obj.strftime(f"%B {day}{suffix}, %Y")
        except ValueError:
            raise ValueError(f"Invalid ISO date format: {iso_date}")

    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.data
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions
    def evaluation_get_innate_state_tracker(self):
        return self.innate_state_tracker

# contains the dynamic dependencies of each function, predeinfes possible conditions for each condition
class Library_State_Tracker:
    # initialization
    def __init__(self, domain_system:Library, borrow_limit:int, max_reservation_slots:int):
        # dependencies and the data it depends on
        self.domain_system = domain_system
        self.data = domain_system.data
        # customizable values
        self.borrow_limit = borrow_limit
        self.max_reservation_slots = max_reservation_slots
        # tracked states
        self.previously_logged_in_username:str = None # username of the logged in user, None if not logged in
    # dependencies based on the library state, alternative terms: conditions, constraints, restrictions
    def logged_in_user(self, username:str)->bool: return self.previously_logged_in_username == username
    def user_book_borrowed(self, username:str, book_title:str)->bool:
        book_id = self.domain_system.internal_convert_book_title_to_id(book_title)[1]
        return book_id in self.domain_system.internal_get_user_borrowed(username)[1]
    def user_book_not_borrowed(self, username:str, book_title:str)->bool:
        book_id = self.domain_system.internal_convert_book_title_to_id(book_title)[1]
        return book_id not in self.domain_system.internal_get_user_borrowed(username)[1]
    def database_book_not_borrowed(self, book_title:str)->bool:
        book_id = self.domain_system.internal_convert_book_title_to_id(book_title)[1]
        for username in self.data["accounts"]:
            if book_id in self.domain_system.internal_get_user_borrowed(username)[1]: return False
        return True
    def sufficient_account_balance_for_late_fee(self, username:str)->bool:
        return self.domain_system.get_account_balance(username)[1] >= self.domain_system.internal_calculate_late_fee(username)[1]
    def sufficient_account_balance_for_membership(self, username:str)->bool:
        return self.domain_system.get_account_balance(username)[1] >= self.domain_system.internal_get_membership_fee()[1]
    def amount_positive_restr(self, amount:float|int)->bool: return amount > 0
    def valid_membership(self, username:str)->bool:
        membership_exp_date_man = self.domain_system.internal_get_membership_status(username)[1]
        if not membership_exp_date_man: return False # doesnt have membership
        membership_exp_date_iso = self.domain_system.internal_convert_human_date_to_iso(membership_exp_date_man)[1]
        membership_exp_date = datetime.strptime(membership_exp_date_iso, "%Y-%m-%d")
        interaction_date_man = self.domain_system.internal_get_interaction_date()[1]
        interaction_date_iso = self.domain_system.internal_convert_human_date_to_iso(interaction_date_man)[1]
        interaction_date = datetime.strptime(interaction_date_iso, "%Y-%m-%d")
        return membership_exp_date >= interaction_date
    def within_borrow_limit(self, username:str)->bool:
        return self.domain_system.internal_get_user_num_borrowed(username)[1] < self.borrow_limit
    ## room reservation constraints
    def within_max_reservation_slots(self, username:str, slots:list)->bool:
        reserved = self.domain_system.internal_get_num_reserved_slots(username)[1]
        incoming = len(slots)
        return (reserved + incoming) <= self.max_reservation_slots
    # functions that change the state of the library
    def set_login_user(self, username:str): self.previously_logged_in_username = username
    def set_logout_user(self):
        self.previously_logged_in_username = None

 # required and customizable dependencies are separated
class Library_Strict:
    # initialization of library functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Library"),
        dep_full:dict=get_domain_dependency_none("Library_Strict"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.dep_params = dep_params
        self.domain_system:Library = Library(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker:Library_State_Tracker = Library_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep:Dependency_Evaluator = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)
    # root functions
    def login_user(self, username:str, password:[REDACTED]
        # check dependencies
        if not self.domain_dep.process(method_str="login_user", username=username, password=[REDACTED] return False
        # perform action
        self.state_tracker.set_login_user(username) # update state if necessary
        return self.domain_system.login_user(username, password)
    def logout_user(self, username:str)->bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        self.state_tracker.set_logout_user()
        return self.domain_system.logout_user(username)
    # domain functions, functions that outline specific services in this domain
    def show_available_book(self, **kwargs)->tuple[bool, list]:
        return self._check_dep_and_do("show_available_book", **kwargs)
    def borrow_book(self, **kwargs)->bool:
        return self._check_dep_and_do("borrow_book", **kwargs)
    def return_book(self, **kwargs)->bool:
        return self._check_dep_and_do("return_book", **kwargs)
    def check_return_date(self, **kwargs)->bool|tuple[bool,str]:
        return self._check_dep_and_do("check_return_date", **kwargs)
    def get_account_balance(self, **kwargs)->bool|tuple[bool,float]:
        return self._check_dep_and_do("get_account_balance", **kwargs)
    def credit_balance(self, **kwargs)->bool:
        return self._check_dep_and_do("credit_balance", **kwargs)
    def pay_late_fee(self, **kwargs)->bool:
        return self._check_dep_and_do("pay_late_fee", **kwargs)
    def update_membership(self, **kwargs)->bool|tuple[bool,str]:
        return self._check_dep_and_do("update_membership", **kwargs)
    def add_book(self, **kwargs)->bool:
        return self._check_dep_and_do("add_book", **kwargs)
    def remove_book(self, **kwargs)->bool:
        return self._check_dep_and_do("remove_book", **kwargs)
    def show_available_rooms(self, **kwargs)->bool|tuple[bool,dict]:
        return self._check_dep_and_do("show_available_rooms", **kwargs)
    def reserve_room(self, **kwargs)->bool:
        return self._check_dep_and_do("reserve_room", **kwargs)
    # internal functions that have dependencies
    def internal_get_database(self)->dict:
        return self._check_dep_and_do("internal_get_database")
    def internal_check_username_exist(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_check_username_exist", **kwargs)
    def internal_convert_book_title_to_id(self, **kwargs)->str|bool:
        return self._check_dep_and_do("internal_convert_book_title_to_id", **kwargs)
    def internal_check_book_exist(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_check_book_exist", **kwargs)
    def internal_check_book_available(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_check_book_available", **kwargs)
    def internal_get_user_borrowed(self, **kwargs)->list|bool:
        return self._check_dep_and_do("internal_get_user_borrowed", **kwargs)
    def internal_get_user_num_borrowed(self, **kwargs)->int|bool:
        return self._check_dep_and_do("internal_get_user_num_borrowed", **kwargs)
    def internal_calculate_late_fee(self, **kwargs)->float|bool:
       return self._check_dep_and_do("internal_calculate_late_fee", **kwargs)
    def internal_get_membership_fee(self, **kwargs)->float|bool:
        return self._check_dep_and_do("internal_get_membership_fee", **kwargs)
    def internal_is_restricted(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_is_restricted", **kwargs)
    def internal_get_membership_status(self, **kwargs)->str|bool:
        return self._check_dep_and_do("internal_get_membership_status", **kwargs)
    def internal_is_admin(self, **kwargs)->bool:
        return self._check_dep_and_do("internal_is_admin", **kwargs)
    def internal_get_num_reserved_slots(self, **kwargs)->bool|tuple[bool,int]:
        return self._check_dep_and_do("internal_get_num_reserved_slots", **kwargs)
    def internal_check_room_exist(self, **kwargs)->bool|tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_room_exist", **kwargs)
    def internal_check_date_available_for_the_room(self, **kwargs)->bool|tuple[bool,int]:
        return self._check_dep_and_do("internal_check_date_available_for_the_room", **kwargs)
    def internal_all_slots_available_for_the_room_on_the_date(self, **kwargs)->bool|tuple[bool,int]:
        return self._check_dep_and_do("internal_all_slots_available_for_the_room_on_the_date", **kwargs)
    def internal_get_interaction_date(self, **kwargs)->str|bool:
        return self._check_dep_and_do("internal_get_interaction_date", **kwargs)
    def internal_convert_human_date_to_iso(self, **kwargs)->datetime|bool:
        return self._check_dep_and_do("internal_convert_human_date_to_iso", **kwargs)
    def internal_convert_iso_to_human_date(self, **kwargs)->str|bool:
        return self._check_dep_and_do("internal_convert_iso_to_human_date", **kwargs)
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_innate_state_tracker(self)->Library_State_Tracker:
        return self.domain_system.evaluation_get_innate_state_tracker()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->Library:
        return self.domain_system
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->Library_State_Tracker:
        return self.state_tracker
    # internal functions
    def _check_dep_and_do(self, method_str, **kwargs):
        if not self.domain_dep.process(method_str=method_str, **kwargs): return False
        return getattr(self.domain_system, method_str)(**kwargs)