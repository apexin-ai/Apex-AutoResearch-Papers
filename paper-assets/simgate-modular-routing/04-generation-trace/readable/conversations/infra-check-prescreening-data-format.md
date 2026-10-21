# infra check prescreening data format

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_infra_check-prescreening-data-format_20260513T171711.jsonl`
- **Structured JSON:** [`5a295e0ff27a704da4fe.json`](../../sessions/5a/5a295e0ff27a704da4fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-13T17:17:58.911195+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T17:17:58.911494+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T17:17:58.911664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "cat /root/autodl-tmp/simgate-modular-routing/src/signal_prescreening.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat /root/autodl-tmp/simgate-modular-routing/src/signal_prescreening.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T17:17:58.911793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "cat /root/autodl-tmp/simgate-modular-routing/src/phase1_signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat /root/autodl-tmp/simgate-modular-routing/src/phase1_signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T17:17:58.911911+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "find /root/autodl-tmp/simgate-modular-routing/results/prescreening/ -name \"*.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "find /root/autodl-tmp/simgate-modular-routing/results/prescreening/ -name \"*.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T17:17:58.912191+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Lightweight 2-way prescreening: always-internal vs always-deterministic.\\n\\nSimplified version of phase1_signal.py for quick signal checks.\\nRuns fewer episodes (default 5) on a single task type,\\noutputs per-episode JSONL and a terminal summary with Δ(D-I) direction.\\n\\nKey differences from phase1_signal.py:\\n  - No oracle-routing mode (2-way only)\\n  - always-internal does NOT use death filter (pure LLM)\\n  - always-deterministic uses death filter via fork_and_lookahead\\n  - Single task type per invocation (--task_type, not comma-separated)\\n\\nUsage:\\n  python src/signal_prescreening.py --task_type boil --episodes 5 --gpu_id 0\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nimport time\\nfrom typing import Dict, Any\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom scienceworld_utils import (\\n    create_env, reset_env, get_valid_actions, get_score,\\n    step_env, close_env, fork_and_lookahead, get_task_types,\\n    get_max_variations,\\n)\\nfrom llm_agent import LLMAgent, find_model_path\\n\\n\\ndef resolve_task_type(name: str) -> str:\\n    \\\"\\\"\\\"Resolve short task name to ScienceWorld task name.\\\"\\\"\\\"\\n    try:\\n        available = get_task_types()\\n    except Exception:\\n        return name\\n    if name in available:\\n        return name\\n    matches = [t for t in available if name.lower() in t.lower()]\\n    if matches:\\n        return matches[0]\\n    return name\\n\\n\\ndef is_lethal(fr: Dict[str, Any]) -> bool:\\n    \\\"\\\"\\\"Check if a fork result indicates a lethal action.\\\"\\\"\\\"\\n    if fr[\\\"done\\\"] and fr[\\\"score\\\"] < 0:\\n        return True\\n    if fr[\\\"score\\\"] <= -100:\\n        return True\\n    return False\\n\\n\\ndef run_episode_internal(\\n    agent: LLMAgent,\\n    task_name: str,\\n    variation_idx: int,\\n    max_steps: int,\\n) -> Dict[str, Any]:\
…[truncated 7312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T17:17:58.912368+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "find /root/autodl-tmp/simgate-modular-routing/results/mvp/ -name \"episodes.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "find /root/autodl-tmp/simgate-modular-routing/results/mvp/ -name \"episodes.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T17:17:58.912618+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 1: 3-way signal detection — always-internal vs always-deterministic vs oracle-routing.\\n\\nFor each task type × episode:\\n  A) always-internal: ReAct LLM picks every action\\n  B) always-deterministic: LLM generates candidates, fork evaluates each, pick best score_delta\\n  C) oracle-routing: run both A and B, pick whichever has higher score_delta\\n\\nUsage:\\n  python src/phase1_signal.py --task_types \\\"boil,melt\\\" --episodes 20 --gpu_id 0\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nimport time\\nfrom typing import List, Dict, Any, Optional\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom scienceworld_utils import (\\n    create_env, reset_env, get_valid_actions, get_score,\\n    step_env, close_env, fork_and_lookahead, get_task_types,\\n    get_max_variations,\\n    STRONG_TASKS, MEDIUM_TASKS, WEAK_TASKS, ALL_MVP_TASKS,\\n)\\nfrom llm_agent import LLMAgent, find_model_path\\n\\n\\ndef resolve_task_type(name: str) -> str:\\n    \\\"\\\"\\\"Resolve a short task name to the actual ScienceWorld task name.\\\"\\\"\\\"\\n    try:\\n        available = get_task_types()\\n    except Exception:\\n        return name\\n    if name in available:\\n        return name\\n    matches = [t for t in available if name.lower() in t.lower()]\\n    if matches:\\n        return matches[0]\\n    return name\\n\\n\\ndef is_lethal(fr: Dict[str, Any]) -> bool:\\n    \\\"\\\"\\\"Check if a fork result indicates a lethal action.\\\"\\\"\\\"\\n    if fr[\\\"done\\\"] and fr[\\\"score\\\"] < 0:\\n        return True\\n    if fr[\\\"score\\\"] <= -100:\\n        return True\\n    return False\\n\\n\\ndef run_episode_always_internal(\\n    agent: LLMAgent,\\n    task_name: str,\\n    variation_idx: int,\\n    max_steps: int,\\n) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Mode A: LLM ReAct picks every action.\\\"\\\"\\\"\\n    env = create_env(task
…[truncated 7269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T17:17:58.912775+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/simgate-modular-routing/results/prescreening/chemistry-mix/episodes.jsonl\\n/root/autodl-tmp/simgate-modular-routing/results/prescreening/chemistry-mix-paint-tertiary-color/episodes.jsonl\\n/root/autodl-tmp/simgate-modular-routing/results/prescreening/find-animal/episodes.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T17:17:58.912902+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/simgate-modular-routing/results/mvp/boil/episodes.jsonl\\n/root/autodl-tmp/simgate-modular-routing/results/mvp/chemistry-mix-paint-secondary-color/episodes.jsonl\\n/root/autodl-tmp/simgate-modular-routing/results/mvp/melt/episodes.jsonl\\n/root/autodl-tmp/simgate-modular-routing/results/mvp/grow-plant/episodes.jsonl\\n/root/autodl-tmp/simgate-modular-routing/results/mvp/change-the-state-of-matter-of/episodes.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T17:17:58.913072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "head -c 3000 /root/autodl-tmp/simgate-modular-routing/results/prescreening/chemistry-mix/episodes.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "head -c 3000 /root/autodl-tmp/simgate-modular-routing/results/prescreening/chemistry-mix/episodes.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T17:17:58.913246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"episode_idx\\\": 0, \\\"variation_idx\\\": 0, \\\"always_internal\\\": {\\\"mode\\\": \\\"always-internal\\\", \\\"task_name\\\": \\\"chemistry-mix\\\", \\\"variation_idx\\\": 0, \\\"final_score\\\": -100.0, \\\"initial_score\\\": 0.0, \\\"num_steps\\\": 17, \\\"total_time_s\\\": 40.495187520980835, \\\"steps\\\": [{\\\"step\\\": 0, \\\"action\\\": \\\"connect agent to air\\\", \\\"modality\\\": \\\"internal\\\", \\\"score_before\\\": 0.0, \\\"score_after\\\": 0.0, \\\"score_delta\\\": 0.0, \\\"observation\\\": \\\"terminal 1 on agent is now connected to terminal 1 on air\\\", \\\"llm_output\\\": \\\"Thought: The agent is currently in the hallway, and the task is not specified. A good first step is to connect the agent to the air, as this is a basic interaction that can provide information about the air quality or simply confirm the agent's presence in the environment.\\\\nAction: connect agent to a\\\"}, {\\\"step\\\": 1, \\\"action\\\": \\\"connect agent to art studio\\\", \\\"modality\\\": \\\"internal\\\", \\\"score_before\\\": 0.0, \\\"score_after\\\": 0.0, \\\"score_delta\\\": 0.0, \\\"observation\\\": \\\"terminal 2 on agent is now connected to terminal 1 on art studio\\\", \\\"llm_output\\\": \\\"Thought: The agent is already connected to the air, so the next logical step would be to explore the environment by connecting to other locations. Since the current observation mentions that the terminal 1 on the agent is now connected to terminal 1 on air, it implies that the agent is in a location\\\"}, {\\\"step\\\": 2, \\\"action\\\": \\\"connect air to art studio\\\", \\\"modality\\\": \\\"internal\\\", \\\"score_before\\\": 0.0, \\\"score_after\\\": 0.0, \\\"score_delta\\\": 0.0, \\\"observation\\\": \\\"terminal 2 on air is now connected to terminal 2 on art studio\\\", \\\"llm_output\\\": \\\"Thought: The agent is now connected to the art studio, and we need to establish an air connection to the ar
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T17:17:58.913388+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "ls -d /root/autodl-tmp/simgate-modular-routing/results/prescreening/*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "ls -d /root/autodl-tmp/simgate-modular-routing/results/prescreening/*/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T17:17:58.913509+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/simgate-modular-routing/results/prescreening/chemistry-mix-paint-tertiary-color/\\n/root/autodl-tmp/simgate-modular-routing/results/prescreening/chemistry-mix/\\n/root/autodl-tmp/simgate-modular-routing/results/prescreening/find-animal/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T17:17:58.913630+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "ps -p 650421 -o pid,etime 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "ps -p 650421 -o pid,etime 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T17:17:58.913745+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T17:17:58.913854+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "tail -5 /tmp/research-boil-v3-gpu1.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "tail -5 /tmp/research-boil-v3-gpu1.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T17:17:58.913998+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\rProcessed prompts:   0%|          | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.03it/s, est. speed input: 951.22 toks/s, output: 101.80 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.03it/s, est. speed input: 951.22 toks/s, output: 101.80 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.03it/s, est. speed input: 951.22 toks/s, output: 101.80 toks/s]\\n\\rRendering prompts:   0%|          | 0/1 [00:00<?, ?it/s]\\rRendering prompts: 100%|██████████| 1/1 [00:00<00:00, 162.95it/s]\\n\\rProcessed prompts:   0%|          | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.24it/s, est. speed input: 1143.46 toks/s, output: 101.47 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.24it/s, est. speed input: 1143.46 toks/s, output: 101.47 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.24it/s, est. speed input: 1143.46 toks/s, output: 101.47 toks/s]\\n\\rRendering prompts:   0%|          | 0/1 [00:00<?, ?it/s]\\rRendering prompts: 100%|██████████| 1/1 [00:00<00:00, 104.15it/s]\\n\\rProcessed prompts:   0%|          | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.26it/s, est. speed input: 1160.27 toks/s, output: 101.82 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.26it/s, est. speed input: 1160.27 toks/s, output: 101.82 toks/s]\\rProcessed prompts: 100%|██████████| 1/1 [00:00<00:00,  1.26it/s, est. speed input: 1160.27 toks/s, output: 101.82 toks/s]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T17:17:58.914153+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "ps -p 650421 -o pid,etime",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "ps -p 650421 -o pid,etime",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T17:17:58.914278+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED\\n650421       54:16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T17:17:58.914427+00:00_

结果：

### 1. signal_prescreening.py — **保存 step-level 数据 ✓**

每步保存到 `steps` 数组，字段：
- `step` (步序号)
- `action` (执行的动作)
- `modality` ("internal" 或 "deterministic")
- `score_before`, `score_after`, `score_delta`
- `observation` (截断到 500 字符)
- `llm_output` (截断到 300 字符)

deterministic 模式额外保存：
- `candidates` (候选动作列表)
- `fork_results` (每个候选的 fork 评估结果)
- `chosen_action`, `chosen_score_delta`
- `death_filtered` (致死过滤的动作列表)

episode 级别还保存：`action_history`（完整动作序列）。

**缺失：** 没有保存 `valid_actions`（当步可选动作全集）。

### 2. phase1_signal.py — **保存 step-level 数据 ✓**

结构与 prescreening 完全一致。三种模式（always-internal / always-deterministic / oracle-routing）都保存相同的 step-level 字段。oracle 模式每步额外记录 `routing_choice`（选了 internal 还是 deterministic）。

同样 **缺失 `valid_actions`**。

### 3. 预筛进度

完成 **3 个 task**：
- `chemistry-mix`
- `chemistry-mix-paint-tertiary-color`
- `find-animal`

### 4. GPU1 boil v3 进度

PID 650421 仍在运行，已运行 **54 分钟**。日志显示 vLLM 推理正在正常执行（~1 it/s）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_infra_check-prescreening-data-format_20260513T171711"
}
```

</details>

---
