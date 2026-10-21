"""
file for hotel functionality implmentations
database dependencies assume chatbot dependencies are followed perfectly
assumes previous steps in the dependency chain were called
"""

from env.dep_eval import Dependency_Evaluator
from env.helpers import get_domain_dependency_none

import copy
import random
from datetime import datetime, timedelta

default_data = {
    "rooms": {
        "single": {
            "availability": {
                "101": ["2024-12-04", "2024-12-05", "2024-12-06"],
                "102": ["2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05", "2024-12-06"]
            },
            "price_per_night": 80
        },
        "double": {
            "availability": {
                "107": ["2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05", "2024-12-06"],
                "108": ["2024-12-02", "2024-12-06"]
            },
            "price_per_night": 110
        },
        "suite": {
            "availability": {
                "110": ["2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05", "2024-12-06"],
            },
            "price_per_night": 160
        }
    },
    "room_checkins": {
        "101": {
            "booking_id": "BK001",
            "check_in_time": "2024-12-02T17:28:31",
            "identity_document": "driver_license"
        }
    },
    "bookings": {
        "BK001": {
            "guest": "John Doe",
            "room_type": "single",
            "check_in_date": "2024-12-02",
            "check_out_date": "2024-12-04",
            "booking_time": "2024-11-20T12:26:39",
            "status": "checked-in", # confirmed, checked-in
            "loyalty_points_to_add": 20, # 10 * 2
            "room_change": 0,
            "room_service": {
                "2024-12-02": 1
            }
        },
        "BK002": {
            "guest": "Jane Smith",
            "room_type": "double",
            "check_in_date": "2024-12-03",
            "check_out_date": "2024-12-06",
            "booking_time": "2024-11-25T09:30:00",
            "status": "confirmed",
            "loyalty_points_to_add": 0,
            "room_change": 0,
            "room_service": {}
        }
    },
    "room_assignment": {
        "BK001": "101",
        "BK002": "108"
    },
    "room_service_options": {
        "dining": {
            "club_sandwich": 12,
            "caesar_salad": 10,
            "grilled_salmon": 20,
            "steak_frites": 24,
            "cheesecake": 7,
            "bottled_water": 3,
            "coffee": 4,
            "coke": 4,
            "orange_juice": 5
        },
        "spa": {
            "swedish_massage": 50,
            "deep_tissue_massage": 70,
            "facial": 40,
            "aromatherapy_session": 30
        },
        "housekeeping": {
            "extra_towels": 0,
            "pillow_request": 0,
            "laundry_service": 15,
            "dry_cleaning": 25
        },
        "tech_support": {
            "wifi_router_delivery": 0,
            "hdmi_cable": 5,
            "universal_adapter": 10
        }
    },
    "room_service_payment_method": ["credit_card", "loyalty_points"],
    "room_service_orders": {
        # Orders placed by guests during their stay
        "RS001": {
            "room": "101",
            "order_time": "2024-12-02T20:00:00",
            "order_type": "dining",
            "order_details": [
                {"item": "club_sandwich", "quantity": 1, "price": 12},
                {"item": "coke", "quantity": 2, "price": 8}
            ],
            "order_total": 20,
            "payment": "loyalty_points",
            "status": "in-progress" # or completed
        }
    },
    "loyalty_members": {
        "HTL0386Y": {
            "name": "John Doe",
            "loyalty_points": 250,
            "tier": "silver" # silver, gold, platinum
        },
        "HTL1003C" : {
            "name": "Sakana Inoue",
            "loyalty_points": 1500,
            "tier": "gold"
        }
    },
    "valid_room_change_reasons": [
        "upgrade",            # guest wants a higher-tier room
        "maintenance",        # AC not working, water leak, etc.
        "noise",              # next to elevator, loud neighbors
        "accessibility",      # needs wheelchair-accessible room
        "temperature",        # heater/AC too hot or cold
        "cleanliness",        # room was not clean on arrival
        "safety",             # broken lock, suspicious activity
        "other"
    ],
    "interaction_time": "2024-12-02T20:04:31"
}


default_data_descriptions = {
    "rooms":                            "a dictionary mapping room types to dictionaries containing availability and pricing information, where:"\
                                        + "\n 'availability': a dict mapping room IDs to lists of available dates (formatted 'YYYY-MM-DD'),"
                                        + "\n 'price_per_night': nightly rate in USD",
    "room_checkins":                    "a dict mapping room IDs to check-in records, each containing:"
                                        + "\n 'booking_id': the booking identifier,"
                                        + "\n 'check_in_time': timestamp of check-in formatted 'YYYY-MM-DDTHH:MM:SS',"
                                        + "\n 'identity_document': type of identification provided",
    "bookings":                         "a dict mapping booking IDs to booking details, each containing:"
                                        + "\n 'guest': name of the guest,"
                                        + "\n 'room_type': type of room reserved,"
                                        + "\n 'check_in_date': reservation start date 'YYYY-MM-DD',"
                                        + "\n 'check_out_date': reservation end date 'YYYY-MM-DD',"
                                        + "\n 'booking_time': timestamp when booking was made 'YYYY-MM-DDTHH:MM:SS',"
                                        + "\n 'status': booking status (e.g., 'confirmed', 'checked-in'),"
                                        + "\n 'loyalty_points_to_add': points to credit after stay,"
                                        + "\n 'room_change': count of room changes requested,"
                                        + "\n 'room_service': record of daily room service usage",
    "room_assignment":                  "a dict mapping booking IDs to assigned room IDs",
    "room_service_options":             "a dict of available room service categories mapping to item-price mappings",
    "room_service_payment_method":      "a list of permitted payment methods for room service orders",
    "room_service_orders":              "a dict mapping order IDs to room service orders, each containing:"
                                        + "\n 'room': room ID,"
                                        + "\n 'order_time': timestamp of order 'YYYY-MM-DDTHH:MM:SS',"
                                        + "\n 'order_type': type of service,"
                                        + "\n 'order_details': list of items with quantities and individual prices,"
                                        + "\n 'order_total': total cost of the order,"
                                        + "\n 'payment': payment method used,"
                                        + "\n 'status': order status (either in 'in-progress' or 'completed')",
    "loyalty_members":                  "a dict mapping loyalty member IDs to member records, each containing:"
                                        + "\n 'name': member name,"
                                        + "\n 'loyalty_points': accumulated points,"
                                        + "\n 'tier': membership tier (must be one of the following: 'silver', 'gold', 'platinum')",
    "valid_room_change_reasons":        "a list of valid reasons for room changes",
    "interaction_time":                 "the timestamp of the current interaction with the hotel system formatted 'YYYY-MM-DDTHH:MM:SS'"
}


ddp = default_dependency_parameters = {
    # booking related
    "min_booking_lead_time_days": 1,
    "max_booking_lead_time_days": 30,
    "max_stays": 10,
    "modification_deadline_hours": 48,

    "min_age": 18,
    "valid_document_types": ["driver_license", "passport", "state_id", "military_id"],
    "check_in_time": "15:00",
    "check_out_time": "11:00",

    "max_room_changes": 1,
    "room_service_start": "8:00",
    "room_service_end": "22:00",
    "max_room_service_orders_per_day": 3,
}

# describes the common functions of a hotel
class Hotel:
    # initialization of Hotel functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Hotel"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.data = data

        # domain specific vars:
        self.bookings = self.data["bookings"]
        self.interaction_time = self.data["interaction_time"]

        self.innate_state_tracker = Hotel_State_Tracker(self, **dep_params)
        self.domain_dep = Dependency_Evaluator(self, self.innate_state_tracker, dep_innate_full) # no state tracker constraints yet
        self.data_descriptions = data_descriptions 
    def show_available_rooms(self)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="show_available_rooms"): return False
        return True, self.data["rooms"]
    def show_room_change_options(self)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="show_available_rooms"): return False
        else: return True, self.data["valid_room_change_reasons"]
    def book_room(self, guest_name: str, room_type:str, check_in_date:str, check_out_date:str, amount:float)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="book_room", guest_name=guest_name, 
                                       room_type=room_type, check_in_date=check_in_date, 
                                       check_out_date=check_out_date, amount=amount):
            return False
        check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        num_days = (check_out_dt - check_in_dt).days
        loyalty_points_to_add = 0
        for member in self.data.get("loyalty_members", {}).values():
            if member.get("name") == guest_name:
                tier = member.get("tier", "").lower()
                if tier == "silver":
                    loyalty_points_to_add = 10 * num_days
                elif tier == "gold":
                    loyalty_points_to_add = 25 * num_days
                elif tier == "platinum":
                    loyalty_points_to_add = 50 * num_days
                break
        new_booking_id = "BK" + str(len(self.data["bookings"]) + 1).zfill(3)
        booking_entry = {
            "guest": guest_name,
            "room_type": room_type,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "booking_time": self.interaction_time,
            "status": "confirmed",
            "loyalty_points_to_add": loyalty_points_to_add,
            "room_change": 0,
            "room_service": 0
        }
        self.bookings[new_booking_id] = booking_entry
        date_list = [(check_in_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]
        available_rooms = self.data["rooms"][room_type]["availability"]
        assigned_room = None
        for room_id, dates in available_rooms.items():
            if all(date in dates for date in date_list):
                assigned_room = room_id
                for date in date_list:
                    dates.remove(date)
                break
        self.data["room_assignment"][new_booking_id] = assigned_room
        return True, True
    def find_booking_info(self, guest_name:str, check_in_date:str, check_out_date:str)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="find_booking_info", guest_name=guest_name):
            return False
        for booking_id, booking in self.bookings.items():
            if booking["guest"] == guest_name and (
                booking["check_in_date"] == check_in_date and
                booking["check_out_date"] == check_out_date
            ):
                return True, booking
        return True, {}
    def cancel_reservation(self, guest_name:str, check_in_date:str, check_out_date:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="cancel_reservation", guest_name=guest_name, 
                                       check_in_date=check_in_date, check_out_date=check_out_date):
            return False
        for booking_id, booking in self.bookings.items():
            if booking["guest"] == guest_name and (
                booking["check_in_date"] == check_in_date and
                booking["check_out_date"] == check_out_date
            ):
                room_type = booking["room_type"]
                check_in_date = booking["check_in_date"]
                check_out_date = booking["check_out_date"]
                assigned_room_id = self.data["room_assignment"].get(booking_id)
                check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
                check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
                num_days = (check_out_dt - check_in_dt).days
                date_list = [(check_in_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]
                if assigned_room_id:
                    availability = self.data["rooms"][room_type]["availability"].get(assigned_room_id, [])
                    for date in date_list:
                        if date not in availability:
                            availability.append(date)
                    availability.sort()
                    self.data["rooms"][room_type]["availability"][assigned_room_id] = availability
                break
        del self.bookings[booking_id]
        if booking_id in self.data["room_assignment"]:
            del self.data["room_assignment"][booking_id]
        return True, True
    def modify_reservation(self, guest_name: str, old_check_in_date:str, old_check_out_date:str,
                           check_in_date:str, check_out_date:str, room_type:str, amount:float)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="modify_reservation", guest_name=guest_name, 
                                       old_check_in_date=old_check_in_date, old_check_out_date = old_check_out_date,
                                       room_type=room_type, check_in_date=check_in_date, check_out_date=check_out_date, 
                                       amount=amount):
            return False
        for booking_id, booking in self.bookings.items():
            if booking["guest"] == guest_name and (
                booking["check_in_date"] == old_check_in_date and
                booking["check_out_date"] == old_check_out_date
            ):
                old_booking = booking
                old_booking_id = booking_id
                break
        assigned_room = self.data["room_assignment"].get(old_booking_id)
        old_check_in_dt = datetime.strptime(old_booking["check_in_date"], "%Y-%m-%d")
        old_check_out_dt = datetime.strptime(old_booking["check_out_date"], "%Y-%m-%d")
        old_room_type = old_booking["room_type"]
        old_num_days = (old_check_out_dt - old_check_in_dt).days
        old_date_list = [(old_check_in_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(old_num_days)]
        if assigned_room:
            availability = self.data["rooms"][old_room_type]["availability"].get(assigned_room, [])
            for date in old_date_list:
                if date not in availability:
                    availability.append(date)
            availability.sort()
            self.data["rooms"][room_type]["availability"][assigned_room] = availability
        new_check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        new_check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        new_num_days = (new_check_out_dt - new_check_in_dt).days
        loyalty_points_to_add = 0
        for member in self.data.get("loyalty_members", {}).values():
            if member.get("name") == guest_name:
                tier = member.get("tier", "").lower()
                if tier == "silver": loyalty_points_to_add = 10 * new_num_days
                elif tier == "gold": loyalty_points_to_add = 25 * new_num_days
                elif tier == "platinum": loyalty_points_to_add = 50 * new_num_days
                break
        old_booking["room_type"] = room_type
        old_booking["check_in_date"] = check_in_date
        old_booking["check_out_date"] = check_out_date
        old_booking["booking_time"] = self.interaction_time
        old_booking["status"] = "confirmed"
        old_booking["loyalty_points_to_add"] = loyalty_points_to_add
        new_date_list = [(new_check_in_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(new_num_days)]
        available_rooms = self.data["rooms"][room_type]["availability"]
        new_assigned_room = None
        for room_id, dates in available_rooms.items():
            if all(date in dates for date in new_date_list):
                new_assigned_room = room_id
                for date in new_date_list:
                    dates.remove(date)
                break
        self.data["room_assignment"][old_booking_id] = new_assigned_room
        return True, True
    def process_guest_checkin(self, guest_name:str, check_in_date:str, check_out_date:str, identification:dict)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="process_guest_checkin", guest_name=guest_name, 
                                       check_in_date=check_in_date, check_out_date=check_out_date,
                                       identification=identification):
            return False
        booking_to_check_in = None
        associated_booking_id = None
        for booking_id, booking in self.bookings.items():
            if (booking["guest"] == guest_name and 
                booking["check_in_date"] == check_in_date and
                booking["check_out_date"] == check_out_date):
                booking_to_check_in = booking
                associated_booking_id = booking_id
                break
        assigned_room = self.data["room_assignment"].get(associated_booking_id)
        check_in_time = self.interaction_time
        self.data["room_checkins"][assigned_room] = {
            "booking_id": associated_booking_id,
            "check_in_time": check_in_time,
            "identity_document": identification.get("type", "")
        }
        booking_to_check_in["status"] = "checked-in"
        return True, assigned_room
    def process_guest_checkout(self, guest_name:str, key_returned:bool)->bool|tuple[bool|bool]:
        if not self.domain_dep.process(method_str="process_guest_checkout", guest_name=guest_name, key_returned=key_returned):
            return False
        loyalty_points = 0
        for booking_id, booking in self.bookings.items():
            if booking["guest"] == guest_name:
                booking_id_to_remove = booking_id
                loyalty_points = booking.get("loyalty_points_to_add", 0)
                break
        del self.bookings[booking_id_to_remove]
        for room, checkin in list(self.data["room_checkins"].items()):
            if checkin.get("booking_id") == booking_id_to_remove:
                del self.data["room_checkins"][room]
                break
        for member in self.data.get("loyalty_members", {}).values():
            if member.get("name") == guest_name:
                member["loyalty_points"] += loyalty_points
                break
        return True, True
    def request_room_change(self, guest_name:str, amount:float, reason:str, room_type:str)->bool|tuple[bool|bool]:
        if not self.domain_dep.process(method_str="request_room_change", guest_name=guest_name,
                                       amount=amount, reason=reason, room_type=room_type):
            return False
        original_booking = None
        for booking_id, booking in self.bookings.items():
            if (booking["guest"] == guest_name
                and booking["status"]=="checked-in"):
                original_booking = booking
                break
        original_room_id = self.data["room_assignment"].get(booking_id)
        original_room_type = original_booking["room_type"]
        check_out_date = booking["check_out_date"]
        change_date_str = self.interaction_time.split("T")[0]
        change_dt = datetime.strptime(change_date_str, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        restore_start = change_dt + timedelta(days=1)
        avail_list = None
        range_days = (check_out_dt - restore_start).days
        for i in range(range_days):
            if range_days > 0:
                date = (restore_start + timedelta(days=i)).strftime("%Y-%m-%d")
                avail_list = self.data["rooms"][original_room_type]["availability"].setdefault(original_room_id, [])
                if date not in avail_list:
                    avail_list.append(date)
        if avail_list: avail_list.sort()
        needed_dates = [
            (change_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((check_out_dt - change_dt).days)
        ]
        for room_id, dates in self.data["rooms"][room_type]["availability"].items():
            if all(d in dates for d in needed_dates):
                new_room_id = room_id
                # remove those dates from new room's availability
                for d in needed_dates:
                    dates.remove(d)
                break
        original_booking["room_type"] = room_type
        original_booking["room_change"]+= 1
        self.data["room_assignment"][booking_id] = new_room_id
        self.data["room_checkins"][new_room_id] = self.data["room_checkins"].pop(original_room_id)
        return True, True
    def place_room_service_order(self, guest_name:str, room_id:str, order_type:str, order_items:list, payment_method:str, amount:float=None)->bool|tuple[bool|bool]:
        if not self.domain_dep.process(method_str="place_room_service_order", guest_name=guest_name, room_id=room_id,
                                   order_type=order_type, order_items=order_items,
                                   payment_method=payment_method, amount=amount):
            return False
        total_cost = 0
        order_details = []
        for entry in order_items:
            item = entry.get("name")
            qty = entry.get("quantity", 0)
            price_per_item = self.data["room_service_options"][order_type][item]
            total_cost += price_per_item * qty
            order_details.append({
                "item": item,
                "quantity": qty,
                "price": price_per_item * qty
            })
        order_id = "RS" + str(len(self.data["room_service_orders"]) + 1).zfill(3)
        order_entry = {
            "room": room_id,
            "order_time": self.interaction_time,
            "order_type": order_type,
            "order_details": order_details,
            "order_total": total_cost,
            "payment": payment_method,
            "status": "in-progress"
        }
        self.data["room_service_orders"][order_id] = order_entry
        for booking_id, assigned_room in self.data["room_assignment"].items():
            if assigned_room == room_id:
                if booking_id in self.bookings:
                    order_date = self.interaction_time.split("T")[0]
                    if order_date not in self.bookings[booking_id]["room_service"]:
                        self.bookings[booking_id]["room_service"][order_date] = 0
                    self.bookings[booking_id]["room_service"][order_date] += 1
                break
        return True, True
    def register_loyalty_member(self, guest_name:str)->bool|tuple[bool, bool]:
        if not self.domain_dep.process(method_str="register_loyalty_member", guest_name=guest_name):
            return False
        random.seed(guest_name)
        digits = str(random.randint(1000, 9999))
        letter = chr(random.randint(65, 90))
        new_id = "HTL" + digits + letter
        self.data["loyalty_members"][new_id] = {
            "name": guest_name,
            "loyalty_points": 0,
            "tier": "silver"
        }
        return True, True
    # internal utility functions
    def internal_get_room_checkin_details(self)->bool|tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_room_checkin_details"): return False
        return True, self.data["room_checkins"]
    def internal_get_booking_details(self)->bool|tuple[bool, dict]:
        if not self.domain_dep.process(method_str="internal_get_booking_details"): return False
        return True, self.bookings
    def internal_get_loyalty_member_info(self, guest_name:str)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_loyalty_member_info",guest_name=guest_name): return False
        for member_id, member_data in self.data["loyalty_members"].items():
            if member_data.get("name") == guest_name:
                return True, {member_id: member_data}
        return True, {}
    def internal_get_interaction_time(self)->bool|tuple[bool,str]:
        if not self.domain_dep.process(method_str="internal_get_interaction_time"): return False
        return True, self.interaction_time
    def internal_get_room_service_order_details(self)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_room_service_order_details"): return False
        return True, self.data["room_service_orders"]
    def internal_get_room_assignment(self)->bool|tuple[bool,dict]:
        if not self.domain_dep.process(method_str="internal_get_room_assignment"): return False
        return True, self.data["room_assignment"]        
    def internal_compute_room_service_order_fee(self, order_type:str, order_items:list)->bool|tuple[bool|float]:
        if not self.domain_dep.process(method_str="internal_compute_room_service_order_fee", 
                                       order_type=order_type, order_items=order_items): 
            return False
        total_cost = 0
        for entry in order_items:
            item = entry.get("name")
            qty = entry.get("quantity", 0)
            price_per_item = self.data["room_service_options"][order_type][item]
            total_cost += price_per_item * qty
        return True, total_cost
    # internal constraints
    def internal_valid_room_type(self, room_type:str)->bool|tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_valid_room_type", room_type=room_type): return False
        return True, room_type in self.data["rooms"]
    def internal_is_loyalty_member(self, guest_name:str)->bool|tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_is_loyalty_member", guest_name=guest_name):
            return False
        return True, any(member.get("name") == guest_name for member in self.data.get("loyalty_members", {}).values())
    def internal_valid_room_change_reason(self, reason:str)->bool|tuple[bool,bool]:
        if not self.domain_dep.process(method_str="internal_valid_room_change_reason", reason=reason):
            return False
        return True, reason in self.show_room_change_options()[1]
    def internal_valid_room_service_order_type(self, order_type:str)->bool|tuple[bool|bool]:
        if not self.domain_dep.process(method_str="internal_valid_room_service_order_type", order_type=order_type):
            return False
        return True, order_type in self.data["room_service_options"]
    def internal_valid_room_service_item(self, order_type:str, order_items:list)->bool|tuple[bool, bool]:
        if not self.domain_dep.process(method_str="internal_valid_room_service_item", 
                                       order_type=order_type, order_items=order_items):
            return False
        valid_items = self.data["room_service_options"][order_type]
        for entry in order_items:
            item = entry.get("name")
            if item not in valid_items:
                return True, False
        return True, True
    def internal_valid_room_id(self, room_id:str)->bool|tuple[bool|bool]:
        if not self.domain_dep.process(method_str="internal_valid_room_id", room_id=room_id):
            return False
        for room_type_data in self.data["rooms"].values():
            if room_id in room_type_data.get("availability", {}):
                return True, True
        return True, False
    def internal_valid_room_service_payment_method(self, payment_method:str)->bool|tuple[bool|bool]:
        if not self.domain_dep.process(method_str="internal_valid_room_id", payment_method=payment_method):
            return False
        return True, payment_method in self.data["room_service_payment_method"]
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.data
    def evaluation_get_database_descriptions(self)->dict:
        return self.data_descriptions
    def evaluation_get_innate_state_tracker(self):
        return self.innate_state_tracker

class Hotel_State_Tracker:
    # initialization
    def __init__(self, domain_system:Hotel, max_booking_lead_time_days:int, min_booking_lead_time_days:int, 
                  max_stays:int, min_age:int, check_in_time:str, check_out_time:str, 
                  valid_document_types:list[str], modification_deadline_hours:int, max_room_changes:int,
                  room_service_start:str, room_service_end:str, max_room_service_orders_per_day:int
                 ):
        # dependencies and the data it depends on
        self.domain_system = domain_system
        # customizable values

        self.max_booking_lead_time_days = max_booking_lead_time_days
        self.min_booking_lead_time_days = min_booking_lead_time_days
        self.max_stays = max_stays

        self.min_age = min_age
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.valid_document_types = valid_document_types
        self.modification_deadline_hours = modification_deadline_hours

        self.max_room_changes = max_room_changes
        self.room_service_start = room_service_start
        self.room_service_end = room_service_end
        self.max_room_service_orders_per_day = max_room_service_orders_per_day
    # general booking constraints
    def valid_booking_date_pair(self, check_in_date:str, check_out_date:str)->bool:
        check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        return check_out_dt > check_in_dt
    def room_type_available_for_dates(self, room_type:str, check_in_date:str, check_out_date:str)->bool:
        check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        num_days = (check_out_dt - check_in_dt).days
        required_dates = [(check_in_dt + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]
        room_data = self.domain_system.data["rooms"].get(room_type)
        for room_id, available_dates in room_data.get("availability", {}).items():
            if all(date in available_dates for date in required_dates):
                return True
        return False
    def is_booking_date_within_lead_time_range(self, check_in_date:str)->bool:
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        interaction_date_str = interaction_time_str.split("T")[0]
        interaction_dt = datetime.strptime(interaction_date_str, "%Y-%m-%d")
        lower_bound = check_in_dt - timedelta(days=self.max_booking_lead_time_days)
        upper_bound = check_in_dt - timedelta(days=self.min_booking_lead_time_days)
        return lower_bound <= interaction_dt <= upper_bound
    def has_exceeded_maximum_stays(self, check_in_date:str, check_out_date:str)->bool:
        check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        new_nights = (check_out_dt - check_in_dt).days
        return new_nights > self.max_stays
    # initial booking constraints
    def sufficient_amount_for_booking(self, room_type:str, check_in_date:str, check_out_date:str, amount:float)->bool:
        rooms_info = self.domain_system.show_available_rooms()[1]
        price_per_night = rooms_info[room_type]["price_per_night"]
        check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        num_nights = (check_out_dt - check_in_dt).days
        total_fee = num_nights * price_per_night
        return amount >= total_fee
    def has_overlapping_booking_for_booking(self, guest_name:str, check_in_date:str, check_out_date:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        new_check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        new_check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
        for booking in bookings.values():
            if booking["guest"] != guest_name:
                continue
            existing_check_in = datetime.strptime(booking["check_in_date"], "%Y-%m-%d")
            existing_check_out = datetime.strptime(booking["check_out_date"], "%Y-%m-%d")
            if new_check_in < existing_check_out and new_check_out > existing_check_in:
                return True
        return False
    def has_overlapping_booking_for_modification(self, guest_name:str, check_in_date:str, check_out_date:str, old_check_in_date:str, old_check_out_date:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        new_check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
        new_check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
        for booking in bookings.values():
            if booking["guest"] != guest_name:
                continue
            existing_check_in = datetime.strptime(booking["check_in_date"], "%Y-%m-%d")
            existing_check_out = datetime.strptime(booking["check_out_date"], "%Y-%m-%d")
            old_in = datetime.strptime(old_check_in_date, "%Y-%m-%d")
            old_out = datetime.strptime(old_check_out_date, "%Y-%m-%d")
            if existing_check_in == old_in and existing_check_out == old_out:
                continue
            if new_check_in < existing_check_out and new_check_out > existing_check_in:
                return True
        return False
    # modification-specific constraints
    def before_modification_deadline(self, check_in_date:str)->bool:
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        current_dt = datetime.strptime(interaction_time_str, "%Y-%m-%dT%H:%M:%S")
        check_in_dt = datetime.strptime(f"{check_in_date}T{self.check_in_time}:00", "%Y-%m-%dT%H:%M:%S")
        deadline_dt = check_in_dt - timedelta(hours=self.modification_deadline_hours)
        return current_dt <= deadline_dt 
    def has_confirmed_reservation(self, guest_name:str, check_in_date:str, check_out_date:str)->bool:      
        bookings = self.domain_system.internal_get_booking_details()[1]
        for booking in bookings.values():
            if (booking.get("guest") == guest_name and 
                booking.get("check_in_date") == check_in_date and
                booking.get("check_out_date") == check_out_date and 
                booking.get("status")=="confirmed"):
                return True
        return False 
    def sufficient_amount_for_reservation_modification(self, guest_name:str, old_check_in_date:str, old_check_out_date:str, check_in_date:str, check_out_date:str, room_type:str, amount:float)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        rooms_info = self.domain_system.show_available_rooms()[1]
        #TODO: remove breakpoints
        original_room_type = None
        for booking in bookings.values():
            if (booking["guest"] == guest_name and
                booking["check_in_date"] == old_check_in_date and
                booking["check_out_date"] == old_check_out_date):
                original_room_type = booking["room_type"]
                break
        # if not original_room_type: return False
        # if not original_room_type: return False
        # Compute original and new durations
        old_check_in_dt = datetime.strptime(old_check_in_date, "%Y-%m-%d")
        old_check_out_dt = datetime.strptime(old_check_out_date, "%Y-%m-%d")
        new_check_in_dt = datetime.strptime(check_in_date, "%Y-%m-%d")
        new_check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        old_nights = (old_check_out_dt - old_check_in_dt).days
        new_nights = (new_check_out_dt - new_check_in_dt).days
        original_fee = old_nights * rooms_info[original_room_type]["price_per_night"]
        new_fee = new_nights * rooms_info[room_type]["price_per_night"]
        fee = max(new_fee - original_fee, 0)
        return amount >= fee
    # check-in constraints
    def valid_identification(self, identification: dict)->bool:
        if not identification or "type" not in identification or "birthday" not in identification:
            return False
        if identification["type"].lower() not in self.valid_document_types: return False
        try:
            birthday_dt = datetime.strptime(identification["birthday"], "%Y-%m-%d")
        except ValueError: return False
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        current_date_str = interaction_time_str.split("T")[0]
        current_dt = datetime.strptime(current_date_str, "%Y-%m-%d")
        age = current_dt.year - birthday_dt.year - ((current_dt.month, current_dt.day) < (birthday_dt.month, birthday_dt.day))
        return age >= self.min_age
    def after_check_in_time(self)->bool:
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        current_date = interaction_time_str.split("T")[0]
        check_in_threshold_str = f"{current_date}T{self.check_in_time}:00"
        check_in_threshold = datetime.strptime(check_in_threshold_str, "%Y-%m-%dT%H:%M:%S")
        current_dt = datetime.strptime(interaction_time_str, "%Y-%m-%dT%H:%M:%S")
        return current_dt >= check_in_threshold
    # check-out constraints
    def before_check_out_time(self)->bool:
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        current_date = interaction_time_str.split("T")[0]
        check_out_threshold_str = f"{current_date}T{self.check_out_time}:00"
        check_out_threshold = datetime.strptime(check_out_threshold_str, "%Y-%m-%dT%H:%M:%S")
        current_dt = datetime.strptime(interaction_time_str, "%Y-%m-%dT%H:%M:%S")
        return current_dt <= check_out_threshold
    def guest_already_checked_in(self, guest_name:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        room_checkins = self.domain_system.internal_get_room_checkin_details()[1]
        checked_in_booking_ids = {checkin["booking_id"] for checkin in room_checkins.values()}
        return any(booking_id in checked_in_booking_ids and booking.get("guest") == guest_name
                for booking_id, booking in bookings.items())
    def room_key_returned(self, key_returned:bool)->bool: return key_returned
    # room-change constraints
    def room_type_available_for_room_change(self, guest_name:str, room_type:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        booking = None
        for b in bookings.values():
            if (b["guest"] == guest_name and b["status"] == "checked-in"):
                booking = b
                break
        check_out_date = booking["check_out_date"]
        check_in_date = self.domain_system.internal_get_interaction_time()[1].split("T")[0]
        return self.room_type_available_for_dates(room_type, check_in_date, check_out_date)
    def has_remaining_nights(self, guest_name:str)->bool:
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        change_date_str = interaction_time_str.split("T")[0]
        change_dt = datetime.strptime(change_date_str, "%Y-%m-%d")
        bookings = self.domain_system.internal_get_booking_details()[1]
        booking = None
        for b in bookings.values():
            if (b["guest"] == guest_name and b["status"] == "checked-in"):
                booking = b
                break
        check_out_date = booking["check_out_date"]
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        nights_remaining = max((check_out_dt - change_dt).days, 0)
        return nights_remaining > 0
    def sufficient_amount_for_room_change_fee(self, guest_name:str, amount:int, room_type:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        booking = None
        for b in bookings.values():
            if (b["guest"] == guest_name and b["status"] == "checked-in"):
                booking = b
                break
        original_room_type = booking["room_type"]
        check_out_date = booking["check_out_date"]
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        change_date_str = interaction_time_str.split("T")[0]
        change_dt = datetime.strptime(change_date_str, "%Y-%m-%d")
        check_out_dt = datetime.strptime(check_out_date, "%Y-%m-%d")
        nights_remaining = max((check_out_dt - change_dt).days, 0)
        rooms_data = self.domain_system.data["rooms"]
        orig_rate = rooms_data[original_room_type]["price_per_night"]
        new_rate = rooms_data[room_type]["price_per_night"]
        orig_total = orig_rate * nights_remaining
        new_total = new_rate * nights_remaining
        fee = max(new_total - orig_total, 0)
        return amount >= fee
    def within_max_room_changes(self, guest_name:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        booking = None
        for b in bookings.values():
            if (b["guest"] == guest_name and b["status"] == "checked-in"):
                booking = b
                break
        return booking["room_change"] < self.max_room_changes
    # room-service constraints
    def within_room_service_order_daily_limit(self, guest_name:str, room_id:str)->bool:
        bookings = self.domain_system.internal_get_booking_details()[1]
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        order_date = interaction_time_str.split("T")[0]
        room_assignment = self.domain_system.internal_get_room_assignment()[1]
        service_record = {}
        for booking_id, booking in bookings.items():
            if room_assignment.get(booking_id) == room_id and booking.get("guest") == guest_name:
                service_record = booking.get("room_service", {})
        return service_record.get(order_date, 0) < self.max_room_service_orders_per_day
    def within_room_service_hours(self) -> bool:
        interaction_time_str = self.domain_system.internal_get_interaction_time()[1]
        current_time = datetime.strptime(interaction_time_str.split("T")[1], "%H:%M:%S")
        start_time = datetime.strptime(self.room_service_start, "%H:%M").time()
        end_time = datetime.strptime(self.room_service_end, "%H:%M").time()
        return start_time <= current_time.time() <= end_time
    def payment_with_loyalty_points(self, payment_method:str)->bool:
        return payment_method=="loyalty_points"
    def sufficient_payment_for_room_service(self, guest_name:str, order_type:str, order_items:list, payment_method:str, amount:float=None)->bool:
        total_cost = self.domain_system.internal_compute_room_service_order_fee(order_type, order_items)[1]
        if payment_method != "loyalty_points":
            return amount is not None and amount >= total_cost
        else: # paying with loyalty_points
            member_info = self.domain_system.internal_get_loyalty_member_info(guest_name)[1]
            loyalty_points = list(member_info.values())[0]["loyalty_points"]
            return loyalty_points >= total_cost * 10 
    def is_gold_or_higher_member(self, guest_name: str) -> bool:
        member_info = self.domain_system.internal_get_loyalty_member_info(guest_name)[1]
        tier = next(iter(member_info.values()))["tier"].lower()
        return tier in ["gold", "platinum"]
    def amount_positive_restr(self, amount:float)->bool: return amount > 0

# required and customizable dependencies are separated
class Hotel_Strict:
    # initialization of dmv functionality
    def __init__(self, data:dict=default_data,
        dep_innate_full:dict=get_domain_dependency_none("Hotel"),
        dep_full:dict=get_domain_dependency_none("Hotel_Strict"),
        dep_params:dict=default_dependency_parameters,
        data_descriptions:dict=default_data_descriptions):
        self.dep_params = dep_params
        self.domain_system:Hotel= Hotel(data, dep_innate_full, dep_params, data_descriptions)
        self.state_tracker:Hotel_State_Tracker= Hotel_State_Tracker(self.domain_system, **dep_params)
        self.domain_dep:Dependency_Evaluator = Dependency_Evaluator(self.domain_system, self.state_tracker, dep_full)
    # domain actions
    def show_available_rooms(self):
        return self._check_dep_and_do("show_available_rooms")
    def show_room_change_options(self):
        return self._check_dep_and_do("show_room_change_options")
    def book_room(self, **kwargs):
        return self._check_dep_and_do("book_room", **kwargs)
    def find_booking_info(self, **kwargs):
        return self._check_dep_and_do("find_booking_info", **kwargs)
    def cancel_reservation(self, **kwargs):
        return self._check_dep_and_do("cancel_reservation", **kwargs)
    def modify_reservation(self, **kwargs):
        return self._check_dep_and_do("modify_reservation", **kwargs)
    def process_guest_checkin(self, **kwargs):
        return self._check_dep_and_do("process_guest_checkin", **kwargs)
    def process_guest_checkout(self, **kwargs):
        return self._check_dep_and_do("process_guest_checkout", **kwargs)
    def request_room_change(self, **kwargs):
        return self._check_dep_and_do("request_room_change", **kwargs)
    def place_room_service_order(self, **kwargs):
        return self._check_dep_and_do("place_room_service_order", **kwargs)
    def register_loyalty_member(self, **kwargs):
        return self._check_dep_and_do("register_loyalty_member", **kwargs)
    # internal utility functions
    def internal_get_room_checkin_details(self):
        return self._check_dep_and_do("internal_get_room_checkin_details")
    def internal_get_booking_details(self):
        return self._check_dep_and_do("internal_get_booking_details")
    def internal_get_loyalty_member_info(self, **kwargs):
        return self._check_dep_and_do("internal_get_loyalty_member_info", **kwargs)
    def internal_get_interaction_time(self):
        return self._check_dep_and_do("internal_get_interaction_time")
    def internal_get_room_service_order_details(self):
        return self._check_dep_and_do("internal_get_room_service_order_details")
    def internal_get_room_assignment(self):
        return self._check_dep_and_do("internal_get_room_assignment")
    def internal_compute_room_service_order_fee(self, **kwargs):
        return self._check_dep_and_do("internal_compute_room_service_order_fee", **kwargs)
    # internal constraints
    def internal_valid_room_type(self, **kwargs):
        return self._check_dep_and_do("internal_valid_room_type", **kwargs)
    def internal_is_loyalty_member(self, **kwargs):
        return self._check_dep_and_do("internal_is_loyalty_member", **kwargs)
    def internal_valid_room_change_reason(self, **kwargs):
        return self._check_dep_and_do("internal_valid_room_change_reason", **kwargs)
    def internal_valid_room_service_order_type(self, **kwargs):
        return self._check_dep_and_do("internal_valid_room_service_order_type", **kwargs)
    def internal_valid_room_service_item(self, **kwargs):
        return self._check_dep_and_do("internal_valid_room_service_item", **kwargs)
    def internal_valid_room_id(self, **kwargs):
        return self._check_dep_and_do("internal_valid_room_id", **kwargs)
    def internal_valid_room_service_payment_method(self, **kwargs):
        return self._check_dep_and_do("internal_valid_room_service_payment_method", **kwargs)
    # evaluation functions, solely used for testing this domain_system in the pipeline
    def evaluation_get_database(self)->dict:
        return self.domain_system.evaluation_get_database()
    def evaluation_get_database_descriptions(self)->dict:
        return self.domain_system.evaluation_get_database_descriptions()
    def evaluation_get_innate_state_tracker(self)->Hotel_State_Tracker:
        return self.domain_system.evaluation_get_innate_state_tracker()
    def evaluation_get_dependency_parameters(self)->dict:
        return self.dep_params
    def evaluation_get_domain_system(self)->Hotel:
        return self.domain_system
    def evaluation_get_dependency_evaluator(self)->Dependency_Evaluator:
        return self.domain_dep
    def evaluation_get_state_tracker(self)->Hotel_State_Tracker:
        return self.state_tracker  
    # internal functions
    def _check_dep_and_do(self, method_str, **kwargs):
        if not self.domain_dep.process(method_str=method_str, **kwargs): return False
        return getattr(self.domain_system, method_str)(**kwargs)