#!/usr/bin/env python3
"""
SOPBench Negative Task Audit
- Parses all 4 domain task files
- Extracts negative tasks (action_should_succeed=False)
- Maps constraints from constraint trees
- Cross-matches with clause pairs
"""

import json
import os
from collections import defaultdict

SOPBENCH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/sopbench"
ARTIFACTS = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"

DOMAINS = ["healthcare", "bank", "hotel", "library"]


def extract_constraint_names(tree):
    """Recursively extract constraint names from a constraint tree."""
    if tree is None:
        return []
    if not isinstance(tree, list):
        return []
    if len(tree) == 0:
        return []

    # "single" leaf: ["single", "constraint_name", {params}]
    if tree[0] == "single":
        return [tree[1]]

    # "chain": ["chain", [subtree1, subtree2, ...]]
    if tree[0] == "chain":
        names = []
        for sub in tree[1]:
            names.extend(extract_constraint_names(sub))
        return names

    # "and"/"or": ["and"/"or", [subtree1, subtree2, ...]]
    if tree[0] in ("and", "or"):
        names = []
        if isinstance(tree[1], list):
            for sub in tree[1]:
                names.extend(extract_constraint_names(sub))
        return names

    # Could be a leaf without "single" prefix: ["constraint_name", {params}]
    if isinstance(tree[0], str) and len(tree) >= 2 and isinstance(tree[-1], dict):
        return [tree[0]]

    # Recurse into sublists
    names = []
    for item in tree:
        if isinstance(item, list):
            names.extend(extract_constraint_names(item))
    return names


def analyze_domain(domain):
    """Analyze a single domain's task file."""
    path = os.path.join(SOPBENCH, f"data/{domain}_tasks.json")
    with open(path) as f:
        data = json.load(f)

    results = {}
    for action_name, task_list in data.items():
        total = len(task_list)
        negative_tasks = []
        for idx, task in enumerate(task_list):
            if not task.get("action_should_succeed", True):
                constraints = extract_constraint_names(task.get("constraints", []))
                constraints_orig = extract_constraint_names(task.get("constraints_original", []))
                negative_tasks.append({
                    "idx": idx,
                    "constraints": constraints,
                    "constraints_original": constraints_orig,
                    "has_user_prompt": bool(task.get("user_prompt")),
                })

        constraint_dist = defaultdict(int)
        for nt in negative_tasks:
            for c in nt["constraints"]:
                constraint_dist[c] += 1

        constraint_orig_dist = defaultdict(int)
        for nt in negative_tasks:
            for c in nt["constraints_original"]:
                constraint_orig_dist[c] += 1

        results[action_name] = {
            "total": total,
            "negative_count": len(negative_tasks),
            "negative_tasks": negative_tasks,
            "constraint_dist": dict(constraint_dist),
            "constraint_orig_dist": dict(constraint_orig_dist),
        }

    return results


def find_binding_constraints(task_data):
    """
    For negative tasks, identify which constraints are 'binding' (cause the failure).
    Compare constraints vs constraints_original — constraints added in the full version
    but not in original may be the ones that are manipulated to fail.
    Actually, for negative tasks the constraint tree values determine which fail.
    We need to look at which constraints differ between the task's env and the passing case.

    Simpler heuristic: constraints present in constraints but NOT in constraints_original
    are the 'customized' ones that may be set to fail.
    """
    constraints = set(task_data["constraints"])
    constraints_orig = set(task_data["constraints_original"])
    added = constraints - constraints_orig
    return added if added else constraints  # fallback to all if no diff


def main():
    # Step 1: Per-domain statistics
    all_domain_results = {}
    print("=" * 80)
    print("STEP 1: PER-DOMAIN NEGATIVE TASK STATISTICS")
    print("=" * 80)

    for domain in DOMAINS:
        results = analyze_domain(domain)
        all_domain_results[domain] = results
        print(f"\nDomain: {domain}")
        print("-" * 40)
        for action, info in sorted(results.items()):
            print(f"  Action: {action}")
            print(f"    Total tasks: {info['total']}, Negative: {info['negative_count']}")
            if info['constraint_dist']:
                print(f"    Constraint distribution (negative tasks):")
                for c, n in sorted(info['constraint_dist'].items()):
                    orig_n = info['constraint_orig_dist'].get(c, 0)
                    marker = "" if orig_n == n else f" (orig: {orig_n})"
                    print(f"      {c}: {n} tasks{marker}")
            if info['negative_count'] > 0:
                for nt in info['negative_tasks']:
                    binding = find_binding_constraints(nt)
                    added = set(nt["constraints"]) - set(nt["constraints_original"])
                    if added:
                        print(f"    Task[{nt['idx']}] added constraints: {added}")

    # Step 2: Cross-match with clause pairs
    print(f"\n{'=' * 80}")
    print("STEP 2: CLAUSE PAIR × NEGATIVE TASK CROSS-MATCH")
    print(f"{'=' * 80}")

    pairs_path = os.path.join(ARTIFACTS, "sopbench_clause_pairs.json")
    with open(pairs_path) as f:
        clause_pairs = json.load(f)

    cross_match = []
    for pair in clause_pairs:
        domain = pair["domain"]
        constraint_name = pair["constraint_name"]
        applicable_actions = pair.get("applicable_actions", [])

        neg_count = 0
        neg_task_indices = []

        if domain in all_domain_results:
            for action in applicable_actions:
                if action in all_domain_results[domain]:
                    action_info = all_domain_results[domain][action]
                    for nt in action_info["negative_tasks"]:
                        if constraint_name in nt["constraints"]:
                            neg_count += 1
                            neg_task_indices.append((action, nt["idx"]))

        # Also check: is this constraint the "binding" one (added beyond original)?
        binding_count = 0
        binding_indices = []
        if domain in all_domain_results:
            for action in applicable_actions:
                if action in all_domain_results[domain]:
                    action_info = all_domain_results[domain][action]
                    for nt in action_info["negative_tasks"]:
                        added = set(nt["constraints"]) - set(nt["constraints_original"])
                        if constraint_name in added:
                            binding_count += 1
                            binding_indices.append((action, nt["idx"]))

        if neg_count >= 3:
            status = "✓"
        elif neg_count >= 1:
            status = "⚠"
        else:
            status = "✗"

        entry = {
            "pair_id": pair["pair_id"],
            "domain": domain,
            "constraint_name": constraint_name,
            "ambiguity_type": pair["ambiguity_type"],
            "applicable_actions": applicable_actions,
            "neg_task_count": neg_count,
            "neg_task_indices": neg_task_indices,
            "binding_count": binding_count,
            "binding_indices": binding_indices,
            "status": status,
        }
        cross_match.append(entry)

        print(f"  {status} {pair['pair_id']:20s} | {constraint_name:40s} | neg={neg_count:2d} binding={binding_count:2d} | actions={applicable_actions}")

    # Summary
    good = sum(1 for e in cross_match if e["status"] == "✓")
    marginal = sum(1 for e in cross_match if e["status"] == "⚠")
    missing = sum(1 for e in cross_match if e["status"] == "✗")
    print(f"\n  Summary: ✓ ≥3 tasks: {good} | ⚠ 1-2 tasks: {marginal} | ✗ 0 tasks: {missing}")

    # Save cross-match for later use
    cross_path = os.path.join(ARTIFACTS, "sopbench_negative_cross_match.json")
    with open(cross_path, "w") as f:
        json.dump(cross_match, f, indent=2)
    print(f"\n  Cross-match saved to: {cross_path}")

    # Print pairs suitable for Phase 2B pilot (≥3 neg tasks, diverse ambiguity types)
    print(f"\n{'=' * 80}")
    print("PHASE 2B PILOT CANDIDATES (≥3 negative tasks)")
    print(f"{'=' * 80}")

    by_type = defaultdict(list)
    for e in cross_match:
        if e["neg_task_count"] >= 3:
            by_type[e["ambiguity_type"]].append(e)

    for amb_type, entries in sorted(by_type.items()):
        print(f"\n  {amb_type}:")
        for e in entries:
            print(f"    {e['pair_id']:20s} | {e['constraint_name']:40s} | neg={e['neg_task_count']} binding={e['binding_count']}")
            for action, idx in e['neg_task_indices'][:3]:
                print(f"      -> {action}[{idx}]")

    # Also show binding-only candidates
    print(f"\n{'=' * 80}")
    print("BINDING-SPECIFIC CANDIDATES (constraint added beyond original)")
    print(f"{'=' * 80}")

    binding_candidates = [e for e in cross_match if e["binding_count"] >= 1]
    for e in sorted(binding_candidates, key=lambda x: -x["binding_count"]):
        print(f"  {e['pair_id']:20s} | {e['constraint_name']:40s} | binding={e['binding_count']} | {e['binding_indices']}")


if __name__ == "__main__":
    main()
