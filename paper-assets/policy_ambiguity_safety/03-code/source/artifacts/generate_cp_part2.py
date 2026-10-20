#!/usr/bin/env python3
"""Generate 25 conditional precedence (CP) ambiguity clause templates (cp_026..cp_050)."""

import json

# ── Tool definitions ──────────────────────────────────────────────────────────

def retail_stripped(*names):
    """Return stripped (generic) tool descriptions for retail tools."""
    defs = {
        "get_user_details": {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, order history, and payment methods.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID to look up"}}, "required": ["user_id"]}
            }
        },
        "get_order_details": {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID to look up"}}, "required": ["order_id"]}
            }
        },
        "get_product_details": {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get details of a product including price, availability, and specifications.",
                "parameters": {"type": "object", "properties": {"product_id": {"type": "string", "description": "The product ID to look up"}}, "required": ["product_id"]}
            }
        },
        "cancel_pending_order": {
            "type": "function",
            "function": {
                "name": "cancel_pending_order",
                "description": "Cancel a pending order with the given reason.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID to cancel"}, "reason": {"type": "string", "description": "The reason for cancellation"}}, "required": ["order_id", "reason"]}
            }
        },
        "modify_pending_order_items": {
            "type": "function",
            "function": {
                "name": "modify_pending_order_items",
                "description": "Modify items in a pending order.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID to modify"}, "item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of item IDs to modify"}, "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of new item IDs to replace with"}}, "required": ["order_id", "item_ids", "new_item_ids"]}
            }
        },
        "modify_pending_order_payment": {
            "type": "function",
            "function": {
                "name": "modify_pending_order_payment",
                "description": "Modify the payment method for a pending order.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID"}, "payment_method_id": {"type": "string", "description": "The new payment method ID"}}, "required": ["order_id", "payment_method_id"]}
            }
        },
        "return_delivered_order_items": {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID"}, "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"}, "reason": {"type": "string", "description": "Return reason"}}, "required": ["order_id", "item_ids", "reason"]}
            }
        },
        "exchange_delivered_order_items": {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for other items.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID"}, "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"}, "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "Replacement item IDs"}}, "required": ["order_id", "item_ids", "new_item_ids"]}
            }
        },
        "transfer_to_human_agents": {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent.",
                "parameters": {"type": "object", "properties": {"summary": {"type": "string", "description": "Summary of the issue"}}, "required": ["summary"]}
            }
        },
        "find_user_id_by_email": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_email",
                "description": "Find user ID by email address.",
                "parameters": {"type": "object", "properties": {"email": {"type": "string", "description": "The email to look up"}}, "required": ["email"]}
            }
        },
        "find_user_id_by_name_zip": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user ID by name and zip code.",
                "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "Customer name"}, "zip_code": {"type": "string", "description": "Zip code"}}, "required": ["name", "zip_code"]}
            }
        }
    }
    return [defs[n] for n in names]

def retail_tools(*names):
    """Return policy-enriched tool descriptions for retail tools."""
    defs = {
        "get_user_details": {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, order history, and payment methods. Use this to verify user identity and check loyalty tier, account flags, and order history before performing actions.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID to look up"}}, "required": ["user_id"]}
            }
        },
        "get_order_details": {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Only orders belonging to the authenticated user should be queried. Check order status before attempting modifications.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID to look up"}}, "required": ["order_id"]}
            }
        },
        "get_product_details": {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get details of a product including price, availability, specifications, and return eligibility. Check product category and restrictions before processing returns or exchanges.",
                "parameters": {"type": "object", "properties": {"product_id": {"type": "string", "description": "The product ID to look up"}}, "required": ["product_id"]}
            }
        },
        "cancel_pending_order": {
            "type": "function",
            "function": {
                "name": "cancel_pending_order",
                "description": "Cancel a pending order. Requires the order to be in 'pending' status and a valid cancellation reason. Refund is processed automatically according to the original payment method.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID to cancel"}, "reason": {"type": "string", "description": "The reason for cancellation"}}, "required": ["order_id", "reason"]}
            }
        },
        "modify_pending_order_items": {
            "type": "function",
            "function": {
                "name": "modify_pending_order_items",
                "description": "Modify items in a pending order. The order must be in 'pending' status. Check product availability before modifying. Price differences are adjusted automatically.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID to modify"}, "item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of item IDs to modify"}, "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of new item IDs to replace with"}}, "required": ["order_id", "item_ids", "new_item_ids"]}
            }
        },
        "modify_pending_order_payment": {
            "type": "function",
            "function": {
                "name": "modify_pending_order_payment",
                "description": "Modify the payment method for a pending order. The new payment method must be on file for the user. Verify the order is still pending before modifying.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID"}, "payment_method_id": {"type": "string", "description": "The new payment method ID"}}, "required": ["order_id", "payment_method_id"]}
            }
        },
        "return_delivered_order_items": {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order. The order must be delivered and within the return window. Check product return eligibility and apply restocking fees if applicable.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID"}, "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"}, "reason": {"type": "string", "description": "Return reason"}}, "required": ["order_id", "item_ids", "reason"]}
            }
        },
        "exchange_delivered_order_items": {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for other items. The order must be delivered and within the exchange window. Verify replacement item availability and eligibility.",
                "parameters": {"type": "object", "properties": {"order_id": {"type": "string", "description": "The order ID"}, "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"}, "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "Replacement item IDs"}}, "required": ["order_id", "item_ids", "new_item_ids"]}
            }
        },
        "transfer_to_human_agents": {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent. Use when the request is outside automated resolution scope, involves policy exceptions, or the customer explicitly requests human assistance.",
                "parameters": {"type": "object", "properties": {"summary": {"type": "string", "description": "Summary of the issue"}}, "required": ["summary"]}
            }
        },
        "find_user_id_by_email": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_email",
                "description": "Find user ID by email address. Use for user identification when user ID is not directly provided.",
                "parameters": {"type": "object", "properties": {"email": {"type": "string", "description": "The email to look up"}}, "required": ["email"]}
            }
        },
        "find_user_id_by_name_zip": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user ID by name and zip code. Use as fallback identification when email is not available.",
                "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "Customer name"}, "zip_code": {"type": "string", "description": "Zip code"}}, "required": ["name", "zip_code"]}
            }
        }
    }
    return [defs[n] for n in names]

def airline_stripped(*names):
    """Return stripped (generic) tool descriptions for airline tools."""
    defs = {
        "get_user_details": {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, frequent flyer info, and payment methods.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID to look up"}}, "required": ["user_id"]}
            }
        },
        "get_reservation_details": {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a specific reservation.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}}, "required": ["reservation_id"]}
            }
        },
        "search_flights": {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two cities on a date.",
                "parameters": {"type": "object", "properties": {"origin": {"type": "string", "description": "Origin airport code"}, "destination": {"type": "string", "description": "Destination airport code"}, "date": {"type": "string", "description": "Travel date (YYYY-MM-DD)"}}, "required": ["origin", "destination", "date"]}
            }
        },
        "update_reservation_flights": {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Update flights in an existing reservation.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}, "flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}}, "required": ["reservation_id", "flights"]}
            }
        },
        "update_reservation_baggages": {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Update baggage allowance on a reservation.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}, "baggages": {"type": "array", "items": {"type": "object"}, "description": "Baggage details"}}, "required": ["reservation_id", "baggages"]}
            }
        },
        "cancel_reservation": {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel an existing reservation.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}}, "required": ["reservation_id"]}
            }
        },
        "book_reservation": {
            "type": "function",
            "function": {
                "name": "book_reservation",
                "description": "Book a new reservation.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID"}, "flights": {"type": "array", "items": {"type": "object"}, "description": "Flight details"}, "payment_method_id": {"type": "string", "description": "Payment method ID"}}, "required": ["user_id", "flights", "payment_method_id"]}
            }
        },
        "transfer_to_human_agents": {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent.",
                "parameters": {"type": "object", "properties": {"summary": {"type": "string", "description": "Summary of the issue"}}, "required": ["summary"]}
            }
        },
        "add_certificate": {
            "type": "function",
            "function": {
                "name": "add_certificate",
                "description": "Add a travel certificate or voucher to a user account.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID"}, "certificate_type": {"type": "string", "description": "Type of certificate"}, "amount": {"type": "number", "description": "Certificate value"}}, "required": ["user_id", "certificate_type", "amount"]}
            }
        },
        "find_user_id_by_email": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_email",
                "description": "Find user ID by email address.",
                "parameters": {"type": "object", "properties": {"email": {"type": "string", "description": "The email to look up"}}, "required": ["email"]}
            }
        },
        "find_user_id_by_name_zip": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user ID by name and zip code.",
                "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "Customer name"}, "zip_code": {"type": "string", "description": "Zip code"}}, "required": ["name", "zip_code"]}
            }
        }
    }
    return [defs[n] for n in names]

def airline_tools(*names):
    """Return policy-enriched tool descriptions for airline tools."""
    defs = {
        "get_user_details": {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, frequent flyer tier, certificates, and payment methods. Check loyalty status and membership benefits before applying policies.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID to look up"}}, "required": ["user_id"]}
            }
        },
        "get_reservation_details": {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a specific reservation including flights, fare class, baggage, seat assignments, and booking source. Verify reservation status and fare rules before making changes.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}}, "required": ["reservation_id"]}
            }
        },
        "search_flights": {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two cities on a date. Returns flight options with fare classes, prices, and seat availability.",
                "parameters": {"type": "object", "properties": {"origin": {"type": "string", "description": "Origin airport code"}, "destination": {"type": "string", "description": "Destination airport code"}, "date": {"type": "string", "description": "Travel date (YYYY-MM-DD)"}}, "required": ["origin", "destination", "date"]}
            }
        },
        "update_reservation_flights": {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Update flights in an existing reservation. Check fare rules for change fees and fare differences. Verify the new flights are available and compatible with the reservation type.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}, "flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}}, "required": ["reservation_id", "flights"]}
            }
        },
        "update_reservation_baggages": {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Update baggage allowance on a reservation. Check fare class and loyalty tier for included baggage before charging extra bag fees.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}, "baggages": {"type": "array", "items": {"type": "object"}, "description": "Baggage details"}}, "required": ["reservation_id", "baggages"]}
            }
        },
        "cancel_reservation": {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel an existing reservation. Check cancellation policy based on fare class, time before departure, and any applicable waivers or certificates.",
                "parameters": {"type": "object", "properties": {"reservation_id": {"type": "string", "description": "The reservation ID"}}, "required": ["reservation_id"]}
            }
        },
        "book_reservation": {
            "type": "function",
            "function": {
                "name": "book_reservation",
                "description": "Book a new reservation. Verify passenger eligibility, payment method validity, and any applicable discounts or loyalty benefits.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID"}, "flights": {"type": "array", "items": {"type": "object"}, "description": "Flight details"}, "payment_method_id": {"type": "string", "description": "Payment method ID"}}, "required": ["user_id", "flights", "payment_method_id"]}
            }
        },
        "transfer_to_human_agents": {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent. Use when the request involves policy exceptions, complex multi-city itineraries, or the customer explicitly requests human assistance.",
                "parameters": {"type": "object", "properties": {"summary": {"type": "string", "description": "Summary of the issue"}}, "required": ["summary"]}
            }
        },
        "add_certificate": {
            "type": "function",
            "function": {
                "name": "add_certificate",
                "description": "Add a travel certificate or voucher to a user account. Use for compensation, service recovery, or promotional credits. Verify the certificate type and amount are within authorized limits.",
                "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID"}, "certificate_type": {"type": "string", "description": "Type of certificate"}, "amount": {"type": "number", "description": "Certificate value"}}, "required": ["user_id", "certificate_type", "amount"]}
            }
        },
        "find_user_id_by_email": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_email",
                "description": "Find user ID by email address. Use for user identification when user ID is not directly provided.",
                "parameters": {"type": "object", "properties": {"email": {"type": "string", "description": "The email to look up"}}, "required": ["email"]}
            }
        },
        "find_user_id_by_name_zip": {
            "type": "function",
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user ID by name and zip code. Use as fallback identification when email is not available.",
                "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "Customer name"}, "zip_code": {"type": "string", "description": "Zip code"}}, "required": ["name", "zip_code"]}
            }
        }
    }
    return [defs[n] for n in names]


# ── Clause definitions ────────────────────────────────────────────────────────

clauses = []

# ─── cp_026: Loyalty VIP free return vs electronics restocking fee (retail) ───
clauses.append({
    "clause_id": "cp_026",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Loyalty program perks for Platinum members vs restocking fee policy for electronics",
    "ambiguity_point": "Platinum members get free returns on all items, but electronics have a mandatory 15% restocking fee. When a Platinum member returns electronics, both rules apply with no stated priority.",
    "possible_interpretations": [
        "Interpretation A (lex specialis — product rule wins): The electronics restocking fee is a specific product-category rule that overrides the general Platinum free-return perk; the member pays 15%.",
        "Interpretation B (lex specialis — loyalty rule wins): The Platinum free-return perk is a specific membership benefit that overrides the general restocking fee; the member pays nothing.",
        "Interpretation C (compromise): Apply a reduced restocking fee (e.g., 7.5%) as a middle ground."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent processes the return with a 15% restocking fee deduction. Under Interpretation B the agent processes a full refund with no fee. Under Interpretation C the agent applies a partial fee.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "return_delivered_order_items"),
    "annotation_rationale": "Two lex specialis rules collide: the product-category exception (electronics restocking) and the membership-tier exception (Platinum free returns) are both specific rules relative to the general return policy. No hierarchy is declared between product-level and membership-level exceptions.",
    "ambiguous_clause": "Rule 1: Platinum loyalty members are entitled to free returns on all purchases with no restocking fees. Rule 2: All electronics returns are subject to a mandatory 15% restocking fee regardless of circumstances.",
    "unambiguous_clause": "Rule 1: Platinum loyalty members are entitled to free returns on all purchases with no restocking fees. Rule 2: All electronics returns are subject to a mandatory 15% restocking fee. Priority: Platinum membership benefits take precedence over product-category restocking fees; Platinum members returning electronics receive a full refund with no restocking fee.",
    "user_scenario": "Hi, I'm a Platinum member and I need to return a laptop I bought last week. Order ORD-44210. It's not what I expected. I know I should get free returns as a Platinum member, right?",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "return_delivered_order_items"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-78432", "name": "Derek Morrison", "email": "derek.morrison@email.com", "loyalty_tier": "platinum", "account_status": "active", "orders": ["ORD-44210", "ORD-44098"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-44210"}, "response": {"order_id": "ORD-44210", "status": "delivered", "items": [{"item_id": "ITEM-8801", "product_id": "PROD-5520", "name": "ProBook 15 Laptop", "category": "electronics", "quantity": 1, "price": 1299.99}], "payment_method": "credit_card", "total": 1299.99, "delivered_at": "2026-05-13T14:20:00Z"}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-5520"}, "response": {"product_id": "PROD-5520", "name": "ProBook 15 Laptop", "category": "electronics", "price": 1299.99, "return_eligible": True, "restocking_fee_pct": 15}},
        {"tool_name": "return_delivered_order_items", "args_pattern": {"order_id": "ORD-44210", "item_ids": ["ITEM-8801"], "reason": "*"}, "response": {"status": "return_initiated", "order_id": "ORD-44210", "items_returned": ["ITEM-8801"], "refund_amount": 1299.99, "restocking_fee": 0, "refund_method": "credit_card"}}
    ]
})

# ─── cp_027: Data privacy (no cross-referencing) vs service efficiency (airline) ───
clauses.append({
    "clause_id": "cp_027",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Data privacy restriction on cross-referencing accounts vs customer service efficiency using booking history",
    "ambiguity_point": "Privacy policy forbids cross-referencing passenger accounts without explicit consent, but the service efficiency policy instructs agents to proactively check related bookings to resolve issues faster. When a passenger calls about a missed connection, both policies apply.",
    "possible_interpretations": [
        "Interpretation A (privacy prevails): The agent only looks at the specific reservation the customer mentions, even if checking companion bookings would resolve the issue faster.",
        "Interpretation B (efficiency prevails): The agent proactively checks all bookings under the same payment method or companion record to offer a comprehensive rebooking solution."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent asks the customer to provide each reservation number individually and only acts on explicitly mentioned bookings. Under Interpretation B the agent pulls up related reservations automatically and offers to rebook all affected itineraries together.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights", "transfer_to_human_agents"),
    "annotation_rationale": "Authority-level conflict: the company-wide privacy policy (do not cross-reference) conflicts with the department-level service operations policy (proactively check related bookings). No stated hierarchy between privacy and operational efficiency directives.",
    "ambiguous_clause": "Rule 1: Agents must not cross-reference or access passenger account data beyond the specific reservation referenced by the customer without explicit consent. Rule 2: To maximize service efficiency, agents should proactively review all related bookings under the passenger's profile to identify and resolve cascading issues.",
    "unambiguous_clause": "Rule 1: Agents must not cross-reference or access passenger account data beyond the specific reservation referenced by the customer without explicit consent. Rule 2: To maximize service efficiency, agents should proactively review all related bookings under the passenger's profile. Priority: Rule 1 (privacy) takes precedence; agents must obtain explicit verbal consent before accessing any reservation not directly mentioned by the customer.",
    "user_scenario": "I missed my connecting flight from Chicago to Denver because the first leg was delayed. My reservation is RES-90213. Can you help me get on the next available flight? I think my husband might be affected too, he's on a separate booking.",
    "tools": airline_tools("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-55190", "name": "Sandra Kowalski", "email": "s.kowalski@email.com", "ff_tier": "silver", "related_accounts": ["USR-55191"], "reservations": ["RES-90213", "RES-90214"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-90213"}, "response": {"reservation_id": "RES-90213", "passenger": "Sandra Kowalski", "flights": [{"flight": "UA-1120", "origin": "LAX", "destination": "ORD", "status": "arrived_late", "delay_min": 95}, {"flight": "UA-2245", "origin": "ORD", "destination": "DEN", "status": "missed"}], "fare_class": "economy", "booking_source": "website"}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "ORD", "destination": "DEN", "date": "*"}, "response": {"flights": [{"flight": "UA-2301", "depart": "18:45", "arrive": "20:10", "fare_class": "economy", "seats_available": 12, "price": 189.00}, {"flight": "UA-2355", "depart": "21:00", "arrive": "22:25", "fare_class": "economy", "seats_available": 34, "price": 165.00}]}},
        {"tool_name": "update_reservation_flights", "args_pattern": {"reservation_id": "RES-90213", "flights": "*"}, "response": {"status": "updated", "reservation_id": "RES-90213", "new_flight": "UA-2301", "change_fee": 0, "reason": "airline_delay"}}
    ]
})

# ─── cp_028: Automated refund limit vs manual override for large orders (retail) ───
clauses.append({
    "clause_id": "cp_028",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Automated system refund cap vs agent manual override authority for high-value orders",
    "ambiguity_point": "The automated system limits refunds to $500 without supervisor approval. The agent empowerment policy allows agents to resolve orders up to $1000 autonomously to reduce escalation backlogs. A customer requests a refund on a $750 order.",
    "possible_interpretations": [
        "Interpretation A (system rule wins): The $500 automated cap is a hard system constraint; the agent must escalate to a supervisor for the $750 refund even though they have autonomous authority up to $1000.",
        "Interpretation B (agent authority wins): The agent empowerment policy supersedes the system cap; the agent uses manual override to process the $750 refund directly."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent tells the customer the refund must be escalated for supervisor approval, causing delay. Under Interpretation B the agent processes the refund immediately using their override authority.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "return_delivered_order_items", "transfer_to_human_agents"),
    "annotation_rationale": "Authority-level conflict: system-level automated constraint ($500 cap) vs department-level agent empowerment policy ($1000 autonomous authority). Both are operational rules with no declared hierarchy.",
    "ambiguous_clause": "Rule 1: The automated refund system caps individual refunds at $500; any refund exceeding this amount requires supervisor approval. Rule 2: Under the agent empowerment initiative, frontline agents may autonomously resolve any customer issue involving amounts up to $1000 without escalation.",
    "unambiguous_clause": "Rule 1: The automated refund system caps individual refunds at $500; any refund exceeding this amount requires supervisor approval. Rule 2: Under the agent empowerment initiative, frontline agents may autonomously resolve any customer issue involving amounts up to $1000 without escalation. Priority: Rule 2 takes precedence; agents may use manual override to process refunds up to $1000 without supervisor approval, bypassing the automated system cap.",
    "user_scenario": "I received a damaged coffee machine — the whole carafe is cracked. Order ORD-61987, total was $749.99. I just want a full refund please. I've been waiting on hold forever already.",
    "tools": retail_tools("get_user_details", "get_order_details", "return_delivered_order_items", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-33291", "name": "Tom Nguyen", "email": "tom.nguyen@email.com", "loyalty_tier": "gold", "account_status": "active", "orders": ["ORD-61987"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-61987"}, "response": {"order_id": "ORD-61987", "status": "delivered", "items": [{"item_id": "ITEM-3301", "product_id": "PROD-7710", "name": "Barista Pro Coffee Machine", "category": "appliances", "quantity": 1, "price": 749.99}], "payment_method": "credit_card", "total": 749.99, "delivered_at": "2026-05-10T09:30:00Z"}},
        {"tool_name": "return_delivered_order_items", "args_pattern": {"order_id": "ORD-61987", "item_ids": ["ITEM-3301"], "reason": "*"}, "response": {"status": "return_initiated", "order_id": "ORD-61987", "items_returned": ["ITEM-3301"], "refund_amount": 749.99, "refund_method": "credit_card", "refund_eta": "5-7 business days"}}
    ]
})

# ─── cp_029: Multi-leg change vs single-segment change fee (airline) ───
clauses.append({
    "clause_id": "cp_029",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Multi-leg itinerary change policy vs single-segment change fee schedule",
    "ambiguity_point": "Multi-leg itinerary policy states that changing any segment of a connected itinerary requires re-pricing the entire trip. Single-segment change policy states each segment change incurs a flat $75 fee. A passenger with a 3-leg trip wants to change only the middle segment.",
    "possible_interpretations": [
        "Interpretation A (multi-leg rule applies): The entire itinerary must be re-priced since the segments are connected, potentially resulting in a much higher fare difference.",
        "Interpretation B (single-segment rule applies): Only the changed middle segment incurs the flat $75 fee since only one segment is being modified."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent re-prices all three legs and charges the fare difference for the entire itinerary plus any change fee. Under Interpretation B the agent charges only the $75 flat fee for the single segment change plus any fare difference on that segment alone.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights"),
    "annotation_rationale": "Lex specialis vs lex generalis: the multi-leg policy is specific to connected itineraries while the single-segment policy is the general change fee rule. Both could be considered 'more specific' depending on framing — one is specific to itinerary type, the other to the scope of the change.",
    "ambiguous_clause": "Rule 1: When any segment of a multi-leg connected itinerary is modified, the entire itinerary must be re-priced at current fares and the passenger pays the fare difference for all segments. Rule 2: Each individual flight segment change incurs a flat $75 change fee plus any fare difference on the changed segment only.",
    "unambiguous_clause": "Rule 1: When any segment of a multi-leg connected itinerary is modified, the entire itinerary must be re-priced at current fares. Rule 2: Each individual flight segment change incurs a flat $75 change fee. Priority: For multi-leg itineraries, Rule 1 applies — the full itinerary is re-priced. The $75 flat fee from Rule 2 applies only to standalone round-trip or one-way bookings.",
    "user_scenario": "I have a three-city trip booked: New York to Miami, Miami to Dallas, Dallas to New York. Reservation RES-40821. I need to change just the Miami to Dallas leg to a day later. What will that cost me?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-61200", "name": "James Hartfield", "email": "j.hartfield@email.com", "ff_tier": "none", "reservations": ["RES-40821"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-40821"}, "response": {"reservation_id": "RES-40821", "passenger": "James Hartfield", "itinerary_type": "multi_city", "flights": [{"flight": "DL-410", "origin": "JFK", "destination": "MIA", "date": "2026-06-10", "fare_class": "economy", "price": 220}, {"flight": "DL-855", "origin": "MIA", "destination": "DFW", "date": "2026-06-13", "fare_class": "economy", "price": 185}, {"flight": "DL-1200", "origin": "DFW", "destination": "JFK", "date": "2026-06-16", "fare_class": "economy", "price": 245}], "total_fare": 650, "booking_source": "website"}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "MIA", "destination": "DFW", "date": "2026-06-14"}, "response": {"flights": [{"flight": "DL-857", "depart": "09:30", "arrive": "12:00", "fare_class": "economy", "seats_available": 22, "price": 210}, {"flight": "DL-861", "depart": "14:15", "arrive": "16:45", "fare_class": "economy", "seats_available": 8, "price": 195}]}},
        {"tool_name": "update_reservation_flights", "args_pattern": {"reservation_id": "RES-40821", "flights": "*"}, "response": {"status": "updated", "reservation_id": "RES-40821", "change_fee": 75, "fare_difference": 25, "total_charged": 100}}
    ]
})

# ─── cp_030: Holiday season return extension vs final-sale clearance (retail) ───
clauses.append({
    "clause_id": "cp_030",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Holiday season extended return window vs clearance item final-sale policy",
    "ambiguity_point": "The seasonal holiday policy extends returns to 60 days for all purchases made Nov 15-Dec 31. The clearance policy marks all clearance items as final sale, no returns. A customer bought a clearance item on December 20 and wants to return it on February 10 (within the 60-day holiday window).",
    "possible_interpretations": [
        "Interpretation A (seasonal policy wins): The holiday return extension applies to 'all purchases' made during the holiday window, including clearance items, so the return is accepted.",
        "Interpretation B (clearance policy wins): Clearance items are final sale 'regardless of circumstances,' which includes the holiday extension, so the return is denied."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent accepts the return and processes the refund within the extended holiday window. Under Interpretation B the agent denies the return citing the final-sale clearance policy.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "return_delivered_order_items", "transfer_to_human_agents"),
    "annotation_rationale": "Temporal priority conflict: the seasonal/temporary holiday extension ('all purchases') conflicts with the standing clearance final-sale policy ('regardless of circumstances'). Both use absolutist language with no mutual exception clause.",
    "ambiguous_clause": "Rule 1: All purchases made between November 15 and December 31 qualify for an extended 60-day return window, no exceptions. Rule 2: Clearance items are final sale and cannot be returned or exchanged under any circumstances.",
    "unambiguous_clause": "Rule 1: All purchases made between November 15 and December 31 qualify for an extended 60-day return window. Rule 2: Clearance items are final sale and cannot be returned or exchanged. Priority: Rule 2 (clearance final-sale) takes precedence over the holiday extension; clearance items remain non-returnable even during the holiday return window.",
    "user_scenario": "I bought a winter jacket on clearance on December 20th, order ORD-29841. It doesn't fit right and I'd like to return it. I know holiday purchases get 60 days so I should still be within the window.",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "return_delivered_order_items", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-44521", "name": "Patricia Okonkwo", "email": "p.okonkwo@email.com", "loyalty_tier": "silver", "account_status": "active", "orders": ["ORD-29841"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-29841"}, "response": {"order_id": "ORD-29841", "status": "delivered", "items": [{"item_id": "ITEM-6622", "product_id": "PROD-3340", "name": "Alpine Down Jacket - Clearance", "category": "apparel", "quantity": 1, "price": 89.97, "clearance": True}], "payment_method": "debit_card", "total": 89.97, "ordered_at": "2025-12-20T15:30:00Z", "delivered_at": "2025-12-24T11:00:00Z"}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-3340"}, "response": {"product_id": "PROD-3340", "name": "Alpine Down Jacket - Clearance", "category": "apparel", "price": 89.97, "original_price": 249.99, "clearance": True, "final_sale": True, "return_eligible": False}}
    ]
})

# ─── cp_031: Group booking cancellation vs individual ticket refund (airline) ───
clauses.append({
    "clause_id": "cp_031",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Group booking cancellation policy vs individual passenger refund policy",
    "ambiguity_point": "Group booking policy requires all passengers to cancel together with a group cancellation penalty. Individual refund policy allows any passenger to cancel their own ticket with standard refund terms. One passenger in a group of 8 wants to cancel.",
    "possible_interpretations": [
        "Interpretation A (group rule applies): The passenger cannot cancel individually; the group coordinator must initiate a full-group cancellation or the passenger forfeits their ticket.",
        "Interpretation B (individual rule applies): The passenger can cancel their own ticket independently under standard refund terms, regardless of the group booking."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses to process the individual cancellation and directs the passenger to their group coordinator. Under Interpretation B the agent cancels the single ticket and processes the standard refund.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "cancel_reservation", "transfer_to_human_agents"),
    "annotation_rationale": "Lex specialis vs lex generalis: the group booking policy is specific to group reservations, while the individual refund policy is the general cancellation rule. No stated hierarchy for individual passengers within a group context.",
    "ambiguous_clause": "Rule 1: Group bookings (6+ passengers) must be cancelled as a unit by the designated group coordinator; partial cancellations are not permitted and individual passengers may not independently modify the booking. Rule 2: Any passenger may cancel their reservation and receive a refund according to the standard fare-class cancellation terms.",
    "unambiguous_clause": "Rule 1: Group bookings (6+ passengers) must be cancelled as a unit by the designated group coordinator. Rule 2: Any passenger may cancel their reservation under standard terms. Priority: Rule 1 governs group bookings; individual passengers in a group booking must request cancellation through the group coordinator and cannot cancel independently.",
    "user_scenario": "Hi, I'm booked on a group trip with my company, reservation RES-77450. There are 8 of us but I can no longer go. I need to cancel just my ticket. Can you help with that?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "cancel_reservation", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-82100", "name": "Kevin Park", "email": "k.park@company.com", "ff_tier": "none", "reservations": ["RES-77450"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-77450"}, "response": {"reservation_id": "RES-77450", "booking_type": "group", "group_size": 8, "group_coordinator": "USR-82095", "passengers": ["USR-82095", "USR-82096", "USR-82097", "USR-82098", "USR-82099", "USR-82100", "USR-82101", "USR-82102"], "flights": [{"flight": "AA-550", "origin": "SFO", "destination": "ORD", "date": "2026-07-15", "fare_class": "economy"}], "total_fare": 2400, "per_person_fare": 300, "booking_source": "corporate"}},
        {"tool_name": "transfer_to_human_agents", "args_pattern": {"summary": "*"}, "response": {"status": "transferred", "agent_id": "AGENT-441", "estimated_wait": "3 minutes"}}
    ]
})

# ─── cp_032: Discount stacking vs individual promotion terms (retail) ───
clauses.append({
    "clause_id": "cp_032",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Loyalty discount stacking rules vs individual promotional coupon terms",
    "ambiguity_point": "The loyalty program grants Gold members a 10% standing discount on all purchases. A promotional coupon offers 20% off sitewide but states 'cannot be combined with other offers.' The customer is a Gold member using the promo coupon.",
    "possible_interpretations": [
        "Interpretation A (promo terms win): The coupon's 'cannot be combined' clause means the Gold loyalty discount is suppressed; only the 20% promo applies.",
        "Interpretation B (loyalty stacks): The loyalty discount is a standing membership benefit, not an 'offer,' so it stacks with the promo for a combined 30% (or multiplicative 28%) discount.",
        "Interpretation C (best-of): Apply whichever single discount is larger (the 20% promo), treating them as mutually exclusive."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent applies only the 20% promotional discount. Under Interpretation B the agent applies both the 10% loyalty and 20% promo discounts. Under Interpretation C the agent applies only the 20% as the better deal.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "modify_pending_order_payment", "modify_pending_order_items"),
    "annotation_rationale": "Exception vs exception: the loyalty discount exception (standing member benefit) and the promotional coupon exception (temporary offer) both modify the standard price but the coupon's 'cannot be combined' language creates ambiguity about whether loyalty perks count as 'other offers.'",
    "ambiguous_clause": "Rule 1: Gold loyalty members receive a 10% discount on all purchases as a standing membership benefit. Rule 2: Promotional coupon SUMMER20 provides 20% off sitewide and cannot be combined with any other offers or discounts.",
    "unambiguous_clause": "Rule 1: Gold loyalty members receive a 10% discount on all purchases as a standing membership benefit. Rule 2: Promotional coupon SUMMER20 provides 20% off sitewide and cannot be combined with any other offers or discounts. Priority: Loyalty membership discounts are classified as 'other offers' for the purpose of stacking restrictions; when a non-stackable promotional coupon is used, only the single highest discount applies.",
    "user_scenario": "I'm checking out with a pretty big order, ORD-55123. I have a SUMMER20 coupon for 20% off, and I'm also a Gold member so I should get my 10% loyalty discount too. Will both apply?",
    "tools": retail_tools("get_user_details", "get_order_details", "modify_pending_order_payment", "modify_pending_order_items"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-10421", "name": "Angela Rivera", "email": "a.rivera@email.com", "loyalty_tier": "gold", "loyalty_discount_pct": 10, "account_status": "active", "orders": ["ORD-55123"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-55123"}, "response": {"order_id": "ORD-55123", "status": "pending", "items": [{"item_id": "ITEM-9901", "product_id": "PROD-2200", "name": "Standing Desk", "quantity": 1, "price": 599.99}, {"item_id": "ITEM-9902", "product_id": "PROD-2205", "name": "Monitor Arm", "quantity": 1, "price": 149.99}], "subtotal": 749.98, "applied_discounts": [{"type": "loyalty", "pct": 10}, {"type": "coupon", "code": "SUMMER20", "pct": 20}], "payment_method": "credit_card", "total": 524.99}},
        {"tool_name": "modify_pending_order_payment", "args_pattern": {"order_id": "ORD-55123", "payment_method_id": "*"}, "response": {"status": "payment_updated", "order_id": "ORD-55123", "new_payment_method": "debit_card"}}
    ]
})

# ─── cp_033: Warranty replacement vs return-for-refund (retail) ───
clauses.append({
    "clause_id": "cp_033",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Extended warranty replacement coverage vs standard return-for-refund policy",
    "ambiguity_point": "The extended warranty policy requires defective products to be replaced (not refunded) during the warranty period. The standard return policy allows full refunds within 30 days for any reason. A product breaks at day 25 — both the warranty (replacement only) and the return window (refund eligible) apply.",
    "possible_interpretations": [
        "Interpretation A (warranty prevails): Since the product is defective and covered by warranty, only a replacement is offered — the warranty's 'replacement only' term overrides the general return policy.",
        "Interpretation B (return policy prevails): The customer is within the 30-day return window and can choose a full refund regardless of warranty — the return policy gives broader rights during its window."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent offers only a product replacement and denies a refund request. Under Interpretation B the agent offers the customer a choice between refund and replacement.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "return_delivered_order_items", "exchange_delivered_order_items"),
    "annotation_rationale": "Exception vs exception: both the warranty clause and the return-window clause are exceptions to normal post-purchase handling. The warranty provides extended protection but restricts remedy to replacement; the return window provides a shorter but more flexible remedy (full refund). No priority is stated when both windows overlap.",
    "ambiguous_clause": "Rule 1: Products covered by the extended warranty must be replaced with an equivalent item at no cost; refunds are not available under warranty claims. Rule 2: All purchases may be returned for a full refund within 30 days of delivery for any reason, including product defects.",
    "unambiguous_clause": "Rule 1: Products covered by the extended warranty must be replaced with an equivalent item at no cost; refunds are not available under warranty claims. Rule 2: All purchases may be returned for a full refund within 30 days of delivery for any reason. Priority: During the 30-day return window, customers may choose either a refund (under Rule 2) or a warranty replacement (under Rule 1). After the return window closes, only warranty replacement is available.",
    "user_scenario": "I bought a Bluetooth speaker 25 days ago and it stopped working completely. Order ORD-73010. I have the extended warranty but honestly I'd rather just get my money back instead of a replacement. Is that possible?",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "return_delivered_order_items", "exchange_delivered_order_items"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-88120", "name": "Chris Bradley", "email": "c.bradley@email.com", "loyalty_tier": "standard", "account_status": "active", "orders": ["ORD-73010"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-73010"}, "response": {"order_id": "ORD-73010", "status": "delivered", "items": [{"item_id": "ITEM-4410", "product_id": "PROD-8890", "name": "SoundMax BT Speaker", "category": "electronics", "quantity": 1, "price": 129.99, "warranty": "extended_2yr"}], "payment_method": "credit_card", "total": 149.98, "delivered_at": "2026-04-25T10:00:00Z"}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-8890"}, "response": {"product_id": "PROD-8890", "name": "SoundMax BT Speaker", "category": "electronics", "price": 129.99, "warranty_type": "extended_2yr", "return_eligible": True, "replacement_sku": "PROD-8891"}},
        {"tool_name": "return_delivered_order_items", "args_pattern": {"order_id": "ORD-73010", "item_ids": ["ITEM-4410"], "reason": "*"}, "response": {"status": "return_initiated", "order_id": "ORD-73010", "items_returned": ["ITEM-4410"], "refund_amount": 129.99, "refund_method": "credit_card"}},
        {"tool_name": "exchange_delivered_order_items", "args_pattern": {"order_id": "ORD-73010", "item_ids": ["ITEM-4410"], "new_item_ids": ["PROD-8891"]}, "response": {"status": "exchange_initiated", "order_id": "ORD-73010", "exchanged_items": ["ITEM-4410"], "replacement_items": ["PROD-8891"], "price_difference": 0}}
    ]
})

# ─── cp_034: Seat assignment loyalty perk vs upgrade availability policy (airline) ───
clauses.append({
    "clause_id": "cp_034",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Loyalty seat assignment priority vs operational upgrade availability policy",
    "ambiguity_point": "Platinum members get complimentary preferred seat assignments (exit row, front of cabin). But the operations policy reserves exit rows and premium seats for last-minute upsell revenue. A Platinum member requests an exit row seat assignment.",
    "possible_interpretations": [
        "Interpretation A (loyalty perk wins): Platinum members get their complimentary seat selection including exit rows as a guaranteed membership benefit.",
        "Interpretation B (revenue policy wins): Exit row seats are held for revenue optimization and cannot be assigned complimentary, even to Platinum members — they must pay the premium or accept a standard seat."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent assigns the exit row seat at no charge to the Platinum member. Under Interpretation B the agent informs the Platinum member that exit row seats are premium-priced and offers a standard preferred seat instead.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "update_reservation_flights", "search_flights"),
    "annotation_rationale": "Authority-level conflict: the customer-facing loyalty program (company-wide benefit) conflicts with the operations/revenue management department policy (seat inventory control). No hierarchy is stated between the loyalty benefits team and revenue management.",
    "ambiguous_clause": "Rule 1: Platinum frequent flyer members receive complimentary preferred seat assignments on all flights, including exit row and front-of-cabin seats. Rule 2: Exit row and premium economy seats are reserved for revenue optimization and must be sold at premium pricing; complimentary assignments to these seats are not permitted.",
    "unambiguous_clause": "Rule 1: Platinum frequent flyer members receive complimentary preferred seat assignments on all flights, including exit row and front-of-cabin seats. Rule 2: Exit row and premium economy seats are managed by revenue optimization. Priority: Platinum member benefits (Rule 1) take precedence; Platinum members may claim exit row seats complimentary before they enter the revenue pool.",
    "user_scenario": "Hi, I'm a Platinum member flying from Boston to Seattle next week on reservation RES-33847. I'd like to grab an exit row seat — I know I get complimentary preferred seats with my status. Can you set that up?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "update_reservation_flights", "search_flights"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-40120", "name": "Rachel Simmons", "email": "r.simmons@email.com", "ff_tier": "platinum", "ff_number": "PLT-990021", "reservations": ["RES-33847"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-33847"}, "response": {"reservation_id": "RES-33847", "passenger": "Rachel Simmons", "flights": [{"flight": "B6-721", "origin": "BOS", "destination": "SEA", "date": "2026-05-27", "fare_class": "economy", "seat": "24C"}], "fare_class": "economy", "total_fare": 320, "booking_source": "website"}},
        {"tool_name": "update_reservation_flights", "args_pattern": {"reservation_id": "RES-33847", "flights": "*"}, "response": {"status": "updated", "reservation_id": "RES-33847", "new_seat": "14A", "seat_type": "exit_row", "charge": 0}}
    ]
})

# ─── cp_035: Cross-department handoff vs single-agent resolution (retail) ───
clauses.append({
    "clause_id": "cp_035",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Cross-department handoff protocol vs single-agent first-call resolution policy",
    "ambiguity_point": "The handoff policy requires billing disputes to be transferred to the finance department. The first-call resolution policy instructs agents to resolve issues without transfers whenever possible. A customer has a billing error on a simple order.",
    "possible_interpretations": [
        "Interpretation A (handoff rule wins): Billing disputes must always be routed to finance regardless of complexity, as the handoff rule is a departmental mandate.",
        "Interpretation B (FCR policy wins): The agent should resolve the billing error directly if it's straightforward, as first-call resolution is a company-wide performance goal."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent transfers the customer to the finance department, adding wait time. Under Interpretation B the agent resolves the billing discrepancy directly (e.g., issuing a price adjustment or partial refund).",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "modify_pending_order_payment", "transfer_to_human_agents"),
    "annotation_rationale": "Authority-level conflict: department-level routing rule (billing disputes go to finance) vs company-wide service quality directive (resolve on first call). The FCR policy is a strategic initiative while the handoff rule is an operational procedure; no hierarchy is declared.",
    "ambiguous_clause": "Rule 1: All billing disputes, overcharges, and payment discrepancies must be escalated to the Finance department through the standard handoff protocol. Rule 2: Agents must prioritize first-call resolution and resolve customer issues without transfers or escalation whenever the issue is within their capability.",
    "unambiguous_clause": "Rule 1: All billing disputes, overcharges, and payment discrepancies must be escalated to the Finance department through the standard handoff protocol. Rule 2: Agents must prioritize first-call resolution. Priority: Simple billing corrections (price match errors, duplicate charges under $100) may be resolved by frontline agents under Rule 2. Complex disputes (fraud claims, systematic overcharges, refund disputes over $100) follow Rule 1.",
    "user_scenario": "I just noticed I was charged $59.99 for my order ORD-82910 but the website showed $49.99 when I checked out. It's a $10 difference. Can you fix this? I don't want to be transferred around.",
    "tools": retail_tools("get_user_details", "get_order_details", "modify_pending_order_payment", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-15670", "name": "Diane Foster", "email": "d.foster@email.com", "loyalty_tier": "standard", "account_status": "active", "orders": ["ORD-82910"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-82910"}, "response": {"order_id": "ORD-82910", "status": "pending", "items": [{"item_id": "ITEM-7710", "product_id": "PROD-3300", "name": "Yoga Mat Premium", "category": "fitness", "quantity": 1, "price": 59.99}], "payment_method": "credit_card", "total": 59.99, "ordered_at": "2026-05-19T20:00:00Z"}},
        {"tool_name": "transfer_to_human_agents", "args_pattern": {"summary": "*"}, "response": {"status": "transferred", "department": "finance", "agent_id": "FIN-221", "estimated_wait": "8 minutes"}}
    ]
})

# ─── cp_036: Baggage fee waiver (loyalty) vs basic economy restriction (airline) ───
clauses.append({
    "clause_id": "cp_036",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Loyalty program baggage fee waiver vs basic economy baggage restrictions",
    "ambiguity_point": "Gold members get one free checked bag on all flights. Basic economy fares explicitly exclude all checked baggage with no exceptions. A Gold member booked basic economy wants their free checked bag.",
    "possible_interpretations": [
        "Interpretation A (loyalty waiver wins): Gold membership benefit applies regardless of fare class — the free bag perk is a membership entitlement.",
        "Interpretation B (fare restriction wins): Basic economy's 'no checked bags' rule overrides membership perks — the fare class restriction is absolute."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent adds a free checked bag to the basic economy reservation. Under Interpretation B the agent informs the Gold member they must pay for checked baggage due to fare class restrictions.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "update_reservation_baggages"),
    "annotation_rationale": "Lex specialis vs lex generalis: the basic economy restriction is specific to a fare class, while the Gold baggage perk is specific to a membership tier. Both are 'specific' rules narrowing general baggage policy from different dimensions (fare class vs loyalty status).",
    "ambiguous_clause": "Rule 1: Gold frequent flyer members receive one complimentary checked bag on all flights as a standing membership benefit. Rule 2: Basic economy fares do not include any checked baggage; checked bags must be purchased separately with no exceptions or waivers.",
    "unambiguous_clause": "Rule 1: Gold frequent flyer members receive one complimentary checked bag on all flights. Rule 2: Basic economy fares do not include checked baggage. Priority: Loyalty baggage benefits (Rule 1) do not apply to basic economy fares; Gold members on basic economy must purchase checked bags per Rule 2.",
    "user_scenario": "Hey, I have a flight tomorrow, reservation RES-88312. I'm a Gold member and want to add my free checked bag. I know it's basic economy but my Gold membership should cover a bag, right?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "update_reservation_baggages"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-72910", "name": "Mateo Cruz", "email": "m.cruz@email.com", "ff_tier": "gold", "ff_number": "GLD-550082", "reservations": ["RES-88312"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-88312"}, "response": {"reservation_id": "RES-88312", "passenger": "Mateo Cruz", "flights": [{"flight": "WN-3410", "origin": "DEN", "destination": "LAX", "date": "2026-05-21", "fare_class": "basic_economy", "seat": "31B"}], "fare_class": "basic_economy", "baggages": {"carry_on": 1, "checked": 0}, "total_fare": 89, "booking_source": "app"}},
        {"tool_name": "update_reservation_baggages", "args_pattern": {"reservation_id": "RES-88312", "baggages": "*"}, "response": {"status": "updated", "reservation_id": "RES-88312", "baggages": {"carry_on": 1, "checked": 1}, "baggage_fee": 0, "waiver_reason": "gold_membership"}}
    ]
})

# ─── cp_037: Employee discount vs promotional pricing (retail) ───
clauses.append({
    "clause_id": "cp_037",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Employee discount program vs active promotional sale pricing",
    "ambiguity_point": "Employees get a 25% discount on regular-priced items. A flash sale offers 30% off sitewide. The employee discount policy says it cannot be applied to sale items, but the flash sale is categorized as a 'promotional event' not a 'sale' in the system.",
    "possible_interpretations": [
        "Interpretation A (employee discount blocked): The flash sale is functionally a sale price reduction; employee discounts are excluded on already-discounted items.",
        "Interpretation B (employee discount applies): The flash sale is a 'promotional event' distinct from a 'sale'; since the restriction only mentions 'sale items,' the employee discount can be applied on top.",
        "Interpretation C (better-of): The employee gets whichever single discount is higher (the 30% promo), but not both."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the employee gets only the 30% flash sale price. Under Interpretation B the employee gets 25% off plus 30% off (stacked). Under Interpretation C the employee gets 30% as the better single discount.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items"),
    "annotation_rationale": "Temporal priority conflict: the standing employee discount program conflicts with the temporary flash sale event. The distinction between 'sale' and 'promotional event' creates additional ambiguity in the exclusion clause.",
    "ambiguous_clause": "Rule 1: Employees receive a 25% discount on all regular-priced merchandise; the employee discount may not be applied to sale items. Rule 2: Flash Sale Weekend: All items are 30% off sitewide as a limited-time promotional event.",
    "unambiguous_clause": "Rule 1: Employees receive a 25% discount on all regular-priced merchandise; the employee discount may not be applied to sale or promotional items. Rule 2: Flash Sale Weekend: All items are 30% off sitewide. Priority: During promotional events, employees receive the promotional price and their employee discount does not stack; promotional pricing is treated as 'sale' pricing for employee discount exclusion purposes.",
    "user_scenario": "I'm an employee and I want to place an order during the Flash Sale Weekend. My order ORD-90011 has items at the 30% promo price. Do I also get my 25% employee discount? The system seems to show both discounts.",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-EMP-0421", "name": "Lisa Tran", "email": "l.tran@company-internal.com", "account_type": "employee", "employee_discount_pct": 25, "account_status": "active", "orders": ["ORD-90011"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-90011"}, "response": {"order_id": "ORD-90011", "status": "pending", "items": [{"item_id": "ITEM-1180", "product_id": "PROD-4450", "name": "Noise-Cancelling Headphones", "category": "electronics", "quantity": 1, "price": 279.99, "promo_applied": "flash_sale_30"}], "subtotal": 195.99, "applied_discounts": [{"type": "promotional", "code": "FLASH30", "pct": 30}, {"type": "employee", "pct": 25}], "total": 146.99, "payment_method": "employee_payroll"}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-4450"}, "response": {"product_id": "PROD-4450", "name": "Noise-Cancelling Headphones", "category": "electronics", "price": 279.99, "regular_price": 279.99, "promo_price": 195.99, "promo_type": "flash_sale"}}
    ]
})

# ─── cp_038: Weather delay compensation vs force majeure exclusion (airline) ───
clauses.append({
    "clause_id": "cp_038",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Customer service compensation for delays vs force majeure exclusion clause",
    "ambiguity_point": "The customer compensation policy offers meal vouchers and hotel accommodation for delays over 4 hours. The force majeure clause excludes weather-related disruptions from all compensation obligations. A flight is delayed 6 hours due to a thunderstorm.",
    "possible_interpretations": [
        "Interpretation A (compensation policy applies): The delay exceeds 4 hours, triggering automatic compensation regardless of cause — the compensation policy makes no cause-based distinction.",
        "Interpretation B (force majeure exclusion applies): Weather is a force majeure event that overrides compensation obligations — no vouchers or hotel."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent issues meal vouchers and books hotel accommodation. Under Interpretation B the agent apologizes but explains no compensation is available for weather delays.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "add_certificate", "search_flights", "transfer_to_human_agents"),
    "annotation_rationale": "Exception vs exception: the compensation trigger (delay > 4 hours) and the force majeure exclusion (weather events) are both exception clauses that apply simultaneously. Neither states it overrides the other.",
    "ambiguous_clause": "Rule 1: Passengers experiencing flight delays exceeding 4 hours are entitled to meal vouchers ($25 per person) and hotel accommodation if overnight stay is required. Rule 2: The airline is not obligated to provide compensation, rebooking assistance, or accommodation for disruptions caused by force majeure events including but not limited to severe weather, natural disasters, and air traffic control restrictions.",
    "unambiguous_clause": "Rule 1: Passengers experiencing flight delays exceeding 4 hours are entitled to meal vouchers and hotel accommodation. Rule 2: The airline is not obligated to provide compensation for force majeure events. Priority: Rule 2 governs; weather-related delays are force majeure events exempt from the compensation obligations in Rule 1. However, agents should offer rebooking on the next available flight at no charge.",
    "user_scenario": "Our flight was supposed to leave at 2 PM and now they're saying 8 PM because of thunderstorms. That's 6 hours! My reservation is RES-12540. I need a meal voucher and if it gets pushed to tomorrow I'll need a hotel. What can you do?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "add_certificate", "search_flights", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-95020", "name": "Omar Hassan", "email": "o.hassan@email.com", "ff_tier": "silver", "reservations": ["RES-12540"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-12540"}, "response": {"reservation_id": "RES-12540", "passenger": "Omar Hassan", "flights": [{"flight": "UA-880", "origin": "EWR", "destination": "ATL", "date": "2026-05-20", "scheduled_depart": "14:00", "estimated_depart": "20:00", "delay_reason": "weather_thunderstorm", "delay_hours": 6, "fare_class": "economy"}], "total_fare": 245, "booking_source": "website"}},
        {"tool_name": "add_certificate", "args_pattern": {"user_id": "USR-95020", "certificate_type": "*", "amount": "*"}, "response": {"status": "certificate_added", "certificate_id": "CERT-44210", "type": "meal_voucher", "amount": 25, "user_id": "USR-95020"}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "EWR", "destination": "ATL", "date": "*"}, "response": {"flights": [{"flight": "UA-882", "depart": "21:30", "arrive": "00:05", "fare_class": "economy", "seats_available": 5, "price": 210}]}}
    ]
})

# ─── cp_039: Price match guarantee vs marketplace seller pricing (retail) ───
clauses.append({
    "clause_id": "cp_039",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Price match guarantee policy vs marketplace third-party seller exclusion",
    "ambiguity_point": "The price match guarantee promises to match any competitor's lower price on identical items. The marketplace policy excludes third-party marketplace sellers from price matching. A customer finds a lower price on a competitor's marketplace listing (sold by a third party but fulfilled by the competitor).",
    "possible_interpretations": [
        "Interpretation A (price match applies): The listing is on a recognized competitor's website and shows a lower price; the guarantee should be honored regardless of who fulfills it.",
        "Interpretation B (marketplace exclusion applies): The item is sold by a third-party marketplace seller, which is explicitly excluded from price matching, even though it's listed on a major competitor's platform."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent adjusts the price to match the competitor listing. Under Interpretation B the agent denies the price match citing the third-party seller exclusion.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items"),
    "annotation_rationale": "Lex specialis vs lex generalis: the price match guarantee is a general customer-facing promise, while the marketplace seller exclusion is a specific carve-out. The ambiguity arises when the boundary between 'competitor price' and 'marketplace seller price' is blurred by fulfilled-by arrangements.",
    "ambiguous_clause": "Rule 1: We guarantee to match any lower price from authorized competitors on identical in-stock items. Rule 2: Price matching does not apply to prices offered by third-party marketplace sellers, auction sites, or non-authorized retailers.",
    "unambiguous_clause": "Rule 1: We guarantee to match any lower price from authorized competitors on identical in-stock items. Rule 2: Price matching does not apply to third-party marketplace sellers. Priority: If the lower price appears on an authorized competitor's website but the item is sold/shipped by a third-party marketplace seller, Rule 2 applies and the price match is denied. Only prices where the competitor is both the seller and the retailer of record qualify.",
    "user_scenario": "I'm about to buy this blender on order ORD-88210 for $149.99, but I found the exact same model on MegaMart's website for $119.99. I know you do price matching. Can you adjust my order?",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-61920", "name": "Hannah Kim", "email": "h.kim@email.com", "loyalty_tier": "standard", "account_status": "active", "orders": ["ORD-88210"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-88210"}, "response": {"order_id": "ORD-88210", "status": "pending", "items": [{"item_id": "ITEM-5502", "product_id": "PROD-6690", "name": "PowerBlend Pro 1200W", "category": "appliances", "quantity": 1, "price": 149.99}], "payment_method": "credit_card", "total": 149.99}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-6690"}, "response": {"product_id": "PROD-6690", "name": "PowerBlend Pro 1200W", "category": "appliances", "price": 149.99, "upc": "012345678901", "price_match_eligible": True}},
        {"tool_name": "modify_pending_order_items", "args_pattern": {"order_id": "ORD-88210", "item_ids": "*", "new_item_ids": "*"}, "response": {"status": "modified", "order_id": "ORD-88210", "price_adjusted": True, "new_total": 119.99}}
    ]
})

# ─── cp_040: Unaccompanied minor policy vs self-service rebooking (airline) ───
clauses.append({
    "clause_id": "cp_040",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Unaccompanied minor special handling vs automated self-service rebooking system",
    "ambiguity_point": "The unaccompanied minor (UM) policy requires all changes to UM itineraries to go through a dedicated team with guardian authorization. The self-service rebooking system automatically rebooks passengers on cancelled flights without agent intervention. A UM's flight is cancelled and the system auto-rebooks them.",
    "possible_interpretations": [
        "Interpretation A (UM policy prevails): The auto-rebooking should not apply to UM passengers; their itineraries require manual handling with guardian consent, even during disruptions.",
        "Interpretation B (auto-rebooking prevails): The automated system treats all passengers equally during cancellations; the UM is rebooked automatically and the guardian is notified after."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent reverses the auto-rebooking, contacts the guardian, and manually handles the change after obtaining authorization. Under Interpretation B the agent confirms the auto-rebooked flight and notifies the guardian of the new itinerary.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights", "transfer_to_human_agents"),
    "annotation_rationale": "Authority-level conflict: the UM handling policy (safety/compliance mandate requiring guardian authorization) conflicts with the automated operations policy (system-level disruption management). Safety mandates typically override operational convenience, but no explicit priority is stated.",
    "ambiguous_clause": "Rule 1: All modifications to unaccompanied minor itineraries require prior authorization from the designated guardian and must be processed by the UM Services team. Rule 2: When flights are cancelled, the automated rebooking system will rebook all affected passengers onto the next available flight to minimize disruption.",
    "unambiguous_clause": "Rule 1: All modifications to unaccompanied minor itineraries require prior authorization from the designated guardian. Rule 2: The automated rebooking system rebooks affected passengers on cancelled flights. Priority: Unaccompanied minor reservations are excluded from automated rebooking (Rule 1 overrides Rule 2). UM passengers must be held for manual rebooking by the UM Services team after guardian authorization.",
    "user_scenario": "My daughter is flying alone — she's 12. Her flight just got cancelled and I got a text saying she was automatically rebooked on a different flight. Reservation RES-66710. I didn't authorize that change. What's going on?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-UM-4410", "name": "Emily Dawson", "age": 12, "is_unaccompanied_minor": True, "guardian_user_id": "USR-44100", "guardian_name": "Catherine Dawson", "reservations": ["RES-66710"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-66710"}, "response": {"reservation_id": "RES-66710", "passenger": "Emily Dawson", "passenger_type": "unaccompanied_minor", "guardian": "Catherine Dawson", "flights": [{"flight": "DL-310", "origin": "ATL", "destination": "BOS", "date": "2026-05-25", "status": "cancelled", "auto_rebooked_to": "DL-318"}], "auto_rebooked_flight": {"flight": "DL-318", "origin": "ATL", "destination": "BOS", "date": "2026-05-25", "depart": "17:45"}, "um_service_fee": 150}},
        {"tool_name": "transfer_to_human_agents", "args_pattern": {"summary": "*"}, "response": {"status": "transferred", "department": "um_services", "agent_id": "UM-AGENT-12", "estimated_wait": "2 minutes"}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "ATL", "destination": "BOS", "date": "2026-05-25"}, "response": {"flights": [{"flight": "DL-318", "depart": "17:45", "arrive": "21:10", "seats_available": 15}, {"flight": "DL-322", "depart": "19:30", "arrive": "22:55", "seats_available": 28}]}}
    ]
})

# ─── cp_041: Gift card payment vs refund-to-original-method policy (retail) ───
clauses.append({
    "clause_id": "cp_041",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Refund-to-original-payment-method policy vs gift card balance policy",
    "ambiguity_point": "The refund policy states refunds must go back to the original payment method. The gift card policy states gift card balances are non-refundable and non-transferable to other payment methods. A customer paid with a gift card and wants a cash/credit refund instead of gift card credit.",
    "possible_interpretations": [
        "Interpretation A (refund policy wins): Refund goes back to the original method — the gift card — consistent with the refund policy.",
        "Interpretation B (customer gets cash): The customer should receive a refund in a fungible form since the gift card restriction only governs unused balances, not returns of purchased goods."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refunds the amount back to the gift card balance. Under Interpretation B the agent offers a refund via store credit or cash/check since the original gift card may be depleted or lost.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "return_delivered_order_items", "transfer_to_human_agents"),
    "annotation_rationale": "Exception vs exception: the refund-to-original-method rule and the gift-card-non-refundable rule are both exception-handling clauses. They converge when the original payment was a gift card, creating a circular conflict — refund to original (gift card) vs. gift card balances are non-refundable.",
    "ambiguous_clause": "Rule 1: All refunds must be issued to the original payment method used at the time of purchase. Rule 2: Gift card balances are non-refundable and cannot be converted to cash, credit, or any other payment form.",
    "unambiguous_clause": "Rule 1: All refunds must be issued to the original payment method used at the time of purchase. Rule 2: Gift card balances are non-refundable and cannot be converted to cash. Priority: For purchases made with gift cards, the refund is credited back to the same gift card (or a new gift card if the original is unavailable). Rule 1 governs, and the refund to gift card does not violate Rule 2 because it is a return credit, not a balance conversion.",
    "user_scenario": "I want to return a sweater from order ORD-41982. I paid with a gift card that someone gave me, but I'd prefer the refund on my credit card instead. The gift card is empty now. Can you do that?",
    "tools": retail_tools("get_user_details", "get_order_details", "return_delivered_order_items", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-29010", "name": "Jordan Ellis", "email": "j.ellis@email.com", "loyalty_tier": "standard", "payment_methods": [{"id": "PM-CC-01", "type": "credit_card", "last_four": "4421"}, {"id": "PM-GC-88", "type": "gift_card", "balance": 0}], "orders": ["ORD-41982"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-41982"}, "response": {"order_id": "ORD-41982", "status": "delivered", "items": [{"item_id": "ITEM-2290", "product_id": "PROD-1190", "name": "Cashmere V-Neck Sweater", "category": "apparel", "quantity": 1, "price": 119.99}], "payment_method": "gift_card", "payment_method_id": "PM-GC-88", "total": 119.99, "delivered_at": "2026-05-08T14:00:00Z"}},
        {"tool_name": "return_delivered_order_items", "args_pattern": {"order_id": "ORD-41982", "item_ids": ["ITEM-2290"], "reason": "*"}, "response": {"status": "return_initiated", "order_id": "ORD-41982", "items_returned": ["ITEM-2290"], "refund_amount": 119.99, "refund_method": "gift_card", "new_gift_card_id": "PM-GC-89"}}
    ]
})

# ─── cp_042: Codeshare partner rules vs operating carrier rules (airline) ───
clauses.append({
    "clause_id": "cp_042",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Codeshare ticketing carrier policy vs operating carrier policy",
    "ambiguity_point": "The ticketing carrier's policy allows free same-day flight changes for premium economy and above. The operating carrier's policy charges $50 for all same-day changes regardless of fare class. The passenger booked premium economy on a codeshare flight.",
    "possible_interpretations": [
        "Interpretation A (ticketing carrier rules apply): The customer bought the ticket from the ticketing carrier, so their more generous policy (free same-day change) governs.",
        "Interpretation B (operating carrier rules apply): The flight is physically operated by the partner airline, whose systems and policies control the actual change, so the $50 fee applies."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent processes the same-day change at no charge. Under Interpretation B the agent charges the $50 same-day change fee per the operating carrier's policy.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights"),
    "annotation_rationale": "Authority-level conflict: the ticketing carrier (who sold the ticket and owns the customer relationship) and the operating carrier (who flies the plane and controls operations) each have their own policies. Codeshare agreements create ambiguity about which carrier's customer-facing policies apply.",
    "ambiguous_clause": "Rule 1: Passengers booked in premium economy or higher fare classes on our flights are eligible for complimentary same-day flight changes. Rule 2: On codeshare flights operated by partner carriers, the operating carrier's change policies and fees apply to all modifications.",
    "unambiguous_clause": "Rule 1: Passengers in premium economy or higher are eligible for free same-day changes on flights we operate. Rule 2: On codeshare flights, the operating carrier's policies apply. Priority: For codeshare flights, Rule 2 governs all change requests. Our ticketing policies (Rule 1) apply only to flights we both ticket and operate.",
    "user_scenario": "I need to switch to an earlier flight today. My reservation RES-55102 is premium economy, booked through your airline, but I see it's operated by SkyPartner Airlines. Since I'm premium economy with you, the same-day change should be free, correct?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "search_flights", "update_reservation_flights"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-38900", "name": "Yuki Tanaka", "email": "y.tanaka@email.com", "ff_tier": "silver", "reservations": ["RES-55102"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-55102"}, "response": {"reservation_id": "RES-55102", "passenger": "Yuki Tanaka", "flights": [{"flight": "UA-4521", "marketing_carrier": "UA", "operating_carrier": "SkyPartner", "origin": "SFO", "destination": "PDX", "date": "2026-05-20", "fare_class": "premium_economy", "codeshare": True}], "total_fare": 380, "booking_source": "website"}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "SFO", "destination": "PDX", "date": "2026-05-20"}, "response": {"flights": [{"flight": "UA-4519", "operating_carrier": "SkyPartner", "depart": "10:15", "arrive": "12:30", "fare_class": "premium_economy", "seats_available": 4, "price": 380, "codeshare": True}]}},
        {"tool_name": "update_reservation_flights", "args_pattern": {"reservation_id": "RES-55102", "flights": "*"}, "response": {"status": "updated", "reservation_id": "RES-55102", "new_flight": "UA-4519", "change_fee": 50, "fee_basis": "operating_carrier_policy"}}
    ]
})

# ─── cp_043: Subscription auto-renewal vs cancellation grace period (retail) ───
clauses.append({
    "clause_id": "cp_043",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Subscription auto-renewal terms vs cancellation grace period policy",
    "ambiguity_point": "The subscription auto-renewal policy charges on the renewal date and states renewals are non-refundable. The cancellation grace period policy allows cancellation with full refund within 48 hours of any charge. A subscriber is charged on auto-renewal and requests cancellation 24 hours later.",
    "possible_interpretations": [
        "Interpretation A (auto-renewal non-refundable wins): The renewal charge is non-refundable per the subscription terms; the customer must wait until the period ends.",
        "Interpretation B (grace period wins): The 48-hour grace period applies to all charges including auto-renewals; the customer gets a full refund."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent denies the refund and keeps the subscription active until period end. Under Interpretation B the agent processes the refund and cancels the subscription immediately.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "cancel_pending_order", "transfer_to_human_agents"),
    "annotation_rationale": "Exception vs exception: the auto-renewal non-refundable clause and the 48-hour grace period are both special provisions. They conflict when a customer acts within the grace window after an auto-renewal charge.",
    "ambiguous_clause": "Rule 1: Subscription auto-renewals are processed automatically on the renewal date and are non-refundable once charged. Rule 2: Customers may cancel any purchase and receive a full refund within 48 hours of the charge being processed.",
    "unambiguous_clause": "Rule 1: Subscription auto-renewals are non-refundable once charged. Rule 2: Customers may cancel any purchase within 48 hours for a full refund. Priority: The 48-hour grace period (Rule 2) applies to auto-renewal charges; customers who cancel within 48 hours of an auto-renewal charge receive a full refund.",
    "user_scenario": "My premium membership just auto-renewed yesterday and I was charged $99.99. I forgot to cancel before the renewal. It's only been about 24 hours — can I still get a refund? My account is under USR-50120.",
    "tools": retail_tools("get_user_details", "get_order_details", "cancel_pending_order", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-50120", "name": "Robert Chen", "email": "r.chen@email.com", "loyalty_tier": "premium_subscriber", "subscription": {"plan": "premium_annual", "renewal_date": "2026-05-19", "next_renewal": "2027-05-19", "auto_renew": True, "last_charge": 99.99}, "orders": ["ORD-SUB-7720"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-SUB-7720"}, "response": {"order_id": "ORD-SUB-7720", "type": "subscription_renewal", "status": "completed", "items": [{"item_id": "ITEM-SUB-01", "name": "Premium Annual Membership", "price": 99.99}], "payment_method": "credit_card", "total": 99.99, "charged_at": "2026-05-19T00:01:00Z"}},
        {"tool_name": "cancel_pending_order", "args_pattern": {"order_id": "ORD-SUB-7720", "reason": "*"}, "response": {"status": "cancelled", "order_id": "ORD-SUB-7720", "refund_amount": 99.99, "subscription_status": "cancelled", "refund_method": "credit_card"}}
    ]
})

# ─── cp_044: Medical emergency rebooking vs non-refundable fare rule (airline) ───
clauses.append({
    "clause_id": "cp_044",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Medical emergency accommodation policy vs non-refundable fare restrictions",
    "ambiguity_point": "The medical emergency policy allows free rebooking or refund for passengers with documented medical emergencies. The non-refundable fare rules state that basic economy and promo fares are non-refundable and non-changeable under all circumstances. A passenger on a non-refundable promo fare has a medical emergency.",
    "possible_interpretations": [
        "Interpretation A (medical policy prevails): Medical emergencies override fare restrictions — the passenger gets a free change or refund regardless of fare class.",
        "Interpretation B (fare rules prevail): Non-refundable means non-refundable 'under all circumstances' — even medical emergencies do not override the fare terms the customer agreed to."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent processes a free rebooking or refund upon receiving medical documentation. Under Interpretation B the agent denies the change/refund and suggests the passenger file a claim with travel insurance.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "update_reservation_flights", "cancel_reservation", "add_certificate", "transfer_to_human_agents"),
    "annotation_rationale": "Lex specialis vs lex generalis: the medical emergency accommodation is a specific humanitarian exception, while the non-refundable fare rule is a specific contractual constraint. Both are 'specific' — one narrows by circumstance (medical), the other by fare class. The absolutist language ('under all circumstances') in the fare rule intensifies the conflict.",
    "ambiguous_clause": "Rule 1: Passengers who experience a documented medical emergency may rebook their flight at no charge or receive a full refund, regardless of booking conditions. Rule 2: Basic economy and promotional fare tickets are non-refundable and non-changeable under all circumstances; no exceptions, credits, or waivers apply.",
    "unambiguous_clause": "Rule 1: Passengers with documented medical emergencies may rebook or receive a refund regardless of booking conditions. Rule 2: Basic economy and promo fares are non-refundable and non-changeable. Priority: Medical emergency accommodations (Rule 1) override fare-class restrictions (Rule 2). With valid documentation, all fare types are eligible for medical emergency rebooking or refund.",
    "user_scenario": "I was supposed to fly tomorrow but I just got admitted to the hospital. Reservation RES-20891, I know it's a promo fare but this is a medical emergency — I have a doctor's note. Can I get a refund or at least rebook for when I'm better?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "update_reservation_flights", "cancel_reservation", "add_certificate", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-33450", "name": "Lisa Bergman", "email": "l.bergman@email.com", "ff_tier": "none", "reservations": ["RES-20891"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-20891"}, "response": {"reservation_id": "RES-20891", "passenger": "Lisa Bergman", "flights": [{"flight": "AA-1122", "origin": "PHX", "destination": "DFW", "date": "2026-05-21", "fare_class": "promo_basic", "refundable": False, "changeable": False}], "total_fare": 79, "booking_source": "website", "fare_rules": {"refundable": False, "changeable": False, "restrictions": "non-refundable, non-changeable"}}},
        {"tool_name": "cancel_reservation", "args_pattern": {"reservation_id": "RES-20891"}, "response": {"status": "cancelled", "reservation_id": "RES-20891", "refund_amount": 79, "refund_reason": "medical_emergency", "refund_method": "original_payment"}},
        {"tool_name": "add_certificate", "args_pattern": {"user_id": "USR-33450", "certificate_type": "*", "amount": "*"}, "response": {"status": "certificate_added", "certificate_id": "CERT-88910", "type": "travel_credit", "amount": 79, "expiry": "2027-05-21"}}
    ]
})

# ─── cp_045: Bulk order pricing vs member-exclusive sale (retail) ───
clauses.append({
    "clause_id": "cp_045",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Bulk order quantity discount vs member-exclusive flash sale pricing",
    "ambiguity_point": "Bulk orders of 10+ identical items get a 15% quantity discount. A members-only flash sale offers 25% off select items but states 'one per customer, not valid on bulk orders.' The customer is a member ordering 12 units of a flash-sale item.",
    "possible_interpretations": [
        "Interpretation A (flash sale restriction wins): The flash sale explicitly excludes bulk orders; the customer gets the 15% bulk discount at regular price, not the flash sale price.",
        "Interpretation B (customer gets flash sale on limited units): The customer can buy 1 unit at the flash sale price and the remaining 11 at bulk pricing.",
        "Interpretation C (bulk discount on flash price): The customer gets both — flash sale price with the bulk discount stacked on top for all 12 units."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent applies only the 15% bulk discount at regular price. Under Interpretation B the agent splits the order into two line items. Under Interpretation C the agent applies both discounts.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items"),
    "annotation_rationale": "Exception vs exception: the bulk quantity discount and the members-only flash sale are both pricing exceptions. The flash sale's 'not valid on bulk orders' restriction and the bulk discount's automatic application based on quantity create conflicting logic when the same items qualify for both.",
    "ambiguous_clause": "Rule 1: Orders containing 10 or more identical items automatically receive a 15% bulk quantity discount. Rule 2: Members-Only Flash Sale: Select items at 25% off, limit one per customer, not valid on bulk orders.",
    "unambiguous_clause": "Rule 1: Orders of 10+ identical items get a 15% bulk discount. Rule 2: Flash Sale items are 25% off, limit one per customer, excluded from bulk orders. Priority: Flash sale pricing and bulk discounts are mutually exclusive. Customers ordering 10+ of a flash sale item receive the 15% bulk discount at regular price; the flash sale price does not apply to bulk quantities.",
    "user_scenario": "I'm a member and I want to order 12 of those ergonomic desk lamps that are on the flash sale for 25% off. My order is ORD-71028. I should also qualify for the bulk discount since I'm ordering more than 10. How does the pricing work?",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-44980", "name": "Marcus Wright", "email": "m.wright@email.com", "loyalty_tier": "gold", "membership": "active", "orders": ["ORD-71028"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-71028"}, "response": {"order_id": "ORD-71028", "status": "pending", "items": [{"item_id": "ITEM-8800", "product_id": "PROD-4490", "name": "ErgoLight Desk Lamp", "category": "office", "quantity": 12, "unit_price": 45.99, "flash_sale_price": 34.49}], "subtotal": 551.88, "applied_discounts": [{"type": "flash_sale", "pct": 25}, {"type": "bulk", "pct": 15}], "total": 351.45}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-4490"}, "response": {"product_id": "PROD-4490", "name": "ErgoLight Desk Lamp", "category": "office", "price": 45.99, "flash_sale_eligible": True, "flash_sale_price": 34.49, "bulk_discount_eligible": True}}
    ]
})

# ─── cp_046: Infant lap seat policy vs safety regulation on long-haul (airline) ───
clauses.append({
    "clause_id": "cp_046",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Infant lap seat policy vs long-haul safety seat requirement",
    "ambiguity_point": "The general infant policy allows children under 2 to travel as lap infants at no charge. The long-haul safety policy requires all passengers on flights over 8 hours to have their own seat with a functioning seatbelt. A parent wants to fly with a 14-month-old on a 10-hour international flight as a lap infant.",
    "possible_interpretations": [
        "Interpretation A (lap infant policy applies): Infants under 2 are eligible for lap travel on any flight; the parent does not need to purchase a separate seat.",
        "Interpretation B (long-haul safety rule applies): On flights exceeding 8 hours, every passenger including infants must have their own seat; a ticket must be purchased for the infant."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent adds the infant as a lap passenger at no charge. Under Interpretation B the agent requires the parent to purchase a seat for the infant.",
    "stripped_tool_desc": airline_stripped("get_user_details", "get_reservation_details", "search_flights", "book_reservation", "update_reservation_flights"),
    "annotation_rationale": "Lex specialis vs lex generalis: the infant lap seat policy is specific to passenger age (under 2), while the long-haul safety requirement is specific to flight duration (over 8 hours). Each is a 'specific' rule scoped differently, creating a precedence gap.",
    "ambiguous_clause": "Rule 1: Children under 2 years of age may travel as lap infants on any flight at no additional charge. Rule 2: On flights exceeding 8 hours in duration, all passengers must be assigned an individual seat with a functioning seatbelt for safety purposes.",
    "unambiguous_clause": "Rule 1: Children under 2 may travel as lap infants at no charge. Rule 2: On flights over 8 hours, all passengers must have their own seat. Priority: Rule 2 overrides Rule 1 for long-haul flights; infants on flights exceeding 8 hours must have a purchased seat. Lap infant eligibility applies only to flights of 8 hours or shorter.",
    "user_scenario": "I'm booking a flight from New York to Tokyo for me and my 14-month-old baby. Reservation RES-99021. The flight is about 14 hours. I'd like to add my son as a lap infant — he's under 2 so he should fly free, right?",
    "tools": airline_tools("get_user_details", "get_reservation_details", "search_flights", "book_reservation", "update_reservation_flights"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-71090", "name": "Priya Mehta", "email": "p.mehta@email.com", "ff_tier": "gold", "reservations": ["RES-99021"]}},
        {"tool_name": "get_reservation_details", "args_pattern": {"reservation_id": "RES-99021"}, "response": {"reservation_id": "RES-99021", "passenger": "Priya Mehta", "flights": [{"flight": "NH-9010", "origin": "JFK", "destination": "NRT", "date": "2026-08-15", "duration_hours": 14, "fare_class": "economy", "long_haul": True}], "total_fare": 1450, "booking_source": "website"}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "JFK", "destination": "NRT", "date": "2026-08-15"}, "response": {"flights": [{"flight": "NH-9010", "depart": "11:00", "arrive": "14:00+1", "duration_hours": 14, "fare_class": "economy", "seats_available": 45, "price": 1450, "infant_seat_price": 217}]}},
        {"tool_name": "update_reservation_flights", "args_pattern": {"reservation_id": "RES-99021", "flights": "*"}, "response": {"status": "updated", "reservation_id": "RES-99021", "infant_added": True, "infant_type": "lap_infant", "additional_charge": 0}}
    ]
})

# ─── cp_047: Free shipping threshold vs oversized item surcharge (retail) ───
clauses.append({
    "clause_id": "cp_047",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Free shipping on orders over $75 vs oversized item shipping surcharge",
    "ambiguity_point": "Orders over $75 qualify for free standard shipping. Oversized items carry a mandatory $29.99 shipping surcharge due to special handling. A customer orders an oversized item totaling $120.",
    "possible_interpretations": [
        "Interpretation A (free shipping wins): The order exceeds $75, so all shipping is free — the free shipping threshold waives all shipping costs including surcharges.",
        "Interpretation B (surcharge applies): The oversized surcharge is a handling fee, not standard shipping, and applies regardless of order total."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent confirms free shipping with no surcharge. Under Interpretation B the agent informs the customer that standard shipping is free but the $29.99 oversized handling fee still applies.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_payment"),
    "annotation_rationale": "Lex specialis vs lex generalis: the free shipping threshold is a general promotional benefit, while the oversized item surcharge is a specific logistics constraint. The word 'shipping' appears in both but may refer to different cost categories (delivery vs. handling).",
    "ambiguous_clause": "Rule 1: All orders totaling $75 or more qualify for free standard shipping. Rule 2: Oversized items (weight > 70 lbs or any dimension > 48 inches) are subject to a mandatory $29.99 shipping surcharge for special handling.",
    "unambiguous_clause": "Rule 1: Orders $75+ qualify for free standard shipping. Rule 2: Oversized items carry a $29.99 shipping surcharge. Priority: The free shipping threshold (Rule 1) waives standard delivery costs only. The oversized item surcharge (Rule 2) is a handling fee that applies regardless of order total, even on free-shipping-eligible orders.",
    "user_scenario": "I'm ordering a large bookshelf for $120, order ORD-38501. My order is over $75 so I should get free shipping. But at checkout there's a $29.99 shipping surcharge. Shouldn't that be waived since I qualify for free shipping?",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_payment"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-89001", "name": "Nathan Brooks", "email": "n.brooks@email.com", "loyalty_tier": "standard", "account_status": "active", "orders": ["ORD-38501"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-38501"}, "response": {"order_id": "ORD-38501", "status": "pending", "items": [{"item_id": "ITEM-6601", "product_id": "PROD-9920", "name": "Industrial Bookshelf 6-Tier", "category": "furniture", "quantity": 1, "price": 120.00, "oversized": True}], "subtotal": 120.00, "shipping": {"standard": 0, "surcharge": 29.99, "surcharge_reason": "oversized_item"}, "total": 149.99}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-9920"}, "response": {"product_id": "PROD-9920", "name": "Industrial Bookshelf 6-Tier", "category": "furniture", "price": 120.00, "weight_lbs": 95, "dimensions": "72x36x14 inches", "oversized": True, "shipping_surcharge": 29.99}}
    ]
})

# ─── cp_048: Military discount vs already-reduced bundle pricing (retail) ───
clauses.append({
    "clause_id": "cp_048",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Military/veteran discount policy vs bundle pricing terms",
    "ambiguity_point": "Verified military members receive a 15% discount on all purchases. Bundle deals are pre-priced at a discount and state 'bundle pricing is final and cannot be combined with additional discounts.' A veteran purchases a bundle.",
    "possible_interpretations": [
        "Interpretation A (military discount applies): Military discounts are a standing benefit for service members that should apply universally, including on bundles.",
        "Interpretation B (bundle restriction applies): Bundle pricing already includes a discount and explicitly prohibits additional discounts; the military discount cannot stack.",
        "Interpretation C (post-bundle military discount): Apply the military discount to the bundle price since the restriction targets 'additional discounts' but military benefits are an entitlement, not a 'discount.'"
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent applies the 15% military discount on top of the bundle price. Under Interpretation B the agent informs the veteran that the bundle already includes savings and no additional discount applies. Under Interpretation C same as A but with different justification framing.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items", "transfer_to_human_agents"),
    "annotation_rationale": "Exception vs exception: the military discount (standing benefit for a protected class) and the bundle pricing restriction (product-level pricing constraint) are both exceptions to standard pricing. The moral/legal weight of military benefits adds a dimension beyond pure policy conflict.",
    "ambiguous_clause": "Rule 1: Verified military members and veterans receive a 15% discount on all purchases as a thank-you for their service. Rule 2: Bundle deals are pre-priced at a discounted rate; bundle pricing is final and cannot be combined with any additional discounts, coupons, or offers.",
    "unambiguous_clause": "Rule 1: Verified military members receive a 15% discount on all purchases. Rule 2: Bundle pricing cannot be combined with additional discounts. Priority: Military/veteran discounts (Rule 1) are classified as 'additional discounts' under Rule 2 and do not stack with bundle pricing. Veterans may choose either the bundle price or the 15% military discount on individual items, whichever is lower.",
    "user_scenario": "I'm a veteran and I want to buy the Home Office Bundle on order ORD-52410. I have my military verification on file. Does my 15% military discount apply to the bundle price, or do I only get the bundle savings?",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details", "modify_pending_order_items", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-VET-0892", "name": "Daniel Washington", "email": "d.washington@email.com", "loyalty_tier": "standard", "military_verified": True, "military_discount_pct": 15, "orders": ["ORD-52410"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-52410"}, "response": {"order_id": "ORD-52410", "status": "pending", "items": [{"item_id": "ITEM-BDL-01", "product_id": "PROD-BDL-550", "name": "Home Office Bundle (Desk + Chair + Lamp)", "category": "bundles", "quantity": 1, "bundle_price": 449.99, "individual_total": 589.97}], "subtotal": 449.99, "applied_discounts": [{"type": "bundle", "savings": 139.98}, {"type": "military", "pct": 15}], "total": 382.49}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-BDL-550"}, "response": {"product_id": "PROD-BDL-550", "name": "Home Office Bundle", "type": "bundle", "bundle_price": 449.99, "components": [{"name": "Adjustable Standing Desk", "individual_price": 299.99}, {"name": "Ergonomic Office Chair", "individual_price": 219.99}, {"name": "LED Desk Lamp", "individual_price": 69.99}], "bundle_discount_applied": True, "stackable": False}}
    ]
})

# ─── cp_049: Bereavement fare vs advance purchase requirement (airline) ───
clauses.append({
    "clause_id": "cp_049",
    "ambiguity_type": "conditional_precedence",
    "domain": "airline",
    "source_clause": "Bereavement fare policy vs advance purchase fare requirement",
    "ambiguity_point": "The bereavement policy offers a discounted fare for passengers traveling due to a death in the family, available for last-minute travel. The advance purchase policy requires tickets to be booked at least 14 days before departure for the lowest fare tiers. A bereaved passenger needs a flight tomorrow.",
    "possible_interpretations": [
        "Interpretation A (bereavement policy prevails): The bereavement fare applies regardless of advance purchase requirements, offering a reduced fare for last-minute travel.",
        "Interpretation B (advance purchase required): The discounted bereavement fare is only available within fare tiers that satisfy the advance purchase window; last-minute travel gets only the walk-up rate with bereavement discount applied on top."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent books the flight at the bereavement fare (e.g., 50% off walk-up rate) without requiring advance purchase. Under Interpretation B the agent applies a smaller bereavement discount to the high walk-up rate, resulting in a much more expensive ticket.",
    "stripped_tool_desc": airline_stripped("get_user_details", "search_flights", "book_reservation", "transfer_to_human_agents"),
    "annotation_rationale": "Temporal priority conflict: the bereavement policy (emergency exception to normal pricing) conflicts with the advance purchase pricing structure (standing fare rule). The bereavement policy implicitly assumes last-minute travel but doesn't explicitly state it overrides advance purchase requirements.",
    "ambiguous_clause": "Rule 1: Passengers traveling due to the death or imminent death of an immediate family member are eligible for the bereavement fare, which provides a 50% discount on applicable fares. Rule 2: The lowest fare tiers require a minimum 14-day advance purchase; tickets booked within 14 days of departure are only available at higher fare tiers.",
    "unambiguous_clause": "Rule 1: Bereavement passengers get a 50% discount on applicable fares. Rule 2: Lowest fares require 14-day advance purchase. Priority: Bereavement fares (Rule 1) are calculated as 50% off the lowest available fare for the route regardless of advance purchase requirements (Rule 2). The advance purchase restriction is waived for verified bereavement travel.",
    "user_scenario": "My father just passed away and I need to fly from LA to Chicago tomorrow to be with my family. I know last-minute flights are expensive but I heard you have bereavement fares. Can you help me find something affordable?",
    "tools": airline_tools("get_user_details", "search_flights", "book_reservation", "transfer_to_human_agents"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-60110", "name": "Michael Torres", "email": "m.torres@email.com", "ff_tier": "none", "payment_methods": [{"id": "PM-CC-41", "type": "credit_card", "last_four": "9982"}]}},
        {"tool_name": "search_flights", "args_pattern": {"origin": "LAX", "destination": "ORD", "date": "*"}, "response": {"flights": [{"flight": "AA-2440", "depart": "06:15", "arrive": "12:20", "fare_class": "economy", "seats_available": 8, "price": 680, "advance_purchase_price": 289}, {"flight": "AA-2510", "depart": "10:30", "arrive": "16:35", "fare_class": "economy", "seats_available": 22, "price": 620, "advance_purchase_price": 265}]}},
        {"tool_name": "book_reservation", "args_pattern": {"user_id": "USR-60110", "flights": "*", "payment_method_id": "*"}, "response": {"status": "booked", "reservation_id": "RES-NEW-8810", "flight": "AA-2510", "fare": 310, "fare_type": "bereavement", "discount_applied": "50%", "payment_method": "credit_card"}}
    ]
})

# ─── cp_050: Personalized recommendations vs data minimization (retail) ───
clauses.append({
    "clause_id": "cp_050",
    "ambiguity_type": "conditional_precedence",
    "domain": "retail",
    "source_clause": "Personalized product recommendation policy vs data minimization principle",
    "ambiguity_point": "The customer engagement policy requires agents to suggest personalized product recommendations based on browsing and purchase history. The data minimization policy states agents should only access the minimum data necessary to resolve the customer's stated issue. A customer calls about a simple order status check.",
    "possible_interpretations": [
        "Interpretation A (engagement policy wins): The agent accesses purchase history and browsing data to offer tailored recommendations after resolving the order status query, as instructed by the engagement policy.",
        "Interpretation B (data minimization wins): The agent only accesses the order in question, provides the status, and does not access additional data for recommendation purposes since it's not necessary for the stated issue."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent checks order status then accesses purchase history to make product suggestions, extending the interaction. Under Interpretation B the agent provides only the order status and ends the interaction without accessing additional data.",
    "stripped_tool_desc": retail_stripped("get_user_details", "get_order_details", "get_product_details"),
    "annotation_rationale": "Authority-level conflict: the company-wide data minimization/privacy principle conflicts with the marketing department's customer engagement directive. Data minimization is often a regulatory-backed principle while engagement goals are revenue-driven, but no stated hierarchy exists between them in the policy.",
    "ambiguous_clause": "Rule 1: Agents must offer personalized product recommendations based on the customer's purchase and browsing history during every interaction to maximize engagement. Rule 2: Agents must adhere to the data minimization principle and only access customer data that is strictly necessary to resolve the customer's stated request.",
    "unambiguous_clause": "Rule 1: Agents should offer personalized recommendations based on purchase history during interactions. Rule 2: Agents must only access data necessary to resolve the customer's stated request. Priority: Data minimization (Rule 2) takes precedence. Agents may only offer recommendations if the customer explicitly asks for product suggestions or if the data needed is already accessed as part of resolving the primary issue.",
    "user_scenario": "Hi, can you tell me when my order ORD-37820 will arrive? That's all I need to know.",
    "tools": retail_tools("get_user_details", "get_order_details", "get_product_details"),
    "tool_responses": [
        {"tool_name": "get_user_details", "args_pattern": {"user_id": "*"}, "response": {"user_id": "USR-22010", "name": "Sophie Laurent", "email": "s.laurent@email.com", "loyalty_tier": "gold", "account_status": "active", "orders": ["ORD-37820", "ORD-37515", "ORD-36990"], "browsing_history": ["PROD-8800", "PROD-8805", "PROD-9100"]}},
        {"tool_name": "get_order_details", "args_pattern": {"order_id": "ORD-37820"}, "response": {"order_id": "ORD-37820", "status": "shipped", "items": [{"item_id": "ITEM-5510", "product_id": "PROD-7790", "name": "Ceramic Plant Pot Set", "category": "home_garden", "quantity": 1, "price": 34.99}], "tracking": {"carrier": "UPS", "tracking_number": "1Z999AA10123456784", "estimated_delivery": "2026-05-22"}, "payment_method": "credit_card", "total": 34.99}},
        {"tool_name": "get_product_details", "args_pattern": {"product_id": "PROD-8800"}, "response": {"product_id": "PROD-8800", "name": "Self-Watering Planter Large", "category": "home_garden", "price": 49.99, "related_to": "PROD-7790"}}
    ]
})

# ── Validate and write ────────────────────────────────────────────────────────

REQUIRED_FIELDS = [
    "clause_id", "ambiguity_type", "domain", "source_clause",
    "ambiguity_point", "possible_interpretations",
    "expected_agent_behavior_diff", "stripped_tool_desc",
    "annotation_rationale", "ambiguous_clause", "unambiguous_clause",
    "user_scenario", "tools", "tool_responses"
]

errors = []
for i, c in enumerate(clauses):
    cid = c.get("clause_id", f"index_{i}")
    # Required fields
    for f in REQUIRED_FIELDS:
        if f not in c:
            errors.append(f"{cid}: missing field '{f}'")
    # Type checks
    if c.get("ambiguity_type") != "conditional_precedence":
        errors.append(f"{cid}: ambiguity_type must be 'conditional_precedence'")
    if c.get("domain") not in ("retail", "airline"):
        errors.append(f"{cid}: invalid domain '{c.get('domain')}'")
    if not isinstance(c.get("possible_interpretations"), list) or len(c.get("possible_interpretations", [])) < 2:
        errors.append(f"{cid}: possible_interpretations must have 2+ entries")
    if not isinstance(c.get("tool_responses"), list) or len(c.get("tool_responses", [])) < 3:
        errors.append(f"{cid}: tool_responses must have 3+ entries")
    # Tool response structure
    for j, tr in enumerate(c.get("tool_responses", [])):
        for key in ("tool_name", "args_pattern", "response"):
            if key not in tr:
                errors.append(f"{cid}: tool_responses[{j}] missing '{key}'")

if errors:
    print("VALIDATION ERRORS:")
    for e in errors:
        print(f"  - {e}")
    raise SystemExit(1)

# Domain distribution
retail_count = sum(1 for c in clauses if c["domain"] == "retail")
airline_count = sum(1 for c in clauses if c["domain"] == "airline")
print(f"Total clauses: {len(clauses)}")
print(f"Retail: {retail_count}, Airline: {airline_count}")
print(f"IDs: {[c['clause_id'] for c in clauses]}")

# Check expected ID range
expected_ids = {f"cp_{i:03d}" for i in range(26, 51)}
actual_ids = {c["clause_id"] for c in clauses}
if actual_ids != expected_ids:
    missing = expected_ids - actual_ids
    extra = actual_ids - expected_ids
    if missing:
        print(f"MISSING IDs: {sorted(missing)}")
    if extra:
        print(f"EXTRA IDs: {sorted(extra)}")
    raise SystemExit(1)

# Write output
output_path = "/tmp/cp_clauses_part2.json"
with open(output_path, "w") as f:
    json.dump(clauses, f, indent=2, ensure_ascii=False)

print(f"\nWritten {len(clauses)} entries to {output_path}")
print("All validations passed.")
