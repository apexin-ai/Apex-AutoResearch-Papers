# todo -> constraint_actions_required write ors + ands + singles, regenerate market + healthcare, etc...

from env.helpers import get_action_full_description

"""
This file contains the information for the online_market assistant for the OpenAI API.
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

name = "Online_market Assistant"

instructions = "You are an online market assistant, responsible for assisting users with managing their online shopping experience."\
                    +"Your role involves supporting various functions related to accounts, orders, products, and transactions."\
                    +"You will handle tasks that a typical online marketplace clerk would manage"



action_descriptions = {
    # root functions
    "login_user":                   "Logs in the user to authenticate them for accessing their online market account using a username and password.",
    "logout_user":                  "Logs out the user by clearing their session information.",
    
    # domain functions
    "add_to_cart":                  "Adds a specified product to the user's cart with the desired quantity. Updates product stock accordingly.",
    "view_cart":                    "Displays the current contents of the user's cart, including product details and total cost.",
    "place_order":                  "Places an order for all items in the user's cart.",
    "view_order_history":           "Retrieves the user's complete order history, including order details and statuses.",
    "add_shipping_address":         "Adds a new shipping address to the user's account.",
    "view_shipping_addresses":      "Lists all shipping addresses associated with the user's account, indicating the default address.",
    "get_product_details":          "Retrieves detailed information about a specific product, including price, stock, and reviews.",
    "add_review":                   "Submits a review for a specific product, including a rating and an optional comment. Updates the product's average rating.",
    "get_order_details": "Fetches detailed information about a specific order, including the order items, status, cost, address, placed date, and number of exchanges.",

    "cancel_order":                 "Cancels a specific order placed by the user, marking its status as canceled.",
    "return_order":                 "Processes a return for a delivered order.",
    "exchange_product":             "Initiates a product exchange for an order, updating the order details accordingly.",
    "use_coupon":                   "Applies a valid coupon to the user's current cart, adjusting the total price.",
    "get_coupons_used":             "Retrieves all used coupons by a user.",

   
    
    # internal functions
    "internal_get_database":        "Displays the complete database of the online market, including accounts, products, orders, and coupons."\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_username_exist":"Checks if a specific username exists in the accounts database."\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_product_exist":"Checks if a specific product exists in the products database."\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_coupon_exist": "Checks if a specific coupon exists in the coupons database."\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_user_credit_status": "Retrieves the user's credit status"\
        + " This is an internal action, only accessible by the assistant.",
    "internal_check_order_exist": "Checks if an order exists under a user."\
        +" This is an internal action, only accessible by the assistant.",
    "internal_get_interaction_time": "Retrieves the current interaction timestamp recorded in the database."\
        + " This is an internal action, only accessible by the assistant.",
    "internal_get_coupon_details": "Fetches details of a specific coupon, such as product valibility and expiration date."\
        + " This is an internal action, only accessible by the assistant.",


    
    

}


action_returns = {
    # Root functions
    "login_user": "Returns true or false for successful or failed login based on provided credentials.",
    "logout_user": "Returns true always because logout is successful.",

    # Domain functions
    "add_to_cart": "Returns true or false for successful addition of a product to the cart.",
    "view_cart": "Returns a list containing the cart's contents.",
    "place_order": "Returns true for successful order placement or false for failure.",
    "view_order_history": "Returns a list containing the user's order history.",
    "add_shipping_address": "Returns true or false for successful addition of a new shipping address.",
    "view_shipping_addresses": "Returns a list containing all the user's shipping addresses.",
    "get_product_details": "Returns a dictionary containing product details.",
    "add_review": "Returns true or false for successful addition of a product review.",
    "cancel_order": "Returns a true or false indicating whether the order cancellation was successful.",
    "return_order": "Returns a true or false indicating whether the return was successfully initiated.",
    "exchange_product": "Returns a true or false indicating whether the product exchange was successfully initiated.",
    "use_coupon": "Returns a true or false indicating whether the coupon was successfully applied to the cart.",
    "get_order_details": "Returns a dictionary containing detailed information about the order, including the order items, status, cost, address, placed date, coupons used, and number of exchanges. The order status can include 'Processing', 'Shipped', 'Delivered', 'Refunding', 'Refunded', or 'Canceled'.",
    "get_coupons_used": "Returns a list of all coupons used.",


    # Internal functions
    "internal_get_database": "Returns the entire database in JSON format.",
    "internal_check_username_exist": "Returns true or false based on whether the username exists in the accounts database.",
    "internal_check_product_exist": "Returns true or false based on whether the product ID exists in the products database.",
    "internal_check_coupon_exist": "Returns true or false based on whether the coupon_code exists in the coupons database.",
    "internal_check_user_credit_status": "Returns a string indicating the user's credit status, such as 'excellent', 'good', or 'restricted'.",
    "internal_check_order_exist": "Returns true or false based on whether an order exists under a user.",
    "internal_get_interaction_time": "Returns the current interaction time as a string in ISO 8601 format.",
    "internal_get_coupon_details": "Returns a dictionary containing details about the specified coupon, such as expiration date, applicable products, and discount amount.",
}




action_innate_dependencies = {
    "login_user":                           ("single", "internal_check_username_exist", {"username": "username"}),
    "logout_user":                          None,
    "add_to_cart":                          ("and",[
                                                ("single", "internal_check_product_exist", {"product_id": "product_id"}),
                                                ("single", "amount_positive_restr", {"amount":"quantity"})
                                            ]),

    "view_cart":                            None,
    "place_order":                          None,

    "view_order_history":                   None,
    "add_shipping_address":                 None,
    "view_shipping_addresses":              None,
    "get_product_details":                  ("single", "internal_check_product_exist", {"product_id": "product_id"}),
    "add_review":                           ("single", "internal_check_product_exist", {"product_id": "product_id"}),

    "cancel_order":                         None,
    "return_order":                         None,
    "exchange_product":                     ("and",[
                                                ("single", "internal_check_product_exist", {"product_id": "new_product_id"}),
                                                ("single", "internal_check_product_exist", {"product_id": "old_product_id"}),
                                                ("single", "amount_positive_restr", {"amount":"quantity"})
                                            ]),
    "use_coupon":                           ("single", "internal_check_coupon_exist", {"coupon_code": "coupon_code"}),
    "get_order_details":                    None,
    "get_coupons_used":                     None,

    "internal_check_coupon_exist":         None,
    "internal_check_user_credit_status":    ("single", "internal_check_username_exist", {"username": "username"}),
    "internal_get_interaction_time":        None,
    "internal_get_coupon_details":          ("single", "internal_check_coupon_exist", {"coupon_code": "coupon_code"}),
    "internal_get_database":                None,
    "internal_check_username_exist":        None,
    "internal_check_product_exist":        None,
    "internal_check_order_exist":           ("single", "internal_check_username_exist", {"username": "username"}),
}



action_required_dependencies = {
    "login_user":                   None,
    "logout_user":                  None,
  # Domain functions
    "add_to_cart":                  ("single", "logged_in_user", {"username": "username"}),

    "view_cart":                    ("single", "logged_in_user", {"username": "username"}),

    "place_order":                  ("and", [
                                        ("single", "has_items_in_cart", {"username": "username"}),
                                        ("single", "has_shipping_address", {"username": "username"}),
                                        ("single", "logged_in_user", {"username": "username"})
                                    ]),
    "view_order_history":           ("single", "logged_in_user", {"username": "username"}),

    "add_shipping_address":         ("single", "logged_in_user", {"username": "username"}),

    "view_shipping_addresses":      ("single", "logged_in_user", {"username": "username"}),

    "get_product_details":          None, #idk
    "add_review":                   ("single", "logged_in_user", {"username": "username"}),
    "get_coupons_used":             ("single", "logged_in_user", {"username": "username"}),


    "cancel_order":                 ("and",[
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
                                    ]),
    "return_order":                 ("and",[
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
                                    ]),
    "exchange_product":             ("and",[
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
                                        ("single", "product_exists_in_order", {"username": "username","order_id":"order_id", "product_id": "old_product_id"}),
                                    ]),
    "use_coupon":                   ("and",[
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
                                    ]),
    "get_order_details":            ("and",[
                                        ("single", "logged_in_user", {"username": "username"}),
                                        ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
                                    ]),

    "internal_check_coupon_exist": None,
    "internal_check_user_credit_status":    None,
    "internal_get_interaction_time": None,
    "internal_get_coupon_details":          None,
    "internal_check_order_exist":           None,

    


    
    

    # Internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_product_exist":None,

}

action_customizable_dependencies = {
    "login_user":                   None,
    "logout_user":                  ("single", "internal_check_username_exist", {"username": "username"}),
    # account functions
    
    "add_to_cart":                  ("single", "enough_stock", {"product_id": "product_id", "quantity": "quantity"}),

    "view_cart":                    None,
    "place_order":                  ("single", "credit_status_not_suspended", {"username": "username"}), 

    "view_order_history":           None,

    "add_shipping_address":         ("single", "not_already_added_shipping_address", {"username": "username", "address": "address"}),

    "view_shipping_addresses":      None,

    "get_product_details":          None,
    "get_coupons_used":             None,
    "add_review":                   [
                                        ("single", "within_review_limits", {"rating": "rating"}),
                                        ("single", "unique_review", {"product_id": "product_id", "username": "username"}),
                                        ("single", "product_bought_by_user", {"username": "username", "product_id": "product_id"}),
                                        ("single", "credit_status_not_restricted_or_suspended", {"username": "username"})
                                    ],


    "cancel_order":                 ("single", "order_processing", {"username": "username", "order_id": "order_id"}),
                                    
    "return_order":                 [
                                        ("single", "order_delivered", {"username": "username", "order_id": "order_id"}),
                                        ("or",[
                                            ("single", "within_return_period", {"username": "username", "order_id": "order_id"}),
                                            ("single", "credit_status_excellent", {"username": "username"}),
                                        ]),
                                    ],
    "exchange_product":              [
                                        ("single", "order_delivered", {"username": "username", "order_id": "order_id"}),
                                        ("single", "enough_stock", {"product_id": "new_product_id", "quantity": "quantity"}),
                                        ("or",[
                                            ("and",[
                                                ("single", "within_exchange_period", {"username": "username", "order_id": "order_id"}),
                                                ("single", "less_than_max_exchanges", {"username": "username", "order_id": "order_id"})
                                            ]),
                                            ("single", "credit_status_excellent", {"username": "username"})
                                        ])
                                    ],
    "use_coupon":                   [
                                        ("single", "coupon_valid", {"coupon_code": "coupon_code", "username": "username", "order_id": "order_id"}),
                                        ("single", "coupon_not_expired", {"coupon_code": "coupon_code"}),
                                        ("single", "credit_status_not_restricted_or_suspended", {"username": "username"}),
                                        ("single", "coupon_not_already_used", {"username": "username", "coupon_code": "coupon_code"}),
                                    ],
    "get_order_details":            None,

    
    "internal_check_coupon_exist": None,
    "internal_check_user_credit_status":    None,
    "internal_get_interaction_time": None,
    "internal_get_coupon_details":          None,
    "internal_check_order_exist":           None,

    





    # Internal functions
    "internal_get_database":        None,
    "internal_check_username_exist":None,
    "internal_check_product_exist":None,

}
#internal check email exists


constraint_links = {
    "logged_in_user":   ("login_user", {"username": "username"}),
}


positive_constraint_descriptions = {
    "logged_in_user":               "The user is logged in previously with the correct credentials to perform this action.",
    "login_user":                   "The user is able to login with the correct credentials of \"{username}\" and \"{password}\" to perform this action,"\
        + " matching the database credentials.",
    "internal_check_username_exist": "The user parameter key \"{username}\" **MUST EXIST** as a top-level key in the accounts section of the database.",
    "internal_check_product_exist": "The product ID parameter \"{product_id}\" **MUST EXIST** as a key in the products section of the database.",
    "internal_check_coupon_exist": "The coupon code \"{coupon_code}\" **MUST EXIST** in the coupons section of the database.",
    "enough_stock": "The product ID \"{product_id}\" must have sufficient stock to fulfill the requested quantity \"{quantity}\" in the database.",
    "has_shipping_address": "The user \"{username}\" **MUST HAVE** at least one shipping address registered in their account to perform this action.",
    "within_review_limits": "The rating parameter \"{rating}\" **MUST BE WITHIN** the allowed range of {rating_lower_bound} to {rating_upper_bound} (inclusive) to perform this action.",
    "has_items_in_cart": "The user \"{username}\" **MUST HAVE** at least one item in their cart to perform this action.",
    "amount_positive_restr": "The amount parameter \"{amount}\" provided **MUST BE GREATER THAN ZERO** to perform this action.",
    "not_already_added_shipping_address": "The shipping address \"{address}\" **MUST NOT ALREADY EXIST** in the user's \"{username}\" shipping addresses section",
    "unique_review":  "The user \"{username}\" **MUST NOT HAVE** already reviewed the product with product ID \"{product_id}\".",
    "product_bought_by_user": "The user \"{username}\" **MUST HAVE** already ordered the product with product ID \"{product_id}\" to perform this action.",
    "internal_check_order_exist":             "The order with order ID \"{order_id}\" **MUST HAVE** been placed by the user \"{username}\" to perform this action.",
    "order_delivered":                  "The order with order ID \"{order_id}\" **MUST HAVE** a status of 'Delivered' to perform this action.",
    "order_processing":                 "The order with order ID \"{order_id}\" **MUST HAVE** a status of 'Processing' to perform this action.",
    "credit_status_not_restricted_or_suspended":     "The user \"{username}\" **MUST NOT HAVE** a credit status of 'restricted' or 'suspended' to perform this action.",
    "credit_status_not_suspended":      "The user \"{username}\" **MUST NOT HAVE** a credit status of 'suspended' to perform this action.",
    "credit_status_excellent":          "The user \"{username}\" **MUST HAVE** a credit status of 'excellent' to perform this action.",
    "within_exchange_period":           "The interaction time falls within the allowable exchange period for the order with ID \"{order_id}\". "\
            +"The exchange period starts from the order placed date and extends for {exchange_period} days after the order placed date."\
            +"Both interaction time and order placed date are ISO 8601 formatted strings and are considered as date-time values.",
    "within_return_period":             "The interaction time falls within the allowable return period for the order with ID \"{order_id}\". "\
            +"The return period starts from the order placed date and extends for {return_period} days after the order placed date."\
            +"Both interaction time and order placed date are ISO 8601 formatted strings and are considered as date-time values.",
    "less_than_max_exchanges":          "The order with order ID \"{order_id}\" **MUST NOT EXCEED** the maximum exchange times of {max_exchange_times} to perform this action.",
    "coupon_not_expired":               "The coupon with code \"{coupon_code}\" **MUST HAVE** an expiration date **AFTER** the interaction time to be applied.",
    "coupon_valid":                     "The user \"{username}\" **MUST HAVE** applicable products in their order \"{order_id}\" to be able to use the coupon with code \"{coupon_code}\".",
    "coupon_not_already_used":          "The coupon with code \"{coupon_code}\" **MUST NOT HAVE** already been used by the user \"{username}\" to perform this action.",
    "product_exists_in_order":          "The product with ID \"{product_id}\" **MUST EXIST** in the order with order ID \"{order_id}\" placed by the user \"{username}\" to perform this action.",

   # "order_delivered_or_refunding":      "",


}


negative_constraint_descriptions = {
    "logged_in_user":               "The user is not logged in with the correct credentials to perform this action.",
    "login_user":                   "The user is unable to login with the incorrect credentials of \"{username}\" and \"{password}\" to perform this action, not matching the database credentials.",
    "internal_check_username_exist": "The user parameter key \"{username}\" **MUST NOT EXIST AT ALL** as a top-level key in the accounts section of the database.",
    "internal_check_product_exist": "The product ID parameter \"{product_id}\" **MUST NOT EXIST** as a key in the products section of the database.",
    "internal_check_coupon_exist": "The coupon code \"{coupon_code}\" **MUST NOT EXIST** in the coupons section of the database.",
    "enough_stock": "The product ID \"{product_id}\" must not have sufficient stock to fulfill the requested quantity \"{quantity}\" in the database.",
    "has_shipping_address": "The user \"{username}\" **MUST NOT HAVE** any shipping addresses registered in their account to perform this action.",
    "within_review_limits": "The rating parameter \"{rating}\" **MUST BE OUTSIDE** the allowed range of {rating_lower_bound} to {rating_upper_bound} (inclusive) to perform this action.",
    "has_items_in_cart": "The user \"{username}\" **MUST NOT HAVE** any items in their cart to perform this action.",
    "amount_positive_restr": "The amount parameter \"{amount}\" provided **MUST BE LESS THAN OR EQUAL TO ZERO** to perform this action.",
    "not_already_added_shipping_address": "The shipping address \"{address}\" **MUST ALREADY EXIST** in the user's \"{username}\" shipping addresses section.",
    "unique_review":  "The user \"{username}\" **MUST HAVE** already reviewed the product with product ID \"{product_id}\".",
    "product_bought_by_user": "The user \"{username}\" **MUST NOT HAVE** the product with product ID \"{product_id}\" in their ORDER HISTORY section with any ORDER to perform this action.",


    "internal_check_order_exist":       "The order with order ID \"{order_id}\" **MUST NOT HAVE** been placed by the user \"{username}\" to perform this action.",
    "order_delivered":                  "The order with order ID \"{order_id}\" **MUST NOT HAVE** a status of 'Delivered' to perform this action.",
    "order_processing":                 "The order with order ID \"{order_id}\" **MUST NOT HAVE** a status of 'Processing' to perform this action.",
    "credit_status_not_restricted_or_suspended":     "The user \"{username}\" **MUST HAVE** a credit status of 'restricted' or 'suspended' to perform this action.",
    "credit_status_not_suspended":      "The user \"{username}\" **MUST HAVE** a credit status of 'suspended' to perform this action.",
    "credit_status_excellent":          "The user \"{username}\" **MUST NOT HAVE** a credit status of 'excellent' to perform this action.",
    "within_exchange_period":           "The interaction time falls outside the allowable exchange period for the order with ID \"{order_id}\". "\
            +"The exchange period starts from the order_placed_date and extends for {exchange_period} days after the order_placed_date."\
            +"Both interaction time and order_placed_date are ISO 8601 formatted strings and are considered as date-time values.",
    "within_return_period":             "The interaction time falls outside the allowable return period for the order with ID \"{order_id}\". "\
            +"The return period starts from the order_placed_date and extends for {return_period} days after the order_placed_date."\
            +"Both interaction time and order_placed_date are ISO 8601 formatted strings and are considered as date-time values.",
    "less_than_max_exchanges":          "The order with order ID \"{order_id}\" **MUST EXCEED** the maximum exchange times of {max_exchange_times} allowed to perform this action.",
    "coupon_not_expired":               "The coupon with code \"{coupon_code}\" **MUST HAVE** an expiration date before the interaction time to be applied.",
    "coupon_valid":                     "The user \"{username}\" **MUST NOT HAVE** applicable products in their order \"{order_id}\" to be able to use the coupon with code \"{coupon_code}\".",
    "coupon_not_already_used":          "The coupon with code \"{coupon_code}\" **MUST HAVE** already been used by the user \"{username}\" to perform this action.",
    "product_exists_in_order":          "The product with ID \"{product_id}\" **MUST NOT EXIST** in the order with order ID \"{order_id}\" placed by the user \"{username}\" to perform this action.",
}


constraint_dependencies = {
    "within_review_limits":                             None,
    "amount_positive_restr":                            None,
    "enough_stock":                                     ("single", "internal_check_product_exist", {"product_id": "product_id"}),
    "has_shipping_address":                             ("single", "internal_check_username_exist", {"username": "username"}),
    "has_items_in_cart":                                ("single", "internal_check_username_exist", {"username": "username"}),
    "not_already_added_shipping_address":               ("single", "internal_check_username_exist", {"username": "username"}),
    "unique_review":                                    ("and", [
                                                            ("single", "internal_check_product_exist", {"product_id": "product_id"}),
                                                            ("single", "internal_check_username_exist", {"username": "username"}),
                                                        ]),

    "product_bought_by_user":                           ("single", "internal_check_username_exist", {"username": "username"}),

    "order_delivered":                                  ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
    "order_processing":                                 ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
    "credit_status_not_restricted_or_suspended":        ("single", "internal_check_username_exist", {"username": "username"}),
    "credit_status_not_suspended":                      ("single", "internal_check_username_exist", {"username": "username"}),
    "credit_status_excellent":                          ("single", "internal_check_username_exist", {"username": "username"}),

    "within_exchange_period":                           ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
    "within_return_period":                             ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
    "less_than_max_exchanges":                          ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
    "coupon_not_expired":                               ("single", "internal_check_coupon_exist", {"coupon_code": "coupon_code"}),
    "coupon_valid":                                     ("and", [
                                                            ("single", "internal_check_coupon_exist", {"coupon_code": "coupon_code"}),
                                                            ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),
                                                        ]),
    "coupon_not_already_used":                          ("single", "internal_check_username_exist", {"username": "username"}),

    "product_exists_in_order":                          ("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}),


}


# ("get_account_balance", {"username": "username"})
constraint_processes = {
    "within_review_limits":                             None,
    "amount_positive_restr":                            None,
    # "login_user":                                       ("or", [
    #                                                         ("single", "login_user", {"username": "username", "password": "[REDACTED]"}),
    #                                                         ("single", "internal_get_database", None)
    #                                                     ]),
                    

    "internal_check_username_exist":                    ("or", [("single", "internal_check_username_exist", {"username": "username"}), ("single", "internal_get_database", None)]),
    "internal_check_product_exist":                     ("or", [("single", "internal_check_product_exist", {"product_id": "product_id"}), ("single", "internal_get_database", None)]),
    "internal_check_coupon_exist":                      ("or", [("single", "internal_check_coupon_exist", {"coupon_code": "coupon_code"}), ("single", "internal_get_database", None)]),
    "internal_check_order_exist":                       ("or", [("single", "internal_check_order_exist", {"username": "username", "order_id": "order_id"}), ("single", "view_order_history", {"username": "username"}), ("single", "internal_get_database", None)]),


    "enough_stock":                                     ("or", [("single", "get_product_details", {"product_id": "product_id"}), ("single", "internal_get_database", None)]),
    "has_shipping_address":                             ("or", [("single", "view_shipping_addresses", {"username": "username"}), ("single", "internal_get_database", None)]),
    "has_items_in_cart":                                ("or", [("single", "view_cart", {"username": "username"}), ("single", "internal_get_database", None)]),
    "not_already_added_shipping_address":               ("or", [("single", "view_shipping_addresses", {"username": "username"}), ("single", "internal_get_database", None)]),
    "unique_review":                                    ("or", [("single", "get_product_details", {"product_id": "product_id"}), ("single", "internal_get_database", None)]),

    "product_bought_by_user":                           ("or", [("single", "view_order_history", {"username": "username"}), ("single", "internal_get_database", None)]),

    "order_delivered":                                  ("or", [("single", "get_order_details", {"username": "username", "order_id": "order_id"}), ("single", "view_order_history", {"username": "username"}), ("single", "internal_get_database", None)]),
    "order_processing":                                 ("or", [("single", "get_order_details", {"username": "username", "order_id": "order_id"}), ("single", "view_order_history", {"username": "username"}), ("single", "internal_get_database", None)]),
    "credit_status_not_restricted_or_suspended":        ("or", [("single", "internal_check_user_credit_status",  {"username": "username"}), ("single", "internal_get_database", None)]),
    "credit_status_not_suspended":                      ("or", [("single", "internal_check_user_credit_status",  {"username": "username"}), ("single", "internal_get_database", None)]),
    "credit_status_excellent":                          ("or", [("single", "internal_check_user_credit_status",  {"username": "username"}), ("single", "internal_get_database", None)]),


    "within_exchange_period":                           ("or", [
                                                            ("and", [
                                                                    ("or", [
                                                                        ("single","get_order_details", {"username": "username", "order_id": "order_id"}),
                                                                        ("single","view_order_history", {"username": "username"})
                                                                    ]),
                                                                    ("single", "internal_get_interaction_time", None),
                                                            ]),
                                                            ("single", "internal_get_database", None)
                                                        ]),
    "within_return_period":                             ("or", [
                                                            ("and", [
                                                                    ("or",[
                                                                        ("single","get_order_details", {"username": "username", "order_id": "order_id"}),
                                                                        ("single","view_order_history", {"username": "username"})
                                                                    ]),
                                                                    ("single", "internal_get_interaction_time", None),
                                                            ]),
                                                            ("single", "internal_get_database", None)
                                                        ]),


    "less_than_max_exchanges":                          ("or", [("single","get_order_details", {"username": "username", "order_id": "order_id"}), ("single","view_order_history", {"username": "username"}), ("single","internal_get_database", None)]),

    "coupon_not_expired":                               ("or", [
                                                            ("and", [
                                                                    ("single", "internal_get_coupon_details", {"coupon_code": "coupon_code"}),
                                                                    ("single", "internal_get_interaction_time", None),
                                                            ]),
                                                            ("single", "internal_get_database", None)
                                                        ]),

    "coupon_valid":                                     ("or", [
                                                            ("and", [
                                                                    ("single","internal_get_coupon_details", {"coupon_code": "coupon_code"}),
                                                                    ("or",[
                                                                        ("single","get_order_details", {"username": "username", "order_id": "order_id"}),
                                                                        ("single","view_order_history", {"username": "username"})
                                                                    ])
                                                            ]),
                                                            ("single", "internal_get_database", None)
                                                        ]),

    "coupon_not_already_used":                          ("or", [("single", "get_coupons_used", {"username": "username"}), ("single", "view_order_history", {"username": "username"}), ("single", "internal_get_database", None)]),

    "product_exists_in_order":                          ("or", [("single", "get_order_details", {"username": "username", "order_id": "order_id"}), ("single", "view_order_history", {"username": "username"}), ("single", "internal_get_database", None)]),
}

action_params_user_not_needed ={}

action_param_descriptions = {
    "username":                  "A string representing the user's account name.",
    "password":                  "[REDACTED] password associated with the user's account.",
    "product_id":                "The unique identifier for a specific product in the market.",
    "quantity":                  "The number of units of a product to add, remove, exchange, buy, etc.",
    "order_id":                  "The unique identifier for a specific order in the user's order history.",
    "address":                   "A full address to add to the user's shipping details.",
    "rating":                    "A numerical value representing the quality rating of a product (typically 1-5).",
    "comment":                   "A brief text description provided by the user as part of a product review.",
    "new_stock":                 "The qunatity added for a specific product.",
    "stock":                     "The initial quantity for a specific product.",
    "price":                     "The price for a specific product.",
    "description":               "The description for a specific product",
    "rating_lower_bound":        "The lowest rating possible for a specific product",
    "rating_upper_bound":        "The highest rating possible for a specific product",
    "index":                     "The index of the shipping address that is being set to default.",
    "coupon_code":               "The unique identifier for a specific coupon in the market",
    "old_product_id":            "The unique identifier for the product the user wants to exchange.",
    "new_product_id":            "The unique identifier for the product the user wants to exchange for.",
    
}

actions = [
    # Account functions
    {
        "name": "login_user",
        "description": get_action_full_description(action_descriptions, action_returns,"login_user"),
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
        "description": get_action_full_description(action_descriptions, action_returns,"logout_user"),
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

    # Cart functions
    {
        "name": "add_to_cart",
        "description": get_action_full_description(action_descriptions, action_returns,"add_to_cart"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "product_id": {
                    "type": "string",
                    "description": action_param_descriptions["product_id"]
                },
                "quantity": {
                    "type": "integer",
                    "description": action_param_descriptions["quantity"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "product_id", "quantity"]
        }
    },
    {
        "name": "view_cart",
        "description": get_action_full_description(action_descriptions, action_returns,"view_cart"),
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
        "name": "place_order",
        "description": get_action_full_description(action_descriptions, action_returns,"place_order"),
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
        "name": "view_order_history",
        "description": get_action_full_description(action_descriptions, action_returns,"view_order_history"),
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
        "name": "add_shipping_address",
        "description": get_action_full_description(action_descriptions, action_returns,"add_shipping_address"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "address": {
                    "type": "string",
                    "description": action_param_descriptions["address"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "address"]
        }
    },

    {
        "name": "view_shipping_addresses",
        "description": get_action_full_description(action_descriptions, action_returns,"view_shipping_addresses"),
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
        "name": "get_product_details",
        "description": get_action_full_description(action_descriptions, action_returns,"get_product_details"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "product_id": {
                    "type": "string",
                    "description": action_param_descriptions["product_id"]
                }
            },
            "additionalProperties": False,
            "required": ["product_id"]
        }
    },
    {
        "name": "add_review",
        "description": get_action_full_description(action_descriptions, action_returns,"add_review"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "product_id": {
                    "type": "string",
                    "description": action_param_descriptions["product_id"]
                },
                "rating": {
                    "type": "integer",
                    "description": action_param_descriptions["rating"]
                },
                "comment": {
                    "type": "string",
                    "description": action_param_descriptions["comment"]
                }
            },
            "additionalProperties": False,
            "required": ["username","product_id", "rating", "comment"]
        }
    },
    {
        "name": "cancel_order",
        "description": get_action_full_description(action_descriptions, action_returns,"cancel_order"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "order_id": {
                    "type": "string",
                    "description": action_param_descriptions["order_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "order_id"]
        }
    },
    {
        "name": "return_order",
        "description": get_action_full_description(action_descriptions, action_returns,"return_order"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "order_id": {
                    "type": "string",
                    "description": action_param_descriptions["order_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "order_id"]
        }
    },
    {
        "name": "exchange_product",
        "description": get_action_full_description(action_descriptions, action_returns,"exchange_product"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "order_id": {
                    "type": "string",
                    "description": action_param_descriptions["order_id"]
                },
                "old_product_id": {
                    "type": "string",
                    "description": action_param_descriptions["old_product_id"]
                },
                "new_product_id": {
                    "type": "string",
                    "description": action_param_descriptions["new_product_id"]
                },
                "quantity": {
                    "type": "number",
                    "description": action_param_descriptions["quantity"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "order_id", "old_product_id", "new_product_id", "quantity"]
        }
    },
    {
        "name": "use_coupon",
        "description": get_action_full_description(action_descriptions, action_returns,"use_coupon"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "order_id": {
                    "type": "string",
                    "description": action_param_descriptions["order_id"]
                },
                "coupon_code": {
                    "type": "string",
                    "description": action_param_descriptions["coupon_code"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "order_id", "coupon_code"]
        }
    },
        {
        "name": "get_order_details",
        "description": get_action_full_description(action_descriptions, action_returns,"get_order_details"),
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "order_id": {
                    "type": "string",
                    "description": action_param_descriptions["order_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "order_id"]
        }
    },
    {
        "name": "get_coupons_used",
        "description": get_action_full_description(action_descriptions, action_returns,"get_coupons_used"),
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
        "name": "internal_check_product_exist",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_check_product_exist"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "product_id": {
                    "type": "string",
                    "description": action_param_descriptions["product_id"]
                }
            },
            "additionalProperties": False,
            "required": ["product_id"]
        }
    },
    {
        "name": "internal_check_coupon_exist",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_check_coupon_exist"),
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "coupon_code": {
                    "type": "string",
                    "description": action_param_descriptions["coupon_code"]
                }
            },
            "additionalProperties": False,
            "required": ["coupon_code"]
        }
    },
    {
        "name": "internal_check_user_credit_status",
        "description": get_action_full_description(action_descriptions, action_returns,"internal_check_user_credit_status"),
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
    {
        "name": "internal_get_coupon_details",
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "coupon_code": {
                    "type": "string",
                    "description": action_param_descriptions["coupon_code"]
                }
            },
            "additionalProperties": False,
            "required": ["coupon_code"]
        }
    },
    {
        "name": "internal_check_order_exist",
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": action_param_descriptions["username"]
                },
                "order_id": {
                    "type": "string",
                    "description": action_param_descriptions["order_id"]
                }
            },
            "additionalProperties": False,
            "required": ["username", "order_id"]
        }
    },
]


