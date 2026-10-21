"""
This file contains the information for the bank assistant fo the openai API.
The three main fields are the name, description/instructions, and actions.
Each function properties, their required fields, and relations are checked in check_data_sanity
Assistant Properties: name, description, instructions, and actions (function definitions)
Action Properties:
    json definition has the name, strict set to true, brief description, and has the required input parameters to call the function
    json definition includes parameter name, description, and type
    every action is referenced in the descriptions, and vice versa
    every key in action_descriptions, action_returns, action_dependencies, and action_shared_dependencies exist in all three, and descriptions and returns must exist
    the action_shared_dependencies must not be circular, and chain links must exist as actions and must have condition descriptions
Database Functionality Properties:
    every function defined as json files in the assistant is defined in the database and database strict
    every function input parameter referenced by the assistant is in the database functionality, and vice versa
"""

from env.helpers import get_action_full_description

# name of the assistant
name = "Bank Assistant"

# specific instructions for the bank assistant to follow
instructions = "You are a bank assistant that helps with processing various bank actions, as illustrated in the descriptions of functions."\
    + " You perform the duties that any bank clerk would."

# action descriptions, keeps track of which actions we have currently
action_descriptions = {
    # <function name>: <action description>
    # root functions
    "login_user":                   "Logs in the user to authenticate the user to access their account."\
        + " The identification used can either be a password or a driver's license.",
    "logout_user":                  "Logs out the user by forgetting all user-said information.",
    # account functions
    "open_account":                 "Creates and opens an account with a specified username and identification, which could be a password or driver's license.",
    "authenticate_admin_password":  "[REDACTED] that the entered admin password is correct for this account. Enables more functionality.",
    "set_admin_password":           "[REDACTED] the admin password for their account.",
    "set_account_information":      "Sets the information for their account.",
    "close_account":                "Closes the account and deletes all information in this account from the database.",
    # domain functions
    "get_account_balance":          "Retrieves the bank account balance of the user's account.",
    "transfer_funds":               "Transfers the funds from the current user's account balance to the destination account balance of another user.",
    "deposit_funds":                "Deposits the amount of funds listed into the account.",
    "pay_bill":                     "Pays a bill from an account. This amount of money will be deducted from the account.",
    "pay_bill_with_credit_card":    "Pays a bill from an account. This amount of money will be added to the credit card balance of the credit card used.",
    "apply_credit_card":            "The user applies for a credit card based on some information. ",
    "exchange_foreign_currency":    "Exchanges some USD for some specified foreign currency.",
    "get_account_owed_balance":     "Retrieves the bank account owed balance of the user's account.",
    "get_loan":                     "The user applies for a loan. Returns the amount owed to the bank.",
    "pay_loan":                     "The user pays off a portion or the entire loan off with their account balance."\
        + " The amount of money the user actually pays towards their loan is dependant on the constraints.",
    "get_safety_box":               "Gets the contents of the safety box.",
    "set_safety_box":               "Sets the contents of the safety box.",
    "get_credit_cards":             "Gets a list of the credit cards a user has along with the information.",
    "get_credit_card_info":         "Gets the information of a specific credit card."\
        + "This includes credit limit and credit balance on the card.",
    "cancel_credit_card":           "Cancels a credit card that a user has.",
    "get_bank_maximum_loan_amount": "Shows the maximum amount of money the bank can loan to any individual at this moment."\
        + " The total amount the bank can loan is based on the total amount of cash at the bank."\
        + " Total amount of cash is calculated by summing the balances of all user accounts in the full database."\
        + " If the total amount of cash currently stored at the bank is not available, assume this amount is 0.", # uses get_data method
    # internal functions
    "internal_get_database":        "Shows the full database of the entire bank, every profile and every detail."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_check_username_exist":"Returns true or false if some username does exist within the database."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_check_foreign_currency_available":"Returns true or false if the foreign currency type is available at this bank."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_get_credit_score": "Gets the credit score of a user."\
        + " This is an internal action, only the assistant should see the information from these function calls.",
    "internal_check_credit_card_exist": "Returns true or false if some credit card does exist within the database for a user."\
        + " This is an internal action, only the assistant should see the information from these function calls."
}

# return values for each action
# return value assumes strict definitions (with no guarantees before the function is called)
# some of these return values are not necessary due to previous guarantees provided by assistant dependencies (such as set_account_information if the user has previously logged in)
action_returns = {
    # <function name>: <action return>
    # root functions
    "login_user":                   "Returns true or false for login success or failure.",
    "logout_user":                  "Returns true always because of successful logout.",
    # account functions
    "open_account":                 "Returns true or false for successful account creation.",
    "authenticate_admin_password":  "[REDACTED] true or false for admin password verification.",
    "set_admin_password":           "[REDACTED] true or false for successful admin password reset.",
    "set_account_information":      "Returns true or false for successful account information reset.",
    "close_account":                "Returns true or false for successful account closing.",
    # domain functions
    "get_account_balance":          "Returns the float account balance or None if retrieval conditions are not met.",
    "transfer_funds":               "Returns true or false for the successful transfer of funds",
    "deposit_funds":                "Returns true or false on if the funds were successfully deposited.",
    "pay_bill":                     "Returns true or false on if payment was successful.",
    "pay_bill_with_credit_card":    "Returns true or false on if payment was successful.",
    "apply_credit_card":            "Returns  true or false for successful application of a credit card.",
    "cancel_credit_card":           "Returns true or false based on successful deletion of a credit card",
    "exchange_foreign_currency":    "Returns the float account of foreign currency exchanged.",
    "get_account_owed_balance":     "Returns the float account owed balance or None if retrieval conditions are not met.",
    "get_loan":                     "Returns true or false for the successful application of a loan amount.",
    "pay_loan":                     "Returns true or false for the successful payment of the loan at the amount specified or less.",
    "get_safety_box":               "Returns the contents of the safety box or None if retrieval conditions are not met.",
    "set_safety_box":               "Returns true or false for successful safety box reset.",
    "get_credit_cards":             "Returns a list of credit cards the user has.",
    "get_credit_card_info":         "Returns a dictionary of information of a credit card, including credit limit and credit balance.",
    "get_bank_maximum_loan_amount": "Returns the maximum amount of money the bank can loan at this moment.",
    
    # internal functions
    "internal_get_database":        "Returns the json of the entire database.",
    "internal_check_username_exist":"Returns true if the inputted username of the account does exist in the database.",
    "internal_check_foreign_currency_available":"Returns true if the foreign currency type is available at this bank.",
    "internal_get_credit_score": "Returns the credit score of the user.",
    "internal_check_credit_card_exist": "Returns true or false if the inputted credit card does exist under a user."

}

# innate action dependencies in the domain system itself
action_innate_dependencies = {
    # root functions
    "login_user":                   ("single", "internal_check_username_exist", {"username": "username"}),
    "logout_user":                  None,
    # account functions
    "open_account":                 None,
    "authenticate_admin_password":  [REDACTED],
    "set_admin_password":           [REDACTED],
    "set_account_information":      None,
    "close_account":                None,
    # domain functions
    "get_account_balance":          None,
    "transfer_funds":               ("single", "amount_positive_restr", {"amount": "amount"}),
    "deposit_funds":                ("single", "amount_positive_restr", {"amount": "amount"}),
    "pay_bill":                     ("single", "amount_positive_restr", {"amount": "amount"}),
    "pay_bill_with_credit_card":    ("single", "amount_positive_restr", {"amount": "amount"}),
    "apply_credit_card":            None,
    "cancel_credit_card":           ("single", "internal_check_credit_card_exist", {"username": "username", "card_number": "card_number"}),
    "exchange_foreign_currency":    None,
    "get_account_owed_balance":     None,
    "get_loan":                     None,
    "pay_loan":                     ("single", "amount_positive_restr", {"amount": "pay_owed_amount_request"}),
    "get_safety_box":               None,
    "set_safety_box":               None,
    "get_credit_cards":             None,
    "get_credit_card_info":         ("single", "internal_check_credit_card_exist", {"username": "username", "card_number": "card_number"}),
    "get_bank_maximum_loan_amount": None,
    # internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_foreign_currency_available":None,
    "internal_get_credit_score": ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_check_credit_card_exist": ("single", "internal_check_username_exist", {"username": "username"}),
}

# the required dependencies for each function, every condition must be true, should have no conflicting constraints
action_required_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  None,
    # account functions
    "open_account":                 ("single", "not internal_check_username_exist", {"username": "username"}),
    "authenticate_admin_password":  [REDACTED]"single", "logged_in_user", {"username": "username"}),
    "set_admin_password":           [REDACTED]"single", "authenticated_admin_password", {"username": "username"}),
    "set_account_information":      ("single", "logged_in_user", {"username": "username"}),
    "close_account":                ("single", "logged_in_user", {"username": "username"}),
    # domain functions
    "get_account_balance":          ("single", "internal_check_username_exist", {"username": "username"}),
    "transfer_funds":               ("and", [
                                        ("single", "internal_check_username_exist", {"username": "username"}),
                                        ("single", "internal_check_username_exist", {"username": "destination_username"})
                                    ]),
    "deposit_funds":                ("single", "internal_check_username_exist", {"username": "username"}),
    "pay_bill":                     ("single", "internal_check_username_exist", {"username": "username"}),
    "pay_bill_with_credit_card":    ("single", "internal_check_username_exist", {"username": "username"}),
    "apply_credit_card":            ("single", "internal_check_username_exist", {"username": "username"}),
    "cancel_credit_card":           ("single", "internal_check_username_exist", {"username": "username"}),
    "exchange_foreign_currency":    ("single", "internal_check_foreign_currency_available", {"foreign_currency_type": "foreign_currency_type"}),
    "get_account_owed_balance":     ("single", "internal_check_username_exist", {"username": "username"}),
    "get_loan":                     ("single", "internal_check_username_exist", {"username": "username"}),
    "pay_loan":                     ("single", "internal_check_username_exist", {"username": "username"}),
    "get_safety_box":               ("single", "internal_check_username_exist", {"username": "username"}),
    "get_credit_card_info":         ("single", "internal_check_username_exist", {"username": "username"}),
    "get_credit_cards":             ("single", "internal_check_username_exist", {"username": "username"}),
    "set_safety_box":               ("single", "internal_check_username_exist", {"username": "username"}),
    "get_bank_maximum_loan_amount": ("single", "call_get_database", None),
    # internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_foreign_currency_available":None,
    "internal_get_credit_score": None,
    "internal_check_credit_card_exist": None
}

# the customizable dependencies for each function, the conditions can be changed, order matters due to sequential data generation
action_customizable_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  ("single", "internal_check_username_exist", {"username": "username"}),
    # account functions
    "open_account":                 [
                                        ("single", "no_owed_balance", {"username": "username"}),
                                        ("single", "no_credit_card_balance", {"username": "username"}),
                                    ],
    "authenticate_admin_password":  [REDACTED],
    "set_admin_password":           [REDACTED],
    "set_account_information":      ("single", "authenticated_admin_password", {"username": "username"}),
    "close_account":                ("single", "authenticated_admin_password", {"username": "username"}),
    # domain functions
    "get_account_balance":          ("single", "logged_in_user", {"username": "username"}),
    "transfer_funds":               [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "authenticated_admin_password", {"username": "username"}),
                                        ("single", "sufficient_account_balance", {"username": "username", "amount": "amount"})
                                    ],

    "deposit_funds":                [
                                        ("single", "maximum_deposit_limit", {"unit":"unit", "amount":"amount"}),
                                        ("single", "logged_in_user", {"username": "username"}),
                                    ],
    "pay_bill":                     [
                                        ("single", "sufficient_account_balance", {"username": "username", "amount": "amount"}),
                                        ("single", "logged_in_user", {"username": "username"}),
                                    ],

    "pay_bill_with_credit_card":    [
                                        ("single", "not_over_credit_limit", {"username": "username", "amount": "amount", "card_number": "card_number"}),
                                        ("single", "logged_in_user", {"username": "username"}),
                                    ],
    "apply_credit_card":            [
                                        ("single", "minimal_elgibile_credit_score", {"username": "username"}),
                                        ("single", "logged_in_user", {"username": "username"}),
                                    ],
    "cancel_credit_card":           [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "authenticated_admin_password", {"username": "username"}), 
                                        ("single", "no_credit_card_balance_on_card", {"username": "username", "card_number": "card_number"}),
                                    ],
    "exchange_foreign_currency":    ("single", "maximum_exchange_amount", {"amount": "amount", "unit": "unit"}),
    "get_account_owed_balance":     ("single", "logged_in_user", {"username": "username"}),
    "get_loan":                     [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "get_loan_owed_balance_restr", {"username": "username"}),
                                        ("single", "minimal_elgibile_credit_score", {"username": "username"})
                                    ],
    "pay_loan":                     [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("or", [
                                            ("single", "pay_loan_account_balance_restr", {"username": "username"}),
                                            ("single", "pay_loan_amount_restr", {"username": "username", "pay_owed_amount_request": "pay_owed_amount_request"}),
                                        ])
                                    ],
    "get_credit_card_info":         ("single", "logged_in_user", {"username": "username"}),
    "get_safety_box":               [
                                        ("single", "authenticated_admin_password", {"username": "username"}),
                                        ("single", "logged_in_user", {"username": "username"}),
                                    ],
    "set_safety_box":               [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "authenticated_admin_password", {"username": "username"}),
                                        ("single", "safety_box_eligible", {"username": "username"}),
                                        ("single", "minimal_elgibile_credit_score", {"username": "username"})
                                    ],
    "get_credit_cards":             [
                                        ("single", "authenticated_admin_password", {"username": "username"}),
                                        ("single", "logged_in_user", {"username": "username"}),
                                    ],
    "get_bank_maximum_loan_amount": None,
    # internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_foreign_currency_available":None,
    "internal_get_credit_score": None,
    "internal_check_credit_card_exist": None
}

# all dependency types that could be in a action, each returns true or false
positive_constraint_descriptions = {
    # state tracker constraints
    "logged_in_user":               "The user with username {username} is logged in previously with the correct credentials to perform this action.",
    "authenticated_admin_password": "[REDACTED] user with username {username} has authenticated the admin password previously to perform this action.",
    "sufficient_account_balance":   "The user does have more account balance \"balance\" than the"\
        + " task amount user parameter \"{amount}\" to perform this task.",
    "get_loan_owed_balance_restr":  "The user with the parameter \"{username}\" does have owed balance less than {maximum_owed_balance} to take a loan.",
    "pay_loan_account_balance_restr":"The user \"{username}\" has an account balance \"balance\""\
        + " that is **equal to or greater than >=** their owed balance \"owed_balance\".",
    "pay_loan_amount_restr":        "The user \"{username}\" has an account balance \"balance\""\
        + " that is **equal to or greater than >=** the requested owed balance payment \"{pay_owed_amount_request}\"",
    "amount_positive_restr":        "The user parameter key \"{amount}\" is more than zero.",
    "minimal_elgibile_credit_score": "The user \"{username}\" **must have** a credit score higher than the {minimum_credit_score} credit score in order to proceed.",
    "no_owed_balance":               "The user \"{username}\" **must not have** any outstanding owed balance \"owed_balance\" in their account to proceed.",
    "no_credit_card_balance":        "The user \"{username}\" **must not have** any outstanding balance on any of their credit cards to proceed.",
    "no_credit_card_balance_on_card":"The user \"{username}\" **must not have** outstanding balance on credit card of \"{card_number}\" to proceed.",
    "safety_box_eligible":           "The user \"{username}\" must have an account balance of at least {minimum_account_balance_safety_box} to be eligible for a safety deposit box.",
    "maximum_deposit_limit":         "The deposit amount \"{amount}\" must be less than or equal to the {maximum_deposit} to be accepted.",
    "maximum_exchange_amount":       "The exchange amount \"{amount}\" must be less than or equal to the {maximum_exchange}",
    "not_over_credit_limit":         "The amount \"{amount}\" must be less than or equal to the avliable credit of credit card \"{card_number}\","\
        + " avaliable credit is defined as the credit limit subtracted from the credit balance.",
    # domain system constraints
    "login_user":                   "The user is able to login with the correct credentials of \"{username}\" and \"{identification}\" to perform this action,"\
        + " matching the database credentials.",
    "authenticate_admin_password":  "[REDACTED] user is able to authenticate the correct \"{username}\" and \"{admin_password}\" to perform this action,"\
        + " matching the database credentials.",
    "internal_check_username_exist":"The user parameter key \"{username}\" must exist within the initial existing database of accounts."\
        + " The users with accounts exist within the accounts section of the initial database.",
    "internal_check_foreign_currency_available":"The user parameter \"{foreign_currency_type}\""\
        + " must exist within the database foreign exchange types.",
    "internal_check_credit_card_exist": "The credit card parameter key \"{card_number}\" must exist within the users credit cards section.",
    # call constraints
    "call_get_database":            "You must base your considerations on the database as a whole.",
}

# all dependency types that could be in a action, each returns true or false
negative_constraint_descriptions = {
    # state tracker constraints
    "logged_in_user":               "The user with username {username} **must not be logged in previously with the correct credentials** to perform this action.",
    "authenticated_admin_password": "[REDACTED] user with username {username} **must not have authenticated** the admin password previously to perform this action.",
    "sufficient_account_balance":   "The user's account balance \"balance\" **must be STRICTLY LESS THAN <** the task amount user-known parameter \"{amount}\".",
    "get_loan_owed_balance_restr":  "The user with the parameter \"{username}\" **must have an owed balance more than {maximum_owed_balance}**.",
    "pay_loan_account_balance_restr":"The user \"{username}\" has an account balance \"balance\""\
        + " that is **STRICTLY LESS THAN <** their owed balance \"owed_balance\".",
    "pay_loan_amount_restr":        "The user \"{username}\" has an account balance \"balance\""\
        + " that is **STRICTLY LESS THAN <** the requested payment amount \"{pay_owed_amount_request}\"",
    "amount_positive_restr":        "The user parameter key \"{amount}\" **must be zero or less**.",
    "minimal_elgibile_credit_score": "The user \"{username}\" **must not have** a credit score higher than the {minimum_credit_score} credit score in order to proceed.",
    "no_owed_balance":               "The user \"{username}\" **must have** any outstanding owed balance \"owed_balance\" in their account to proceed.",
    "no_credit_card_balance":        "The user \"{username}\" **must have** any outstanding balance on any of their credit cards to proceed.",
    "no_credit_card_balance_on_card":"The user \"{username}\" **must have** outstanding balance on credit card of \"{card_number}\" to proceed.",
    "safety_box_eligible":           "The user \"{username}\" must not have an account balance of at least {minimum_account_balance_safety_box} to be eligible for a safety deposit box.",
    "maximum_deposit_limit":         "The deposit amount \"{amount}\" must be greater than {maximum_deposit} to be accepted.",
    "maximum_exchange_amount":       "The exchange amount \"{amount}\" must be greater than the {maximum_exchange}",
    "not_over_credit_limit":         "The amount \"{amount}\" must be greater than the avliable credit of credit card \"{card_number}\","\
        + " avaliable credit is defined as the credit limit subtracted from the credit balance.",
    # domain system constraints
    "login_user":                   "The user **must not be able to login** with the correct credentials of \"{username}\" and \"{identification}\" to perform this action,"\
        + " **not matching** the database credentials.",
    "authenticate_admin_password":  "[REDACTED] user **must not** authenticate the correct \"{username}\" and \"{admin_password}\" to perform this action,"\
        + " **not matching** the database credentials.",
    "internal_check_username_exist":"The user-known \"{username}\" **MUST NOT EXIST** within the initial existing database of accounts.",
    "internal_check_foreign_currency_available":"The user parameter \"{foreign_currency_type}\" is real-world foreign currency type"\
        + " that **IS NOT INCLUDED** in the database foreign exchange types.",
    "internal_check_credit_card_exist": "The credit card parameter key \"{card_number}\" must not exist within the users credit cards section.",
    # call constraints
    "call_get_database":            "You must not base your considerations on the database as a whole.",
}

# links the dependency to the action that changes its state in the state tracker, should be one to one
constraint_links = {
    "logged_in_user":               ("login_user", {"username": "username"}),
    "authenticated_admin_password": [REDACTED]"authenticate_admin_password", {"username": "username"}),
}

# dependencies of the constraints not in the action dependencies, mutually exclusive with the actions
constraint_dependencies = {
    # state tracker constraints
    "sufficient_account_balance":               ("single", "internal_check_username_exist", {"username": "username"}),
    "get_loan_owed_balance_restr":              ("single", "internal_check_username_exist", {"username": "username"}),
    "pay_loan_account_balance_restr":           ("single", "internal_check_username_exist", {"username": "username"}),
    "pay_loan_amount_restr":                    ("single", "internal_check_username_exist", {"username": "username"}),
    "minimal_elgibile_credit_score":            ("single", "internal_check_username_exist", {"username": "username"}),
    "no_owed_balance":                          ("single", "internal_check_username_exist", {"username": "username"}),
    "no_credit_card_balance":                   ("single", "internal_check_username_exist", {"username": "username"}),
    "no_credit_card_balance_on_card":           ("single", "internal_check_credit_card_exist", {"username": "username", "card_number": "card_number"}),
    "safety_box_eligible":                      ("single", "internal_check_username_exist", {"username": "username"}),
    "not_over_credit_limit":                    ("single", "internal_check_username_exist", {"username": "username"}),
    "maximum_deposit_limit":                    None,
    "maximum_exchange_amount":                  None,
    "amount_positive_restr":                    None,
    "call_get_database":                        None,

}



# full list of actions the assistant needs to call to successfully verify the constraint, mutually exclusive with constraint_links
constraint_processes = {
    "sufficient_account_balance":       ("or", [
                                            ("single", "get_account_balance", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "get_loan_owed_balance_restr":      ("or", [
                                            ("single", "get_account_owed_balance", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "pay_loan_account_balance_restr":   ("or", [
                                            ("and", [
                                                ("single", "get_account_balance", {"username": "username"}),
                                                ("single", "get_account_owed_balance", {"username": "username"})
                                            ]),
                                            ("single", "internal_get_database", None)
                                        ]),
    "pay_loan_amount_restr":            ("or", [
                                            ("single", "get_account_balance", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "minimal_elgibile_credit_score": ("or", [
                                            ("single", "internal_get_credit_score", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "no_owed_balance":               ("or", [
                                            ("single", "get_account_owed_balance", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "no_credit_card_balance":        ("or", [
                                            ("single", "get_credit_cards", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                    ]),
    "no_credit_card_balance_on_card":("or", [
                                            ("single", "get_credit_card_info", {"username": "username", "card_number": "card_number"}),
                                            ("single", "get_credit_cards", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                    ]),

    "safety_box_eligible":          ("or", [
                                            ("single", "get_account_balance", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                    ]),
    "maximum_deposit_limit":        None,
    "maximum_exchange_amount":      None,
    "not_over_credit_limit":        ("or",  [
                                        ("single", "get_credit_card_info", {"username": "username", "card_number": "card_number"}),
                                        ("single", "get_credit_cards", {"username": "username"}),
                                        ("single", "internal_get_database", None)
                                    ]),

    "internal_check_username_exist":    ("or", [
                                            ("single", "internal_check_username_exist", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "internal_check_foreign_currency_available":("or", [
                                            ("single", "internal_check_foreign_currency_available", {"foreign_currency_type": "foreign_currency_type"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "internal_check_credit_card_exist": ("or",  [
                                            ("single", "internal_check_credit_card_exist", {"username": "username", "card_number": "card_number"}),
                                            ("single", "get_credit_card_info", {"username": "username", "card_number": "card_number"}),
                                            ("single", "get_credit_cards", {"username": "username"}),
                                            ("single", "internal_get_database", None)
                                        ]),
    "amount_positive_restr":            None,
    "call_get_database":                ("single", "internal_get_database", None)
}

# method parameters may have parameters that do not go into user_known because they should be filled by the assistant
action_params_user_not_needed = {
    "get_bank_maximum_loan_amount": ["bank_total_cash"]
}

# descriptions of parameters in the funcitons and actions
action_param_descriptions = {
    "username":             "a string of letters, numbers, and symbols to represent their username",
    "identification":       ["the password to their account", "the driver's license of the user"],
    "drivers_license_id":   "the state the driver's license is registered in",
    "drivers_license_state":"the state the driver's license is registered in",
    "admin_password":       "[REDACTED] admin password of the user's account to access additional functionalities in their account.",
    "admin_password_new":   "The new admin password of the user's account that the user set.",
    "username_new":         "The new username of the user's account.",
    "identification_new":   ["the new password to their account", "the new driver's license of the user"],
    "destination_username": "the username of the destination account",
    "amount":               "the amount of funds specified by the function description",
    "unit":                 "the unit of money dollar, cent, dollars, or cents",
    "deposit_form":         ["a string description of what form the deposit is used, usually cash", "deposit form of a check"],
    "check_name":           "the owner name of the account the check is written from",
    "check_routing_number": "the routing number of the account the check is made out from",
    "bill_description":     "The description of the what bill is being paid.",
    "total_assets":         "The applicant's total assets. This determines the eligibility for the credit card",
    "monthly_income":       "The applicant's monthly income. This determines the spending limit for this credit card.",
    "foreign_currency_type":"The foreign currency type the customer wants to change to.",
    "loan_amount":          "Amount of money the user wants to loan.",
    "pay_owed_amount_request":"Amount of money the user wants use to pay off their loan, owed balance.",
    "safety_box_new":       "the new contents of the safety box",
    "card_number":          "the card number of a specific card in the database",
    "bank_total_cash":      "the total amount of cash at the bank",
}

# actions the assistant can take
actions = [
# root functions
{
    "name": "login_user",
    "description": get_action_full_description(action_descriptions, action_returns, "login_user"),
    "strict": False,
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
                    "required": [
                        "drivers_license_id",
                        "drivers_license_state"
                    ]
                }
                ]
            }
        },
        "additionalProperties": False,
        "required": [
            "username",
            "identification"
        ]
    }
},
{
    "name": "logout_user",
    "description": get_action_full_description(action_descriptions, action_returns, "logout_user"),
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
# account functions
{
    "name": "open_account",
    "description": get_action_full_description(action_descriptions, action_returns, "open_account"),
    "strict": False,
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
                    "required": [
                        "drivers_license_id",
                        "drivers_license_state"
                    ]
                }
                ]
            },
            "admin_password": [REDACTED]
                "type": "string",
                "description": action_param_descriptions["admin_password"]
            }
        },
        "additionalProperties": False,
        "required": [
            "username",
            "identification",
            "admin_password"
        ]
    }
},
{
    "name": "authenticate_admin_password",
    "description": get_action_full_description(action_descriptions, action_returns, "authenticate_admin_password"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "admin_password": [REDACTED]
                "type": "string",
                "description": action_param_descriptions["admin_password"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "admin_password"]
    }
},
{
    "name": "set_admin_password",
    "description": get_action_full_description(action_descriptions, action_returns, "set_admin_password"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "admin_password_new": {
                "type": "string",
                "description": action_param_descriptions["admin_password_new"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "admin_password_new"]
    }
},
{
    "name": "set_account_information",
    "description": get_action_full_description(action_descriptions, action_returns, "set_account_information"),
    "strict": False,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "username_new": {
                "type": "string",
                "description": action_param_descriptions["username_new"]
            },
            "identification_new": {
                "anyOf": [
                {
                    "type": "string",
                    "description": action_param_descriptions["identification_new"][0]
                },
                {
                    "type": "object",
                    "description": action_param_descriptions["identification_new"][1],
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
                    "required": [
                        "drivers_license_id",
                        "drivers_license_state"
                    ]
                }
                ]
            }
        },
        "additionalProperties": False,
        "required": ["username", "username_new", "identification_new"]
    }
},
{
    "name": "close_account",
    "description": get_action_full_description(action_descriptions, action_returns, "close_account"),
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
# domain functions
{
    "name": "get_account_balance",
    "description": get_action_full_description(action_descriptions, action_returns, "get_account_balance"),
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
    "name": "transfer_funds",
    "description": get_action_full_description(action_descriptions, action_returns, "transfer_funds"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "destination_username": {
                "type": "string",
                "description": action_param_descriptions["destination_username"]
            },
            "amount": {
                "type": "number",
                "description": action_param_descriptions["amount"]
            },
            "unit": {
                "type": "string",
                "description": action_param_descriptions["unit"],
                "enum": ["dollar", "cent", "dollars", "cents"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "destination_username", "amount", "unit"]
    }
},
{
    "name": "deposit_funds",
    "description": get_action_full_description(action_descriptions, action_returns, "deposit_funds"),
    "strict": True,
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
            "unit": {
                "type": "string",
                "description": action_param_descriptions["unit"],
                "enum": ["dollar", "cent", "dollars", "cents"]
            },
            "deposit_form": {
                "anyOf": [
                {
                    "type": "string",
                    "description": action_param_descriptions["deposit_form"][0]
                },
                {
                    "type": "object",
                    "description": action_param_descriptions["deposit_form"][1],
                    "properties": {
                        "check_name": {
                            "type": "string",
                            "description": action_param_descriptions["check_name"]
                        },
                        "check_routing_number": {
                            "type": "number",
                            "description": action_param_descriptions["check_routing_number"]
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "check_name",
                        "check_routing_number"
                    ]
                }
                ]
            }
        },
        "additionalProperties": False,
        "required": ["username", "amount", "unit", "deposit_form"]
    }
},
{
    "name": "pay_bill",
    "description": get_action_full_description(action_descriptions, action_returns, "pay_bill"),
    "strict": False,
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
            "unit": {
                "type": "string",
                "description": action_param_descriptions["unit"],
                "enum": ["dollar", "cent", "dollars", "cents"]
            },
            "bill_description": {
                "type": "string",
                "description": action_param_descriptions["bill_description"]
            }
        },
        "additionalProperties": True,
        "required": ["username", "amount", "unit"]
    }
},
{
    "name": "apply_credit_card",
    "description": get_action_full_description(action_descriptions, action_returns, "apply_credit_card"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "total_assets": {
                "type": "number",
                "description": action_param_descriptions["total_assets"]
            },
            "monthly_income": {
                "type": "number",
                "description": action_param_descriptions["monthly_income"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "total_assets", "monthly_income"]
    }
},
{
    "name": "exchange_foreign_currency",
    "description": get_action_full_description(action_descriptions, action_returns, "exchange_foreign_currency"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "amount": {
                "type": "number",
                "description": action_param_descriptions["amount"]
            },
            "unit": {
                "type": "string",
                "description": action_param_descriptions["unit"],
                "enum": ["dollar", "cent", "dollars", "cents"]
            },
            "foreign_currency_type": {
                "type": "string",
                "description": action_param_descriptions["foreign_currency_type"]
            }
        },
        "additionalProperties": False,
        "required": ["amount", "unit", "foreign_currency_type"]
    }
},
{
    "name": "get_account_owed_balance",
    "description": get_action_full_description(action_descriptions, action_returns, "get_account_owed_balance"),
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
    "name": "get_loan",
    "description": get_action_full_description(action_descriptions, action_returns, "get_loan"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "loan_amount": {
                "type": "number",
                "description": action_param_descriptions["loan_amount"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "loan_amount"]
    }
},
{
    "name": "pay_loan",
    "description": get_action_full_description(action_descriptions, action_returns, "pay_loan"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "pay_owed_amount_request": {
                "type": "number",
                "description": action_param_descriptions["pay_owed_amount_request"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "pay_owed_amount_request"]
    }
},
{
    "name": "get_safety_box",
    "description": get_action_full_description(action_descriptions, action_returns, "get_safety_box"),
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
    "name": "set_safety_box",
    "description": get_action_full_description(action_descriptions, action_returns, "set_safety_box"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "safety_box_new": {
                "type": "string",
                "description": action_param_descriptions["safety_box_new"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "safety_box_new"]
    }
},
{
    "name": "get_credit_cards",
    "description": get_action_full_description(action_descriptions, action_returns, "get_credit_cards"),
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
    "name": "get_credit_card_info",
    "description": get_action_full_description(action_descriptions, action_returns, "get_credit_card_info"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "card_number": {
                "type": "string",
                "description": action_param_descriptions["card_number"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "card_number"]
    }
},
{
    "name": "get_bank_maximum_loan_amount",
    "description": get_action_full_description(action_descriptions, action_returns, "get_bank_maximum_loan_amount"),
    "strict": False,
    "parameters": {
        "type": "object",
        "properties": {
            "bank_total_cash": {
                "type": "number",
                "description": action_param_descriptions["bank_total_cash"]
            }
        },
        "additionalProperties": True,
        "required": []
    }
},
# internal functions
{
    "name": "internal_get_database",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_database"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {},
        "additionalProperties": False,
        "required": []
    }
},
{
    "name": "internal_check_username_exist",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_username_exist"),
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
    "name": "internal_check_foreign_currency_available",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_foreign_currency_available"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "foreign_currency_type": {
                "type": "string",
                "description": action_param_descriptions["foreign_currency_type"]
            }
        },
        "additionalProperties": False,
        "required": ["foreign_currency_type"]
    }
},
{
    "name": "internal_get_credit_score",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_credit_score"),
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
    "name": "internal_check_credit_card_exist",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_credit_card_exist"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "card_number": {
                "type": "string",
                "description": action_param_descriptions["card_number"]
            }
        },
        "additionalProperties": False,
        "required": ["username","card_number"]
    }
},
]
