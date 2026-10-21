# todo -> move policy active back into the statetracker, do not have get_policy_details depend on policy active. Move internal_coupon_not_already_used to statetracker, have a coupon_used function, regenerate all, fix internal functions, return both.

"""
file for healthcare functionality implmentations
database dependencies assume chatbot dependencies are followed perfectly
assumes previous stpes in the dependency chain were called
"""

from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none

import copy
from datetime import datetime, timedelta


default_data = {
    "accounts": {
        "Henry Smith": {
            "identification": "sdfojngsmnlvx",
            "policy_number": "102938412808014",
            "policy": {
                "details": {
                    "type": "Health",
                    "coverage_amount": 10000,
                    "enrollment_date": "2023-05-10",
                    "authorized_providers": ["mayo_clinic_rochester", "cleveland_clinic_ohio"],
                    "annual_income": 1000000,
                },
                "claims": [
                    {
                        "claim_id": "CLM-001",
                        "amount": 500,
                        "status": "approved",
                        "description": "General checkup",
                        "claim_date": "2024-06-15"
                    },
                    {
                        "claim_id": "CLM-002",
                        "amount": 1200,
                        "status": "pending",
                        "description": "Specialist consultation",
                        "claim_date": "2024-12-01"
                    }
                ],
            },
            "scheduled_appointments": []
        },
        "Zhang Jia Ming": {
            "identification": "zm,xz,cmzxczx,",
            "policy_number": "123470128479",
            "policy": {
                "details": {
                    "type": "Inactive",
                    "coverage_amount": 0,
                    "authorized_providers": [],
                    "annual_income": 0,
                },
                "claims": [],
            },
            "scheduled_appointments": []
        }
    },
    "providers": {
        "mayo_clinic_rochester": {
            "name": "Mayo Clinic",
            "location": "Rochester",
            "service_type": "Health",
            "availability": "Avaliable",
            "appointments": []
        },
        "cleveland_clinic_ohio": {
            "name": "Cleveland Clinic",
            "location": "Ohio",
            "service_type": "Health",
            "availability": "Avaliable",
            "appointments": []
        },
        "johns_hopkins_baltimore": {
            "name": "John Hopkins",
            "location": "Baltimore",
            "service_type": "Dental",
            "availability": "Unavaliable",
            "appointments": []
        },
        "kaiser_permanente_oakland": {
            "name": "Kaiser Permanente",
            "location": "Oakland",
            "service_type": "Pharmacy",
            "availability": "Unavaliable",
            "appointments": []
        }
    },
    "interaction_time": "2025-01-15T12:56:39"
}


default_data_descriptions = {
    "accounts": "A dictionary containing user accounts, each identified by the user's name.",
    "identification": "A unique identifier for the user, used for authentication.",
    "policy_number": "A unique number assigned to the user's policy for identification.",
    "policy": "A dictionary containing details of the user's insurance policy, including type, coverage, claims, and authorized providers.",
    "details": "The dictionary including all of the policy's details.",
    "type": "The type of insurance policy the user holds (e.g., Health, Inactive).",
    "coverage_amount": "The maximum amount the policy will cover for claims.",
    "enrollment_date": "The date the user's policy was activated.",
    "claims": "A list of claims filed under the user's policy, including claim details such as amount, status, and description.",
    "claim_id": "A unique identifier for each claim filed under the user's policy.",
    "amount": "The monetary amount requested for a claim.",
    "status": "The current status of the claim (e.g., approved, pending, denied).",
    "description": "A brief explanation of the medical service or treatment for which the claim was filed.",
    "claim_date": "The date when the claim was submitted.",
    "authorized_providers": "A list of healthcare providers approved to provide services under the user's policy.",
    "annual_income": "The user's reported annual income, used for eligibility and coverage determination.",
    "scheduled_appointments": "A list of upcoming healthcare appointments scheduled by the user.",
    "policy_type": "The type of policy. Must be one of the following: Health, Dental, Pharmacy, Vision, or Invalid.",
    
    "providers": "A dictionary containing information about healthcare providers, each identified by a unique provider ID.",
    "name": "The official name of the healthcare provider.",
    "location": "The city or region where the healthcare provider is located.",
    "service_type": "The type of medical service the provider specializes in (e.g., Health, Dental, Pharmacy).",
    "availability": "The availability status of the provider (e.g., Available, Unavailable).",
    "appointments": "A list of scheduled appointments for the provider.",

    "interaction_time": "The current system time, used for determining policy and claim deadlines."
}


ddp = default_dependency_parameters = {
    "max_coverage_percentage": 20,
    "enrollment_period": 90,
    "appeal_period": 180,
    "maximum_claimable_amount": 5000

}

# the main healthcare functionality
class Healthcare:
    def __init__(self, data:dict=default_data, dep_innate_full:dict=get_domain_dependency_none("Healthcare"), dep_params:dict=default_dependency_parameters, data_descriptions:dict=default_data_descriptions):
        self.data = data
        self.accounts = self.data["accounts"] if data else {}
        self.providers = self.data["providers"] if data else {}
        self.interaction_time = self.data["interaction_time"]
        self.innate_state_tracker = Healthcare_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full) 
        self.data_descriptions = data_descriptions


#######################################################################################################
#Root Functions
#######################################################################################################

    def login_user(self, username: str, identification: str) -> bool:
        if username not in self.accounts: return False
        return self.accounts[username]["identification"] == identification

    def logout_user(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        return True


    def update_policy(self, username: str, policy_type: str, coverage_amount: float, annual_income: float) -> bool:
        if not self.domain_dep.process(method_str="update_policy", username=username, policy_type = policy_type, coverage_amount = coverage_amount, annual_income = annual_income): return False
        self.accounts[username]["policy"]["details"]["type"] = policy_type
        self.accounts[username]["policy"]["details"]["coverage_amount"] = coverage_amount
        self.accounts[username]["policy"]["details"]["annual_income"] = annual_income
        return True
    
#######################################################################################################
#Domain Functions
#######################################################################################################

    # maybe change how submit claim works -> it is kinda strange right now.
    def submit_claim(self, username: str, amount: float, description: str, provider_id: str) -> bool:
        if not self.domain_dep.process(method_str="submit_claim", username=username, amount = amount, description = description, provider_id = provider_id): return False
        policy = self.accounts[username]["policy"]
        claim_id = f"CLM-{len(policy['claims']) + 1}"

        policy["claims"].append({
            "claim_id": claim_id,
            "amount": amount,
            "status": "pending",
            "description": description,
            "provider_id": provider_id,
            "claim_date": self.interaction_time
        })

        return True

    def get_policy_details(self, username: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="get_policy_details", username=username): return False, {}
        return True, self.accounts.get(username, {}).get("policy", {}).get("details", {})

    def get_claim_details(self, username: str, claim_id: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="get_claim_details", username=username, claim_id = claim_id): return False, {}
        for claim in self.accounts[username]["policy"]["claims"]:
            if claim["claim_id"] == claim_id:
                return True, claim
            
    def get_provider_details(self, provider_id: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="get_provider_details",provider_id = provider_id): return False, {}
        return True, self.providers[provider_id]

    def add_authorized_provider(self, username: str, provider_id: str) -> bool:
        if not self.domain_dep.process(method_str="add_authorized_provider", username=username, provider_id=provider_id): return False
        self.accounts[username]["policy"]["details"]["authorized_providers"].append(provider_id)
        return True



    def get_claim_history(self, username: str) -> tuple[bool, list]:
        if not self.domain_dep.process(method_str="get_claim_history", username=username): return False, []
        return True, self.accounts[username]["policy"]["claims"]
    
    #add in assistants
    def deactivate_policy(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="deactivate_policy", username=username): return False
        self.accounts[username]["policy"]["details"] = {
            "type": "Inactive",
            "coverage_amount": 0,
            "enrollment_date": "",
            "authorized_providers": [],
            "annual_income": 0,
        }
        self.accounts[username]["policy"]["claims"] = []
        return True
    
    def reactivate_policy(self, username: str, policy_type: str, coverage_amount: float, annual_income: float) -> bool:
        if not self.domain_dep.process(method_str="reactivate_policy", username=username, policy_type=policy_type, coverage_amount=coverage_amount, annual_income = annual_income): return False
        self.accounts[username]["policy"]["details"] = {
            "type": policy_type,
            "coverage_amount": coverage_amount,
            "enrollment_date": self.interaction_time,
            "authorized_providers": [],
            "annual_income": annual_income
        }
        return True
    

    
    def appeal_claim(self, username: str, claim_id: str) -> bool:
        if not self.domain_dep.process(method_str="appeal_claim", username=username, claim_id=claim_id): return False
        for claim in self.accounts[username]["policy"]["claims"]:
            if claim["claim_id"] == claim_id:
                claim["status"] = "pending"
                return True
        return False
    
    #maybe fix
    def schedule_appointment(self, username: str, provider_id: str, appointment_date: str) -> bool:
        if not self.domain_dep.process(method_str="schedule_appointment", username=username, provider_id=provider_id, appointment_date=appointment_date): return False
        appointment_id = f"APT-{len(self.accounts[username]['scheduled_appointments']) + 1}"

        appointment_details = {
            "appointment_id": appointment_id,
            "provider_id": provider_id,
            "appointment_date": appointment_date
        }

        self.accounts[username]["scheduled_appointments"].append(appointment_details)
        self.providers[provider_id]["appointments"].append({
            "appointment_id": appointment_id,
            "username": username,
            "appointment_date": appointment_date
        })
        return True
    
    
    
    def internal_get_database(self) -> tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_database"): return False
        return True, self.data
    
    def internal_check_username_exist(self, username:str)->tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_username_exist", username=username): return False
        return True, username in self.accounts

    def internal_check_provider_exists(self, provider_id: str) -> tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_provider_exists", provider_id=provider_id): return False
        return True, provider_id in self.providers
    
    def internal_check_claim_exists(self, username: str, claim_id: str) -> tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_claim_exists",username = username, claim_id=claim_id): return False
        for claim in self.accounts[username]["policy"]["claims"]:
            if claim["claim_id"] == claim_id:
                return True, True
        return True, False
    
    def internal_get_interaction_time(self) -> tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_interaction_time"): return False
        return True, self.interaction_time
    

    def evaluation_get_database(self)->dict:
        return self.data
    
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions


class Healthcare_State_Tracker:
    # Initialization
    def __init__(self, domain_system: Healthcare, max_coverage_percentage: float, enrollment_period: int, appeal_period:int, maximum_claimable_amount:int):
        self.domain_system = domain_system
        self.max_coverage_percentage = max_coverage_percentage
        self.enrollment_period = enrollment_period
        self.appeal_period = appeal_period
        self.maximum_claimable_amount = maximum_claimable_amount
        self.previously_logged_in_username: str = None 
        
    def logged_in_user(self, username: str) -> bool:
        return self.previously_logged_in_username == username
    def amount_positive_restr(self, amount) -> bool:
        return amount >= 0
    
    def claim_within_limits(self, amount: float) -> bool:
        return amount < self.maximum_claimable_amount

    def claim_within_coverage_amount(self, username: str, amount: float) -> bool:
        _, claim_history = self.domain_system.get_claim_history(username)
        _, policy_details = self.domain_system.get_policy_details(username)

        coverage_amount = policy_details["coverage_amount"]
        total_claimed = sum(
            claim["amount"] for claim in claim_history if claim["status"] in ["pending", "approved"]
        )
        return (total_claimed + amount) <= coverage_amount
    
    def provider_not_already_authorized(self, username: str, provider_id: str) -> bool:
        _, policy = self.domain_system.get_policy_details(username)
        authorized_providers = policy["authorized_providers"]
        return provider_id not in authorized_providers
    
    def policy_inactive(self, username: str) -> bool:
        _, policy = self.domain_system.get_policy_details(username)
        return policy["type"] == "Inactive"
    
    def policy_active(self, username: str) -> bool:
        _, policy = self.domain_system.get_policy_details(username)
        return policy["type"] != "Inactive"
    
    def no_pending_claims(self, username: str):
        _, claim_history = self.domain_system.get_claim_history(username)
        return all(claim["status"] != "pending" for claim in claim_history)
    
    def provider_covers_policy(self, username: str, provider_id: str):
        _, provider = self.domain_system.get_provider_details(provider_id)
        provider_coverage = provider["service_type"]
        _, policy = self.domain_system.get_policy_details(username)
        policy_type = policy["type"]
        return provider_coverage == policy_type
    
    def income_proof_enough(self, annual_income: float, coverage_amount: float) -> bool:
        return coverage_amount <= (annual_income * self.max_coverage_percentage / 100)
    
    def claim_status_denied(self, username: str, claim_id: str):
        _, claim = self.domain_system.get_claim_details(username, claim_id)
        claim_status = claim["status"]
        return claim_status == "denied"
    
    def within_enrollment_period(self, username: str) -> bool:
        _, policy = self.domain_system.get_policy_details(username)
        enrollment_date = datetime.strptime(policy["enrollment_date"], "%Y-%m-%d") 
        _, current_time = self.domain_system.internal_get_interaction_time()
        time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
        return (time - enrollment_date) <= timedelta(days=self.enrollment_period)
    
    def within_appeal_period(self, username: str, claim_id: str) -> bool:
        _, claim = self.domain_system.get_claim_details(username, claim_id)
        claim_date = datetime.strptime(claim["claim_date"], "%Y-%m-%d") 
        _, current_time = self.domain_system.internal_get_interaction_time()
        time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
        return (time - claim_date) <= timedelta(days=self.appeal_period)
    
    def provider_available(self, provider_id: str) -> bool:
        _, provider = self.domain_system.get_provider_details(provider_id)
        return provider["availability"].lower() == "available"
    
    def provider_authorized(self, username: str, provider_id: str) -> bool:
        _, policy = self.domain_system.get_policy_details(username)
        providers = policy["authorized_providers"]
        return provider_id in providers
    
    def policy_type_valid(self, policy_type: str) -> bool:
        valid_policy_types = {"Health", "Dental", "Pharmacy", "Vision"}
        return policy_type in valid_policy_types
    
    def appointment_date_valid(self, appointment_date: str) -> bool:
        _, current_time = self.domain_system.internal_get_interaction_time()
        time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
        date_formats = [
            "%Y-%m-%d %H:%M:%S",  
            "%Y-%m-%d %H:%M",  
            "%Y-%m-%dT%H:%M:%S", 
            "%Y-%m-%dT%H:%M",   
            "%Y-%m-%d",         
        ]
        for fmt in date_formats:
            try:
                appointment_time = datetime.strptime(appointment_date, fmt)
                break
            except ValueError:
                continue
        else:
            return False
        appointment_time = appointment_time.replace(hour=0, minute=0, second=0, microsecond=0)
        return appointment_time >= time
    
    def set_login_user(self, username: str):
        self.previously_logged_in_username = username
    def set_logout_user(self):
        self.previously_logged_in_username = None 
    


class Healthcare_Strict:
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Healthcare"),
        dep_full:dict=get_domain_dependency_none("Healthcare_Strict"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        
        self.dep_params = dep_params
        self.domain_system:Healthcare = Healthcare(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker:Healthcare_State_Tracker = Healthcare_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep:Dependency_Evaluator = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)
    
    # Root functions
    def login_user(self, username:str, identification:str|dict[str:str|int]=None)->bool:
        if not self.domain_dep.process(method_str="login_user", username=username, identification=identification): return False
        self.state_tracker.set_login_user(username)
        return self.domain_system.login_user(username, identification)

    def logout_user(self, username: str) -> bool:
        dep_res = self.domain_dep.process(method_str="logout_user", username=username)
        if not dep_res:
            return False
        self.state_tracker.set_logout_user()
        return self.domain_system.logout_user(username)

    # Account functions
    
    def update_policy(self, **kwargs) -> bool:
        return self._check_dep_and_do("update_policy", **kwargs)


    def submit_claim(self, **kwargs) -> tuple[bool, str]:
        return self._check_dep_and_do("submit_claim", **kwargs)


    def get_claim_details(self, **kwargs) -> tuple[bool, dict]:
        return self._check_dep_and_do("get_claim_details", **kwargs)



    def add_authorized_provider(self, **kwargs) -> bool:
        return self._check_dep_and_do("add_authorized_provider", **kwargs)



    def get_claim_history(self, **kwargs) -> tuple[bool, list]:
        return self._check_dep_and_do("get_claim_history", **kwargs)

    
    def deactivate_policy(self, **kwargs) -> bool:
        return self._check_dep_and_do("deactivate_policy", **kwargs)


    def reactivate_policy(self, **kwargs) -> bool:
        return self._check_dep_and_do("reactivate_policy", **kwargs)


    
    def appeal_claim(self, **kwargs) -> bool:
        return self._check_dep_and_do("appeal_claim", **kwargs)

    
    def schedule_appointment(self, **kwargs) -> bool:
        return self._check_dep_and_do("schedule_appointment", **kwargs)
    
    def get_policy_details(self, **kwargs) -> tuple[bool, dict]:
        return self._check_dep_and_do("get_policy_details", **kwargs)
    
    def get_provider_details(self, **kwargs) -> tuple[bool, dict]:
        return self._check_dep_and_do("get_provider_details", **kwargs)

    def internal_get_database(self, **kwargs) -> tuple[bool, dict]:
        return self._check_dep_and_do("internal_get_database", **kwargs)

    def internal_check_username_exist(self, **kwargs) -> tuple[bool, bool]:
        return self._check_dep_and_do("internal_check_username_exist", **kwargs)

    def internal_check_provider_exists(self, **kwargs) -> tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_provider_exists", **kwargs)

    
    def internal_check_claim_exists(self, **kwargs) -> tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_claim_exists", **kwargs)

    def internal_get_interaction_time(self, **kwargs) -> tuple[bool,str]:
        return self._check_dep_and_do("internal_get_interaction_time", **kwargs)

    

    # Evaluation functions, solely used for testing this domain_system in the pipeline
    
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->Healthcare:
        return self.domain_system
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->Healthcare_State_Tracker:
        return self.state_tracker
    def _check_dep_and_do(self, method_str, **kwargs):
        if not self.domain_dep.process(method_str=method_str, **kwargs): return False
        return getattr(self.domain_system, method_str)(**kwargs)