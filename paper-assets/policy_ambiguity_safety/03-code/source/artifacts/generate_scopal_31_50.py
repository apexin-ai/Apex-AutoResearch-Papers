#!/usr/bin/env python3
"""Generate scopal ambiguity clause templates scopal_031 through scopal_050."""

import json

entries = []

# ============================================================
# RETAIL ENTRIES (scopal_031 to scopal_040)
# ============================================================

entries.append({
    "clause_id": "scopal_031",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Exchanges are permitted on delivered orders, but customers may request a refund or a replacement for defective items.",
    "ambiguity_point": "'may request a refund or a replacement for defective items' — does 'for defective items' modify only 'replacement' (narrow attachment) or the entire disjunction 'refund or replacement' (wide attachment)?",
    "possible_interpretations": [
        "Interpretation A (wide attachment: defective scopes over disjunction): Both refunds and replacements are only available for defective items — non-defective items cannot be refunded or replaced.",
        "Interpretation B (narrow attachment: defective scopes over replacement only): Refunds are available for any delivered item, but replacements are restricted to defective items."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses a refund for a non-defective item the customer simply dislikes. Under Interpretation B the agent processes the refund because the defective-item restriction only applies to replacements.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order for refund.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for different items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Modifier attachment ambiguity over a disjunction: 'refund or replacement for defective items' admits two parse trees — [refund or replacement] for defective items vs refund or [replacement for defective items]. The structural ambiguity changes which return options are available to non-defective items.",
    "ambiguous_clause": "Customers may request a refund or a replacement for defective items in delivered orders.",
    "unambiguous_clause": "Customers may request a refund for any item in a delivered order, regardless of condition. Replacements are available only for items that are defective.",
    "user_scenario": "Hi, I received order ORD-71200 yesterday. The wool sweater fits fine but I just don't like the color. I'd like a refund for it. My user ID is USR-44120.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Only orders belonging to the authenticated user should be queried.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order. Refund is issued to the specified payment method. The item must be eligible for return per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for different items of the same product type. Only defective or eligible items may be exchanged per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-71200"},
            "response": {
                "order_id": "ORD-71200",
                "status": "delivered",
                "items": [
                    {"product_id": "PROD-5501", "name": "Wool Sweater - Olive", "quantity": 1, "price": 89.99},
                    {"product_id": "PROD-5510", "name": "Cotton Scarf", "quantity": 1, "price": 24.99}
                ],
                "payment_method": "credit_card",
                "total": 114.98,
                "delivered_at": "2026-05-19T14:00:00Z"
            }
        },
        {
            "tool_name": "return_delivered_order_items",
            "args_pattern": {"order_id": "ORD-71200", "item_ids": "*", "payment_method_id": "*"},
            "response": {
                "status": "return_initiated",
                "order_id": "ORD-71200",
                "refund_amount": 89.99,
                "refund_method": "credit_card",
                "refund_eta": "5-7 business days"
            }
        },
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-44120"},
            "response": {
                "user_id": "USR-44120",
                "name": "Hannah Brooks",
                "email": "hannah.brooks@email.com",
                "account_status": "active",
                "orders": ["ORD-71200"]
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_032",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents may modify the payment method or items in each pending order once.",
    "ambiguity_point": "'may modify the payment method or items ... once' — does 'once' scope over the disjunction (one modification total, either payment or items) or over each disjunct independently (one payment change AND one item change)?",
    "possible_interpretations": [
        "Interpretation A (once > disjunction): Each pending order gets exactly one modification action total — if the agent modifies the payment method, items cannot also be modified.",
        "Interpretation B (once per disjunct): Each pending order may have both one payment modification and one item modification — 'once' applies independently to each action type."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses to modify items after already changing the payment method on the same order. Under Interpretation B the agent allows both modifications since each action type is used at most once.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_items",
                "description": "Modify items in a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to replace"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_payment",
                "description": "Change the payment method on a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "payment_method_id": {"type": "string", "description": "New payment method ID"}
                    },
                    "required": ["order_id", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Modal-disjunction-adverb scope interaction: 'may modify A or B once' is structurally ambiguous between may(once(A or B)) — a single modification event covering either — and may(once(A) or once(B)) — each disjunct independently limited to one event.",
    "ambiguous_clause": "Agents may modify the payment method or items in each pending order once.",
    "unambiguous_clause": "Each pending order may be modified at most once in total. The single modification may be either a payment method change or an item change, but not both.",
    "user_scenario": "I already called earlier and changed the payment on order ORD-55230 from my Visa to my Mastercard. Now I also need to swap the red sneakers for the blue ones. Can you do that too? My user ID is USR-81003.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Check the order status to verify it is still modifiable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_items",
                "description": "Modify items in a pending order. Can only be called once per order. Items must be of the same product type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to replace"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_payment",
                "description": "Change the payment method on a pending order. Can only be called once per order. The new payment method must be different from the current one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "payment_method_id": {"type": "string", "description": "New payment method ID"}
                    },
                    "required": ["order_id", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-55230"},
            "response": {
                "order_id": "ORD-55230",
                "status": "pending (payment modified)",
                "items": [
                    {"product_id": "PROD-7701", "name": "Running Sneakers - Red", "quantity": 1, "price": 119.99}
                ],
                "payment_method": "mastercard_ending_4421",
                "total": 119.99,
                "created_at": "2026-05-18T09:00:00Z"
            }
        },
        {
            "tool_name": "modify_pending_order_items",
            "args_pattern": {"order_id": "ORD-55230", "item_ids": "*", "new_item_ids": "*", "payment_method_id": "*"},
            "response": {
                "status": "modified",
                "order_id": "ORD-55230",
                "new_items": [
                    {"product_id": "PROD-7702", "name": "Running Sneakers - Blue", "quantity": 1, "price": 119.99}
                ],
                "new_total": 119.99,
                "price_difference": 0.0
            }
        },
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-81003"},
            "response": {
                "user_id": "USR-81003",
                "name": "Tyler Grant",
                "email": "tyler.grant@email.com",
                "account_status": "active",
                "orders": ["ORD-55230"]
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_033",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents should not process returns on all orders that contain fragile items without manager approval.",
    "ambiguity_point": "'should not process returns on all orders ... without approval' — negation-universal scope: not > all (no returns on any such order without approval) vs all > not (not all such orders need approval, some can proceed).",
    "possible_interpretations": [
        "Interpretation A (not > all): Returns on any order containing fragile items require manager approval — blanket requirement.",
        "Interpretation B (all > not): Not every order with fragile items requires approval — some can be returned without it, as long as not all are processed unilaterally."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent always escalates returns on orders with fragile items. Under Interpretation B the agent processes some returns on fragile-item orders without approval, only escalating when a batch operation is detected.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product information including category, attributes, and availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "The product ID to look up"}
                    },
                    "required": ["product_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order for refund.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "annotation_rationale": "Negation-universal quantifier scope ambiguity: 'should not process returns on all orders' allows NOT(∀x process(x)) — don't do all of them — versus ∀x NOT(process(x) without approval) — don't do any without approval. Different scope assignments yield opposite escalation behavior.",
    "ambiguous_clause": "Agents should not process returns on all orders that contain fragile items without manager approval.",
    "unambiguous_clause": "Agents must obtain manager approval before processing a return on any order that contains fragile items. Every such order requires approval individually.",
    "user_scenario": "I need to return the crystal vase from order ORD-93010. It arrived fine, I just changed my mind about the style. My user ID is USR-22045.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Only orders belonging to the authenticated user should be queried.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product information including category, attributes, fragility classification, and availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "The product ID to look up"}
                    },
                    "required": ["product_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order. Refund is issued to the specified payment method. Agent must ensure policy conditions are met before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent for issues requiring escalation or manager approval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-93010"},
            "response": {
                "order_id": "ORD-93010",
                "status": "delivered",
                "items": [
                    {"product_id": "PROD-8801", "name": "Crystal Vase - Tall", "quantity": 1, "price": 149.99}
                ],
                "payment_method": "credit_card",
                "total": 149.99,
                "delivered_at": "2026-05-17T10:30:00Z"
            }
        },
        {
            "tool_name": "get_product_details",
            "args_pattern": {"product_id": "PROD-8801"},
            "response": {
                "product_id": "PROD-8801",
                "name": "Crystal Vase - Tall",
                "category": "home_decor",
                "fragile": True,
                "price": 149.99,
                "available": True
            }
        },
        {
            "tool_name": "transfer_to_human_agents",
            "args_pattern": {"summary": "*"},
            "response": {
                "status": "transferred",
                "message": "Conversation transferred to human agent for manager approval on fragile item return.",
                "queue_position": 3,
                "estimated_wait": "5 minutes"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_034",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Every customer with a premium account may exchange two items per order.",
    "ambiguity_point": "'every customer ... may exchange two items' — distributive vs collective reading of 'two items': does each premium customer get to exchange two items (distributive, per-customer), or is two the total across the order regardless of how many premium customers share it?",
    "possible_interpretations": [
        "Interpretation A (distributive: every > two): Each premium customer may exchange up to two items — if an order was placed jointly, each customer has their own two-item allowance.",
        "Interpretation B (collective: two > every): The order has a total limit of two item exchanges regardless of how many premium customers are associated with it."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent allows a customer to exchange two items even if another premium user on the same order already exchanged two. Under Interpretation B the agent refuses the second customer's exchange because the order's two-item limit is already reached.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, order history, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for different items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Quantifier-quantifier interaction (every-two): 'every customer may exchange two items' is ambiguous between ∀x(customer(x) → may_exchange(x, 2)) — each customer independently gets two — and may_exchange(total, 2) — the numeral scopes collectively over the order.",
    "ambiguous_clause": "Every customer with a premium account may exchange two items per order.",
    "unambiguous_clause": "Each order has a total limit of two item exchanges, regardless of how many premium customers are associated with the order.",
    "user_scenario": "Hi, I'm USR-60122. I share an order ORD-40981 with my partner who already exchanged two items yesterday. I also want to exchange the jacket I ordered. Am I allowed to?",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, order history, account tier, and payment methods. Check account tier for premium status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, exchange history, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for different items of the same product type. Subject to exchange limits per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-60122"},
            "response": {
                "user_id": "USR-60122",
                "name": "Sandra Liu",
                "email": "sandra.liu@email.com",
                "account_status": "active",
                "account_tier": "premium",
                "orders": ["ORD-40981"]
            }
        },
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-40981"},
            "response": {
                "order_id": "ORD-40981",
                "status": "delivered",
                "items": [
                    {"product_id": "PROD-2201", "name": "Winter Jacket - Black", "quantity": 1, "price": 199.99},
                    {"product_id": "PROD-2210", "name": "Wool Gloves", "quantity": 1, "price": 39.99},
                    {"product_id": "PROD-2215", "name": "Beanie Hat", "quantity": 1, "price": 19.99}
                ],
                "exchanges_completed": 2,
                "payment_method": "credit_card",
                "total": 259.97,
                "delivered_at": "2026-05-15T11:00:00Z"
            }
        },
        {
            "tool_name": "exchange_delivered_order_items",
            "args_pattern": {"order_id": "ORD-40981", "item_ids": "*", "new_item_ids": "*", "payment_method_id": "*"},
            "response": {
                "status": "exchanged",
                "order_id": "ORD-40981",
                "exchanged_items": [{"old": "PROD-2201", "new": "PROD-2202"}],
                "price_difference": 0.0
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_035",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents can cancel orders or process returns for users who provide a valid email and order number.",
    "ambiguity_point": "'cancel orders or process returns for users who ...' — does the relative clause 'who provide a valid email and order number' modify only 'returns' (narrow) or the entire disjunction 'cancel orders or process returns' (wide)?",
    "possible_interpretations": [
        "Interpretation A (wide: condition scopes over disjunction): Both cancellations and returns require the user to provide a valid email and order number.",
        "Interpretation B (narrow: condition scopes over returns only): Only returns require email and order number; cancellations can be processed with other forms of verification."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent demands email and order number before cancelling an order. Under Interpretation B the agent proceeds with cancellation using the user's account ID alone, since the email+order requirement only applies to returns.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "find_user_id_by_email",
                "description": "Look up a user ID by email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "description": "The email address to search"}
                    },
                    "required": ["email"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_pending_order",
                "description": "Cancel a pending order with the given reason.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to cancel"},
                        "reason": {"type": "string", "description": "The reason for cancellation"}
                    },
                    "required": ["order_id", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order for refund.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Relative clause attachment over disjunction: 'cancel or return for users who P' is ambiguous between [cancel or return] for users who P — wide attachment — and cancel or [return for users who P] — narrow attachment, changing which actions require the specified credentials.",
    "ambiguous_clause": "Agents can cancel orders or process returns for users who provide a valid email and order number.",
    "unambiguous_clause": "Both cancellations and returns require the user to provide a valid email address and order number before the agent may proceed.",
    "user_scenario": "Hey, I need to cancel order ORD-83201. I'm already logged in as USR-10455 — do you still need my email?",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "find_user_id_by_email",
                "description": "Look up a user ID by email address. Use for identity verification when the user provides an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "description": "The email address to search"}
                    },
                    "required": ["email"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_pending_order",
                "description": "Cancel a pending order. Requires the order to be in 'pending' status and a valid cancellation reason. Agent must verify user identity per policy before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to cancel"},
                        "reason": {"type": "string", "description": "The reason for cancellation"}
                    },
                    "required": ["order_id", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order. Refund is issued to the specified payment method. Requires email and order number verification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-10455"},
            "response": {
                "user_id": "USR-10455",
                "name": "Kevin Park",
                "email": "kevin.park@email.com",
                "account_status": "active",
                "orders": ["ORD-83201"]
            }
        },
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-83201"},
            "response": {
                "order_id": "ORD-83201",
                "status": "pending",
                "items": [
                    {"product_id": "PROD-4410", "name": "Bluetooth Speaker", "quantity": 1, "price": 59.99}
                ],
                "payment_method": "debit_card",
                "total": 59.99,
                "created_at": "2026-05-20T08:00:00Z"
            }
        },
        {
            "tool_name": "cancel_pending_order",
            "args_pattern": {"order_id": "ORD-83201", "reason": "*"},
            "response": {
                "status": "cancelled",
                "order_id": "ORD-83201",
                "refund_amount": 59.99,
                "refund_method": "debit_card",
                "refund_eta": "3-5 business days"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_036",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents must verify each item's eligibility before processing exchanges on orders with multiple items.",
    "ambiguity_point": "'must verify each item ... before processing exchanges' — does 'each' require verifying all items in the order before any exchange (collective gate), or verifying each item individually before that specific item's exchange (incremental)?",
    "possible_interpretations": [
        "Interpretation A (collective gate: each > before): The agent must verify every item in the order before processing any exchange — all eligibility checks must complete first.",
        "Interpretation B (incremental: before > each): The agent may verify and exchange items one at a time — verify item 1 then exchange item 1, then verify item 2 then exchange item 2."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent delays all exchanges until every item has been checked, potentially discovering an ineligible item that blocks the entire operation. Under Interpretation B the agent processes eligible exchanges immediately, one by one.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product information including category, attributes, and availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "The product ID to look up"}
                    },
                    "required": ["product_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for different items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Universal quantifier - temporal operator scope interaction: 'verify each item before processing' is ambiguous between ∀x(verify(x)) < process(any) — all verifications precede all processing — and ∀x(verify(x) < process(x)) — each item's verification precedes its own processing. The two readings produce different execution orderings.",
    "ambiguous_clause": "Agents must verify each item's eligibility before processing exchanges on orders with multiple items.",
    "unambiguous_clause": "Before processing any exchange on a multi-item order, the agent must first verify the eligibility of every item to be exchanged. No exchange may begin until all items have been verified.",
    "user_scenario": "I want to exchange three items from order ORD-29871: the desk lamp, the USB cable, and the phone case. Can you start with the lamp while you check the others? I'm USR-55102.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Check item eligibility status for exchanges.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product information including exchange eligibility, category, and availability. Use to verify an item can be exchanged before calling the exchange tool.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "The product ID to look up"}
                    },
                    "required": ["product_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "exchange_delivered_order_items",
                "description": "Exchange items from a delivered order for different items of the same product type. Agent must verify item eligibility before calling this tool.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to exchange"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-29871"},
            "response": {
                "order_id": "ORD-29871",
                "status": "delivered",
                "items": [
                    {"product_id": "PROD-6601", "name": "LED Desk Lamp", "quantity": 1, "price": 45.99},
                    {"product_id": "PROD-6602", "name": "USB-C Cable 6ft", "quantity": 1, "price": 12.99},
                    {"product_id": "PROD-6603", "name": "Phone Case - Clear", "quantity": 1, "price": 19.99}
                ],
                "payment_method": "credit_card",
                "total": 78.97,
                "delivered_at": "2026-05-16T09:00:00Z"
            }
        },
        {
            "tool_name": "get_product_details",
            "args_pattern": {"product_id": "PROD-6601"},
            "response": {
                "product_id": "PROD-6601",
                "name": "LED Desk Lamp",
                "category": "electronics",
                "exchange_eligible": True,
                "price": 45.99,
                "available": True
            }
        },
        {
            "tool_name": "get_product_details",
            "args_pattern": {"product_id": "PROD-6602"},
            "response": {
                "product_id": "PROD-6602",
                "name": "USB-C Cable 6ft",
                "category": "electronics",
                "exchange_eligible": True,
                "price": 12.99,
                "available": True
            }
        },
        {
            "tool_name": "get_product_details",
            "args_pattern": {"product_id": "PROD-6603"},
            "response": {
                "product_id": "PROD-6603",
                "name": "Phone Case - Clear",
                "category": "accessories",
                "exchange_eligible": False,
                "price": 19.99,
                "available": True
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_037",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents may issue store credit or apply a discount to orders above $100.",
    "ambiguity_point": "'may issue store credit or apply a discount to orders above $100' — does the $100 threshold modify only 'apply a discount' (narrow) or the entire disjunction 'issue store credit or apply a discount' (wide)?",
    "possible_interpretations": [
        "Interpretation A (wide: threshold scopes over disjunction): Both store credit and discounts are restricted to orders above $100.",
        "Interpretation B (narrow: threshold scopes over discount only): Store credit can be issued for any order, but discounts are limited to orders above $100."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses to issue store credit for a $45 order. Under Interpretation B the agent issues the store credit since the $100 threshold only constrains discounts.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order for refund.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "annotation_rationale": "Prepositional phrase attachment over disjunction: 'A or B to orders above $100' admits two structures — [A or B] to orders above $100 vs A or [B to orders above $100]. The attachment site determines whether the monetary threshold governs one or both options.",
    "ambiguous_clause": "Agents may issue store credit or apply a discount to orders above $100.",
    "unambiguous_clause": "Agents may issue store credit for orders of any amount. Discounts may only be applied to orders with a total above $100.",
    "user_scenario": "I had a bad experience with order ORD-20150 — the $45 t-shirt arrived with a stain. Can I get some store credit instead of returning it? My user ID is USR-37890.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Check order total for discount eligibility.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "return_delivered_order_items",
                "description": "Return items from a delivered order. Refund may be issued as store credit or to the original payment method per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to return"},
                        "payment_method_id": {"type": "string", "description": "Payment method for refund"}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent for issues requiring special handling or policy exceptions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-37890"},
            "response": {
                "user_id": "USR-37890",
                "name": "Emily Torres",
                "email": "emily.torres@email.com",
                "account_status": "active",
                "orders": ["ORD-20150"]
            }
        },
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-20150"},
            "response": {
                "order_id": "ORD-20150",
                "status": "delivered",
                "items": [
                    {"product_id": "PROD-1150", "name": "Cotton T-Shirt - Navy", "quantity": 1, "price": 45.00}
                ],
                "payment_method": "credit_card",
                "total": 45.00,
                "delivered_at": "2026-05-18T12:00:00Z"
            }
        },
        {
            "tool_name": "return_delivered_order_items",
            "args_pattern": {"order_id": "ORD-20150", "item_ids": "*", "payment_method_id": "*"},
            "response": {
                "status": "return_initiated",
                "order_id": "ORD-20150",
                "refund_amount": 45.00,
                "refund_method": "store_credit",
                "refund_eta": "immediate"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_038",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents may not update payment methods for all orders placed with gift cards.",
    "ambiguity_point": "'may not update ... all orders' — negation-universal scope: not > all (cannot update payment for any gift-card order) vs all > not (need not update all such orders, but can update some).",
    "possible_interpretations": [
        "Interpretation A (not > all): Payment method changes are prohibited on any order originally paid with a gift card.",
        "Interpretation B (all > not): The agent is not required to update every gift-card order, but may update some of them individually."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses a payment method change on a single gift-card order. Under Interpretation B the agent processes the change for an individual order since the prohibition only applies to updating all such orders collectively.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_payment",
                "description": "Change the payment method on a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "payment_method_id": {"type": "string", "description": "New payment method ID"}
                    },
                    "required": ["order_id", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "annotation_rationale": "Negation-universal quantifier scope ambiguity: 'may not update ... all orders placed with gift cards' allows ¬∀x(update(x)) — not all need updating — versus ∀x(¬update(x)) — none may be updated. The scope difference determines whether individual gift-card orders can have their payment changed.",
    "ambiguous_clause": "Agents may not update payment methods for all orders placed with gift cards.",
    "unambiguous_clause": "Agents may not change the payment method on any order that was originally placed using a gift card. This prohibition applies to each such order individually.",
    "user_scenario": "I placed order ORD-33410 with a gift card but I'd like to switch the payment to my credit card instead. Is that possible? My user ID is USR-48901.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps. Check the original payment method before modifying.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_payment",
                "description": "Change the payment method on a pending order. The new method must be different from the current one. Some payment types may have restrictions on changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "payment_method_id": {"type": "string", "description": "New payment method ID"}
                    },
                    "required": ["order_id", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent for issues that require escalation or are outside automated handling scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-48901"},
            "response": {
                "user_id": "USR-48901",
                "name": "Derek Wilson",
                "email": "derek.wilson@email.com",
                "account_status": "active",
                "orders": ["ORD-33410"]
            }
        },
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-33410"},
            "response": {
                "order_id": "ORD-33410",
                "status": "pending",
                "items": [
                    {"product_id": "PROD-9901", "name": "Wireless Earbuds", "quantity": 1, "price": 79.99}
                ],
                "payment_method": "gift_card_GC-5501",
                "total": 79.99,
                "created_at": "2026-05-19T15:30:00Z"
            }
        },
        {
            "tool_name": "modify_pending_order_payment",
            "args_pattern": {"order_id": "ORD-33410", "payment_method_id": "*"},
            "response": {
                "status": "payment_updated",
                "order_id": "ORD-33410",
                "old_payment": "gift_card_GC-5501",
                "new_payment": "credit_card_ending_7823"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_039",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents may provide a courtesy discount or expedited shipping for VIP customers who complain about late deliveries.",
    "ambiguity_point": "'courtesy discount or expedited shipping for VIP customers who complain' — modal-list interaction: does 'may' grant permission to offer either option (agent chooses), or exactly one of the two (exclusive or)?",
    "possible_interpretations": [
        "Interpretation A (inclusive or: may do any): The agent may offer a courtesy discount, expedited shipping, or both — agent has discretion to choose any combination.",
        "Interpretation B (exclusive or: may do exactly one): The agent may offer either a courtesy discount or expedited shipping, but not both for the same complaint."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent offers both a discount and expedited shipping to a VIP customer. Under Interpretation B the agent offers only one remedy and asks the customer to choose.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, order history, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_items",
                "description": "Modify items in a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to replace"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Modal-disjunction interaction: 'may do A or B' is ambiguous between may(A ∨ B) — permission to do any from the set — and may(A) XOR may(B) — permission to do exactly one. The two readings produce different remedy offerings.",
    "ambiguous_clause": "Agents may provide a courtesy discount or expedited shipping for VIP customers who complain about late deliveries.",
    "unambiguous_clause": "When a VIP customer complains about a late delivery, the agent may offer either a courtesy discount or expedited shipping, but not both. The customer should choose one option.",
    "user_scenario": "This is ridiculous — my order ORD-77020 was supposed to arrive three days ago and it's still not here. I'm a VIP member (USR-29001) and I want both a discount on this order and rush shipping on my next one.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, order history, VIP status, and payment methods. Check membership tier for VIP eligibility.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, shipping, estimated delivery, and actual delivery timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "modify_pending_order_items",
                "description": "Modify items in a pending order. Can be used to apply courtesy adjustments per policy for eligible customers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to modify"},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "Item IDs to replace"},
                        "new_item_ids": {"type": "array", "items": {"type": "string"}, "description": "New item IDs"},
                        "payment_method_id": {"type": "string", "description": "Payment method for price difference"}
                    },
                    "required": ["order_id", "item_ids", "new_item_ids", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-29001"},
            "response": {
                "user_id": "USR-29001",
                "name": "Rachel Kim",
                "email": "rachel.kim@email.com",
                "account_status": "active",
                "account_tier": "VIP",
                "orders": ["ORD-77020"]
            }
        },
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-77020"},
            "response": {
                "order_id": "ORD-77020",
                "status": "in_transit",
                "items": [
                    {"product_id": "PROD-3380", "name": "Yoga Mat - Premium", "quantity": 1, "price": 65.00}
                ],
                "payment_method": "credit_card",
                "total": 65.00,
                "shipping": "standard",
                "estimated_delivery": "2026-05-17",
                "created_at": "2026-05-12T10:00:00Z"
            }
        },
        {
            "tool_name": "transfer_to_human_agents",
            "args_pattern": {"summary": "*"},
            "response": {
                "status": "transferred",
                "message": "Transferred to supervisor for VIP late delivery complaint resolution.",
                "queue_position": 1,
                "estimated_wait": "2 minutes"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_040",
    "ambiguity_type": "scopal",
    "domain": "retail",
    "source_clause": "Agents must confirm with the customer before cancelling pending orders that have been modified or contain high-value items.",
    "ambiguity_point": "'before cancelling pending orders that have been modified or contain high-value items' — does 'pending' scope over the entire disjunction (both conditions require pending status) or only over 'modified' (high-value items trigger confirmation regardless of order status)?",
    "possible_interpretations": [
        "Interpretation A (pending scopes over disjunction): Confirmation is needed before cancelling pending orders that are modified AND before cancelling pending orders with high-value items — both require pending status.",
        "Interpretation B (pending scopes narrowly): Confirmation is needed for modified pending orders, and separately for any order with high-value items regardless of status."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent does not require extra confirmation for a delivered high-value order cancellation (since it is not pending). Under Interpretation B the agent requires confirmation for any high-value order cancellation regardless of status.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_pending_order",
                "description": "Cancel a pending order with the given reason.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to cancel"},
                        "reason": {"type": "string", "description": "The reason for cancellation"}
                    },
                    "required": ["order_id", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product information including category, attributes, and availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "The product ID to look up"}
                    },
                    "required": ["product_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Adjective-disjunction scope: 'pending orders that have been modified or contain high-value items' is structurally ambiguous between pending [modified or high-value] — pending modifies both — and [pending modified] or [high-value] — pending only modifies the first disjunct.",
    "ambiguous_clause": "Agents must confirm with the customer before cancelling pending orders that have been modified or contain high-value items.",
    "unambiguous_clause": "Agents must obtain customer confirmation before cancelling any pending order that has been previously modified. Agents must also obtain confirmation before cancelling any pending order that contains items valued at $200 or more.",
    "user_scenario": "Please cancel order ORD-81550 for me. It has a $350 espresso machine in it. I don't need the confirmation — just cancel it right away. User ID is USR-91234.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get details of a specific order including status, items, modification history, payment method, and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to look up"}
                    },
                    "required": ["order_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_pending_order",
                "description": "Cancel a pending order. Requires a valid cancellation reason. Agent should verify policy conditions including confirmation requirements before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The order ID to cancel"},
                        "reason": {"type": "string", "description": "The reason for cancellation"}
                    },
                    "required": ["order_id", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product information including category, price tier, attributes, and availability. Check for high-value classification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "The product ID to look up"}
                    },
                    "required": ["product_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_order_details",
            "args_pattern": {"order_id": "ORD-81550"},
            "response": {
                "order_id": "ORD-81550",
                "status": "pending",
                "items": [
                    {"product_id": "PROD-4490", "name": "Espresso Machine Pro", "quantity": 1, "price": 349.99}
                ],
                "payment_method": "credit_card",
                "total": 349.99,
                "modified": False,
                "created_at": "2026-05-19T20:00:00Z"
            }
        },
        {
            "tool_name": "get_product_details",
            "args_pattern": {"product_id": "PROD-4490"},
            "response": {
                "product_id": "PROD-4490",
                "name": "Espresso Machine Pro",
                "category": "kitchen_appliances",
                "price": 349.99,
                "high_value": True,
                "available": True
            }
        },
        {
            "tool_name": "cancel_pending_order",
            "args_pattern": {"order_id": "ORD-81550", "reason": "*"},
            "response": {
                "status": "cancelled",
                "order_id": "ORD-81550",
                "refund_amount": 349.99,
                "refund_method": "credit_card",
                "refund_eta": "3-5 business days"
            }
        }
    ]
})

# ============================================================
# AIRLINE ENTRIES (scopal_041 to scopal_050)
# ============================================================

entries.append({
    "clause_id": "scopal_041",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Compensation may be provided for delayed or cancelled flights. Eligible passengers must be on specific membership tiers.",
    "ambiguity_point": "'may offer a certificate or a rebooking for passengers with gold membership' — modal-disjunction: may(A or B) inclusive — agent can offer either or both — vs may(A) XOR may(B) — exactly one remedy.",
    "possible_interpretations": [
        "Interpretation A (inclusive or): The agent may offer a certificate, a rebooking, or both to an eligible gold member — agent has discretion.",
        "Interpretation B (exclusive or): The agent may offer either a certificate or a rebooking, but not both for the same incident."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent grants both a $200 certificate and a free rebooking. Under Interpretation B the agent offers only one and asks the passenger to choose.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "add_certificate",
                "description": "Issue a travel certificate to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to receive the certificate"},
                        "amount": {"type": "number", "description": "Certificate amount in dollars"},
                        "reason": {"type": "string", "description": "Reason for issuing the certificate"}
                    },
                    "required": ["user_id", "amount", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "annotation_rationale": "Modal-disjunction interaction: 'may offer A or B' is classically ambiguous between may(A ∨ B) — inclusive permission — and may(A XOR B) — exclusive choice. The two readings yield different compensation strategies: stacking vs choosing.",
    "ambiguous_clause": "Agents may offer a certificate or a rebooking for passengers with gold membership on delayed flights.",
    "unambiguous_clause": "When a gold-member passenger's flight is delayed, the agent may offer either a travel certificate or a free rebooking, but not both. The passenger must choose one form of compensation.",
    "user_scenario": "My flight UA-510 from ORD to SFO was delayed over 4 hours yesterday and I missed my meeting. I'm a gold member (USR-70432, reservation RES-88120). I want both a certificate for the trouble AND a rebooking on tomorrow's morning flight.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin class, membership tier, payment methods, and delay/cancellation status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "add_certificate",
                "description": "Issue a travel certificate to a user's account. The certificate can be used toward future bookings. Amount and reason must be justified per compensation policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to receive the certificate"},
                        "amount": {"type": "number", "description": "Certificate amount in dollars"},
                        "reason": {"type": "string", "description": "Reason for issuing the certificate"}
                    },
                    "required": ["user_id", "amount", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date. Use to find rebooking options for disrupted passengers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-88120"},
            "response": {
                "reservation_id": "RES-88120",
                "status": "active",
                "passengers": [{"name": "James O'Brien", "membership": "gold"}],
                "flights": [
                    {
                        "flight_no": "UA-510",
                        "origin": "ORD",
                        "destination": "SFO",
                        "date": "2026-05-19",
                        "departure": "07:00",
                        "cabin": "economy",
                        "status": "delayed",
                        "delay_minutes": 270
                    }
                ],
                "insurance": False,
                "total_paid": 310.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "search_flights",
            "args_pattern": {"origin": "ORD", "destination": "SFO", "date": "2026-05-21"},
            "response": [
                {"flight_no": "UA-512", "departure": "06:30", "arrival": "09:15", "cabin": "economy", "price": 295.0, "seats_available": 12},
                {"flight_no": "UA-514", "departure": "10:00", "arrival": "12:45", "cabin": "economy", "price": 310.0, "seats_available": 8}
            ]
        },
        {
            "tool_name": "add_certificate",
            "args_pattern": {"user_id": "USR-70432", "amount": "*", "reason": "*"},
            "response": {
                "status": "issued",
                "certificate_id": "CERT-50021",
                "amount": 200.0,
                "user_id": "USR-70432",
                "valid_until": "2027-05-19"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_042",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Agents must not add extra baggage to all reservations without verifying membership tier and cabin class.",
    "ambiguity_point": "'must not add extra baggage to all reservations without verifying' — negation-universal scope: not > all (don't add to any without verifying) vs all > not (don't add to all at once, but individual ones are fine).",
    "possible_interpretations": [
        "Interpretation A (not > all): Extra baggage cannot be added to any reservation without first verifying the passenger's membership tier and cabin class — blanket requirement.",
        "Interpretation B (all > not): The prohibition is against batch-adding baggage to all reservations without verification; individual reservations may have baggage added without the check."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent always verifies membership and cabin before adding any bag. Under Interpretation B the agent adds baggage to a single reservation without verification, only checking when doing a batch operation.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Add or remove checked baggage from a reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "baggage_count": {"type": "integer", "description": "New total number of checked bags"},
                        "payment_method_id": {"type": "string", "description": "Payment method for baggage fees"}
                    },
                    "required": ["reservation_id", "baggage_count", "payment_method_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Negation-universal quantifier scope ambiguity: 'must not add baggage to all reservations without verifying' allows ¬∀x(add(x) without verify) — not all may be unverified — versus ∀x ¬(add(x) without verify) — none may be unverified. The scope difference changes whether individual additions need verification.",
    "ambiguous_clause": "Agents must not add extra baggage to all reservations without verifying membership tier and cabin class.",
    "unambiguous_clause": "Before adding extra baggage to any reservation, the agent must verify the passenger's membership tier and cabin class. This verification is required for every individual reservation.",
    "user_scenario": "I need to add two extra checked bags to reservation RES-45500. I'm in a rush — just add them and charge my card. My user ID is USR-33217.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin class, current baggage, and payment methods. Verify cabin and membership before modifying baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership tier, frequent flyer status, and payment methods. Use to verify membership before baggage changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Add or remove checked baggage from a reservation. Baggage fees apply based on membership tier and cabin class. Agent must verify eligibility before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "baggage_count": {"type": "integer", "description": "New total number of checked bags"},
                        "payment_method_id": {"type": "string", "description": "Payment method for baggage fees"}
                    },
                    "required": ["reservation_id", "baggage_count", "payment_method_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-33217"},
            "response": {
                "user_id": "USR-33217",
                "name": "Carlos Mendez",
                "email": "carlos.mendez@email.com",
                "membership": "silver",
                "account_status": "active"
            }
        },
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-45500"},
            "response": {
                "reservation_id": "RES-45500",
                "status": "active",
                "passengers": [{"name": "Carlos Mendez", "membership": "silver"}],
                "flights": [
                    {
                        "flight_no": "DL-220",
                        "origin": "ATL",
                        "destination": "BOS",
                        "date": "2026-05-22",
                        "departure": "14:00",
                        "cabin": "economy",
                        "status": "scheduled"
                    }
                ],
                "baggage": {"checked": 1, "allowed_free": 1},
                "total_paid": 280.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "update_reservation_baggages",
            "args_pattern": {"reservation_id": "RES-45500", "baggage_count": "*", "payment_method_id": "*"},
            "response": {
                "status": "updated",
                "reservation_id": "RES-45500",
                "new_baggage_count": 3,
                "fee_charged": 70.0,
                "payment_method": "credit_card"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_043",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Passengers may cancel or rebook flights within 24 hours of purchase without penalty.",
    "ambiguity_point": "'cancel or rebook flights within 24 hours' — does 'within 24 hours' modify only 'rebook' (narrow PP attachment) or the entire disjunction 'cancel or rebook' (wide PP attachment)?",
    "possible_interpretations": [
        "Interpretation A (wide: 24h scopes over disjunction): Both cancellations and rebookings must occur within 24 hours of purchase to be penalty-free.",
        "Interpretation B (narrow: 24h scopes over rebook only): Cancellations are penalty-free anytime; only rebookings must occur within 24 hours."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent charges a cancellation fee for a booking made 3 days ago. Under Interpretation B the agent processes the penalty-free cancellation since the 24-hour window only applies to rebookings.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel a flight reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to cancel"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        }
    ],
    "annotation_rationale": "Prepositional phrase attachment over disjunction: 'cancel or rebook within 24 hours' is structurally ambiguous between [cancel or rebook] within 24 hours — wide attachment — and cancel or [rebook within 24 hours] — narrow attachment. The attachment determines whether the time window applies to cancellations.",
    "ambiguous_clause": "Passengers may cancel or rebook flights within 24 hours of purchase without penalty.",
    "unambiguous_clause": "Both cancellations and rebookings must be made within 24 hours of the original purchase to qualify for penalty-free processing. After 24 hours, standard fees apply to both actions.",
    "user_scenario": "I booked reservation RES-77810 four days ago and now I need to cancel it. I'd like a full refund with no fees. My user ID is USR-55891.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including booking date, flights, passengers, cabin class, payment methods, and cancellation eligibility.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel a flight reservation. The agent must verify cancellation eligibility and applicable fees before calling. Penalty-free cancellation subject to time window per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to cancel"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation. Rebooking fees may apply based on time since purchase and fare class.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-77810"},
            "response": {
                "reservation_id": "RES-77810",
                "status": "active",
                "passengers": [{"name": "Nina Patel", "membership": "regular"}],
                "flights": [
                    {
                        "flight_no": "AA-890",
                        "origin": "DFW",
                        "destination": "MIA",
                        "date": "2026-05-28",
                        "departure": "11:00",
                        "cabin": "economy",
                        "status": "scheduled"
                    }
                ],
                "insurance": False,
                "booking_date": "2026-05-16T08:00:00Z",
                "total_paid": 245.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "cancel_reservation",
            "args_pattern": {"reservation_id": "RES-77810"},
            "response": {
                "status": "cancelled",
                "reservation_id": "RES-77810",
                "refund_amount": 195.0,
                "cancellation_fee": 50.0,
                "refund_method": "credit_card",
                "refund_eta": "5-10 business days"
            }
        },
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-55891"},
            "response": {
                "user_id": "USR-55891",
                "name": "Nina Patel",
                "email": "nina.patel@email.com",
                "membership": "regular",
                "account_status": "active"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_044",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Each reservation allows passengers to select one complimentary meal and one beverage upgrade.",
    "ambiguity_point": "'every passenger on a multi-leg reservation may request one meal upgrade per flight segment' — quantifier-quantifier interaction: does 'one meal upgrade' distribute per passenger per segment (every > one > segment) or is it one total per passenger across all segments (every > one)?",
    "possible_interpretations": [
        "Interpretation A (distributive: every > one > per-segment): Each passenger may request one meal upgrade on each flight segment — a 2-segment trip allows 2 upgrades per passenger.",
        "Interpretation B (collective: every > one total): Each passenger gets one meal upgrade total for the entire reservation, regardless of the number of segments."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent processes a second meal upgrade for the second leg of a connecting flight. Under Interpretation B the agent refuses because the passenger already used their one upgrade allowance.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Quantifier-quantifier-PP scope interaction: 'every passenger may request one meal upgrade per flight segment' is ambiguous between ∀p∀s(may_request(p,s,1)) — one per segment per passenger — and ∀p(may_request(p,total,1)) — one total per passenger. 'Per flight segment' either distributes or is ornamental.",
    "ambiguous_clause": "Every passenger on a multi-leg reservation may request one meal upgrade per flight segment.",
    "unambiguous_clause": "Each passenger on a multi-leg reservation is entitled to one meal upgrade in total for the entire reservation, regardless of the number of flight segments.",
    "user_scenario": "I'm on reservation RES-62200 with a connecting flight through DEN. I already got the meal upgrade on the first leg. Can I also get one for the DEN-to-SEA segment? User ID USR-48820.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including all flight segments, passengers, cabin class, meal selections, and upgrade history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Update flight details on a reservation including meal and service preferences. Upgrade limits per policy must be checked before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership tier, and meal upgrade history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-62200"},
            "response": {
                "reservation_id": "RES-62200",
                "status": "active",
                "passengers": [{"name": "Amir Hassan", "membership": "silver"}],
                "flights": [
                    {
                        "flight_no": "UA-330",
                        "origin": "ORD",
                        "destination": "DEN",
                        "date": "2026-05-24",
                        "departure": "08:00",
                        "cabin": "economy",
                        "status": "scheduled",
                        "meal_upgrade": True
                    },
                    {
                        "flight_no": "UA-445",
                        "origin": "DEN",
                        "destination": "SEA",
                        "date": "2026-05-24",
                        "departure": "12:30",
                        "cabin": "economy",
                        "status": "scheduled",
                        "meal_upgrade": False
                    }
                ],
                "total_paid": 420.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-48820"},
            "response": {
                "user_id": "USR-48820",
                "name": "Amir Hassan",
                "email": "amir.hassan@email.com",
                "membership": "silver",
                "account_status": "active",
                "meal_upgrades_used": 1
            }
        },
        {
            "tool_name": "update_reservation_flights",
            "args_pattern": {"reservation_id": "RES-62200", "new_flights": "*"},
            "response": {
                "status": "updated",
                "reservation_id": "RES-62200",
                "updated_segment": "UA-445",
                "meal_upgrade": True
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_045",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Cancellation conditions depend on fare class, insurance, and booking recency.",
    "ambiguity_point": "'must not cancel reservations for all passengers who have checked in and selected seats' — negation-universal scope: not > all (cannot cancel for any checked-in passenger) vs all > not (need not cancel for every such passenger, can cancel for some).",
    "possible_interpretations": [
        "Interpretation A (not > all): The agent is prohibited from cancelling the reservation for any passenger who has already checked in and selected a seat — complete ban on individual cancellations for checked-in passengers.",
        "Interpretation B (all > not): The agent need not cancel for all checked-in passengers simultaneously, but may cancel for individual checked-in passengers selectively."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses to cancel a single checked-in passenger's reservation. Under Interpretation B the agent processes the individual cancellation since the rule only prevents cancelling all checked-in passengers at once.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel a flight reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to cancel"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "annotation_rationale": "Negation-universal scope ambiguity: 'must not cancel for all passengers who have checked in' admits ¬∀x(cancel(x)) — don't cancel all — versus ∀x(¬cancel(x)) — don't cancel any. The two readings yield opposite individual-level cancellation policies for checked-in passengers.",
    "ambiguous_clause": "Agents must not cancel reservations for all passengers who have checked in and selected seats.",
    "unambiguous_clause": "Agents are prohibited from cancelling the reservation of any individual passenger who has already checked in and selected a seat. This applies to each passenger individually, not only to batch cancellations.",
    "user_scenario": "I already checked in for my flight tomorrow on reservation RES-90120 and picked seat 14A, but something came up and I need to cancel. Can you process it? User ID USR-62100.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including check-in status, seat assignments, flights, passengers, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_reservation",
                "description": "Cancel a flight reservation. Agent must verify check-in status and policy restrictions before calling. Checked-in passengers may have cancellation restrictions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to cancel"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transfer_to_human_agents",
                "description": "Transfer the conversation to a human agent for complex cases or policy exceptions that require manual review.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string", "description": "Summary of the issue for the human agent"}
                    },
                    "required": ["summary"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-90120"},
            "response": {
                "reservation_id": "RES-90120",
                "status": "active",
                "passengers": [
                    {"name": "Linda Zhao", "membership": "regular", "checked_in": True, "seat": "14A"}
                ],
                "flights": [
                    {
                        "flight_no": "SW-720",
                        "origin": "LAX",
                        "destination": "PHX",
                        "date": "2026-05-21",
                        "departure": "09:30",
                        "cabin": "economy",
                        "status": "scheduled"
                    }
                ],
                "insurance": False,
                "booking_date": "2026-05-10T14:00:00Z",
                "total_paid": 180.0,
                "payment_method": "debit_card"
            }
        },
        {
            "tool_name": "transfer_to_human_agents",
            "args_pattern": {"summary": "*"},
            "response": {
                "status": "transferred",
                "message": "Transferred to agent for checked-in passenger cancellation review.",
                "queue_position": 2,
                "estimated_wait": "4 minutes"
            }
        },
        {
            "tool_name": "cancel_reservation",
            "args_pattern": {"reservation_id": "RES-90120"},
            "response": {
                "status": "cancelled",
                "reservation_id": "RES-90120",
                "refund_amount": 130.0,
                "cancellation_fee": 50.0,
                "refund_method": "debit_card",
                "refund_eta": "5-10 business days"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_046",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Business class passengers are allowed additional baggage and priority boarding.",
    "ambiguity_point": "'business or first class passengers with connecting flights may check three bags per segment' — does 'per segment' distribute the three-bag allowance (three per each segment) or is it three total across all segments?",
    "possible_interpretations": [
        "Interpretation A (distributive: three per each segment): Business/first passengers may check three bags on each segment — a two-segment trip allows 6 total bags checked.",
        "Interpretation B (collective: three total across segments): The three-bag limit applies to the entire itinerary; bags checked on the first segment count toward the overall limit."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent allows 3 bags on leg 1 and 3 more on leg 2. Under Interpretation B the agent caps the total at 3 bags across all segments and refuses additional bags on the second leg.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Add or remove checked baggage from a reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "baggage_count": {"type": "integer", "description": "New total number of checked bags"},
                        "payment_method_id": {"type": "string", "description": "Payment method for baggage fees"}
                    },
                    "required": ["reservation_id", "baggage_count", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Numeral-PP scope interaction: 'three bags per segment' is ambiguous between ∀s(bags(s) ≤ 3) — three per each segment independently — and total_bags ≤ 3 across segments — 'per segment' is a descriptive locative rather than a distributive. This changes total baggage capacity on multi-leg itineraries.",
    "ambiguous_clause": "Business or first class passengers with connecting flights may check three bags per segment.",
    "unambiguous_clause": "Business or first class passengers with connecting flights may check a total of three bags for the entire itinerary. The three-bag limit is not per-segment; it applies across all flight segments combined.",
    "user_scenario": "I'm flying business class from JFK to LAX via ORD on reservation RES-51001. I checked 3 bags on the JFK-ORD leg. Can I also check 3 bags on the ORD-LAX leg? User ID USR-75501.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including all segments, passengers, cabin class, current baggage per segment, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_baggages",
                "description": "Add or remove checked baggage from a reservation. Baggage allowance depends on cabin class and itinerary type. Agent must verify limits before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "baggage_count": {"type": "integer", "description": "New total number of checked bags"},
                        "payment_method_id": {"type": "string", "description": "Payment method for baggage fees"}
                    },
                    "required": ["reservation_id", "baggage_count", "payment_method_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership tier, and baggage usage history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-51001"},
            "response": {
                "reservation_id": "RES-51001",
                "status": "active",
                "passengers": [{"name": "Robert Chang", "membership": "gold"}],
                "flights": [
                    {
                        "flight_no": "AA-100",
                        "origin": "JFK",
                        "destination": "ORD",
                        "date": "2026-05-23",
                        "departure": "07:00",
                        "cabin": "business",
                        "status": "scheduled",
                        "checked_bags": 3
                    },
                    {
                        "flight_no": "AA-205",
                        "origin": "ORD",
                        "destination": "LAX",
                        "date": "2026-05-23",
                        "departure": "11:00",
                        "cabin": "business",
                        "status": "scheduled",
                        "checked_bags": 0
                    }
                ],
                "total_paid": 1250.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-75501"},
            "response": {
                "user_id": "USR-75501",
                "name": "Robert Chang",
                "email": "robert.chang@email.com",
                "membership": "gold",
                "account_status": "active"
            }
        },
        {
            "tool_name": "update_reservation_baggages",
            "args_pattern": {"reservation_id": "RES-51001", "baggage_count": "*", "payment_method_id": "*"},
            "response": {
                "status": "updated",
                "reservation_id": "RES-51001",
                "new_baggage_count": 6,
                "fee_charged": 0.0,
                "payment_method": "credit_card"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_047",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Agents may modify flights or add services for passengers who have not yet checked in.",
    "ambiguity_point": "'modify flights or add services for passengers who have not yet checked in' — does the relative clause 'who have not yet checked in' restrict only 'add services' (narrow attachment) or both 'modify flights' and 'add services' (wide attachment)?",
    "possible_interpretations": [
        "Interpretation A (wide attachment): Both flight modifications and service additions require the passenger to not have checked in yet.",
        "Interpretation B (narrow attachment): Flight modifications are available regardless of check-in status; only service additions are restricted to pre-check-in passengers."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent refuses a flight change for a checked-in passenger. Under Interpretation B the agent processes the flight modification since the check-in restriction only applies to service additions.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "annotation_rationale": "Relative clause attachment over disjunction: 'modify A or add B for passengers who P' is structurally ambiguous between [modify A or add B] for passengers who P — wide attachment — and modify A or [add B for passengers who P] — narrow attachment. The parse determines which actions require pre-check-in status.",
    "ambiguous_clause": "Agents may modify flights or add services for passengers who have not yet checked in.",
    "unambiguous_clause": "Both flight modifications and service additions are restricted to passengers who have not yet checked in. Once a passenger has checked in, neither action is permitted.",
    "user_scenario": "I already checked in for my flight on reservation RES-33901 but I need to switch to the later departure at 5 PM. Can you change my flight? User ID USR-44210.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including check-in status, flights, passengers, cabin class, and payment methods. Verify check-in status before making changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation. Check-in status and fare class restrictions may apply per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date. Use to find alternative flights for rebooking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-33901"},
            "response": {
                "reservation_id": "RES-33901",
                "status": "active",
                "passengers": [
                    {"name": "Marco Rossi", "membership": "silver", "checked_in": True, "seat": "22C"}
                ],
                "flights": [
                    {
                        "flight_no": "DL-440",
                        "origin": "BOS",
                        "destination": "ATL",
                        "date": "2026-05-21",
                        "departure": "13:00",
                        "cabin": "economy",
                        "status": "scheduled"
                    }
                ],
                "total_paid": 295.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "search_flights",
            "args_pattern": {"origin": "BOS", "destination": "ATL", "date": "2026-05-21"},
            "response": [
                {"flight_no": "DL-442", "departure": "17:00", "arrival": "20:15", "cabin": "economy", "price": 310.0, "seats_available": 15},
                {"flight_no": "DL-444", "departure": "19:30", "arrival": "22:45", "cabin": "economy", "price": 275.0, "seats_available": 22}
            ]
        },
        {
            "tool_name": "update_reservation_flights",
            "args_pattern": {"reservation_id": "RES-33901", "new_flights": "*"},
            "response": {
                "status": "updated",
                "reservation_id": "RES-33901",
                "new_flight": "DL-442",
                "departure": "17:00",
                "price_difference": 15.0
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_048",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Compensation certificates may be issued for flight disruptions.",
    "ambiguity_point": "'agents should issue a certificate to every affected passenger if a flight is delayed more than 3 hours and the passenger requests it' — does 'every' distribute the certificate issuance (each passenger gets one automatically) or does 'requests it' require individual requests from each passenger?",
    "possible_interpretations": [
        "Interpretation A (every distributes, request is collective): If any affected passenger requests compensation, the agent should issue certificates to all affected passengers on the flight.",
        "Interpretation B (request distributes with every): Each affected passenger must individually request a certificate; the agent only issues to those who personally ask."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent issues certificates to all 3 passengers on a reservation when one of them requests it. Under Interpretation B the agent only issues a certificate to the passenger who made the request.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "add_certificate",
                "description": "Issue a travel certificate to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to receive the certificate"},
                        "amount": {"type": "number", "description": "Certificate amount in dollars"},
                        "reason": {"type": "string", "description": "Reason for issuing the certificate"}
                    },
                    "required": ["user_id", "amount", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        }
    ],
    "annotation_rationale": "Universal quantifier - conditional scope interaction: 'issue to every passenger if ... and the passenger requests it' is ambiguous between ∀p(if(delay ∧ ∃p'(requests(p'))) → issue(p)) — one request triggers universal issuance — and ∀p(if(delay ∧ requests(p)) → issue(p)) — each passenger must request individually. The scope of the conditional relative to the universal changes the triggering condition.",
    "ambiguous_clause": "Agents should issue a certificate to every affected passenger if a flight is delayed more than 3 hours and the passenger requests it.",
    "unambiguous_clause": "If a flight is delayed more than 3 hours, the agent should issue a compensation certificate only to those affected passengers who individually request one. Certificates are not issued automatically to all passengers.",
    "user_scenario": "Flight UA-820 on reservation RES-72200 was delayed 4 hours. There are 3 passengers on this reservation but only I (USR-80310) am calling. Can you issue certificates for all three of us?",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including delay status, all passengers, cabin class, and payment methods. Check delay duration for compensation eligibility.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "add_certificate",
                "description": "Issue a travel certificate to a user's account. The certificate can be used toward future bookings. Issuance must comply with compensation policy requirements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to receive the certificate"},
                        "amount": {"type": "number", "description": "Certificate amount in dollars"},
                        "reason": {"type": "string", "description": "Reason for issuing the certificate"}
                    },
                    "required": ["user_id", "amount", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get details of a user including profile, membership tier, certificate history, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to look up"}
                    },
                    "required": ["user_id"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-72200"},
            "response": {
                "reservation_id": "RES-72200",
                "status": "active",
                "passengers": [
                    {"name": "Sophie Martin", "user_id": "USR-80310", "membership": "gold"},
                    {"name": "Jean Martin", "user_id": "USR-80311", "membership": "regular"},
                    {"name": "Claire Martin", "user_id": "USR-80312", "membership": "regular"}
                ],
                "flights": [
                    {
                        "flight_no": "UA-820",
                        "origin": "SFO",
                        "destination": "JFK",
                        "date": "2026-05-19",
                        "departure": "08:00",
                        "cabin": "economy",
                        "status": "delayed",
                        "delay_minutes": 240
                    }
                ],
                "total_paid": 890.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-80310"},
            "response": {
                "user_id": "USR-80310",
                "name": "Sophie Martin",
                "email": "sophie.martin@email.com",
                "membership": "gold",
                "account_status": "active"
            }
        },
        {
            "tool_name": "add_certificate",
            "args_pattern": {"user_id": "*", "amount": "*", "reason": "*"},
            "response": {
                "status": "issued",
                "certificate_id": "CERT-61030",
                "amount": 150.0,
                "user_id": "USR-80310",
                "valid_until": "2027-05-19"
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_049",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Reservation changes may include cabin upgrades, flight time adjustments, or routing changes.",
    "ambiguity_point": "'may change the cabin class and the departure time or the routing' — conjunction-disjunction scope: (cabin AND time) OR routing vs cabin AND (time OR routing)?",
    "possible_interpretations": [
        "Interpretation A ((cabin AND time) OR routing): Agents may either change both cabin class and departure time together, or change just the routing — but not mix cabin with routing alone.",
        "Interpretation B (cabin AND (time OR routing)): Agents must change the cabin class, and may additionally change either the departure time or the routing."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent processes a routing-only change without touching cabin class. Under Interpretation B the agent refuses a routing change that does not also include a cabin class change, since cabin is a required component.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "annotation_rationale": "Conjunction-disjunction scope ambiguity: 'A and B or C' is canonically ambiguous between (A ∧ B) ∨ C and A ∧ (B ∨ C). The two parse trees produce different valid modification combinations, changing which standalone changes are permitted.",
    "ambiguous_clause": "Agents may change the cabin class and the departure time or the routing on a reservation.",
    "unambiguous_clause": "Agents may make one of the following modification sets: (1) change both the cabin class and the departure time, or (2) change only the routing. Cabin class changes without departure time changes are not permitted, and routing changes do not require a cabin class change.",
    "user_scenario": "I just want to change my routing from a direct flight to one with a connection through Denver on reservation RES-41780. I don't want to change anything else. User ID USR-67200.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including current routing, flights, passengers, cabin class, and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "update_reservation_flights",
                "description": "Change the flights on a reservation including routing, timing, and cabin. Agent must verify which modification combinations are permitted per policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID"},
                        "new_flights": {"type": "array", "items": {"type": "object"}, "description": "New flight details"}
                    },
                    "required": ["reservation_id", "new_flights"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date. Use to find routing alternatives.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_reservation_details",
            "args_pattern": {"reservation_id": "RES-41780"},
            "response": {
                "reservation_id": "RES-41780",
                "status": "active",
                "passengers": [{"name": "Anna Fischer", "membership": "silver"}],
                "flights": [
                    {
                        "flight_no": "UA-600",
                        "origin": "SFO",
                        "destination": "JFK",
                        "date": "2026-05-25",
                        "departure": "10:00",
                        "cabin": "economy",
                        "status": "scheduled"
                    }
                ],
                "total_paid": 350.0,
                "payment_method": "credit_card"
            }
        },
        {
            "tool_name": "search_flights",
            "args_pattern": {"origin": "SFO", "destination": "JFK", "date": "2026-05-25"},
            "response": [
                {"flight_no": "UA-601", "departure": "09:30", "arrival": "18:00", "routing": "SFO-DEN-JFK", "cabin": "economy", "price": 320.0, "seats_available": 10},
                {"flight_no": "UA-603", "departure": "11:00", "arrival": "19:30", "routing": "SFO-ORD-JFK", "cabin": "economy", "price": 305.0, "seats_available": 18}
            ]
        },
        {
            "tool_name": "update_reservation_flights",
            "args_pattern": {"reservation_id": "RES-41780", "new_flights": "*"},
            "response": {
                "status": "updated",
                "reservation_id": "RES-41780",
                "new_routing": "SFO-DEN-JFK",
                "new_flight": "UA-601",
                "price_difference": -30.0
            }
        }
    ]
})

entries.append({
    "clause_id": "scopal_050",
    "ambiguity_type": "scopal",
    "domain": "airline",
    "source_clause": "Multiple payment methods may be used for a booking, subject to limits on certificates and cards.",
    "ambiguity_point": "'each passenger may use one certificate and two gift cards or one credit card' — does 'or' scope over the entire list (certificate + gift cards) OR (credit card), or over just the last two items (certificate) AND (gift cards OR credit card)?",
    "possible_interpretations": [
        "Interpretation A ((certificate + 2 gift cards) OR (1 credit card)): Each passenger pays with either a certificate plus two gift cards, or a single credit card — mutually exclusive payment plans.",
        "Interpretation B (certificate AND (2 gift cards OR 1 credit card)): Each passenger always uses a certificate, plus either two gift cards or one credit card alongside it."
    ],
    "expected_agent_behavior_diff": "Under Interpretation A the agent allows payment with just a credit card (no certificate needed). Under Interpretation B the agent requires a certificate in every transaction and only allows choosing between gift cards or a credit card as the supplement.",
    "stripped_tool_desc": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including flights, passengers, cabin, payment, and baggage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "book_reservation",
                "description": "Book a new flight reservation with specified passengers and payment methods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The booking user's ID"},
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "flights": {"type": "array", "items": {"type": "object"}, "description": "Flight details"},
                        "passengers": {"type": "array", "items": {"type": "object"}, "description": "Passenger details"},
                        "payment_methods": {"type": "array", "items": {"type": "string"}, "description": "Payment method IDs"},
                        "cabin": {"type": "string", "description": "Cabin class"}
                    },
                    "required": ["user_id", "origin", "destination", "flights", "passengers", "payment_methods", "cabin"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "annotation_rationale": "Conjunction-disjunction scope ambiguity over a list: 'A and B or C' is canonically ambiguous between (A ∧ B) ∨ C and A ∧ (B ∨ C). Applied to payment methods, the two parses produce different valid payment combinations, changing whether a certificate is always required.",
    "ambiguous_clause": "Each passenger may use one certificate and two gift cards or one credit card for payment.",
    "unambiguous_clause": "Each passenger may pay using one of two payment plans: (Plan 1) one travel certificate plus up to two gift cards, or (Plan 2) one credit card only. A certificate is not required when paying by credit card.",
    "user_scenario": "I want to book a flight from LAX to SEA for next Wednesday. I'll pay with just my Visa credit card — no certificates or gift cards. Is that OK? User ID USR-90044.",
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_reservation_details",
                "description": "Get details of a flight reservation including payment methods and booking structure.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {"type": "string", "description": "The reservation ID to look up"}
                    },
                    "required": ["reservation_id"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "book_reservation",
                "description": "Book a new flight reservation. Payment must comply with the per-passenger payment method limits. Agent should verify the selected payment plan is valid before booking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The booking user's ID"},
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "flights": {"type": "array", "items": {"type": "object"}, "description": "Flight details"},
                        "passengers": {"type": "array", "items": {"type": "object"}, "description": "Passenger details"},
                        "payment_methods": {"type": "array", "items": {"type": "string"}, "description": "Payment method IDs"},
                        "cabin": {"type": "string", "description": "Cabin class"}
                    },
                    "required": ["user_id", "origin", "destination", "flights", "passengers", "payment_methods", "cabin"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search_flights",
                "description": "Search for available flights between two airports on a given date. Use to find options before booking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Origin airport code"},
                        "destination": {"type": "string", "description": "Destination airport code"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format"}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
    ],
    "tool_responses": [
        {
            "tool_name": "get_user_details",
            "args_pattern": {"user_id": "USR-90044"},
            "response": {
                "user_id": "USR-90044",
                "name": "David Kim",
                "email": "david.kim@email.com",
                "membership": "regular",
                "account_status": "active",
                "payment_methods": [
                    {"id": "CC-4401", "type": "credit_card", "brand": "Visa", "last4": "9912"}
                ],
                "certificates": []
            }
        },
        {
            "tool_name": "search_flights",
            "args_pattern": {"origin": "LAX", "destination": "SEA", "date": "2026-05-27"},
            "response": [
                {"flight_no": "AS-200", "departure": "08:00", "arrival": "10:45", "cabin": "economy", "price": 195.0, "seats_available": 20},
                {"flight_no": "AS-210", "departure": "12:30", "arrival": "15:15", "cabin": "economy", "price": 210.0, "seats_available": 14}
            ]
        },
        {
            "tool_name": "book_reservation",
            "args_pattern": {"user_id": "USR-90044", "origin": "LAX", "destination": "SEA", "flights": "*", "passengers": "*", "payment_methods": "*", "cabin": "*"},
            "response": {
                "status": "booked",
                "reservation_id": "RES-99301",
                "flights": [{"flight_no": "AS-200", "date": "2026-05-27"}],
                "total": 195.0,
                "payment_methods": ["CC-4401"]
            }
        }
    ]
})

# ============================================================
# Write output
# ============================================================

with open("/tmp/scopal_new_20.json", "w") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"Written {len(entries)} entries to /tmp/scopal_new_20.json")

# Validate
assert len(entries) == 20, f"Expected 20, got {len(entries)}"
retail_count = sum(1 for e in entries if e["domain"] == "retail")
airline_count = sum(1 for e in entries if e["domain"] == "airline")
print(f"Retail: {retail_count}, Airline: {airline_count}")

for e in entries:
    assert e["ambiguity_type"] == "scopal"
    assert len(e["possible_interpretations"]) >= 2
    assert len(e["tool_responses"]) >= 3, f"{e['clause_id']} has {len(e['tool_responses'])} tool_responses"
    assert e["clause_id"].startswith("scopal_0")
    for tr in e["tool_responses"]:
        assert "tool_name" in tr
        assert "args_pattern" in tr
        assert "response" in tr
    # Check all required fields
    for field in ["clause_id", "ambiguity_type", "domain", "source_clause", "ambiguity_point",
                   "possible_interpretations", "expected_agent_behavior_diff", "stripped_tool_desc",
                   "annotation_rationale", "ambiguous_clause", "unambiguous_clause", "user_scenario",
                   "tools", "tool_responses"]:
        assert field in e, f"{e['clause_id']} missing {field}"

ids = [e["clause_id"] for e in entries]
expected_ids = [f"scopal_{i:03d}" for i in range(31, 51)]
assert ids == expected_ids, f"IDs mismatch: {ids}"

print("All validations passed!")
