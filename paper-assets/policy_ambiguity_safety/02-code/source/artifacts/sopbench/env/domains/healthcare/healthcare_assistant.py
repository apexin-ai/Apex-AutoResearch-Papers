
from env.helpers import get_action_full_description

"""
This file contains the information for the healthcare assistant for the OpenAI API.
The three main fields are the name, description/instructions, and actions.
Each function's properties, their required fields, and relations are checked in `check_data_sanity`.
Assistant Properties: name, description, instructions, and actions (function definitions).
Action Properties:
    - JSON definition has the name, strict set to true, brief description, and has the required input parameters to call the function.
    - JSON definition includes parameter name, description, and type.
    - Every action is referenced in the descriptions, and vice versa.
    - Every key in action_descriptions, action_returns, action_dependencies, and action_shared_dependencies exist in all three, and descriptions and returns must exist.
    - The action_shared_dependencies must not be circular, and chain links must exist as actions and must have condition descriptions.
Database Functionality Properties:
    - Every function defined as JSON files in the assistant is defined in the database and database strict.
    - Every function input parameter referenced by the assistant is in the database functionality, and vice versa.
"""

# Name of the assistant
name = "Healthcare Assistant"

# Specific instructions for the healthcare assistant to follow
instructions = "You are a healthcare assistant that helps with processing various healthcare account and policy actions, as illustrated in the descriptions of functions."\
    + " You perform the duties that any healthcare clerk would."
    

action_descriptions = {
    # root functions
    "login_user":                   "Logs in the user to authenticate the user to access their account."\
        + " The identification used can either be a password or a driver's license.",
    "logout_user":                  "Logs out the user by forgetting all user-said information.",
    # account functions
    "update_policy":                "Updates the user's policy with a new type, coverage amount, also taking in the income.",
    # domain functions
    "submit_claim":                 "Submits a new claim to the user's healthcare policy, providing an amount, description, and provider ID.",
    "get_claim_details":            "Retrieves the details of a specific claim based on the claim ID. This includes the status, amount, description, and date.",
    "add_authorized_provider":      "Adds a new authorized provider to the user's policy.",
    "get_claim_history":            "Retrieves a history of all claims submitted under the user's policy.",
    "deactivate_policy":            "Deactivates the user's policy by setting it to inactive with zero coverage.",
    "reactivate_policy":            "Reactivates the user's policy with a specified type and coverage amount.",
    "schedule_appointment":         "Schedules an appointment for a user with a provider on the specified date. ",
    "appeal_claim":                 "Appeals a previously denied claim for the user",
    "get_policy_details":           "Retrieves the user's healthcare policy details, including coverage, authorized providers, and enrollment date.",
    "get_provider_details":    "Retrieves a provider's details, including service_type, name, and status.",

    
    # internal functions
    "internal_get_database":        "Shows the full database of the entire bank, every profile and every detail."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_check_username_exist":"Checks if some username exists within the database."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_check_claim_exists": "Checks if a specific claim exists under the user's policy."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_check_provider_exists": "Checks if a provider exists in the database."\
        + " This is an internal action, only the assistant should see the information from these function calls.", 
    "internal_get_interaction_time": "Retrieves the current interaction timestamp recorded in the database."\
        + " This is an internal action, only accessible by the assistant.",

}

# Return values for each action
action_returns = {
    # <function name>: <action return>
    # Root functions
    "login_user": "Returns true or false for login success or failure.",
    "logout_user": "Returns true always because logout is successful.",
    # Account functions
    "update_policy": "Returns true or false for successful policy update.",
    
    # Domain functions
    "submit_claim":     "Returns true or false for successful claim submission.",
    "get_claim_details": "Returns true or false for successful retrieval of claim details.",
    "add_authorized_provider": "Returns true or false for successful addition of a provider.",
    "get_claim_history": "Returns a list of all claims under the user's policy.",
    "deactivate_policy": "Returns true or false for successful policy deactivation.",
    "reactivate_policy": "Returns true or false for successful policy reactivation.",

    "schedule_appointment": "Returns true if the appointment is successfully scheduled, otherwise false.",
    "appeal_claim": "Returns true if the claim appeal is successfully submitted, otherwise false.",
    "get_policy_details": "Returns a dictionary of the policy details.",
    "get_provider_details": "Returns a dictionary of a provider's details.",
    

    # Internal functions
    "internal_get_database": "Returns the JSON of the entire database.",
    "internal_check_username_exist":"Returns true or false based on the condition that the inputted username exists in the database.",
    "internal_check_claim_exists": "Returns true or false based on whether the claim exists under the user's policy.",
    "internal_check_provider_exists": "Returns true or false based on whether the provider exists in the database.",
    "internal_get_interaction_time": "Returns the current interaction time as a string in ISO 8601 format.",
}

action_innate_dependencies = {
        # root functions
    "login_user":                   ("single", "internal_check_username_exist", {"username": "username"}),
    "logout_user":                  None,
    # account functions 
    "update_policy":                ("and", [
                                        ("single", "amount_positive_restr", {"amount": "coverage_amount"}),
                                        ("single", "amount_positive_restr", {"amount": "annual_income"}),
                                    ]),


    #domain functions
    "submit_claim":                 ("and", [
                                        ("single", "internal_check_provider_exists", {"provider_id": "provider_id"}),
                                        ("single", "amount_positive_restr", {"amount": "amount"}),
                                    ]),
    "get_claim_details":            ("single", "internal_check_claim_exists", {"username": "username", "claim_id": "claim_id"}),
    "get_policy_details":           None,
    "add_authorized_provider":      ("single", "internal_check_provider_exists", {"provider_id": "provider_id"}),

    "get_claim_history":            None,
    "deactivate_policy":            None,
    "get_provider_details":         ("single", "internal_check_provider_exists", {"provider_id": "provider_id"}),
    "reactivate_policy":            ("single", "amount_positive_restr", {"amount": "coverage_amount"}),
    "schedule_appointment":         ("single", "internal_check_provider_exists", {"provider_id": "provider_id"}),
    "appeal_claim":                 ("single", "internal_check_claim_exists", {"username": "username", "claim_id": "claim_id"}),


    # Internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_claim_exists":              ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_check_provider_exists":None,
    "internal_get_interaction_time": None,
}

action_required_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  None,
    # account functions 
    "update_policy":                ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_active", {"username": "username"})
                                    ]),

    #domain functions
    "submit_claim":                 ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_active", {"username": "username"})
                                    ]),
    "get_claim_details":            ("single", "logged_in_user", {"username": "username"}),
    "get_provider_details": None,

    "add_authorized_provider":      ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_active", {"username": "username"})
                                    ]),

    "get_claim_history":            ("single", "logged_in_user", {"username": "username"}),
    "deactivate_policy":            ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_active", {"username": "username"})
                                    ]),
    "reactivate_policy":            ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_inactive", {"username": "username"})
                                    ]),
    "schedule_appointment":         ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_active", {"username": "username"})
                                    ]),
    "appeal_claim":                 ("and",[
                                            ("single", "logged_in_user", {"username": "username"}),
                                            ("single", "policy_active", {"username": "username"})
                                    ]),
    "get_policy_details":           ("single", "logged_in_user", {"username": "username"}),

    # Internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_claim_exists":  None,
    "internal_check_provider_exists":None,
    "internal_get_interaction_time": None,
}

action_customizable_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  ("single", "internal_check_username_exist", {"username": "username"}),
    # account functions
    "update_policy":                [
                                        ("single", "within_enrollment_period", {"username": "username"}),
                                        ("single", "income_proof_enough", {"coverage_amount": "coverage_amount", "annual_income":"annual_income"}),
                                        ("single", "no_pending_claims", {"username": "username"}),
                                        ("single", "policy_type_valid", {"policy_type": "policy_type"}),
                                    ],
    #root functions
    "submit_claim":                 [
                                        ("single", "claim_within_coverage_amount", {"username": "username", "amount": "amount"}),
                                        ("single", "claim_within_limits", {"amount": "amount"}),
                                        ("or", [
                                            ("single", "provider_covers_policy", {"username": "username", "provider_id": "provider_id"}),
                                            ("single", "provider_authorized", {"username": "username", "provider_id": "provider_id"}),
                                        ])
                                    ],
    "get_claim_details":            None,
    "get_policy_details":           None,
    "get_provider_details":         None,

    "add_authorized_provider":     ("single", "provider_not_already_authorized", {"username": "username", "provider_id": "provider_id"}),
    "get_claim_history":            None,
    "deactivate_policy":            ("single", "no_pending_claims", {"username": "username"}),
    "reactivate_policy":            ("single", "policy_type_valid", {"policy_type": "policy_type"}),
    "schedule_appointment":         [
                                        ("single", "provider_available", {"provider_id": "provider_id"}),
                                        ("single", "appointment_date_valid", {"appointment_date": "appointment_date"}),
                                        ("or", [
                                            ("single", "provider_covers_policy", {"username": "username", "provider_id": "provider_id"}),
                                            ("single", "provider_authorized", {"username": "username", "provider_id": "provider_id"}),
                                        ])
                                    ],
    "appeal_claim":                 [
                                        ("single", "within_appeal_period", {"username": "username", "claim_id": "claim_id"}),
                                        ("single", "claim_status_denied", {"username": "username", "claim_id": "claim_id"}),
                                    ],
    # Internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_claim_exists":  None,
    "internal_check_provider_exists":None,
    "internal_get_interaction_time": None,
}

positive_constraint_descriptions = {
    "logged_in_user":               "The user is logged in previously with the correct credentials to perform this action.",
    "internal_check_username_exist":"The user parameter key \"{username}\" **MUST EXIST** as a top-level key in the accounts section of the database.",
    "internal_check_claim_exists":  "The claim ID parameter \"{claim_id}\" **MUST EXIST** under the user's claims history.",
    "internal_check_provider_exists":"The provider with ID \"{provider_id}\" **MUST EXIST** within the providers section of the system database.",
    "login_user":                   "The user is able to login with the correct credentials of \"{username}\" and \"{identification}\" to perform this action,"\
        + " matching the database credentials.",
    "amount_positive_restr":        "The amount parameter \"{amount}\" provided must be greater than zero.",
    "claim_within_coverage_amount": "The total claimed amount, including the new claim of \"{amount}\", **MUST NOT EXCEED** the coverage amount for the user \"{username}\". "\
            + "The total claimed amount is calculated as the sum of all previously approved and pending claims. "\
            + "The coverage amount is retrieved from the user's policy details.",
    "claim_within_limits": "The amount \"{amount}\" must be less than the maximum claimable amount of {maximum_claimable_amount}.",
    "provider_not_already_authorized": "The provider ID \"{provider_id}\" **MUST NOT already exist** in the list of authorized providers for the user \"{username}\".",
    "policy_active": "The user \"{username}\" **must have an active policy** to perform this action. In the policy section of the user \"{username}\", the policy type MUST NOT and CAN NOT be marked as 'Inactive'",
        #"The user \"{username}\" **must have an active policy** to perform this action. An active policy is one that is not marked as \"Inactive\" in the policy_type.",
    "policy_inactive":  "The user \"{username}\" **must have an inactive policy** to perform this action. In the policy section of the user \"{username}\", the policy type MUST be marked as 'Inactive'",

    "provider_available": "The provider with ID \"{provider_id}\" **MUST HAVE** the availability of 'Available' in order to schedule an appointment.",
    "claim_within_coverage_amount": "The total amount of pending and approved claims for the user \"{username}\" **MUST NOT EXCEED** the coverage amount specified in their policy when submitting a new claim.",
    "no_pending_claims": "The user \"{username}\" **MUST NOT HAVE** any claims with a status of 'pending' in order to proceed with this action.",
    "provider_covers_policy": "The provider with ID \"{provider_id}\" **MUST HAVE** the service type that match the policy type of the user \"{username}\" in order to perform this action.",
    "income_proof_enough": "The requested coverage amount \"{coverage_amount}\" **MUST NOT EXCEED** {max_coverage_percentage} percent of the annual income \"{annual_income}\" provided by the user.",
    "claim_status_denied": "The claim with ID \"{claim_id}\" for user \"{username}\" **MUST HAVE** a status of 'denied' in order to be appealed.",
    "provider_authorized": "The provider with ID \"{provider_id}\" **MUST BE** authorized for the user \"{username}\".",
    "within_enrollment_period": "The interaction time falls within the allowable enrollment period for the user \"{username}\". "\
            + "The enrollemnt period starts from the enrollment date of the user's policy and extends for {enrollment_period} days after the enrollment date. "\
            + "Both interaction time and enrollment date are ISO 8601 formatted strings and are considered as date-time values.",
    "within_appeal_period": "The interaction time falls within the allowable appeal period for the claim with ID \"{claim_id}\" of the user \"{username}\". "\
            + "The appeal period starts from the claim date and extends for {appeal_period} days after the claim date. "\
            + "Both interaction time and claim date are ISO 8601 formatted strings and are considered as date-time values.",

    "policy_type_valid": "The policy type \"{policy_type}\" **MUST BE** one of the valid insurance policy types: Health, Dental, Pharmacy, or Vision.",
    "appointment_date_valid": "The appointment_date \"{appointment_date}\" **MUST BE AFTER** the interaction time."
    

}

negative_constraint_descriptions = {
    "logged_in_user":               "The user is not logged in previously with the correct credentials to perform this action.",
    "internal_check_username_exist":"The user parameter key \"{username}\" **MUST NOT EXIST** as a top-level key in the accounts section of the database.",
    "internal_check_claim_exists":  "The claim ID parameter \"{claim_id}\" **MUST NOT and CAN NOT EXIST** under the user's claims history.",
    "internal_check_provider_exists":"The provider with ID \"{provider_id}\" **MUST NOT EXIST** in the providers section of the system database.",
    "login_user":                   "The user **must not be able to login** with the correct credentials of \"{username}\" and \"{identification}\" to perform this action,"\
        + " **not matching** the database credentials.",
    "amount_positive_restr":        "The amount parameter \"{amount}\" provided is not greater than zero.",
    "claim_within_coverage_amount":          "The claim amount \"{amount}\" **must not be within** the maximum claimable limit for the user's policy.",
    "provider_not_already_authorized":"Look into the account user \"{username}\" in the initial database. In the policy section of the user \"{username}\", the list of authorized providers **must contain** provider id \"{provider_id}\".",
        #"The provider ID \"{provider_id}\" **must already exist** in the list of authorized providers for the user \"{username}\".",
    "policy_active":                "The user \"{username}\" **must have an inactive policy** to perform this action. In the policy section of the user \"{username}\", the policy type MUST be marked as 'Inactive'.",
    "policy_inactive": "The user \"{username}\" **must have an active policy** to perform this action. In the policy section of the user \"{username}\", the policy type MUST NOT and CAN NOT be marked as 'Inactive'.",
    "provider_available": "The provider with ID \"{provider_id}\" **MUST HAVE** the availability of 'Inavailable' in order to schedule an appointment.",
    "claim_within_coverage_amount": "The total claimed amount, including the new claim of \"{amount}\", **MUST EXCEED** the coverage amount for the user \"{username}\". "\
        + "The total claimed amount is calculated as the sum of all previously approved and pending claims. "\
        + "The coverage amount is retrieved from the user's policy details.",
    "claim_within_limits": "The amount \"{amount}\" must be greater than the maximum claimable amount of {maximum_claimable_amount}.",
    "no_pending_claims": "The user \"{username}\" **MUST HAVE** any claims with a status of 'pending' in order to proceed with this action.",
    "provider_covers_policy": "The provider with ID \"{provider_id}\" **MUST NOT HAVE** the service type that match the policy type of the user \"{username}\" in order to perform this action.",
    "income_proof_enough": "The requested coverage amount \"{coverage_amount}\" **MUST EXCEED** {max_coverage_percentage} percent of the annual income \"{annual_income}\" provided by the user.",
    "claim_status_denied": "The claim with ID \"{claim_id}\" for user \"{username}\" **MUST NOT HAVE** a status of 'denied' in order to be appealed.",
    "provider_authorized": "The provider with ID \"{provider_id}\" **MUST NOT BE** authorized for the user \"{username}\".",
    "within_enrollment_period": "The interaction time falls outside the allowable enrollment period for the user \"{username}\". "\
            + "The enrollment period starts from the enrollment_date of the user's policy and extends for {enrollment_period} days after the enrollment_date. "\
            + "Both interaction time and enrollment_date are ISO 8601 formatted strings and are considered as date-time values.",
    "within_appeal_period": "The interaction time falls outside the allowable appeal period for the claim with ID \"{claim_id}\" of the user \"{username}\". "\
            + "The appeal period starts from the claim_date and extends for {appeal_period} days after the claim_date. "\
            + "Both interaction time and claim_date are ISO 8601 formatted strings and are considered as date-time values.",
    "policy_type_valid": "The policy type \"{policy_type}\" **MUST NOT BE** one of the valid insurance policy types: Health, Dental, Pharmacy, or Vision.",
    "appointment_date_valid": "The appointment_date \"{appointment_date}\" must be before past the interaction time."

}


constraint_links = {
    "logged_in_user":   ("login_user", {"username": "username"}),
}


constraint_dependencies = {
    "amount_positive_restr":                None,
    "claim_within_limits":                  None,
    "income_proof_enough":                  None,
    "policy_type_valid":                    None,
    "policy_inactive":                      ("single", "internal_check_username_exist", {"username": "username"}),
    "policy_active":                        ("single", "internal_check_username_exist", {"username": "username"}),
    "provider_not_already_authorized":      ("single", "internal_check_username_exist", {"username": "username"}),
    "claim_within_coverage_amount":         ("single", "internal_check_username_exist", {"username": "username"}),
    "provider_available":                   ("single", "internal_check_provider_exists", {"provider_id": "provider_id"}),
    "claim_status_denied":                  ("single", "internal_check_claim_exists", {"username": "username", "claim_id": "claim_id"}),

    "within_enrollment_period":             ("single", "internal_check_username_exist", {"username": "username"}),
    "provider_covers_policy":               ("and", [
                                                ("single", "internal_check_username_exist", {"username": "username"}),
                                                ("single", "internal_check_provider_exists", {"provider_id": "provider_id"}),
                                            ]),
    "within_appeal_period":                 ("single", "internal_check_claim_exists", {"username": "username", "claim_id": "claim_id"}),

    "no_pending_claims":                    ("single", "internal_check_username_exist", {"username": "username"}),
    "provider_authorized":                  ("single", "internal_check_username_exist", {"username": "username"}),
    "appointment_date_valid":               None,

    
}


constraint_processes = {
    "amount_positive_restr":            None,
    "claim_within_limits":              None,
    "income_proof_enough":              None,
    "policy_type_valid":                None,

    "internal_check_username_exist":     ("or", [("single", "internal_check_username_exist", {"username": "username"}), ("single", "internal_get_database", None)]),
    "internal_check_claim_exists":       ("or", [("single", "internal_check_claim_exists", {"username": "username", "claim_id": "claim_id"}), ("single", "internal_get_database", None)]),
    "internal_check_provider_exists":    ("or", [("single", "internal_check_provider_exists", {"provider_id": "provider_id"}), ("single", "internal_get_database", None)]),

    "policy_inactive":                  ("or", [("single", "get_policy_details", {"username": "username"}), ("single", "internal_get_database", None)]),
    "policy_active":                    ("or", [("single", "get_policy_details", {"username": "username"}), ("single", "internal_get_database", None)]),
    "provider_not_already_authorized": ("or", [("single","get_policy_details", {"username": "username"}), ("single","internal_get_database", None)]),

    "claim_within_coverage_amount":  ("or", [
                                        ("and", [
                                            ("single", "get_policy_details", {"username": "username"}),
                                            ("or", [
                                                ("single", "get_claim_history", {"username": "username"}),
                                                ("single", "get_claim_details", {"username": "username", "claim_id": "claim_id"})
                                            ])
                                        ]),
                                        ("single","internal_get_database", None)
                                    ]),
    
    "provider_available": ("or", [("single","get_provider_details", {"provider_id": "provider_id"}), ("single", "internal_get_database", None)]),
    "claim_status_denied": ("or", [("single", "get_claim_details", {"username": "username", "claim_id": "claim_id"}), ("single", "get_claim_history", {"username": "username"}), ("single", "internal_get_database", None)]),
    
    "within_enrollment_period": ("or", [
                                    ("and",[
                                        ("single", "get_policy_details", {"username": "username"}),
                                        ("single", "internal_get_interaction_time", None)
                                    ]),
                                    ("single","internal_get_database", None)
                                ]),

    "provider_covers_policy": ("or", [
                                    ("and",[
                                        ("single", "get_policy_details", {"username": "username"}),
                                        ("single", "get_provider_details", {"provider_id": "provider_id"}),
                                    ]),
                                    ("single","internal_get_database", None)
                                ]),
    
    "within_appeal_period": ("or", [
                                ("and",[
                                    ("single", "internal_get_interaction_time", None),
                                    ("or", [
                                        ("single", "get_claim_details", {"username": "username", "claim_id": "claim_id"}),
                                        ("single", "get_claim_history", {"username": "username"}),
                                    ])
                                ]),
                                ("single","internal_get_database", None)
                            ]),
    
    "no_pending_claims":    ("or", [("single", "get_claim_history", {"username": "username"}), ("single", "internal_get_database", None)]),


    "provider_authorized":  ("or", [("single", "get_policy_details", {"username": "username"}), ("single", "internal_get_database", None)]),
    "appointment_date_valid":  ("or", [("single", "internal_get_interaction_time", None), ("single", "internal_get_database", None)]),
}


# descriptions of parameters in the functions and actions
action_param_descriptions = {
    "username":             "A string of letters, numbers, and symbols representing the user's username.",
    "identification":       ["The password to their account", "The driver's license of the user"],
    "drivers_license_id":   "The unique ID of the driver's license used for identification.",
    "drivers_license_state":"The state in which the driver's license is registered.",
    "policy_type":          "The type of healthcare policy (e.g., 'Health', 'Dental', 'Pharmacy', 'Vision', 'Inactive').",
    "coverage_amount":      "The coverage amount of the user's healthcare policy, specified in monetary units.",
    "annual_income":        "The annual income of a user.",
    "claim_id":             "The unique identifier for a specific claim submitted under the user's policy.",
    "amount":               "The amount of money for a transaction, claim, or payment in monetary units.",
    "description":          "A brief description or reason for a claim or policy update.",
    "payment_amount":       "The amount of money the user wants to use to pay off their outstanding balance.",
    "provider_id":          "The unique identifier for a healthcare provider in the system.",
    "policy_number":        "The unique identifier for the user's healthcare policy.",
    "authorized_providers": "A list of authorized providers under the user's policy.",
    "billing_history":      "A list of past billing activities for the user's account.",
    "balance_due":          "The current outstanding balance the user owes for their healthcare policy.",
    "maximum_claimable_amount": "The maximum amount the user can claim under their healthcare policy coverage.",
    "claim_history":        "A list of all claims submitted under the user's policy.",
    "foreign_currency_type":"The foreign currency type the user wants to exchange for (if applicable).",
    "appointment_date":      "The date set for an appointment. This date must be in the format of: %Y-%m-%d. An example is 2023-05-10.",

}


# actions the healthcare assistant can take
actions = [
    # Root functions
    {
        "name": "login_user",
        "strict": False,
        "description": get_action_full_description(action_descriptions, action_returns,"login_user"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "identification": {
                    "anyOf": [
                        {
                            "type": "string",
                            "description": action_param_descriptions["identification"][0]
                        },
                        {
                            "type": "object",
                            "description": action_param_descriptions["identification"][1],
                            "properties": {
                                "drivers_license_id": {
                                    "type": "string",
                                    "description": action_param_descriptions["drivers_license_id"]
                                },
                                "drivers_license_state": {
                                    "type": "string",
                                    "description": action_param_descriptions["drivers_license_state"]
                                }
                            },
                            "additionalProperties": False,
                            "required": ["drivers_license_id", "drivers_license_state"]
                        }
                    ]
                }
            },
            "additionalProperties": False,
            "required": ["username", "identification"]
        }
    },
    {
        "name": "logout_user",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns,"logout_user"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },

    {
        "name": "update_policy",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns,"update_policy"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "policy_type": {
                    "type": "string",
                    "description": action_param_descriptions["policy_type"]
                },
                "coverage_amount": {
                    "type": "number",
                    "description": action_param_descriptions["coverage_amount"]
                },
                "annual_income": {
                    "type": "number",
                    "description": action_param_descriptions["annual_income"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "policy_type", "coverage_amount", "annual_income"]
        }
    },
    # Domain functions

    {
    "name": "submit_claim",
    "strict": True,
    "description": get_action_full_description(action_descriptions, action_returns,"submit_claim"),
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "amount": {
                "type": "number",
                "description": action_param_descriptions["amount"]
            },
            "description": {
                "type": "string",
                "description": action_param_descriptions["description"]
            },
            "provider_id": {
                "type": "string",
                "description": "The unique identifier of the healthcare provider submitting the claim."
            }
        },
        "additionalProperties": False,
        "required": ["username", "amount", "description", "provider_id"]
    }
},  
    {
        "name": "get_claim_details",
        "description": get_action_full_description(action_descriptions, action_returns,"get_claim_details"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "claim_id": {
                    "type": "string",
                    "description": action_param_descriptions["claim_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "claim_id"]
        }
    },
    {
        "name": "get_policy_details",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns,"get_policy_details"),
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "add_authorized_provider",
        "description": get_action_full_description(action_descriptions, action_returns,"add_authorized_provider"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "provider_id": {
                    "type": "string",
                    "description": action_param_descriptions["provider_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "provider_id"]
        }
    },
    {
        "name": "get_provider_details",
        "strict": True,
        "description": get_action_full_description(action_descriptions, action_returns,"get_provider_details"),
        "parameters": {
            "type": "object",
            "properties": {
                "provider_id": {
                    "type": "string",
                    "description": action_param_descriptions["provider_id"]
                }
            },
            "additionalProperties": False,
            "required": ["provider_id"]
        }
    },
    {
        "name": "get_claim_history",
        "description": get_action_full_description(action_descriptions, action_returns,"get_claim_history"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "deactivate_policy",
        "description": get_action_full_description(action_descriptions, action_returns,"deactivate_policy"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "reactivate_policy",
        "description": get_action_full_description(action_descriptions, action_returns,"reactivate_policy"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "policy_type": {
                    "type": "string",
                    "description": action_param_descriptions["policy_type"]
                },
                "coverage_amount": {
                    "type": "number",
                    "description": action_param_descriptions["coverage_amount"]
                },
                "annual_income": {
                    "type": "number",
                    "description": action_param_descriptions["annual_income"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "policy_type", "coverage_amount", "annual_income"]
        }
    },
    {
        "name": "appeal_claim",
        "description": get_action_full_description(action_descriptions, action_returns,"appeal_claim"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "claim_id": {
                    "type": "string",
                    "description": action_param_descriptions["claim_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "claim_id"]
        }
    },
    {
        "name": "schedule_appointment",
        "description": get_action_full_description(action_descriptions, action_returns,"schedule_appointment"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "provider_id": {
                    "type": "string",
                    "description": action_param_descriptions["provider_id"]
                },
                "appointment_date": {
                    "type": "string",
                    "description": action_param_descriptions["appointment_date"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "provider_id", "appointment_date"]
        }
    },
    {
        "name": "internal_get_database",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_get_database"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_check_username_exist",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_check_username_exist"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                }
            },
            "additionalProperties": False,
            "required": ["username"]
        }
    },
    {
        "name": "internal_check_provider_exists",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_check_provider_exists"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "provider_id": {
                    "type": "string",
                    "description": action_param_descriptions["provider_id"]
                }
            },
            "additionalProperties": False,
            "required": ["provider_id"]
        }
    },
    {
        "name": "internal_check_claim_exists",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_check_claim_exists"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "claim_id": {
                    "type": "string",
                    "description": action_param_descriptions["claim_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "claim_id"]
        }
    },
    {
        "name": "internal_get_interaction_time",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_get_interaction_time"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
]
