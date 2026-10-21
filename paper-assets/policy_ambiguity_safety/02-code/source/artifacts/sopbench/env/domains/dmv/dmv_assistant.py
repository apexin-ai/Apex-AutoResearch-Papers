"""
This file contains the information for the dmv assistant fo the openai API.
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
name = "DMV Assistant"

# specific instructions for the dmv assistant to follow
instructions = "You are a dmv assistant that helps with processing various dmv actions, as illustrated in the descriptions of functions."\
    + " You perform the duties that any dmv agent would."

# action descriptions, keeps track of which actions we have currently
action_descriptions = {
    # root functions
    "login_user":                   "Logs in the user to authenticate the user to access their account.",
    "logout_user":                  "Logs out the user if the user was previously logged in.",
    # account functions
    "authenticate_admin_password":  "[REDACTED] that the entered admin password is correct for this account. Enables more functionality.",
    "set_admin_password":           "[REDACTED] the admin password for their account.",
    # domain functions
    "register_vehicle":             "Registers the vehicle with the specfied plate number to the user.",
    "get_reg_status":               "Gets the registration status of a specific vehicle.",
    "change_vehicle_address":       "Changes the address associated with the specified vehicle.",
    "validate_vehicle_insurance":   "Validates the user's specified vehicle's insurance status.",
    "renew_vehicle":                "Renews the registration of the specified vehicle.",
    "get_dl_status":                "Retrieves the status of the user's driver's license.",
    "update_dl_legal_name":         "Updates the user's name on the driver's license.",
    "change_dl_address":            "Updates the address associated with the user's driver's license.",
    "renew_dl":                     "Renews the user's driver's license.",
    "show_available_test_slots":    "Shows available test slots for the specified test_type.",
    "schedule_test":                "Schedules a knowledge or driving test for the user at the expected date and time.",
    "cancel_test":                  "Cancels a knowledge or driving test for the user.",
    "update_test_status":           "Marks the status of a scheduled test as passed or not based on user's input."\
                                    + "Issues a driver's license if the user passed the drive test",
    "transfer_title":               "Transfers a vehicle's title from one owner to another.",
    # internal functions
    "internal_get_database":                "Shows the full database of the DMV system, including all profiles and details.",
    "internal_check_username_exist":        "Checks if a specific username exists in the DMV database.",
    "internal_get_user_birthday":           "Retrieves the user's birthday.",
    "internal_has_vehicle":                 "Checks if a specific vehicle belongs to the user given a plate number.",
    "internal_vehicle_registered":          "Checks if a specified plate number has been registered by any user in the database.",
    "internal_get_vehicle_details":         "Retrieves the details of the user's specified vehicle, "\
                                            + "including its model name, vin, registration date, registered address, and associated insurance status.", 
    "internal_has_dl":                      "Checks if the user has a driver's license.",
    "internal_get_dl_details":              "Retrieves the details of the user's driver's license, "\
                                            + "including the dl number, legal name, expiration date, and address.", 
    "internal_valid_test_type":             "Checks if the input test type is valid.",
    "internal_check_test_slot_available":   "Checks if a specific test slot is available for the desired test type and time.",
    "internal_get_test_details":            "Retrieves the user's details of the specified test, "\
                                            + "including its status, scheduled time if any, and the number of attempts they made for the test.",
    "internal_get_interaction_time":        "Retrieves the  current interaction timestamp recorded in the database."
}

# return values for each action
# return value assumes strict definitions (with no guarantees before the function is called)
# some of these return values are not necessary due to previous guarantees provided by assistant dependencies
action_returns = {
    # <function name>: <action return>
    # root functions
    "login_user":                   "Returns true or false for login success or failure.",
    "logout_user":                  "Returns true always because of successful logout.",
    # account functions
    "authenticate_admin_password":  "[REDACTED] true or false for admin password verification.",
    "set_admin_password":           "[REDACTED] true or false for successful admin password reset.",
    # domain functions
    "register_vehicle":             "Returns true or false for successful vehicle registration.",
    "get_reg_status":               "Returns the registration renewal date for the specified vehicle or None if retrieval conditions are not met.",
    "change_vehicle_address":       "Returns true or false for successful change of the address asspciated with the specified vehicle.",
    "validate_vehicle_insurance":   "Returns true or false for successful vehicle insurance validation.",
    "renew_vehicle":                "Returns the vehicles's new renewal date or None if renewal conditions are not met.",
    "get_dl_status":                "Returns the expiration date of the user's driver's license or None if retrieval conditions are not met.",
    "update_dl_legal_name":         "Returns true or false for successful update of the driver's license owner information.",
    "change_dl_address":            "Returns true or false for successful change of the address associated with the driver's license.",
    "renew_dl":                     "Returns the new expiration date of the driver's license or None if the renewal condtions are not met.",
    "show_available_test_slots":    "Returns the available test slots for the specified test_type.",
    "schedule_test":                "Returns true or false for successfully scheduling the specified test at the expected date and time.",
    "cancel_test":                  "Returns true or false for successfully canceling the specified test",
    "update_test_status":           "Returns true or false for successfully updating the status of a scheduled test",
    "transfer_title":               "Returns true or false for successful title transfer from the current owner to the new owner.",
    # internal functions
    "internal_get_database":                "Returns the json of the entire database.",
    "internal_check_username_exist":        "Returns true or false based on the condition that the inputted username exists in the database.",
    "internal_get_user_birthday":           "Returns the datatime object representing the user's birthday.",
    "internal_has_vehicle":                 "Returns true or false based on the user's ownership of the specified vehicle.",
    "internal_vehicle_registered":          "Returns true or false based on whether the specified plate number has been registered by any user in the database.",
    "internal_get_vehicle_details":         "Returns the dicitonary with the user's specified vehicle, "\
                                            + "including its model name, vin, registration date, registered address, and associated insurance status.", 
    "internal_has_dl":                      "Returns true or false based on the user's possession of the driver's license.",
    "internal_get_dl_details":              "Returns the dictionary with details of the user's driver's license, "\
                                            + "including the dl number, legal name, expiration date, and address.", 
    "internal_valid_test_type":             "Returns true or false based on the validity of the input test type.",
    "internal_check_test_slot_available":   "Returns true or false based on the availability of the specified test at the expected date and time in the database.",
    "internal_get_test_details":            "Returns a dictionary with the user's details of the specified test, "\
                                            + "including its status, scheduled time if any, and the number of attempts they made for the test.",
    "internal_get_interaction_time":        "Returns the interaction timestamp."
}

# innate action dependencies in the domain system itself
action_innate_dependencies = {
    # root functions
    "login_user":                   ("single", "internal_check_username_exist", {"username": "username"}),
    "logout_user":                  None,
    # account functions
    "authenticate_admin_password":  [REDACTED],
    "set_admin_password":           [REDACTED],
    # domain functions
    "register_vehicle":             None,
    "get_reg_status":               None,
    "change_vehicle_address":       None,
    "validate_vehicle_insurance":   None,
    "renew_vehicle":                None,
    "get_dl_status":                None,
    "update_dl_legal_name":         None,
    "change_dl_address":            None,
    "renew_dl":                     None,
    "show_available_test_slots":    ("single", "internal_valid_test_type", {"test_type": "test_type"}),
    "schedule_test":                ("single", "internal_valid_test_type", {"test_type": "test_type"}),
    "cancel_test":                  ("single", "internal_valid_test_type", {"test_type": "test_type"}),
    "update_test_status":           ("single", "internal_valid_test_type", {"test_type": "test_type"}),
    "transfer_title":               None,
    # internal functions
    "internal_get_database":                None,
    "internal_check_username_exist":        None,
    "internal_get_user_birthday":           ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_has_vehicle":                 ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_vehicle_registered":          None,
    "internal_get_vehicle_details":         ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
    "internal_has_dl":                      ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_get_dl_details":              ("single", "internal_has_dl", {"username": "username"}),
    "internal_valid_test_type":             None,
    "internal_check_test_slot_available":   ("single", "internal_valid_test_type", {"test_type": "test_type"}),
    "internal_get_test_details":            ("and", [
                                                ("single", "internal_check_username_exist", {"username": "username"}),
                                                ("single", "internal_valid_test_type", {"test_type": "test_type"})
                                            ]),
    "internal_get_interaction_time":        None
}

# the required dependencies for each function, every condition must be true
action_required_dependencies = {
    # root functions
    "login_user":                   None,   
    "logout_user":                  ("single", "logged_in_user", {"username": "username"}),
    # account functions
    "authenticate_admin_password":  [REDACTED]"single", "logged_in_user", {"username": "username"}),
    "set_admin_password":           [REDACTED]"single", "authenticated_admin_password", {"username": "username"}),
    # domain functions
    "register_vehicle":             ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "not internal_vehicle_registered", {"plate_num": "plate_num"})
                                    ]),
    "get_reg_status":               ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
    "change_vehicle_address":       ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
    "validate_vehicle_insurance":   ("chain", [
                                        ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
                                        ("single", "not valid_vehicle_insurance", {"username": "username", "plate_num": "plate_num"}),
                                    ]),
    "renew_vehicle":                ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
    "get_dl_status":                ("single", "internal_has_dl", {"username": "username"}),
    "update_dl_legal_name":         ("single", "internal_has_dl", {"username": "username"}),
    "change_dl_address":            ("single", "internal_has_dl", {"username": "username"}),
    "renew_dl":                     ("single", "internal_has_dl", {"username": "username"}),
    "show_available_test_slots":    None,
    "schedule_test":                ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_test_slot_available", {"test_type": "test_type", "schedule_time":"schedule_time"})
                                    ]),
    "cancel_test":                  ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "test_scheduled", {"username": "username", "test_type": "test_type"})
                                    ]),
    "update_test_status":           ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "test_scheduled", {"username": "username", "test_type": "test_type"}),
                                    ]),
    "transfer_title":               ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_username_exist", {"username": "target_owner"}),
                                        ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"})
                                    ]),
    # internal functions
    "internal_get_database":                None,
    "internal_check_username_exist":        None,
    "internal_get_user_birthday":           None,
    "internal_has_vehicle":                 None,
    "internal_vehicle_registered":          None,
    "internal_get_vehicle_details":         None,
    "internal_has_dl":                      None,
    "internal_get_dl_details":              None,
    "internal_valid_test_type":             None,
    "internal_check_test_slot_available":   None,
    "internal_get_test_details":            None,
    "internal_get_interaction_time":        None
}

# the customizable dependencies for each function, the conditions can be changed, order matters due to sequential data generation
action_customizable_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  None,
    # account functions
    "authenticate_admin_password":  [REDACTED],
    "set_admin_password":           [REDACTED],
    # domain functions
    "register_vehicle":             ("single", "internal_has_dl", {"username": "username"}),
    "get_reg_status":               ("single", "logged_in_user", {"username": "username"}),
    "change_vehicle_address":       [("single", "logged_in_user", {"username": "username"}),
                                     ("single", "is_vehicle_address_different", {"username":"username", "plate_num":"plate_num", "address_new": "address_new"})],
    "validate_vehicle_insurance":   [("single", "logged_in_user", {"username": "username"}),
                                     ("single", "internal_has_dl", {"username": "username"})],
    "renew_vehicle":                [("single", "logged_in_user", {"username": "username"}),
                                    ("single", "valid_vehicle_insurance", {"username": "username", "plate_num": "plate_num"}),
                                    ("single", "within_vehicle_renewal_period", {"username": "username", "plate_num": "plate_num"}),],
    "get_dl_status":                ("single", "logged_in_user", {"username": "username"}),
    "update_dl_legal_name":         ("single", "logged_in_user", {"username": "username"}),
    "change_dl_address":            [("single", "logged_in_user", {"username": "username"}),
                                     ("single", "is_dl_address_different", {"username":"username", "address_new": "address_new"})],
    "renew_dl":                     [("single", "logged_in_user", {"username": "username"}),
                                    ("single", "within_dl_renewal_period", {"username": "username"})],  
    "show_available_test_slots":    ("single", "logged_in_user", {"username": "username"}),
    "schedule_test":                [("and", [
                                        ("or", [
                                            ("and", [
                                                ("single", "test_type_is_drive", {"test_type": "test_type"}),
                                                ("single", "drive_test_ready", {"username": "username"})
                                            ]),
                                            ("and", [
                                                ("single", "not test_type_is_drive", {"test_type": "test_type"}),
                                                ("single", "not drive_test_ready", {"username": "username"})
                                            ]),
                                        ]),
                                        ("single", "above_minimum_age", {"username": "username"})
                                    ]),
                                    ("single", "within_attempt_limit", {"username": "username", "test_type": "test_type"})],
    "cancel_test":                  [("single", "before_test_date", {"username": "username", "test_type": "test_type"})], 
    "update_test_status":           [("single", "not before_test_date", {"username": "username", "test_type": "test_type"})],
    "transfer_title":               [("single", "internal_has_dl", {"username": "username"}),
                                    ("single", "internal_has_dl", {"username": "target_owner"})],
    # internal functions
    "internal_get_database":                None,
    "internal_check_username_exist":        None,
    "internal_get_user_birthday":           None,
    "internal_has_vehicle":                 None,
    "internal_vehicle_registered":          None,
    "internal_get_vehicle_details":         None,
    "internal_has_dl":                      None,
    "internal_get_dl_details":              None,
    "internal_valid_test_type":             None,
    "internal_check_test_slot_available":   None,
    "internal_get_test_details":            None,
    "internal_get_interaction_time":        None
}

# all dependency types that could be in a action, each returns true or false
positive_constraint_descriptions = {
    "login_user":                           "The user \"{username}\" is able to login with the correct \"{identification}\" to perform this action, matching the database credentials.",
    "authenticate_admin_password":          "[REDACTED] user is able to authenticate the correct \"{username}\" and \"{admin_password}\" to perform this action,"\
                                            + " matching the database credentials.",
    "internal_check_username_exist":        "The user parameter key \"{username}\" **MUST EXIST** as a top-level key in the accounts section of the database.",
    "internal_has_vehicle":                 "The user with \"{username}\" owns the vehicle with the plate number \"{plate_num}\" in their vehicles.",
    "internal_vehicle_registered":          "The vehicle with the plate number \"{plate_num}\" is registed under one user's 'vehicles' in the database." ,  
    "internal_has_dl":                      "The user with \"{username}\" has a driver_license that is not null in their account.",
    "internal_valid_test_type":             "The input test type \"{test_type}\" is valid (either 'knowledge' or 'drive').",
    "internal_check_test_slot_available":   "The specified \"{schedule_time}\" exists only in the \"{test_type}\" of test_slots. "\
                                            + "If it exists elsewhere in the databse, it is consided **NON-EXISTENT**." ,
    # state tracker constraints
    "logged_in_user":                       "The user with \"{username}\" is logged in previously with the correct credentials to perform this action.",
    "authenticated_admin_password":         "[REDACTED] user with \"{username}\" has authenticated the admin password previously to perform this action.",
    "is_vehicle_address_different":         "The vehicle with the plate number \"{plate_num}\" belonging to the user \"{username}\" must have an address different from \"{address_new}\".",
    "valid_vehicle_insurance":              "The vehicle with the plate number \"{plate_num}\" belonging to the user \"{username}\" must have an insurance_status of 'valid'.",
    "within_vehicle_renewal_period":        "The interaction_time falls within the vehicle renewal period for the vehicle with \"{plate_num}\" of the user \"{username}\". "\
                                            + "The renewal period is defined as the time starting {vehicle_renewal_window} days before the reg_date and ending on the reg_date itself. "\
                                            + "Both interaction_time and reg_date are ISO 8601 formatted strings and are considered as date-time values.",
    "is_dl_address_different":              "The driver license of the user \"{username}\" must have an address different from \"{address_new}\".",
    "within_dl_renewal_period":             "The interaction_time falls within the driver_license renewal period for the user \"{username}\". "\
                                            + "The renewal period is defined as the time starting {dl_renewal_window} days before the exp_date and ending on the expiration date itself. "\
                                            + "Both interaction_time and exp_date are ISO 8601 formatted strings and are considered as date-time values.",
    "above_minimum_age":                    "The user with \"{username}\" must be above the minimum age of {min_age}. "\
                                            + "The age should be determined as per interaction_time.",
    "test_type_is_drive":                   "The input test type \"{test_type}\" must be 'drive'.",
    "drive_test_ready":                     "The user with \"{username}\" must have passed the knowledge test and must have a status of \"not scheduled\" in \"drive\" of their tests.",
    "test_scheduled":                       "The user with \"{username}\" has their test status set to 'scheduled' and has a corersponding scheduled_time in \"{test_type}\" of their tests.",
    "within_attempt_limit":                 "The user with \"{username}\" has an \"attempts\" of less than {attempt_limit} their \"{test_type}\" of tests.",
    "before_test_date":                     "The interaction_time in the database **must be strictly before** the scheduled_time of the \"{test_type}\" in the tests for the user \"{username}\". "\
                                            + "The interaction_time and scheduled_time are compared as **ISO 8601 formatted datetime values**. " \
                                            + "Ensure that the scheduled_time is **at least one second later** than the interaction_time."
}

# all dependency types that could be in a action, each returns true or false
negative_constraint_descriptions = {
    "login_user":                           "The user \"{username}\" is unable to login with the **incorrect** \"{identification}\" to perform this action, **not matching** the database credentials.",
    "authenticate_admin_password":          "[REDACTED] user **must not** authenticate the correct \"{username}\" and \"{admin_password}\" to perform this action,"\
                                            + " **not matching** the database credentials.",
    "internal_check_username_exist":        "The user parameter key \"{username}\" **MUST NOT EXIST** as a top-level key in the accounts section of the database.",
    "internal_has_vehicle":                 "The user with \"{username}\" **does not own** the vehicle with the plate number \"{plate_num}\" in their vehicles.",
    "internal_vehicle_registered":          "The vehicle with the plate number \"{plate_num}\" **must not be** registed under one user's 'vehicles' in the database." , 
    "internal_has_dl":                      "The user with \"{username}\" has a driver_license that **is null** in their account.",
    "internal_valid_test_type":             "The input test type \"{test_type}\" is **invalid (neither 'knowledge' nor 'drive')**.",
    "internal_check_test_slot_available":   "The specified \"{schedule_time}\" **does not exist in the \"{test_type}\"** of test_slots.",
    # state tracker constraints
    "logged_in_user":                       "The user with \"{username}\" **must not be logged in previously with the correct credentials** to perform this action.",
    "authenticated_admin_password":         "[REDACTED] user with \"{username}\" **must not have authenticated** the admin password previously to perform this action.",
    "is_vehicle_address_different":         "The vehicle with the plate number \"{plate_num}\" belonging to the user \"{username}\" **must not** have an address different from \"{address_new}\".",    
    "valid_vehicle_insurance":              "The vehicle with the plate number \"{plate_num}\" belonging to the user \"{username}\" **must not** have an insurance_status of 'valid'.",
    "within_vehicle_renewal_period":        "The interaction_time **does not fall within** the vehicle renewal period for the vehicle with \"{plate_num}\" of the user \"{username}\". "\
                                            + "The renewal period is defined as the time starting {vehicle_renewal_window} days before the reg_date and ending on the reg_date itself. "\
                                            + "Both interaction_time and reg_date are ISO 8601 formatted strings and are considered as date-time values.",
    "is_dl_address_different":              "The driver license of the user \"{username}\" **must** have an address **identical to** \"{address_new}\".",
    "within_dl_renewal_period":             "The interaction_time **does not fall within** the driver_license renewal period for the user \"{username}\". "\
                                            + "The renewal period is defined as the time starting {dl_renewal_window} days before the exp_date and ending on the expiration date itself. "\
                                            + "Both interaction_time and exp_date are ISO 8601 formatted strings and are considered as date-time values.",

    "above_minimum_age":                    "The user with \"{username}\" **must not** be above the minimum age of {min_age}. "\
                                            + "The age should be determined as per interaction_time.",
    "test_type_is_drive":                   "The input test type \"{test_type}\" **must not** be 'drive'.",
    "drive_test_ready":                     "The user with \"{username}\" **must not have passed** the knowledge test "\
                                            + "and must have a status **different from** \"not scheduled\" in \"drive\" of their tests.",
    "test_scheduled":                       "The user with \"{username}\" **must not** have their test status set to 'scheduled' and **must not have** a corersponding scheduled_time in \"{test_type}\" of their tests.",
    "within_attempt_limit":                 "The user with \"{username}\" has an \"attempts\" of **more than {attempt_limit}** their \"{test_type}\" of tests.",
    "before_test_date":                     "The interaction_time in the database **must be strictly after** the scheduled_time of the \"{test_type}\" in the tests for the user \"{username}\". "\
                                            + "The interaction_time and scheduled_time are compared as **ISO 8601 formatted datetime values**. " \
                                            + "Ensure that the scheduled_time is **at least one second earlier** than the interaction_time."
}

# links the dependency to the action that changes its state in the state tracker, should be one to one
constraint_links = {
    "logged_in_user":   ("login_user", {"username":"username", "identification": "identification"}),
    "authenticated_admin_password":  [REDACTED]"authenticate_admin_password", {"username": "username", "admin_password": "[REDACTED]"})
}

# defines the dependencies of constraints based on functionality needs, mainly used for task generation verification
constraint_dependencies = {
   "authenticate_admin_password":          [REDACTED]"single", "logged_in_user", {"username": "username"}),
   "is_vehicle_address_different":         ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
   "valid_vehicle_insurance":              ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
   "within_vehicle_renewal_period":        ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
   "is_dl_address_different":              ("single", "internal_has_dl", {"username": "username"}),
   "within_dl_renewal_period" :            ("single", "internal_has_dl", {"username": "username"}),
   "above_minimum_age":                    ("single", "internal_check_username_exist", {"username": "username"}),
   "drive_test_ready":                     ("single", "internal_check_username_exist", {"username": "username"}),
   "test_scheduled" :                      ("and", [
                                               ("single", "internal_check_username_exist", {"username": "username"}),
                                               ("single", "internal_valid_test_type", {"test_type": "test_type"})
                                           ]),
   "within_attempt_limit":                 ("and", [
                                               ("single", "internal_check_username_exist", {"username": "username"}),
                                               ("single", "internal_valid_test_type", {"test_type": "test_type"})
                                           ]),
   "before_test_date" :                    ("and", [
                                               ("single", "internal_check_username_exist", {"username": "username"}),
                                               ("single", "internal_valid_test_type", {"test_type": "test_type"})
                                           ]),
}


# full list of actions the assistant needs to call to successfully verify the constraint, mutually exclusive with constraint_links
constraint_processes = {
    "internal_check_username_exist":            ("or", [
                                                    ("single", "internal_check_username_exist", {"username": "username"}),
                                                    ("single", "internal_get_database", None)
                                                ]),
    "internal_has_vehicle":                     ("or", [
                                                    ("single", "internal_has_vehicle", {"username": "username", "plate_num": "plate_num"}),
                                                    ("single", "internal_get_database", None)
                                                ]),
    "internal_vehicle_registered":              ("or", [
                                                    ("single", "internal_vehicle_registered", {"plate_num": "plate_num"}),
                                                    ("single", "internal_get_database", None)
                                                ]), 
    "internal_has_dl":                          ("or", [
                                                    ("single", "internal_has_dl", {"username": "username"}),
                                                    ("single", "internal_get_database", None)
                                                ]),
    "internal_valid_test_type":                 ("or", [
                                                    ("single", "internal_valid_test_type", {"test_type": "test_type"}),
                                                    ("single", "internal_get_database", None)
                                                ]),
    "internal_check_test_slot_available":       ("or", [
                                                    ("single", "internal_check_test_slot_available", {"test_type": "test_type", "schedule_time":"schedule_time"}),
                                                    ("single", "internal_get_database", None)
                                                ]),
    "is_vehicle_address_different":             ("or", [
                                                    ("single", "internal_get_vehicle_details", {"username": "username", "plate_num": "plate_num"}),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "valid_vehicle_insurance":                  ("or", [
                                                    ("single", "internal_get_vehicle_details", {"username": "username", "plate_num": "plate_num"}),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "within_vehicle_renewal_period" :           ("or", [
                                                    ("and", [
                                                        ("single", "internal_get_vehicle_details", {"username": "username", "plate_num": "plate_num"}),
                                                        ("single", "internal_get_interaction_time", {})
                                                    ]),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "is_dl_address_different":                  ("or", [
                                                    ("single", "internal_get_dl_details", {"username": "username"}),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "within_dl_renewal_period" :                ("or", [
                                                    ("and", [
                                                        ("single", "internal_get_dl_details", {"username": "username"}),
                                                        ("single", "internal_get_interaction_time", {})
                                                    ]),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "above_minimum_age":                        ("or", [
                                                    ("and", [
                                                        ("single", "internal_get_interaction_time", {}),
                                                        ("single", "internal_get_user_birthday", {"username": "username"})
                                                    ]),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "test_type_is_drive":                       None,
    "drive_test_ready":                         ("or", [
                                                    ("single", "internal_get_test_details", {"username": "username", "test_type": "test_type"}),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "test_scheduled" :                          ("or", [
                                                    ("single", "internal_get_test_details", {"username": "username", "test_type": "test_type"}),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "within_attempt_limit":                     ("or", [
                                                    ("single", "internal_get_test_details", {"username": "username", "test_type": "test_type"}),
                                                    ("single", "internal_get_database", {})
                                                ]),
    "before_test_date" :                        ("or", [
                                                    ("and", [
                                                        ("single", "internal_get_test_details", {"username": "username", "test_type": "test_type"}),
                                                        ("single", "internal_get_interaction_time", {}),
                                                    ]),    
                                                    ("single", "internal_get_database", {})
                                                ]),
}

# method parameters may have parameters that do not go into user_known because they should be filled by the assistant
action_params_user_not_needed = {}

# descriptions of parameters in the funcitons and actions
action_param_descriptions = {
    "username":             "A string of letters, numbers, and symbols to represent their username",
    "identification":       "The password to the user's account",
    "admin_password":       "[REDACTED] admin password of the user's account to access additional functionalities in their account.",
    "bday":                 "The birthday of the user",
    "address":              "The address of the user",
    "admin_password_new":   "The new admin password of the user's account that the user set.",
    "username_new":         "The new username of the user's account.",
    "password_new":         "The new password to the user's account",
    "address_new":          "The user's new address.",
    "plate_num":            "An alphanumeric string to represent the plate number of a vehicle.",
    "model":                "The model name of a vehicle.",
    "vin":                  "The Vehicle Identification Number of a vehicle.",
    "legal_name":           "The legal name displayed on the driver's license.",
    "exp_date":             "The current expiration date of the user's driver's license.",
    "new_name":             "The new name to display on the driver's license",
    "test_type":            "The type of the test whose status the user wants to manage.",
    "schedule_time":        "The user's expected scheduling time.",
    "passed":               "A boolean indicating whether the user have passed the test.",
    "target_owner":         "The username of the target owner.",
}

# actions the assistant can take
actions = [
# Root functions
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
                "type": "string",
                "description": action_param_descriptions["identification"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "identification"]
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
# Account functions
{
    "name": "authenticate_admin_password",
    "description": get_action_full_description(action_descriptions, action_returns,"authenticate_admin_password"),
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
# Domain functions
{
    "name": "register_vehicle",
    "description": get_action_full_description(action_descriptions, action_returns, "register_vehicle"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            },
            "model": {
                "type": "string",
                "description": action_param_descriptions["model"]
            },
            "vin": {
                "type": "string",
                "description": action_param_descriptions["vin"]
            },
        },
        "additionalProperties": False,
        "required": ["username", "plate_num", "model", "vin"]
    }
},
{
    "name": "get_reg_status",
    "description": get_action_full_description(action_descriptions, action_returns, "get_reg_status"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "plate_num"]
    }
},
{
    "name": "change_vehicle_address",
    "description": get_action_full_description(action_descriptions, action_returns, "change_vehicle_address"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            },
            "address_new": {
                "type": "string",
                "description": action_param_descriptions["address_new"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "plate_num", "address_new"]
    }
},
{
    "name": "validate_vehicle_insurance",
    "description": get_action_full_description(action_descriptions, action_returns, "validate_vehicle_insurance"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "plate_num"]
    }
},
{
    "name": "renew_vehicle",
    "description": get_action_full_description(action_descriptions, action_returns, "renew_vehicle"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "plate_num"]
    }
},
{
    "name": "get_dl_status",
    "description": get_action_full_description(action_descriptions, action_returns, "get_dl_status"),
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
    "name": "update_dl_legal_name",
    "description": get_action_full_description(action_descriptions, action_returns, "update_dl_legal_name"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "new_name": {
                "type": "string",
                "description": action_param_descriptions["new_name"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "new_name"]
    }
},
{
    "name": "change_dl_address",
    "description": get_action_full_description(action_descriptions, action_returns, "change_dl_address"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "address_new": {
                "type": "string",
                "description": action_param_descriptions["address_new"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "address_new"]
    }
},
{
    "name": "renew_dl",
    "description": get_action_full_description(action_descriptions, action_returns, "renew_dl"),
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
    "name": "show_available_test_slots",
    "description": get_action_full_description(action_descriptions, action_returns, "show_available_test_slots"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "test_type"]
    }
},
{
    "name": "schedule_test",
    "description": get_action_full_description(action_descriptions, action_returns, "schedule_test"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            },
            "schedule_time": {
                "type": "string",
                "description": action_param_descriptions["schedule_time"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "test_type", "schedule_time"]
    }
},
{
    "name": "cancel_test",
    "description": get_action_full_description(action_descriptions, action_returns, "cancel_test"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "test_type"]
    }
},
{
    "name": "update_test_status",
    "description": get_action_full_description(action_descriptions, action_returns, "update_test_status"),
    "strict": False,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            },
            "passed": {
                "type": "boolean",
                "description": action_param_descriptions["passed"]
            },
            "legal_name": {
                "type": "string",
                "description": action_param_descriptions["legal_name"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "test_type", "passed"]
    }
},
{
    "name": "transfer_title",
    "description": get_action_full_description(action_descriptions, action_returns, "transfer_title"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "target_owner": {
                "type": "string",
                "description": action_param_descriptions["target_owner"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "target_owner", "plate_num"]
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
    "name": "internal_get_user_birthday",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_user_birthday"),
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
    "name": "internal_has_vehicle",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_has_vehicle"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "plate_num"]
    }
},
{
    "name": "internal_vehicle_registered",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_vehicle_registered"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["plate_num"]
    }
},
{
    "name": "internal_get_vehicle_details",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_vehicle_details"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "plate_num": {
                "type": "string",
                "description": action_param_descriptions["plate_num"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "plate_num"]
    }
},
{
    "name": "internal_has_dl",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_has_dl"),
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
    "name": "internal_get_dl_details",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_dl_details"),
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
    "name": "internal_valid_test_type",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_test_type"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            }
        },
        "additionalProperties": False,
        "required": ["test_type"]
    }
},
{
    "name": "internal_check_test_slot_available",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_test_slot_available"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            },
            "schedule_time": {
                "type": "string",
                "description": action_param_descriptions["schedule_time"]
            }
        },
        "additionalProperties": False,
        "required": ["test_type", "schedule_time"]
    }
},
{
    "name": "internal_get_test_details",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_test_details"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "test_type": {
                "type": "string",
                "description": action_param_descriptions["test_type"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "test_type"]
    }
},
{
    "name": "internal_get_interaction_time",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_interaction_time"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {},
        "additionalProperties": False,
        "required": []
    }
}
]