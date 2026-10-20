# code plan 001b prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_code_plan-001b-prep_20260513T183608.jsonl`
- **Structured JSON:** [`e0877f87566699f762c6.json`](../../sessions/e0/e0877f87566699f762c6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-13T18:38:16.175857+00:00_

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
  "session": "worker_code_plan-001b-prep_20260513T183608",
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

_source line 2 · 2026-05-13T18:38:16.176233+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T18:38:16.176410+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "ls -la /root/autodl-tmp/simgate-modular-routing/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "ls -la /root/autodl-tmp/simgate-modular-routing/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T18:38:16.176546+00:00_

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
  "session": "worker_code_plan-001b-prep_20260513T183608",
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

### Tool result

_source line 5 · 2026-05-13T18:38:16.176693+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 160\\ndrwxr-xr-x 3 root root  4096 May 14 02:33 .\\ndrwxr-xr-x 6 root root   116 May 14 00:22 ..\\ndrwxr-xr-x 2 root root   134 May 13 15:56 __pycache__\\n-rw-r--r-- 1 root root  4981 May 14 01:13 action_divergence_analysis.py\\n-rw-r--r-- 1 root root  7237 May 13 13:15 analysis.py\\n-rw-r--r-- 1 root root 12347 May 14 01:13 counterfactual_labeling.py\\n-rw-r--r-- 1 root root 13874 May 14 01:40 episode_level_collection.py\\n-rw-r--r-- 1 root root 11979 May 13 15:19 llm_agent.py\\n-rw-r--r-- 1 root root  9974 May 13 13:12 phase0_validate_forking.py\\n-rw-r--r-- 1 root root 17186 May 13 16:03 phase1_signal.py\\n-rw-r--r-- 1 root root 12752 May 14 02:33 router_sft_train.py\\n-rw-r--r-- 1 root root   365 May 14 01:06 rule_based_keywords.json\\n-rw-r--r-- 1 root root 11559 May 14 02:33 rule_based_routing.py\\n-rwxr-xr-x 1 root root  2773 May 13 13:15 run_all.sh\\n-rw-r--r-- 1 root root  7516 May 13 13:12 scienceworld_utils.py\\n-rw-r--r-- 1 root root 10786 May 13 23:45 signal_prescreening.py\\n-rw-r--r-- 1 root root  5523 May 14 01:07 tie_rate_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T18:38:16.176959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 1: 3-way signal detection — always-internal vs always-deterministic vs oracle-routing.\\n\\nFor each task type × episode:\\n  A) always-internal: ReAct LLM picks every action\\n  B) always-deterministic: LLM generates candidates, fork evaluates each, pick best score_delta\\n  C) oracle-routing: run both A and B, pick whichever has higher score_delta\\n\\nUsage:\\n  python src/phase1_signal.py --task_types \\\"boil,melt\\\" --episodes 20 --gpu_id 0\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nimport time\\nfrom typing import List, Dict, Any, Optional\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom scienceworld_utils import (\\n    create_env, reset_env, get_valid_actions, get_score,\\n    step_env, close_env, fork_and_lookahead, get_task_types,\\n    get_max_variations,\\n    STRONG_TASKS, MEDIUM_TASKS, WEAK_TASKS, ALL_MVP_TASKS,\\n)\\nfrom llm_agent import LLMAgent, find_model_path\\n\\n\\ndef resolve_task_type(name: str) -> str:\\n    \\\"\\\"\\\"Resolve a short task name to the actual ScienceWorld task name.\\\"\\\"\\\"\\n    try:\\n        available = get_task_types()\\n    except Exception:\\n        return name\\n    if name in available:\\n        return name\\n    matches = [t for t in available if name.lower() in t.lower()]\\n    if matches:\\n        return matches[0]\\n    return name\\n\\n\\ndef is_lethal(fr: Dict[str, Any]) -> bool:\\n    \\\"\\\"\\\"Check if a fork result indicates a lethal action.\\\"\\\"\\\"\\n    if fr[\\\"done\\\"] and fr[\\\"score\\\"] < 0:\\n        return True\\n    if fr[\\\"score\\\"] <= -100:\\n        return True\\n    return False\\n\\n\\ndef run_episode_always_internal(\\n    agent: LLMAgent,\\n    task_name: str,\\n    variation_idx: int,\\n    max_steps: int,\\n) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Mode A: LLM ReAct picks every action.\\\"\\\"\\\"\\n    env = create_env(task
…[truncated 7269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T18:38:16.177242+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "head -200 /root/autodl-tmp/simgate-modular-routing/src/phase1_signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "head -200 /root/autodl-tmp/simgate-modular-routing/src/phase1_signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T18:38:16.177490+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Phase 1: 3-way signal detection — always-internal vs always-deterministic vs oracle-routing.\\n\\nFor each task type × episode:\\n  A) always-internal: ReAct LLM picks every action\\n  B) always-deterministic: LLM generates candidates, fork evaluates each, pick best score_delta\\n  C) oracle-routing: run both A and B, pick whichever has higher score_delta\\n\\nUsage:\\n  python src/phase1_signal.py --task_types \\\"boil,melt\\\" --episodes 20 --gpu_id 0\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nimport time\\nfrom typing import List, Dict, Any, Optional\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom scienceworld_utils import (\\n    create_env, reset_env, get_valid_actions, get_score,\\n    step_env, close_env, fork_and_lookahead, get_task_types,\\n    get_max_variations,\\n    STRONG_TASKS, MEDIUM_TASKS, WEAK_TASKS, ALL_MVP_TASKS,\\n)\\nfrom llm_agent import LLMAgent, find_model_path\\n\\n\\ndef resolve_task_type(name: str) -> str:\\n    \\\"\\\"\\\"Resolve a short task name to the actual ScienceWorld task name.\\\"\\\"\\\"\\n    try:\\n        available = get_task_types()\\n    except Exception:\\n        return name\\n    if name in available:\\n        return name\\n    matches = [t for t in available if name.lower() in t.lower()]\\n    if matches:\\n        return matches[0]\\n    return name\\n\\n\\ndef is_lethal(fr: Dict[str, Any]) -> bool:\\n    \\\"\\\"\\\"Check if a fork result indicates a lethal action.\\\"\\\"\\\"\\n    if fr[\\\"done\\\"] and fr[\\\"score\\\"] < 0:\\n        return True\\n    if fr[\\\"score\\\"] <= -100:\\n        return True\\n    return False\\n\\n\\ndef run_episode_always_internal(\\n    agent: LLMAgent,\\n    task_name: str,\\n    variation_idx: int,\\n    max_steps: int,\\n) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Mode A: LLM ReAct picks every action.\\\"\\\"\\\"\\n    env = create_env(task
…[truncated 5112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T18:38:16.177650+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "cat /root/autodl-tmp/simgate-modular-routing/src/llm_agent.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat /root/autodl-tmp/simgate-modular-routing/src/llm_agent.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T18:38:16.177787+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "cat /root/autodl-tmp/simgate-modular-routing/src/scienceworld_utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat /root/autodl-tmp/simgate-modular-routing/src/scienceworld_utils.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T18:38:16.178097+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"LLM Agent: Qwen2.5-7B-Instruct ReAct agent for ScienceWorld.\\n\\nSupports vLLM serving (default) or HuggingFace transformers local inference.\\nProvides:\\n  - select_action_react(): standard ReAct single-action selection\\n  - generate_candidate_actions(): top-n candidate generation for deterministic routing\\n\\nUsage:\\n  agent = LLMAgent(model_path=\\\"/root/autodl-tmp/models/Qwen2.5-7B-Instruct\\\", gpu_id=0)\\n  action = agent.select_action_react(obs, valid_actions, history)\\n\\\"\\\"\\\"\\n\\nimport os\\nimport re\\nimport glob\\nimport json\\nimport time\\nfrom typing import List, Optional, Tuple\\n\\n# Detect model path: ModelScope or HuggingFace naming conventions\\nMODEL_SEARCH_PATHS = [\\n    \\\"/root/autodl-tmp/models/Qwen2.5-7B-Instruct\\\",\\n    \\\"/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct\\\",\\n    \\\"/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct\\\",\\n    \\\"/root/autodl-tmp/models/qwen/Qwen2.5-7B-Instruct\\\",\\n    \\\"/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-7B-Instruct\\\",\\n]\\n\\n\\ndef find_model_path(hint: Optional[str] = None) -> str:\\n    \\\"\\\"\\\"Find Qwen2.5-7B-Instruct model path on disk.\\\"\\\"\\\"\\n    if hint and os.path.isdir(hint):\\n        return hint\\n    for p in MODEL_SEARCH_PATHS:\\n        if os.path.isdir(p):\\n            return p\\n    # Glob fallback\\n    for pattern in [\\\"/root/autodl-tmp/models/**/Qwen2*7B*Instruct\\\",\\n                    \\\"/root/autodl-tmp/.hf_cache/**/Qwen2*7B*\\\"]:\\n        matches = glob.glob(pattern, recursive=True)\\n        if matches:\\n            return matches[0]\\n    raise FileNotFoundError(\\n        \\\"Cannot find Qwen2.5-7B-Instruct. Searched: \\\" + str(MODEL_SEARCH_PATHS)\\n    )\\n\\n\\n# ---------------------------------------------------------------------------\\n# Prompt templates\\n# ---------------------------------------------------------------------------\\n\\nSY
…[truncated 7146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T18:38:16.178282+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "cat /root/autodl-tmp/simgate-modular-routing/src/episode_level_collection.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat /root/autodl-tmp/simgate-modular-routing/src/episode_level_collection.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T18:38:16.178525+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"ScienceWorld environment utilities: creation, forking via action-replay, episode logging.\\n\\nDependencies: scienceworld (pip install scienceworld)\\nKey constraint: ScienceWorld uses py4j → each env is a separate JVM process.\\nFork = new JVM instance + replay all historical actions.\\n\\\"\\\"\\\"\\n\\nimport time\\nimport os\\nimport traceback\\nfrom typing import List, Tuple, Optional, Dict, Any\\n\\nimport scienceworld\\n\\n# ---------------------------------------------------------------------------\\n# Task type constants — update after running get_task_types() on the server\\n# ---------------------------------------------------------------------------\\nSTRONG_TASKS = [\\n    \\\"boil\\\",\\n    \\\"melt\\\",\\n    \\\"change-the-state-of-matter-of\\\",\\n]\\nMEDIUM_TASKS = [\\n    \\\"chemistry-mix-paint-secondary-color\\\",\\n]\\nWEAK_TASKS = [\\n    \\\"grow-plant\\\",\\n]\\nALL_MVP_TASKS = STRONG_TASKS + MEDIUM_TASKS + WEAK_TASKS\\n\\n\\ndef get_task_types() -> List[str]:\\n    \\\"\\\"\\\"Return all ScienceWorld task type names.\\\"\\\"\\\"\\n    env = scienceworld.ScienceWorldEnv(\\\"\\\")\\n    try:\\n        names = env.get_task_names()\\n    finally:\\n        env.close()\\n    return list(names)\\n\\n\\ndef get_max_variations(task_name: str) -> int:\\n    \\\"\\\"\\\"Return the number of available variations for a task type.\\\"\\\"\\\"\\n    env = scienceworld.ScienceWorldEnv(\\\"\\\")\\n    try:\\n        n = env.get_max_variations(task_name)\\n        return int(n)\\n    except Exception:\\n        return 100\\n    finally:\\n        env.close()\\n\\n\\ndef create_env(task_name: str, variation_idx: int = 0,\\n               simplification_str: str = \\\"\\\") -> scienceworld.ScienceWorldEnv:\\n    \\\"\\\"\\\"Create and initialize a ScienceWorld environment.\\\"\\\"\\\"\\n    env = scienceworld.ScienceWorldEnv(task_name, envStepLimit=100)\\n    env.load(task_name, variation_id
…[truncated 6676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T18:38:16.178828+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Plan C episode-level labeling data collection for router SFT training.\\n#\\n# For each task variation, runs 2 complete episodes (always-internal + always-deterministic),\\n# compares final episode scores to label each step's modality preference.\\n# Reuses run_episode_internal / run_episode_deterministic from signal_prescreening.py.\\n#\\n# Outputs:\\n#   {output_dir}/{task_type}/labeled_steps.jsonl  — one labeled step per line (training data)\\n#   {output_dir}/{task_type}/episode_summary.jsonl — one episode summary per line\\n#\\n# Usage:\\n#   python src/episode_level_collection.py --task_types \\\"boil,melt\\\" --episodes 20 --gpu_id 0\\n\\nimport argparse\\nimport json\\nimport os\\nimport random\\nimport sys\\nimport time\\nfrom typing import List, Dict, Any\\n\\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\nfrom scienceworld_utils import (\\n    create_env, reset_env, get_valid_actions, get_score,\\n    step_env, close_env, fork_and_lookahead, get_task_types,\\n    get_max_variations,\\n)\\nfrom llm_agent import LLMAgent, find_model_path\\n\\nDEATH_THRESHOLD = -100\\n\\n\\ndef resolve_task_type(name: str) -> str:\\n    try:\\n        available = get_task_types()\\n    except Exception:\\n        return name\\n    if name in available:\\n        return name\\n    matches = [t for t in available if name.lower() in t.lower()]\\n    if matches:\\n        return matches[0]\\n    return name\\n\\n\\ndef is_lethal(fr: Dict[str, Any]) -> bool:\\n    if fr[\\\"done\\\"] and fr[\\\"score\\\"] < 0:\\n        return True\\n    if fr[\\\"score\\\"] <= -100:\\n        return True\\n    return False\\n\\n\\ndef run_episode_internal(\\n    agent: LLMAgent,\\n    task_name: str,\\n    variation_idx: int,\\n    max_steps: int,\\n) -> Dict[str, Any]:\\n    \\\"\\\"\\\"Always-internal: pure LLM ReAct, no death filter.\\\"\\\"\\\"\\n    env = create_env(task_name, variation_idx)\\n    obs, _ = reset_env
…[truncated 7230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T18:38:16.179056+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-13313",
  "command": "tail -n +130 /root/autodl-tmp/simgate-modular-routing/src/episode_level_collection.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-13313",
    "command": "tail -n +130 /root/autodl-tmp/simgate-modular-routing/src/episode_level_collection.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T18:38:16.179349+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    t0 = time.time()\\n\\n    for step_idx in range(max_steps):\\n        valid_actions = get_valid_actions(env)\\n        if not valid_actions:\\n            break\\n\\n        candidates, raw_output = agent.generate_candidate_actions(\\n            obs, valid_actions, history_dicts, n=n_candidates\\n        )\\n\\n        best_action = None\\n        best_delta = float(\\\"-inf\\\")\\n        best_action_fallback = None\\n        best_delta_fallback = float(\\\"-inf\\\")\\n        fork_results = []\\n        for cand in candidates:\\n            fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)\\n            lethal = is_lethal(fr)\\n            fork_results.append({\\n                \\\"action\\\": cand,\\n                \\\"score_delta\\\": fr[\\\"score_delta\\\"],\\n                \\\"score\\\": fr[\\\"score\\\"],\\n                \\\"lethal\\\": lethal,\\n            })\\n            if fr[\\\"score_delta\\\"] > best_delta_fallback:\\n                best_delta_fallback = fr[\\\"score_delta\\\"]\\n                best_action_fallback = cand\\n            if not lethal and fr[\\\"score_delta\\\"] > best_delta:\\n                best_delta = fr[\\\"score_delta\\\"]\\n                best_action = cand\\n\\n        if best_action is None:\\n            best_action = best_action_fallback if best_action_fallback else valid_actions[0]\\n\\n        score_before = get_score(env)\\n        obs_new, reward, done, info = step_env(env, best_action)\\n        score_after = get_score(env)\\n\\n        steps.append({\\n            \\\"step\\\": step_idx,\\n            \\\"action\\\": best_action,\\n            \\\"modality\\\": \\\"deterministic\\\",\\n            \\\"score_before\\\": score_before,\\n            \\\"score_after\\\": score_after,\\n            \\\"score_delta\\\": score_after - score_before,\\n            \\\"candidates\\\": fork_results,\\n            \\\"observation\\\": obs_n
…[truncated 7350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T18:38:16.179611+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "cat > /root/autodl-tmp/simgate-modular-routing/src/collect_trajectories.py << 'PYEOF'\n\"\"\"Episode-level counterfactual trajectory collection for router SFT training.\n\nPlan C (D010): For each task type, run N independent episodes under always-internal\nand N under always-deterministic. Compare episode total scores to assign modality\nlabels. Death episodes (score <= -100) automatically lose.\n\nInput:\n  - ScienceWorld task types (via --task_types)\n  - Qwen2.5-7B-Instruct model (via --model_path or auto-detected)\n  - vLLM or HF transformers backend\n\nOutput:\n  - {output_dir}/{task}/raw_episodes.jsonl   — full episode data (both modalities)\n  - {output_dir}/{task}/sft_triples.jsonl    — (observation, action, modality_label) for SFT\n  - {output_dir}/collection_summary.json     — global statistics\n\nDependencies: scienceworld, vllm (or transformers), scienceworld_utils, llm_agent\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nimport time\nfrom typing import List, Dict, Any\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom scienceworld_utils import (\n    create_env, reset_env, get_valid_actions, get_score,\n    step_env, close_env, fork_and_lookahead, get_task_types,\n    get_max_variations,\n)\nfrom llm_agent import LLMAgent, find_model_path\n\nDEATH_THRESHOLD = -100\n\n\ndef resolve_task_type(name: str) -> str:\n    \"\"\"Resolve short task name to ScienceWorld's full task name.\"\"\"\n    try:\n        available = get_task_types()\n    except Exception:\n        return name\n    if name in available:\n        return name\n    matches = [t for t in available if name.lower() in t.lower()]\n    return matches[0] if matches else name\n\n\ndef is_lethal(fr: Dict[str, Any]) -> bool:\n    if fr[\"done\"] and fr[\"score\"] < 0:\n        return True\n    return fr[\"score\"] <= -100\n\n\ndef is_death_episode(final_score: float) -> bool:\n    \"\"\"Check if an episode ended in death (score <= -100).\"\"\"\n    return final_score <= DEATH_THRESHOLD\n\n\ndef run_episode_internal(\n    agent: LLMAgent,\n    task_name: str,\n    variation_idx: int,\n    max_steps: int,\n) -> Dict[str, Any]:\n    \"\"\"Run one always-internal episode. LLM ReAct picks every action.\"\"\"\n    env = create_env(task_name, variation_idx)\n    obs, _ = reset_env(env)\n    initial_score = get_score(env)\n\n    steps = []\n    action_history = []\n    history_dicts = []\n    t0 = time.time()\n\n    for step_idx in range(max_steps):\n        valid_actions = get_valid_actions(env)\n        if not valid_actions:\n            break\n\n        action, raw_output = agent.select_action_react(obs, valid_actions, history_dicts)\n\n        score_before = get_score(env)\n        obs_new, reward, done, info = step_env(env, action)\n        score_after = get_score(env)\n\n        steps.append({\n            \"step_idx\": step_idx,\n            \"observation_text\": obs[:500],\n            \"action_text\": action,\n            \"available_actions\": valid_actions,\n            \"score_before\": score_before,\n            \"score_after\": score_after,\n            \"score_delta\": score_after - score_before,\n            \"is_death\": score_after <= DEATH_THRESHOLD,\n            \"done\": done,\n            \"llm_output\": raw_output[:300],\n        })\n        action_history.append(action)\n        history_dicts.append({\"action\": action, \"observation\": obs_new[:200], \"score\": score_after})\n        obs = obs_new\n\n        if done:\n            break\n\n    final_score = get_score(env)\n    close_env(env)\n\n    return {\n        \"modality\": \"internal\",\n        \"task_name\": task_name,\n        \"variation_idx\": variation_idx,\n        \"final_score\": final_score,\n        \"initial_score\": initial_score,\n        \"is_death\": is_death_episode(final_score),\n        \"num_steps\": len(steps),\n        \"total_time_s\": round(time.time() - t0, 2),\n        \"steps\": steps,\n    }\n\n\ndef run_episode_deterministic(\n    agent: LLMAgent,\n    task_name: str,\n    variation_idx: int,\n    max_steps: int,\n    n_candidates: int = 3,\n) -> Dict[str, Any]:\n    \"\"\"Run one always-deterministic episode. LLM generates candidates, fork evaluates.\"\"\"\n    env = create_env(task_name, variation_idx)\n    obs, _ = reset_env(env)\n    initial_score = get_score(env)\n\n    steps = []\n    action_history = []\n    history_dicts = []\n    t0 = time.time()\n\n    for step_idx in range(max_steps):\n        valid_actions = get_valid_actions(env)\n        if not valid_actions:\n            break\n\n        candidates, raw_output = agent.generate_candidate_actions(\n            obs, valid_actions, history_dicts, n=n_candidates\n        )\n\n        best_action = None\n        best_delta = float(\"-inf\")\n        best_action_fallback = None\n        best_delta_fallback = float(\"-inf\")\n        fork_results = []\n        for cand in candidates:\n            fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)\n            lethal = is_lethal(fr)\n            fork_results.append({\n                \"action\": cand,\n                \"score_delta\": fr[\"score_delta\"],\n                \"score\": fr[\"score\"],\n                \"lethal\": lethal,\n            })\n            if fr[\"score_delta\"] > best_delta_fallback:\n                best_delta_fallback = fr[\"score_delta\"]\n                best_action_fallback = cand\n            if not lethal and fr[\"score_delta\"] > best_delta:\n                best_delta = fr[\"score_delta\"]\n                best_action = cand\n\n        if best_action is None:\n            best_action = best_action_fallback if best_action_fallback else valid_actions[0]\n\n        score_before = get_score(env)\n        obs_new, reward, done, info = step_env(env, best_action)\n        score_after = get_score(env)\n\n        steps.append({\n            \"step_idx\": step_idx,\n            \"observation_text\": obs[:500],\n            \"action_text\": best_action,\n            \"available_actions\": valid_actions,\n            \"score_before\": score_before,\n            \"score_after\": score_after,\n            \"score_delta\": score_after - score_before,\n            \"is_death\": score_after <= DEATH_THRESHOLD,\n            \"done\": done,\n            \"candidates\": fork_results,\n            \"llm_output\": raw_output[:300],\n        })\n        action_history.append(best_action)\n        history_dicts.append({\"action\": best_action, \"observation\": obs_new[:200], \"score\": score_after})\n        obs = obs_new\n\n        if done:\n            break\n\n    final_score = get_score(env)\n    close_env(env)\n\n    return {\n        \"modality\": \"deterministic\",\n        \"task_name\": task_name,\n        \"variation_idx\": variation_idx,\n        \"final_score\": final_score,\n        \"initial_score\": initial_score,\n        \"is_death\": is_death_episode(final_score),\n        \"num_steps\": len(steps),\n        \"total_time_s\": round(time.time() - t0, 2),\n        \"steps\": steps,\n    }\n\n\ndef label_episode_pair(internal_score: float, det_score: float) -> str:\n    \"\"\"Determine which modality wins the episode-level comparison.\n\n    Returns \"deterministic\", \"internal\", or \"tie\".\n    Death episodes (score <= -100) automatically lose.\n    \"\"\"\n    int_death = internal_score <= DEATH_THRESHOLD\n    det_death = det_score <= DEATH_THRESHOLD\n\n    if int_death and det_death:\n        return \"tie\"\n    if int_death:\n        return \"deterministic\"\n    if det_death:\n        return \"internal\"\n\n    if det_score > internal_score:\n        return \"deterministic\"\n    elif internal_score > det_score:\n        return \"internal\"\n    return \"tie\"\n\n\ndef extract_sft_triples(episode: Dict[str, Any], label: str) -> List[Dict[str, Any]]:\n    \"\"\"Extract (observation, action, modality_label) triples from the winning episode.\"\"\"\n    triples = []\n    for step in episode[\"steps\"]:\n        triples.append({\n            \"observation\": step[\"observation_text\"],\n            \"action\": step[\"action_text\"],\n            \"available_actions\": step[\"available_actions\"],\n            \"modality_label\": label,\n            \"task_name\": episode[\"task_name\"],\n            \"variation_idx\": episode[\"variation_idx\"],\n            \"step_idx\": step[\"step_idx\"],\n            \"score_after\": step[\"score_after\"],\n        })\n    return triples\n\n\ndef run_task_collection(\n    agent: LLMAgent,\n    task_name: str,\n    n_episodes: int,\n    max_steps: int,\n    output_dir: str,\n    n_candidates: int = 3,\n) -> Dict[str, Any]:\n    \"\"\"Collect episode-level trajectory data for one task type.\n\n    For each of n_episodes variations:\n      1. Run always-internal episode\n      2. Run always-deterministic episode (same variation)\n      3. Compare final scores → assign modality label\n      4. Extract SFT triples from the winning episode\n\n    Writes raw_episodes.jsonl and sft_triples.jsonl incrementally.\n    \"\"\"\n    task_dir = os.path.join(output_dir, task_name.replace(\" \", \"_\"))\n    os.makedirs(task_dir, exist_ok=True)\n\n    raw_file = os.path.join(task_dir, \"raw_episodes.jsonl\")\n    sft_file = os.path.join(task_dir, \"sft_triples.jsonl\")\n\n    max_var = get_max_variations(task_name)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"TRAJECTORY COLLECTION: {task_name}\")\n    print(f\"Episodes: {n_episodes} | Max steps: {max_steps} | Variations: {max_var}\")\n    print(f\"{'='*60}\")\n\n    label_counts = {\"deterministic\": 0, \"internal\": 0, \"tie\": 0}\n    death_counts = {\"internal\": 0, \"det\": 0, \"both\": 0}\n    total_sft_triples = 0\n    score_gaps = []\n\n    for ep_idx in range(n_episodes):\n        variation_idx = ep_idx % max_var\n        print(f\"\\n--- Episode {ep_idx}/{n_episodes} (variation={variation_idx}) ---\")\n\n        # Run both modalities on the same variation\n        t_ep = time.time()\n        ep_internal = run_episode_internal(agent, task_name, variation_idx, max_steps)\n        ep_det = run_episode_deterministic(agent, task_name, variation_idx, max_steps, n_candidates)\n        ep_time = time.time() - t_ep\n\n        int_score = ep_internal[\"final_score\"]\n        det_score = ep_det[\"final_score\"]\n        label = label_episode_pair(int_score, det_score)\n\n        # Track deaths\n        if ep_internal[\"is_death\"] and ep_det[\"is_death\"]:\n            death_counts[\"both\"] += 1\n        elif ep_internal[\"is_death\"]:\n            death_counts[\"internal\"] += 1\n        elif ep_det[\"is_death\"]:\n            death_counts[\"det\"] += 1\n\n        label_counts[label] += 1\n        score_gap = abs(det_score - int_score)\n        if label != \"tie\":\n            score_gaps.append(score_gap)\n\n        print(f\"  internal={int_score:.1f} | det={det_score:.1f} | label={label} | gap={score_gap:.1f} | {ep_time:.1f}s\")\n\n        # Save raw episode data (both modalities)\n        for ep in [ep_internal, ep_det]:\n            ep_record = {\n                \"episode_idx\": ep_idx,\n                \"label\": label,\n                \"score_gap\": score_gap,\n                **ep,\n            }\n            with open(raw_file, \"a\") as f:\n                f.write(json.dumps(ep_record) + \"\\n\")\n\n        # Extract and save SFT triples from the winning modality only\n        if label == \"tie\":\n            continue\n\n        winning_ep = ep_det if label == \"deterministic\" else ep_internal\n        triples = extract_sft_triples(winning_ep, label)\n        with open(sft_file, \"a\") as f:\n            for t in triples:\n                f.write(json.dumps(t) + \"\\n\")\n        total_sft_triples += len(triples)\n\n    avg_gap = sum(score_gaps) / len(score_gaps) if score_gaps else 0.0\n\n    print(f\"\\n=== {task_name} SUMMARY ===\")\n    print(f\"Labels: det={label_counts['deterministic']} int={label_counts['internal']} tie={label_counts['tie']}\")\n    print(f\"Deaths: int={death_counts['internal']} det={death_counts['det']} both={death_counts['both']}\")\n    print(f\"Avg score gap (non-tie): {avg_gap:.2f}\")\n    print(f\"SFT triples: {total_sft_triples}\")\n\n    return {\n        \"task_name\": task_name,\n        \"n_episodes\": n_episodes,\n        \"label_counts\": label_counts,\n        \"death_counts\": death_counts,\n        \"total_sft_triples\": total_sft_triples,\n        \"avg_score_gap\": avg_gap,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect episode-level counterfactual trajectories for router SFT (Plan C / D010)\"\n    )\n    parser.add_argument(\"--task_types\", type=str, required=True,\n                        help=\"Comma-separated task type names (e.g. 'boil,melt')\")\n    parser.add_argument(\"--episodes\", type=int, default=20,\n                        help=\"Number of episodes per task type (default: 20)\")\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--output_dir\", type=str, default=\"results/trajectories/\",\n                        help=\"Output directory for trajectory data\")\n    parser.add_argument(\"--model_path\", type=str, default=None,\n                        help=\"Path to Qwen2.5-7B-Instruct (auto-detected if omitted)\")\n    parser.add_argument(\"--use_vllm\", action=\"store_true\", default=True,\n                        help=\"Use vLLM backend (default: True)\")\n    parser.add_argument(\"--no_vllm\", action=\"store_true\", default=False,\n                        help=\"Use HF transformers instead of vLLM\")\n    parser.add_argument(\"--max_steps\", type=int, default=30,\n                        help=\"Max steps per episode (default: 30)\")\n    parser.add_argument(\"--n_candidates\", type=int, default=3,\n                        help=\"Candidate actions for deterministic mode (default: 3)\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    if args.no_vllm:\n        args.use_vllm = False\n\n    random.seed(args.seed)\n\n    task_names_raw = [t.strip() for t in args.task_types.split(\",\") if t.strip()]\n    task_names = [resolve_task_type(t) for t in task_names_raw]\n\n    print(f\"Task types: {task_names}\")\n    print(f\"Episodes: {args.episodes} | Max steps: {args.max_steps}\")\n    print(f\"GPU: {args.gpu_id} | vLLM: {args.use_vllm} | Seed: {args.seed}\")\n    print(f\"Output: {args.output_dir}\")\n\n    agent = LLMAgent(\n        model_path=args.model_path,\n        use_vllm=args.use_vllm,\n        gpu_id=args.gpu_id,\n    )\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    all_results = {}\n\n    for task_name in task_names:\n        result = run_task_collection(\n            agent, task_name, args.episodes, args.max_steps,\n            args.output_dir, args.n_candidates,\n        )\n        all_results[task_name] = result\n\n    # Global summary\n    summary_path = os.path.join(args.output_dir, \"collection_summary.json\")\n    with open(summary_path, \"w\") as f:\n        json.dump(all_results, f, indent=2)\n    print(f\"\\nSummary saved to {summary_path}\")\n\n    total_triples = sum(r[\"total_sft_triples\"] for r in all_results.values())\n    print(f\"Total SFT triples across all tasks: {total_triples}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "cat > /root/autodl-tmp/simgate-modular-routing/src/collect_trajectories.py << 'PYEOF'\n\"\"\"Episode-level counterfactual trajectory collection for router SFT training.\n\nPlan C (D010): For each task type, run N independent episodes under always-internal\nand N under always-deterministic. Compare episode total scores to assign modality\nlabels. Death episodes (score <= -100) automatically lose.\n\nInput:\n  - ScienceWorld task types (via --task_types)\n  - Qwen2.5-7B-Instruct model (via --model_path or auto-detected)\n  - vLLM or HF transformers backend\n\nOutput:\n  - {output_dir}/{task}/raw_episodes.jsonl   — full episode data (both modalities)\n  - {output_dir}/{task}/sft_triples.jsonl    — (observation, action, modality_label) for SFT\n  - {output_dir}/collection_summary.json     — global statistics\n\nDependencies: scienceworld, vllm (or transformers), scienceworld_utils, llm_agent\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nimport time\nfrom typing import List, Dict, Any\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom scienceworld_utils import (\n    create_env, reset_env, get_valid_actions, get_score,\n    step_env, close_env, fork_and_lookahead, get_task_types,\n    get_max_variations,\n)\nfrom llm_agent import LLMAgent, find_model_path\n\nDEATH_THRESHOLD = -100\n\n\ndef resolve_task_type(name: str) -> str:\n    \"\"\"Resolve short task name to ScienceWorld's full task name.\"\"\"\n    try:\n        available = get_task_types()\n    except Exception:\n        return name\n    if name in available:\n        return name\n    matches = [t for t in available if name.lower() in t.lower()]\n    return matches[0] if matches else name\n\n\ndef is_lethal(fr: Dict[str, Any]) -> bool:\n    if fr[\"done\"] and fr[\"score\"] < 0:\n        return True\n    return fr[\"score\"] <= -100\n\n\ndef is_death_episode(final_score: float) -> bool:\n    \"\"\"Check if an episode ended in death (score <= -100).\"\"\"\n    return final_score <= DEATH_THRESHOLD\n\n\ndef run_episode_internal(\n    agent: LLMAgent,\n    task_name: str,\n    variation_idx: int,\n    max_steps: int,\n) -> Dict[str, Any]:\n    \"\"\"Run one always-internal episode. LLM ReAct picks every action.\"\"\"\n    env = create_env(task_name, variation_idx)\n    obs, _ = reset_env(env)\n    initial_score = get_score(env)\n\n    steps = []\n    action_history = []\n    history_dicts = []\n    t0 = time.time()\n\n    for step_idx in range(max_steps):\n        valid_actions = get_valid_actions(env)\n        if not valid_actions:\n            break\n\n        action, raw_output = agent.select_action_react(obs, valid_actions, history_dicts)\n\n        score_before = get_score(env)\n        obs_new, reward, done, info = step_env(env, action)\n        score_after = get_score(env)\n\n        steps.append({\n            \"step_idx\": step_idx,\n            \"observation_text\": obs[:500],\n            \"action_text\": action,\n            \"available_actions\": valid_actions,\n            \"score_before\": score_before,\n            \"score_after\": score_after,\n            \"score_delta\": score_after - score_before,\n            \"is_death\": score_after <= DEATH_THRESHOLD,\n            \"done\": done,\n            \"llm_output\": raw_output[:300],\n        })\n        action_history.append(action)\n        history_dicts.append({\"action\": action, \"observation\": obs_new[:200], \"score\": score_after})\n        obs = obs_new\n\n        if done:\n            break\n\n    final_score = get_score(env)\n    close_env(env)\n\n    return {\n        \"modality\": \"internal\",\n        \"task_name\": task_name,\n        \"variation_idx\": variation_idx,\n        \"final_score\": final_score,\n        \"initial_score\": initial_score,\n        \"is_death\": is_death_episode(final_score),\n        \"num_steps\": len(steps),\n        \"total_time_s\": round(time.time() - t0, 2),\n        \"steps\": steps,\n    }\n\n\ndef run_episode_deterministic(\n    agent: LLMAgent,\n    task_name: str,\n    variation_idx: int,\n    max_steps: int,\n    n_candidates: int = 3,\n) -> Dict[str, Any]:\n    \"\"\"Run one always-deterministic episode. LLM generates candidates, fork evaluates.\"\"\"\n    env = create_env(task_name, variation_idx)\n    obs, _ = reset_env(env)\n    initial_score = get_score(env)\n\n    steps = []\n    action_history = []\n    history_dicts = []\n    t0 = time.time()\n\n    for step_idx in range(max_steps):\n        valid_actions = get_valid_actions(env)\n        if not valid_actions:\n            break\n\n        candidates, raw_output = agent.generate_candidate_actions(\n            obs, valid_actions, history_dicts, n=n_candidates\n        )\n\n        best_action = None\n        best_delta = float(\"-inf\")\n        best_action_fallback = None\n        best_delta_fallback = float(\"-inf\")\n        fork_results = []\n        for cand in candidates:\n            fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)\n            lethal = is_lethal(fr)\n            fork_results.append({\n                \"action\": cand,\n                \"score_delta\": fr[\"score_delta\"],\n                \"score\": fr[\"score\"],\n                \"lethal\": lethal,\n            })\n            if fr[\"score_delta\"] > best_delta_fallback:\n                best_delta_fallback = fr[\"score_delta\"]\n                best_action_fallback = cand\n            if not lethal and fr[\"score_delta\"] > best_delta:\n                best_delta = fr[\"score_delta\"]\n                best_action = cand\n\n        if best_action is None:\n            best_action = best_action_fallback if best_action_fallback else valid_actions[0]\n\n        score_before = get_score(env)\n        obs_new, reward, done, info = step_env(env, best_action)\n        score_after = get_score(env)\n\n        steps.append({\n            \"step_idx\": step_idx,\n            \"observation_text\": obs[:500],\n            \"action_text\": best_action,\n            \"available_actions\": valid_actions,\n            \"score_before\": score_before,\n            \"score_after\": score_after,\n            \"score_delta\": score_after - score_before,\n            \"is_death\": score_after <= DEATH_THRESHOLD,\n            \"done\": done,\n            \"candidates\": fork_results,\n            \"llm_output\": raw_output[:300],\n        })\n        action_history.append(best_action)\n        history_dicts.append({\"action\": best_action, \"observation\": obs_new[:200], \"score\": score_after})\n        obs = obs_new\n\n        if done:\n            break\n\n    final_score = get_score(env)\n    close_env(env)\n\n    return {\n        \"modality\": \"deterministic\",\n        \"task_name\": task_name,\n        \"variation_idx\": variation_idx,\n        \"final_score\": final_score,\n        \"initial_score\": initial_score,\n        \"is_death\": is_death_episode(final_score),\n        \"num_steps\": len(steps),\n        \"total_time_s\": round(time.time() - t0, 2),\n        \"steps\": steps,\n    }\n\n\ndef label_episode_pair(internal_score: float, det_score: float) -> str:\n    \"\"\"Determine which modality wins the episode-level comparison.\n\n    Returns \"deterministic\", \"internal\", or \"tie\".\n    Death episodes (score <= -100) automatically lose.\n    \"\"\"\n    int_death = internal_score <= DEATH_THRESHOLD\n    det_death = det_score <= DEATH_THRESHOLD\n\n    if int_death and det_death:\n        return \"tie\"\n    if int_death:\n        return \"deterministic\"\n    if det_death:\n        return \"internal\"\n\n    if det_score > internal_score:\n        return \"deterministic\"\n    elif internal_score > det_score:\n        return \"internal\"\n    return \"tie\"\n\n\ndef extract_sft_triples(episode: Dict[str, Any], label: str) -> List[Dict[str, Any]]:\n    \"\"\"Extract (observation, action, modality_label) triples from the winning episode.\"\"\"\n    triples = []\n    for step in episode[\"steps\"]:\n        triples.append({\n            \"observation\": step[\"observation_text\"],\n            \"action\": step[\"action_text\"],\n            \"available_actions\": step[\"available_actions\"],\n            \"modality_label\": label,\n            \"task_name\": episode[\"task_name\"],\n            \"variation_idx\": episode[\"variation_idx\"],\n            \"step_idx\": step[\"step_idx\"],\n            \"score_after\": step[\"score_after\"],\n        })\n    return triples\n\n\ndef run_task_collection(\n    agent: LLMAgent,\n    task_name: str,\n    n_episodes: int,\n    max_steps: int,\n    output_dir: str,\n    n_candidates: int = 3,\n) -> Dict[str, Any]:\n    \"\"\"Collect episode-level trajectory data for one task type.\n\n    For each of n_episodes variations:\n      1. Run always-internal episode\n      2. Run always-deterministic episode (same variation)\n      3. Compare final scores → assign modality label\n      4. Extract SFT triples from the winning episode\n\n    Writes raw_episodes.jsonl and sft_triples.jsonl incrementally.\n    \"\"\"\n    task_dir = os.path.join(output_dir, task_name.replace(\" \", \"_\"))\n    os.makedirs(task_dir, exist_ok=True)\n\n    raw_file = os.path.join(task_dir, \"raw_episodes.jsonl\")\n    sft_file = os.path.join(task_dir, \"sft_triples.jsonl\")\n\n    max_var = get_max_variations(task_name)\n\n    print(f\"\\n{'='*60}\")\n    print(f\"TRAJECTORY COLLECTION: {task_name}\")\n    print(f\"Episodes: {n_episodes} | Max steps: {max_steps} | Variations: {max_var}\")\n    print(f\"{'='*60}\")\n\n    label_counts = {\"deterministic\": 0, \"internal\": 0, \"tie\": 0}\n    death_counts = {\"internal\": 0, \"det\": 0, \"both\": 0}\n    total_sft_triples = 0\n    score_gaps = []\n\n    for ep_idx in range(n_episodes):\n        variation_idx = ep_idx % max_var\n        print(f\"\\n--- Episode {ep_idx}/{n_episodes} (variation={variation_idx}) ---\")\n\n        # Run both modalities on the same variation\n        t_ep = time.time()\n        ep_internal = run_episode_internal(agent, task_name, variation_idx, max_steps)\n        ep_det = run_episode_deterministic(agent, task_name, variation_idx, max_steps, n_candidates)\n        ep_time = time.time() - t_ep\n\n        int_score = ep_internal[\"final_score\"]\n        det_score = ep_det[\"final_score\"]\n        label = label_episode_pair(int_score, det_score)\n\n        # Track deaths\n        if ep_internal[\"is_death\"] and ep_det[\"is_death\"]:\n            death_counts[\"both\"] += 1\n        elif ep_internal[\"is_death\"]:\n            death_counts[\"internal\"] += 1\n        elif ep_det[\"is_death\"]:\n            death_counts[\"det\"] += 1\n\n        label_counts[label] += 1\n        score_gap = abs(det_score - int_score)\n        if label != \"tie\":\n            score_gaps.append(score_gap)\n\n        print(f\"  internal={int_score:.1f} | det={det_score:.1f} | label={label} | gap={score_gap:.1f} | {ep_time:.1f}s\")\n\n        # Save raw episode data (both modalities)\n        for ep in [ep_internal, ep_det]:\n            ep_record = {\n                \"episode_idx\": ep_idx,\n                \"label\": label,\n                \"score_gap\": score_gap,\n                **ep,\n            }\n            with open(raw_file, \"a\") as f:\n                f.write(json.dumps(ep_record) + \"\\n\")\n\n        # Extract and save SFT triples from the winning modality only\n        if label == \"tie\":\n            continue\n\n        winning_ep = ep_det if label == \"deterministic\" else ep_internal\n        triples = extract_sft_triples(winning_ep, label)\n        with open(sft_file, \"a\") as f:\n            for t in triples:\n                f.write(json.dumps(t) + \"\\n\")\n        total_sft_triples += len(triples)\n\n    avg_gap = sum(score_gaps) / len(score_gaps) if score_gaps else 0.0\n\n    print(f\"\\n=== {task_name} SUMMARY ===\")\n    print(f\"Labels: det={label_counts['deterministic']} int={label_counts['internal']} tie={label_counts['tie']}\")\n    print(f\"Deaths: int={death_counts['internal']} det={death_counts['det']} both={death_counts['both']}\")\n    print(f\"Avg score gap (non-tie): {avg_gap:.2f}\")\n    print(f\"SFT triples: {total_sft_triples}\")\n\n    return {\n        \"task_name\": task_name,\n        \"n_episodes\": n_episodes,\n        \"label_counts\": label_counts,\n        \"death_counts\": death_counts,\n        \"total_sft_triples\": total_sft_triples,\n        \"avg_score_gap\": avg_gap,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Collect episode-level counterfactual trajectories for router SFT (Plan C / D010)\"\n    )\n    parser.add_argument(\"--task_types\", type=str, required=True,\n                        help=\"Comma-separated task type names (e.g. 'boil,melt')\")\n    parser.add_argument(\"--episodes\", type=int, default=20,\n                        help=\"Number of episodes per task type (default: 20)\")\n    parser.add_argument(\"--gpu_id\", type=int, default=0)\n    parser.add_argument(\"--output_dir\", type=str, default=\"results/trajectories/\",\n                        help=\"Output directory for trajectory data\")\n    parser.add_argument(\"--model_path\", type=str, default=None,\n                        help=\"Path to Qwen2.5-7B-Instruct (auto-detected if omitted)\")\n    parser.add_argument(\"--use_vllm\", action=\"store_true\", default=True,\n                        help=\"Use vLLM backend (default: True)\")\n    parser.add_argument(\"--no_vllm\", action=\"store_true\", default=False,\n                        help=\"Use HF transformers instead of vLLM\")\n    parser.add_argument(\"--max_steps\", type=int, default=30,\n                        help=\"Max steps per episode (default: 30)\")\n    parser.add_argument(\"--n_candidates\", type=int, default=3,\n                        help=\"Candidate actions for deterministic mode (default: 3)\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    args = parser.parse_args()\n\n    if args.no_vllm:\n        args.use_vllm = False\n\n    random.seed(args.seed)\n\n    task_names_raw = [t.strip() for t in args.task_types.split(\",\") if t.strip()]\n    task_names = [resolve_task_type(t) for t in task_names_raw]\n\n    print(f\"Task types: {task_names}\")\n    print(f\"Episodes: {args.episodes} | Max steps: {args.max_steps}\")\n    print(f\"GPU: {args.gpu_id} | vLLM: {args.use_vllm} | Seed: {args.seed}\")\n    print(f\"Output: {args.output_dir}\")\n\n    agent = LLMAgent(\n        model_path=args.model_path,\n        use_vllm=args.use_vllm,\n        gpu_id=args.gpu_id,\n    )\n\n    os.makedirs(args.output_dir, exist_ok=True)\n    all_results = {}\n\n    for task_name in task_names:\n        result = run_task_collection(\n            agent, task_name, args.episodes, args.max_steps,\n            args.output_dir, args.n_candidates,\n        )\n        all_results[task_name] = result\n\n    # Global summary\n    summary_path = os.path.join(args.output_dir, \"collection_summary.json\")\n    with open(summary_path, \"w\") as f:\n        json.dump(all_results, f, indent=2)\n    print(f\"\\nSummary saved to {summary_path}\")\n\n    total_triples = sum(r[\"total_sft_triples\"] for r in all_results.values())\n    print(f\"Total SFT triples across all tasks: {total_triples}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T18:38:16.179915+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T18:38:16.180089+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westb-13313",
  "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/simgate-modular-routing && python src/collect_trajectories.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westb-13313",
    "command": "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/simgate-modular-routing && python src/collect_trajectories.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T18:38:16.180235+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: collect_trajectories.py [-h] --task_types TASK_TYPES\\n                               [--episodes EPISODES] [--gpu_id GPU_ID]\\n                               [--output_dir OUTPUT_DIR]\\n                               [--model_path MODEL_PATH] [--use_vllm]\\n                               [--no_vllm] [--max_steps MAX_STEPS]\\n                               [--n_candidates N_CANDIDATES] [--seed SEED]\\n\\nCollect episode-level counterfactual trajectories for router SFT (Plan C /\\nD010)\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --task_types TASK_TYPES\\n                        Comma-separated task type names (e.g. 'boil,melt')\\n  --episodes EPISODES   Number of episodes per task type (default: 20)\\n  --gpu_id GPU_ID\\n  --output_dir OUTPUT_DIR\\n                        Output directory for trajectory data\\n  --model_path MODEL_PATH\\n                        Path to Qwen2.5-7B-Instruct (auto-detected if omitted)\\n  --use_vllm            Use vLLM backend (default: True)\\n  --no_vllm             Use HF transformers instead of vLLM\\n  --max_steps MAX_STEPS\\n                        Max steps per episode (default: 30)\\n  --n_candidates N_CANDIDATES\\n                        Candidate actions for deterministic mode (default: 3)\\n  --seed SEED\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan-001b-prep_20260513T183608",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T18:38:16.180410+00:00_

Dry-run 通过，参数解析正常。

产出：
- **远程文件**：`/root/autodl-tmp/simgate-modular-routing/src/collect_trajectories.py`
- **`--help` 验证通过**，所有 CLI 参数可正常解析

与现有 `episode_level_collection.py` 的主要区别：
1. 每步额外记录 `available_actions`、`is_death`、`observation_text`（步骤执行前的 obs）
2. 输出分两层：`raw_episodes.jsonl`（两种 modality 的完整 episode 数据）+ `sft_triples.jsonl`（仅 winning modality 的 (obs, action, label) 三元组）
3. Death episode 自动判负逻辑保持一致，tie 时不产出 SFT 数据
4. 全局统计写入 `collection_summary.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_plan-001b-prep_20260513T183608"
}
```

</details>

---
