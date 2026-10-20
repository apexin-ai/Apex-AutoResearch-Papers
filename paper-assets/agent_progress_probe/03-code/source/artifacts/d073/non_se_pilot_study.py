#!/usr/bin/env python3
"""Non-SE trajectory pilot study: cross-domain structural feature extraction.

Downloads ToolBench (API tool-calling) and ALFWorld (household robot) trajectories,
maps them to the ProgressProbe step format, extracts 30 structural features
with domain-adapted command classification, and evaluates cross-domain applicability.
"""

import json
import re
import os
import sys
import traceback
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# 0. Config
# ---------------------------------------------------------------------------
DATA_DIR = Path("/root/autodl-tmp/agent_progress_probe/data/non_se_pilot")
DATA_DIR.mkdir(parents=True, exist_ok=True)

PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1

# ---------------------------------------------------------------------------
# 1. Data loading helpers
# ---------------------------------------------------------------------------

def load_toolbench_from_hf(limit=300):
    """Load ToolBench trajectories from HuggingFace."""
    from datasets import load_dataset
    print("[ToolBench] Loading from HuggingFace (tuandunghcmut/toolbench-v1)...")
    try:
        ds = load_dataset("tuandunghcmut/toolbench-v1", split="train", streaming=True)
        trajs = []
        for i, row in enumerate(ds):
            if i >= limit:
                break
            trajs.append(row)
        print(f"[ToolBench] Loaded {len(trajs)} rows")
        return trajs
    except Exception as e:
        print(f"[ToolBench] HF load failed: {e}")
        return None


def load_alfworld_from_hf(limit=300):
    """Load ALFWorld trajectories from HuggingFace."""
    from datasets import load_dataset
    print("[ALFWorld] Loading from HuggingFace (u-10bei/sft_alfworld_trajectory_dataset)...")
    try:
        ds = load_dataset("u-10bei/sft_alfworld_trajectory_dataset", split="train", streaming=True)
        trajs = []
        for i, row in enumerate(ds):
            if i >= limit:
                break
            trajs.append(row)
        print(f"[ALFWorld] Loaded {len(trajs)} rows")
        return trajs
    except Exception as e:
        print(f"[ALFWorld] HF load failed: {e}")
        return None


def load_atbench_from_hf(limit=500):
    """Load ATBench trajectories from HuggingFace."""
    from datasets import load_dataset
    print("[ATBench] Loading from HuggingFace (AI45Research/ATBench)...")
    try:
        ds = load_dataset("AI45Research/ATBench", "ATBench", split="test", streaming=True)
        trajs = []
        for i, row in enumerate(ds):
            if i >= limit:
                break
            trajs.append(row)
        print(f"[ATBench] Loaded {len(trajs)} rows")
        return trajs
    except Exception as e:
        print(f"[ATBench] HF load failed: {e}")
        return None


# ---------------------------------------------------------------------------
# 2. Trajectory normalization → common step format
# ---------------------------------------------------------------------------

def normalize_toolbench(raw_rows):
    """Convert ToolBench rows to list of trajectories in common format.

    Each trajectory = dict with:
      - id: str
      - domain: "toolbench"
      - steps: list of {role: "ai"|"user"|"system", text: str}
      - outcome: bool (True=solved) or None
      - metadata: dict
    """
    trajectories = []
    for idx, row in enumerate(raw_rows):
        steps = []
        # ToolBench has 'conversations' or 'intermediate_steps' depending on version
        # Try common keys
        conversations = None
        for key in ['conversations', 'messages', 'intermediate_steps']:
            if key in row and row[key]:
                conversations = row[key]
                break

        if conversations is None:
            # Try to parse from 'answer' field which may contain Thought/Action/Observation
            answer = row.get('answer', '') or row.get('response', '') or ''
            if not answer:
                continue
            # Parse Thought/Action/Action Input/Observation blocks
            blocks = re.split(r'(Thought:|Action:|Action Input:|Observation:)', answer)
            current_role = "ai"
            current_text = ""
            for block in blocks:
                block = block.strip()
                if block in ('Thought:', 'Action:', 'Action Input:'):
                    if current_text and current_role == "user":
                        steps.append({"role": "user", "text": current_text.strip()})
                        current_text = ""
                    current_role = "ai"
                    current_text += block + " "
                elif block == 'Observation:':
                    if current_text:
                        steps.append({"role": "ai", "text": current_text.strip()})
                        current_text = ""
                    current_role = "user"
                elif block:
                    current_text += block + " "
            if current_text.strip():
                steps.append({"role": current_role, "text": current_text.strip()})
        else:
            # Parse conversation format
            for msg in conversations:
                if isinstance(msg, str):
                    steps.append({"role": "user", "text": msg})
                    continue
                if not isinstance(msg, dict):
                    continue
                role_raw = msg.get('role', msg.get('from', ''))
                text = msg.get('content', msg.get('value', ''))
                if role_raw in ('assistant', 'gpt', 'ai', 'model'):
                    role = "ai"
                elif role_raw in ('user', 'human', 'tool', 'function', 'observation'):
                    role = "user"
                elif role_raw == 'system':
                    role = "system"
                else:
                    role = "user"
                if text:
                    steps.append({"role": role, "text": str(text)})

        if len(steps) < 2:
            continue

        # Determine outcome from the trajectory
        outcome = None
        last_ai = [s for s in steps if s["role"] == "ai"]
        if last_ai:
            last_text = last_ai[-1]["text"].lower()
            if "final answer" in last_text or "give up" not in last_text:
                outcome = True
            if "give up" in last_text or "i cannot" in last_text:
                outcome = False

        trajectories.append({
            "id": f"toolbench_{idx}",
            "domain": "toolbench",
            "steps": steps,
            "outcome": outcome,
            "metadata": {"query": str(row.get('query', row.get('instruction', '')))[:200]}
        })

    return trajectories


def normalize_alfworld(raw_rows):
    """Convert ALFWorld rows to common format."""
    trajectories = []
    for idx, row in enumerate(raw_rows):
        steps = []
        messages = row.get('messages', [])
        if not messages:
            continue

        for msg in messages:
            role_raw = msg.get('role', '')
            text = msg.get('content', '')
            if role_raw == 'assistant':
                role = "ai"
            elif role_raw in ('user', 'tool'):
                role = "user"
            elif role_raw == 'system':
                role = "system"
            else:
                role = "user"
            if text:
                steps.append({"role": role, "text": str(text)})

        if len(steps) < 2:
            continue

        # ALFWorld: check for success in metadata or last message
        metadata = row.get('metadata', {}) or {}
        outcome = None
        task_type = metadata.get('task_type', 'unknown')

        # Check if trajectory ends with success
        for s in reversed(steps):
            if 'you win' in s['text'].lower() or 'task completed' in s['text'].lower():
                outcome = True
                break
            if 'nothing happens' in s['text'].lower() and s == steps[-1]:
                outcome = False
                break

        trajectories.append({
            "id": f"alfworld_{idx}",
            "domain": "alfworld",
            "steps": steps,
            "outcome": outcome,
            "metadata": {"task_type": task_type}
        })

    return trajectories


def normalize_atbench(raw_rows):
    """Convert ATBench rows to common format."""
    if raw_rows:
        sample = raw_rows[0]
        print(f"[ATBench] Sample row keys: {list(sample.keys())}")
        for k, v in sample.items():
            vstr = str(v)[:200]
            print(f"  {k}: type={type(v).__name__}, preview={vstr}")

    trajectories = []
    for idx, row in enumerate(raw_rows):
        steps = []
        messages = None
        # Try all plausible keys for trajectory data
        for key in ['trajectory', 'messages', 'conversation', 'dialog',
                     'turns', 'history', 'chat', 'interactions', 'steps']:
            if key in row and row[key]:
                messages = row[key]
                break

        if messages is None:
            # Try to build trajectory from query/response pairs
            q = row.get('query', row.get('instruction', row.get('input', '')))
            a = row.get('response', row.get('output', row.get('answer', '')))
            if q and a:
                steps.append({"role": "user", "text": str(q)})
                steps.append({"role": "ai", "text": str(a)})

        if messages is not None:
            if isinstance(messages, str):
                turns = messages.split('\n\n')
                for turn in turns:
                    if turn.strip():
                        if any(k in turn.lower() for k in ['assistant:', 'agent:', 'thought:']):
                            steps.append({"role": "ai", "text": turn.strip()})
                        else:
                            steps.append({"role": "user", "text": turn.strip()})
            elif isinstance(messages, list):
                for msg in messages:
                    if isinstance(msg, dict):
                        role_raw = msg.get('role', msg.get('from', 'user'))
                        text = msg.get('content', msg.get('value', msg.get('text', '')))
                        if role_raw in ('assistant', 'ai', 'agent', 'model'):
                            role = "ai"
                        elif role_raw == 'system':
                            role = "system"
                        else:
                            role = "user"
                        if text:
                            steps.append({"role": role, "text": str(text)})
                    elif isinstance(msg, str):
                        steps.append({"role": "user", "text": msg})

        if len(steps) < 2:
            continue

        label = row.get('label', row.get('safety_label', None))
        outcome = None
        if label is not None:
            if isinstance(label, str):
                outcome = label.lower() in ('safe', 'success', '1', 'true')
            elif isinstance(label, (int, float)):
                outcome = bool(label)

        trajectories.append({
            "id": f"atbench_{idx}",
            "domain": "atbench",
            "steps": steps,
            "outcome": outcome,
            "metadata": {k: str(v)[:100] for k, v in row.items()
                         if k not in ('trajectory', 'messages', 'conversation')}
        })

    return trajectories


# ---------------------------------------------------------------------------
# 3. Domain-adapted command extraction
# ---------------------------------------------------------------------------

# SE-original command categories
SE_EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SE_SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
SE_NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}

# ToolBench: API action types → command categories
TOOLBENCH_MUTATION_KEYWORDS = {"create", "update", "delete", "post", "put", "patch",
                                "write", "modify", "set", "add", "remove", "send"}
TOOLBENCH_QUERY_KEYWORDS = {"get", "search", "list", "fetch", "find", "query",
                             "retrieve", "lookup", "check", "read", "show"}

# ALFWorld: household action → command categories
ALFWORLD_STATE_CHANGE = {"pick", "put", "open", "close", "heat", "cool", "clean",
                          "use", "slice", "toggle"}
ALFWORLD_EXPLORE = {"go", "examine", "look", "inventory", "think"}


def extract_command_generic(text, domain):
    """Extract the 'command' from an AI step, domain-aware."""
    if domain == "toolbench":
        # Look for Action: line or function call
        m = re.search(r'Action:\s*(.+?)(?:\n|$)', text)
        if m:
            return m.group(1).strip()
        m = re.search(r'"action":\s*"([^"]+)"', text)
        if m:
            return m.group(1).strip()
        # Look for code blocks
        m = re.search(r'```\n?(.*?)```', text, re.DOTALL)
        if m:
            return m.group(1).strip()
        return None
    elif domain == "alfworld":
        # ALFWorld actions are typically the full assistant message
        # Look for action patterns
        text_lower = text.lower().strip()
        for prefix in ['think:', '>', 'ok.']:
            if text_lower.startswith(prefix):
                return text[len(prefix):].strip() or text
        return text.strip() if len(text.strip()) < 200 else text.strip()[:200]
    elif domain == "atbench":
        # ATBench: tool calls embedded in assistant messages
        m = re.search(r'(?:tool_call|function_call|action)[\s:]+(.+?)(?:\n|$)', text, re.I)
        if m:
            return m.group(1).strip()
        m = re.search(r'"name":\s*"([^"]+)"', text)
        if m:
            return m.group(1).strip()
        m = re.search(r'```\n?(.*?)```', text, re.DOTALL)
        if m:
            return m.group(1).strip()
        return None
    else:
        # Fallback: SE-style
        m = re.search(r'```\n?(.*?)```', text, re.DOTALL)
        return m.group(1).strip() if m else None


def classify_command(cmd, domain):
    """Classify a command into edit/search/nav/submit categories, domain-aware.

    Returns: (is_edit, is_search, is_nav, is_submit)
    """
    if not cmd:
        return False, False, False, False

    cmd_lower = cmd.lower()
    first_word = cmd_lower.split()[0] if cmd_lower.split() else ""

    if domain == "toolbench":
        is_edit = any(k in cmd_lower for k in TOOLBENCH_MUTATION_KEYWORDS)
        is_search = any(k in cmd_lower for k in TOOLBENCH_QUERY_KEYWORDS)
        is_nav = False  # no navigation concept in API calls
        is_submit = "finish" in cmd_lower or "final answer" in cmd_lower
        return is_edit, is_search, is_nav, is_submit

    elif domain == "alfworld":
        is_edit = any(cmd_lower.startswith(k) or f" {k} " in f" {cmd_lower} "
                      for k in ALFWORLD_STATE_CHANGE)
        is_search = any(cmd_lower.startswith(k) or f" {k} " in f" {cmd_lower} "
                        for k in ALFWORLD_EXPLORE)
        is_nav = cmd_lower.startswith("go to") or cmd_lower.startswith("go ")
        is_submit = False
        return is_edit, is_search, is_nav, is_submit

    elif domain == "atbench":
        is_edit = any(k in cmd_lower for k in TOOLBENCH_MUTATION_KEYWORDS)
        is_search = any(k in cmd_lower for k in TOOLBENCH_QUERY_KEYWORDS)
        is_nav = any(k in cmd_lower for k in ["navigate", "browse", "open", "visit"])
        is_submit = "finish" in cmd_lower or "final" in cmd_lower
        return is_edit, is_search, is_nav, is_submit

    else:
        # SE fallback
        is_edit = first_word in SE_EDIT_CMDS
        is_search = first_word in SE_SEARCH_CMDS
        is_nav = first_word in SE_NAV_CMDS
        is_submit = first_word == "submit"
        return is_edit, is_search, is_nav, is_submit


def detect_error(text, domain):
    """Detect error patterns in observation text, domain-aware."""
    text_lower = text.lower()
    if domain == "toolbench":
        return any(k in text_lower for k in ["error", "exception", "invalid",
                                              "unauthorized", "404", "500",
                                              "failed", "timeout", "rate limit"])
    elif domain == "alfworld":
        return "nothing happens" in text_lower or "can't" in text_lower
    elif domain == "atbench":
        return any(k in text_lower for k in ["error", "exception", "failed",
                                              "unauthorized", "denied", "invalid"])
    else:
        return "Traceback" in text or "Error" in text


def detect_nonzero_exit(text, domain):
    """Detect non-zero exit / failure patterns in observations."""
    if domain == "toolbench":
        return bool(re.search(r'"error"|"status":\s*[45]\d\d|"code":\s*[1-9]', text))
    elif domain == "alfworld":
        return "nothing happens" in text.lower()
    elif domain == "atbench":
        return bool(re.search(r'"error"|failed|exception', text, re.I))
    else:
        return bool(re.search(r"exit code [1-9]|returned non-zero|command not found", text))


# ---------------------------------------------------------------------------
# 4. Feature extraction (domain-aware version of the 30 features)
# ---------------------------------------------------------------------------

def cmd_similarity(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def extract_features_generic(steps, domain, is_short=False):
    """Extract 30 structural features from steps in any domain."""
    n = len(steps)
    if n == 0:
        return np.zeros(30)

    texts = [s["text"] for s in steps]
    text_lens = [len(t) for t in texts]

    actions = [s for s in steps if s["role"] == "ai"]
    observations = [s for s in steps if s["role"] == "user"]

    n_actions = len(actions)
    n_obs = len(observations)

    mean_tlen = np.mean(text_lens)
    std_tlen = np.std(text_lens) if n > 1 else 0.0
    max_tlen = max(text_lens)
    min_tlen = min(text_lens)

    action_lens = [len(s["text"]) for s in actions] if actions else [0]
    obs_lens = [len(s["text"]) for s in observations] if observations else [0]
    mean_action_len = np.mean(action_lens)
    mean_obs_len = np.mean(obs_lens)

    if n > 1:
        x = np.arange(n, dtype=float)
        y = np.array(text_lens, dtype=float)
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
    else:
        slope = 0.0

    # Command extraction (domain-aware)
    commands = []
    for s in actions:
        cmd = extract_command_generic(s["text"], domain)
        if cmd:
            commands.append(cmd)

    n_cmds = len(commands)
    cmd_lens = [len(c) for c in commands] if commands else [0]
    mean_cmd_len = np.mean(cmd_lens)
    max_cmd_len = max(cmd_lens) if cmd_lens else 0

    if n_cmds > 0:
        unique_cmds = len(set(commands))
        unique_cmd_ratio = unique_cmds / n_cmds
        cmd_counter = Counter(commands)
        max_repeat = cmd_counter.most_common(1)[0][1]
        repeat_ratio = max_repeat / n_cmds
    else:
        unique_cmd_ratio = 1.0
        repeat_ratio = 0.0

    # Command type classification (domain-aware)
    n_edit = n_search = n_nav = n_submit = 0
    for cmd in commands:
        is_edit, is_search, is_nav, is_submit = classify_command(cmd, domain)
        n_edit += int(is_edit)
        n_search += int(is_search)
        n_nav += int(is_nav)
        n_submit += int(is_submit)

    edit_ratio = n_edit / max(n_cmds, 1)
    search_ratio = n_search / max(n_cmds, 1)

    # Adjacent command similarity
    if n_cmds >= 2:
        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
        avg_adj_sim = np.mean(sims)
        max_adj_sim = max(sims)
        max_run = 1
        cur_run = 1
        for s in sims:
            if s >= 0.9:
                cur_run += 1
                max_run = max(max_run, cur_run)
            else:
                cur_run = 1
    else:
        avg_adj_sim = 0.0
        max_adj_sim = 0.0
        max_run = 0

    # Content patterns (domain-aware)
    n_errors = sum(1 for s in steps if detect_error(s["text"], domain))
    n_test_output = 0  # No test concept in non-SE → always 0
    n_file_display = 0  # No file display in non-SE → always 0
    n_nonzero_exit = sum(1 for s in observations if detect_nonzero_exit(s["text"], domain))

    feature_vec = np.array([
        n,                      # 0: num_steps
        n_actions,              # 1: num_actions
        n_obs,                  # 2: num_observations
        n_actions / max(n, 1),  # 3: action_ratio
        mean_tlen,              # 4: mean_text_len
        std_tlen,               # 5: std_text_len
        max_tlen,               # 6: max_text_len
        min_tlen,               # 7: min_text_len
        mean_action_len,        # 8: mean_action_len
        mean_obs_len,           # 9: mean_obs_len
        slope,                  # 10: text_len_trend
        n_cmds,                 # 11: num_commands
        mean_cmd_len,           # 12: mean_cmd_len
        max_cmd_len,            # 13: max_cmd_len
        unique_cmd_ratio,       # 14: unique_cmd_ratio
        repeat_ratio,           # 15: max_repeat_ratio
        n_edit,                 # 16: num_edit_cmds (→ mutation actions)
        n_search,               # 17: num_search_cmds (→ query actions)
        n_nav,                  # 18: num_nav_cmds
        n_submit,               # 19: num_submit_cmds
        edit_ratio,             # 20: edit_ratio (→ mutation_ratio)
        search_ratio,           # 21: search_ratio (→ query_ratio)
        avg_adj_sim,            # 22: avg_adjacent_cmd_similarity
        max_adj_sim,            # 23: max_adjacent_cmd_similarity
        max_run,                # 24: max_consecutive_similar_cmds
        n_errors,               # 25: num_errors
        n_test_output,          # 26: num_test_outputs (always 0 for non-SE)
        n_file_display,         # 27: num_file_displays (always 0 for non-SE)
        n_nonzero_exit,         # 28: num_nonzero_exits (→ failure responses)
        float(is_short),        # 29: is_short_trajectory
    ], dtype=np.float32)

    return feature_vec


FEATURE_NAMES = [
    "num_steps", "num_actions", "num_observations", "action_ratio",
    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
    "mean_action_len", "mean_obs_len", "text_len_trend",
    "num_commands", "mean_cmd_len", "max_cmd_len",
    "unique_cmd_ratio", "max_repeat_ratio",
    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
    "edit_ratio", "search_ratio",
    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
    "num_errors", "num_test_outputs", "num_file_displays",
    "num_nonzero_exits", "is_short_trajectory",
]


# ---------------------------------------------------------------------------
# 5. Domain-adapted labeling functions
# ---------------------------------------------------------------------------

def lf_action_diversity(steps, domain):
    """Adapted LF1: Are actions diverse (progress) or repetitive (stagnation)?

    Replaces SE-specific lf_file_diff_delta with domain-general action diversity.
    """
    commands = []
    for s in steps:
        if s["role"] != "ai":
            continue
        cmd = extract_command_generic(s["text"], domain)
        if cmd:
            commands.append(cmd)

    if len(commands) < 2:
        return ABSTAIN

    n_mutation = sum(1 for c in commands if classify_command(c, domain)[0])
    n_query = sum(1 for c in commands if classify_command(c, domain)[1])

    if n_mutation >= 2:
        return PROGRESS
    if n_mutation == 0 and n_query >= 3:
        return STAGNATION
    return ABSTAIN


def lf_command_repetition(steps, domain):
    """Adapted LF2: Detect repetitive action patterns. (Nearly domain-invariant.)"""
    commands = []
    for s in steps:
        if s["role"] != "ai":
            continue
        cmd = extract_command_generic(s["text"], domain)
        if cmd:
            commands.append(cmd)

    if len(commands) < 2:
        return ABSTAIN

    # Check exact repetition (≥3 consecutive identical)
    run = 1
    for i in range(1, len(commands)):
        if commands[i] == commands[i-1]:
            run += 1
            if run >= 3:
                return STAGNATION
        else:
            run = 1

    # Check high-similarity repetition (≥3 consecutive with sim ≥ 0.9)
    run = 1
    for i in range(1, len(commands)):
        if cmd_similarity(commands[i-1], commands[i]) >= 0.9:
            run += 1
            if run >= 3:
                return STAGNATION
        else:
            run = 1

    if len(set(commands)) == len(commands):
        return PROGRESS

    return ABSTAIN


def lf_error_accumulation(steps, domain):
    """New LF: Accumulating errors without recovery → stagnation.

    Domain-general: works with any error detection mechanism.
    """
    obs_steps = [s for s in steps if s["role"] == "user"]
    if len(obs_steps) < 3:
        return ABSTAIN

    error_flags = [detect_error(s["text"], domain) for s in obs_steps]
    n_errors = sum(error_flags)

    if n_errors == 0:
        return PROGRESS

    # Check if errors are at the end (no recovery)
    last_3 = error_flags[-3:] if len(error_flags) >= 3 else error_flags
    if all(last_3):
        return STAGNATION

    if n_errors >= len(obs_steps) * 0.6:
        return STAGNATION

    return ABSTAIN


# ---------------------------------------------------------------------------
# 6. Window extraction
# ---------------------------------------------------------------------------

def extract_windows(steps, window_size=10, stride=4):
    """Extract sliding windows from a step sequence."""
    interaction_steps = [s for s in steps if s["role"] != "system"]
    windows = []
    for start in range(0, max(1, len(interaction_steps) - window_size + 1), stride):
        end = min(start + window_size, len(interaction_steps))
        window = interaction_steps[start:end]
        if len(window) >= 4:  # minimum viable window
            windows.append(window)
    if not windows and len(interaction_steps) >= 2:
        windows.append(interaction_steps)
    return windows


# ---------------------------------------------------------------------------
# 7. Main pilot study
# ---------------------------------------------------------------------------

def run_pilot_for_dataset(name, trajectories):
    """Run pilot study on a set of normalized trajectories."""
    print(f"\n{'='*60}")
    print(f"  Pilot Study: {name} ({len(trajectories)} trajectories)")
    print(f"{'='*60}")

    if not trajectories:
        print("  No trajectories loaded. Skipping.")
        return None

    domain = trajectories[0]["domain"]

    # Trajectory-level stats
    step_counts = [len(t["steps"]) for t in trajectories]
    outcomes = [t["outcome"] for t in trajectories]
    n_with_outcome = sum(1 for o in outcomes if o is not None)
    n_success = sum(1 for o in outcomes if o is True)
    n_fail = sum(1 for o in outcomes if o is False)

    print(f"\n  Trajectory stats:")
    print(f"    Total: {len(trajectories)}")
    print(f"    Steps: mean={np.mean(step_counts):.1f}, median={np.median(step_counts):.0f}, "
          f"min={min(step_counts)}, max={max(step_counts)}")
    print(f"    With outcome label: {n_with_outcome} "
          f"(success={n_success}, fail={n_fail})")

    # Extract windows and features
    all_features = []
    all_lf_labels = []
    all_window_meta = []
    n_short = 0

    for traj in trajectories:
        steps = traj["steps"]
        is_short = len([s for s in steps if s["role"] != "system"]) < 10
        n_short += int(is_short)

        windows = extract_windows(steps)
        for w_idx, window in enumerate(windows):
            feat = extract_features_generic(window, domain, is_short=is_short)
            all_features.append(feat)

            # Apply LFs
            lf1 = lf_action_diversity(window, domain)
            lf2 = lf_command_repetition(window, domain)
            lf3 = lf_error_accumulation(window, domain)

            # Majority vote
            votes = [v for v in [lf1, lf2, lf3] if v != ABSTAIN]
            if votes:
                majority = int(Counter(votes).most_common(1)[0][0])
            else:
                majority = ABSTAIN

            all_lf_labels.append({
                "action_diversity": lf1,
                "command_repetition": lf2,
                "error_accumulation": lf3,
                "majority": majority,
            })

            all_window_meta.append({
                "traj_id": traj["id"],
                "window_idx": w_idx,
                "outcome": traj["outcome"],
            })

    features_matrix = np.array(all_features)
    n_windows = len(all_features)

    print(f"\n  Window extraction:")
    print(f"    Total windows: {n_windows}")
    print(f"    Short trajectories: {n_short}/{len(trajectories)}")

    # Feature statistics
    print(f"\n  Feature statistics (30 features):")
    print(f"    {'Feature':<28} {'Mean':>8} {'Std':>8} {'NonZero%':>8}")
    print(f"    {'-'*56}")

    feature_applicability = {}
    for i, fname in enumerate(FEATURE_NAMES):
        col = features_matrix[:, i]
        mean_val = np.mean(col)
        std_val = np.std(col)
        nonzero_pct = np.mean(col != 0) * 100
        feature_applicability[fname] = {
            "mean": float(mean_val),
            "std": float(std_val),
            "nonzero_pct": float(nonzero_pct),
        }
        marker = "✗" if nonzero_pct < 1.0 else ("~" if nonzero_pct < 10.0 else "✓")
        print(f"    {fname:<28} {mean_val:>8.2f} {std_val:>8.2f} {nonzero_pct:>7.1f}% {marker}")

    # LF firing rates
    print(f"\n  LF firing rates:")
    for lf_name in ["action_diversity", "command_repetition", "error_accumulation", "majority"]:
        labels = [l[lf_name] for l in all_lf_labels]
        n_prog = sum(1 for v in labels if v == PROGRESS)
        n_stag = sum(1 for v in labels if v == STAGNATION)
        n_abs = sum(1 for v in labels if v == ABSTAIN)
        coverage = (n_prog + n_stag) / len(labels) * 100 if labels else 0
        print(f"    {lf_name:<24} progress={n_prog:>5}  stagnation={n_stag:>5}  "
              f"abstain={n_abs:>5}  coverage={coverage:.1f}%")

    # If we have outcome labels, check correlation
    results = {
        "name": name,
        "domain": domain,
        "n_trajectories": len(trajectories),
        "n_windows": n_windows,
        "step_stats": {
            "mean": float(np.mean(step_counts)),
            "median": float(np.median(step_counts)),
            "min": int(min(step_counts)),
            "max": int(max(step_counts)),
        },
        "n_with_outcome": n_with_outcome,
        "n_success": n_success,
        "n_fail": n_fail,
        "feature_applicability": feature_applicability,
    }

    # Outcome-label correlation (if available)
    windows_with_outcome = [(meta, lf) for meta, lf in zip(all_window_meta, all_lf_labels)
                            if meta["outcome"] is not None]
    if len(windows_with_outcome) >= 20:
        # For last windows of trajectories, check if majority label correlates with outcome
        last_windows = {}
        for meta, lf in zip(all_window_meta, all_lf_labels):
            tid = meta["traj_id"]
            if tid not in last_windows or meta["window_idx"] > last_windows[tid][0]["window_idx"]:
                last_windows[tid] = (meta, lf)

        agree = 0
        disagree = 0
        abstain_count = 0
        for tid, (meta, lf) in last_windows.items():
            if meta["outcome"] is None or lf["majority"] == ABSTAIN:
                abstain_count += 1
                continue
            expected = PROGRESS if meta["outcome"] else STAGNATION
            if lf["majority"] == expected:
                agree += 1
            else:
                disagree += 1

        total_labeled = agree + disagree
        if total_labeled > 0:
            accuracy = agree / total_labeled
            print(f"\n  Outcome-label correlation (last window per trajectory):")
            print(f"    Agree: {agree}, Disagree: {disagree}, Abstain: {abstain_count}")
            print(f"    Accuracy: {accuracy:.3f} (n={total_labeled})")
            results["outcome_correlation"] = {
                "agree": agree,
                "disagree": disagree,
                "abstain": abstain_count,
                "accuracy": float(accuracy),
                "n": total_labeled,
            }

    # Save features
    out_path = DATA_DIR / f"{name}_pilot_features.json"
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {out_path}")

    return results


def main():
    print("=" * 60)
    print("  Non-SE Trajectory Pilot Study")
    print("  Cross-domain structural feature evaluation")
    print("=" * 60)

    all_results = {}

    # --- ToolBench ---
    try:
        tb_raw = load_toolbench_from_hf(limit=300)
        if tb_raw:
            tb_trajs = normalize_toolbench(tb_raw)
            r = run_pilot_for_dataset("toolbench", tb_trajs)
            if r:
                all_results["toolbench"] = r
    except Exception as e:
        print(f"[ToolBench] Error: {e}")
        traceback.print_exc()

    # --- ALFWorld ---
    try:
        alf_raw = load_alfworld_from_hf(limit=300)
        if alf_raw:
            alf_trajs = normalize_alfworld(alf_raw)
            r = run_pilot_for_dataset("alfworld", alf_trajs)
            if r:
                all_results["alfworld"] = r
    except Exception as e:
        print(f"[ALFWorld] Error: {e}")
        traceback.print_exc()

    # --- ATBench ---
    try:
        at_raw = load_atbench_from_hf(limit=500)
        if at_raw:
            at_trajs = normalize_atbench(at_raw)
            r = run_pilot_for_dataset("atbench", at_trajs)
            if r:
                all_results["atbench"] = r
    except Exception as e:
        print(f"[ATBench] Error: {e}")
        traceback.print_exc()

    # --- Summary ---
    print("\n" + "=" * 60)
    print("  CROSS-DOMAIN SUMMARY")
    print("=" * 60)

    # Feature applicability comparison
    if len(all_results) >= 2:
        print("\n  Feature applicability across domains (NonZero%):")
        print(f"    {'Feature':<28}", end="")
        for name in all_results:
            print(f" {name:>12}", end="")
        print()
        print(f"    {'-'*28}", end="")
        for _ in all_results:
            print(f" {'-'*12}", end="")
        print()

        for fname in FEATURE_NAMES:
            print(f"    {fname:<28}", end="")
            for name, r in all_results.items():
                pct = r["feature_applicability"].get(fname, {}).get("nonzero_pct", 0)
                marker = "✗" if pct < 1.0 else ("~" if pct < 10.0 else "✓")
                print(f" {pct:>9.1f}% {marker}", end="")
            print()

    # Categorize features by cross-domain applicability
    domain_general = []
    partially_applicable = []
    se_specific = []

    for fname in FEATURE_NAMES:
        pcts = []
        for name, r in all_results.items():
            pct = r["feature_applicability"].get(fname, {}).get("nonzero_pct", 0)
            pcts.append(pct)
        if not pcts:
            continue
        if all(p >= 10 for p in pcts):
            domain_general.append(fname)
        elif any(p >= 10 for p in pcts):
            partially_applicable.append(fname)
        else:
            se_specific.append(fname)

    print(f"\n  Feature categories:")
    print(f"    Domain-general ({len(domain_general)}): {', '.join(domain_general)}")
    print(f"    Partially applicable ({len(partially_applicable)}): {', '.join(partially_applicable)}")
    print(f"    SE-specific ({len(se_specific)}): {', '.join(se_specific)}")

    # Save combined results
    combined_path = DATA_DIR / "pilot_study_combined.json"
    with open(combined_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\n  Combined results saved to {combined_path}")

    return all_results


if __name__ == "__main__":
    results = main()
