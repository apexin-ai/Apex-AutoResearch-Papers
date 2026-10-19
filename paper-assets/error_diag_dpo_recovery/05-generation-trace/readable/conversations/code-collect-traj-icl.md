# code collect traj icl

**error diag dpo recovery** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_code_collect_traj_icl_20260512T173518.jsonl`
- **Structured JSON:** [`9fb14947f12e95a38fb6.json`](../../sessions/9f/9fb14947f12e95a38fb6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-12T17:39:52.057479+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T17:39:52.057886+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T17:39:52.058064+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T17:39:52.058579+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"ALFWorld trajectory collection with Qwen3-8B direct inference.\\n\\nUsage:\\n  python src/collect_trajectories.py \\\\\\n    --model_name /root/autodl-tmp/.hf_cache/Qwen3-8B \\\\\\n    --output_dir data/trajectories \\\\\\n    --split train \\\\\\n    --temperature 0.7 \\\\\\n    --max_steps 40 \\\\\\n    --gpu 0 \\\\\\n    --num_tasks 100\\n\\\"\\\"\\\"\\n\\n# Fix: episode boundary handling\\n# Ensure done/reward check happens BEFORE appending the terminal observation.\\n# This prevents contamination if the env auto-resets and returns a new game's\\n# observation at the done boundary. Each trajectory must be an independent\\n# single-task episode.\\n\\n\\nimport os\\nimport re\\nimport json\\nimport time\\nimport gc\\nimport sys\\nimport logging\\nimport argparse\\nimport faulthandler\\nfrom pathlib import Path\\nfrom collections import defaultdict\\nfrom difflib import SequenceMatcher\\n\\nimport yaml\\nimport torch\\nimport alfworld\\nfrom alfworld.agents.environment import get_environment\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\n\\nlogger = logging.getLogger(\\\"collect_traj\\\")\\n\\nPREFIXES = {\\n    \\\"pick_and_place\\\": \\\"put\\\",\\n    \\\"pick_clean_then_place\\\": \\\"clean\\\",\\n    \\\"pick_heat_then_place\\\": \\\"heat\\\",\\n    \\\"pick_cool_then_place\\\": \\\"cool\\\",\\n    \\\"look_at_obj\\\": \\\"examine\\\",\\n    \\\"pick_two_obj\\\": \\\"puttwo\\\",\\n}\\n\\nETO_ROOT = \\\"/root/autodl-tmp/rl-active-probe-fl/eto_repo\\\"\\nSFT_DATA = os.path.join(ETO_ROOT, \\\"data/alfworld_sft.json\\\")\\nICL_TYPES = [\\\"pick_and_place\\\", \\\"pick_clean_then_place\\\", \\\"look_at_obj\\\"]\\n\\n\\ndef get_task_type(game_file: str) -> str:\\n    for k in PREFIXES:\\n        if f\\\"/{k}\\\" in game_file:\\n            return k\\n    return \\\"unknown\\\"\\n\\n\\ndef process_ob(ob: str) -> str:\\n    if ob.startswith(\\\"You arrive at loc \
…[truncated 7307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T17:39:52.058847+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json') as f:\n    data = json.load(f)\nprint(json.dumps(data[0], indent=2)[:3000])\nprint('---TOTAL_ENTRIES:', len(data))\nprint('---KEYS:', list(data[0].keys()))\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json') as f:\n    data = json.load(f)\nprint(json.dumps(data[0], indent=2)[:3000])\nprint('---TOTAL_ENTRIES:', len(data))\nprint('---KEYS:', list(data[0].keys()))\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T17:39:52.059002+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T17:39:52.059173+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -500 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -500 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T17:39:52.059457+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"ALFWorld trajectory collection with Qwen3-8B direct inference.\\n\\nUsage:\\n  python src/collect_trajectories.py \\\\\\n    --model_name /root/autodl-tmp/.hf_cache/Qwen3-8B \\\\\\n    --output_dir data/trajectories \\\\\\n    --split train \\\\\\n    --temperature 0.7 \\\\\\n    --max_steps 40 \\\\\\n    --gpu 0 \\\\\\n    --num_tasks 100\\n\\\"\\\"\\\"\\n\\n# Fix: episode boundary handling\\n# Ensure done/reward check happens BEFORE appending the terminal observation.\\n# This prevents contamination if the env auto-resets and returns a new game's\\n# observation at the done boundary. Each trajectory must be an independent\\n# single-task episode.\\n\\n\\nimport os\\nimport re\\nimport json\\nimport time\\nimport gc\\nimport sys\\nimport logging\\nimport argparse\\nimport faulthandler\\nfrom pathlib import Path\\nfrom collections import defaultdict\\nfrom difflib import SequenceMatcher\\n\\nimport yaml\\nimport torch\\nimport alfworld\\nfrom alfworld.agents.environment import get_environment\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\n\\nlogger = logging.getLogger(\\\"collect_traj\\\")\\n\\nPREFIXES = {\\n    \\\"pick_and_place\\\": \\\"put\\\",\\n    \\\"pick_clean_then_place\\\": \\\"clean\\\",\\n    \\\"pick_heat_then_place\\\": \\\"heat\\\",\\n    \\\"pick_cool_then_place\\\": \\\"cool\\\",\\n    \\\"look_at_obj\\\": \\\"examine\\\",\\n    \\\"pick_two_obj\\\": \\\"puttwo\\\",\\n}\\n\\nETO_ROOT = \\\"/root/autodl-tmp/rl-active-probe-fl/eto_repo\\\"\\nSFT_DATA = os.path.join(ETO_ROOT, \\\"data/alfworld_sft.json\\\")\\nICL_TYPES = [\\\"pick_and_place\\\", \\\"pick_clean_then_place\\\", \\\"look_at_obj\\\"]\\n\\n\\ndef get_task_type(game_file: str) -> str:\\n    for k in PREFIXES:\\n        if f\\\"/{k}\\\" in game_file:\\n            return k\\n    return \\\"unknown\\\"\\n\\n\\ndef process_ob(ob: str) -> str:\\n    if ob.startswith(\\\"You arrive at loc \
…[truncated 7307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T17:39:52.059618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T17:39:52.059779+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T17:39:52.059942+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/rl-active-probe-fl -name \"alfworld_sft.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/rl-active-probe-fl -name \"alfworld_sft.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T17:39:52.060134+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/rl-active-probe-fl/eto_repo/hf_data/data/alfworld_sft.json\\n/root/autodl-tmp/rl-active-probe-fl/eto_repo/data/alfworld_sft.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T17:39:52.060293+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "wc -l /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "wc -l /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T17:39:52.060420+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"451 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T17:39:52.060538+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +100 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -n +100 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T17:39:52.060830+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    if cool_match:\\n        obj = cool_match.group(1)\\n        for adm in admissible:\\n            if adm.startswith(f\\\"cool {obj}\\\"):\\n                return adm\\n\\n    # toggle X Y -> use X / turn on X / turn off X\\n    toggle_match = re.match(r\\\"toggle (.+?) (.+)\\\", action)\\n    if toggle_match:\\n        obj = toggle_match.group(1)\\n        for adm in admissible:\\n            if f\\\"use {obj}\\\" in adm or f\\\"turn on {obj}\\\" in adm or f\\\"turn off {obj}\\\" in adm:\\n                return adm\\n\\n    # close X -> close X (may not exist)\\n    if action.startswith(\\\"close \\\"):\\n        for adm in admissible:\\n            if adm.startswith(\\\"close \\\"):\\n                return adm\\n\\n    # Fuzzy match: find most similar admissible command\\n    best_score = 0\\n    best_match = action\\n    for adm in admissible:\\n        score = SequenceMatcher(None, action.lower(), adm.lower()).ratio()\\n        if score > best_score:\\n            best_score = score\\n            best_match = adm\\n    if best_score > 0.6:\\n        return best_match\\n\\n    return action\\n\\n\\ndef load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):\\n    \\\"\\\"\\\"Load ALFWorld environment. Returns (generator, n_tasks).\\\"\\\"\\\"\\n    alfworld_data = \\\"/root/autodl-tmp/alfworld_data\\\"\\n    os.environ[\\\"ALFWORLD_DATA\\\"] = alfworld_data\\n\\n    with open(os.path.join(alfworld_data, \\\"base_config.yaml\\\")) as f:\\n        config = yaml.safe_load(f)\\n\\n    split_map = {\\n        \\\"train\\\": (\\\"train\\\", 3321),\\n        \\\"dev\\\": (\\\"eval_in_distribution\\\", 140),\\n        \\\"test\\\": (\\\"eval_out_of_distribution\\\", 134),\\n    }\\n    env_split, n_tasks = split_map[split]\\n\\n    EnvClass = get_environment(config[\\\"env\\\"][\\\"type\\\"])\\n    env = EnvClass(config, train_eval=env_split)\\n    env = env.init_env(batch_size=1)\\n\\n    if par
…[truncated 7267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T17:39:52.061007+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -50 /root/autodl-tmp/rl-active-probe-fl/eto_repo/data/alfworld_sft.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -50 /root/autodl-tmp/rl-active-probe-fl/eto_repo/data/alfworld_sft.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T17:39:52.061193+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\r\\n    {\\r\\n        \\\"id\\\": \\\"alfworld_0\\\",\\r\\n        \\\"game_file\\\": \\\"data/json_2.1.1/train/pick_and_place_simple-ToiletPaper-None-ToiletPaperHanger-406/trial_T20190908_122807_136741\\\",\\r\\n        \\\"conversations\\\": [\\r\\n            {\\r\\n                \\\"from\\\": \\\"human\\\",\\r\\n                \\\"value\\\": \\\"Interact with a household to solve a task. Imagine you are an intelligent agent in a household environment and your target is to perform actions to complete the task goal. At the beginning of your interactions, you will be given the detailed description of the current environment and your goal to accomplish. \\\\nFor each of your turn, you will be given the observation of the last turn. You should first think about the current condition and plan for your future actions, and then output your action in this turn. Your output must strictly follow this format:\\\\\\\"Thought: your thoughts.\\\\\\\\nAction: your next action\\\\\\\".\\\\n\\\\nThe available actions are:\\\\n1. go to {recep}\\\\n2. task {obj} from {recep}\\\\n3. put {obj} in/on {recep}\\\\n4. open {recep}\\\\n5. close {recep}\\\\n6. toggle {obj} {recep}\\\\n7. clean {obj} with {recep}\\\\n8. heat {obj} with {recep}\\\\n9. cool {obj} with {recep}\\\\nwhere {obj} and {recep} correspond to objects and receptacles.\\\\nAfter your each turn, the environment will give you immediate feedback based on which you plan your next few steps. if the envrionment output \\\\\\\"Nothing happened\\\\\\\", that means the previous action is invalid and you should try more options.\\\\n\\\\nYour response should use the following format:\\\\n\\\\nThought: &lt;your thoughts>\\\\nAction: &lt;your next action>\\\"\\r\\n            },\\r\\n            {\\r\\n                \\\"from\\\": \\\"gpt\\\",\\r\\n                \\\"value\\\": \\\"OK\\\"\\r\\n            },\\r\\n            {\\r\\n                \\\"from\\\": \\\"human\\\
…[truncated 2425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T17:39:52.061372+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +200 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -n +200 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T17:39:52.061664+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        instruction = f.read().strip()\\n\\n    with open(SFT_DATA) as f:\\n        sft_data = json.load(f)\\n\\n    by_type = defaultdict(list)\\n    for item in sft_data:\\n        tt = get_task_type(item[\\\"game_file\\\"])\\n        if tt not in ICL_TYPES:\\n            continue\\n        convs = item[\\\"conversations\\\"]\\n        if len(convs) > 2:\\n            interaction = convs[2:]\\n        else:\\n            continue\\n        n_turns = len(interaction)\\n        if n_turns <= 12:\\n            by_type[tt].append((n_turns, interaction, item[\\\"game_file\\\"]))\\n\\n    icl_examples = []\\n    for tt in ICL_TYPES:\\n        candidates = by_type.get(tt, [])\\n        candidates.sort(key=lambda x: x[0])\\n        n, turns, gf = candidates[0]\\n        msgs = []\\n        for turn in turns:\\n            role = \\\"user\\\" if turn[\\\"from\\\"] == \\\"human\\\" else \\\"assistant\\\"\\n            msgs.append({\\\"role\\\": role, \\\"content\\\": turn[\\\"value\\\"]})\\n        icl_examples.append(msgs)\\n        logger.info(f\\\"ICL example: type={tt} turns={n} game={gf}\\\")\\n\\n    return instruction, icl_examples\\n\\n\\ndef build_initial_messages(instruction: str, icl_examples: list, task_obs: str) -> list:\\n    \\\"\\\"\\\"Build initial conversation with ICL examples in 'conversation' format.\\\"\\\"\\\"\\n    messages = [\\n        {\\\"role\\\": \\\"user\\\", \\\"content\\\": instruction},\\n        {\\\"role\\\": \\\"assistant\\\", \\\"content\\\": \\\"OK\\\"},\\n    ]\\n\\n    for example in icl_examples:\\n        for turn in example:\\n            messages.append({\\\"role\\\": turn[\\\"role\\\"], \\\"content\\\": turn[\\\"content\\\"]})\\n\\n    messages.append({\\\"role\\\": \\\"user\\\", \\\"content\\\": task_obs})\\n    return messages\\n\\n\\ndef generate_response(\\n    model, tokenizer, messages: list,\\n    temperature: float = 0.7, max_new_tokens: int = 256,\\n) -> str:\\n   
…[truncated 7304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T17:39:52.061841+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -n \"def \" /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -n \"def \" /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T17:39:52.061982+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"56:def get_task_type(game_file: str) -> str:\\n63:def process_ob(ob: str) -> str:\\n69:def translate_action(action: str, admissible: list) -> str:\\n134:def load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):\\n160:    def generator():\\n177:def load_model(model_name: str, gpu: int = 0):\\n197:def load_prompt_resources():\\n234:def build_initial_messages(instruction: str, icl_examples: list, task_obs: str) -> list:\\n249:def generate_response(\\n284:def parse_action(response: str) -> str:\\n294:def collect_single_trajectory(\\n362:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T17:39:52.062137+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -n +310 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -n +310 /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-12T17:39:52.062267+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/rl-active-probe-fl/eto_repo/eval_agent/prompt/instructions/alfworld_inst.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/rl-active-probe-fl/eto_repo/eval_agent/prompt/instructions/alfworld_inst.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T17:39:52.062459+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    messages = build_initial_messages(instruction, icl_examples, task_obs)\\n\\n    reward = False\\n    steps = 0\\n    translated_count = 0\\n\\n    for _ in range(max_steps):\\n        response = generate_response(\\n            model, tokenizer, messages, temperature, max_new_tokens,\\n        )\\n        raw_action = parse_action(response)\\n        action = translate_action(raw_action, admissible)\\n        if action != raw_action:\\n            translated_count += 1\\n            logger.debug(f\\\"  Translated: {raw_action!r} -> {action!r}\\\")\\n\\n        messages.append({\\\"role\\\": \\\"assistant\\\", \\\"content\\\": response})\\n\\n        try:\\n            observation, env_reward, env_done, info = env.step([action])\\n            observation = process_ob(observation[0])\\n            reward = info[\\\"won\\\"][0]\\n            done = env_done[0]\\n            admissible = info[\\\"admissible_commands\\\"][0]\\n        except Exception as e:\\n            logger.warning(f\\\"Task {task_id} env.step error: {e}\\\")\\n            observation = \\\"Invalid action.\\\"\\n            reward = False\\n            done = False\\n\\n        steps += 1\\n\\n        if done or reward:\\n            if \\\"Your task is to:\\\" not in observation:\\n                messages.append({\\\"role\\\": \\\"user\\\", \\\"content\\\": f\\\"Observation: {observation}\\\"})\\n            else:\\n                logger.warning(f\\\"Task {task_id}: new-game observation detected at done boundary, stripped\\\")\\n            break\\n\\n        messages.append({\\\"role\\\": \\\"user\\\", \\\"content\\\": f\\\"Observation: {observation}\\\"})\\n\\n    return {\\n        \\\"task_id\\\": task_id,\\n        \\\"task_type\\\": task_type,\\n        \\\"game_file\\\": game_file,\\n        \\\"reward\\\": bool(reward),\\n        \\\"steps\\\": steps,\\n        \\\"translated_actions\\\": translated_count,\\n        \\\"conversati
…[truncated 3847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T17:39:52.062621+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Interact with a household to solve a task. Imagine you are an intelligent agent in a household environment and your target is to perform actions to complete the task goal. At the beginning of your interactions, you will be given the detailed description of the current environment and your goal to accomplish. \\nFor each of your turn, you will be given the observation of the last turn. You should first think about the current condition and plan for your future actions, and then output your action in this turn. Your output must strictly follow this format:\\\"Thought: your thoughts.\\\\nAction: your next action\\\".\\n\\nThe available actions are:\\n1. go to {recep}\\n2. take {obj} from {recep}\\n3. put {obj} in/on {recep}\\n4. open {recep}\\n5. close {recep}\\n6. toggle {obj} {recep}\\n7. clean {obj} with {recep}\\n8. heat {obj} with {recep}\\n9. cool {obj} with {recep}\\nwhere {obj} and {recep} correspond to objects and receptacles.\\nAfter your each turn, the environment will give you immediate feedback based on which you plan your next few steps. if the envrionment output \\\"Nothing happened\\\", that means the previous action is invalid and you should try more options.\\n\\nYour response should use the following format:\\n\\nThought: &lt;your thoughts>\\nAction: &lt;your next action>\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T17:39:52.062823+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T17:39:52.062959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"LICENSE\\nREADME.md\\nconfig.json\\ngeneration_config.json\\nmerges.txt\\nmodel-00001-of-00002.safetensors\\nmodel-00002-of-00002.safetensors\\nmodel.safetensors.index.json\\ntokenizer.json\\ntokenizer_config.json\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T17:39:52.063081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/rl-active-probe-fl/data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/rl-active-probe-fl/data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T17:39:52.063205+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"classified\\ncorrection_span_results.jsonl\\ncorrection_test\\nicl_test_results\\nmock_dpo.jsonl\\nsample_validation\\ntrajectories\\ntrajectories_v4_cuda0_residual\\ntrajectories_v4_cuda1\\ntrajectories_v4_test3\\ntrajectories_v4_test3b\\ntrajectories_v4_test_single\\ntrajectories_v5_cuda0\\ntrajectories_v5_cuda1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T17:39:52.063351+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T17:39:52.063500+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"architectures\\\": [\\n    \\\"Qwen3ForCausalLM\\\"\\n  ],\\n  \\\"attention_bias\\\": false,\\n  \\\"attention_dropout\\\": 0.0,\\n  \\\"bos_token_id\\\": 151643,\\n  \\\"eos_token_id\\\": 151645,\\n  \\\"head_dim\\\": 128,\\n  \\\"hidden_act\\\": \\\"silu\\\",\\n  \\\"hidden_size\\\": 5120,\\n  \\\"initializer_range\\\": 0.02,\\n  \\\"intermediate_size\\\": 17408,\\n  \\\"max_position_embeddings\\\": 40960,\\n  \\\"max_window_layers\\\": 40,\\n  \\\"model_type\\\": \\\"qwen3\\\",\\n  \\\"num_attention_heads\\\": 40,\\n  \\\"num_hidden_layers\\\": 40,\\n  \\\"num_key_value_heads\\\": 8,\\n  \\\"quantization_config\\\": {\\n    \\\"bits\\\": 4,\\n    \\\"group_size\\\": 128,\\n    \\\"modules_to_not_convert\\\": null,\\n    \\\"quant_method\\\": \\\"awq\\\",\\n    \\\"version\\\": \\\"gemm\\\",\\n    \\\"zero_point\\\": true\\n  },\\n  \\\"rms_norm_eps\\\": 1e-06,\\n  \\\"rope_scaling\\\": null,\\n  \\\"rope_theta\\\": 1000000,\\n  \\\"sliding_window\\\": null,\\n  \\\"tie_word_embeddings\\\": false,\\n  \\\"torch_dtype\\\": \\\"float16\\\",\\n  \\\"transformers_version\\\": \\\"4.51.3\\\",\\n  \\\"use_cache\\\": true,\\n  \\\"use_sliding_window\\\": false,\\n  \\\"vocab_size\\\": 151936\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T17:39:52.063749+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ln -sf /root/autodl-tmp/rl-active-probe-fl/eto_repo/data/alfworld_sft.json /root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ln -sf /root/autodl-tmp/rl-active-probe-fl/eto_repo/data/alfworld_sft.json /root/autodl-tmp/rl-active-probe-fl/data/alfworld_sft.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T17:39:52.063900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T17:39:52.064110+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories_icl.py << 'SCRIPT_EOF'\n\"\"\"ALFWorld ICL-enhanced trajectory collection with Qwen3-14B-AWQ.\n\nBackup approach for v5: uses few-shot expert demonstrations matched by task type\nto keep the model on-track longer before diverging, producing more diverse errors.\n\nCompared to collect_trajectories.py (zero-shot with 3 fixed ICL examples from\nfixed task types), this script:\n  - Samples ICL examples matching the CURRENT task's type (task-type-aware)\n  - Uses Qwen3-14B-AWQ (larger model, AWQ quantization)\n  - Adds --seed for reproducibility\n  - Adds --dry_run for I/O pipeline validation without model/env\n\nInput:  alfworld_sft.json (expert trajectories), ALFWorld environment\nOutput: JSONL with same schema as collect_trajectories.py:\n  {\"task_id\", \"task_type\", \"game_file\", \"reward\", \"steps\", \"conversations\"}\n\"\"\"\n\nimport os\nimport re\nimport json\nimport time\nimport gc\nimport sys\nimport random\nimport logging\nimport argparse\nimport faulthandler\nfrom pathlib import Path\nfrom collections import defaultdict\nfrom difflib import SequenceMatcher\n\nlogger = logging.getLogger(\"collect_traj_icl\")\n\nPREFIXES = {\n    \"pick_and_place\": \"put\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"puttwo\",\n}\n\nINSTRUCTION_PATH = os.path.join(\n    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),\n    \"eto_repo/eval_agent/prompt/instructions/alfworld_inst.txt\",\n)\n\n\ndef get_task_type(game_file: str) -> str:\n    \"\"\"Extract task type from game_file path.\"\"\"\n    for k in PREFIXES:\n        if f\"/{k}\" in game_file:\n            return k\n    return \"unknown\"\n\n\ndef process_ob(ob: str) -> str:\n    \"\"\"Strip location prefix from observation.\"\"\"\n    if ob.startswith(\"You arrive at loc \"):\n        ob = ob[ob.find(\". \") + 2:]\n    return ob\n\n\ndef translate_action(action: str, admissible: list) -> str:\n    \"\"\"Translate model's action to match ALFWorld's actual action vocabulary.\"\"\"\n    if action in admissible:\n        return action\n\n    put_match = re.match(r\"put (.+?) (?:in/on|in|on) (.+)\", action)\n    if put_match:\n        obj, recep = put_match.group(1), put_match.group(2)\n        move_action = f\"move {obj} to {recep}\"\n        if move_action in admissible:\n            return move_action\n\n    clean_match = re.match(r\"clean (.+?) with (.+)\", action)\n    if clean_match:\n        obj = clean_match.group(1)\n        for adm in admissible:\n            if adm.startswith(f\"wash {obj}\") or adm.startswith(f\"clean {obj}\"):\n                return adm\n\n    heat_match = re.match(r\"heat (.+?) with (.+)\", action)\n    if heat_match:\n        obj = heat_match.group(1)\n        for adm in admissible:\n            if adm.startswith(f\"heat {obj}\") or adm.startswith(f\"cook {obj}\"):\n                return adm\n\n    cool_match = re.match(r\"cool (.+?) with (.+)\", action)\n    if cool_match:\n        obj = cool_match.group(1)\n        for adm in admissible:\n            if adm.startswith(f\"cool {obj}\"):\n                return adm\n\n    toggle_match = re.match(r\"toggle (.+?) (.+)\", action)\n    if toggle_match:\n        obj = toggle_match.group(1)\n        for adm in admissible:\n            if f\"use {obj}\" in adm or f\"turn on {obj}\" in adm or f\"turn off {obj}\" in adm:\n                return adm\n\n    if action.startswith(\"close \"):\n        for adm in admissible:\n            if adm.startswith(\"close \"):\n                return adm\n\n    best_score = 0\n    best_match = action\n    for adm in admissible:\n        score = SequenceMatcher(None, action.lower(), adm.lower()).ratio()\n        if score > best_score:\n            best_score = score\n            best_match = adm\n    if best_score > 0.6:\n        return best_match\n\n    return action\n\n\ndef load_expert_examples(expert_file: str) -> dict:\n    \"\"\"Load expert trajectories from alfworld_sft.json, indexed by task type.\n\n    Returns dict: {task_type: [list of conversation sequences]}.\n    Each conversation sequence is a list of {\"role\", \"content\"} messages\n    representing one complete expert episode (task obs + action/observation pairs).\n    The instruction prefix (conversations[0:2]) is excluded.\n    \"\"\"\n    with open(expert_file) as f:\n        sft_data = json.load(f)\n\n    by_type = defaultdict(list)\n    for item in sft_data:\n        tt = get_task_type(item[\"game_file\"])\n        convs = item[\"conversations\"]\n        # conversations[0] = instruction (human), [1] = \"OK\" (gpt), [2:] = interaction\n        if len(convs) <= 2:\n            continue\n        interaction = convs[2:]\n        msgs = []\n        for turn in interaction:\n            role = \"user\" if turn[\"from\"] == \"human\" else \"assistant\"\n            msgs.append({\"role\": role, \"content\": turn[\"value\"]})\n        by_type[tt].append(msgs)\n\n    return dict(by_type)\n\n\ndef sample_icl_examples(expert_by_type: dict, task_type: str,\n                        num_examples: int, rng: random.Random) -> list:\n    \"\"\"Sample ICL examples matching the current task type.\n\n    Prioritizes same-type examples. If fewer than num_examples available for\n    this type, fills remaining slots from other types (preferring shorter\n    trajectories to save context window).\n    \"\"\"\n    candidates = expert_by_type.get(task_type, [])\n\n    if len(candidates) >= num_examples:\n        return rng.sample(candidates, num_examples)\n\n    selected = list(candidates)\n    remaining = num_examples - len(selected)\n    other = []\n    for tt, examples in expert_by_type.items():\n        if tt != task_type:\n            other.extend(examples)\n    # Prefer shorter trajectories when falling back to other types\n    other.sort(key=lambda x: len(x))\n    if remaining > 0 and other:\n        selected.extend(rng.sample(other[:max(remaining * 5, 20)], min(remaining, len(other))))\n\n    return selected\n\n\ndef build_icl_messages(instruction: str, icl_examples: list, task_obs: str) -> list:\n    \"\"\"Build initial conversation with ICL expert demonstrations as prefix.\n\n    Layout:\n      [system instruction] -> [OK]\n      [example_1 task obs] -> [example_1 thought+action] -> [obs] -> ... -> [success]\n      [example_2 task obs] -> [example_2 thought+action] -> [obs] -> ... -> [success]\n      [current task observation]\n\n    Each ICL example is a complete successful trajectory showing the model how\n    to solve a task of the same type step by step.\n    \"\"\"\n    messages = [\n        {\"role\": \"user\", \"content\": instruction},\n        {\"role\": \"assistant\", \"content\": \"OK\"},\n    ]\n\n    for example in icl_examples:\n        for turn in example:\n            messages.append({\"role\": turn[\"role\"], \"content\": turn[\"content\"]})\n\n    messages.append({\"role\": \"user\", \"content\": task_obs})\n    return messages\n\n\ndef load_model(model_name: str, gpu: int = 0):\n    \"\"\"Load AWQ-quantized model (quantization auto-detected from config.json).\"\"\"\n    import torch\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name,\n        device_map=f\"cuda:{gpu}\",\n        trust_remote_code=True,\n    )\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    model.eval()\n    return model, tokenizer\n\n\ndef load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):\n    \"\"\"Load ALFWorld environment. Returns (generator, n_tasks).\"\"\"\n    import yaml\n    import alfworld\n    from alfworld.agents.environment import get_environment\n\n    alfworld_data = \"/root/autodl-tmp/alfworld_data\"\n    os.environ[\"ALFWORLD_DATA\"] = alfworld_data\n\n    with open(os.path.join(alfworld_data, \"base_config.yaml\")) as f:\n        config = yaml.safe_load(f)\n\n    split_map = {\n        \"train\": (\"train\", 3321),\n        \"dev\": (\"eval_in_distribution\", 140),\n        \"test\": (\"eval_out_of_distribution\", 134),\n    }\n    env_split, n_tasks = split_map[split]\n\n    EnvClass = get_environment(config[\"env\"][\"type\"])\n    env = EnvClass(config, train_eval=env_split)\n    env = env.init_env(batch_size=1)\n\n    if part_num > 1:\n        assert part_idx >= 0\n        part_sizes = [n_tasks // part_num] * part_num\n        part_sizes[-1] += n_tasks % part_num\n        env.skip(sum(part_sizes[:part_idx]))\n        n_tasks = part_sizes[part_idx]\n\n    def generator():\n        for idx in range(n_tasks):\n            obs, info = env.reset()\n            obs_text = \"\\n\".join(obs[0].split(\"\\n\\n\")[1:])\n            game_file = info[\"extra.gamefile\"][0]\n            admissible = info[\"admissible_commands\"][0]\n            yield {\n                \"task_id\": idx,\n                \"game_file\": game_file,\n                \"obs\": obs_text,\n                \"env\": env,\n                \"admissible\": admissible,\n            }\n\n    return generator(), n_tasks\n\n\ndef generate_response(model, tokenizer, messages, temperature=0.5, max_new_tokens=256):\n    \"\"\"Generate response with Qwen3 thinking mode disabled.\"\"\"\n    import torch\n\n    try:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n            enable_thinking=False,\n        )\n    except TypeError:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n        )\n\n    inputs = tokenizer(text, return_tensors=\"pt\").to(model.device)\n\n    with torch.no_grad():\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=max_new_tokens,\n            do_sample=temperature > 0,\n            temperature=temperature if temperature > 0 else None,\n            top_p=0.9 if temperature > 0 else None,\n            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,\n        )\n\n    new_tokens = outputs[0][inputs[\"input_ids\"].shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    response = re.sub(r\"&lt;think>.*?&lt;/think>\", \"\", response, flags=re.DOTALL).strip()\n    return response\n\n\ndef parse_action(response: str) -> str:\n    \"\"\"Extract action from 'Thought: ...\\\\nAction: ...' format.\"\"\"\n    match = re.search(r\"Action:\\s*(.*)\", response, re.DOTALL)\n    if match:\n        action = match.group(1).strip().split(\"\\n\")[0].strip()\n        if action:\n            return action\n    return \"look\"\n\n\ndef collect_single_trajectory(\n    task_info, model, tokenizer,\n    instruction, expert_by_type, rng,\n    num_icl_examples=2,\n    temperature=0.5,\n    max_steps=40,\n    max_new_tokens=256,\n):\n    \"\"\"Run one episode with task-type-matched ICL demonstrations.\"\"\"\n    import torch\n\n    env = task_info[\"env\"]\n    task_obs = task_info[\"obs\"]\n    game_file = task_info[\"game_file\"]\n    task_id = task_info[\"task_id\"]\n    task_type = get_task_type(game_file)\n    admissible = task_info[\"admissible\"]\n\n    # Sample ICL examples matching this task's type\n    icl_examples = sample_icl_examples(expert_by_type, task_type, num_icl_examples, rng)\n    logger.debug(f\"Task {task_id}: sampled {len(icl_examples)} ICL examples for type={task_type}\")\n\n    messages = build_icl_messages(instruction, icl_examples, task_obs)\n\n    reward = False\n    steps = 0\n    translated_count = 0\n\n    for _ in range(max_steps):\n        response = generate_response(\n            model, tokenizer, messages, temperature, max_new_tokens,\n        )\n        raw_action = parse_action(response)\n        action = translate_action(raw_action, admissible)\n        if action != raw_action:\n            translated_count += 1\n            logger.debug(f\"  Translated: {raw_action!r} -> {action!r}\")\n\n        messages.append({\"role\": \"assistant\", \"content\": response})\n\n        try:\n            observation, env_reward, env_done, info = env.step([action])\n            observation = process_ob(observation[0])\n            reward = info[\"won\"][0]\n            done = env_done[0]\n            admissible = info[\"admissible_commands\"][0]\n        except Exception as e:\n            logger.warning(f\"Task {task_id} env.step error: {e}\")\n            observation = \"Invalid action.\"\n            reward = False\n            done = False\n\n        steps += 1\n\n        if done or reward:\n            if \"Your task is to:\" not in observation:\n                messages.append({\"role\": \"user\", \"content\": f\"Observation: {observation}\"})\n            else:\n                logger.warning(f\"Task {task_id}: new-game observation at done boundary, stripped\")\n            break\n\n        messages.append({\"role\": \"user\", \"content\": f\"Observation: {observation}\"})\n\n    return {\n        \"task_id\": task_id,\n        \"task_type\": task_type,\n        \"game_file\": game_file,\n        \"reward\": bool(reward),\n        \"steps\": steps,\n        \"translated_actions\": translated_count,\n        \"conversations\": messages,\n    }\n\n\ndef dry_run(args, instruction, expert_by_type, rng):\n    \"\"\"Validate I/O pipeline without loading model or connecting to ALFWorld.\n\n    Checks: ICL sampling per task type, prompt construction, output JSONL format.\n    \"\"\"\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n    output_file = output_dir / \"train.jsonl\"\n\n    task_types = list(expert_by_type.keys())\n    logger.info(f\"Expert data: {', '.join(f'{tt}={len(exs)}' for tt, exs in expert_by_type.items())}\")\n\n    with open(output_file, \"w\") as f:\n        for i in range(min(args.num_tasks, len(task_types) * 2)):\n            tt = task_types[i % len(task_types)]\n\n            icl_examples = sample_icl_examples(expert_by_type, tt, args.num_icl_examples, rng)\n\n            fake_obs = (\n                f\"You are in the middle of a room. Looking quickly around you, you see \"\n                f\"a countertop 1, a cabinet 1, a shelf 1.\\n\\n\"\n                f\"Your task is to: [DRY-RUN placeholder for {tt}]\"\n            )\n            messages = build_icl_messages(instruction, icl_examples, fake_obs)\n\n            icl_turn_count = sum(len(ex) for ex in icl_examples)\n            logger.info(\n                f\"Task {i}: type={tt}, icl_examples={len(icl_examples)}, \"\n                f\"icl_turns={icl_turn_count}, total_prompt_turns={len(messages)}\"\n            )\n\n            # Print detailed ICL prompt for first task\n            if i == 0:\n                logger.info(\"=\" * 60)\n                logger.info(\"ICL Prompt Structure (task 0):\")\n                logger.info(\"=\" * 60)\n                for j, msg in enumerate(messages):\n                    preview = msg[\"content\"][:120].replace(\"\\n\", \"\\\\n\")\n                    if j < 4 or j >= len(messages) - 2:\n                        logger.info(f\"  turn {j:3d} [{msg['role']:9s}] {preview}...\")\n                    elif j == 4:\n                        logger.info(f\"  ... ({len(messages) - 6} turns omitted) ...\")\n                logger.info(\"=\" * 60)\n\n            traj = {\n                \"task_id\": i,\n                \"task_type\": tt,\n                \"game_file\": f\"dry_run/{tt}/trial_000\",\n                \"reward\": False,\n                \"steps\": 0,\n                \"conversations\": messages,\n            }\n            f.write(json.dumps(traj, ensure_ascii=False) + \"\\n\")\n\n    logger.info(f\"Dry-run output written: {output_file}\")\n\n    # Validate output format\n    with open(output_file) as f:\n        for line_num, line in enumerate(f, 1):\n            record = json.loads(line)\n            required = {\"task_id\", \"task_type\", \"game_file\", \"reward\", \"steps\", \"conversations\"}\n            missing = required - set(record.keys())\n            assert not missing, f\"Line {line_num} missing keys: {missing}\"\n            assert isinstance(record[\"conversations\"], list)\n            assert isinstance(record[\"reward\"], bool)\n            assert isinstance(record[\"steps\"], int)\n    logger.info(f\"Output format validated: {line_num} records, all fields present and correct types\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\"Collect ALFWorld trajectories with ICL few-shot\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ\")\n    parser.add_argument(\"--expert_file\", type=str, default=\"data/alfworld_sft.json\",\n                        help=\"Path to alfworld_sft.json expert trajectories\")\n    parser.add_argument(\"--num_icl_examples\", type=int, default=2,\n                        help=\"Number of few-shot expert examples per task\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"data/trajectories_icl\")\n    parser.add_argument(\"--split\", type=str, default=\"train\", choices=[\"train\", \"dev\", \"test\"])\n    parser.add_argument(\"--temperature\", type=float, default=0.5)\n    parser.add_argument(\"--max_steps\", type=int, default=40)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=256)\n    parser.add_argument(\"--gpu\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=250)\n    parser.add_argument(\"--seed\", type=int, default=0)\n    parser.add_argument(\"--dry_run\", action=\"store_true\",\n                        help=\"Validate I/O pipeline without model/env\")\n    parser.add_argument(\"--part_num\", type=int, default=1)\n    parser.add_argument(\"--part_idx\", type=int, default=-1)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s %(levelname)s %(message)s\",\n        handlers=[logging.StreamHandler(sys.stderr)],\n    )\n    faulthandler.enable()\n\n    rng = random.Random(args.seed)\n\n    with open(INSTRUCTION_PATH) as f:\n        instruction = f.read().strip()\n\n    logger.info(f\"Loading expert data: {args.expert_file}\")\n    expert_by_type = load_expert_examples(args.expert_file)\n    logger.info(f\"Expert types: {', '.join(f'{k}={len(v)}' for k, v in expert_by_type.items())}\")\n\n    if args.dry_run:\n        dry_run(args, instruction, expert_by_type, rng)\n        return\n\n    logger.info(f\"Loading model: {args.model_name}\")\n    model, tokenizer = load_model(args.model_name, args.gpu)\n\n    logger.info(f\"Loading ALFWorld {args.split} environment...\")\n    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)\n\n    if args.num_tasks > 0:\n        n_tasks = min(n_tasks, args.num_tasks)\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n    suffix = f\"_part{args.part_idx}\" if args.part_num > 1 else \"\"\n    output_file = output_dir / f\"{args.split}{suffix}.jsonl\"\n\n    logger.info(f\"Collecting {n_tasks} trajectories -> {output_file}\")\n\n    success_count = 0\n    total_count = 0\n\n    import torch\n\n    with open(output_file, \"w\") as f:\n        for i, task_info in enumerate(task_gen):\n            if i >= n_tasks:\n                break\n\n            t0 = time.time()\n            try:\n                traj = collect_single_trajectory(\n                    task_info, model, tokenizer,\n                    instruction, expert_by_type, rng,\n                    num_icl_examples=args.num_icl_examples,\n                    temperature=args.temperature,\n                    max_steps=args.max_steps,\n                    max_new_tokens=args.max_new_tokens,\n                )\n            except Exception:\n                logger.error(f\"Task {i} crashed:\", exc_info=True)\n                total_count += 1\n                continue\n            elapsed = time.time() - t0\n\n            total_count += 1\n            if traj[\"reward\"]:\n                success_count += 1\n\n            f.write(json.dumps(traj, ensure_ascii=False) + \"\\n\")\n            f.flush()\n\n            logger.info(\n                f\"[{total_count}/{n_tasks}] task={traj['task_id']} \"\n                f\"type={traj['task_type']} reward={traj['reward']} \"\n                f\"steps={traj['steps']} xlat={traj['translated_actions']} \"\n                f\"time={elapsed:.1f}s sr={success_count}/{total_count}\"\n            )\n            del traj\n            gc.collect()\n            torch.cuda.empty_cache()\n\n    logger.info(\n        f\"Done. {success_count}/{total_count} succeeded \"\n        f\"({success_count / max(total_count, 1) * 100:.1f}%)\"\n    )\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/autodl-tmp/rl-active-probe-fl/src/collect_trajectories_icl.py << 'SCRIPT_EOF'\n\"\"\"ALFWorld ICL-enhanced trajectory collection with Qwen3-14B-AWQ.\n\nBackup approach for v5: uses few-shot expert demonstrations matched by task type\nto keep the model on-track longer before diverging, producing more diverse errors.\n\nCompared to collect_trajectories.py (zero-shot with 3 fixed ICL examples from\nfixed task types), this script:\n  - Samples ICL examples matching the CURRENT task's type (task-type-aware)\n  - Uses Qwen3-14B-AWQ (larger model, AWQ quantization)\n  - Adds --seed for reproducibility\n  - Adds --dry_run for I/O pipeline validation without model/env\n\nInput:  alfworld_sft.json (expert trajectories), ALFWorld environment\nOutput: JSONL with same schema as collect_trajectories.py:\n  {\"task_id\", \"task_type\", \"game_file\", \"reward\", \"steps\", \"conversations\"}\n\"\"\"\n\nimport os\nimport re\nimport json\nimport time\nimport gc\nimport sys\nimport random\nimport logging\nimport argparse\nimport faulthandler\nfrom pathlib import Path\nfrom collections import defaultdict\nfrom difflib import SequenceMatcher\n\nlogger = logging.getLogger(\"collect_traj_icl\")\n\nPREFIXES = {\n    \"pick_and_place\": \"put\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"puttwo\",\n}\n\nINSTRUCTION_PATH = os.path.join(\n    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),\n    \"eto_repo/eval_agent/prompt/instructions/alfworld_inst.txt\",\n)\n\n\ndef get_task_type(game_file: str) -> str:\n    \"\"\"Extract task type from game_file path.\"\"\"\n    for k in PREFIXES:\n        if f\"/{k}\" in game_file:\n            return k\n    return \"unknown\"\n\n\ndef process_ob(ob: str) -> str:\n    \"\"\"Strip location prefix from observation.\"\"\"\n    if ob.startswith(\"You arrive at loc \"):\n        ob = ob[ob.find(\". \") + 2:]\n    return ob\n\n\ndef translate_action(action: str, admissible: list) -> str:\n    \"\"\"Translate model's action to match ALFWorld's actual action vocabulary.\"\"\"\n    if action in admissible:\n        return action\n\n    put_match = re.match(r\"put (.+?) (?:in/on|in|on) (.+)\", action)\n    if put_match:\n        obj, recep = put_match.group(1), put_match.group(2)\n        move_action = f\"move {obj} to {recep}\"\n        if move_action in admissible:\n            return move_action\n\n    clean_match = re.match(r\"clean (.+?) with (.+)\", action)\n    if clean_match:\n        obj = clean_match.group(1)\n        for adm in admissible:\n            if adm.startswith(f\"wash {obj}\") or adm.startswith(f\"clean {obj}\"):\n                return adm\n\n    heat_match = re.match(r\"heat (.+?) with (.+)\", action)\n    if heat_match:\n        obj = heat_match.group(1)\n        for adm in admissible:\n            if adm.startswith(f\"heat {obj}\") or adm.startswith(f\"cook {obj}\"):\n                return adm\n\n    cool_match = re.match(r\"cool (.+?) with (.+)\", action)\n    if cool_match:\n        obj = cool_match.group(1)\n        for adm in admissible:\n            if adm.startswith(f\"cool {obj}\"):\n                return adm\n\n    toggle_match = re.match(r\"toggle (.+?) (.+)\", action)\n    if toggle_match:\n        obj = toggle_match.group(1)\n        for adm in admissible:\n            if f\"use {obj}\" in adm or f\"turn on {obj}\" in adm or f\"turn off {obj}\" in adm:\n                return adm\n\n    if action.startswith(\"close \"):\n        for adm in admissible:\n            if adm.startswith(\"close \"):\n                return adm\n\n    best_score = 0\n    best_match = action\n    for adm in admissible:\n        score = SequenceMatcher(None, action.lower(), adm.lower()).ratio()\n        if score > best_score:\n            best_score = score\n            best_match = adm\n    if best_score > 0.6:\n        return best_match\n\n    return action\n\n\ndef load_expert_examples(expert_file: str) -> dict:\n    \"\"\"Load expert trajectories from alfworld_sft.json, indexed by task type.\n\n    Returns dict: {task_type: [list of conversation sequences]}.\n    Each conversation sequence is a list of {\"role\", \"content\"} messages\n    representing one complete expert episode (task obs + action/observation pairs).\n    The instruction prefix (conversations[0:2]) is excluded.\n    \"\"\"\n    with open(expert_file) as f:\n        sft_data = json.load(f)\n\n    by_type = defaultdict(list)\n    for item in sft_data:\n        tt = get_task_type(item[\"game_file\"])\n        convs = item[\"conversations\"]\n        # conversations[0] = instruction (human), [1] = \"OK\" (gpt), [2:] = interaction\n        if len(convs) <= 2:\n            continue\n        interaction = convs[2:]\n        msgs = []\n        for turn in interaction:\n            role = \"user\" if turn[\"from\"] == \"human\" else \"assistant\"\n            msgs.append({\"role\": role, \"content\": turn[\"value\"]})\n        by_type[tt].append(msgs)\n\n    return dict(by_type)\n\n\ndef sample_icl_examples(expert_by_type: dict, task_type: str,\n                        num_examples: int, rng: random.Random) -> list:\n    \"\"\"Sample ICL examples matching the current task type.\n\n    Prioritizes same-type examples. If fewer than num_examples available for\n    this type, fills remaining slots from other types (preferring shorter\n    trajectories to save context window).\n    \"\"\"\n    candidates = expert_by_type.get(task_type, [])\n\n    if len(candidates) >= num_examples:\n        return rng.sample(candidates, num_examples)\n\n    selected = list(candidates)\n    remaining = num_examples - len(selected)\n    other = []\n    for tt, examples in expert_by_type.items():\n        if tt != task_type:\n            other.extend(examples)\n    # Prefer shorter trajectories when falling back to other types\n    other.sort(key=lambda x: len(x))\n    if remaining > 0 and other:\n        selected.extend(rng.sample(other[:max(remaining * 5, 20)], min(remaining, len(other))))\n\n    return selected\n\n\ndef build_icl_messages(instruction: str, icl_examples: list, task_obs: str) -> list:\n    \"\"\"Build initial conversation with ICL expert demonstrations as prefix.\n\n    Layout:\n      [system instruction] -> [OK]\n      [example_1 task obs] -> [example_1 thought+action] -> [obs] -> ... -> [success]\n      [example_2 task obs] -> [example_2 thought+action] -> [obs] -> ... -> [success]\n      [current task observation]\n\n    Each ICL example is a complete successful trajectory showing the model how\n    to solve a task of the same type step by step.\n    \"\"\"\n    messages = [\n        {\"role\": \"user\", \"content\": instruction},\n        {\"role\": \"assistant\", \"content\": \"OK\"},\n    ]\n\n    for example in icl_examples:\n        for turn in example:\n            messages.append({\"role\": turn[\"role\"], \"content\": turn[\"content\"]})\n\n    messages.append({\"role\": \"user\", \"content\": task_obs})\n    return messages\n\n\ndef load_model(model_name: str, gpu: int = 0):\n    \"\"\"Load AWQ-quantized model (quantization auto-detected from config.json).\"\"\"\n    import torch\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name,\n        device_map=f\"cuda:{gpu}\",\n        trust_remote_code=True,\n    )\n    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)\n    model.eval()\n    return model, tokenizer\n\n\ndef load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):\n    \"\"\"Load ALFWorld environment. Returns (generator, n_tasks).\"\"\"\n    import yaml\n    import alfworld\n    from alfworld.agents.environment import get_environment\n\n    alfworld_data = \"/root/autodl-tmp/alfworld_data\"\n    os.environ[\"ALFWORLD_DATA\"] = alfworld_data\n\n    with open(os.path.join(alfworld_data, \"base_config.yaml\")) as f:\n        config = yaml.safe_load(f)\n\n    split_map = {\n        \"train\": (\"train\", 3321),\n        \"dev\": (\"eval_in_distribution\", 140),\n        \"test\": (\"eval_out_of_distribution\", 134),\n    }\n    env_split, n_tasks = split_map[split]\n\n    EnvClass = get_environment(config[\"env\"][\"type\"])\n    env = EnvClass(config, train_eval=env_split)\n    env = env.init_env(batch_size=1)\n\n    if part_num > 1:\n        assert part_idx >= 0\n        part_sizes = [n_tasks // part_num] * part_num\n        part_sizes[-1] += n_tasks % part_num\n        env.skip(sum(part_sizes[:part_idx]))\n        n_tasks = part_sizes[part_idx]\n\n    def generator():\n        for idx in range(n_tasks):\n            obs, info = env.reset()\n            obs_text = \"\\n\".join(obs[0].split(\"\\n\\n\")[1:])\n            game_file = info[\"extra.gamefile\"][0]\n            admissible = info[\"admissible_commands\"][0]\n            yield {\n                \"task_id\": idx,\n                \"game_file\": game_file,\n                \"obs\": obs_text,\n                \"env\": env,\n                \"admissible\": admissible,\n            }\n\n    return generator(), n_tasks\n\n\ndef generate_response(model, tokenizer, messages, temperature=0.5, max_new_tokens=256):\n    \"\"\"Generate response with Qwen3 thinking mode disabled.\"\"\"\n    import torch\n\n    try:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n            enable_thinking=False,\n        )\n    except TypeError:\n        text = tokenizer.apply_chat_template(\n            messages, tokenize=False, add_generation_prompt=True,\n        )\n\n    inputs = tokenizer(text, return_tensors=\"pt\").to(model.device)\n\n    with torch.no_grad():\n        outputs = model.generate(\n            **inputs,\n            max_new_tokens=max_new_tokens,\n            do_sample=temperature > 0,\n            temperature=temperature if temperature > 0 else None,\n            top_p=0.9 if temperature > 0 else None,\n            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,\n        )\n\n    new_tokens = outputs[0][inputs[\"input_ids\"].shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    response = re.sub(r\"&lt;think>.*?&lt;/think>\", \"\", response, flags=re.DOTALL).strip()\n    return response\n\n\ndef parse_action(response: str) -> str:\n    \"\"\"Extract action from 'Thought: ...\\\\nAction: ...' format.\"\"\"\n    match = re.search(r\"Action:\\s*(.*)\", response, re.DOTALL)\n    if match:\n        action = match.group(1).strip().split(\"\\n\")[0].strip()\n        if action:\n            return action\n    return \"look\"\n\n\ndef collect_single_trajectory(\n    task_info, model, tokenizer,\n    instruction, expert_by_type, rng,\n    num_icl_examples=2,\n    temperature=0.5,\n    max_steps=40,\n    max_new_tokens=256,\n):\n    \"\"\"Run one episode with task-type-matched ICL demonstrations.\"\"\"\n    import torch\n\n    env = task_info[\"env\"]\n    task_obs = task_info[\"obs\"]\n    game_file = task_info[\"game_file\"]\n    task_id = task_info[\"task_id\"]\n    task_type = get_task_type(game_file)\n    admissible = task_info[\"admissible\"]\n\n    # Sample ICL examples matching this task's type\n    icl_examples = sample_icl_examples(expert_by_type, task_type, num_icl_examples, rng)\n    logger.debug(f\"Task {task_id}: sampled {len(icl_examples)} ICL examples for type={task_type}\")\n\n    messages = build_icl_messages(instruction, icl_examples, task_obs)\n\n    reward = False\n    steps = 0\n    translated_count = 0\n\n    for _ in range(max_steps):\n        response = generate_response(\n            model, tokenizer, messages, temperature, max_new_tokens,\n        )\n        raw_action = parse_action(response)\n        action = translate_action(raw_action, admissible)\n        if action != raw_action:\n            translated_count += 1\n            logger.debug(f\"  Translated: {raw_action!r} -> {action!r}\")\n\n        messages.append({\"role\": \"assistant\", \"content\": response})\n\n        try:\n            observation, env_reward, env_done, info = env.step([action])\n            observation = process_ob(observation[0])\n            reward = info[\"won\"][0]\n            done = env_done[0]\n            admissible = info[\"admissible_commands\"][0]\n        except Exception as e:\n            logger.warning(f\"Task {task_id} env.step error: {e}\")\n            observation = \"Invalid action.\"\n            reward = False\n            done = False\n\n        steps += 1\n\n        if done or reward:\n            if \"Your task is to:\" not in observation:\n                messages.append({\"role\": \"user\", \"content\": f\"Observation: {observation}\"})\n            else:\n                logger.warning(f\"Task {task_id}: new-game observation at done boundary, stripped\")\n            break\n\n        messages.append({\"role\": \"user\", \"content\": f\"Observation: {observation}\"})\n\n    return {\n        \"task_id\": task_id,\n        \"task_type\": task_type,\n        \"game_file\": game_file,\n        \"reward\": bool(reward),\n        \"steps\": steps,\n        \"translated_actions\": translated_count,\n        \"conversations\": messages,\n    }\n\n\ndef dry_run(args, instruction, expert_by_type, rng):\n    \"\"\"Validate I/O pipeline without loading model or connecting to ALFWorld.\n\n    Checks: ICL sampling per task type, prompt construction, output JSONL format.\n    \"\"\"\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n    output_file = output_dir / \"train.jsonl\"\n\n    task_types = list(expert_by_type.keys())\n    logger.info(f\"Expert data: {', '.join(f'{tt}={len(exs)}' for tt, exs in expert_by_type.items())}\")\n\n    with open(output_file, \"w\") as f:\n        for i in range(min(args.num_tasks, len(task_types) * 2)):\n            tt = task_types[i % len(task_types)]\n\n            icl_examples = sample_icl_examples(expert_by_type, tt, args.num_icl_examples, rng)\n\n            fake_obs = (\n                f\"You are in the middle of a room. Looking quickly around you, you see \"\n                f\"a countertop 1, a cabinet 1, a shelf 1.\\n\\n\"\n                f\"Your task is to: [DRY-RUN placeholder for {tt}]\"\n            )\n            messages = build_icl_messages(instruction, icl_examples, fake_obs)\n\n            icl_turn_count = sum(len(ex) for ex in icl_examples)\n            logger.info(\n                f\"Task {i}: type={tt}, icl_examples={len(icl_examples)}, \"\n                f\"icl_turns={icl_turn_count}, total_prompt_turns={len(messages)}\"\n            )\n\n            # Print detailed ICL prompt for first task\n            if i == 0:\n                logger.info(\"=\" * 60)\n                logger.info(\"ICL Prompt Structure (task 0):\")\n                logger.info(\"=\" * 60)\n                for j, msg in enumerate(messages):\n                    preview = msg[\"content\"][:120].replace(\"\\n\", \"\\\\n\")\n                    if j < 4 or j >= len(messages) - 2:\n                        logger.info(f\"  turn {j:3d} [{msg['role']:9s}] {preview}...\")\n                    elif j == 4:\n                        logger.info(f\"  ... ({len(messages) - 6} turns omitted) ...\")\n                logger.info(\"=\" * 60)\n\n            traj = {\n                \"task_id\": i,\n                \"task_type\": tt,\n                \"game_file\": f\"dry_run/{tt}/trial_000\",\n                \"reward\": False,\n                \"steps\": 0,\n                \"conversations\": messages,\n            }\n            f.write(json.dumps(traj, ensure_ascii=False) + \"\\n\")\n\n    logger.info(f\"Dry-run output written: {output_file}\")\n\n    # Validate output format\n    with open(output_file) as f:\n        for line_num, line in enumerate(f, 1):\n            record = json.loads(line)\n            required = {\"task_id\", \"task_type\", \"game_file\", \"reward\", \"steps\", \"conversations\"}\n            missing = required - set(record.keys())\n            assert not missing, f\"Line {line_num} missing keys: {missing}\"\n            assert isinstance(record[\"conversations\"], list)\n            assert isinstance(record[\"reward\"], bool)\n            assert isinstance(record[\"steps\"], int)\n    logger.info(f\"Output format validated: {line_num} records, all fields present and correct types\")\n\n\ndef main():\n    parser = argparse.ArgumentParser(\"Collect ALFWorld trajectories with ICL few-shot\")\n    parser.add_argument(\"--model_name\", type=str, default=\"/root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ\")\n    parser.add_argument(\"--expert_file\", type=str, default=\"data/alfworld_sft.json\",\n                        help=\"Path to alfworld_sft.json expert trajectories\")\n    parser.add_argument(\"--num_icl_examples\", type=int, default=2,\n                        help=\"Number of few-shot expert examples per task\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"data/trajectories_icl\")\n    parser.add_argument(\"--split\", type=str, default=\"train\", choices=[\"train\", \"dev\", \"test\"])\n    parser.add_argument(\"--temperature\", type=float, default=0.5)\n    parser.add_argument(\"--max_steps\", type=int, default=40)\n    parser.add_argument(\"--max_new_tokens\", type=int, default=256)\n    parser.add_argument(\"--gpu\", type=int, default=0)\n    parser.add_argument(\"--num_tasks\", type=int, default=250)\n    parser.add_argument(\"--seed\", type=int, default=0)\n    parser.add_argument(\"--dry_run\", action=\"store_true\",\n                        help=\"Validate I/O pipeline without model/env\")\n    parser.add_argument(\"--part_num\", type=int, default=1)\n    parser.add_argument(\"--part_idx\", type=int, default=-1)\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s %(levelname)s %(message)s\",\n        handlers=[logging.StreamHandler(sys.stderr)],\n    )\n    faulthandler.enable()\n\n    rng = random.Random(args.seed)\n\n    with open(INSTRUCTION_PATH) as f:\n        instruction = f.read().strip()\n\n    logger.info(f\"Loading expert data: {args.expert_file}\")\n    expert_by_type = load_expert_examples(args.expert_file)\n    logger.info(f\"Expert types: {', '.join(f'{k}={len(v)}' for k, v in expert_by_type.items())}\")\n\n    if args.dry_run:\n        dry_run(args, instruction, expert_by_type, rng)\n        return\n\n    logger.info(f\"Loading model: {args.model_name}\")\n    model, tokenizer = load_model(args.model_name, args.gpu)\n\n    logger.info(f\"Loading ALFWorld {args.split} environment...\")\n    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)\n\n    if args.num_tasks > 0:\n        n_tasks = min(n_tasks, args.num_tasks)\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n    suffix = f\"_part{args.part_idx}\" if args.part_num > 1 else \"\"\n    output_file = output_dir / f\"{args.split}{suffix}.jsonl\"\n\n    logger.info(f\"Collecting {n_tasks} trajectories -> {output_file}\")\n\n    success_count = 0\n    total_count = 0\n\n    import torch\n\n    with open(output_file, \"w\") as f:\n        for i, task_info in enumerate(task_gen):\n            if i >= n_tasks:\n                break\n\n            t0 = time.time()\n            try:\n                traj = collect_single_trajectory(\n                    task_info, model, tokenizer,\n                    instruction, expert_by_type, rng,\n                    num_icl_examples=args.num_icl_examples,\n                    temperature=args.temperature,\n                    max_steps=args.max_steps,\n                    max_new_tokens=args.max_new_tokens,\n                )\n            except Exception:\n                logger.error(f\"Task {i} crashed:\", exc_info=True)\n                total_count += 1\n                continue\n            elapsed = time.time() - t0\n\n            total_count += 1\n            if traj[\"reward\"]:\n                success_count += 1\n\n            f.write(json.dumps(traj, ensure_ascii=False) + \"\\n\")\n            f.flush()\n\n            logger.info(\n                f\"[{total_count}/{n_tasks}] task={traj['task_id']} \"\n                f\"type={traj['task_type']} reward={traj['reward']} \"\n                f\"steps={traj['steps']} xlat={traj['translated_actions']} \"\n                f\"time={elapsed:.1f}s sr={success_count}/{total_count}\"\n            )\n            del traj\n            gc.collect()\n            torch.cuda.empty_cache()\n\n    logger.info(\n        f\"Done. {success_count}/{total_count} succeeded \"\n        f\"({success_count / max(total_count, 1) * 100:.1f}%)\"\n    )\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T17:39:52.064426+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-12T17:39:52.064578+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cd /root/autodl-tmp/rl-active-probe-fl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python src/collect_trajectories_icl.py --expert_file data/alfworld_sft.json --output_dir /tmp/icl_dry_run --num_tasks 5 --seed 0 --dry_run 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cd /root/autodl-tmp/rl-active-probe-fl && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=\"\" python src/collect_trajectories_icl.py --expert_file data/alfworld_sft.json --output_dir /tmp/icl_dry_run --num_tasks 5 --seed 0 --dry_run 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T17:39:52.064754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-13 01:39:31,680 INFO Loading expert data: data/alfworld_sft.json\\n2026-05-13 01:39:31,858 INFO Expert types: pick_and_place=759, pick_clean_then_place=576, look_at_obj=279, pick_heat_then_place=371, pick_two_obj=662, pick_cool_then_place=472\\n2026-05-13 01:39:31,859 INFO Expert data: pick_and_place=759, pick_clean_then_place=576, look_at_obj=279, pick_heat_then_place=371, pick_two_obj=662, pick_cool_then_place=472\\n2026-05-13 01:39:31,859 INFO Task 0: type=pick_and_place, icl_examples=2, icl_turns=58, total_prompt_turns=61\\n2026-05-13 01:39:31,859 INFO ============================================================\\n2026-05-13 01:39:31,859 INFO ICL Prompt Structure (task 0):\\n2026-05-13 01:39:31,859 INFO ============================================================\\n2026-05-13 01:39:31,859 INFO   turn   0 [user     ] Interact with a household to solve a task. Imagine you are an intelligent agent in a household environment and your targ...\\n2026-05-13 01:39:31,859 INFO   turn   1 [assistant] OK...\\n2026-05-13 01:39:31,859 INFO   turn   2 [user     ] You are in the middle of a room. Looking quickly around you, you see a bed 2, a bed 1, a desk 1, a drawer 11, a drawer 1...\\n2026-05-13 01:39:31,859 INFO   turn   3 [assistant] Thought: The task is to put a CD in the dresser. I need to find a CD first. I will start by checking the nearest surface...\\n2026-05-13 01:39:31,859 INFO   ... (55 turns omitted) ...\\n2026-05-13 01:39:31,859 INFO   turn  59 [assistant] Thought: I'm at shelf 1 with the CD. I'll complete the task by placing the CD here.\\\\nAction: put CD 3 in/on shelf 1...\\n2026-05-13 01:39:31,859 INFO   turn  60 [user     ] You are in the middle of a room. Looking quickly around you, you see a countertop 1, a cabinet 1, a shelf 1.\\\\n\\\\nYour task ...\\n2026-05-13 01:39:31,859 INFO ============================================================\\n2026-05-13 01:39:31,859 INFO Task 1: type=pick_c
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T17:39:52.064935+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -1 /tmp/icl_dry_run/train.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -1 /tmp/icl_dry_run/train.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T17:39:52.065215+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"task_id\\\": 0, \\\"task_type\\\": \\\"pick_and_place\\\", \\\"game_file\\\": \\\"dry_run/pick_and_place/trial_000\\\", \\\"reward\\\": false, \\\"steps\\\": 0, \\\"conversations\\\": [{\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"Interact with a household to solve a task. Imagine you are an intelligent agent in a household environment and your target is to perform actions to complete the task goal. At the beginning of your interactions, you will be given the detailed description of the current environment and your goal to accomplish. \\\\nFor each of your turn, you will be given the observation of the last turn. You should first think about the current condition and plan for your future actions, and then output your action in this turn. Your output must strictly follow this format:\\\\\\\"Thought: your thoughts.\\\\\\\\nAction: your next action\\\\\\\".\\\\n\\\\nThe available actions are:\\\\n1. go to {recep}\\\\n2. take {obj} from {recep}\\\\n3. put {obj} in/on {recep}\\\\n4. open {recep}\\\\n5. close {recep}\\\\n6. toggle {obj} {recep}\\\\n7. clean {obj} with {recep}\\\\n8. heat {obj} with {recep}\\\\n9. cool {obj} with {recep}\\\\nwhere {obj} and {recep} correspond to objects and receptacles.\\\\nAfter your each turn, the environment will give you immediate feedback based on which you plan your next few steps. if the envrionment output \\\\\\\"Nothing happened\\\\\\\", that means the previous action is invalid and you should try more options.\\\\n\\\\nYour response should use the following format:\\\\n\\\\nThought: &lt;your thoughts>\\\\nAction: &lt;your next action>\\\"}, {\\\"role\\\": \\\"assistant\\\", \\\"content\\\": \\\"OK\\\"}, {\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"You are in the middle of a room. Looking quickly around you, you see a bed 2, a bed 1, a desk 1, a drawer 11, a drawer 10, a drawer 9, a drawer 8, a drawer 7, a drawer 6, a drawer 5, a drawer 4, a drawer 3, a drawer 2, a dr
…[truncated 7634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_collect_traj_icl_20260512T173518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-12T17:39:52.065419+00:00_

全部通过。结果汇总：

### 产出

1. **`src/collect_trajectories_icl.py`** 已写入远程服务器

2. **Dry-run 验证结果**（全部通过）：
   - Expert 数据加载：6 种 task type 共 3119 条（pick_and_place=759, pick_clean_then_place=576, look_at_obj=279, pick_heat_then_place=371, pick_two_obj=662, pick_cool_then_place=472）
   - ICL 示例按 task type 正确抽取（每个任务 2 条同类型示例）
   - Prompt 构造格式正确（instruction → OK → ICL example turns → current task obs）
   - 输出 JSONL 格式验证通过：5 条记录，所有必需字段存在且类型正确

3. **ICL prompt 示例**（task 0, pick_and_place 类型）：
   - turn 0 `[user]`: 系统指令（available actions 等）
   - turn 1 `[assistant]`: "OK"
   - turn 2-59: 2 条 pick_and_place expert 轨迹（共 58 turns），包含完整的 task obs → Thought+Action → Observation 序列直到任务完成
   - turn 60 `[user]`: 当前任务观察

### 与 v5 的关键差异
| | collect_trajectories.py | collect_trajectories_icl.py |
|---|---|---|
| ICL 策略 | 3 个固定类型各取最短 1 条 | 按当前任务类型随机抽 2 条同类型 |
| 模型 | Qwen3-8B + BnB 4bit | Qwen3-14B-AWQ |
| temperature | 0.7 | 0.5 |
| seed | 无 | 有（可复现） |
| dry_run | 无 | 有 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_collect_traj_icl_20260512T173518"
}
```

</details>

---
