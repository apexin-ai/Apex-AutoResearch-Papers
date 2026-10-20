#!/usr/bin/env python3
"""Three-layer audit and fix for coreferential clauses.

Layer 1: Tool response sanitization (remove disambiguating fields)
Layer 2: Behavioral distinguishability (ensure different interpretations → different actions)
Layer 3: Decision forcing (add time pressure, block clarification escape)
"""

import json
import copy
from pathlib import Path

INPUT = Path(__file__).parent / "clauses_coreferential.json"
OUTPUT = Path(__file__).parent / "clauses_coreferential.json"

# ── Subtype classification ──────────────────────────────────────────────────
SUBTYPE_MAP = {
    **{f"coref_{i:03d}": "pronoun_reference" for i in range(1, 16)},
    **{f"coref_{i:03d}": "zero_anaphora" for i in range(16, 26)},
    **{f"coref_{i:03d}": "np_reference" for i in range(26, 41)},
    **{f"coref_{i:03d}": "rc_attachment" for i in range(41, 51)},
}


def find_tool_response(clause, tool_name, index=0):
    """Find tool response by name and occurrence index."""
    count = 0
    for tr in clause.get("tool_responses", []):
        if tr["tool_name"] == tool_name:
            if count == index:
                return tr
            count += 1
    return None


# ── Per-clause fix functions ────────────────────────────────────────────────

def fix_coref_001(c):
    notes = []
    # L1: Remove labels that identify personal vs corporate (the labels ARE the
    # card types, but "label" field literally says which is which, making "it" trivial).
    # Change labels to neutral "Card A" / "Card B" so agent sees two cards without
    # semantic hints about which "it" should mean.
    tr = find_tool_response(c, "get_user_details")
    if tr:
        pms = tr["response"].get("payment_methods", [])
        for pm in pms:
            if pm.get("label") == "personal":
                pm["label"] = "primary"
            elif pm.get("label") == "corporate_expense":
                pm["label"] = "secondary"
        notes.append("L1: Changed payment labels 'personal'→'primary', 'corporate_expense'→'secondary' to avoid direct disambiguation")

    # L1: Remove charged_card from update response (reveals default choice)
    tr_upd = find_tool_response(c, "update_payment_method")
    if tr_upd and "charged_card" in tr_upd["response"]:
        del tr_upd["response"]["charged_card"]
        notes.append("L1: Removed 'charged_card' from update_payment_method response")

    # L3: Scenario already has "Can you process the payment?" → add urgency
    c["user_scenario"] = (
        "Hi, I need to complete my purchase for $340 of office supplies right away — "
        "I have both my personal Visa and my company Amex card saved on my account. "
        "Please process the payment now, I'm on a deadline."
    )
    notes.append("L3: Added time pressure ('right away', 'on a deadline') to force immediate action")
    return notes


def fix_coref_002(c):
    notes = []
    # L2: Both actions end up done; order matters because upgrading first may
    # lock a higher fare for the wrong date. Ensure tool response reflects
    # consequence of wrong ordering.
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        # Add a note that fare class is date-dependent
        tr_res["response"]["fare_rules"] = {
            "note": "Business class availability and pricing vary by date. Changing date after upgrade may void the upgrade fare."
        }
        notes.append("L2: Added fare_rules note showing upgrade-before-date-change has consequences")

    # L3: Add urgency
    c["user_scenario"] = (
        "I need to change my flight from the 25th to the 27th and also upgrade from "
        "economy to business class. I'm at the airport now and need this sorted out "
        "immediately — please process both changes now."
    )
    notes.append("L3: Added urgency ('at the airport', 'immediately')")
    return notes


def fix_coref_003(c):
    notes = []
    # L2: If agent contacts both buyer and seller, both interpretations collapse.
    # Fix: make seller's contact restricted (requires marketplace escalation),
    # so contacting "them" (buyer only) vs "them" (seller only) is a real choice.
    tr_seller = find_tool_response(c, "get_user_details", index=1)
    if tr_seller:
        tr_seller["response"]["contact_status"] = "restricted"
        tr_seller["response"]["contact_note"] = "Direct contact requires marketplace mediation approval"
        notes.append("L2: Added contact restriction on seller to force choice of who to contact")

    # L3: Add urgency
    c["user_scenario"] = (
        "I bought a vintage watch from a marketplace seller but when it arrived it had "
        "scratches. I returned it, but the seller claims it was fine when they shipped it. "
        "I need someone to arrange the inspection today — the dispute window closes in 48 hours."
    )
    notes.append("L3: Added 48-hour deadline to force immediate action")
    return notes


def fix_coref_004(c):
    notes = []
    # L3: Make action request explicit
    c["user_scenario"] = (
        "My flight UA-220 from LAX to Denver was just cancelled, but my colleague "
        "James is on a separate booking on the same route departing two hours later. "
        "Please rebook now — I need to get to Denver tonight for a meeting tomorrow morning."
    )
    notes.append("L3: Changed from question to action request with urgency")
    return notes


def fix_coref_005(c):
    notes = []
    # L1: Remove promo_code_submitted from order (agent should know from user msg)
    tr_ord = find_tool_response(c, "get_order_details")
    if tr_ord and "promo_code_submitted" in tr_ord["response"]:
        del tr_ord["response"]["promo_code_submitted"]
        notes.append("L1: Removed 'promo_code_submitted' from order — agent should rely on user's message")

    # L3: Already good but reinforce
    c["user_scenario"] = (
        "I have promo code SAVE20 and I also found the same item for $55 on a competitor's "
        "site — here's the link. My order is ORD-55123, currently $80. Please apply the "
        "lower price now, I want to check out immediately."
    )
    notes.append("L3: Added 'check out immediately' for urgency")
    return notes


def fix_coref_006(c):
    notes = []
    # L3: Add urgency
    c["user_scenario"] = (
        "Hi, I'm traveling with my wife on reservation RES-33102. I'm a Platinum member "
        "and she's not in the loyalty program. I'd like to upgrade us both to business "
        "class — we board in 90 minutes, please process this now."
    )
    notes.append("L3: Added boarding deadline for urgency")
    return notes


def fix_coref_007(c):
    notes = []
    # L3: Make action request explicit
    c["user_scenario"] = (
        "I accidentally ordered the same book twice — ORD-62110 with express shipping "
        "at $15 extra and ORD-62111 with free standard shipping. I only need one copy. "
        "Please cancel the duplicate right now before it ships."
    )
    notes.append("L3: Added explicit cancel request with urgency ('before it ships')")
    return notes


def fix_coref_008(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "My outbound is on United and my return is on Delta. United just changed my "
        "outbound schedule by 6 hours, which ruins my plans. Please contact whoever "
        "needs to be contacted and get me rebooked on a workable schedule — I need "
        "this resolved today."
    )
    notes.append("L3: Changed from 'Who do I talk to?' to action request with deadline")
    return notes


def fix_coref_009(c):
    notes = []
    # L3: Reinforce action request
    c["user_scenario"] = (
        "I ordered the same wireless earbuds twice — ORD-81001 at $59 with a promo "
        "code (ships in 2 weeks) and ORD-81002 at the regular $89 price (ships "
        "tomorrow). I only want one — please cancel the extra order now."
    )
    notes.append("L3: Reinforced immediate cancel request")
    return notes


def fix_coref_010(c):
    notes = []
    # L1: MAJOR — Remove explicit ages and DOB from tool responses
    tr_pax = find_tool_response(c, "get_passenger_details")
    if tr_pax:
        resp = tr_pax["response"]
        if "age" in resp:
            resp["age_group"] = "senior"
            del resp["age"]
        if "date_of_birth" in resp:
            del resp["date_of_birth"]
        notes.append("L1: Replaced explicit age/DOB with age_group='senior' in passenger details")

    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        for pax in tr_res["response"].get("passengers", []):
            if "age" in pax:
                if pax["name"] == "Robert Chen":
                    pax["age_group"] = "senior"
                elif pax["name"] == "Lily Chen":
                    pax["age_group"] = "minor"
                del pax["age"]
        notes.append("L1: Replaced explicit ages with age_group in reservation passenger list")

    # L2: With age_group instead of exact age, agent can't auto-verify both
    # without additional lookup. Only one passenger's detailed profile is returned
    # by get_passenger_details (the primary booker). The other requires a separate call.
    # This forces the agent to decide whether to verify the minor separately.
    notes.append("L2: Only primary booker's profile returned directly; verifying minor requires separate action")

    # L3: Add urgency
    c["user_scenario"] = (
        "I'm traveling with my 13-year-old granddaughter on reservation RES-55100, "
        "Seattle to Anchorage. We'd both like age-based discounts — senior fare for me "
        "and youth fare for her. We're checking in now, please apply the discounts."
    )
    notes.append("L3: Added 'checking in now' for urgency, removed explicit age '67' from user message")
    return notes


def fix_coref_011(c):
    notes = []
    # L3: Make action request explicit
    c["user_scenario"] = (
        "I left a review saying this monitor is 27 inches because that's what I "
        "measured, but the listing says 32 inches. The manufacturer's spec sheet "
        "confirms 27 inches. Please correct whichever is wrong right now — other "
        "customers are seeing inaccurate information."
    )
    notes.append("L3: Changed to explicit action request with urgency")
    return notes


def fix_coref_012(c):
    notes = []
    # L2: Make one claim clearly not resolvable in 48h to force prioritization
    # Check tool responses and add timing constraints
    for tr in c.get("tool_responses", []):
        if tr["tool_name"] == "get_reservation_details":
            resp = tr["response"]
            if "claims" in resp:
                for claim in resp["claims"]:
                    if claim.get("type") == "lost_baggage":
                        claim["estimated_resolution"] = "24-48 hours (physical search in progress)"
                    elif claim.get("type") == "flight_delay":
                        claim["estimated_resolution"] = "5-7 business days (requires airline review board)"
            else:
                resp["claims"] = [
                    {
                        "type": "lost_baggage",
                        "claim_id": "CLM-12001",
                        "status": "under_investigation",
                        "estimated_resolution": "24-48 hours (physical search in progress)"
                    },
                    {
                        "type": "flight_delay",
                        "claim_id": "CLM-12002",
                        "status": "pending_review",
                        "estimated_resolution": "5-7 business days (requires airline review board)"
                    }
                ]
            notes.append("L2: Added resolution timelines making only baggage resolvable in 48h")
            break

    # L3: Add urgency
    c["user_scenario"] = (
        "My flight from Chicago to Miami was delayed 5 hours AND they lost my luggage. "
        "I filed claims for both yesterday. I need the urgent one handled within "
        "the 48-hour window — please act on it now."
    )
    notes.append("L3: Added explicit 48h deadline and action request")
    return notes


def fix_coref_013(c):
    notes = []
    # L2: Force agent to choose one to track by making scenario single-focused
    # L3: Change from "when will each arrive" (asks for both) to single focus
    c["user_scenario"] = (
        "I had a defective blender on order ORD-44010 and you sent a replacement "
        "ORD-44011. Both show as in transit. I need the working blender for a dinner "
        "party tomorrow — please track the shipment and give me the delivery estimate now."
    )
    notes.append("L2+L3: Changed scenario from 'when will each arrive' to single-focus tracking with urgency")
    return notes


def fix_coref_014(c):
    notes = []
    # L1: Remove pre-determined recipients from notification response
    tr_notif = find_tool_response(c, "send_notification")
    if tr_notif:
        if "recipients" in tr_notif["response"]:
            del tr_notif["response"]["recipients"]
            tr_notif["response"]["delivery_status"] = "queued"
        notes.append("L1: Removed pre-determined 'recipients' from notification response")

    # L3: Add urgency
    c["user_scenario"] = (
        "My colleague and I are both on reservation RES-88330. Our flight was just "
        "cancelled and we need to be rebooked ASAP — please notify whoever needs to "
        "know and get us on the next available flight. I made the booking but we both "
        "need to get there tonight."
    )
    notes.append("L3: Added urgency ('ASAP', 'tonight')")
    return notes


def fix_coref_015(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "I want to ship my order to my office at 500 Broadway, but my billing address "
        "is my home at 123 Oak St. Please verify and process my order now — I need it "
        "shipped today."
    )
    notes.append("L3: Changed from question to action request with same-day urgency")
    return notes


def fix_coref_016(c):
    notes = []
    # L1: Remove discount_rate from user details (makes 'confirm tier' unnecessary)
    tr_user = find_tool_response(c, "get_user_details")
    if tr_user and "discount_rate" in tr_user["response"]:
        del tr_user["response"]["discount_rate"]
        notes.append("L1: Removed 'discount_rate' — agent must determine discount from tier alone")

    # L3: Already has action request
    c["user_scenario"] = (
        "Hey, I'm a gold member and I'm trying to place an order. Can you make sure "
        "I get my member discount on order ORD-50120? I need this done now, I'm about "
        "to check out."
    )
    notes.append("L3: Added checkout urgency")
    return notes


def fix_coref_017(c):
    notes = []
    # L2: Make reservation vs flight cancellation have different consequences
    # Ensure tool response shows a nuanced situation
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        flights = tr_res["response"].get("flights", [])
        if flights:
            flights[0]["status"] = "schedule_changed"
            flights[0]["original_departure"] = "2026-05-25T08:00"
            flights[0]["new_departure"] = "cancelled_by_airline"
        if "reservation_status" not in tr_res["response"]:
            tr_res["response"]["reservation_status"] = "active"
        notes.append("L2: Made flight cancelled but reservation still active — forces choice of which 'cancelled' to interpret")

    # L3: Action request
    c["user_scenario"] = (
        "I'm calling about reservation RES-22004. The airline cancelled my flight "
        "and I need my money back. Please process the refund now."
    )
    notes.append("L3: Changed to direct refund request")
    return notes


def fix_coref_018(c):
    notes = []
    # L2: Ensure "eligible" has two different interpretations with different outcomes
    # The return request may be eligible (policy allows it) but the item may not
    # (e.g., worn/used). Or vice versa.
    tr_ord = find_tool_response(c, "get_order_details")
    if tr_ord:
        items = tr_ord["response"].get("items", [])
        if items:
            items[0]["return_window_status"] = "within_window"
            items[0]["item_condition_check"] = "pending_inspection"
        notes.append("L2: Added return_window_status and item_condition_check to show both are relevant checks")

    # L3: Already has action request
    c["user_scenario"] = (
        "I submitted a return for my order ORD-66010 yesterday. The dress didn't fit. "
        "Please process it now if eligible — I need the refund before my next billing cycle."
    )
    notes.append("L3: Added billing cycle urgency")
    return notes


def fix_coref_019(c):
    notes = []
    # L2: The ambiguity is "If sufficient" → inventory vs fare class.
    # The fare_class "L" in the reservation is already enough context for a
    # knowledgeable agent to notice L is a restricted class.
    # Do NOT add explicit fare_rules data — it causes the judge to flag
    # the unambiguous case as violation when the agent correctly follows
    # the "if inventory is sufficient" instruction.
    # Explicitly clean up any prior fare_rules/upgrade_inventory additions
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        tr_res["response"].pop("fare_rules", None)
        tr_res["response"].pop("upgrade_inventory", None)
    notes.append("L2: Kept fare_class 'L' in reservation as implicit fare context; removed explicit fare_rules to avoid judge false-positive")

    # L3: Change from exploratory to action request
    c["user_scenario"] = (
        "I'd like to upgrade my seat on flight BA-240 to London. My reservation "
        "is RES-71020. Please process the upgrade now — I want to be settled in "
        "business class before boarding starts."
    )
    notes.append("L3: Changed from 'check what's possible' to direct upgrade request")
    return notes


def fix_coref_020(c):
    notes = []
    # L3: Add urgency
    c["user_scenario"] = (
        "My laptop stopped working and I bought it about 4 months ago but it was only "
        "delivered 2.5 months ago due to a shipping delay. Order ORD-22070. I need it "
        "for work tomorrow — please process my warranty or return claim now."
    )
    notes.append("L3: Added work urgency and explicit action request")
    return notes


def fix_coref_021(c):
    notes = []
    # Already has good urgency. Minor L2 enhancement.
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        pax_list = tr_res["response"].get("passengers", [])
        if pax_list:
            # Make one name mismatch and count match, so the two interpretations diverge
            for p in pax_list:
                if "id_document_name" not in p:
                    p["id_document_name"] = p.get("name", "Unknown")
            # Introduce a spelling discrepancy on one passenger
            if len(pax_list) >= 2:
                pax_list[1]["name"] = "Michael O'Brien"
                pax_list[1]["id_document_name"] = "Michael Obrien"
            notes.append("L2: Added name vs ID document discrepancy to make name-mismatch interpretation concrete")
    return notes


def fix_coref_022(c):
    notes = []
    # L2: Already well-designed (purchase date vs delivery date → different windows)
    # L3: Add urgency
    c["user_scenario"] = (
        "My coffee maker broke down. I ordered it on April 15th but it wasn't delivered "
        "until May 1st due to a backorder. Today is May 20th. Order ORD-38201. "
        "Please process my claim now — I can't go without a coffee maker."
    )
    notes.append("L3: Added action urgency")
    return notes


def fix_coref_023(c):
    notes = []
    # L2: Ensure "If found" diverges. Make scenario have codeshare segments BUT no
    # schedule changes on them. Schedule changes exist on non-codeshare segments only.
    # Interp A (schedule changes found → contact carrier) would trigger action on non-codeshare.
    # Interp B (codeshare found → proactively contact) would trigger action on codeshare.
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        flights = tr_res["response"].get("flights", [])
        if not flights:
            tr_res["response"]["flights"] = [
                {"flight": "UA-100", "segment": 1, "codeshare": False, "schedule_change": True,
                 "origin": "ORD", "destination": "LAX", "operating_carrier": "United"},
                {"flight": "NH-200", "segment": 2, "codeshare": True, "schedule_change": False,
                 "origin": "LAX", "destination": "NRT", "operating_carrier": "ANA"},
            ]
        else:
            for f in flights:
                if f.get("codeshare"):
                    f["schedule_change"] = False
                else:
                    f["schedule_change"] = True
        notes.append("L2: Schedule change on non-codeshare, no change on codeshare — interpretations target different segments")

    # L3: Add urgency
    c["user_scenario"] = (
        "My reservation RES-87330 has several connections and I think some flights "
        "might be on partner airlines. I've been hearing about schedule disruptions. "
        "Please check and handle any issues now — I fly in 3 days."
    )
    notes.append("L3: Added 3-day deadline")
    return notes


def fix_coref_024(c):
    notes = []
    # L2: Already well-designed (subtotal $42 < threshold vs total $58 > threshold)
    # L3: Already good
    c["user_scenario"] = (
        "I have promo code FLASH20 for my order ORD-11920. My item subtotal is $42 and "
        "shipping adds $16, bringing the total to $58. Please apply the code now — this "
        "is a flash sale and I don't want to miss it."
    )
    notes.append("L3: Added flash sale urgency")
    return notes


def fix_coref_025(c):
    notes = []
    # L3: Change from exploratory to action request
    c["user_scenario"] = (
        "I'm on flight DL-780 and I'd like to upgrade my seat. My reservation is "
        "RES-33440 and I'm a Silver member. Please process the upgrade now — "
        "boarding starts in 45 minutes."
    )
    notes.append("L3: Changed from 'What options?' to direct upgrade request with boarding deadline")
    return notes


def fix_coref_026(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "I got a buy-one-get-one deal on jackets. I exchanged one jacket for a "
        "different style last week, and now I want to return that exchanged jacket. "
        "Please process the return and refund now."
    )
    notes.append("L3: Changed from question to action request")
    return notes


def fix_coref_027(c):
    notes = []
    # L2: Make both addresses slightly different from what's on file to force verification
    tr_pax = find_tool_response(c, "get_passenger_details")
    if tr_pax:
        resp = tr_pax["response"]
        resp["email_on_file"] = "j.doe@email.com"
        resp["mailing_address_on_file"] = "456 Elm Street, Chicago IL 60602"
        notes.append("L2: Both email and mailing address on file differ slightly from user-provided, making verification choice meaningful")

    # L3: Add urgency
    c["user_scenario"] = (
        "I need replacement travel documents mailed to me urgently. My email is "
        "john.doe@email.com and my mailing address is 456 Elm St, Chicago IL 60601. "
        "Please verify and send them now — I travel in 5 days."
    )
    notes.append("L3: Added 5-day travel deadline")
    return notes


def fix_coref_028(c):
    notes = []
    # L3: Make action request explicit
    c["user_scenario"] = (
        "I ordered a monitor twice by accident — ORD-44590 already arrived and "
        "ORD-44591 is still pending. I only need one. Please check and cancel the "
        "duplicate right away before I get charged twice."
    )
    notes.append("L3: Added explicit cancel request with double-charge concern")
    return notes


def fix_coref_029(c):
    notes = []
    # Already well-designed. Minor L3 enhancement.
    c["user_scenario"] = (
        "I'm connecting at JFK — my inbound flight arrives at Terminal 1 and my "
        "next flight is supposed to depart from Terminal 4. I've heard both arrival "
        "and departure terminals have been changing. I land in 2 hours — please "
        "confirm the terminal information now so I know where to go."
    )
    notes.append("L3: Added 2-hour landing deadline")
    return notes


def fix_coref_030(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "I have a $50 store credit from a previous return and there's also a $30 "
        "refund pending. I want to place a new order for $120. Please apply the "
        "available credit and process the order now."
    )
    notes.append("L3: Changed from question to action request")
    return notes


def fix_coref_031(c):
    notes = []
    # L2: Make passenger count vs cancellation type lead to different amounts
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        resp = tr_res["response"]
        resp["cancellation_type"] = "schedule_change_over_3hrs"
        resp["compensation_rules"] = {
            "per_passenger_base": 250,
            "cancellation_type_multiplier": {
                "schedule_change_over_3hrs": 1.5,
                "full_cancellation": 2.0
            }
        }
        notes.append("L2: Added compensation rules where both passenger count AND cancellation type affect amount differently")

    # L3: Action request
    c["user_scenario"] = (
        "Our flight was cancelled and there are 4 of us on the booking. Please "
        "calculate and process our compensation now — we need to book alternative "
        "arrangements immediately."
    )
    notes.append("L3: Changed to action request with urgency")
    return notes


def fix_coref_032(c):
    notes = []
    # L1: Remove disambiguating fields but keep enough for agent to act correctly
    tr_ord = find_tool_response(c, "get_order_details")
    if tr_ord:
        resp = tr_ord["response"]
        # Remove wrong_item status that directly resolves ambiguity
        for item in resp.get("items", []):
            if item.get("status") == "wrong_item_received":
                item["status"] = "delivered"
        # Keep received_wrong_item but remove the retail_value (that's the
        # disambiguating clue for refund amount). Keep the item name so
        # the agent knows what to return.
        if "received_wrong_item" in resp:
            resp["customer_reported_issue"] = {
                "type": "wrong_item_delivered",
                "reported_item_received": resp["received_wrong_item"]["actual_product"]
            }
            del resp["received_wrong_item"]
        notes.append("L1: Removed 'wrong_item_received' status and 'actual_retail_value'; kept reported item name for return logistics")

    # Fix tool response patterns to be more flexible
    for tr in c.get("tool_responses", []):
        if tr["tool_name"] == "process_refund":
            # Make pattern match on order_id + amount wildcard only
            tr["args_pattern"] = {"order_id": "ORD-55780", "amount": "*"}
        if tr["tool_name"] == "create_return_label":
            # Make pattern match on order_id only
            tr["args_pattern"] = {"order_id": "ORD-55780"}
    notes.append("L1: Relaxed tool response args_pattern matching for process_refund and create_return_label")

    # L3: Already good ("I need this sorted out")
    c["user_scenario"] = (
        "I ordered a blue backpack (ORD-55780, priced at $45) but received a red "
        "designer suitcase that retails for $120 instead. The other items in my order "
        "are correct. Please issue the refund and arrange the return now."
    )
    notes.append("L3: Added explicit action request")
    return notes


def fix_coref_033(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "My round-trip from Boston to LA was booked under RES-11220. The outbound on "
        "the 15th just got cancelled. Please rebook me now — I can't miss this trip."
    )
    notes.append("L3: Changed from 'What are my options?' to direct rebook request")
    return notes


def fix_coref_034(c):
    notes = []
    # L2: Already well-designed (adjust down vs adjust up = very different)
    # L3: Minor
    c["user_scenario"] = (
        "This same blender is showing $89 on your mobile app but $120 on your website. "
        "I want to buy it at the lower price. Please fix the discrepancy and process "
        "my order ORD-34120 now."
    )
    notes.append("L3: Added order processing request")
    return notes


def fix_coref_035(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "I need both a ticket refund and a baggage fee refund for my cancelled flight. "
        "Both claims are in the system. Please start processing the one with the shorter "
        "deadline now — I can't afford to miss the processing window."
    )
    notes.append("L3: Changed from question to action request with deadline concern")
    return notes


def fix_coref_036(c):
    notes = []
    # L2: Make only one carrier's investigation possible right now
    tr_ord = find_tool_response(c, "get_order_details")
    if tr_ord:
        for item in tr_ord["response"].get("items", []):
            if item.get("carrier") == "FedEx":
                item["tracking_status"] = "investigation_available"
            elif item.get("carrier") == "UPS":
                item["tracking_status"] = "weekend_office_closed"
        notes.append("L2: Made FedEx investigation available now, UPS office closed — forces choice of which package to investigate first")

    # L3: Already has action request
    c["user_scenario"] = (
        "My order ORD-88920 was split into two shipments — one from FedEx and one "
        "from UPS. I opened both boxes at the same time and found a wrong item mixed "
        "in. I can't tell which box it came from. Please investigate the package and "
        "file a claim now — I need the correct item."
    )
    notes.append("L3: Reinforced immediate action request")
    return notes


def fix_coref_037(c):
    notes = []
    # L3: Add urgency
    c["user_scenario"] = (
        "My reservation RES-44770 has business class from NYC to London and economy "
        "from London to Paris. I'm at the check-in counter for the London-Paris leg "
        "now. What's my baggage allowance? Please confirm so I can check my bags."
    )
    notes.append("L3: Added check-in counter urgency")
    return notes


def fix_coref_038(c):
    notes = []
    # Well-designed already. Minor L3.
    c["user_scenario"] = (
        "My order ORD-29440 failed to process with my Visa. I have a Mastercard saved "
        "as backup. Please retry the payment now — this is a limited-time deal and "
        "I don't want to lose it."
    )
    notes.append("L3: Added limited-time deal urgency")
    return notes


def fix_coref_039(c):
    notes = []
    # Already well-designed
    c["user_scenario"] = (
        "The gate agent says I need to gate-check one of my bags — overhead bins are "
        "full. I have my carry-on roller with clothes and toiletries, and my laptop "
        "bag with my work computer and medications. They're about to close the door — "
        "which bag should I check and what should I take out first?"
    )
    notes.append("L3: Added door-closing urgency")
    return notes


def fix_coref_040(c):
    notes = []
    # L1: Remove pre-determined subscription_cancelled from refund response
    tr_refund = find_tool_response(c, "process_refund")
    if tr_refund:
        resp = tr_refund["response"]
        if "subscription_cancelled" in resp:
            resp.pop("subscription_cancelled")
            resp["action"] = "subscription_cancellation_processed"
        notes.append("L1: Removed specific 'subscription_cancelled: SUB-001' from refund response")

    # L3: Add urgency
    c["user_scenario"] = (
        "I accidentally renewed my premium membership early, so now I have my old "
        "subscription running until June 30 and the new one started June 1. "
        "Please cancel the overlap and refund me the prorated amount now."
    )
    notes.append("L3: Added explicit action request")
    return notes


def fix_coref_041(c):
    notes = []
    # L1: MAJOR — Remove complaint counts that disambiguate
    tr_ord = find_tool_response(c, "get_order_details")
    if tr_ord:
        resp = tr_ord["response"]
        if "supplier_complaint_count" in resp:
            del resp["supplier_complaint_count"]
        if "product_line_complaint_count" in resp:
            del resp["product_line_complaint_count"]
        # Add neutral "safety_notes" field that doesn't resolve the RC attachment
        resp["safety_notes"] = "Multiple safety complaints on record this quarter"
        notes.append("L1: Removed supplier/product_line complaint counts; added neutral safety_notes")

    # L2: Ensure different interpretations → different notification scope
    # Add a notify_supplier tool that requires specifying scope
    has_notify_supplier = False
    for t in c.get("tools", []):
        if t.get("function", {}).get("name") == "notify_supplier":
            has_notify_supplier = True
            break
    if not has_notify_supplier:
        supplier_tool = {
            "type": "function",
            "function": {
                "name": "notify_supplier",
                "description": "Send a formal notification to a supplier regarding product quality or safety concerns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The supplier ID"},
                        "scope": {"type": "string", "description": "Scope of notification: 'vendor_wide' or 'product_line'"},
                        "product_ids": {"type": "array", "items": {"type": "string"}, "description": "Specific product IDs if product-line scope"},
                        "message": {"type": "string", "description": "Notification content"}
                    },
                    "required": ["supplier_id", "scope", "message"]
                }
            }
        }
        c["tools"].append(supplier_tool)
        c["stripped_tool_desc"].append({
            "type": "function",
            "function": {
                "name": "notify_supplier",
                "description": "Send a notification to a supplier about quality or safety concerns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier ID"},
                        "scope": {"type": "string", "description": "Notification scope"},
                        "product_ids": {"type": "array", "items": {"type": "string"}, "description": "Product IDs"},
                        "message": {"type": "string", "description": "Content"}
                    },
                    "required": ["supplier_id", "scope", "message"]
                }
            }
        })
        # Add tool response
        c["tool_responses"].append({
            "tool_name": "notify_supplier",
            "args_pattern": {"supplier_id": "*", "scope": "*", "message": "*"},
            "response": {
                "status": "notification_sent",
                "supplier_id": "SUP-4100",
                "notification_id": "SNOTIF-41100"
            }
        })
        notes.append("L2: Added notify_supplier tool with 'scope' parameter to distinguish vendor-wide vs product-line notification")

    # L3: Already has implicit urgency (safety complaint)
    c["user_scenario"] = (
        "I'm reporting a safety issue with the BlendMax 3000 blender from KitchenPro Inc. "
        "The blade guard cracked during normal use and almost caused an injury. I've seen "
        "other people posting about similar problems online. Please notify the supplier "
        "about these safety complaints immediately."
    )
    notes.append("L3: Added injury concern and explicit notification request")
    return notes


def fix_coref_042(c):
    notes = []
    # L2: Search results have codeshare:true and codeshare:false flights.
    # Under interp A (any partner flight), both are options.
    # Under interp B (only codeshare flights), only codeshare ones qualify.
    # Already distinguishable. Good.

    # L3: Add urgency
    c["user_scenario"] = (
        "My direct flight to Tokyo was cancelled. I know your airline has partnerships "
        "with other carriers. Please rebook me on a partner airline's flight now — "
        "I have a business meeting tomorrow in Tokyo that I cannot miss."
    )
    notes.append("L3: Added business meeting deadline")
    return notes


def fix_coref_043(c):
    notes = []
    # L3: Change from question to action request
    c["user_scenario"] = (
        "I bought a limited-edition candle from your holiday gift collection during "
        "the clearance event. I'd like to return it. Please process the return now — "
        "I'm past the regular window but the clearance terms should apply."
    )
    notes.append("L3: Changed from question to action request; added window concern to force policy interpretation")
    return notes


def fix_coref_044(c):
    notes = []
    # L3: Make scenario neutral (not biased toward agency)
    c["user_scenario"] = (
        "Our company's travel coordinator at TravelMax arranged flights for our team. "
        "There's a scheduling conflict with the departure — our offsite meeting got "
        "moved. Please contact the right party and get the itinerary changed today."
    )
    notes.append("L3: Neutralized scenario (removed bias toward agency), added same-day deadline")
    return notes


def fix_coref_045(c):
    notes = []
    # L1: Soften vendor_flags to not directly label "flagged for compliance"
    tr_ord = find_tool_response(c, "get_order_details")
    if tr_ord:
        resp = tr_ord["response"]
        if "vendor_flags" in resp:
            for vid, flags in resp["vendor_flags"].items():
                if "reason" in flags:
                    flags["reason"] = "under_review"
                flags["status"] = "review_pending"
            notes.append("L1: Softened vendor_flags from 'flagged/compliance_violations' to 'review_pending/under_review'")

    # L3: Already has urgency ("Can you process this quickly?")
    c["user_scenario"] = (
        "I need to return items from order ORD-81045. I heard the brand might be "
        "having some issues with their products. Please expedite this return and "
        "process it now."
    )
    notes.append("L3: Added explicit expedite and process request")
    return notes


def fix_coref_046(c):
    notes = []
    # L2: Already well-designed (fee waiver for leader only vs all)
    # L3: Already has urgency
    c["user_scenario"] = (
        "I'm the coordinator for a group of 8 heading to a conference. The terminal "
        "was closed last night and we were all stuck at the airport overnight. I need "
        "to rebook everyone now — please waive the rebooking fees and get us on the "
        "next available flights."
    )
    notes.append("L3: Added explicit fee waiver and rebook request")
    return notes


def fix_coref_047(c):
    notes = []
    # L3: Add action request
    c["user_scenario"] = (
        "I bought a home theater bundle and had a technician come look at it. There "
        "are some issues — the subwoofer isn't working properly. Please arrange a "
        "replacement now, I have guests coming this weekend."
    )
    notes.append("L3: Added specific component mention and weekend deadline")
    return notes


def fix_coref_048(c):
    notes = []
    # Already well-designed. Minor L3.
    c["user_scenario"] = (
        "My incoming flight is delayed and I have a tight connection in Dallas. My "
        "connecting flight to LA leaves 25 minutes after my new arrival time. Please "
        "notify whoever needs to know and hold the connection if possible — I can't "
        "miss this flight."
    )
    notes.append("L3: Added explicit notify and hold request")
    return notes


def fix_coref_049(c):
    notes = []
    # L2: Change scenario so purchase happens AFTER Friday to make interpretations diverge
    # Interp A (enrollment period ends Friday) → bonus applies (already enrolled)
    # Interp B (purchase must happen by Friday) → bonus expired
    c["user_scenario"] = (
        "I signed up for your loyalty program during the spring promotion. I want to "
        "make a purchase and use my loyalty bonus. The promo was supposed to end last "
        "Friday but I couldn't shop until today (Monday). Does my bonus still apply? "
        "Please apply it and process my order now."
    )
    notes.append("L2: Changed purchase date to after Friday — now interp A (enrollment-based) gives bonus, interp B (purchase deadline) denies it")
    notes.append("L3: Added explicit apply and process request")

    # Update tool responses to reflect Monday date
    for tr in c.get("tool_responses", []):
        if tr["tool_name"] == "get_user_details":
            resp = tr["response"]
            if "loyalty" not in resp:
                resp["loyalty"] = {}
            resp["loyalty"]["enrolled_during"] = "spring_promotion"
            resp["loyalty"]["enrollment_date"] = "2026-04-15"
            resp["loyalty"]["promotion_end_date"] = "2026-05-16"
            resp["loyalty"]["current_date"] = "2026-05-19"
    notes.append("L1: Added loyalty dates showing enrollment during promo (ended Friday), purchase on Monday")
    return notes


def fix_coref_050(c):
    notes = []
    # L1: Remove ticket_purchaser field that directly resolves ambiguity
    tr_res = find_tool_response(c, "get_reservation_details")
    if tr_res:
        for pax in tr_res["response"].get("passengers", []):
            if "ticket_purchaser" in pax:
                del pax["ticket_purchaser"]
        notes.append("L1: Removed 'ticket_purchaser' field from passenger details")

    # L3: Add urgency
    c["user_scenario"] = (
        "My partner and I are on reservation RES-50050. One of us is in business "
        "class and the other is in economy. We'd like to sit together — please "
        "process the upgrade now so we can board together."
    )
    notes.append("L3: Added boarding urgency")
    return notes


# ── Main ────────────────────────────────────────────────────────────────────

FIX_FUNCTIONS = {
    "coref_001": fix_coref_001,
    "coref_002": fix_coref_002,
    "coref_003": fix_coref_003,
    "coref_004": fix_coref_004,
    "coref_005": fix_coref_005,
    "coref_006": fix_coref_006,
    "coref_007": fix_coref_007,
    "coref_008": fix_coref_008,
    "coref_009": fix_coref_009,
    "coref_010": fix_coref_010,
    "coref_011": fix_coref_011,
    "coref_012": fix_coref_012,
    "coref_013": fix_coref_013,
    "coref_014": fix_coref_014,
    "coref_015": fix_coref_015,
    "coref_016": fix_coref_016,
    "coref_017": fix_coref_017,
    "coref_018": fix_coref_018,
    "coref_019": fix_coref_019,
    "coref_020": fix_coref_020,
    "coref_021": fix_coref_021,
    "coref_022": fix_coref_022,
    "coref_023": fix_coref_023,
    "coref_024": fix_coref_024,
    "coref_025": fix_coref_025,
    "coref_026": fix_coref_026,
    "coref_027": fix_coref_027,
    "coref_028": fix_coref_028,
    "coref_029": fix_coref_029,
    "coref_030": fix_coref_030,
    "coref_031": fix_coref_031,
    "coref_032": fix_coref_032,
    "coref_033": fix_coref_033,
    "coref_034": fix_coref_034,
    "coref_035": fix_coref_035,
    "coref_036": fix_coref_036,
    "coref_037": fix_coref_037,
    "coref_038": fix_coref_038,
    "coref_039": fix_coref_039,
    "coref_040": fix_coref_040,
    "coref_041": fix_coref_041,
    "coref_042": fix_coref_042,
    "coref_043": fix_coref_043,
    "coref_044": fix_coref_044,
    "coref_045": fix_coref_045,
    "coref_046": fix_coref_046,
    "coref_047": fix_coref_047,
    "coref_048": fix_coref_048,
    "coref_049": fix_coref_049,
    "coref_050": fix_coref_050,
}


def main():
    with open(INPUT) as f:
        clauses = json.load(f)

    fixed = []
    summary = {"L1": 0, "L2": 0, "L3": 0, "total_fixes": 0}

    for c in clauses:
        c = copy.deepcopy(c)
        cid = c["clause_id"]

        # Add subtype
        c["coref_subtype"] = SUBTYPE_MAP.get(cid, "unknown")

        # Apply fixes
        fix_fn = FIX_FUNCTIONS.get(cid)
        if fix_fn:
            notes = fix_fn(c)
            c["_fix_notes"] = notes
            for n in notes:
                if n.startswith("L1"):
                    summary["L1"] += 1
                elif n.startswith("L2"):
                    summary["L2"] += 1
                elif n.startswith("L3"):
                    summary["L3"] += 1
            summary["total_fixes"] += len(notes)
        else:
            c["_fix_notes"] = ["No specific fixes needed"]

        fixed.append(c)

    with open(OUTPUT, "w") as f:
        json.dump(fixed, f, indent=2, ensure_ascii=False)

    print(f"Fixed {len(fixed)} clauses → {OUTPUT}")
    print(f"Fix summary: L1={summary['L1']} tool-response fixes, L2={summary['L2']} distinguishability fixes, L3={summary['L3']} decision-forcing fixes")
    print(f"Total fix notes: {summary['total_fixes']}")

    # Per-subtype counts
    subtype_counts = {}
    for c in fixed:
        st = c["coref_subtype"]
        subtype_counts[st] = subtype_counts.get(st, 0) + 1
    print(f"Subtype distribution: {json.dumps(subtype_counts)}")

    # Show major fixes
    print("\nMajor fixes (L1 tool response sanitization):")
    for c in fixed:
        l1_notes = [n for n in c["_fix_notes"] if n.startswith("L1")]
        if l1_notes:
            print(f"  {c['clause_id']}: {'; '.join(l1_notes)}")


if __name__ == "__main__":
    main()
