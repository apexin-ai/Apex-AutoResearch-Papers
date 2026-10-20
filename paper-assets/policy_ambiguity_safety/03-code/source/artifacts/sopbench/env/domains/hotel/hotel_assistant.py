"""
This file contains the information for the hotel assistant fo the openai API.
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
name = "Hotel Assistant"

# specific instructions for the hotel assistant to follow
instructions = "You are a hotel assistant that helps with processing various hotel-related actions, as illustrated in the descriptions of functions."\
    + " You perform tasks that any hotel front desk agent would."

# action descriptions, keeps track of which actions we have currently
action_descriptions = {
    "show_available_rooms":                         "Displays available rooms across all room types.",
    "show_room_change_options":                     "Lists valid reasons a guest can request a room change.",
    "book_room":                                    "Books a room for the guest given the room type, date range, and payment details.",
    "find_booking_info":                            "Finds the booking information for the guest with the specified date range.",
    "cancel_reservation":                           "Cancels a confirmed reservation for the guest for the specified date range.",
    "modify_reservation":                           "Modifies the guest's existing reservation to new dates and room type.",
    "process_guest_checkin":                        "Processes the check-in of a guest on the day of arrival.",
    "process_guest_checkout":                       "Processes the checkout of a guest and applies loyalty rewards if eligible.",
    "request_room_change":                          "Processes a room change request by the guest during their stay given a valid reason and payment.",
    "place_room_service_order":                     "Places a new room service order for the guest.",
    "register_loyalty_member":                      "Registers the specified guest into the loyalty program with a generated unique ID and initial tier.",
    # internal functions
    "internal_get_room_checkin_details":            "Retrieves current room check-in records.",
    "internal_get_booking_details":                 "Retrieves all current bookings in the hotel system.",
    "internal_get_loyalty_member_info":             "Retrieves information of the specified loyalty members, including status and points.",
    "internal_get_interaction_time":                "Returns the timestamp of the current system interaction.",
    "internal_get_room_service_order_details":      "Retrieves the details of all room service orders.",
    "internal_get_room_assignment":                 "Retrieves the mapping of booking IDs to their assigned room IDs.",
    "internal_compute_room_service_order_fee":      "Calculates the total cost of a room service order given item quantities and order type.",
    "internal_valid_room_type":                     "Checks whether the specified room type exists in the hotel system.",
    "internal_is_loyalty_member":                   "Checks if the guest is currently registered as a loyalty member.",
    "internal_valid_room_change_reason":            "Checks whether the provided reason is valid for requesting a room change.",
    "internal_valid_room_service_order_type":       "Checks if the specified room service order type exists.",
    "internal_valid_room_service_item":             "Checks if the room service items are available in the specified category.",
    "internal_valid_room_id":                       "Checks if the specified room id exists in the availability section of any room type.",
    "internal_valid_room_service_payment_method":   "Checks if the specified payment method is one of the accepted payment methods for room service.",
}

# return values for each action
# return value assumes strict definitions (with no guarantees before the function is called)
# some of these return values are not necessary due to previous guarantees provided by assistant dependencies
# return values for each hotel domain action
action_returns = {
    "show_available_rooms":                         "Returns the dictionary of all room types and their availability.",
    "show_room_change_options":                     "Returns a list of valid reasons guests may provide to request a room change.",
    "book_room":                                    "Returns true or false for whether the booking and room assignment was successful.",
    "find_booking_info":                            "Returns a dictionary of booking details for the guest if a matching reservation is found.",
    "cancel_reservation":                           "Returns true or false for whether the reservation was successfully canceled.",
    "modify_reservation":                           "Returns true or false for whether the reservation was successfully modified.",
    "process_guest_checkin":                        "Returns the assigneed room id upon successful check-in.",
    "process_guest_checkout":                       "Returns true or false for whether the checkout was successful.",
    "request_room_change":                          "Returns true or false for whether the room change was successful.",
    "place_room_service_order":                     "Returns true or false for whether the room service order was placed successfully.",
    "register_loyalty_member":                      "Returns true or false for whether the registration to the loyalty program was successful.", 
    # internal functions
    "internal_get_room_checkin_details":            "Returns the dictionary of current room check-in records.",
    "internal_get_booking_details":                 "Returns the dictionary of all current guest bookings with full reservation data.",
    "internal_get_loyalty_member_info":             "Returns the dictionary of the specified loyalty program member with their status and points.",
    "internal_get_interaction_time":                "Returns the current system timestamp indicating the time of interaction.",
    "internal_get_room_service_order_details":      "Returns a dictionary of all room service orders placed during guest stays.",
    "internal_get_room_assignment":                 "Returns a dictionary mapping booking IDs to room IDs.",
    "internal_compute_room_service_order_fee":      "Returns the total cost of the specified room service order.",
    "internal_valid_room_type":                     "Returns true or false depending on whether the provided room type exists in the hotel database.",
    "internal_is_loyalty_member":                   "Returns true or false depending on whether the given user is enrolled in the loyalty program.",
    "internal_valid_room_change_reason":            "Returns true or false depending on whether the reason is a valid room change reason.",
    "internal_valid_room_service_order_type":       "Returns true or false depending on whether the room service order type is valid.",
    "internal_valid_room_service_item":             "Returns true or false depending on whether the room service item exists in any category.",
    "internal_valid_room_id":                       "Returns true or false depending on whether the room id exists in the availability section of any room type.",
    "internal_valid_room_service_payment_method":   "Returns true or false depending on whether the payment method is accetable for room service.",
}

# innate action dependencies in the domain system itself
action_innate_dependencies = {
    "show_available_rooms":                         None,
    "show_room_change_options":                     None,
    "book_room":                                    ("and", [
                                                        ("single", "amount_positive_restr", {"amount": "amount"}),
                                                        ("single", "internal_valid_room_type", {"room_type": "room_type"}),
                                                        ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),                                                        
                                                    ]),
    "find_booking_info":                            None,
    "cancel_reservation":                           ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
    "modify_reservation":                           ("and", [
                                                        ("single", "amount_positive_restr", {"amount": "amount"}),
                                                        ("single", "internal_valid_room_type", {"room_type": "room_type"}),
                                                        ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                        ("single", "valid_booking_date_pair", {"check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"}),
                                                    ]),
    "process_guest_checkin":                        None,
    "process_guest_checkout":                       None,
    "request_room_change":                          ("single", "amount_positive_restr", {"amount": "amount"}),
    "place_room_service_order":                     ("single", "internal_valid_room_service_item", {"order_type": "order_type", "order_items": "order_items"}),
    "register_loyalty_member":                      None,
    # internal functions
    "internal_get_room_checkin_details":            None,
    "internal_get_booking_details":                 None,
    "internal_get_loyalty_member_info":             ("single", "internal_is_loyalty_member", {"guest_name": "guest_name"}),
    "internal_get_interaction_time":                None,
    "internal_get_room_service_order_details":      None,
    "internal_get_room_assignment":                 None,
    "internal_compute_room_service_order_fee":      ("single", "internal_valid_room_service_item", {"order_type": "order_type", "order_items": "order_items"}),
    "internal_valid_room_type":                     None,
    "internal_is_loyalty_member":                   None,
    "internal_valid_room_change_reason":            None,
    "internal_valid_room_service_order_type":       None,
    "internal_valid_room_service_item":             ("single", "internal_valid_room_service_order_type", {"order_type": "order_type"}),
    "internal_valid_room_id":                       None,
    "internal_valid_room_service_payment_method":   None
}

# the required dependencies for each function, every condition must be true
action_required_dependencies = {
    "show_available_rooms":                         None,
    "show_room_change_options":                     None,
    "book_room":                                    ("and", [
                                                        ("single", "room_type_available_for_dates", {"room_type": "room_type", "check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                        ("single", "sufficient_amount_for_booking", {"room_type": "room_type", "check_in_date": "check_in_date", "check_out_date": "check_out_date", "amount": "amount"})
                                                    ]),
    "find_booking_info":                            None,
    "cancel_reservation":                           ("single", "has_confirmed_reservation", {"guest_name": "guest_name", "check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
    "modify_reservation":                           ("and", [
                                                        ("single", "room_type_available_for_dates", {"room_type": "room_type", "check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                        ("single", "sufficient_amount_for_reservation_modification", {"guest_name": "guest_name", "old_check_in_date": "old_check_in_date", "old_check_out_date": "old_check_out_date", "check_in_date": "check_in_date", "check_out_date": "check_out_date", "room_type": "room_type", "amount": "amount"})
                                                    ]),
    "process_guest_checkin":                        ("single", "has_confirmed_reservation", {"guest_name": "guest_name", "check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
    "process_guest_checkout":                       ("single", "guest_already_checked_in", {"guest_name": "guest_name"}),
    "request_room_change":                          ("single", "sufficient_amount_for_room_change_fee", {"guest_name": "guest_name", "amount": "amount", "room_type": "room_type"}),
    "place_room_service_order":                     ("and", [
                                                        ("single", "guest_already_checked_in", {"guest_name": "guest_name"}),
                                                        ("single", "sufficient_payment_for_room_service", {"guest_name":"guest_name", "order_type": "order_type", "order_items": "order_items", "payment_method": "payment_method", "amount": "amount"})
                                                    ]),
    "register_loyalty_member":                      ("single", "not internal_is_loyalty_member", {"guest_name": "guest_name"}),
    # internal functions
    "internal_get_room_checkin_details":            None,
    "internal_get_booking_details":                 None,
    "internal_get_loyalty_member_info":             None,
    "internal_get_interaction_time":                None,
    "internal_get_room_service_order_details":      None,
    "internal_get_room_assignment":                 None,
    "internal_compute_room_service_order_fee":      None,
    "internal_valid_room_type":                     None,
    "internal_is_loyalty_member":                   None,
    "internal_valid_room_change_reason":            None,
    "internal_valid_room_service_order_type":       None,
    "internal_valid_room_service_item":             None,
    "internal_valid_room_id":                       None,
    "internal_valid_room_service_payment_method":   None
}

# the customizable dependencies for each function, the conditions can be changed, order matters due to sequential data generation
action_customizable_dependencies = {
    "show_available_rooms":                         None,
    "show_room_change_options":                     None,
    "book_room":                                    [
                                                        ("single", "not has_overlapping_booking_for_booking", {"guest_name": "guest_name", "check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                        ("single", "is_booking_date_within_lead_time_range", {"check_in_date": "check_in_date"}),
                                                        ("or", [
                                                            ("single", "not has_exceeded_maximum_stays", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                            ("single", "is_gold_or_higher_member", {"guest_name": "guest_name"})
                                                        ]),
                                                    ],
    "find_booking_info":                            None,
    "cancel_reservation":                           [
                                                        ("single", "before_modification_deadline", {"check_in_date": "check_in_date"})
                                                    ],
    "modify_reservation":                           [
                                                        ("single", "not has_overlapping_booking_for_modification", {"guest_name": "guest_name", "check_in_date": "check_in_date", "check_out_date": "check_out_date", "old_check_in_date": "old_check_in_date", "old_check_out_date": "old_check_out_date"}),
                                                        ("single", "is_booking_date_within_lead_time_range", {"check_in_date": "check_in_date"}),
                                                        ("single", "before_modification_deadline", {"check_in_date": "old_check_in_date"}),
                                                        ("or", [
                                                            ("single", "not has_exceeded_maximum_stays", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                            ("single", "is_gold_or_higher_member", {"guest_name": "guest_name"})
                                                        ])
                                                    ],
    "process_guest_checkin":                        [
                                                        ("single", "valid_identification", {"identification": "identification"}),
                                                        ("single", "after_check_in_time", {}), 
                                                    ],
    "process_guest_checkout":                       [
                                                        ("single", "room_key_returned", {"key_returned": "key_returned"}),
                                                        ("single", "before_check_out_time", {}), 
                                                    ],
    "request_room_change":                          [
                                                        ("single", "internal_valid_room_change_reason", {"reason":"reason"}),
                                                        ("single", "within_max_room_changes", {"guest_name": "guest_name"}), 
                                                    ],
    "place_room_service_order":                     [
                                                        ("single", "within_room_service_order_daily_limit", {"guest_name": "guest_name", "room_id": "room_id"}),
                                                        ("single", "within_room_service_hours", {})
                                                    ],
    "register_loyalty_member":                      None,
    # internal functions
    "internal_get_room_checkin_details":            None,
    "internal_get_booking_details":                 None,
    "internal_get_loyalty_member_info":             None,
    "internal_get_interaction_time":                None,
    "internal_get_room_service_order_details":      None,
    "internal_get_room_assignment":                 None,
    "internal_compute_room_service_order_fee":      None,
    "internal_valid_room_type":                     None,
    "internal_is_loyalty_member":                   None,
    "internal_valid_room_change_reason":            None,
    "internal_valid_room_service_order_type":       None,
    "internal_valid_room_service_item":             None,
    "internal_valid_room_id":                       None,
    "internal_valid_room_service_payment_method":   None
}

# all dependency types that could be in a action, each returns true or false
positive_constraint_descriptions = {
    # internal constraints
    "internal_valid_room_type":                             "The \"{room_type}\" must refer to one of the room types currently offered by the hotel.",
    "internal_is_loyalty_member":                           "The guest \"{guest_name}\" must be enrolled in the hotel's loyalty program.",
    "internal_valid_room_change_reason":                    "The \"{reason}\" must be listed as one of the hotel's accepted reasons for requesting a room change.",
    "internal_valid_room_service_order_type":               "The \"{order_type}\" must correspond to an available category of room service offered by the hotel.",
    "internal_valid_room_service_item":                     "All items in the input \"{order_items}\" must belong to the \"{order_type}\" category of room service.",
    "internal_valid_room_id":                               "The \"{room_id}\" must exist in the availability records of a room type offered by the hotel.",
    "internal_valid_room_service_payment_method":           "The \"{payment_method}\" must be listed as one of the accepted payment methods for room service.",
    # state tracker constraints
    "valid_booking_date_pair":                              "The \"{check_in_date}\" must come **strictly before** the \"{check_out_date}\".",
    "room_type_available_for_dates":                        "The \"{room_type}\" must have at least one specific room available for every date from \"{check_in_date}\" up to (but not including) \"{check_out_date}\".",
    "is_booking_date_within_lead_time_range":               "The \"{check_in_date}\" must be **no earlier than** {min_booking_lead_time_days} days after and **no later than** {max_booking_lead_time_days} days after the current interaction date.",
    "has_exceeded_maximum_stays":                           "The stay from \"{check_in_date}\" to \"{check_out_date}\" must span more than {max_stays} nights.",
    "sufficient_amount_for_booking":                        "The \"{amount}\" must be **greater than or equal to** the total booking cost for the selected \"{room_type}\" from \"{check_in_date}\" to \"{check_out_date}\".",
    "has_overlapping_booking_for_booking":                  "The guest \"{guest_name}\" must have at least one existing booking that overlaps with the new date range from \"{check_in_date}\" to \"{check_out_date}\" when booking.",
    "has_overlapping_booking_for_modification":             "The guest \"{guest_name}\" must have at least one existing booking, excluding the one from \"{old_check_in_date}\" to \"{old_check_out_date}\","\
                                                            + " that overlaps with the new date range from \"{check_in_date}\" to \"{check_out_date}\" when modifying their reservation.",
    "before_modification_deadline":                         "The current interaction time must be **no later than** {modification_deadline_hours} hours before {check_in_time} on \"{check_in_date}\".",
    "has_confirmed_reservation":                            "The guest \"{guest_name}\" must have a reservation from \"{check_in_date}\" to \"{check_out_date}\" with status marked as \"confirmed\".",
    "sufficient_amount_for_reservation_modification":       "The \"{amount}\" must be **greater than or equal to** the difference in booking cost when modifying from the original stay (\"{old_check_in_date}\" to \"{old_check_out_date}\")"
                                                            +" to the new stay (\"{check_in_date}\" to \"{check_out_date}\") with a new room type \"{room_type}\".",
    "valid_identification":                                 "The \"{identification}\" must include a \"type\" that matches one of {valid_document_types} and a valid \"birthday\" indicating the guest is at least {min_age} years old.",
    "after_check_in_time":                                  "The current interaction time must be **on or after** the check-in time {check_in_time} on the interaction date.",
    "before_check_out_time":                                "The current interaction time must be **before** the check-out time {check_out_time} on the interaction date.",
    "guest_already_checked_in":                             "The guest \"{guest_name}\" must be listed in the room check-in records.",
    "room_key_returned":                                    "The input \"{key_returned}\" must be set to true.",
    "room_type_available_for_room_change":                  "The \"{room_type}\" must have at least one room available for all remaining nights between the current interaction date and the \"check_out_date\" in the reservation of the checked-in guest \"{guest_name}\".",
    "has_remaining_nights":                                 "The checked-in guest \"{guest_name}\" must have **at least one** night remaining between the current interaction date and the \"check_out_date\" in their reservation.",
    "sufficient_amount_for_room_change_fee":                "The checked-in guest \"{guest_name}\" must provide an amount \"{amount}\" that is **greater than or equal to** the additional fee for changing from the original room type to \"{room_type}\""
                                                            + " for the remaining nights between the current interaction date and the \"check_out_date\" in their reservation.",
    "within_max_room_changes":                              "The number of room changes for the guest \"{guest_name}\" must be **less than** {max_room_changes}.",
    "within_room_service_order_daily_limit":                "The guest \"{guest_name}\" must have placed **fewer than** {max_room_service_orders_per_day} room service orders for room \"{room_id}\" on the current interaction date.",
    "within_room_service_hours":                            "The current interaction time must be between \"{room_service_start}\" and \"{room_service_end}\" on the interaction date.",
    "payment_with_loyalty_points":                          "The \"{payment_method}\" must be set to \"loyalty_points\".",
    "sufficient_payment_for_room_service":                  "If the \"{payment_method}\" is not \"loyalty_points\", then the \"{amount}\" must be **greater than or equal to** the cost of \"{order_items}\" in the \"{order_type}\" category."\
                                                            + " Otherwise, the guest \"{guest_name}\" must have enough loyalty points to cover the total room service cost (10 points per dollar).",
    "is_gold_or_higher_member":                             "The guest \"{guest_name}\" must have a loyalty tier of either \"gold\" or \"platinum\".",
    "amount_positive_restr":                                "The user parameter key \"{amount}\" is **greater than** zero.",
}

# all dependency types that could be in a action, each returns true or false
negative_constraint_descriptions = {
    "internal_valid_room_type":                             "The \"{room_type}\" **must not** match any of the room types currently offered by the hotel.",
    "internal_is_loyalty_member":                           "The guest \"{guest_name}\" **must not** be enrolled in the hotel's loyalty program.",
    "internal_valid_room_change_reason":                    "The \"{reason}\" **must not** be one of the accepted reasons for requesting a room change.",
    "internal_valid_room_service_order_type":               "The \"{order_type}\" **must not** match any recognized category of room service offered by the hotel.",
    "internal_valid_room_service_item":                     "**One or more** items in the input \"{order_items}\" **must not** belong to the \"{order_type}\" category of room service.",
    "internal_valid_room_id":                               "The \"{room_id}\" **must not** exist in the availability records of a room type offered by the hotel.",
    "internal_valid_room_service_payment_method":           "The \"{payment_method}\" **must not** be listed as one of the accepted payment methods for room service.",
    # state tracker constraints
    "valid_booking_date_pair":                              "The \"{check_in_date}\" **must** come **on or after** the \"{check_out_date}\".",
    "room_type_available_for_dates":                        "The \"{room_type}\" **must not** have **any** single room available for the entire date span from \"{check_in_date}\" up to (but not including) \"{check_out_date}\".",
    "is_booking_date_within_lead_time_range":               "The \"{check_in_date}\" must be **earlier than** {min_booking_lead_time_days} days after or **later than** {max_booking_lead_time_days} days after the current interaction date.",
    "has_exceeded_maximum_stays":                           "The stay from \"{check_in_date}\" to \"{check_out_date}\" must span **exactly** {max_stays} nights **or fewer**.",
    "sufficient_amount_for_booking":                        "The \"{amount}\" must be **less than** the total booking cost for the selected \"{room_type}\" from \"{check_in_date}\" to \"{check_out_date}\".",
    "has_overlapping_booking_for_booking":                  "The guest \"{guest_name}\" **must not** have any existing booking that overlaps with the new date range from \"{check_in_date}\" to \"{check_out_date}\" when booking.",
    "has_overlapping_booking_for_modification":             "The guest \"{guest_name}\" **must not** have any existing booking, excluding the one from \"{old_check_in_date}\" to \"{old_check_out_date}\","\
                                                            + " that overlaps with the new date range from \"{check_in_date}\" to \"{check_out_date}\" when modifying their reservation.",
    "before_modification_deadline":                         "The current interaction time must be **later than** {modification_deadline_hours} hours before {check_in_time} on \"{check_in_date}\".",
    "has_confirmed_reservation":                            "The guest \"{guest_name}\" must not have any reservation from \"{check_in_date}\" to \"{check_out_date}\" with status marked as \"confirmed\".",
    "sufficient_amount_for_reservation_modification":       "The \"{amount}\" must be **less than** the difference in booking cost when modifying from the original stay (\"{old_check_in_date}\" to \"{old_check_out_date}\")"
                                                            +" to the new stay (\"{check_in_date}\" to \"{check_out_date}\") with a new room type \"{room_type}\".",
    "valid_identification":                                 "The \"{identification}\" must include a \"type\" that **does not match** any of {valid_document_types} or an invalid \"birthday\" indicating the guest is **less than** {min_age} years old.",
    "after_check_in_time":                                  "The current interaction time must be **before** the check-in time {check_in_time} on the interaction date.",
    "before_check_out_time":                                "The current interaction time must be **on or after** the check-out time {check_out_time} on the interaction date.",
    "guest_already_checked_in":                             "The guest \"{guest_name}\" **must not** be listed in the room check-in records.",
    "room_key_returned":                                    "The input \"{key_returned}\" must be set to **false**.",
    "room_type_available_for_room_change":                  "The \"{room_type}\" **must not** have any room available for all remaining nights between the current interaction date and the \"check_out_date\" in the reservation of the checked-in guest \"{guest_name}\".",
    "has_remaining_nights":                                 "The checked-in guest \"{guest_name}\" **must not** have any nights remaining between the current interaction date and the \"check_out_date\" in their reservation.",
    "sufficient_amount_for_room_change_fee":                "The checked-in guest \"{guest_name}\" must provide an amount \"{amount}\" that is *less than** the additional fee for changing from the original room type to \"{room_type}\""
                                                            + " for the remaining nights between the current interaction date and the \"check_out_date\" in their reservation.",
    "within_max_room_changes":                              "The number of room changes for the checked-in guest \"{guest_name}\" must be **greater than or equal to** {max_room_changes}.",
    "within_room_service_order_daily_limit":                "The guest \"{guest_name}\" must have already placed **{max_room_service_orders_per_day} or more** room service orders for room \"{room_id}\" on the current interaction date.",
    "within_room_service_hours":                            "The current interaction time must be **before** \"{room_service_start}\" or **after** \"{room_service_end}\" on the interaction date.",
    "payment_with_loyalty_points":                          "The \"{payment_method}\" **must not** be set to \"loyalty_points\".",
    "sufficient_payment_for_room_service":                  "If the \"{payment_method}\" is not \"loyalty_points\", then the \"{amount}\" must be **less than** the cost of \"{order_items}\" in the \"{order_type}\" category."\
                                                            + " Otherwise, the guest \"{guest_name}\" **must not** have enough loyalty points to cover the total room service cost (10 points per dollar).",
    "is_gold_or_higher_member":                             "The guest \"{guest_name}\" **must** have a loyalty tier of \"silver\".",
    "amount_positive_restr":                                "The user parameter key \"{amount}\" is **less than or equal to** zero.",
}

# links the dependency to the action that changes its state in the state tracker, should be one to one
constraint_links = {}

# defines the dependencies of constraints based on functionality needs, mainly used for task generation verification
constraint_dependencies = {
    "room_type_available_for_dates":                        ("and", [
                                                                ("single", "internal_valid_room_type", {"room_type": "room_type"}),
                                                                ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"})
                                                            ]),
    "has_exceeded_maximum_stays":                           ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
    "sufficient_amount_for_booking":                        ("and", [
                                                                ("single", "internal_valid_room_type", {"room_type": "room_type"}),
                                                                ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                                ("single", "amount_positive_restr", {"amount": "amount"})
                                                            ]),
    "has_overlapping_booking_for_booking":                  ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
    "has_overlapping_booking_for_modification":             ("and", [
                                                                ("single", "valid_booking_date_pair", {"check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"}),
                                                                ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                                ("single", "has_confirmed_reservation", {"guest_name": "guest_name", "check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"})
                                                            ]),
    "has_confirmed_reservation":                            ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
    "sufficient_amount_for_reservation_modification":       ("and", [
                                                                ("single", "internal_valid_room_type", {"room_type": "room_type"}),
                                                                ("single", "valid_booking_date_pair", {"check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"}),
                                                                ("single", "valid_booking_date_pair", {"check_in_date": "check_in_date", "check_out_date": "check_out_date"}),
                                                                ("single", "has_confirmed_reservation", {"guest_name": "guest_name", "check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"}),
                                                                ("single", "amount_positive_restr", {"amount": "amount"}),
                                                            ]),
    "room_type_available_for_room_change":                  ("and", [
                                                                ("single", "internal_valid_room_type", {"room_type": "room_type"}),
                                                                ("single", "has_remaining_nights", {"guest_name": "guest_name"})
                                                            ]),
    "has_remaining_nights":                                 ("single", "guest_already_checked_in", {"guest_name": "guest_name"}),
    "sufficient_amount_for_room_change_fee":                ("and", [
                                                                ("single", "room_type_available_for_room_change", {"guest_name": "guest_name", "room_type": "room_type"}),
                                                                ("single", "amount_positive_restr", {"amount": "amount"})
                                                            ]),
    "within_max_room_changes":                              ("single", "guest_already_checked_in", {"guest_name": "guest_name"}),
    "within_room_service_order_daily_limit":                ("and", [
                                                                ("single", "internal_valid_room_id", {"room_id": "room_id"}),
                                                                ("single", "guest_already_checked_in", {"guest_name": "guest_name"}),
                                                            ]),
    "payment_with_loyalty_points":                          ("single", "internal_valid_room_service_payment_method", {"payment_method": "payment_method"}),
    "sufficient_payment_for_room_service":                  ("and", [
                                                                ("single", "internal_valid_room_service_payment_method", {"payment_method": "payment_method"}),
                                                                ("single", "internal_valid_room_service_item", {"order_type": "order_type", "order_items": "order_items"}),
                                                                ("or", [
                                                                    ("single", "not payment_with_loyalty_points", {"payment_method": "payment_method"}),
                                                                    ("single", "internal_is_loyalty_member", {"guest_name": "guest_name"}),
                                                                ]),
                                                            ]),
    "is_gold_or_higher_member":                             ("single", "internal_is_loyalty_member", {"guest_name": "guest_name"})
}

# full list of actions the assistant needs to call to successfully verify the constraint, mutually exclusive with constraint_links
constraint_processes = {
    # internal constraints
    "internal_valid_room_type":                             ("single", "internal_valid_room_type", {"room_type": "room_type"}),
    "internal_is_loyalty_member":                           ("single", "internal_is_loyalty_member", {"guest_name": "guest_name"}),
    "internal_valid_room_change_reason":                    ("or", [
                                                                ("single", "internal_valid_room_change_reason", {"reason":"reason"}),
                                                                ("single", "show_room_change_options", {})
                                                            ]),
                                                             
    "internal_valid_room_service_order_type":               ("single", "internal_valid_room_service_order_type", {"order_type": "order_type"}),
    "internal_valid_room_service_item":                     ("single", "internal_valid_room_service_item", {"order_type": "order_type", "order_items": "order_items"}),
    "internal_valid_room_id":                               ("single", "internal_valid_room_id", {"room_id": "room_id"}),
    "internal_valid_room_service_payment_method":           ("single", "internal_valid_room_service_payment_method", {"payment_method": "payment_method"}),
    # state tracker constraints
    "valid_booking_date_pair":                              None,
    "room_type_available_for_dates":                        ("single", "show_available_rooms", {}),
    "is_booking_date_within_lead_time_range":               ("single", "internal_get_interaction_time", {}),
    "has_exceeded_maximum_stays":                           None,
    "sufficient_amount_for_booking":                        ("single", "show_available_rooms", {}),
    "has_overlapping_booking_for_booking":                  ("single", "internal_get_booking_details", {}),
    "has_overlapping_booking_for_modification":             ("or", [
                                                                ("and", [
                                                                    ("single", "internal_get_booking_details", {}),
                                                                    ("single", "find_booking_info", {"guest_name": "guest_name", "check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"})
                                                                ]),
                                                                ("single", "internal_get_booking_details", {}),
                                                            ]),
    "before_modification_deadline":                         ("single", "internal_get_interaction_time", {}),
    "has_confirmed_reservation":                            ("or", [
                                                                ("single", "internal_get_booking_details", {}),
                                                                ("single", "find_booking_info", {"guest_name": "guest_name", "check_in_date": "check_in_date", "check_out_date": "check_out_date"})
                                                            ]),
    "sufficient_amount_for_reservation_modification":       ("and", [
                                                                ("or", [
                                                                    ("single", "internal_get_booking_details", {}),
                                                                    ("single", "find_booking_info", {"guest_name": "guest_name", "check_in_date": "old_check_in_date", "check_out_date": "old_check_out_date"})
                                                                ]),
                                                                ("single", "show_available_rooms", {})
                                                            ]),
    "valid_identification":                                 ("single", "internal_get_interaction_time", {}),
    "after_check_in_time":                                  ("single", "internal_get_interaction_time", {}),
    "before_check_out_time":                                ("single", "internal_get_interaction_time", {}),
    "guest_already_checked_in":                             ("or", [
                                                                ("and", [
                                                                    ("single", "internal_get_booking_details", {}),
                                                                    ("single", "internal_get_room_checkin_details", {})
                                                                ]),
                                                                ("single", "internal_get_booking_details", {}),
                                                            ]),
    "room_key_returned":                                    None,
    "room_type_available_for_room_change":                  ("and", [
                                                                ("single", "show_available_rooms", {}),
                                                                ("single", "internal_get_interaction_time", {}),
                                                                ("single", "internal_get_booking_details", {}),
                                                            ]),
    "has_remaining_nights":                                 ("and", [
                                                                ("single", "internal_get_interaction_time", {}),
                                                                ("single", "internal_get_booking_details", {})
                                                            ]),
    "sufficient_amount_for_room_change_fee":                ("and", [
                                                                ("single", "internal_get_interaction_time", {}),
                                                                ("single", "internal_get_booking_details", {}),
                                                            ]),
    "within_max_room_changes":                              ("single", "internal_get_booking_details", {}),
    "within_room_service_order_daily_limit":                ("and", [
                                                                ("single", "internal_get_interaction_time", {}),
                                                                ("single", "internal_get_booking_details", {}),
                                                                ("single", "internal_get_room_assignment", {})
                                                            ]),
    "within_room_service_hours":                            ("single", "internal_get_interaction_time", {}),
    "payment_with_loyalty_points":                          None,
    "sufficient_payment_for_room_service":                  ("or", [
                                                                ("single", "internal_compute_room_service_order_fee", {"order_type": "order_type", "order_items": "order_items"}),
                                                                ("and", [
                                                                    ("single", "internal_compute_room_service_order_fee", {"order_type": "order_type", "order_items": "order_items"}),
                                                                    ("single", "internal_get_loyalty_member_info", {"guest_name": "guest_name"})
                                                                ])
                                                            ]),
    "is_gold_or_higher_member":                             ("single", "internal_get_loyalty_member_info", {"guest_name": "guest_name"}),
    "amount_positive_restr":                                None
}

# method parameters may have parameters that do not go into user_known because they should be filled by the assistant
action_params_user_not_needed = {}

# descriptions of parameters in the funcitons and actions
action_param_descriptions = {
    "guest_name":                            "A string representing the name of the guest.",
    "room_type":                             "A string representing the category of room the guest wishes to book or switch to.",
    "check_in_date":                         "A string of the format \"YYYY-MM-DD\" representing the date when the guest expects to check in.",
    "check_out_date":                        "A string of the format \"YYYY-MM-DD\" representing the date when the guest expects to check out.",
    "amount":                                "A float representing the amount of money provided by the user for a given transaction.",
    "old_check_in_date":                     "A string of the format \"YYYY-MM-DD\" representing the original check-in date before modification.",
    "old_check_out_date":                    "A string of the format \"YYYY-MM-DD\" representing the original check-out date before modification.",
    "identification":                        "A dictionary of the guest's identification document, including the type of the document and the guest's birthday.",
    "type":                                  "A string representing the type of the identification document (e.g., passport, driver_license).",
    "birthday":                              "A string representing the guest's date of birth in YYYY-MM-DD format.",
    "key_returned":                          "A boolean value indicating whether the guest has returned their room key upon checkout.",
    "reason":                                "A string representing the reason for a room change request.",
    "room_id":                               "A string representing the ID of a specific room.",
    "order_type":                            "A string representing a category of the room service provided by the hotel.",
    "order_items":                           "A list of objects representing each room service order entry, where each object contains a \"name\" field for the menu item and a \"quantity\" field for how many of that item to order.",
    "payment_method":                        "A string indicating how the guest will pay for the room service."
}

# actions the assistant can take
actions = [
    {
        "name": "show_available_rooms",
        "description": get_action_full_description(action_descriptions, action_returns, "show_available_rooms"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "show_room_change_options",
        "description": get_action_full_description(action_descriptions, action_returns, "show_room_change_options"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "book_room",
        "description": get_action_full_description(action_descriptions, action_returns, "book_room"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "room_type": {
                    "type": "string", 
                    "description": action_param_descriptions["room_type"]
                },
                "check_in_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_in_date"]
                },
                "check_out_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_out_date"]
                },
                "amount": {
                    "type": "number", 
                    "description": action_param_descriptions["amount"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "room_type", "check_in_date", "check_out_date", "amount"]
        }
    },
    {
        "name": "find_booking_info",
        "description": get_action_full_description(action_descriptions, action_returns, "find_booking_info"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "check_in_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_in_date"]
                },
                "check_out_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_out_date"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "check_in_date", "check_out_date"]
        }
    },
    {
        "name": "cancel_reservation",
        "description": get_action_full_description(action_descriptions, action_returns, "cancel_reservation"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "check_in_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_in_date"]
                },
                "check_out_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_out_date"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "check_in_date", "check_out_date"]
        }
    },
    {
        "name": "modify_reservation",
        "description": get_action_full_description(action_descriptions, action_returns, "modify_reservation"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "old_check_in_date": {
                    "type": "string", 
                    "description": action_param_descriptions["old_check_in_date"]
                },
                "old_check_out_date": {
                    "type": "string", 
                    "description": action_param_descriptions["old_check_out_date"]
                },
                "check_in_date": {
                    "type": "string",
                    "description": action_param_descriptions["check_in_date"]
                },
                "check_out_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_out_date"]
                },
                "room_type": {
                    "type": "string", 
                    "description": action_param_descriptions["room_type"]
                },
                "amount": {
                    "type": "number", 
                    "description": action_param_descriptions["amount"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "old_check_in_date", "old_check_out_date", "check_in_date", "check_out_date", "room_type", "amount"]
        }
    },
    {
        "name": "process_guest_checkin",
        "description": get_action_full_description(action_descriptions, action_returns, "process_guest_checkin"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "check_in_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_in_date"]
                },
                "check_out_date": {
                    "type": "string", 
                    "description": action_param_descriptions["check_out_date"]
                },
                "identification": {
                    "type": "object", 
                    "description": action_param_descriptions["identification"],
                    "properties": {
                        "type": {
                            "type": "string",
                            "description": action_param_descriptions["type"]
                        },
                        "birthday": {
                            "type": "string",
                            "description": action_param_descriptions["birthday"]
                        }
                    },
                    "additionalProperties": False,
                    "required": ["type", "birthday"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "check_in_date", "check_out_date", "identification"]
        }
    },
    {
        "name": "process_guest_checkout",
        "description": get_action_full_description(action_descriptions, action_returns, "process_guest_checkout"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "key_returned": {
                    "type": "boolean", 
                    "description": action_param_descriptions["key_returned"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "key_returned"]
        }
    },
    {
        "name": "request_room_change",
        "description": get_action_full_description(action_descriptions, action_returns, "request_room_change"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "amount": {
                    "type": "number", 
                    "description": action_param_descriptions["amount"]
                },
                "reason": {
                    "type": "string", 
                    "description": action_param_descriptions["reason"]
                },
                "room_type": {
                    "type": "string", 
                    "description": action_param_descriptions["room_type"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "amount", "reason", "room_type"]
        }
    },
    {
        "name": "place_room_service_order",
        "description": get_action_full_description(action_descriptions, action_returns, "place_room_service_order"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                },
                "room_id": {
                    "type": "string", 
                    "description": action_param_descriptions["room_id"]
                },
                "order_type": {
                    "type": "string", 
                    "description": action_param_descriptions["order_type"]
                },
                "order_items": {
                    "type": "array",
                    "description": action_param_descriptions["order_items"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The name of the menu item."
                            },
                            "quantity": {
                                "type": "integer",
                                "description": "Quantity for the menu item."
                            }
                        },
                        "additionalProperties": False,
                        "required": ["name", "quantity"]
                    }
                },
                "payment_method": {
                    "type": "string", 
                    "description": action_param_descriptions["payment_method"]
                },
                "amount": {
                    "type": "number", 
                    "description": action_param_descriptions["amount"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name", "room_id", "order_type", "order_items", "payment_method"]
        }
    },
    {
        "name": "register_loyalty_member",
        "description": get_action_full_description(action_descriptions, action_returns, "register_loyalty_member"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name"]
        }
    },
    {
        "name": "internal_get_room_checkin_details",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_room_checkin_details"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_get_booking_details",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_booking_details"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_get_loyalty_member_info",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_loyalty_member_info"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name"]
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
    },
    {
        "name": "internal_get_room_service_order_details",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_room_service_order_details"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_get_room_assignment",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_get_room_assignment"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": []
        }
    },
    {
        "name": "internal_compute_room_service_order_fee",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_compute_room_service_order_fee"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "order_type": {
                    "type": "string", 
                    "description": action_param_descriptions["order_type"]
                },
                "order_items": {
                    "type": "array",
                    "description": action_param_descriptions["order_items"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The name of the menu item."
                            },
                            "quantity": {
                                "type": "integer",
                                "description": "Quantity for the menu item."
                            }
                        },
                        "additionalProperties": False,
                        "required": ["name", "quantity"]
                    }
                },
            },
            "additionalProperties": False,
            "required": ["order_type", "order_items"]
        }
    },
    {
        "name": "internal_valid_room_type",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_room_type"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "room_type": {
                    "type": "string", 
                    "description": action_param_descriptions["room_type"]
                }
            },
            "additionalProperties": False,
            "required": ["room_type"]
        }
    },
    {
        "name": "internal_is_loyalty_member",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_is_loyalty_member"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "guest_name": {
                    "type": "string", 
                    "description": action_param_descriptions["guest_name"]
                }
            },
            "additionalProperties": False,
            "required": ["guest_name"]
        }
    },
    {
        "name": "internal_valid_room_change_reason",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_room_change_reason"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string", 
                    "description": action_param_descriptions["reason"]
                }
            },
            "additionalProperties": False,
            "required": ["reason"]
        }
    },
    {
        "name": "internal_valid_room_service_order_type",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_room_service_order_type"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "order_type": {
                    "type": "string", 
                    "description": action_param_descriptions["order_type"]
                }
            },
            "additionalProperties": False,
            "required": ["order_type"]
        }
    },
    {
        "name": "internal_valid_room_service_item",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_room_service_item"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "order_type": {
                    "type": "string", 
                    "description": action_param_descriptions["order_type"]
                },
                "order_items": {
                    "type": "array",
                    "description": action_param_descriptions["order_items"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The name of the menu item."
                            },
                            "quantity": {
                                "type": "integer",
                                "description": "Quantity for the menu item."
                            }
                        },
                        "additionalProperties": False,
                        "required": ["name", "quantity"]
                    }
                },
            },
            "additionalProperties": False,
            "required": ["order_type", "order_items"]
        }
    },
    {
        "name": "internal_valid_room_id",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_room_id"),
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
        "name": "internal_valid_room_service_payment_method",
        "description": get_action_full_description(action_descriptions, action_returns, "internal_valid_room_service_payment_method"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "payment_method": {
                    "type": "string", 
                    "description": action_param_descriptions["payment_method"]
                }
            },
            "additionalProperties": False,
            "required": ["payment_method"]
        }
    }
]