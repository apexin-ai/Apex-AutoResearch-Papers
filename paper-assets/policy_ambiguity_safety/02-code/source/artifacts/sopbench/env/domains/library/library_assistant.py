"""
This file contains the information for the library assistant fo the openai API.
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
name = "Library Assistant"

# specific instructions for the library assistant to follow
instructions = "You are a library assistant that helps with processing various library actions, as illustrated in the descriptions of functions."\
    + " You perform the duties that any library clerk would."

# action descriptions, keeps track of which actions we have currently
action_descriptions = {
    # <function name>: <action description>
    # root functions
    "login_user":                   "Logs in the user to authenticate the user to access their account.",
    "logout_user":                  "Logs out the user if the user was previously logged in.",
    # domain functions
    "show_available_book":          "Retrieves a list of books available for borrowing.",
    "borrow_book":                  "Allows a user to borrow a book and sets its return date.",
    "return_book":                  "Allows a user to return a borrowed book and updates their late count if the book is overdue.",
    "check_return_date":            "Retrieves the return date for the user's specified borrowed book.",
    "get_account_balance":          "Retrieves the current balance of the user's account.",
    "credit_balance":               "Adds a specified amount to the user's account balance.",
    "pay_late_fee":                 "Deducts the total late fee from the user's account balance.",
    "update_membership":            "Updates the user's restricted access status and deducts the monthly fee from their balance.",
    "add_book":                     "Adds a new book to the library database.",
    "remove_book":                  "Removes a book from the library database.",
    "show_available_rooms":         "Retrieves a dictionary of rooms with their available slots to reserve.",
    "reserve_room":                 "Reserves the specified room for the user on the specified date for a list of specified slots.",
    # internal functions
    "internal_get_database":                                        "Shows the full database of the Library system, including all profiles and details.",
    "internal_check_username_exist":                                "Checks if a specific username exists in the Library database.",
    "internal_convert_book_title_to_id":                            "Converts a book title to the corresponding book id.",
    "internal_check_book_exist":                                    "Checks if a book title exists in the library database.",
    "internal_check_book_available":                                "Checks if a book is available for borrowing.",
    "internal_get_user_borrowed":                                   "Retrieves a list of user's borrowed books.",
    "internal_get_user_num_borrowed":                               "Retrieves the number of books the user has borrowed.",
    "internal_calculate_late_fee":                                  "Calculates the user's late fee based on their number of late returns.",
    "internal_get_membership_fee":                                  "Retrieves the restricted access monthly fee from the database.",
    "internal_is_restricted":                                       "Checks if a book is marked as restricted.",
    "internal_get_membership_status":                               "Retrieves the restricted access status of a user.",
    "internal_is_admin":                                            "Checks if a user has admin privileges.",
    "internal_get_num_reserved_slots":                              "Counts the number of the user's reserved slots based on their current reservation.",
    "internal_check_room_exist":                                   "Checks if a specified room id exists in the database.",
    "internal_check_date_available_for_the_room":                   "Checks if the specified date is available for the room.",
    "internal_all_slots_available_for_the_room_on_the_date":        "Checks if the provided slots are alll available for the specified room on the specified date.",
    "internal_get_interaction_date":                                "Retrieves the current interaction date from the database.",
    "internal_convert_human_date_to_iso":                           "Converts a verbalized date string to an ISO 8601 formatted date string ('YYYY-MM-DD').",
    "internal_convert_iso_to_human_date":                           "Converts an ISO 8601 formatted date string ('YYYY-MM-DD') to a verbalized date string."
}

# return values for each action
# return value assumes strict definitions (with no guarantees before the function is called)
# some of these return values are not necessary due to previous guarantees provided by assistant dependencies (such as set_account_information if the user has previously logged in)
action_returns = {
    # <function name>: <action return>
    # root functions
    "login_user":                   "Returns true or false for login success or failure.",
    "logout_user":                  "Returns true always because of successful logout.",
    # domain functions
    "show_available_book":          "Returns a list of books available for borrowing.",
    "borrow_book":                  "Returns true or false for successful book borrowing.",
    "return_book":                  "Returns true or false for successful book return.",
    "check_return_date":            "Returns the return date for the user's specified borrowed book.",
    "get_account_balance":          "Returns the float account balance or None if retrieval conditions are not met.",
    "credit_balance":               "Returns true or false for successful addition of funds to the user's account balance.",
    "pay_late_fee":                 "Returns true or false for successful deduction of late fees from the user's account balance.",
    "update_membership":            "Returns the new expiration date of the restricted access or None if the update condition is not met.",
    "add_book":                     "Returns true or false for successful addition of a new book to the library database.",
    "remove_book":                  "Returns true or false for successful removal of a book from the library database.",
    "show_available_rooms":         "Returns a dictionary of a dictionary of rooms with their available slots to reserve.",
    "reserve_room":                 "Returns true or false for successful room reservation.",
    # internal functions
    "internal_get_database":                                        "Returns the json of the entire database.",
    "internal_check_username_exist":                                "Returns true if the inputted username of the account does exist in the database.",
    "internal_convert_book_title_to_id":                            "Returns a string representing the book id.",
    "internal_check_book_exist":                                    "Returns true or false based on the existence of the book title in the library database.",
    "internal_check_book_available":                                "Returns true or false based on the availability of a book for borrowing.",
    "internal_get_user_borrowed":                                   "Returns a list of user's borrowed books' ids.",
    "internal_get_user_num_borrowed":                               "Returns an integer of the number of books the user has borrowed.",
    "internal_calculate_late_fee":                                  "Returns a float of the late fee the user has to pay.",
    "internal_get_membership_fee":                                  "Returns a floar representing the restricted access monthly fee.",
    "internal_is_restricted":                                       "Returns true or false based on whether a book is marked as restricted.",
    "internal_get_membership_status":                               "Returns a string representing the expiration date of the user's restricted access status "\
                                                                    + "or none if the user don't have a restricted access.",
    "internal_is_admin":                                            "Returns true or false based on whether the user has admin privileges.",
    "internal_get_num_reserved_slots":                              "Returns an integer of the number of reserved slots in the user's current reservation",
    "internal_check_room_exist":                                   "Returns true or false based on the existence of the specified room id in the database.",
    "internal_check_date_available_for_the_room":                   "Returns true or false based on the availability of the specified date for the specified room.",
    "internal_all_slots_available_for_the_room_on_the_date":        "Returns true or false based on the availability of time slots for the specified room on the specified date.",
    "internal_get_interaction_date":                                "Returns the current interaction date recorded in the database.",
    "internal_convert_human_date_to_iso":                           "Returns an ISO 8601 formatted date string ('YYYY-MM-DD').",
    "internal_convert_iso_to_human_date":                           "Returns a verbalized date string."
}

# innate action dependencies in the domain system itself
action_innate_dependencies = {
    # root functions
    "login_user":                   ("single", "internal_check_username_exist", {"username": "username"}),
    "logout_user":                  None,
    # domain functions
    "show_available_book":          None,
    "borrow_book":                  None,
    "return_book":                  None,
    "check_return_date":            None,
    "get_account_balance":          None,
    "credit_balance":               ("single", "amount_positive_restr", {"amount": "amount"}),
    "pay_late_fee":                 None, 
    "update_membership":            None,
    "add_book":                     ("single", "amount_positive_restr", {"amount": "count"}),
    "remove_book":                  ("single", "internal_check_book_exist", {"book_title": "book_title"}),
    "show_available_rooms":         None,
    "reserve_room":                 ("single", "internal_check_room_exist", {"room_id": "room_id"}),
    
    # internal functions
    "internal_get_database":                                        None,
    "internal_check_username_exist":                                None,
    "internal_convert_book_title_to_id":                            None,
    "internal_check_book_exist" :                                   None,
    "internal_check_book_available" :                               ("single", "internal_check_book_exist", {"book_title": "book_title"}),
    "internal_get_user_borrowed":                                   ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_get_user_num_borrowed":                               ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_calculate_late_fee":                                  ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_get_membership_fee":                                  None,
    "internal_is_restricted" :                                      ("single", "internal_check_book_exist", {"book_title": "book_title"}),
    "internal_get_membership_status":                               ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_is_admin" :                                           ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_get_num_reserved_slots":                              ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_check_room_exist":                                    None,
    "internal_check_date_available_for_the_room":                   ("single", "internal_check_room_exist", {"room_id": "room_id"}),
    "internal_all_slots_available_for_the_room_on_the_date":        ("single", "internal_check_date_available_for_the_room", {"room_id": "room_id", "resv_date": "resv_date"}),
    "internal_get_interaction_date":                                None,
    "internal_convert_human_date_to_iso":                           None,
    "internal_convert_iso_to_human_date":                           None
}

# the required dependencies for each function, every condition must be true, should have no conflicting constraints
action_required_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  ("single", "logged_in_user", {"username": "username"}),
    # domain functions
    "show_available_book":          None,
    "borrow_book":                  ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),  
                                        ("single", "internal_check_book_available", {"book_title": "book_title"})
                                    ]),
    "return_book":                  ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),  
                                        ("single", "user_book_borrowed", {"username": "username", "book_title": "book_title"})
                                    ]),
    "check_return_date":            ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),  
                                        ("single", "user_book_borrowed", {"username": "username", "book_title": "book_title"})
                                    ]),
    "get_account_balance":          ("single", "logged_in_user", {"username": "username"}),  
    "credit_balance":               ("single", "logged_in_user", {"username": "username"}),
    "pay_late_fee":                 ("single", "logged_in_user", {"username": "username"}),  
    "update_membership":            ("single", "logged_in_user", {"username": "username"}),  
    "add_book":                     ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),  
                                        ("single", "internal_is_admin", {"username": "username"})
                                    ]),
    "remove_book":                  ("and", [
                                        ("single", "logged_in_user", {"username": "username"}),  
                                        ("single", "internal_is_admin", {"username": "username"})
                                    ]),
    "show_available_rooms":         None,
    "reserve_room":                 ("single", "logged_in_user", {"username": "username"}),
    # internal functions
    "internal_get_database":                                        None,
    "internal_check_username_exist":                                None,
    "internal_convert_book_title_to_id":                            None,
    "internal_check_book_exist" :                                   None,
    "internal_check_book_available" :                               None,
    "internal_get_user_borrowed":                                   None,
    "internal_get_user_num_borrowed":                               None,
    "internal_calculate_late_fee":                                  None,
    "internal_get_membership_fee":                                  None,
    "internal_is_restricted" :                                      None,
    "internal_get_membership_status":                               None,
    "internal_is_admin" :                                           None,
    "internal_get_num_reserved_slots":                              None,
    "internal_check_room_exist":                                    None,
    "internal_check_date_available_for_the_room":                   None,
    "internal_all_slots_available_for_the_room_on_the_date":        None,
    "internal_get_interaction_date":                                None,
    "internal_convert_human_date_to_iso":                           None,
    "internal_convert_iso_to_human_date":                           None
}

# the required dependencies for each function, every condition must be true, should have no conflicting constraints
action_customizable_dependencies = {
    # root functions
    "login_user":                   None,
    "logout_user":                  ("single", "internal_check_username_exist", {"username": "username"}),
    # domain functions
    "show_available_book":          ("single", "logged_in_user", {"username": "username"}),
    "borrow_book":                  [("single", "user_book_not_borrowed", {"username": "username", "book_title": "book_title"}),
                                    ("or", [
                                        ("single", "not internal_is_restricted", {"book_title": "book_title"}),  
                                        ("single", "valid_membership", {"username": "username"})
                                    ]),
                                    ("single", "within_borrow_limit", {"username": "username"})],
    "return_book":                  None,                                   
    "check_return_date":            None, 
    "get_account_balance":          None,
    "credit_balance":               None,  
    "pay_late_fee":                 ("single", "sufficient_account_balance_for_late_fee", {"username": "username"}),
    "update_membership":            ("single", "sufficient_account_balance_for_membership", {"username": "username"}),
    "add_book":                     None,
    "remove_book":                  ("single", "database_book_not_borrowed", {"book_title": "book_title"}),
    "show_available_rooms":         ("single", "logged_in_user", {"username": "username"}),
    "reserve_room":                 [("single", "internal_all_slots_available_for_the_room_on_the_date", {"room_id": "room_id", "resv_date": "resv_date", "slots": "slots"}),
                                     ("or", [
                                         ("single", "valid_membership", {"username": "username"}),
                                         ("single", "within_max_reservation_slots", {"username": "username", "slots": "slots"})
                                     ])],
    # internal functions
    "internal_get_database":                                        None,
    "internal_check_username_exist":                                None,
    "internal_convert_book_title_to_id":                            None,
    "internal_check_book_exist" :                                   None,
    "internal_check_book_available" :                               None,
    "internal_get_user_borrowed":                                   None,
    "internal_get_user_num_borrowed":                               None,
    "internal_calculate_late_fee":                                  None,
    "internal_get_membership_fee":                                  None,
    "internal_is_restricted" :                                      None,
    "internal_get_membership_status":                               None,
    "internal_is_admin" :                                           None,
    "internal_get_num_reserved_slots":                              None,
    "internal_check_room_exist":                                    None,
    "internal_check_date_available_for_the_room":                   None,
    "internal_all_slots_available_for_the_room_on_the_date":        None,
    "internal_get_interaction_date":                                None,
    "internal_convert_human_date_to_iso":                           None,
    "internal_convert_iso_to_human_date":                           None
}

# all dependency types that could be in a action, each returns true or false
positive_constraint_descriptions = {
    # state tracker constraints
    "logged_in_user":                                       "The user with \"{username}\" is logged in previously with the correct credentials to perform this action.",
    "user_book_borrowed":                                   "The book's ID (retrieved using \"{book_title}\" from the \"book_title_to_id\" section) exists "\
                                                            + "in the \"borrowed\" of the user \"{username}\".",
    "user_book_not_borrowed":                               "The book's ID (retrieved using \"{book_title}\" from the \"book_title_to_id\" section) **must not exist** "\
                                                            + "in the \"borrowed\" of the user \"{username}\".",
    "database_book_not_borrowed":                           "The book's ID, retrieved using the \"{book_title}\" from the \"book_title_to_id\" section, "\
                                                            + "**must NOT appear** as a key in the \"borrowed\" dictionaries of "\
                                                            + "any users listed in the \"accounts\" section of the database.",
    "sufficient_account_balance_for_late_fee":              "The user \"{username}\" does have more account balance \"balance\" than the late fee, "\
                                                            + " which is the product of the user's \"late_book_count\" in their account and late_fee_per_book in the database.",
    "sufficient_account_balance_for_membership":            "The user \"{username}\" does have more account balance \"balance\" than the monthly resitrcted access fee, "\
                                                            + " which is the membership_monthly_fee in the database.",
    "amount_positive_restr":                                "The user parameter key \"{amount}\" is more than zero.",
    "valid_membership":                                     "The user \"{username}\" must have a 'membership' field that is a date on or after the interaction_time. ",            
    "within_borrow_limit":                                  "The user \"{username}\" must have less than {borrow_limit} books in their \"borrowed\".",
    "within_max_reservation_slots":                         "The user \"{username}\" must have a total number of reserved slots less than or equal to {max_reservation_slots}, "\
                                                            + "calculated as the sum of their currently reserved slots in 'room_reservation' and the newly requested slots \"{slots}\".",
    # domain system constraints
    "login_user":                                                   "The user \"{username}\" must be able to login with the correct password \"{password}\" to perform this action.",
    "internal_check_username_exist":                                "The user parameter key \"{username}\" must exist as a top-level key in the accounts section of the database.",
    "internal_check_book_exist":                                    "The book's title \"{book_title}\" exists in the \"book_title_to_id\" section of the database "\
                                                                    "and the book's ID (retrieved using \"{book_title}\") exists in the books.",
    "internal_check_book_available":                                "The book \"{book_title}\" has a count value of **more than 0**.",
    "internal_is_restricted":                                       "The book \"{book_title}\" has its restricted status set to **true**.",
    "internal_is_admin":                                            "The user \"{username}\" has an \"admin\" of **true** in the database.",
    "internal_check_room_exist":                                    "The specified room ID \"{room_id}\" must exist in the database under the 'rooms' section.",
    "internal_check_date_available_for_the_room":                   "The specified reservation date \"{resv_date}\" must be listed under the 'rooms' section for the given room ID \"{room_id}\".",
    "internal_all_slots_available_for_the_room_on_the_date":        "All requested slots \"{slots}\" for the specified reservation date \"{resv_date}\" in the room \"{room_id}\" must be available in the database."
}

# all dependency types that could be in a action, each returns true or false
negative_constraint_descriptions = {
    # state tracker constraints
    "logged_in_user":                                       "The user with \"{username}\" **must not be logged in previously with the correct credentials** to perform this action.",
    "user_book_borrowed":                                   "The book's ID, retrieved using its \"{book_title}\" from the \"book_title_to_id\" section, **must not exist**  "\
                                                            + "as a key in the \"borrowed\" dictionary of **at least one user** in the \"accounts\" section of the database.",
    "user_book_not_borrowed":                               "The book's ID (retrieved using \"{book_title}\" from the \"book_title_to_id\" section) **must exist** "\
                                                            + "in the \"borrowed\" of the user \"{username}\".",
    "database_book_not_borrowed":                           "The book's ID, retrieved using the \"{book_title}\" from the \"book_title_to_id\" section, "\
                                                            + "**must appear** as a key in the \"borrowed\" dictionaries of "\
                                                            + "**at least 1 user** listed in the \"accounts\" section of the database.",
    "sufficient_account_balance_for_late_fee":              "The user \"{username}\" **does not have** more account balance \"balance\" than the late fee, "\
                                                            + " which is the product of the user's \"late_book_count\" in their account and late_fee_per_book in the database.",
    "sufficient_account_balance_for_membership":            "The user \"{username}\" **does not have** more account balance \"balance\" than the monthly resitrcted access fee, "\
                                                            + " which is the membership_monthly_fee in the database.",
    "amount_positive_restr":                                "The user parameter key \"{amount}\" **must be less than or equal to zero**.",
    "valid_membership":                                     "The user \"{username}\" must have a 'membership' field that is **EITHER null OR** a date that is **before** the interaction_time.",
    "within_borrow_limit":                                  "The user \"{username}\" must have **more than or equal to** {borrow_limit} books in their \"borrowed\".",
    "within_max_reservation_slots":                         "The user \"{username}\" must have a total number of reserved slots **more than** {max_reservation_slots}, "\
                                                            + "calculated as the sum of their currently reserved slots in 'room_reservation' and the newly requested slots \"{slots}\".",
    # domain system constraints
    "login_user":                                                   "The user \"{username}\" **must not be able to login** with the **incorrect password** \"{password}\" to perform this action.",    
    "internal_check_username_exist":                                "The user parameter key \"{username}\" **MUST NOT EXIST** as a top-level key in the accounts section of the database.",
    "internal_check_book_exist":                                    "The book's title \"{book_title}\" **does not exist** in the \"book_title_to_id\" section of the database "\
                                                                    "or the book's ID (retrieved using \"{book_title}\") **does not exist** in the books.",
    "internal_check_book_available":                                "The book \"{book_title}\" has a count value of **less than 1**.",
    "internal_is_restricted":                                       "The book \"{book_title}\" has its restricted status set to **false**.",
    "internal_is_admin":                                            "The user \"{username}\" has an \"admin\" of **false** in the database.",
    "internal_check_room_exist":                                    "The specified room ID \"{room_id}\" **must not** exist in the database under the 'rooms' section.",
    "internal_check_date_available_for_the_room":                   "The specified reservation date \"{resv_date}\" **must not** be listed under the 'rooms' section for the given room ID \"{room_id}\".",
    "internal_all_slots_available_for_the_room_on_the_date":        "**NOT** all requested slots \"{slots}\" for the specified reservation date \"{resv_date}\" in the room \"{room_id}\" are available in the database."
}

# links the dependency to the action that changes its state in the state tracker, should be one to one
constraint_links = {
    "logged_in_user":               ("login_user", {"username": "username"})
}

# defines the dependencies of constraints based on functionality needs, mainly used for task generation verification
constraint_dependencies = {
   "user_book_borrowed":                                           ("and", [
                                                                       ("single","internal_check_username_exist", {"username": "username"}),
                                                                       ("single", "internal_check_book_exist", {"book_title": "book_title"})
                                                                   ]),
   "user_book_not_borrowed":                                       ("and", [
                                                                       ("single","internal_check_username_exist", {"username": "username"}),
                                                                       ("single", "internal_check_book_exist", {"book_title": "book_title"})
                                                                   ]),
   "database_book_not_borrowed":                                   ("single", "internal_check_book_exist", {"book_title": "book_title"}),
   "sufficient_account_balance_for_late_fee":                      ("single", "internal_check_username_exist", {"username": "username"}),
   "sufficient_account_balance_for_membership":                    ("single", "internal_check_username_exist", {"username": "username"}),
   "valid_membership":                                             ("single", "internal_check_username_exist", {"username": "username"}),
   "within_borrow_limit":                                          ("single", "internal_check_username_exist", {"username": "username"}),
   "within_max_reservation_slots":                                 ("single", "internal_check_username_exist", {"username": "username"})
}  

# full list of actions the assistant needs to call to successfully verify the constraint, mutually exclusive with action_dependency_links
constraint_processes = {
    "internal_check_username_exist":                                ("or", [
                                                                        ("single", "internal_check_username_exist", {"username": "username"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]),
    "internal_check_book_exist":                                    ("or", [
                                                                        ("single", "internal_check_book_exist", {"book_title": "book_title"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]),
    "internal_check_book_available":                                ("or", [
                                                                        ("single", "internal_check_book_available", {"book_title": "book_title"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]), 
    "internal_is_restricted":                                       ("or", [
                                                                        ("single", "internal_is_restricted", {"book_title": "book_title"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]),
    "internal_is_admin":                                            ("or", [
                                                                        ("single", "internal_is_admin", {"username": "username"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]),
    "internal_check_room_exist":                                    ("or", [
                                                                        ("single", "internal_check_room_exist", {"room_id": "room_id"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]), 
    "internal_check_date_available_for_the_room":                   ("or", [
                                                                        ("single", "internal_check_date_available_for_the_room", {"room_id": "room_id", "resv_date": "resv_date"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]),
    "internal_all_slots_available_for_the_room_on_the_date":        ("or", [
                                                                        ("single", "internal_all_slots_available_for_the_room_on_the_date", {"room_id": "room_id", "resv_date": "resv_date", "slots": "slots"}),
                                                                        ("single", "internal_get_database", None)
                                                                    ]),
    "user_book_borrowed":                                           ("or", [
                                                                        ("and", [
                                                                            ("single", "internal_check_book_exist", {"book_title": "book_title"}),
                                                                            ("single", "internal_get_user_borrowed", {"username": "username"})
                                                                        ]),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "user_book_not_borrowed":                                       ("or", [
                                                                        ("and", [
                                                                            ("single", "internal_check_book_exist", {"book_title": "book_title"}),
                                                                            ("single", "internal_get_user_borrowed", {"username": "username"})
                                                                        ]),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "database_book_not_borrowed":                                   ("or", [
                                                                        ("and", [
                                                                            ("single", "internal_check_book_exist", {"book_title": "book_title"}),
                                                                            ("single", "internal_get_user_borrowed", {"username": "username"})
                                                                        ]),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "sufficient_account_balance_for_late_fee":                      ("or", [
                                                                        ("and", [
                                                                            ("single", "get_account_balance", {"username": "username"}),
                                                                            ("single", "internal_calculate_late_fee", {"username": "username"})
                                                                        ]),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "sufficient_account_balance_for_membership":                    ("or", [
                                                                        ("and", [
                                                                            ("single", "get_account_balance", {"username": "username"}),
                                                                            ("single", "internal_get_membership_fee", {})
                                                                        ]),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "amount_positive_restr":                                        None,
    "valid_membership":                                             ("or", [
                                                                        ("and", [
                                                                            ("single", "internal_get_membership_status", {"username": "username"}),
                                                                            ("single", "internal_get_interaction_date", {})
                                                                        ]),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "within_borrow_limit":                                          ("or", [
                                                                        ("single", "internal_get_user_num_borrowed", {"username": "username"}),
                                                                        ("single", "internal_get_database", {})
                                                                    ]),
    "within_max_reservation_slots":                                 ("or", [
                                                                        ("single", "internal_get_num_reserved_slots", {"username": "username"}),
                                                                        ("single", "internal_get_database", {})
                                                                    ])
}

# method parameters may have parameters that do not go into user_known because they should be filled by the assistant
action_params_user_not_needed = {}

# descriptions of parameters in the funcitons and actions
action_param_descriptions = {
    "username":                         "a string of letters, numbers, and symbols to represent their username",
    "password":                         "[REDACTED] password to their account",
    "initial_amount":                   "the initial balance to be credited to the user's account when opening a new account.",
    "username_new":                     "The new username of the user's account.",
    "password_new":                     "the new password to their account.",
    "book_title":                       "the title of the book to be borrowed, returned, or managed.",
    "amount":                           "the amount of money specified by the function description.",
    "count":                            "the number of copies of a book to add or remove from the library's database.",
    "restricted":                       "a boolean indicating whether a book is restricted.",
    "room_id":                          "a string representing the id of a library room to reserve",
    "resv_date":                        "a string representing the date when the user want to reserve a room.",
    "slots":                            "a list of time slots that the user want to reserve a certain room on a specified day.",
    "date_string":                      "the date in a human-readable string format," \
                                        + "where the month is an English word (e.g., 'January'), "\
                                        + "the day is a number followed by a proper suffix (e.g., '1st', '2nd', '4th'), "
                                        + "and the year is a four-digit number (e.g., '2024'). "\
                                        + "Example: 'January 25th, 2024'.",
    "iso_date":                         "an ISO date string ('YYYY-MM-DD')."
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
            "password": [REDACTED]
                "type": "string",
                "description": action_param_descriptions["password"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "password"]
    }
},
{
    "name": "logout_user",
    "description":  get_action_full_description(action_descriptions, action_returns, "logout_user"),
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
    "name": "show_available_book",
    "description":  get_action_full_description(action_descriptions, action_returns, "show_available_book"),
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
    "name": "borrow_book",
    "description":  get_action_full_description(action_descriptions, action_returns, "borrow_book"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "book_title"]
    }
},
{
    "name": "return_book",
    "description":  get_action_full_description(action_descriptions, action_returns, "return_book"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "book_title"]
    }
},
{
    "name": "check_return_date",
    "description":  get_action_full_description(action_descriptions, action_returns, "check_return_date"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "book_title"]
    }
},
{
    "name": "get_account_balance",
    "description":  get_action_full_description(action_descriptions, action_returns, "get_account_balance"),
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
    "name": "credit_balance",
    "description":  get_action_full_description(action_descriptions, action_returns, "credit_balance"),
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
            }
        },
        "additionalProperties": False,
        "required": ["username", "amount"]
    }
},
{
    "name": "pay_late_fee",
    "description":  get_action_full_description(action_descriptions, action_returns, "pay_late_fee"),
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
    "name": "update_membership",
    "description":  get_action_full_description(action_descriptions, action_returns, "update_membership"),
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
    "name": "add_book",
    "description": get_action_full_description(action_descriptions, action_returns, "add_book"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            },
            "count": {
                "type": "number",
                "description": action_param_descriptions["count"]
            },
            "restricted": {
                "type": "boolean",
                "description": action_param_descriptions["restricted"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "book_title", "count", "restricted"]
    }
},
{
    "name": "remove_book",
    "description": get_action_full_description(action_descriptions, action_returns, "remove_book"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            },
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["username", "book_title"]
    }
},
{
    "name": "show_available_rooms",
    "description": get_action_full_description(action_descriptions, action_returns, "show_available_rooms"),
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
    "name": "reserve_room",
    "description": get_action_full_description(action_descriptions, action_returns, "show_available_rooms"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string",
                "description": action_param_descriptions["username"]
            }, 
            "room_id": {
                "type": "string",
                "description": action_param_descriptions["room_id"]
            },
            "resv_date": {
                "type": "string",
                "description": action_param_descriptions["resv_date"]
            },
            "slots":{
                "type": "array",
                "description": action_param_descriptions["slots"],
                "items": {
                    "type": "string"
                }
            }
        },
        "additionalProperties": False,
        "required": ["username", "room_id", "resv_date", "slots"]
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
    "name": "internal_convert_book_title_to_id",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_convert_book_title_to_id"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["book_title"]
    }
},
{
    "name": "internal_check_book_exist",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_book_exist"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["book_title"]
    }
},
{
    "name": "internal_check_book_available",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_book_available"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["book_title"]
    }
},
{
    "name": "internal_get_user_borrowed",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_user_borrowed"),
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
    "name": "internal_get_user_num_borrowed",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_user_num_borrowed"),
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
    "name": "internal_calculate_late_fee",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_calculate_late_fee"),
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
    "name": "internal_get_membership_fee",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_membership_fee"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {},
        "additionalProperties": False,
        "required": []
    }
},
{
    "name": "internal_is_restricted",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_is_restricted"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "book_title": {
                "type": "string",
                "description": action_param_descriptions["book_title"]
            }
        },
        "additionalProperties": False,
        "required": ["book_title"]
    }
},
{
    "name": "internal_get_membership_status",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_membership_status"),
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
    "name": "internal_is_admin",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_is_admin"),
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
    "name": "internal_get_num_reserved_slots",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_get_num_reserved_slots"),
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
    "name": "internal_check_room_exist",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_room_exist"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "room_id": {
                "type": "string",
                "description": action_param_descriptions["room_id"]
            }
        },
        "additionalProperties": False,
        "required": ["room_id"]
    }
},
{
    "name": "internal_check_date_available_for_the_room",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_check_date_available_for_the_room"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "room_id": {
                "type": "string",
                "description": action_param_descriptions["room_id"]
            },
            "resv_date": {
                "type": "string",
                "description": action_param_descriptions["resv_date"]
            }
        },
        "additionalProperties": False,
        "required": ["room_id", "resv_date"]
    }
},
{
    "name": "internal_all_slots_available_for_the_room_on_the_date",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_all_slots_available_for_the_room_on_the_date"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "room_id": {
                "type": "string",
                "description": action_param_descriptions["room_id"]
            },
            "resv_date": {
                "type": "string",
                "description": action_param_descriptions["resv_date"]
            },
            "slots": {
                "type": "array",
                "description": action_param_descriptions["slots"],
                "items": {
                    "type": "string"
                }
            }
        },
        "additionalProperties": False,
        "required": ["room_id", "resv_date", "slots"]
    }
},
{
    "name": "internal_convert_human_date_to_iso",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_convert_human_date_to_iso"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "date_string": {
                "type": "string",
                "description": action_param_descriptions["date_string"]
            }
        },
        "additionalProperties": False,
        "required": ["date_string"]
    }
},
{
    "name": "internal_convert_iso_to_human_date",
    "description": get_action_full_description(action_descriptions, action_returns, "internal_convert_iso_to_human_date"),
    "strict": True,
    "parameters": {
        "type": "object",
        "properties": {
            "iso_date": {
                "type": "string",
                "description": action_param_descriptions["iso_date"]
            }
        },
        "additionalProperties": False,
        "required": ["iso_date"]
    }
}
]