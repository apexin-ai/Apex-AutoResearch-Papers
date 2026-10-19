#!/usr/bin/env python3
"""Rule-based error classifier for ALFWorld failure trajectories.

Pure rule-based classification (no LLM) using 10 rules in priority order,
mapping to three error types: action, verification, planning.

Output JSONL format is compatible with classify_errors.py for comparison
via compare_classifiers.py.

Rules (by priority):
  1. pcb            → verification  (premature completion)
  2. wrong_object   → action        (wrong object selected)
  3. wrong_instance → action        (correct type, wrong instance number)
  4. wrong_receptacle → action      (wrong container)
  5. wrong_verb     → action        (wrong action verb)
  6. ignored_failure → verification (ignored "Nothing happens")
  7. repeated_action → verification (same action ≥3 times)
  8. missing_subtask → planning     (skipped required step)
  9. inefficient_search → planning  (revisited locations)
 10. default        → planning      (fallback)

Usage:
  python src/classify_errors_rulebased.py \
    --failure_dir data/failures/iter1 \
    --expert_file eto_repo/data/alfworld_sft.json \
    --output_file outputs/classified_errors_rulebased.jsonl
"""

import argparse
import json
import logging
import re
from collections import Counter
from pathlib import Path

logger = logging.getLogger("classify_rulebased")

ERROR_TYPES = ["action", "verification", "planning"]

# Task types that require intermediate processing steps
PROCESSING_TASKS = {
    "pick_clean_then_place": "clean",
    "pick_heat_then_place": "heat",
    "pick_cool_then_place": "cool",
}


# ---------------------------------------------------------------------------
# Game file normalization
# ---------------------------------------------------------------------------

def normalize_game_file(game_file: str) -> str:
    """Extract <task_dir>/<trial_dir> as matching key."""
    gf = game_file.rstrip("/")
    if gf.endswith("/game.tw-pddl"):
        gf = gf[: -len("/game.tw-pddl")]
    parts = gf.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else gf


# ---------------------------------------------------------------------------
# Message helpers
# ---------------------------------------------------------------------------

def _role(msg: dict) -> str:
    return msg.get("role") or {"human": "user", "gpt": "assistant"}.get(msg.get("from", ""), "")


def _content(msg: dict) -> str:
    return msg.get("content") or msg.get("value", "")


# ---------------------------------------------------------------------------
# Step extraction
# ---------------------------------------------------------------------------

def find_task_start(conversations: list) -> int:
    """Index of first action step after the actual task description."""
    task_desc_idx = -1
    for i, msg in enumerate(conversations):
        if _role(msg) in ("user", "human") and "Your task is to:" in _content(msg):
            task_desc_idx = i

    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0
    for i in range(search_from, len(conversations)):
        if _role(conversations[i]) in ("assistant", "gpt") and "Action:" in _content(conversations[i]):
            return i
    return len(conversations)


def extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:
    """Extract (action_msg, obs_msg|None) pairs from start_idx onward."""
    steps = []
    i = start_idx
    while i < len(conversations):
        if _role(conversations[i]) in ("assistant", "gpt"):
            action = conversations[i]
            obs = None
            if i + 1 < len(conversations) and _role(conversations[i + 1]) in ("user", "human"):
                obs = conversations[i + 1]
                i += 2
            else:
                i += 1
            steps.append((action, obs))
        else:
            i += 1
    return steps


def extract_action_text(content: str) -> str:
    """Extract normalized 'Action: ...' line from a step message."""
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.lower().startswith("action:"):
            return " ".join(stripped[len("action:"):].split()).lower()
    return " ".join(content.split()).lower()


def extract_action_verb(action_text: str) -> str:
    """Extract the verb from an action string (e.g., 'go to shelf 1' → 'go to')."""
    # ALFWorld verbs: go to, take, put, open, close, use, clean, heat, cool, examine, look
    for verb in ["go to", "take", "put", "open", "close", "use", "clean", "heat", "cool", "examine", "look"]:
        if action_text.startswith(verb):
            return verb
    return action_text.split()[0] if action_text.split() else ""


def extract_object_from_action(action_text: str) -> str:
    """Extract the target object/receptacle from an action string."""
    verb = extract_action_verb(action_text)
    rest = action_text[len(verb):].strip()
    # Remove "from ..." or "with ..." suffix
    rest = re.sub(r"\s+(from|with|in|on)\s+.*$", "", rest)
    return rest.strip()


def extract_object_type(obj_str: str) -> str:
    """Extract the base type without instance number (e.g., 'shelf 1' → 'shelf')."""
    return re.sub(r"\s+\d+$", "", obj_str).strip()


def count_expert_action_steps(expert: dict) -> int:
    """Count gpt turns with 'Action:' in expert trajectory."""
    return sum(
        1
        for m in expert["conversations"]
        if m["from"] == "gpt" and "Action:" in m.get("value", "")
    )


# ---------------------------------------------------------------------------
# Divergence computation
# ---------------------------------------------------------------------------

def find_divergence_point(
    expert_steps: list[tuple[dict, dict | None]],
    fail_steps: list[tuple[dict, dict | None]],
) -> int:
    """Find the first step where expert and failure trajectories diverge."""
    min_len = min(len(expert_steps), len(fail_steps))
    for i in range(min_len):
        ea = extract_action_text(_content(expert_steps[i][0]))
        fa = extract_action_text(_content(fail_steps[i][0]))
        if ea != fa:
            return i
    return min_len


# ---------------------------------------------------------------------------
# Task type detection
# ---------------------------------------------------------------------------

def get_task_type(game_file: str) -> str:
    """Infer task type from game_file path."""
    for key in PROCESSING_TASKS:
        if f"/{key}" in game_file or game_file.startswith(key):
            return key
    if "/pick_and_place" in game_file:
        return "pick_and_place"
    if "/look_at_obj" in game_file:
        return "look_at_obj"
    if "/pick_two_obj" in game_file:
        return "pick_two_obj"
    return "unknown"


def get_required_processing_verb(task_type: str) -> str | None:
    """Return the required processing verb for a task type, or None."""
    return PROCESSING_TASKS.get(task_type)


# ---------------------------------------------------------------------------
# 10 Classification Rules
# ---------------------------------------------------------------------------

def rule_pcb(
    fail_steps: list[tuple[dict, dict | None]],
    expert_steps: list[tuple[dict, dict | None]],
    **kwargs,
) -> dict | None:
    """Rule 1: Premature Completion Bug → verification.

    Last action is a completion action (close/put) but expert has more steps.
    """
    if not fail_steps or not expert_steps:
        return None

    last_action = extract_action_text(_content(fail_steps[-1][0]))
    pcb_verbs = ("close", "put", "use")
    has_completion = any(last_action.startswith(v) for v in pcb_verbs)
    expert_has_more = len(expert_steps) > len(fail_steps)

    if has_completion and expert_has_more:
        return {
            "error_type": "verification",
            "rule_matched": "pcb",
            "reasoning": f"Agent prematurely completed with '{last_action}' but expert has "
                         f"{len(expert_steps) - len(fail_steps)} more steps remaining.",
        }
    return None


def rule_wrong_object(
    fail_steps: list[tuple[dict, dict | None]],
    expert_steps: list[tuple[dict, dict | None]],
    divergence: int,
    **kwargs,
) -> dict | None:
    """Rule 2: Wrong object selected → action.

    At divergence point, the verb is the same but the object is different.
    """
    if divergence >= len(fail_steps) or divergence >= len(expert_steps):
        return None

    fa = extract_action_text(_content(fail_steps[divergence][0]))
    ea = extract_action_text(_content(expert_steps[divergence][0]))

    fv = extract_action_verb(fa)
    ev = extract_action_verb(ea)

    if fv != ev:
        return None

    # Same verb — check if objects differ
    fo = extract_object_from_action(fa)
    eo = extract_object_from_action(ea)

    if fo == eo:
        return None

    # Check if it's the same type but different instance (→ wrong_instance rule)
    ft = extract_object_type(fo)
    et = extract_object_type(eo)
    if ft == et:
        return None  # Let wrong_instance rule handle it

    if fv in ("take", "use", "examine"):
        return {
            "error_type": "action",
            "rule_matched": "wrong_object",
            "reasoning": f"Agent selected '{fo}' instead of '{eo}' at step {divergence + 1}. "
                         f"Same action verb '{fv}' but wrong target object.",
        }
    return None


def rule_wrong_instance(
    fail_steps: list[tuple[dict, dict | None]],
    expert_steps: list[tuple[dict, dict | None]],
    divergence: int,
    **kwargs,
) -> dict | None:
    """Rule 3: Correct object type but wrong instance number → action.

    E.g., 'drawer 1' vs 'drawer 3'.
    """
    if divergence >= len(fail_steps) or divergence >= len(expert_steps):
        return None

    fa = extract_action_text(_content(fail_steps[divergence][0]))
    ea = extract_action_text(_content(expert_steps[divergence][0]))

    fv = extract_action_verb(fa)
    ev = extract_action_verb(ea)
    if fv != ev:
        return None

    fo = extract_object_from_action(fa)
    eo = extract_object_from_action(ea)
    ft = extract_object_type(fo)
    et = extract_object_type(eo)

    if ft == et and fo != eo:
        return {
            "error_type": "action",
            "rule_matched": "wrong_instance",
            "reasoning": f"Agent went to '{fo}' instead of '{eo}' at step {divergence + 1}. "
                         f"Correct type '{ft}' but wrong instance number.",
        }
    return None


def rule_wrong_receptacle(
    fail_steps: list[tuple[dict, dict | None]],
    expert_steps: list[tuple[dict, dict | None]],
    divergence: int,
    **kwargs,
) -> dict | None:
    """Rule 4: Wrong receptacle → action.

    Agent goes to or places in the wrong container.
    """
    if divergence >= len(fail_steps) or divergence >= len(expert_steps):
        return None

    fa = extract_action_text(_content(fail_steps[divergence][0]))
    ea = extract_action_text(_content(expert_steps[divergence][0]))

    fv = extract_action_verb(fa)
    ev = extract_action_verb(ea)

    # Only applies to navigation/placement verbs
    if fv not in ("go to", "put"):
        return None
    if fv != ev:
        return None

    fo = extract_object_from_action(fa)
    eo = extract_object_from_action(ea)
    if fo == eo:
        return None

    ft = extract_object_type(fo)
    et = extract_object_type(eo)

    if ft != et:
        # Different receptacle type — could be planning error, but we classify as action
        # if the overall strategy is on track (same verb, just wrong target)
        return {
            "error_type": "action",
            "rule_matched": "wrong_receptacle",
            "reasoning": f"Agent targeted receptacle '{fo}' instead of '{eo}' at step {divergence + 1}. "
                         f"Different receptacle type '{ft}' vs '{et}'.",
        }
    return None


def rule_wrong_verb(
    fail_steps: list[tuple[dict, dict | None]],
    expert_steps: list[tuple[dict, dict | None]],
    divergence: int,
    **kwargs,
) -> dict | None:
    """Rule 5: Wrong action verb → action.

    Agent uses the wrong verb (e.g., 'take' instead of 'open').
    """
    if divergence >= len(fail_steps) or divergence >= len(expert_steps):
        return None

    fa = extract_action_text(_content(fail_steps[divergence][0]))
    ea = extract_action_text(_content(expert_steps[divergence][0]))

    fv = extract_action_verb(fa)
    ev = extract_action_verb(ea)

    if fv != ev:
        return {
            "error_type": "action",
            "rule_matched": "wrong_verb",
            "reasoning": f"Agent used verb '{fv}' instead of '{ev}' at step {divergence + 1}.",
        }
    return None


def rule_ignored_failure(
    fail_steps: list[tuple[dict, dict | None]],
    **kwargs,
) -> dict | None:
    """Rule 6: Ignored environment failure signal → verification.

    Agent continues after receiving 'Nothing happens' without correcting.
    """
    for i, (action, obs) in enumerate(fail_steps):
        if obs is None:
            continue
        obs_text = _content(obs).strip().lower()
        if "nothing happens" in obs_text:
            # Check if next action is different (tried to correct) or same (ignored)
            if i + 1 < len(fail_steps):
                current_action = extract_action_text(_content(action))
                next_action = extract_action_text(_content(fail_steps[i + 1][0]))
                # If next action is completely unrelated (not a retry or correction),
                # the agent ignored the failure
                if current_action != next_action and not next_action.startswith(extract_action_verb(current_action)):
                    return {
                        "error_type": "verification",
                        "rule_matched": "ignored_failure",
                        "reasoning": f"At step {i + 1}, action '{current_action}' failed ('Nothing happens') "
                                     f"but agent proceeded with unrelated action '{next_action}' without acknowledging failure.",
                    }
    return None


def rule_repeated_action(
    fail_steps: list[tuple[dict, dict | None]],
    **kwargs,
) -> dict | None:
    """Rule 7: Repeated same action ≥3 consecutive times → verification.

    Agent stuck in a loop repeating the same failed action.
    """
    if len(fail_steps) < 3:
        return None

    for i in range(len(fail_steps) - 2):
        a1 = extract_action_text(_content(fail_steps[i][0]))
        a2 = extract_action_text(_content(fail_steps[i + 1][0]))
        a3 = extract_action_text(_content(fail_steps[i + 2][0]))
        if a1 == a2 == a3:
            return {
                "error_type": "verification",
                "rule_matched": "repeated_action",
                "reasoning": f"Agent repeated action '{a1}' at least 3 consecutive times "
                             f"starting at step {i + 1}, indicating failure to process environment feedback.",
            }
    return None


def rule_missing_subtask(
    fail_steps: list[tuple[dict, dict | None]],
    task_type: str,
    **kwargs,
) -> dict | None:
    """Rule 8: Missing required subtask → planning.

    For clean/heat/cool tasks, checks if the processing step was skipped entirely.
    """
    required_verb = get_required_processing_verb(task_type)
    if required_verb is None:
        return None

    # Check if any action contains the required processing verb
    for action, _ in fail_steps:
        action_text = extract_action_text(_content(action))
        if action_text.startswith(required_verb):
            return None  # Found the required step

    return {
        "error_type": "planning",
        "rule_matched": "missing_subtask",
        "reasoning": f"Task type '{task_type}' requires '{required_verb}' step, "
                     f"but agent's trajectory contains no '{required_verb}' action. "
                     f"The required subtask was completely omitted from the plan.",
    }


def rule_inefficient_search(
    fail_steps: list[tuple[dict, dict | None]],
    **kwargs,
) -> dict | None:
    """Rule 9: Inefficient search strategy → planning.

    Agent revisits locations it has already checked.
    """
    visited = []
    revisit_count = 0

    for action, _ in fail_steps:
        action_text = extract_action_text(_content(action))
        if action_text.startswith("go to"):
            location = action_text[len("go to"):].strip()
            if location in visited:
                revisit_count += 1
            else:
                visited.append(location)

    # Threshold: revisiting ≥3 locations suggests inefficient search
    if revisit_count >= 3:
        return {
            "error_type": "planning",
            "rule_matched": "inefficient_search",
            "reasoning": f"Agent revisited {revisit_count} previously checked locations "
                         f"out of {len(visited)} unique locations visited, "
                         f"indicating an inefficient search strategy.",
        }
    return None


def rule_default(**kwargs) -> dict:
    """Rule 10: Default fallback → planning."""
    return {
        "error_type": "planning",
        "rule_matched": "default",
        "reasoning": "No specific error pattern matched. Classified as planning error by default.",
    }


# Ordered list of all rules
RULES = [
    rule_pcb,
    rule_wrong_object,
    rule_wrong_instance,
    rule_wrong_receptacle,
    rule_wrong_verb,
    rule_ignored_failure,
    rule_repeated_action,
    rule_missing_subtask,
    rule_inefficient_search,
    rule_default,
]


def classify_trajectory(
    fail_traj: dict,
    expert: dict,
    divergence_info: dict,
) -> dict:
    """Apply rules in priority order and return the first match."""
    fail_steps = divergence_info["fail_steps"]
    expert_steps = divergence_info["expert_steps"]
    divergence = divergence_info["divergence_step"]

    game_file = fail_traj.get("game_file", "")
    task_type = fail_traj.get("task_type") or get_task_type(game_file)

    context = {
        "fail_steps": fail_steps,
        "expert_steps": expert_steps,
        "divergence": divergence,
        "task_type": task_type,
        "game_file": game_file,
    }

    for rule_fn in RULES:
        result = rule_fn(**context)
        if result is not None:
            return result

    # Should never reach here because rule_default always matches
    return rule_default()


# ---------------------------------------------------------------------------
# Data loading (shared logic with classify_errors.py)
# ---------------------------------------------------------------------------

def load_expert_index(path: str) -> dict:
    """Load expert trajectories indexed by normalized game_file."""
    with open(path) as f:
        experts = json.load(f)
    index = {}
    for ex in experts:
        index[normalize_game_file(ex["game_file"])] = ex
    logger.info("Loaded %d experts, %d unique game_files", len(experts), len(index))
    return index


def load_failure_trajectories(failure_dir: str) -> list[dict]:
    """Load failure trajectories from JSONL files in directory."""
    trajectories = []
    fail_path = Path(failure_dir)
    for p in sorted(fail_path.glob("*.jsonl")):
        with open(p) as f:
            for line in f:
                if line.strip():
                    traj = json.loads(line)
                    if not traj.get("success", True):
                        trajectories.append(traj)
    logger.info("Loaded %d failure trajectories from %s", len(trajectories), failure_dir)
    return trajectories


def compute_divergence_info(expert: dict, fail_traj: dict) -> dict | None:
    """Compute divergence point and correction span between expert and failure."""
    fail_convs = fail_traj.get("conversations", [])
    expert_convs = expert["conversations"]

    fail_start = find_task_start(fail_convs)
    expert_start = find_task_start(expert_convs)

    fail_steps = extract_steps(fail_convs, fail_start)
    expert_steps = extract_steps(expert_convs, expert_start)

    if not fail_steps or not expert_steps:
        return None

    divergence = find_divergence_point(expert_steps, fail_steps)
    expert_total = len(expert_steps)
    model_total = len(fail_steps)
    correction_span = max(1, expert_total - divergence)

    return {
        "divergence_step": divergence,
        "correction_span": correction_span,
        "expert_total_steps": expert_total,
        "model_total_steps": model_total,
        "expert_steps": expert_steps,
        "fail_steps": fail_steps,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Rule-based error classifier for ALFWorld failure trajectories"
    )
    parser.add_argument("--failure_dir", type=str, required=True,
                        help="Directory containing failure trajectory JSONL files")
    parser.add_argument("--expert_file", type=str, required=True,
                        help="Expert trajectories JSON file (alfworld_sft.json)")
    parser.add_argument("--output_file", type=str, required=True,
                        help="Output JSONL path for classified errors")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s %(levelname)s %(message)s",
    )

    # Load data
    expert_index = load_expert_index(args.expert_file)
    failures = load_failure_trajectories(args.failure_dir)

    # Match and classify
    out_path = Path(args.output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    records = []
    matched = 0
    unmatched = 0

    with open(out_path, "w") as f:
        for traj in failures:
            key = normalize_game_file(traj.get("game_file", ""))
            expert = expert_index.get(key)
            if expert is None:
                unmatched += 1
                logger.debug("No expert match for: %s", key)
                continue

            div_info = compute_divergence_info(expert, traj)
            if div_info is None:
                unmatched += 1
                continue

            matched += 1
            classification = classify_trajectory(traj, expert, div_info)

            rec = {
                "task_id": traj.get("task_id"),
                "task_type": traj.get("task_type") or get_task_type(traj.get("game_file", "")),
                "game_file": traj["game_file"],
                "error_type": classification["error_type"],
                "rule_matched": classification["rule_matched"],
                "divergence_point": div_info["divergence_step"],
                "correction_span": div_info["correction_span"],
                "expert_total_steps": div_info["expert_total_steps"],
                "model_total_steps": div_info["model_total_steps"],
                "is_pcb": classification["rule_matched"] == "pcb",
                "reasoning": classification["reasoning"],
            }
            records.append(rec)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    logger.info(
        "Classified %d trajectories (%d unmatched), wrote to %s",
        matched, unmatched, out_path,
    )

    # Print summary
    type_counts = Counter(r["error_type"] for r in records)
    rule_counts = Counter(r["rule_matched"] for r in records)

    print(f"\n{'='*60}")
    print("RULE-BASED CLASSIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total classified: {len(records)}")
    print(f"\nBy error type:")
    for et in ERROR_TYPES:
        n = type_counts.get(et, 0)
        pct = 100 * n / len(records) if records else 0
        print(f"  {et:<16s} {n:>4d} ({pct:5.1f}%)")
    print(f"\nBy rule matched:")
    for rule, n in rule_counts.most_common():
        pct = 100 * n / len(records) if records else 0
        print(f"  {rule:<20s} {n:>4d} ({pct:5.1f}%)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
