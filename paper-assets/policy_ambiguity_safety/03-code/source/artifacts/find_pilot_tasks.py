#!/usr/bin/env python3
"""Find the best negative tasks for Phase 2B pilot.
For each selected pair, find negative tasks where the target constraint
appears in constraints_original (the tree that gets verbalized to the agent).
"""
import json
import os
import sys

SOPBENCH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/sopbench"

def extract_constraint_names(tree):
    if tree is None or not isinstance(tree, list) or len(tree) == 0:
        return []
    if tree[0] == "single":
        return [tree[1]]
    if tree[0] in ("chain", "and", "or") and isinstance(tree[1], list):
        names = []
        for sub in tree[1]:
            names.extend(extract_constraint_names(sub))
        return names
    if isinstance(tree[0], str) and len(tree) >= 2 and isinstance(tree[-1], dict):
        return [tree[0]]
    names = []
    for item in tree:
        if isinstance(item, list):
            names.extend(extract_constraint_names(item))
    return names

PILOT_PAIRS = [
    {"pair_id": "HC02_incomp", "domain": "healthcare", "constraint": "claim_within_limits", "action": "submit_claim"},
    {"pair_id": "BK02_lexical", "domain": "bank", "constraint": "get_loan_owed_balance_restr", "action": "get_loan"},
    {"pair_id": "HC09_coref", "domain": "healthcare", "constraint": "provider_covers_policy", "action": "schedule_appointment"},
]

for pair in PILOT_PAIRS:
    path = os.path.join(SOPBENCH, f"data/{pair['domain']}_tasks.json")
    with open(path) as f:
        data = json.load(f)

    task_list = data[pair["action"]]
    print(f"\n{'='*60}")
    print(f"{pair['pair_id']} | {pair['constraint']} | {pair['action']}")
    print(f"{'='*60}")

    for idx, task in enumerate(task_list):
        if not task.get("action_should_succeed", True):
            orig_constraints = extract_constraint_names(task.get("constraints_original", []))
            full_constraints = extract_constraint_names(task.get("constraints", []))
            has_in_orig = pair["constraint"] in orig_constraints
            has_in_full = pair["constraint"] in full_constraints

            # Count how many non-internal constraints are in original
            non_internal_orig = [c for c in orig_constraints if not c.startswith("internal_")]

            print(f"  Task[{idx}]: in_orig={has_in_orig} in_full={has_in_full}")
            print(f"    orig constraints: {orig_constraints}")
            print(f"    non-internal orig: {non_internal_orig}")
            if has_in_orig:
                print(f"    *** GOOD CANDIDATE (target in verbalized constraints)")
