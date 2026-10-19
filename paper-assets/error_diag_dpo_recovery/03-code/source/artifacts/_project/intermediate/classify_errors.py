#!/usr/bin/env python3
"""LLM-based error classifier for ALFWorld failure trajectories.

Uses vLLM to classify failed ALFWorld trajectories into three error types:
action, verification, planning. Includes PCB (Premature Completion Bug)
detection and override logic, plus dual-version Kruskal-Wallis analysis.

Output JSONL fields:
  task_id, task_type, game_file, error_type, llm_original_type,
  llm_original_type_source, divergence_step, correction_span,
  expert_total_steps, model_total_steps, reasoning

Usage:
  python src/classify_errors.py \
    --failure_dir data/failures/iter1 \
    --expert_file eto_repo/data/alfworld_sft.json \
    --output_file outputs/classified_errors.jsonl \
    --model_name /root/autodl-tmp/models/Qwen3-8B \
    --gpu 0

  # Dry-run (no LLM, rule-based classification for pipeline testing):
  python src/classify_errors.py \
    --failure_dir data/failures/iter1 \
    --expert_file eto_repo/data/alfworld_sft.json \
    --output_file outputs/classified_errors_dry.jsonl \
    --dry_run 10
"""

import argparse
import json
import logging
import os
import random
import re
from pathlib import Path
from statistics import mean, median, stdev

logger = logging.getLogger("classify_errors")

ERROR_TYPES = ["action", "verification", "planning"]


# ---------------------------------------------------------------------------
# Game file normalization
# ---------------------------------------------------------------------------

def normalize_game_file(game_file: str) -> str:
    """Extract <task_dir>/<trial_dir> as matching key.

    Expert:     data/json_2.1.1/train/<task>/<trial>
    Trajectory: /root/.../json_2.1.1/train/<task>/<trial>/game.tw-pddl
    """
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
        expert_action = extract_action_text(_content(expert_steps[i][0]))
        fail_action = extract_action_text(_content(fail_steps[i][0]))
        if expert_action != fail_action:
            return i
    return min_len


def compute_divergence_info(
    expert: dict,
    fail_traj: dict,
) -> dict | None:
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

    expert_action_at_div = ""
    model_action_at_div = ""
    if divergence < len(expert_steps):
        expert_action_at_div = extract_action_text(_content(expert_steps[divergence][0]))
    if divergence < len(fail_steps):
        model_action_at_div = extract_action_text(_content(fail_steps[divergence][0]))

    return {
        "divergence_step": divergence,
        "correction_span": correction_span,
        "expert_total_steps": expert_total,
        "model_total_steps": model_total,
        "expert_action_at_div": expert_action_at_div,
        "model_action_at_div": model_action_at_div,
        "expert_steps": expert_steps,
        "fail_steps": fail_steps,
    }


# ---------------------------------------------------------------------------
# Trajectory formatting for LLM
# ---------------------------------------------------------------------------

def format_steps_for_prompt(steps: list[tuple[dict, dict | None]], label: str = "Trajectory") -> str:
    """Format extracted steps into readable text for the LLM prompt."""
    lines = [f"### {label}"]
    for i, (action_msg, obs_msg) in enumerate(steps, 1):
        content = _content(action_msg)
        lines.append(f"\nStep {i}:")
        if obs_msg:
            obs_text = _content(obs_msg)
            if obs_text.strip():
                lines.append(f"Observation: {obs_text.strip()}")
        for line in content.split("\n"):
            line = line.strip()
            if line:
                lines.append(line)
    return "\n".join(lines)


def get_task_description(conversations: list) -> str:
    """Extract task description from conversations."""
    for msg in conversations:
        if _role(msg) in ("user", "human"):
            c = _content(msg)
            if "Your task is to:" in c:
                idx = c.index("Your task is to:")
                return c[idx:].split("\n")[0].strip()
    return "Unknown task"


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

CLASSIFICATION_PROMPT = """You are an expert at analyzing agent failure trajectories in ALFWorld, a text-based household environment. Your task is to classify the root cause of a failed trajectory into exactly one of three error types.

## Error Type Definitions

### Action Error
Single-step execution mistakes where the agent's overall strategy is sound but a specific action parameter is wrong.
- Picking up the wrong object (e.g., pen instead of pencil)
- Going to the wrong instance of the correct receptacle type (shelf 1 instead of shelf 2)
- Using an invalid action verb or format (parse errors)
- The hallmark: fixing ONE step would have led to success

### Verification Error
The agent fails to check preconditions or action outcomes, causing error cascading from undetected failures.
- Proceeding after a failed "take" action without noticing "Nothing happens"
- Not confirming whether clean/heat/cool succeeded before moving on
- Repeating the same failed action without reading environment feedback
- The hallmark: the agent HAD the information (or could have obtained it) but did not use it

### Planning Error
Fundamental flaws in the task strategy or step sequence that cannot be fixed by correcting a single action.
- Skipping a required subtask entirely (e.g., forgetting to clean in a Clean & Place task)
- Searching for objects in highly unlikely locations, wasting steps
- Misunderstanding the task goal (e.g., ignoring the "clean" requirement)
- Having no fallback strategy when the primary approach fails
- The hallmark: even with perfect single-step execution and verification, the plan would not succeed

## Classification Rules

1. **Root cause principle**: When multiple error types are present, classify by the EARLIEST error that caused the failure cascade. Later errors are often consequences of the root cause.

2. **Conditional mappings**:
   - `wrong_receptacle`: If the agent went to the wrong TYPE of receptacle → Planning. If wrong INSTANCE of the correct type → Action.
   - `repeated_action`: If the agent shows no awareness of failure (no thought change) → Verification. If aware but has no alternative → Planning.
   - `max_steps_exceeded`: If the agent was on track and within 3 steps of completion → Action. If the search strategy was fundamentally inefficient → Planning.

3. **Tie-breaking**: Planning > Verification > Action. If genuinely ambiguous, the deeper structural error takes precedence.

## Task Context

ALFWorld has 6 task types:
- Pick & Place: take object → put in receptacle
- Clean & Place: take object → clean at sinkbasin → put in receptacle
- Heat & Place: take object → heat at microwave → put in receptacle
- Cool & Place: take object → cool at fridge → put in receptacle
- Examine in Light: take object → use desklamp
- Pick Two & Place: repeat pick-and-place for two objects of the same type

## Your Analysis Process

Analyze the following failed trajectory step by step:

1. **Identify the task type** from the initial observation (which of the 6 types?)
2. **Identify the required steps** for this task type (what should the agent have done?)
3. **Find the failure point** — the first step where things went wrong
4. **Determine why** — was it a wrong parameter (Action), missing check (Verification), or wrong strategy (Planning)?
5. **Check for root cause** — trace backward from the failure: is the identified error the root cause, or a symptom of an earlier error?

{trajectory_section}

## Output Format

Respond with ONLY a JSON object, no other text:

```json
{{
  "error_type": "action|verification|planning",
  "failure_step": <step number where the root cause error first occurs>,
  "failure_pattern": "wrong_object|wrong_receptacle|missing_step|repeated_action|max_steps_exceeded|parse_error",
  "reasoning": "<2-3 sentences: what the agent should have done vs what it did, and why this constitutes the classified error type>"
}}
```"""


FEW_SHOT_EXAMPLES = """
## Few-shot Examples

### Example 1: Action Error
Task: put a pencil in drawer.
The agent found the correct drawer but took "pen 1" instead of "pencil 1" from the desk.
Classification: {"error_type": "action", "failure_step": 3, "failure_pattern": "wrong_object", "reasoning": "The agent's strategy was correct (find pencil, put in drawer), but it picked up the wrong object (pen instead of pencil). Fixing this single take action would have led to success."}

### Example 2: Verification Error
Task: clean a mug and put it in cabinet.
The agent attempted "take mug 1 from countertop 1" which returned "Nothing happens" (mug was not there), but proceeded to go to sinkbasin to clean without noticing the take failed.
Classification: {"error_type": "verification", "failure_step": 4, "failure_pattern": "repeated_action", "reasoning": "The environment signaled the take action failed, but the agent did not check whether it was holding the mug. It proceeded with an empty hand to the sinkbasin. The information was available but not utilized."}

### Example 3: Planning Error
Task: clean a plate and put it in cabinet.
The agent took the plate and went directly to the cabinet to put it, completely skipping the clean step at the sinkbasin.
Classification: {"error_type": "planning", "failure_step": 3, "failure_pattern": "missing_step", "reasoning": "The agent misunderstood the task requirements by omitting the cleaning subtask entirely. Even with perfect execution of each step, the plan would not achieve the goal because the clean step was never included in the strategy."}

"""


def build_classification_prompt(
    fail_traj: dict,
    expert: dict,
    divergence_info: dict,
    span_hint: bool = True,
    few_shot: bool = False,
) -> str:
    """Build the full classification prompt for one trajectory."""
    task_desc = get_task_description(fail_traj.get("conversations", []))

    # Format failure trajectory
    fail_steps = divergence_info["fail_steps"]
    fail_text = format_steps_for_prompt(fail_steps, "Failed Agent Trajectory")

    # Format expert trajectory
    expert_steps = divergence_info["expert_steps"]
    expert_text = format_steps_for_prompt(expert_steps, "Expert (Correct) Trajectory")

    # Build trajectory section
    sections = [f"## Task\n{task_desc}\n"]

    if few_shot:
        sections.append(FEW_SHOT_EXAMPLES)

    sections.append(f"## Trajectory to Classify\n\n{fail_text}\n\n[FAILED after step {len(fail_steps)}]\n")
    sections.append(f"## Reference\n\n{expert_text}\n")

    if span_hint:
        div_step = divergence_info["divergence_step"]
        corr_span = divergence_info["correction_span"]
        sections.append(
            f"## Divergence Info\n"
            f"- Divergence point: step {div_step + 1} (0-indexed: {div_step})\n"
            f"- Correction span: {corr_span} expert steps remaining from divergence\n"
            f"- Expert action at divergence: {divergence_info['expert_action_at_div']}\n"
            f"- Agent action at divergence: {divergence_info['model_action_at_div']}\n"
        )

    trajectory_section = "\n".join(sections)
    return CLASSIFICATION_PROMPT.format(trajectory_section=trajectory_section)


# ---------------------------------------------------------------------------
# LLM response parsing
# ---------------------------------------------------------------------------

def parse_llm_response(text: str) -> dict | None:
    """Parse JSON classification from LLM output."""
    # Try to extract JSON from markdown code blocks
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if json_match:
        text = json_match.group(1)
    else:
        # Try to find raw JSON object
        json_match = re.search(r"\{[^{}]*\"error_type\"[^{}]*\}", text, re.DOTALL)
        if json_match:
            text = json_match.group(0)

    try:
        result = json.loads(text)
        et = result.get("error_type", "").lower().strip()
        if et not in ERROR_TYPES:
            logger.warning("Invalid error_type '%s', defaulting to unknown", et)
            return None
        result["error_type"] = et
        return result
    except (json.JSONDecodeError, AttributeError) as e:
        logger.warning("Failed to parse LLM response: %s", e)
        return None


# ---------------------------------------------------------------------------
# PCB detection
# ---------------------------------------------------------------------------

def detect_pcb(
    fail_steps: list[tuple[dict, dict | None]],
    expert_steps: list[tuple[dict, dict | None]],
) -> bool:
    """Detect Premature Completion Bug.

    PCB occurs when the agent's last action is a completion action (close/put)
    but the expert trajectory still has more steps remaining.
    """
    if not fail_steps or not expert_steps:
        return False

    last_action = extract_action_text(_content(fail_steps[-1][0]))
    pcb_verbs = ("close", "put", "use")
    has_completion_action = any(last_action.startswith(v) for v in pcb_verbs)
    expert_has_more = len(expert_steps) > len(fail_steps)

    return has_completion_action and expert_has_more


# ---------------------------------------------------------------------------
# Rule-based fallback (for dry-run)
# ---------------------------------------------------------------------------

def _rule_based_error_type(correction_span: int) -> str:
    """Simple rule-based classification from correction span (dry-run only)."""
    if correction_span <= 3:
        return "action"
    elif correction_span <= 7:
        return "verification"
    else:
        return "planning"


# ---------------------------------------------------------------------------
# Data loading
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


def match_failures_to_experts(
    failures: list[dict],
    expert_index: dict,
) -> list[dict]:
    """Match failure trajectories to expert trajectories and compute divergence."""
    matched = []
    unmatched = 0

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

        matched.append({"traj": traj, "expert": expert, "divergence": div_info})

    logger.info("Matched %d failures, %d unmatched", len(matched), unmatched)
    return matched


# ---------------------------------------------------------------------------
# Dual-version KW analysis (with/without PCB override)
# ---------------------------------------------------------------------------

def run_dual_analysis(records: list[dict], output_dir: str, is_dry_run: bool = False):
    """Dual-version KW: with vs without PCB override, for methodological fairness.

    Reviewer requirement: P1 (correction_span ordering) must hold in both the
    override version (PCB -> verification) and the no-override version (using
    llm_original_type) to rule out the possibility that the conclusion depends
    on the PCB reclassification bias.
    """
    from scipy.stats import kruskal as kruskal_test

    DEDUP_SEED = 42

    def _stats(recs, type_key="error_type"):
        groups = {}
        for et in ERROR_TYPES:
            spans = [r["correction_span"] for r in recs if r.get(type_key) == et]
            if spans:
                groups[et] = {
                    "n": len(spans),
                    "mean": round(mean(spans), 2),
                    "median": round(median(spans), 2),
                    "std": round(stdev(spans), 2) if len(spans) > 1 else 0.0,
                    "_spans": spans,
                }
        valid = [g for g in groups.values() if g["n"] >= 3]
        kw_h, kw_p = None, None
        if len(valid) >= 2:
            h, p = kruskal_test(*[g["_spans"] for g in valid])
            kw_h, kw_p = round(float(h), 4), round(float(p), 6)
        elif len(valid) < 2:
            logger.warning("Kruskal-Wallis skipped: need >=2 groups with n>=3, got %d", len(valid))
        return groups, kw_h, kw_p

    def _check_ordinal(groups):
        medians = {et: groups[et]["median"] for et in ERROR_TYPES if et in groups}
        if len(medians) < 3:
            return None
        return medians["action"] < medians["verification"] < medians["planning"]

    def _dedup(recs, seed):
        rng = random.Random(seed)
        by_task: dict[str, list] = {}
        for r in recs:
            by_task.setdefault(normalize_game_file(r["game_file"]), []).append(r)
        return [rng.choice(v) for v in by_task.values()]

    def _to_json(groups):
        return {et: {k: v for k, v in g.items() if k != "_spans"}
                for et, g in groups.items()}

    # --- Prepare three record sets ---
    # with_override: PCB error_type = verification (current logic)
    # without_override: use llm_original_type (excluding unknown/DRY_RUN)
    # pcb_excluded: drop PCB records entirely
    valid_types = set(ERROR_TYPES)
    no_override_recs = []
    for r in records:
        lot = r.get("llm_original_type")
        if lot in valid_types:
            no_override_recs.append({**r, "error_type": lot})
    pcb_excluded_recs = [r for r in records if not r.get("is_pcb")]
    n_pcb = sum(1 for r in records if r.get("is_pcb"))

    # --- Compute stats for each version ---
    all_results = {}
    for label, recs in [
        ("with_override", records),
        ("without_override", no_override_recs),
        ("pcb_excluded", pcb_excluded_recs),
    ]:
        groups, h, p = _stats(recs)
        deduped = _dedup(recs, DEDUP_SEED)
        groups_d, h_d, p_d = _stats(deduped)
        all_results[label] = {
            "full": {"n": len(recs), "groups": groups, "h": h, "p": p,
                     "ordinal": _check_ordinal(groups)},
            "dedup": {"n": len(deduped), "groups": groups_d, "h": h_d, "p": p_d,
                      "ordinal": _check_ordinal(groups_d)},
        }

    # --- Task-type stratified (with_override only) ---
    by_task_type: dict[str, list] = {}
    for r in records:
        tt = r.get("task_type") or "unknown"
        by_task_type.setdefault(tt, []).append(r)

    version_c_groups = {}
    for tt, tt_recs in sorted(by_task_type.items()):
        et_groups = {}
        for et in ERROR_TYPES:
            spans = [r["correction_span"] for r in tt_recs if r["error_type"] == et]
            if spans:
                et_groups[et] = spans
        valid_et = [g for g in et_groups.values() if len(g) >= 3]
        if len(valid_et) < 2:
            version_c_groups[tt] = {
                "n": len(tt_recs), "error_types": len(et_groups),
                "kruskal_h": None, "kruskal_p": None, "verdict": "insufficient"
            }
        else:
            h, p = kruskal_test(*valid_et)
            verdict = "significant" if p < 0.05 else "not_significant"
            version_c_groups[tt] = {
                "n": len(tt_recs), "error_types": len(et_groups),
                "kruskal_h": round(float(h), 4), "kruskal_p": round(float(p), 6),
                "verdict": verdict
            }

    # --- P1 gate ---
    wo = all_results["with_override"]["full"]
    wno = all_results["without_override"]["full"]
    pe = all_results["pcb_excluded"]["full"]

    override_sig = wo["p"] is not None and wo["p"] < 0.05 and wo["ordinal"] is True
    no_override_sig = wno["p"] is not None and wno["p"] < 0.05 and wno["ordinal"] is True
    pcb_excl_sig = pe["p"] is not None and pe["p"] < 0.05 and pe["ordinal"] is True
    p1_pass = override_sig and (no_override_sig or pcb_excl_sig)

    # --- Print ---
    if is_dry_run:
        print("\n⚠️  WARNING: rule-based classification — stats are tautological, for pipeline testing only")

    print(f"\n=== P1 Correction Span Analysis (PCB trajectories: {n_pcb}) ===")

    for label in ["with_override", "without_override", "pcb_excluded"]:
        res = all_results[label]
        for sub_label, sub in [("Full", res["full"]), ("Deduplicated", res["dedup"])]:
            print(f"\n{label} / {sub_label} (N={sub['n']}):")
            for et in ERROR_TYPES:
                if et in sub["groups"]:
                    g = sub["groups"][et]
                    print(f"  {et+':':<17s} N={g['n']}, mean={g['mean']:.2f}, "
                          f"median={g['median']:.1f}, std={g['std']:.2f}")
                else:
                    print(f"  {et+':':<17s} N=0")
            if sub["h"] is not None:
                print(f"  Kruskal-Wallis: H={sub['h']:.4f}, p={sub['p']:.6f}")
                ord_str = "✓" if sub["ordinal"] else "✗"
                print(f"  Ordinal (action < verification < planning): {ord_str}")
            else:
                print(f"  Kruskal-Wallis: SKIPPED (need >=2 groups with n>=3)")

    print(f"\nTask-type stratified (with_override):")
    vc_sig = sum(1 for g in version_c_groups.values() if g["verdict"] == "significant")
    vc_insuf = sum(1 for g in version_c_groups.values() if g["verdict"] == "insufficient")
    vc_total = len(version_c_groups)
    for tt in sorted(version_c_groups):
        g = version_c_groups[tt]
        h_str = f"H={g['kruskal_h']:.4f}" if g["kruskal_h"] is not None else "H=N/A"
        p_str = f"p={g['kruskal_p']:.6f}" if g["kruskal_p"] is not None else "p=N/A"
        print(f"  {tt+':':<30s} N={g['n']}, {h_str}, {p_str} [{g['verdict'].upper()}]")
    print(f"  Summary: {vc_sig}/{vc_total} groups significant, {vc_insuf} insufficient")

    print(f"\n{'='*50}")
    print(f"P1 GATE: {'PASS ✓' if p1_pass else 'FAIL ✗'}")
    wo_p = '%.6f' % wo['p'] if wo['p'] is not None else 'N/A'
    wno_p = '%.6f' % wno['p'] if wno['p'] is not None else 'N/A'
    pe_p = '%.6f' % pe['p'] if pe['p'] is not None else 'N/A'
    print(f"  with_override:    p={wo_p}, ordinal={wo['ordinal']}")
    print(f"  without_override: p={wno_p}, ordinal={wno['ordinal']}")
    print(f"  pcb_excluded:     p={pe_p}, ordinal={pe['ordinal']}")
    print(f"{'='*50}")

    # --- Save JSON ---
    analysis = {
        "tautological_warning": is_dry_run,
        "n_pcb": n_pcb,
        "p1_gate": {
            "pass": p1_pass,
            "with_override_significant": override_sig,
            "without_override_significant": no_override_sig,
            "pcb_excluded_significant": pcb_excl_sig,
        },
    }
    for label in ["with_override", "without_override", "pcb_excluded"]:
        res = all_results[label]
        for sub_label in ["full", "dedup"]:
            sub = res[sub_label]
            key = f"{label}_{sub_label}"
            analysis[key] = {
                "n": sub["n"],
                "kruskal_h": sub["h"],
                "kruskal_p": sub["p"],
                "ordinal_holds": sub["ordinal"],
                "groups": _to_json(sub["groups"]),
            }
    analysis["task_type_stratified"] = {
        "groups": version_c_groups,
        "summary": {"significant": vc_sig, "insufficient": vc_insuf, "total": vc_total},
    }
    analysis["dedup_seed"] = DEDUP_SEED

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "p1_analysis.json"
    with open(json_path, "w") as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    logger.info("Dual analysis saved → %s", json_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="LLM-based error classifier for ALFWorld failure trajectories"
    )
    parser.add_argument("--failure_dir", type=str, required=True,
                        help="Directory containing failure trajectory JSONL files")
    parser.add_argument("--expert_file", type=str, required=True,
                        help="Expert trajectories JSON file (alfworld_sft.json)")
    parser.add_argument("--output_file", type=str, required=True,
                        help="Output JSONL path for classified errors")
    parser.add_argument("--model_name", type=str, default=None,
                        help="LLM model path for vLLM inference")
    parser.add_argument("--gpu", type=int, default=0,
                        help="GPU device index")
    parser.add_argument("--no_span_hint", action="store_true",
                        help="Do not include divergence span info in prompt")
    parser.add_argument("--few_shot", action="store_true",
                        help="Use few-shot examples in prompt")
    parser.add_argument("--dry_run", type=int, default=0, metavar="N",
                        help="Process only first N trajectories with rule-based classification (no LLM)")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(name)s %(levelname)s %(message)s",
    )

    # --- Load data ---
    expert_index = load_expert_index(args.expert_file)
    failures = load_failure_trajectories(args.failure_dir)

    if args.dry_run:
        failures = failures[:args.dry_run]
        logger.info("Dry-run mode: processing %d trajectories", len(failures))

    # --- Match ---
    matched = match_failures_to_experts(failures, expert_index)
    if not matched:
        logger.error("No matched trajectories. Check game_file normalization.")
        return

    # --- Output ---
    out_path = Path(args.output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        # Rule-based classification (no LLM)
        records = []
        with open(out_path, "w") as f:
            for m in matched:
                d = m["divergence"]
                is_pcb = "csf_details" in m["traj"]
                rb_type = _rule_based_error_type(d["correction_span"])
                rec = {
                    "task_id": m["traj"].get("task_id"),
                    "task_type": m["traj"].get("task_type"),
                    "game_file": m["traj"]["game_file"],
                    "error_type": "DRY_RUN",
                    "llm_original_type": rb_type if is_pcb else "DRY_RUN",
                    "llm_original_type_source": "rule-based" if is_pcb else "dry_run",
                    "divergence_step": d["divergence_step"],
                    "correction_span": d["correction_span"],
                    "expert_total_steps": d["expert_total_steps"],
                    "model_total_steps": d["model_total_steps"],
                    "expert_action_at_div": d["expert_action_at_div"],
                    "model_action_at_div": d["model_action_at_div"],
                    "reasoning": "dry_run",
                }
                if is_pcb:
                    rec["error_type"] = "verification"
                    rec["sub_type"] = "premature_completion_belief"
                    rec["csf_details"] = m["traj"]["csf_details"]
                    rec["reasoning"] = "D023: CSF pattern with incomplete task — agent failed to verify critical sub-steps"
                records.append(rec)
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

        logger.info("Dry-run: wrote %d records to %s", len(records), out_path)

        # Dual analysis with rule-based types
        analysis_recs = []
        for m in matched:
            d = m["divergence"]
            is_pcb = "csf_details" in m["traj"]
            rb_type = _rule_based_error_type(d["correction_span"])
            et = "verification" if is_pcb else rb_type
            analysis_recs.append({
                "game_file": m["traj"]["game_file"],
                "task_type": m["traj"].get("task_type", "unknown"),
                "error_type": et,
                "llm_original_type": rb_type if is_pcb else et,
                "is_pcb": is_pcb,
                "correction_span": d["correction_span"],
            })
        run_dual_analysis(analysis_recs, str(Path(args.output_file).parent), is_dry_run=True)
        return

    # --- Full LLM inference ---
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    from vllm import LLM, SamplingParams

    logger.info("Loading model: %s", args.model_name)
    llm = LLM(
        model=args.model_name,
        trust_remote_code=True,
        max_model_len=8192,
        gpu_memory_utilization=0.9,
    )
    sampling_params = SamplingParams(
        temperature=0,
        max_tokens=512,
        stop=["```\n"],
    )

    # Build prompts
    prompts = []
    for m in matched:
        prompt = build_classification_prompt(
            fail_traj=m["traj"],
            expert=m["expert"],
            divergence_info=m["divergence"],
            span_hint=not args.no_span_hint,
            few_shot=args.few_shot,
        )
        prompts.append(prompt)

    logger.info("Running vLLM inference on %d prompts...", len(prompts))
    outputs = llm.generate(prompts, sampling_params)

    # Parse results
    results = []
    for output in outputs:
        text = output.outputs[0].text
        parsed = parse_llm_response(text)
        results.append(parsed)

    # Write output with PCB override
    records = []
    with open(out_path, "w") as f:
        for m, res in zip(matched, results):
            d = m["divergence"]
            llm_type = res["error_type"] if res else "unknown"
            rec = {
                "task_id": m["traj"].get("task_id"),
                "task_type": m["traj"].get("task_type"),
                "game_file": m["traj"]["game_file"],
                "error_type": llm_type,
                "llm_original_type": llm_type,
                "llm_original_type_source": "llm",
                "divergence_step": d["divergence_step"],
                "correction_span": d["correction_span"],
                "expert_total_steps": d["expert_total_steps"],
                "model_total_steps": d["model_total_steps"],
                "reasoning": res.get("reasoning", "") if res else "LLM parse failed",
            }
            if "csf_details" in m["traj"]:
                rec["error_type"] = "verification"
                rec["sub_type"] = "premature_completion_belief"
                rec["csf_details"] = m["traj"]["csf_details"]
                rec["is_pcb"] = True
            else:
                rec["is_pcb"] = False

            if res:
                rec["failure_step"] = res.get("failure_step")
                rec["failure_pattern"] = res.get("failure_pattern")
                rec["confidence"] = res.get("confidence")

            records.append(rec)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    n_pcb = sum(1 for r in records if r.get("is_pcb"))
    n_overridden = sum(1 for r in records if r.get("is_pcb") and r.get("llm_original_type") != "verification")
    logger.info(
        "Wrote %d records to %s (PCB: %d, overridden: %d)",
        len(records), out_path, n_pcb, n_overridden,
    )

    # Dual analysis
    analysis_recs = []
    for m, res in zip(matched, results):
        d = m["divergence"]
        is_pcb = "csf_details" in m["traj"]
        llm_type = res["error_type"] if res else "unknown"
        et = "verification" if is_pcb else llm_type
        analysis_recs.append({
            "game_file": m["traj"]["game_file"],
            "task_type": m["traj"].get("task_type", "unknown"),
            "error_type": et,
            "llm_original_type": llm_type,
            "is_pcb": is_pcb,
            "correction_span": d["correction_span"],
        })
    run_dual_analysis(analysis_recs, str(Path(args.output_file).parent), is_dry_run=False)


if __name__ == "__main__":
    main()
