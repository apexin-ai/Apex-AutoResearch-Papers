"""
file for online market functionality implementations
database dependencies assume chatbot dependencies are followed perfectly
assumes previous steps in the dependency chain were called
"""

from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none

import copy
from datetime import datetime, timedelta
import re

default_data = {
    "accounts": {
        "alice": {
            "password": "[REDACTED]",
            "cart": [],
            "credit_rating": "excellent",
            "order_history": [
                {
                    "order_id": "ORD-1",
                    "items": [
                        {"product_id": "Laptop", "quantity": 1, "price": 1000.0}
                    ],
                    "status": "Delivered",
                    "total_amount": 1000.0,
                    "shipping_address": "15442 Saratoga Ave, Saratoga, CA, 95070",
                    "order_placed_date": "2023-10-01",
                    "number_of_exchanges": 0,
                    "coupons_used": []
                },
                {
                    "order_id": "ORD-2",
                    "items": [
                        {"product_id": "Headphones", "quantity": 1, "price": 1000.0}
                    ],
                    "status": "Processing",
                    "total_amount": 1000.0,
                    "shipping_address": "3524 Linden Avenue, Orlando, FL, 32789",
                    "order_placed_date": "2021-10-01",
                    "number_of_exchanges": 2,
                    "coupons_used": []
                },
                {
                    "order_id": "ORD-3",
                    "items": [
                        {"product_id": "Laptop", "quantity": 1, "price": 1000.0},
                        {"product_id": "Headphones", "quantity": 1, "price": 1000.0}
                    ],
                    "status": "Canceled",
                    "total_amount": 2000.0,
                    "shipping_address": "2257 Boone Crockett Lane, Portland, WA, 97205",
                    "order_placed_date": "2022-12-01",
                    "number_of_exchanges": 3,
                    "coupons_used": []
                },
            ],
            "shipping_addresses": [
                {"address": "3592 Rebecca St, Hickory Hills, IL, 60547"}
            ],
            "default_address_index": 0
        }
    },
    "products": {
        "Laptop": {
            "price": 1000.0,
            "stock": 9,
            "description": "A high-performance laptop",
            "reviews": [
                {"username": "alice", "rating": 5, "comment": "Excellent performance!"}
            ],
            "average_rating": 5
        },
        "Headphones": {
            "price": 100.0,
            "stock": 48,
            "description": "Noise-cancelling headphones",
            "reviews": [],
            "average_rating": 0
        }
    },
    "coupons": {
        "SAVE10": {
            "discount_value": 10,
            "discount_type": "percentage",
            "valid_products": ["Laptop"],
            "expiration_date": "2025-12-31"
        },
        "FLAT50": {
            "discount_value": 50,
            "discount_type": "flat",
            "valid_products": ["Headphones"],
            "expiration_date": "2024-12-31"
        }
    },
    "interaction_time": "2025-01-15T12:56:39"
}




default_data_descriptions = {
    "accounts":                 "Information for each account, including credentials, order history, cart, shipping addresses, and credit rating.",
    "password":                 "[REDACTED] password to the user's account for authentication.",
    "products":                 "Details of all available products, including price, stock, description, reviews, and average rating.",
    "coupons":                  "Details of all available coupons, including discount value, type, applicable products, and expiration date.",
    "interaction_time":         "The current time when the user interacts with the system, used for validating time-based constraints such as coupon expiration.",
    "cart":                     "A list of items the user has added to their cart, each with product ID, quantity, and price.",
    "order_history":            "A record of all orders placed by the user, including order details, status, and shipping address.",
    "shipping_addresses":       "A list of shipping addresses associated with the user’s account.",
    "default_address_index":    "The index of the default shipping address in the user's shipping addresses list.",
    "credit_rating":            "The credit rating of the user, indicating their creditworthiness, including 'excellent', 'suspended', 'good', 'normal', or 'restricted'.",
    "reviews":                  "Customer reviews for each product, including username, rating, and comment.",
    "average_rating":           "The average rating of a product, calculated from all reviews.",
    "order_id":                 "A unique identifier for each order in the user's order history.",
    "status":                   "The current status of an order, such as 'Processing', 'Shipped', 'Delivered', 'Refunding', 'Refunded', or 'Canceled'.",
    "number_of_exchanges":      "The number of times an order has been exchanged.",
    "coupons_used":             "A list of coupon codes applied to an order.",
    "valid_products":           "A list of product IDs that a coupon can be applied to.",
    "expiration_date":          "The expiration date of a coupon, after which it is no longer valid."
}

ddp = default_dependency_parameters = {
    "rating_lower_bound": 1,
    "rating_upper_bound": 5,
    "max_exchange_times": 2,
    "exchange_period": 365,
    "return_period": 182
}

class OnlineMarket:

    def __init__(self, data:dict=default_data, dep_innate_full:dict=get_domain_dependency_none("OnlineMarket"), dep_params:dict=default_dependency_parameters, data_descriptions:dict=default_data_descriptions):
        self.data = data
        self.accounts = self.data["accounts"] if data else {}
        self.products = self.data["products"] if data else {}
        self.coupons = self.data["coupons"] if data else {}
        self.interaction_time = self.data["interaction_time"]
        self.innate_state_tracker = OnlineMarket_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full) 
        self.data_descriptions = data_descriptions
#######################################################################################################
# Root Functions
#######################################################################################################

    def login_user(self, username: str, password: [REDACTED] -> bool:
        if not self.domain_dep.process(method_str="login_user", username=username, password=[REDACTED] return False

        return self.accounts[username]["password"] == password

    def logout_user(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="logout_user", username=username): return False
        return True

#######################################################################################################
# Domain Functions
#######################################################################################################

    def add_to_cart(self, username: str, product_id: str, quantity: int) -> bool:
        if not self.domain_dep.process(method_str="add_to_cart", username=username, product_id = product_id, quantity = quantity): return False
        self.products[product_id]["stock"] -= quantity
        self.accounts[username]["cart"].append({
            "product_id": product_id,
            "quantity": quantity,
            "price": self.products[product_id]["price"] * quantity
        })
        return True

    def view_cart(self, username: str) -> tuple[bool, list]:
        if not self.domain_dep.process(method_str="view_cart", username=username): return False
        return True, self.accounts[username]["cart"]

    def place_order(self, username: str) -> bool:
        if not self.domain_dep.process(method_str="place_order", username=username): return False
        account = self.accounts.get(username)
        cart = account["cart"]
        total_amount = sum(item["price"] for item in cart)
        default_index = account.get("default_address_index")
        order_date = self.interaction_time
        order = {
            "order_id": f"ORD-{len(account['order_history']) + 1}",
            "items": cart,
            "status": "Processing",
            "total_amount": round(total_amount, 2),
            "shipping_address": account["shipping_addresses"][default_index]["address"],
            "order_placed_date": order_date
        }
        account["order_history"].append(order)
        account["cart"] = []
        return True
    

    def view_order_history(self, username: str) -> tuple[bool, list]:
        if not self.domain_dep.process(method_str="view_order_history", username=username): return False
        return True, self.accounts[username]["order_history"]

    def add_shipping_address(self, username: str, address: str) -> bool:
        if not self.domain_dep.process(method_str="add_shipping_address", username=username, address=address): return False
        account = self.accounts.get(username)
        account["shipping_addresses"].append({"address": address})
        if len(account["shipping_addresses"]) == 1:
            account["default_address_index"] = 0
        return True

    def view_shipping_addresses(self, username: str) -> tuple[bool, list]:
        if not self.domain_dep.process(method_str="view_shipping_addresses", username=username): return False
        return True, self.accounts[username]["shipping_addresses"]

    def get_product_details(self, product_id: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="get_product_details", product_id=product_id): return False
        return True, self.products[product_id]

    def add_review(self, product_id: str, username: str, rating: int, comment: str) -> bool:
        if not self.domain_dep.process(method_str="add_review", product_id=product_id, username = username, rating = rating, comment = comment): return False
        review = {
            "username": username,
            "rating": rating,
            "comment": comment
        }
        self.products[product_id]["reviews"].append(review)

        # Update average rating
        reviews = self.products[product_id]["reviews"]
        self.products[product_id]["average_rating"] = round(
            sum(int(r["rating"]) for r in reviews) / len(reviews), 2
        )
        return True


    
    def get_order_details(self, username: str, order_id: str) -> tuple[bool, dict]:
        if not self.domain_dep.process(method_str="get_order_details", username=username, order_id = order_id): return False, {}
        account = self.accounts.get(username)
        order = next((o for o in account["order_history"] if o["order_id"] == order_id), None)
        return True, order
    
    
    def cancel_order(self, username: str, order_id: str) -> bool:
        if not self.domain_dep.process(method_str="cancel_order", username=username, order_id = order_id): return False
        account = self.accounts.get(username)
        order = next((o for o in account["order_history"] if o["order_id"] == order_id), None)
        order["status"] = "Canceled"
        return True


    
    def return_order(self, username: str, order_id: str) -> bool:
        if not self.domain_dep.process(method_str="return_order", username=username, order_id = order_id): return False
        account = self.accounts.get(username)
        order = next((o for o in account["order_history"] if o["order_id"] == order_id), None)
        order["status"] = "Refunding"
        return True
    
    def exchange_product(self, username: str, order_id: str, old_product_id: str, new_product_id: str, quantity: int) -> bool:
        if not self.domain_dep.process(method_str="exchange_product", username=username, order_id = order_id, old_product_id = old_product_id, new_product_id = new_product_id, quantity = quantity): return False

        account = self.accounts.get(username)
        order = next((o for o in account["order_history"] if o["order_id"] == order_id), None)
        order_item = next((item for item in order["items"] if item["product_id"] == old_product_id), None)
        new_product = self.products[new_product_id]
        new_product["stock"] -= quantity
        old_product = self.products[old_product_id]
        old_product["stock"] += order_item["quantity"]
        order_item["product_id"] = new_product_id
        order_item["price"] = new_product["price"] * quantity
        order["total_amount"] = sum(item["price"] for item in order["items"])
        return True
    
    def use_coupon(self, username: str, order_id: str, coupon_code: str) -> bool:
        if not self.domain_dep.process(method_str="use_coupon", username=username, order_id = order_id, coupon_code = coupon_code): return False
        account = self.accounts.get(username)
        order = next(order for order in account["order_history"] if order["order_id"] == order_id)
        coupon = self.coupons[coupon_code]
        order.setdefault("coupons_used", []).append(coupon_code)
        discount = (coupon["discount_value"] / 100) * order["total_amount"] if coupon["discount_type"] == "percentage" else coupon["discount_value"]
        order["total_amount"] -= round(discount, 2)
        return True
    
    def get_coupons_used(self, username: str) -> tuple[bool,list]:
        if not self.domain_dep.process(method_str="get_coupons_used",username = username): return False
        order_history = self.accounts[username]["order_history"]
        coupons_used = [coupon for order in order_history for coupon in order.get("coupons_used", [])]
        return True, coupons_used
           
    


#######################################################################################################
# Internal Functions
#######################################################################################################

    def internal_get_database(self) -> tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_database"): return False
        return self.data

    def internal_check_username_exist(self, username: str) -> tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_username_exist", username = username): return False

        return True, username in self.accounts

    def internal_check_product_exist(self, product_id: str) -> tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_product_exist", product_id = product_id): return False

        return True, product_id in self.products
    
    def internal_check_coupon_exist(self, coupon_code: str) -> tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_check_coupon_exist", coupon_code = coupon_code): return False

        return True, coupon_code in self.coupons
    
    def internal_check_user_credit_status(self, username: str) -> tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_check_user_credit_status", username = username): return False
        return True, self.accounts[username]["credit_rating"]
    
    def internal_get_interaction_time(self) -> tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_interaction_time"): return False
        return True, self.interaction_time
    
    def internal_get_coupon_details(self, coupon_code: str) -> tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_coupon_details", coupon_code = coupon_code): return False
        return True, self.coupons[coupon_code]
    
    def internal_check_order_exist(self, username: str, order_id: str) -> tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_check_order_exist", username = username, order_id = order_id): return False
        
        order_history = self.accounts[username].get("order_history", [])
        for order in order_history:
            if order["order_id"] == order_id:
                return True, True
        return True, False   

    def evaluation_get_database(self)->dict:
        return self.data
    
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions



class OnlineMarket_State_Tracker:
    def __init__(self, domain_system: OnlineMarket, rating_lower_bound:int, rating_upper_bound:int, max_exchange_times: int, exchange_period: int, return_period: int):
        self.domain_system = domain_system
        self.previously_logged_in_username: str = None
        self.rating_lower_bound = rating_lower_bound
        self.rating_upper_bound = rating_upper_bound
        self.exchange_period = exchange_period
        self.return_period = return_period
        self.max_exchange_times = max_exchange_times

    def logged_in_user(self, username: str) -> bool:
        return self.previously_logged_in_username == username
    def set_login_user(self, username: str):
        self.previously_logged_in_username = username
    def set_logout_user(self):
        self.previously_logged_in_username = None
        
    def enough_stock(self, product_id: str, quantity: int) -> bool:
        _, product = self.domain_system.get_product_details(product_id)
        return product["stock"] >= quantity
    
    def has_shipping_address(self, username: str) -> bool:
        _, shipping_address = self.domain_system.view_shipping_addresses(username)
        return bool(shipping_address)
    def within_review_limits(self, rating: int) -> bool:
        return self.rating_lower_bound <= rating <= self.rating_upper_bound
    def has_items_in_cart(self, username: str) -> bool:
        _, cart = self.domain_system.view_cart(username)
        return bool(cart)
    def amount_positive_restr(self, amount) -> bool:
        return amount > 0
    def not_already_added_shipping_address(self, username: str, address: str) -> bool:
        _, addresses = self.domain_system.view_shipping_addresses(username)
        existing_addresses = [addr["address"].lower() for addr in addresses]
        return address.lower() not in existing_addresses
    def unique_review(self, product_id: str, username: str) -> bool:
        _, product = self.domain_system.get_product_details(product_id)
        reviews = product["reviews"]
        return username not in [r["username"] for r in reviews]
    
    def product_bought_by_user(self, username: str, product_id: str) -> bool:
        _, order_history = self.domain_system.view_order_history(username)
        if not order_history:
            return False
        for order in order_history:
            for item in order["items"]:
                if item["product_id"] == product_id:
                    return True
        return False
    

  
    def coupon_not_already_used(self, username: str, coupon_code: str) -> bool:
        _, coupons_used = self.domain_system.get_coupons_used(username)
        return coupon_code not in coupons_used
    
    def product_exists_in_order(self, username: str, order_id: str, product_id: str) -> bool:
        _, order_details = self.domain_system.get_order_details(username, order_id)
        return any(item.get("product_id") == product_id for item in order_details.get("items", []))


    
    def order_delivered(self, username: str, order_id: str) -> bool:
        _, order = self.domain_system.get_order_details(username, order_id)
        order_status = order["status"].lower()
        return order_status == "delivered"
    def order_delivered_or_refunding(self, username: str, order_id: str) -> bool:
        _, order = self.domain_system.get_order_details(username, order_id)
        order_status = order["status"].lower()
        return order_status == "delivered" or order_status == "refunding" or order_status == "refunded"
    def order_processing(self, username: str, order_id: str) -> bool:
        _, order = self.domain_system.get_order_details(username, order_id)
        order_status = order["status"].lower()
        return order_status == "processing"
    
    
    def credit_status_not_restricted_or_suspended(self, username: str) -> bool:
        _, credit_status = self.domain_system.internal_check_user_credit_status(username)
        return credit_status.lower() != "restricted" and credit_status.lower() != "suspended"
    def credit_status_not_suspended(self, username: str) -> bool:
        _, credit_status = self.domain_system.internal_check_user_credit_status(username)
        return credit_status.lower() != "suspended"
    def credit_status_excellent(self, username: str) -> bool:
        _, credit_status = self.domain_system.internal_check_user_credit_status(username)
        return credit_status.lower() == "excellent"
    
    def within_exchange_period(self, username: str, order_id: str) -> bool:
        _, order = self.domain_system.get_order_details(username, order_id)
        order_date = datetime.strptime(order["order_placed_date"], "%Y-%m-%d") 
        _, current_time = self.domain_system.internal_get_interaction_time()
        time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
        return (time - order_date) <= timedelta(days=self.exchange_period)

    def within_return_period(self, username: str, order_id: str) -> bool:
        _, order = self.domain_system.get_order_details(username, order_id)
        order_date = datetime.strptime(order["order_placed_date"], "%Y-%m-%d") 
        _, current_time = self.domain_system.internal_get_interaction_time()
        time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
        return (time - order_date) <= timedelta(days=self.return_period)
    
    def less_than_max_exchanges(self, username: str, order_id:str) -> bool:
        _, order = self.domain_system.get_order_details(username, order_id)
        exchanges = order["number_of_exchanges"]
        return exchanges < self.max_exchange_times
    
    def coupon_not_expired(self, coupon_code: str) -> bool:
        _, coupon = self.domain_system.internal_get_coupon_details(coupon_code)
        _, current_time = self.domain_system.internal_get_interaction_time()
        time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S")
        expiration_date = datetime.strptime(coupon["expiration_date"], "%Y-%m-%d")
        return expiration_date > time
    
    def coupon_valid(self, username: str, order_id: str, coupon_code: str) -> bool:
        _, coupon_details = self.domain_system.internal_get_coupon_details(coupon_code)
        valid_products = coupon_details.get("valid_products", []) 
        _, order = self.domain_system.get_order_details(username, order_id)
        return any(item["product_id"] in valid_products for item in order["items"])


    
    


class OnlineMarket_Strict:

    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("OnlineMarket"),
        dep_full:dict=get_domain_dependency_none("OnlineMarket_Strict"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.dep_params = dep_params
        self.domain_system:OnlineMarket = OnlineMarket(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker:OnlineMarket_State_Tracker = OnlineMarket_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep:Dependency_Evaluator = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)

    def login_user(self, username: str, password: [REDACTED] -> bool:
        if not self.domain_dep.process(method_str="login_user", username=username, password=[REDACTED]
            return False
        self.state_tracker.set_login_user(username)
        return self.domain_system.login_user(username, password)

    def logout_user(self, username: str) -> bool:
        dep_res = self.domain_dep.process(method_str="logout_user", username=username)
        if not dep_res:
            return False
        self.state_tracker.set_logout_user()
        return self.domain_system.logout_user(username)
    
    def add_to_cart(self, **kwargs) -> bool:
        return self._check_dep_and_do("add_to_cart", **kwargs)

    def view_cart(self, **kwargs) -> tuple[bool, list]:
        return self._check_dep_and_do("view_cart", **kwargs)


    def place_order(self, **kwargs) -> bool:
        return self._check_dep_and_do("place_order", **kwargs)

    def view_order_history(self, **kwargs) -> tuple[bool, list]:
        return self._check_dep_and_do("view_order_history", **kwargs)

    def add_shipping_address(self, **kwargs) -> bool:
        return self._check_dep_and_do("add_shipping_address", **kwargs)


    def view_shipping_addresses(self, **kwargs) -> tuple[bool, list]:
        return self._check_dep_and_do("view_shipping_addresses", **kwargs)


    def get_product_details(self, **kwargs) -> tuple[bool, dict]:
        return self._check_dep_and_do("get_product_details", **kwargs)


    def add_review(self, **kwargs) -> bool:
        return self._check_dep_and_do("add_review", **kwargs)

    
    def cancel_order(self, **kwargs) -> bool:
        return self._check_dep_and_do("cancel_order", **kwargs)

    
    def return_order(self, **kwargs) -> bool:
        return self._check_dep_and_do("return_order", **kwargs)

    
    def exchange_product(self, **kwargs) -> bool:
        return self._check_dep_and_do("exchange_product", **kwargs)

    
    def use_coupon(self, **kwargs) -> bool:
        return self._check_dep_and_do("use_coupon", **kwargs)
    
    def get_order_details(self, **kwargs) -> tuple[bool, dict]:
        return self._check_dep_and_do("get_order_details", **kwargs)
    
    def get_coupons_used(self, **kwargs) -> tuple[bool, list]:
        return self._check_dep_and_do("get_coupons_used", **kwargs)


    def internal_get_database(self, **kwargs) -> tuple[bool,dict]:
        return self._check_dep_and_do("internal_get_database", **kwargs)


    def internal_check_username_exist(self, **kwargs) -> tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_username_exist", **kwargs)


    def internal_check_product_exist(self, **kwargs) -> tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_product_exist", **kwargs)

    def internal_check_coupon_exist(self, **kwargs) -> tuple[bool,bool]:
        return self._check_dep_and_do("internal_check_coupon_exist", **kwargs)

    def internal_check_user_credit_status(self, **kwargs) -> tuple[bool,str]:
        return self._check_dep_and_do("internal_check_user_credit_status", **kwargs)

    
    def internal_get_interaction_time(self, **kwargs) -> tuple[bool,str]:
        return self._check_dep_and_do("internal_get_interaction_time", **kwargs)

    
    def internal_get_coupon_details(self, **kwargs) -> tuple[bool,dict]:
        return self._check_dep_and_do("internal_get_coupon_details", **kwargs)
    
    def internal_check_order_exist(self, **kwargs) -> tuple[bool, bool]:
        return self._check_dep_and_do("internal_check_order_exist", **kwargs)




    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->OnlineMarket:
        return self.domain_system
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->OnlineMarket_State_Tracker:
        return self.state_tracker
    def _check_dep_and_do(self, method_str, **kwargs):
        if not self.domain_dep.process(method_str=method_str, **kwargs): return False
        return getattr(self.domain_system, method_str)(**kwargs)
    
    
    