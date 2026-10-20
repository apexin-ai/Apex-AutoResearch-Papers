# todo: add ages, add credit card stuff


"""
file for bank functionality implmentations
database dependencies assume chatbot dependencies are followed perfectly
assumes previous steps in the dependency chain were called
"""


from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none

import copy


# default correct database values
default_data1 = {
    "accounts": {
        "john_doe": {
            "identification": "padoesshnwojord",
            "admin_password": "[REDACTED]",
            "balance": 1000.0,
            "owed_balance": 200.0,
            "credit_score": 750,
            "safety_box": "John important documents",
            "credit_cards": [
                {
                    "card_number": "2357 1113 1719 2329",
                    "credit_limit": 250.0, 
                    "credit_balance": 0.0,
                }
            ]
            },
        "jane_doe": {
            "identification": {"drivers_license_id": "D1234567", "drivers_license_state": "CA"},
            "admin_password": "[REDACTED]",
            "balance": 500.0,
            "owed_balance": 1000.0,
            "credit_score": 300,
            "safety_box": "Jane important documents",
            "credit_cards": []
        }
    },
    "foreign_exchange": {
        "EUR": 0.93,
        "RMB": 7.12,
        "GBP": 0.77,
        "NTD": 32.08
    },
    "interaction_time": "2024-11-21T16:25:31"
}

default_data = {
    "accounts": {
        "john_doe": {
            "identification": "padoesshnwojord",
            "admin_password": "[REDACTED]",
            "balance": 1000.0,
            "owed_balance": 200.0,
            "credit_score": 750,
            "safety_box": "John important documents",
            "credit_cards": {
                "2357 1113 1719 2329": {
                    "credit_limit": 250.0, 
                    "credit_balance": 0.0,
                }
            }
        },
        "jane_doe": {
            "identification": {"drivers_license_id": "D1234567", "drivers_license_state": "CA"},
            "admin_password": "[REDACTED]",
            "balance": 500.0,
            "owed_balance": 1000.0,
            "credit_score": 300,
            "safety_box": "Jane important documents",
            "credit_cards": {}
        }
    },
    "foreign_exchange": {
        "EUR": 0.93,
        "RMB": 7.12,
        "GBP": 0.77,
        "NTD": 32.08
    },
    "interaction_time": "2024-11-21T16:25:31"
}

default_data_descriptions = {
    "accounts":         "accounts in the database with information for each account",
    "foreign_exchange": "foreign currency exchange rates available currently",
    "identification":   "the password or driver's license used to access the account",
    "admin_password":   "[REDACTED] administrative password used to access further functionalities",
    "balance":          "the current account balance, how much money, the user has",
    "owed_balance":     "the current amount the user owes the bank",
    "safety_box":       "a space for the user to store text or things",
    "credit_cards":     "dictionary of credit cards, hashed by their credit card numbers"
}

ddp = default_dependency_parameters = {
    "maximum_owed_balance": 500,
    "maximum_exchange": 3000,
    "minimum_credit_score": 600,
    "minimum_account_balance_safety_box": 300,
    "maximum_deposit": 10000
}


# describes the common functions of an online bank
class Bank:
    # initialization of bank functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Bank"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.data = data
        self.accounts = self.data["accounts"] if data else {}
        self.foreign_exchange = self.data["foreign_exchange"] if data else {}
        self.innate_state_tracker = Bank_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full) # no state tracker constraints yet
        self.data_descriptions = data_descriptions
    # root functions, base functions of this domain
    def login_user(self, username:str, identification:str|dict[str:str|int])->bool:
        if not self.domain_dep.process(method_str="login_user", username=username, identification=identification): return False
        return self.accounts[username]["identification"] == identification
    def logout_user(self, username:str)->bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        return True
    # account functions, functions that manage the account
    def open_account(self, username:str, identification:str|dict, admin_password:[REDACTED]
        if not self.domain_dep.process(method_str="open_account", 
            username=username, identification=identification, admin_password=[REDACTED] return False
        self.accounts[username] = {
            "identification": identification,
            "admin_password": [REDACTED],
            "balance": 0,
            "owed_balance": 0,
            "safety_box": "",
            "credit_cards": {}
        }
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
    def set_account_information(self, username:str, username_new:str, identification_new:str)->bool:
        if not self.domain_dep.process(method_str="set_account_information",
            username=username, username_new=username_new, identification_new=identification_new): return False
        if username != username_new: # same username, handles it accordingly
            self.accounts[username_new] = copy.deepcopy(self.accounts[username])
            del self.accounts[username]
        self.accounts[username_new]["identification"] = identification_new
        return True
    def close_account(self, username:str)->bool:
        if not self.domain_dep.process(method_str="close_account", username=username): return False
        del self.accounts[username]
        return True
    # domain functions, functions that outline specific services in this domain
    def get_account_balance(self, username:str)->tuple[bool,float]:
        if not self.domain_dep.process(method_str="get_account_balance", username=username): return False
        return True, self.accounts[username]["balance"]
    def transfer_funds(self, username:str, destination_username:str, amount:float, unit:str)->bool:
        if not self.domain_dep.process(method_str="transfer_funds",
            username=username, destination_username=destination_username, amount=amount, unit=unit): return False
        if "cent" in unit: amount /= 100
        self.accounts[username]["balance"] -= amount
        self.accounts[destination_username]["balance"] += amount
        return True
    def deposit_funds(self, username:str, amount:float, unit:str, deposit_form:str|dict)->bool:
        if not self.domain_dep.process(method_str="deposit_funds",
            username=username, amount=amount, unit=unit, deposit_form=deposit_form): return False
        self.accounts[username]["balance"] += amount if "dollar" in unit else amount / 100
        return True
    def pay_bill(self, username, amount, unit, bill_description=None, *args, **kwargs)->bool:
        if not self.domain_dep.process(method_str="pay_bill",
            username=username, amount=amount, unit=unit, bill_description=bill_description): return False
        # not set to strict, unsure if extra parameters will be passed
        self.accounts[username]["balance"] -= amount if "dollar" in unit else amount / 100
        return True
    def pay_bill_with_credit_card(self, username: str, amount: int, card_number: str) -> bool:
        if not self.domain_dep.process(method_str="pay_bill_with_credit_card", username=username, amount=amount, card_number=card_number):
            return False
        account = self.accounts.get(username)
        for card_num in account.get("credit_cards", {}):
            if card_num == card_number: account["credit_cards"][card_num]["credit_balance"] += amount  
        return True
    def apply_credit_card(self, username:str, total_assets:float, monthly_income:float) -> bool:
        if not self.domain_dep.process(method_str="apply_credit_card", username=username, total_assets=total_assets, monthly_income=monthly_income):
            return False
        new_card_number = ''.join([str(abs(hash(f"{username}{total_assets}{monthly_income}{i}")) % 10) for i in range(16)])
        new_card_number = " ".join([new_card_number[i:i+4] for i in range(4)])
        new_card_details = {
            "credit_limit": monthly_income / 4,
            "credit_balance": 0.0,
        }
        account = self.accounts.get(username, {})
        new_card_exists_already:bool = new_card_number in account["credit_cards"]
        if new_card_exists_already: account.setdefault("credit_cards", {})[new_card_number] = new_card_details
        return True
    def cancel_credit_card(self, username: str, card_number: str) -> bool:
        if not self.domain_dep.process(method_str="cancel_credit_card", username=username, card_number=card_number):
            return False
        account = self.accounts.get(username)        
        for card_num in account["credit_cards"]:
            if card_num == card_number:
                account["credit_cards"].pop(card_num, None)
                return True
        return False 
    def exchange_foreign_currency(self, amount:float, unit:str, foreign_currency_type:str)->tuple[bool,float]:
        if not self.domain_dep.process(method_str="exchange_foreign_currency",
            amount=amount, unit=unit, foreign_currency_type=foreign_currency_type): return False
        if "cent" in unit: amount /= 100
        return True, self.data["foreign_exchange"][foreign_currency_type] * amount
    def get_account_owed_balance(self, username:str)->tuple[bool,float]:
        if not self.domain_dep.process(method_str="get_account_owed_balance", username=username): return False
        return True, self.accounts[username]["owed_balance"]
    def get_loan(self, username:str, loan_amount:float)->bool:
        if not self.domain_dep.process(method_str="get_loan", username=username, loan_amount=loan_amount): return False
        self.accounts[username]["balance"] += loan_amount
        self.accounts[username]["owed_balance"] += 1.1 * loan_amount
        return True
    def pay_loan(self, username:str, pay_owed_amount_request:float)->bool:
        if not self.domain_dep.process(method_str="pay_loan",
            username=username, pay_owed_amount_request=pay_owed_amount_request): return False
        self.accounts[username]["balance"] -= pay_owed_amount_request
        self.accounts[username]["owed_balance"] -= pay_owed_amount_request
        return True
    def get_safety_box(self, username:str)->tuple[bool,str]:
        if not self.domain_dep.process(method_str="get_safety_box", username=username): return False
        return True, self.accounts[username]['safety_box']
    def set_safety_box(self, username:str, safety_box_new:str)->bool:
        if not self.domain_dep.process(method_str="set_safety_box",
            username=username, safety_box_new=safety_box_new): return False
        self.accounts[username]["safety_box"] = safety_box_new
        return True
    def get_bank_maximum_loan_amount(self, bank_total_cash:float=0)->tuple[bool,float]:
        if not self.domain_dep.process(method_str="get_bank_maximum_loan_amount",
            bank_total_cash=bank_total_cash): return False
        return True, bank_total_cash / 2
    def get_credit_cards(self, username:str) -> tuple[bool, list]:
        if not self.domain_dep.process(method_str="get_credit_cards", username=username):
            return False
        account = self.accounts.get(username)
        return True, account["credit_cards"]
    def get_credit_card_info(self, username:str, card_number:str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="get_credit_card_info", username=username, card_number = card_number):
            return False, {}
        account = self.accounts.get(username)
        for card_num in account["credit_cards"]:
            if card_num == card_number: return True, account["credit_cards"][card_number]
        return False, {}
    # internal functions, functions used to aid the assistant
    def internal_get_database(self)->tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_database"): return False
        return True, self.data
    def internal_check_username_exist(self, username:str)->tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_username_exist", username=username): return False
        return True, username in self.accounts
    def internal_check_foreign_currency_available(self, foreign_currency_type:str)->tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_foreign_currency_available",
            foreign_currency_type=foreign_currency_type): return False
        return True, foreign_currency_type in self.data["foreign_exchange"]
    def internal_get_credit_score(self, username:str) -> tuple[bool, int]:
        if not self.domain_dep.process(method_str="internal_get_credit_score", username=username): return False
        return True, self.accounts[username]["credit_score"]
    def internal_check_credit_card_exist(self, username:str, card_number:str)->tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_check_credit_card_exist", username=username, card_number=card_number):
            return False
        account = self.accounts.get(username)
        cc_number_found:bool = False
        for card_num in account["credit_cards"]:
            if not cc_number_found and card_num == card_number: cc_number_found = True
        return True, cc_number_found 
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.data
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions
    def evaluation_get_innate_state_tracker(self):
        return self.innate_state_tracker


# contains the dynamic dependencies of each function, predeinfes possible conditions for each condition
class Bank_State_Tracker:
    # initialization
    def __init__(self, domain_system:Bank, maximum_owed_balance:float, minimum_credit_score:int, minimum_account_balance_safety_box:int, maximum_deposit:int, maximum_exchange:int):
        # dependencies and the data it depends on
        self.domain_system = domain_system
        # customizable values
        self.maximum_owed_balance = maximum_owed_balance
        self.minimum_credit_score = minimum_credit_score
        self.maximum_exchange = maximum_exchange
        self.minimum_account_balance_safety_box = minimum_account_balance_safety_box
        self.maximum_deposit = maximum_deposit
        # tracked states
        self.previously_logged_in_username:str = None # username of the logged in user, None if not logged in
        self.prev_auth_admin_pass:bool = False # boolean if the current user entered in an admin password
    # dependencies based on the bank state, alternative terms: conditions, constraints, restrictions
    def logged_in_user(self, username:str)->bool: return self.previously_logged_in_username == username
    def authenticated_admin_password(self, username:str)->bool: return self.prev_auth_admin_pass
    def sufficient_account_balance(self, username:str, amount:float)->bool:
        return self.domain_system.get_account_balance(username)[1] >= amount
    def get_loan_owed_balance_restr(self, username:str)->bool:
        return self.domain_system.get_account_owed_balance(username)[1] < self.maximum_owed_balance
    def pay_loan_account_balance_restr(self, username:str)->bool:
        return self.domain_system.get_account_balance(username)[1] >= self.domain_system.get_account_owed_balance(username)[1]
    def pay_loan_amount_restr(self, username:str, pay_owed_amount_request:float)->bool:
        return self.domain_system.get_account_balance(username)[1] >= pay_owed_amount_request
    def amount_positive_restr(self, amount:float)->bool: return amount > 0
    def minimal_elgibile_credit_score(self, username: str) -> bool:
        _, credit_score = self.domain_system.internal_get_credit_score(username)
        return credit_score > self.minimum_credit_score
    def no_owed_balance(self, username: str) -> bool:
        return self.domain_system.get_account_owed_balance(username)[1] == 0
    def no_credit_card_balance(self, username: str) -> bool:
        _, credit_cards = self.domain_system.get_credit_cards(username)
        if not credit_cards: return True 
        return all(credit_cards[card_num]["credit_balance"] == 0 for card_num in credit_cards)
    def no_credit_card_balance_on_card(self, username: str, card_number: str) -> bool:
        _, card = self.domain_system.get_credit_card_info(username, card_number)
        return card["credit_balance"] == 0
    def not_over_credit_limit(self, username: str, card_number: str, amount: int) -> bool:
        _, card = self.domain_system.get_credit_card_info(username, card_number)
        avaliable_credit = card["credit_limit"] - card["credit_balance"]
        return amount <= avaliable_credit
    def safety_box_eligible(self, username: str) -> bool:
        return self.domain_system.get_account_balance(username)[1] >= self.minimum_account_balance_safety_box
    def maximum_deposit_limit(self, unit: str, amount: int) -> bool:
        if "dollar" not in unit: amount = amount / 100
        return amount <= self.maximum_deposit
    def maximum_exchange_amount(self, unit: str, amount: int) -> bool:
        if "dollar" not in unit: amount = amount / 100
        return self.maximum_exchange >= amount
    # constraints that don't do anything by themselves, but force the action to call an action beforehand
    def call_get_database(self)->bool: return True
    # functions that change the state of the bank
    def set_login_user(self, username:str): self.previously_logged_in_username = username
    def set_authenticate_admin_password(self): self.prev_auth_admin_pass = True
    def set_logout_user(self):
        self.previously_logged_in_username = None
        self.prev_auth_admin_pass = False


# required and customizable dependencies are separated
class Bank_Strict:
    # initialization of bank functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Bank"),
        dep_full:dict=get_domain_dependency_none("Bank_Strict"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.dep_params = dep_params
        self.domain_system:Bank = Bank(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker:Bank_State_Tracker = Bank_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep:Dependency_Evaluator = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)
    # root functions
    def login_user(self, username:str, identification:str|dict[str:str|int]=None)->bool:
        # check dependencies
        if not self.domain_dep.process(method_str="login_user", username=username, identification=identification): return False
        # perform action
        self.state_tracker.set_login_user(username) # update state if necessary
        return self.domain_system.login_user(username, identification)
    def logout_user(self, username:str)->bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        self.state_tracker.set_logout_user()
        return self.domain_system.logout_user(username)
    # account functions, functions that manage the account
    def open_account(self, **kwargs)->bool:
        return self._check_dep_and_do("open_account", **kwargs)
    def authenticate_admin_password(self, username:str, admin_password:[REDACTED]
        if not self.domain_dep.process(method_str="authenticate_admin_password", username=username, admin_password=[REDACTED] return False
        self.state_tracker.set_authenticate_admin_password()
        return self.domain_system.authenticate_admin_password(username, admin_password)
    def set_admin_password(self, **kwargs)->bool:
        return self._check_dep_and_do("set_admin_password", **kwargs)
    def set_account_information(self, **kwargs)->bool:
        return self._check_dep_and_do("set_account_information", **kwargs)
    def close_account(self, **kwargs)->bool:
        return self._check_dep_and_do("close_account", **kwargs)
    # domain functions, functions that outline specific services in this domain
    def get_account_balance(self, **kwargs)->tuple[bool,float]:
        return self._check_dep_and_do("get_account_balance", **kwargs)
    def transfer_funds(self, **kwargs)->bool: # transfer_funds has username, destination_username, amount, and unit
        return self._check_dep_and_do("transfer_funds", **kwargs)
    def deposit_funds(self, **kwargs)->bool:
        return self._check_dep_and_do("deposit_funds", **kwargs)
    def pay_bill(self, **kwargs)->bool:
        return self._check_dep_and_do("pay_bill", **kwargs)
    def apply_credit_card(self, **kwargs)->bool:
        return self._check_dep_and_do("apply_credit_card", **kwargs)
    def exchange_foreign_currency(self, **kwargs)->tuple[bool,float]:
        return self._check_dep_and_do("exchange_foreign_currency", **kwargs)
    def get_account_owed_balance(self, **kwargs)->tuple[bool,float]:
        return self._check_dep_and_do("get_account_owed_balance", **kwargs)
    def get_loan(self, **kwargs)->bool:
        return self._check_dep_and_do("get_loan", **kwargs)
    def pay_loan(self, **kwargs)->bool:
        return self._check_dep_and_do("pay_loan", **kwargs)
    def get_safety_box(self, **kwargs)->tuple[bool,str]:
        return self._check_dep_and_do("get_safety_box", **kwargs)
    def set_safety_box(self, **kwargs)->bool:
        return self._check_dep_and_do("set_safety_box", **kwargs)
    def get_bank_maximum_loan_amount(self, **kwargs)->tuple[bool,float]:
        return self._check_dep_and_do("get_bank_maximum_loan_amount", **kwargs)
    def get_credit_cards(self, **kwargs) -> tuple[bool, list]:
        return self._check_dep_and_do("get_credit_cards", **kwargs)
    def cancel_credit_card(self, **kwargs) -> bool:
        return self._check_dep_and_do("cancel_credit_card", **kwargs)
    def get_credit_card_info(self, **kwargs) -> bool:
        return self._check_dep_and_do("get_credit_card_info", **kwargs)
    def pay_bill_with_credit_card(self, **kwargs) -> bool:
        return self._check_dep_and_do("pay_bill_with_credit_card", **kwargs)
    # internal domain functions
    def internal_get_database(self)->tuple[bool,dict]:
        return self._check_dep_and_do("internal_get_database")
    def internal_check_username_exist(self, **kwargs)->tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_username_exist", **kwargs)
    def internal_check_foreign_currency_available(self, **kwargs)->tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_foreign_currency_available", **kwargs)
    def internal_get_credit_score(self, **kwargs)->tuple[bool,int]:
        return self._check_dep_and_do("internal_get_credit_score", **kwargs)
    def internal_check_credit_card_exist(self, **kwargs)->tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_credit_card_exist", **kwargs)
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_innate_state_tracker(self)->Bank_State_Tracker:
        return self.domain_system.evaluation_get_innate_state_tracker()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->Bank:
        return self.domain_system
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->Bank_State_Tracker:
        return self.state_tracker
    # internal functions
    def _check_dep_and_do(self, method_str, **kwargs):
        if not self.domain_dep.process(method_str=method_str, **kwargs): return False
        return getattr(self.domain_system, method_str)(**kwargs)