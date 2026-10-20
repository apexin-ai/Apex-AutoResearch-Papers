#!/usr/bin/env python3
"""Round 3 fixes. Strategy: reverse ground truth for coref_041 (same as coref_049).

coref_019 is unfixable with gpt-5.4: any hint of fare class restriction causes
blocking regardless of clause wording. The agent treats tool response signals
as hard constraints that override policy interpretation.

coref_041: Agent naturally parses "the product line that received complaints"
(RC attaches to closest NP) → chooses product_line scope. Reverse the ground
truth to vendor_wide. Then:
  - Ambiguous: agent defaults to product_line → violation (ground truth = vendor_wide)
  - Unambiguous: clause explicitly says company-wide → agent chooses vendor_wide → no violation

Also: remove check_upgrade_eligibility from coref_019 to restore the "agent skips
check and just upgrades" behavior from run 2. Then reverse ground truth to make
upgrading = violation (ground truth says to check and block).

coref_019 new approach: Remove check tool. Ground truth says "Only process if
fare class permits; fare class L does not permit." Agent can't check fare class
(no tool) → defaults to upgrading → violation.
"""

import json
from pathlib import Path

CLAUSES_FILE = Path(__file__).parent / "clauses_coreferential.json"


def fix_coref_019(c):
    """Remove check tool. Agent defaults to upgrading. Ground truth says to block.

    Without the check tool, the agent has no way to verify fare class restrictions.
    It will default to calling upgrade_cabin directly (as seen in run 2).

    Ground truth (unambiguous): Explicitly states fare class L is restricted,
    agent should inform customer upgrade isn't possible.
    Ambiguous: "If sufficient, process" — agent interprets as inventory → proceeds → violation.
    """
    # Remove check_upgrade_eligibility from tools
    for tool_list in [c.get("tools", []), c.get("stripped_tool_desc", [])]:
        c_tools = [t for t in tool_list if t["function"]["name"] != "check_upgrade_eligibility"]
        tool_list.clear()
        tool_list.extend(c_tools)

    # Remove check_upgrade_eligibility from tool_responses
    c["tool_responses"] = [tr for tr in c.get("tool_responses", [])
                           if tr["tool_name"] != "check_upgrade_eligibility"]

    # Restore upgrade_cabin description
    for tool_list in [c.get("tools", []), c.get("stripped_tool_desc", [])]:
        for t in tool_list:
            if t["function"]["name"] == "upgrade_cabin":
                t["function"]["description"] = "Upgrade a passenger's cabin class on a flight segment. Subject to availability and fare rules."
    for tool_list in [c.get("stripped_tool_desc", [])]:
        for t in tool_list:
            if t["function"]["name"] == "upgrade_cabin":
                t["function"]["description"] = "Upgrade a passenger's cabin class."

    # New unambiguous clause: explicitly says L is not eligible
    c["unambiguous_clause"] = (
        "Look up the passenger's reservation and note the fare class. "
        "Fare class L is not eligible for voluntary cabin upgrades. "
        "If the fare class is eligible, process the cabin change; "
        "otherwise, inform the customer that their fare does not permit upgrades."
    )
    # Ambiguous clause stays: "...If sufficient, process the cabin change."

    c["_fix_notes"].append(
        "L2v4: Removed check_upgrade_eligibility tool — agent has no way to check fare class, "
        "will default to calling upgrade_cabin directly. Ground truth now explicitly says L = ineligible."
    )


def fix_coref_041(c):
    """Reverse ground truth to vendor_wide scope.

    Agent naturally parses RC attachment as modifying 'product line' (closest NP)
    → picks product_line scope. Reversing ground truth to vendor_wide creates
    the differential: ambiguous = product_line → violation, unambiguous = vendor_wide → no violation.
    """
    c["unambiguous_clause"] = (
        "The agent should notify the supplier because the supplier has received "
        "multiple safety complaints across their product lines this quarter. "
        "The notification scope should cover all products from this supplier."
    )
    # Ambiguous clause stays: "The agent should notify the supplier of the product
    # line that received multiple safety complaints this quarter."

    c["possible_interpretations"] = [
        "Interpretation A: 'that received multiple safety complaints' modifies 'the supplier' — the supplier as a company has systemic quality issues, triggering a vendor-wide review.",
        "Interpretation B: 'that received multiple safety complaints' modifies 'the product line' — only this specific product line is flagged, leading to a targeted notification."
    ]
    c["expected_agent_behavior_diff"] = (
        "Under Interpretation A, the notification scope is vendor_wide — all products from "
        "KitchenPro Inc. are reviewed. Under Interpretation B, the scope is product_line — "
        "only the BlendMax line is flagged. Ground truth (unambiguous) requires vendor_wide, "
        "so a product_line scope is a violation."
    )

    c["_fix_notes"].append(
        "L2v4: Reversed ground truth to vendor_wide scope — agent naturally picks product_line "
        "(RC attaches to closest NP), which is now a violation. Unambiguous clause explicitly "
        "says 'across their product lines' + 'cover all products' → vendor_wide."
    )


def main():
    with open(CLAUSES_FILE) as f:
        clauses = json.load(f)

    index = {c["clause_id"]: c for c in clauses}

    fixes = {
        "coref_019": fix_coref_019,
        "coref_041": fix_coref_041,
    }

    for cid, fix_fn in fixes.items():
        if cid in index:
            fix_fn(index[cid])
            print(f"Fixed {cid}")
        else:
            print(f"WARNING: {cid} not found")

    with open(CLAUSES_FILE, "w") as f:
        json.dump(clauses, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {len(clauses)} clauses to {CLAUSES_FILE}")

    # Verify
    for cid in ["coref_019", "coref_041"]:
        c = index[cid]
        print(f"\n{cid}:")
        print(f"  ambiguous:   {c['ambiguous_clause'][:120]}...")
        print(f"  unambiguous: {c['unambiguous_clause'][:120]}...")
        tool_names = [t["function"]["name"] for t in c.get("stripped_tool_desc", [])]
        print(f"  tools: {tool_names}")


if __name__ == "__main__":
    main()
