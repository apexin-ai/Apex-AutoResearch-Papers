# research e4 dataset survey

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 255
- **Recorded user turns:** 0
- **Tool calls:** 127
- **Original source:** `logs/chats/worker_research_e4_dataset_survey_20260514T092619.jsonl`
- **Structured JSON:** [`60e617e051413c07e940.json`](../../sessions/60/60e617e051413c07e940.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

255 recorded events

### Tool call

_source line 1 · 2026-05-14T09:34:41.918913+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Survey NER datasets availability",
  "subagent_type": "Explore",
  "prompt": "I need to understand the current project's data format and evaluation code for a NER (Named Entity Recognition) project. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/\n\nSearch thoroughly for:\n1. Any sharegpt format training data files (JSON) - look for SciERC training data to understand the exact format\n2. The evaluation code - especially `entity_strict_match` function\n3. Any existing data conversion/preprocessing scripts\n4. The UIE format schema used\n\nLook in the project artifacts directory too: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/\n\nReport the exact data format (show examples), entity types used, and evaluation logic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "tool_args": {
    "description": "Survey NER datasets availability",
    "subagent_type": "Explore",
    "prompt": "I need to understand the current project's data format and evaluation code for a NER (Named Entity Recognition) project. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/\n\nSearch thoroughly for:\n1. Any sharegpt format training data files (JSON) - look for SciERC training data to understand the exact format\n2. The evaluation code - especially `entity_strict_match` function\n3. Any existing data conversion/preprocessing scripts\n4. The UIE format schema used\n\nLook in the project artifacts directory too: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/\n\nReport the exact data format (show examples), entity types used, and evaluation logic."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T09:34:41.919334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.json\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T09:34:41.919519+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_sampling_and_main_20260514T042643_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_consistency_module_20260514T042604_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_add_re_subtask_20260514T050825_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_eval_gate0_ft002v2_20260514T084152_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_eval_gate0_ft001_20260514T063206_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_infra_model_download_20260514T054921_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_infra_install_tmux_and_retrain_ft002_20260514T080436_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_fix_sample_f1_dist_20260514T043208_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_eval_gate0_ft002v2_ckpt400_20260514T084649_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_infra_env_setup_20260514T044757_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_data_eval_modules_20260514T042533_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_fix_chat_template_20260514T043155_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_span_realignment_and_gate0_20260514T070233_result.json
/home/ubuntu/.agent-ml-researc
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T09:34:41.919679+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T09:34:41.919808+00:00_

artifacts/_project/data/data_utils.py
artifacts/data_utils.py
artifacts/_project/data/evaluation.py
artifacts/_project/intermediate/consistency.py
artifacts/_project/data/consistency.py
artifacts/_project/data/sampling.py
artifacts/_project/data/run_mvp_pilot.py
artifacts/evaluation.py
artifacts/consistency.py
artifacts/_project/intermediate/sampling.py
artifacts/ft_001/report/sampling.py
artifacts/mvp_pilot.py
artifacts/mvp_pilot_001/report/mvp_pilot.py
artifacts/sampling.py
artifacts/run_mvp_pilot.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T09:34:41.919952+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.jsonl\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.jsonl\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T09:34:41.920082+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/ralph_loop_timeline.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_train_ft_002_v2_20260514T080903.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_check_ft_002_and_cleanup_20260514T080112.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_eval_mvp_pilot_001_20260514T074023.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260514T084303_347636.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer_20260514T084336_282523.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3_reviewer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_infra_env_setup_v2_20260514T050925.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_523053f5a039428dc15666668fa856b3.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_train_ft_002_20260514T074046.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_data_scierc_prep_20260514T052927.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_infra_env_setup_20260514T044757.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worke
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T09:34:41.920299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type d -name \"data*\" -o -name \"*train*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type d -name \"data*\" -o -name \"*train*\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T09:34:41.920436+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_infra_install_tmux_and_retrain_ft002_20260514T080436.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_infra_install_tmux_and_retrain_ft002_20260514T080436_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_train_ft_002_20260514T074046_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_train_ft_002_20260514T074046.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_train_ft_002_v2_20260514T080903_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_train_ft_001_20260514T060518_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_train_ft_001_20260514T060518.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_train_ft_002_v2_20260514T080903.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_train_ft_002_v2_20260514T080903.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_train_ft_002_v2_20260514T080903.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_train_ft_002_20260514T074046.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_train_ft_002_20260514T074046.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T09:34:41.920583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T09:34:41.920708+00:00_

total 136
drwxr-xr-x 8 ubuntu ubuntu  4096 May 14 09:13 .
drwxr-xr-x 8 ubuntu ubuntu  4096 May 14 09:25 ..
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 05:09 __pycache__
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 04:30 _project
-rw-r--r-- 1 ubuntu ubuntu 13271 May 14 05:50 consistency.py
-rw-r--r-- 1 ubuntu ubuntu  9089 May 14 04:26 data_utils.py
-rw-r--r-- 1 ubuntu ubuntu 13031 May 14 05:09 evaluation.py
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 06:57 ft_001
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 07:44 ft_002
-rw-r--r-- 1 ubuntu ubuntu  5831 May 14 09:13 manifest.yaml
-rw-r--r-- 1 ubuntu ubuntu 11096 May 14 07:46 mvp_pilot.py
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 07:53 mvp_pilot_001
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 09:13 mvp_pilot_004
-rw-r--r-- 1 ubuntu ubuntu 14377 May 14 08:50 run_mvp_pilot.py
-rw-r--r-- 1 ubuntu ubuntu 20746 May 14 07:46 sampling.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T09:34:41.920839+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T09:34:41.920990+00:00_

total 68
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 04:30 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 04:30 ..
-rw-r--r-- 1 ubuntu ubuntu 11501 May 14 04:27 consistency.py
-rw-r--r-- 1 ubuntu ubuntu  9089 May 14 04:26 data_utils.py
-rw-r--r-- 1 ubuntu ubuntu  9754 May 14 04:27 evaluation.py
-rw-r--r-- 1 ubuntu ubuntu  7671 May 14 04:29 run_mvp_pilot.py
-rw-r--r-- 1 ubuntu ubuntu 14918 May 14 04:27 sampling.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T09:34:41.921120+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T09:34:41.921326+00:00_

1	"""Evaluation module for structured self-consistency IE experiments.
2	
3	Provides strict-match NER/EAE evaluation, per-instance F1 computation,
4	correlation analysis, and summary report generation.
5	"""
6	
7	from __future__ import annotations
8	
9	import statistics
10	from typing import Any
11	
12	from scipy.stats import spearmanr
13	
14	
15	# ---------------------------------------------------------------------------
16	# NER evaluation (strict match)
17	# ---------------------------------------------------------------------------
18	
19	def entity_strict_match(
20	    pred_entities: list[dict],
21	    gold_entities: list[dict],
22	) -> tuple[int, int, int]:
23	    """Compute strict entity match counts.
24	
25	    Strict match requires exact span (start, end) AND exact type.
26	
27	    Args:
28	        pred_entities: Predicted entity dicts with keys text, type, start, end.
29	        gold_entities: Gold entity dicts with the same schema.
30	
31	    Returns:
32	        (tp, fp, fn) counts.
33	    """
34	    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
35	    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
36	    tp = len(pred_set & gold_set)
37	    fp = len(pred_set - gold_set)
38	    fn = len(gold_set - pred_set)
39	    return tp, fp, fn
40	
41	
42	def compute_ner_f1(
43	    predictions: list[dict],
44	    golds: list[dict],
45	) -> dict[str, float]:
46	    """Compute micro-averaged NER precision, recall, and F1.
47	
48	    Args:
49	        predictions: List of Extraction dicts (one per instance).
50	        golds: List of Extraction dicts (one per instance), aligned with predictions.
51	
52	    Returns:
53	        Dict with keys "precision", "recall", "f1".
54	    """
55	    total_tp = total_fp = total_fn = 0
56	    for pred, gold in zip(predictions, golds):
57	        tp, fp, fn = entity_strict_match(
58	            pred.get("entities", []),
59	            gold.get("entities", []),
60	        )
61	        total_
…[truncated 12463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T09:34:41.921489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T09:34:41.921652+00:00_

1	"""Data processing utilities for structured self-consistency IE experiments.
2	
3	Handles loading, converting, and splitting datasets into the unified UIE JSON format.
4	Supported datasets: SciERC (fully implemented), ACE05 (interface only).
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	import random
12	from typing import Any, TypedDict
13	
14	
15	# ---------------------------------------------------------------------------
16	# Shared type definitions (UIE JSON format)
17	# ---------------------------------------------------------------------------
18	
19	class Entity(TypedDict):
20	    text: str
21	    type: str
22	    start: int
23	    end: int
24	
25	
26	class Relation(TypedDict):
27	    head: str
28	    tail: str
29	    type: str
30	    head_start: int
31	    head_end: int
32	    tail_start: int
33	    tail_end: int
34	
35	
36	class EventArgument(TypedDict):
37	    text: str
38	    role: str
39	    start: int
40	    end: int
41	
42	
43	class Trigger(TypedDict):
44	    text: str
45	    type: str
46	    start: int
47	    end: int
48	
49	
50	class Event(TypedDict):
51	    trigger: Trigger
52	    arguments: list[EventArgument]
53	
54	
55	class Extraction(TypedDict, total=False):
56	    entities: list[Entity]
57	    relations: list[Relation]
58	    events: list[Event]
59	
60	
61	class Instance(TypedDict, total=False):
62	    id: str
63	    text: str
64	    entities: list[Entity]
65	    relations: list[Relation]
66	    events: list[Event]
67	
68	
69	# ---------------------------------------------------------------------------
70	# SciERC
71	# ---------------------------------------------------------------------------
72	
73	def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
74	    """Compute (char_start, char_end) for each token when joined by single spaces."""
75	    offsets = []
76	    pos = 0
77	    for tok in tokens:
78	        offsets.append((pos, pos + len(tok)))
79	        pos += len(tok) + 1  # +1 for the space

…[truncated 8145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T09:34:41.921809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T09:34:41.922025+00:00_

1	"""Multi-sample inference module for structured IE with vLLM + XGrammar constrained decoding.
2	
3	Provides VLLMSampler for batch sampling, prompt construction for UIE tasks,
4	and a full pipeline that produces SampledInstance dicts.
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	from typing import Any
12	
13	
14	# ---------------------------------------------------------------------------
15	# UIE JSON schema for XGrammar constrained decoding
16	# ---------------------------------------------------------------------------
17	
18	UIE_JSON_SCHEMA: dict[str, Any] = {
19	    "type": "object",
20	    "properties": {
21	        "entities": {
22	            "type": "array",
23	            "items": {
24	                "type": "object",
25	                "properties": {
26	                    "text": {"type": "string"},
27	                    "type": {"type": "string"},
28	                    "start": {"type": "integer"},
29	                    "end": {"type": "integer"},
30	                },
31	                "required": ["text", "type", "start", "end"],
32	            },
33	        },
34	        "relations": {
35	            "type": "array",
36	            "items": {
37	                "type": "object",
38	                "properties": {
39	                    "head": {"type": "string"},
40	                    "tail": {"type": "string"},
41	                    "type": {"type": "string"},
42	                    "head_start": {"type": "integer"},
43	                    "head_end": {"type": "integer"},
44	                    "tail_start": {"type": "integer"},
45	                    "tail_end": {"type": "integer"},
46	                },
47	                "required": ["head", "tail", "type", "head_start", "head_end",
48	                             "tail_start", "tail_end"],
49	            },
50	        },
51	        "events": {
52	            "type": "array",
53	            "items": {
54	                "type": "object",
55	             
…[truncated 21062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T09:34:41.922212+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.json\" -path \"*artifact*\" -o -name \"*scierc*\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.json\" -path \"*artifact*\" -o -name \"*scierc*\" | head -10"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T09:34:41.922342+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_data_scierc_prep_20260514T052927.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_data_scierc_prep_20260514T052927_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_data_scierc_prep_20260514T052927.lock
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_data_scierc_prep_20260514T052927.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T09:34:41.922481+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts -type f \\( -name \"*.jsonl\" -o -name \"*.json\" \\) | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts -type f \\( -name \"*.jsonl\" -o -name \"*.json\" \\) | head -20"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T09:34:41.922601+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T09:34:41.922726+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ft_001/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ft_001/"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T09:34:41.922843+00:00_

total 12
drwxr-xr-x 3 ubuntu ubuntu 4096 May 14 06:57 .
drwxr-xr-x 8 ubuntu ubuntu 4096 May 14 09:13 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 07:30 report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T09:34:41.922967+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/mvp_pilot_001/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/mvp_pilot_001/"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T09:34:41.923078+00:00_

total 12
drwxr-xr-x 3 ubuntu ubuntu 4096 May 14 07:53 .
drwxr-xr-x 8 ubuntu ubuntu 4096 May 14 09:13 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 07:53 report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T09:34:41.923220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T09:34:41.923417+00:00_

1	"""Consistency metrics for structured information extraction with self-consistency.
2	
3	Implements three complementary consistency measures over N sampled extractions:
4	1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence
5	2. Structural soft Jaccard — span-level soft overlap with Hungarian matching
6	3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance
7	
8	Key dependencies: numpy, scipy (linear_sum_assignment).
9	"""
10	
11	from __future__ import annotations
12	
13	from itertools import combinations
14	from typing import TYPE_CHECKING
15	
16	import numpy as np
17	from scipy.optimize import linear_sum_assignment
18	
19	if TYPE_CHECKING:
20	    pass
21	
22	# ---------------------------------------------------------------------------
23	# Type aliases (mirrors shared data format)
24	# ---------------------------------------------------------------------------
25	Entity = dict       # {"text", "type", "start", "end"}
26	Relation = dict     # {"head", "tail", "type", ...}
27	Event = dict        # {"trigger": {...}, "arguments": [...]}
28	Extraction = dict   # {"entities", "relations", "events"}
29	
30	
31	# ===================================================================
32	# 1. Fleiss' Kappa — surface‐level entity agreement
33	# ===================================================================
34	
35	def _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:
36	    """Extract surface-level keys from a sample for Fleiss' Kappa computation."""
37	    if subtask == "ner":
38	        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
39	    elif subtask == "re":
40	        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
41	    elif subtask == "eae":
42	        keys: set[tuple] = set()
43	        for ev in sample.get("events", []):
44	            t = ev.get("trigger", {})
45	            for arg in ev.get("arguments", []):
46	                k
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T09:34:41.923608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mvp_pilot.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mvp_pilot.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T09:34:41.923772+00:00_

1	"""MVP pilot experiment script for structured self-consistency IE.
2	
3	Integrates data loading, vLLM sampling, consistency scoring, and evaluation
4	into a single CLI-driven pipeline. Outputs a verdict (PASS/MARGINAL/FAIL)
5	based on the correlation between structural consistency and per-instance F1.
6	"""
7	
8	from __future__ import annotations
9	
10	import argparse
11	import json
12	import os
13	import random
14	import sys
15	
16	import numpy as np
17	
18	from data_utils import load_scierc, load_ace05
19	from sampling import (
20	    VLLMSampler,
21	    run_sampling_pipeline,
22	    save_sampled_results,
23	    load_sampled_results,
24	    realign_spans,
25	    SCIERC_SCHEMA_HINT,
26	)
27	from consistency import compute_all_consistency_scores
28	from evaluation import (
29	    per_instance_f1,
30	    compute_ner_f1,
31	    compute_re_f1,
32	    compute_eae_f1,
33	    spearman_correlation,
34	    compute_sample_f1_distribution,
35	)
36	
37	
38	def parse_args() -> argparse.Namespace:
39	    """Parse command-line arguments."""
40	    p = argparse.ArgumentParser(description="MVP pilot for structured self-consistency IE")
41	    p.add_argument("--model_path", type=str, required=True, help="Path to the fine-tuned model")
42	    p.add_argument("--data_dir", type=str, required=True, help="Dataset directory (SciERC or ACE05)")
43	    p.add_argument("--dataset", type=str, default="scierc", choices=["scierc", "ace05"],
44	                   help="Dataset name (default: scierc)")
45	    p.add_argument("--subtask", type=str, default="ner", choices=["ner", "re", "eae", "joint"],
46	                   help="Subtask (default: ner)")
47	    p.add_argument("--schema_hint", type=str, default="",
48	                   help="Schema hint string (entity/relation types). Auto-set for scierc if empty")
49	    p.add_argument("--use_train_format", type=lambda x: x.lower() != "false", default=True,
50	                   help="Use train-aligned prompt template (default: True)")
51	    p.ad
…[truncated 3331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T09:34:41.923929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_data_scierc_prep_20260514T052927_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_data_scierc_prep_20260514T052927_result.json"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T09:34:41.924055+00:00_

{
  "raw": "完成。汇报如下：\n\n| Split | Sentences | Entities | Entity Types | Relations | Relation Types |\n|-------|-----------|----------|-------------|-----------|---------------|\n| train | 1861 | 5598 | 6 | 3219 | 7 |\n| dev | 275 | 811 | 6 | 455 | 7 |\n| test | 551 | 1685 | 6 | 974 | 7 |\n\n**Entity types (6)**: Generic, Material, Method, Metric, OtherScientificTerm, Task\n\n**Relation types (7)**: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR\n\nUIE JSONL 文件已生成到：\n- `/root/autodl-tmp/struct_self_consist_ie/data/train.jsonl`\n- `/root/autodl-tmp/struct_self_consist_ie/data/dev.jsonl`\n- `/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl`"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T09:34:41.924249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T09:34:41.924424+00:00_

1	- id: art_20260514_8c5ac9
2	  name: consistency.py
3	  type: intermediate
4	  description: 'Core consistency metrics module: Fleiss kappa (surface), structural
5	    soft Jaccard (span-level Hungarian matching), oracle best-of-N F1, and aggregate
6	    helper.'
7	  path: projects/struct_self_consist_ie/artifacts/_project/intermediate/consistency.py
8	  url: null
9	  project: struct_self_consist_ie
10	  exp_id: null
11	  skill: ''
12	  created_at: '2026-05-14T04:27:26.880296+00:00'
13	  tags:
14	  - consistency
15	  - metrics
16	  - core
17	- id: art_20260514_822db6
18	  name: data_utils.py
19	  type: data
20	  description: SciERC/ACE05 数据处理模块：加载、转 UIE JSON、JSONL I/O、数据集划分
21	  path: projects/struct_self_consist_ie/artifacts/_project/data/data_utils.py
22	  url: null
23	  project: struct_self_consist_ie
24	  exp_id: null
25	  skill: ''
26	  created_at: '2026-05-14T04:30:08.325433+00:00'
27	  tags:
28	  - code
29	  - mvp
30	  - data-processing
31	- id: art_20260514_fd59f2
32	  name: evaluation.py
33	  type: data
34	  description: 评估模块：NER/EAE strict F1、per-instance F1、Spearman correlation、汇总报告
35	  path: projects/struct_self_consist_ie/artifacts/_project/data/evaluation.py
36	  url: null
37	  project: struct_self_consist_ie
38	  exp_id: null
39	  skill: ''
40	  created_at: '2026-05-14T04:30:09.120642+00:00'
41	  tags:
42	  - code
43	  - mvp
44	  - evaluation
45	- id: art_20260514_e88003
46	  name: consistency.py
47	  type: data
48	  description: 核心一致性度量：Fleiss Kappa (surface)、soft Jaccard (structural, Hungarian
49	    matching)、oracle best-of-N
50	  path: projects/struct_self_consist_ie/artifacts/_project/data/consistency.py
51	  url: null
52	  project: struct_self_consist_ie
53	  exp_id: null
54	  skill: ''
55	  created_at: '2026-05-14T04:30:12.419423+00:00'
56	  tags:
57	  - code
58	  - mvp
59	  - core-metric
60	- id: art_20260514_52a8cf
61	  name: sampling.py
62	  type: data
63	  description: vLLM 批量采样模块：VLLMSampler + XGrammar constrained decoding + prompt 构建
64	
…[truncated 4248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T09:34:41.924583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"entities\\|relations\\|events\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/*.py | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"entities\\|relations\\|events\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/*.py | head -50"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T09:34:41.924724+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:Extraction = dict   # {"entities", "relations", "events"}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:        for ev in sample.get("events", []):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:def _ner_soft_jaccard_pair(entities_a: list[Entity], entities_b: list[Entity]) -> float:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:    Groups entities by type, finds optimal alignment within each group using
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:        entities_a: Entities from sample i.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:        entities_b: Entities from sample j.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:    if not entities_a and not entities_b:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:    if not entities_a or not entities_b:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:    for e in entities_a:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py:    for e in entities_b:
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifac
…[truncated 5626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T09:34:41.924899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
  "offset": "73",
  "limit": "82"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
    "offset": "73",
    "limit": "82"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T09:34:41.925056+00:00_

73	def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
74	    """Compute (char_start, char_end) for each token when joined by single spaces."""
75	    offsets = []
76	    pos = 0
77	    for tok in tokens:
78	        offsets.append((pos, pos + len(tok)))
79	        pos += len(tok) + 1  # +1 for the space
80	    return offsets
81	
82	
83	def _parse_scierc_sentence(
84	    doc_key: str,
85	    sent_idx: int,
86	    tokens: list[str],
87	    ner_spans: list[list],
88	    rel_spans: list[list],
89	    global_token_offset: int,
90	) -> Instance:
91	    """Convert one SciERC sentence into a UIE Instance.
92	
93	    Args:
94	        doc_key: Document identifier.
95	        sent_idx: Sentence index within the document.
96	        tokens: List of tokens for this sentence.
97	        ner_spans: NER annotations [[start, end, type], ...] with global token indices (inclusive).
98	        rel_spans: Relation annotations [[s1, e1, s2, e2, type], ...] with global token indices.
99	        global_token_offset: Token index of the first token of this sentence in the document.
100	
101	    Returns:
102	        A UIE Instance dict.
103	    """
104	    text = " ".join(tokens)
105	    offsets = _token_offsets(tokens)
106	
107	    def _local(global_idx: int) -> int:
108	        return global_idx - global_token_offset
109	
110	    # --- entities ---
111	    entities: list[Entity] = []
112	    span_to_text: dict[tuple[int, int], str] = {}
113	    for span in ner_spans:
114	        tok_start, tok_end, etype = span[0], span[1], span[2]
115	        local_s, local_e = _local(tok_start), _local(tok_end)
116	        if local_s < 0 or local_e >= len(tokens):
117	            continue
118	        char_start = offsets[local_s][0]
119	        char_end = offsets[local_e][1]
120	        entity_text = text[char_start:char_end]
121	        entities.append(Entity(text=entity_text, type=etype, start=char_start, end=char_end))
122	        span_to_text[(tok_start, tok_end)] = entity_text
123	
124	  
…[truncated 1217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T09:34:41.925237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "offset": "320",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "offset": "320",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T09:34:41.925381+00:00_

320	
321	def _validate_entities(raw: Any) -> list[dict]:
322	    if not isinstance(raw, list):
323	        return []
324	    validated = []
325	    for e in raw:
326	        if not isinstance(e, dict):
327	            continue
328	        try:
329	            validated.append({
330	                "text": str(e["text"]),
331	                "type": str(e["type"]),
332	                "start": int(e["start"]),
333	                "end": int(e["end"]),
334	            })
335	        except (KeyError, ValueError, TypeError):
336	            continue
337	    return validated
338	
339	
340	def _validate_relations(raw: Any) -> list[dict]:
341	    if not isinstance(raw, list):
342	        return []
343	    validated = []
344	    for r in raw:
345	        if not isinstance(r, dict):
346	            continue
347	        try:
348	            validated.append({
349	                "head": str(r["head"]),
350	                "tail": str(r["tail"]),
351	                "type": str(r["type"]),
352	                "head_start": int(r["head_start"]),
353	                "head_end": int(r["head_end"]),
354	                "tail_start": int(r["tail_start"]),
355	                "tail_end": int(r["tail_end"]),
356	            })
357	        except (KeyError, ValueError, TypeError):
358	            continue
359	    return validated
360	
361	
362	def _validate_events(raw: Any) -> list[dict]:
363	    if not isinstance(raw, list):
364	        return []
365	    validated = []
366	    for ev in raw:
367	        if not isinstance(ev, dict):
368	            continue
369	        trigger_raw = ev.get("trigger")
370	        if not isinstance(trigger_raw, dict):
371	            continue
372	        try:
373	            trigger = {
374	                "text": str(trigger_raw["text"]),
375	                "type": str(trigger_raw["type"]),
376	                "start": int(trigger_raw["start"]),
377	                "end": int(trigger_raw["end"]),
378	            }
379	        except (KeyError, ValueE
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T09:34:41.925533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "offset": "18",
  "limit": "70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "offset": "18",
    "limit": "70"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T09:34:41.925674+00:00_

18	UIE_JSON_SCHEMA: dict[str, Any] = {
19	    "type": "object",
20	    "properties": {
21	        "entities": {
22	            "type": "array",
23	            "items": {
24	                "type": "object",
25	                "properties": {
26	                    "text": {"type": "string"},
27	                    "type": {"type": "string"},
28	                    "start": {"type": "integer"},
29	                    "end": {"type": "integer"},
30	                },
31	                "required": ["text", "type", "start", "end"],
32	            },
33	        },
34	        "relations": {
35	            "type": "array",
36	            "items": {
37	                "type": "object",
38	                "properties": {
39	                    "head": {"type": "string"},
40	                    "tail": {"type": "string"},
41	                    "type": {"type": "string"},
42	                    "head_start": {"type": "integer"},
43	                    "head_end": {"type": "integer"},
44	                    "tail_start": {"type": "integer"},
45	                    "tail_end": {"type": "integer"},
46	                },
47	                "required": ["head", "tail", "type", "head_start", "head_end",
48	                             "tail_start", "tail_end"],
49	            },
50	        },
51	        "events": {
52	            "type": "array",
53	            "items": {
54	                "type": "object",
55	                "properties": {
56	                    "trigger": {
57	                        "type": "object",
58	                        "properties": {
59	                            "text": {"type": "string"},
60	                            "type": {"type": "string"},
61	                            "start": {"type": "integer"},
62	                            "end": {"type": "integer"},
63	                        },
64	                        "required": ["text", "type", "start", "end"],
65	                    },
66	                    "arguments": {
67	                
…[truncated 853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T09:34:41.925833+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.md\" -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.md\" -type f | head -20"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T09:34:41.925959+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/director_786277ea/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/mvp_pilot_004/report/framing_proposal_post_pilot004.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ft_002/intermediate/ft_002_config_notes.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T09:34:41.926093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T09:34:41.926253+00:00_

1	# Memory — struct_self_consist_ie
2	
3	## 经验教训
4	
5	### Offset hallucination
6	Fine-tuned generative IE 模型输出正确 entity text 但 hallucinate character offsets（准确率仅 16.7%）。必须用 span realignment 后处理修复。这是 generative IE 的已知问题，不影响 paper claim。
7	
8	### Qwen3 think block vs XGrammar
9	Qwen3 默认输出 `&lt;think>...&lt;/think>` 再接 JSON，但 XGrammar 强制 `{` 为第一个 token。必须在 `apply_chat_template` 中设 `enable_thinking=False`。
10	
11	### Train/inference prompt alignment
12	训练用 unified template "Extract all structured information..."，推理必须用完全一致的 template + schema hints。不对齐会导致模型不识别指令。
13	
14	### Parse failures from max_tokens truncation (2026-05-14)
15	max_tokens=512 导致 3.7% stochastic + 5.3% greedy parse failures。max_tokens=1024 完全消除了 parse failures (0/4408)。
16	
17	### submit_training_job 需要 tmux (2026-05-14)
18	AutoDL 5090 服务器默认无 tmux。已安装 tmux 3.2a。
19	
20	### ft_002 nohup 崩溃教训 (2026-05-14)
21	Worker 用 nohup 启动训练后退出，训练在 step 70/585 崩溃，无日志、无 checkpoint、无监控。必须用 submit_training_job（tmux + cron）确保持久化和监控。
22	
23	### OOM 修复：batch_size + gradient_checkpointing (2026-05-14)
24	Qwen3-8B LoRA r=32 在 RTX 5090 32GB 上 batch_size=4 会 OOM（step 73 崩溃）。修复：batch_size=2 + gradient_accumulation_steps=8 + gradient_checkpointing=true → 显存 82% (26.8/32.6 GB)，成功完成 585 steps。
25	
26	### vLLM 不能直接加载 LoRA adapter (2026-05-14)
27	vLLM 需要加载 merged model（有 config.json），不能直接加载 LoRA adapter 目录。必须先用 LLaMA Factory export 或 PEFT merge 合并 adapter 到基座模型。
28	
29	### 训练配置必须保留 best checkpoint (2026-05-14)
30	ft_002_v2 的 best eval 在 ~step 300 但被 save_total_limit=3 删掉了。未来 SFT 训练配置必须加：
31	```yaml
32	load_best_model_at_end: true
33	metric_for_best_model: eval_loss
34	save_total_limit: 5  # 至少保证 best checkpoint 不被删
35	```
36	
37	### E1 否定乘性惩罚假说——RE SJ 问题是根本性的 (2026-05-14)
38	Component-wise 分解结果：
39	- head_sj ρ=0.210 **远低于** NER ρ_sj=0.383（Δ=-0.173）
40	- **每个 component 单独都比乘性组合差**——乘性组合实际在整合三个弱信号，不是在伤害
41	- additive fix 无效（additive ρ ≈ multiplicative ρ，差 0.001）
42	- **根因修正**：不是"乘性惩罚导致 RE SJ 差"，而是 span-level SJ 对 RE 任务**根本缺乏区分力**
43	- Fleiss'
…[truncated 1317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T09:34:41.926536+00:00_

Excellent! Now let me create a comprehensive summary with actual concrete examples by looking at the prompt templates and format specifications:

Based on my thorough exploration of the project codebase, I'll now provide a comprehensive report on the data formats, evaluation code, and preprocessing:

## Summary: Data Format, Evaluation Code, and Entity Types

### 1. UNIFIED UIE JSON FORMAT (Unified Information Extraction)

The project uses a **unified JSON schema** for all structured IE tasks. This format is enforced via XGrammar constrained decoding in vLLM.

**Full UIE JSON Schema:**
```json
{
  "entities": [
    {
      "text": "string",
      "type": "string",
      "start": integer,
      "end": integer
    }
  ],
  "relations": [
    {
      "head": "string",
      "tail": "string",
      "type": "string",
      "head_start": integer,
      "head_end": integer,
      "tail_start": integer,
      "tail_end": integer
    }
  ],
  "events": [
    {
      "trigger": {
        "text": "string",
        "type": "string",
        "start": integer,
        "end": integer
      },
      "arguments": [
        {
          "text": "string",
          "role": "string",
          "start": integer,
          "end": integer
        }
      ]
    }
  ]
}
```

**Key characteristics:**
- All spans are **character offsets** (not token indices)
- `start` and `end` are **character indices** where `start` is inclusive and `end` is exclusive
- For relations: `head_start`, `head_end`, `tail_start`, `tail_end` define head and tail entity spans
- The format always requires all three fields (entities, relations, events) even if empty

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py` (lines 18-85)**

---

### 2. SCIERC DATA CONVERSION & FORMAT

**SciERC Original Format (Training JSON):**
The raw SciERC data is in a document-per-line JSON format with token indices:
```json
{
  "doc_key": "document_id",
  "sentences": [["token1
…[truncated 10481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T09:34:41.926754+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research CoNLL-2003 NER dataset",
  "subagent_type": "general-purpose",
  "prompt": "Research the CoNLL-2003 NER dataset for use in a NER generalization experiment. I need concrete, up-to-date information:\n\n1. **HuggingFace availability**: Is it directly downloadable via `datasets.load_dataset(\"conll2003\")`? Or has it been restricted/removed? Check if there are alternative HF dataset IDs (e.g., \"eriktks/conll2003\", \"tner/conll2003\").\n\n2. **Entity types**: List all NER entity types (PER, ORG, LOC, MISC?)\n\n3. **Dataset size**: How many sentences in train/dev/test splits?\n\n4. **Data format**: It's BIO-tagged token-level. Show the exact format structure.\n\n5. **Licensing concerns**: Reuters news text - any access restrictions as of 2025-2026?\n\n6. **Existing UIE/JSON conversion**: Search for projects that have already converted CoNLL-2003 to unified IE JSON format, especially:\n   - InstructUIE (https://github.com/BeyonderXX/InstructUIE)\n   - USM (Universal Structured Model)\n   - GoLLIE\n   - Any other generative IE projects\n\nUse WebSearch and WebFetch to verify current HuggingFace status. Report concrete findings, not speculation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "tool_args": {
    "description": "Research CoNLL-2003 NER dataset",
    "subagent_type": "general-purpose",
    "prompt": "Research the CoNLL-2003 NER dataset for use in a NER generalization experiment. I need concrete, up-to-date information:\n\n1. **HuggingFace availability**: Is it directly downloadable via `datasets.load_dataset(\"conll2003\")`? Or has it been restricted/removed? Check if there are alternative HF dataset IDs (e.g., \"eriktks/conll2003\", \"tner/conll2003\").\n\n2. **Entity types**: List all NER entity types (PER, ORG, LOC, MISC?)\n\n3. **Dataset size**: How many sentences in train/dev/test splits?\n\n4. **Data format**: It's BIO-tagged token-level. Show the exact format structure.\n\n5. **Licensing concerns**: Reuters news text - any access restrictions as of 2025-2026?\n\n6. **Existing UIE/JSON conversion**: Search for projects that have already converted CoNLL-2003 to unified IE JSON format, especially:\n   - InstructUIE (https://github.com/BeyonderXX/InstructUIE)\n   - USM (Universal Structured Model)\n   - GoLLIE\n   - Any other generative IE projects\n\nUse WebSearch and WebFetch to verify current HuggingFace status. Report concrete findings, not speculation."
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T09:34:41.926955+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T09:34:41.927085+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T09:34:41.927227+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoNLL-2003 NER dataset HuggingFace availability 2025 2026 load_dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoNLL-2003 NER dataset HuggingFace availability 2025 2026 load_dataset"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T09:34:41.927351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE CoNLL-2003 JSON format conversion unified information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE CoNLL-2003 JSON format conversion unified information extraction"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T09:34:41.927468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE CoNLL-2003 NER generative IE JSON format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE CoNLL-2003 NER generative IE JSON format"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T09:34:41.927582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoNLL-2003 dataset removed HuggingFace Reuters license restriction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoNLL-2003 dataset removed HuggingFace Reuters license restriction 2025"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T09:34:41.927709+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research OntoNotes and other NER datasets",
  "subagent_type": "general-purpose",
  "prompt": "Research the following NER datasets for a generalization experiment. I need concrete, actionable information for each. Use WebSearch/WebFetch to verify.\n\n## OntoNotes 5.0\n- Is it freely available or requires LDC license?\n- Any public alternatives/mirrors? (e.g., \"tner/ontonotes5\", \"conll2012\" on HuggingFace)\n- Entity types (18 types?)\n- Test set size\n- Realistic to obtain by 2026-05-25 deadline?\n\n## GENIA\n- HuggingFace availability (dataset ID?)\n- Entity types (biomedical entities - what exactly?)\n- Test set size\n- Is it commonly used for NER benchmarking in recent papers?\n\n## Few-NERD\n- HuggingFace availability\n- Entity types (fine-grained? how many?)\n- Test set size\n- Suitable for standard NER evaluation?\n\n## WNUT-17\n- HuggingFace availability\n- Entity types\n- Test set size (reportedly small?)\n- Social media / emerging entities?\n\n## ACE05\n- LDC license required?\n- Any public workaround?\n\n## Other candidates\n- MIT Movie/Restaurant NER?\n- MultiNERD?\n- CrossNER?\n- WikiANN/WikiNER?\n- Any widely-cited, freely available NER dataset with >200 test instances\n\nFor each dataset, report: availability (free/restricted), HF dataset ID, entity types, train/test size, and how commonly cited it is in NER papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "tool_args": {
    "description": "Research OntoNotes and other NER datasets",
    "subagent_type": "general-purpose",
    "prompt": "Research the following NER datasets for a generalization experiment. I need concrete, actionable information for each. Use WebSearch/WebFetch to verify.\n\n## OntoNotes 5.0\n- Is it freely available or requires LDC license?\n- Any public alternatives/mirrors? (e.g., \"tner/ontonotes5\", \"conll2012\" on HuggingFace)\n- Entity types (18 types?)\n- Test set size\n- Realistic to obtain by 2026-05-25 deadline?\n\n## GENIA\n- HuggingFace availability (dataset ID?)\n- Entity types (biomedical entities - what exactly?)\n- Test set size\n- Is it commonly used for NER benchmarking in recent papers?\n\n## Few-NERD\n- HuggingFace availability\n- Entity types (fine-grained? how many?)\n- Test set size\n- Suitable for standard NER evaluation?\n\n## WNUT-17\n- HuggingFace availability\n- Entity types\n- Test set size (reportedly small?)\n- Social media / emerging entities?\n\n## ACE05\n- LDC license required?\n- Any public workaround?\n\n## Other candidates\n- MIT Movie/Restaurant NER?\n- MultiNERD?\n- CrossNER?\n- WikiANN/WikiNER?\n- Any widely-cited, freely available NER dataset with >200 test instances\n\nFor each dataset, report: availability (free/restricted), HF dataset ID, entity types, train/test size, and how commonly cited it is in NER papers."
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T09:34:41.927898+00:00_

Web search results for query: "CoNLL-2003 NER dataset HuggingFace availability 2025 2026 load_dataset"

Links: [{"title":"tner/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/conll2003"},{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"},{"title":"Loading Data - Recon","url":"https://kabirkhan.github.io/recon/tutorial/conll/loading/"},{"title":"ZihanWangKi/conllpp · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ZihanWangKi/conllpp"},{"title":"conll2003 dataset loads original data. · Issue #4248 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/4248"},{"title":"Loading Custom Datasets - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/loading-custom-datasets/6166"},{"title":"[Request] NER Scripts on CoNLL 2003 dataset · Issue #4250 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/4250"},{"title":"How to deal with differences between CoNLL 2003 dataset tokenisation and BER tokeniser when fine tuning NER model? - Intermediate - Hugging Face Forums","url":"https://discuss.huggingface.co/t/how-to-deal-with-differences-between-conll-2003-dataset-tokenisation-and-ber-tokeniser-when-fine-tuning-ner-model/11129"},{"title":"conll 2003 dataset source url is no longer valid · Issue #3582 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/3582"},{"title":"CoNLL2003 Dataset | Kaggle","url":"https://www.kaggle.com/datasets/juliangarratt/conll2003-dataset"}]

Based on the search results, here's what I found about the CoNLL-2003 NER dataset and its availability on HuggingFace:

## Dataset Availability on HuggingFace

The CoNLL-2003 NER dataset is available on HuggingFace and consists of news wire articles from the Reuters Corpus, annotated by people from the University of Antwerp. There are multiple versions available:

1. **Official HuggingFace version*
…[truncated 988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T09:34:41.928060+00:00_

Web search results for query: "CoNLL-2003 dataset removed HuggingFace Reuters license restriction 2025"

Links: [{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"},{"title":"conll2003 at main","url":"https://huggingface.co/datasets/conll2003/tree/main"},{"title":"tner/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/conll2003"},{"title":"conll2003.py · conll2003 at main","url":"https://huggingface.co/datasets/conll2003/blob/main/conll2003.py"},{"title":"conll 2003 dataset source url is no longer valid · Issue #3582 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/3582"},{"title":"README.md · conll2003 at main","url":"https://huggingface.co/datasets/conll2003/blob/main/README.md"},{"title":"README.md · eriktks/conll2003 at main","url":"https://huggingface.co/datasets/eriktks/conll2003/blob/main/README.md"},{"title":"README.md · eriktks/conll2003 at 9b32634fdcdb632e98eef59f45c99a70723535d2","url":"https://huggingface.co/datasets/eriktks/conll2003/blob/9b32634fdcdb632e98eef59f45c99a70723535d2/README.md"},{"title":"CoNLL2003 Dataset | Kaggle","url":"https://www.kaggle.com/datasets/juliangarratt/conll2003-dataset"},{"title":"Update files from the datasets library (from 1.18.0) · conll2003 at c9635d4","url":"https://huggingface.co/datasets/conll2003/commit/c9635d484ff855a5eadac4bcf1a3df2e7419abfb"}]

Based on the search results, I found information about the CoNLL-2003 dataset on HuggingFace and its Reuters license restrictions, but the results do not show any evidence of the dataset being removed in 2025 or any recent changes to the license restrictions.

The current search results show that:

The CoNLL-2003 dataset on HuggingFace requires agreement to be signed by all researchers using the Reuters Corpus at their organization. The dataset is still available on HuggingFace with a license marked as "other" and source datasets listed as "extended|ot
…[truncated 552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T09:34:41.928241+00:00_

Web search results for query: "InstructUIE CoNLL-2003 JSON format conversion unified information extraction"

Links: [{"title":"InstructUIE: Unified Info Extraction Framework | PDF | Conceptual Model | Information","url":"https://www.scribd.com/document/797504751/2304-08085v1"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://ar5iv.labs.arxiv.org/html/2304.08085"},{"title":"(PDF) A Tool for Converting Different Data Representation Formats","url":"https://www.academia.edu/9409249/A_Tool_for_Converting_Different_Data_Representation_Formats"},{"title":"A Tool for Converting Different Data Representation Formats | Springer Nature Link","url":"https://link.springer.com/content/pdf/10.1007/978-3-319-13817-6_28.pdf"},{"title":"Language-Independent Named Entity Recognition (II)","url":"https://www.clips.uantwerpen.be/conll2003/ner/"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"Convert command line on .iob Conll-2003 file not working · Issue #3620 · explosion/spaCy","url":"https://github.com/explosion/spaCy/issues/3620"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"}]

Based on the search results, here's what I found about InstructUIE and its relationship to CoNLL-2003:

## In
…[truncated 1459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T09:34:41.928406+00:00_

Web search results for query: "GoLLIE CoNLL-2003 NER generative IE JSON format"

Links: [{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668"},{"title":"Ner format to CONLL - usage - Prodigy Support","url":"https://support.prodi.gy/t/ner-format-to-conll/1153"},{"title":"Solving NER with RL | Israel Adewuyi","url":"https://israel-adewuyi.github.io/blog/2025/ner_with_rl/"},{"title":"ConLL-2003 Dataset: Named Entity Recognition (NER) | Innovatiana","url":"https://www.innovatiana.com/en/datasets/conll-2003"},{"title":"Language-Independent Named Entity Recognition (II)","url":"https://www.clips.uantwerpen.be/conll2003/ner/"},{"title":"Data preparation for NER in CONLL 2003 BIO formatWhat is CoNLL data format?Chunking Stanford Named Entity Recognizer (NER) outputs from NLTK formatAnnotated Training data for NER corpusHow to group up NER tags in order to get data from sentence as a whole?convert xml (into iob2 format for NER/ABSA)Training spaCy's NER model from scratch on CoNLL 2003 data got very weird resultsTensorFlow crashes for NER task using large dataWhat is the list of possible tags with a description of CoNLL 2003 NER Task?How to c","url":"http://styjun.blogspot.com/2019/06/data-preparation-for-ner-in-conll-2003.html"},{"title":"NER/corpus/CoNLL-2003 at master · synalp/NER","url":"https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003"},{"title":"sparknlp_jsl.training — Spark NLP documentation","url":"https://nlp.johnsnowlabs.com/licensed/api/python/reference/autosummary/sparknlp_jsl/training/index.html"},{"title":"CoNLL-2003 NER for English - flair-experiments - GitHub","url":"https://github.com/stefan-it/flair-experiments/blob/master/conll2003-ner-english/README.md"},{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"}]

Based on the search results, here's what I found about GoLLIE, CoNLL-2003 NER, and their connection:

## Go
…[truncated 1579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T09:34:41.928551+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T09:34:41.928670+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T09:34:41.928785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OntoNotes 5.0 NER dataset availability LDC license HuggingFace alternative 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OntoNotes 5.0 NER dataset availability LDC license HuggingFace alternative 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T09:34:41.928936+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Research UIE conversion scripts",
  "subagent_type": "general-purpose",
  "prompt": "Search for existing code that converts standard NER datasets (CoNLL-2003, OntoNotes, GENIA, Few-NERD, etc.) into a unified IE JSON format suitable for generative/LLM-based NER. \n\nThe target format is:\n```json\n{\n  \"entities\": [{\"text\": \"Barack Obama\", \"type\": \"PER\", \"start\": 0, \"end\": 12}],\n  \"relations\": [],\n  \"events\": []\n}\n```\nWhere start/end are character offsets.\n\nSearch for these specific projects and check if they include NER dataset converters:\n\n1. **InstructUIE** (BeyonderXX/InstructUIE on GitHub) - Does it include CoNLL-2003, OntoNotes conversion to its unified format?\n2. **GoLLIE** (hitz-zentroa/GoLLIE on GitHub) - What datasets does it support?\n3. **UniversalNER** - Does it have dataset processing scripts?\n4. **DeepKE** - NER data processing utilities?\n5. **YAYI-UIE** or similar Chinese UIE projects\n6. **LLaMA Factory** - Does it have any NER dataset conversion utilities?\n\nFor CoNLL-2003 specifically: converting from BIO token tags to character-offset spans is straightforward. I need to know if someone has already done it, or if I need to write ~50 lines of Python.\n\nUse WebSearch to find these repos and check their data processing code. Report which projects have ready-to-use converters and for which datasets."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "tool_args": {
    "description": "Research UIE conversion scripts",
    "subagent_type": "general-purpose",
    "prompt": "Search for existing code that converts standard NER datasets (CoNLL-2003, OntoNotes, GENIA, Few-NERD, etc.) into a unified IE JSON format suitable for generative/LLM-based NER. \n\nThe target format is:\n```json\n{\n  \"entities\": [{\"text\": \"Barack Obama\", \"type\": \"PER\", \"start\": 0, \"end\": 12}],\n  \"relations\": [],\n  \"events\": []\n}\n```\nWhere start/end are character offsets.\n\nSearch for these specific projects and check if they include NER dataset converters:\n\n1. **InstructUIE** (BeyonderXX/InstructUIE on GitHub) - Does it include CoNLL-2003, OntoNotes conversion to its unified format?\n2. **GoLLIE** (hitz-zentroa/GoLLIE on GitHub) - What datasets does it support?\n3. **UniversalNER** - Does it have dataset processing scripts?\n4. **DeepKE** - NER data processing utilities?\n5. **YAYI-UIE** or similar Chinese UIE projects\n6. **LLaMA Factory** - Does it have any NER dataset conversion utilities?\n\nFor CoNLL-2003 specifically: converting from BIO token tags to character-offset spans is straightforward. I need to know if someone has already done it, or if I need to write ~50 lines of Python.\n\nUse WebSearch to find these repos and check their data processing code. Report which projects have ready-to-use converters and for which datasets."
  }
}
````

</details>

---

### Tool call

_source line 65 · 2026-05-14T09:34:41.929118+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T09:34:41.929349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T09:34:41.929557+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/conll2003",
  "prompt": "What is the current status of this dataset? Is it gated, restricted, or freely downloadable? What are the entity types, dataset splits and sizes, and license information? Is there any notice about the dataset being removed or restricted?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/conll2003",
    "prompt": "What is the current status of this dataset? Is it gated, restricted, or freely downloadable? What are the entity types, dataset splits and sizes, and license information? Is there any notice about the dataset being removed or restricted?"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T09:34:41.929744+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T09:34:41.929937+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/eriktks/conll2003",
  "prompt": "What is the status of this dataset? Is it freely downloadable? What are the entity types, splits, sizes, and format? Any restrictions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/eriktks/conll2003",
    "prompt": "What is the status of this dataset? Is it freely downloadable? What are the entity types, splits, sizes, and format? Any restrictions?"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T09:34:41.930168+00:00_

Web search results for query: "OntoNotes 5.0 NER dataset availability LDC license HuggingFace alternative 2025 2026"

Links: [{"title":"tner/ontonotes5 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/ontonotes5"},{"title":"ontonotes/conll2012_ontonotesv5 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ontonotes/conll2012_ontonotesv5"},{"title":"OntoNotes Release 5.0 - Linguistic Data Consortium","url":"https://catalog.ldc.upenn.edu/LDC2013T19"},{"title":"OntoNotes 5.0 Dataset","url":"https://paperswithcode.com/dataset/ontonotes-5-0"},{"title":"OntoNotes Release 5.0 - LDC Catalog","url":"https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf"},{"title":"OntoNotes Release 5.0 - Linguistic Data Consortium","url":"https://abacus.library.ubc.ca/dataset.xhtml?persistentId=hdl:11272.1/AB2/MKJJ2R"},{"title":"nickprock/bert-finetuned-ner-ontonotes · Hugging Face","url":"https://huggingface.co/nickprock/bert-finetuned-ner-ontonotes"},{"title":"djagatiya/ner-ontonotes-v5-eng-v4 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/djagatiya/ner-ontonotes-v5-eng-v4"},{"title":"Ontonotes 5.0 - Dataset - LDM","url":"https://service.tib.eu/ldmservice/dataset/ontonotes-5-0"},{"title":"GitHub - datasets-mila/datasets--LDC--ontonotes · GitHub","url":"https://github.com/datasets-mila/datasets--LDC--ontonotes"}]

Based on the search results, here's what I found about OntoNotes 5.0 NER dataset availability:

## Official LDC Distribution

OntoNotes Release 5.0 is the final release of the OntoNotes project, a collaborative effort between BBN Technologies, the University of Colorado, the University of Pennsylvania and the University of Southern California's Information Sciences Institute. The official version is available from the Linguistic Data Consortium (LDC) under catalog number LDC2013T19.

## HuggingFace Alternatives

There are several OntoNotes 5.0 datasets available on HuggingFace:

1. Ontonotes5 NER dataset 
…[truncated 956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T09:34:41.930418+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tner/conll2003",
  "prompt": "What is the status of this dataset? Is it freely downloadable? What entity types does it contain, how many examples per split, and what format?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tner/conll2003",
    "prompt": "What is the status of this dataset? Is it freely downloadable? What entity types does it contain, how many examples per split, and what format?"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-14T09:34:41.930632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE BeyonderXX GitHub CoNLL-2003 OntoNotes data conversion unified format",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE BeyonderXX GitHub CoNLL-2003 OntoNotes data conversion unified format",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T09:34:41.930836+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE hitz-zentroa GitHub NER dataset processing CoNLL OntoNotes GENIA",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE hitz-zentroa GitHub NER dataset processing CoNLL OntoNotes GENIA",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-14T09:34:41.931036+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/BeyonderXX/InstructUIE",
  "prompt": "How does InstructUIE format NER data like CoNLL-2003? What JSON format does it use for NER tasks? Show the data format/schema for NER conversion. Look for IE INSTRUCTIONS format, data processing scripts, or example data formats."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/BeyonderXX/InstructUIE",
    "prompt": "How does InstructUIE format NER data like CoNLL-2003? What JSON format does it use for NER tasks? Show the data format/schema for NER conversion. Look for IE INSTRUCTIONS format, data processing scripts, or example data formats."
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T09:34:41.931257+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UniversalNER GitHub dataset processing scripts CoNLL NER conversion",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UniversalNER GitHub dataset processing scripts CoNLL NER conversion",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-14T09:34:41.931452+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepKE GitHub NER data processing BIO to JSON conversion",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepKE GitHub NER data processing BIO to JSON conversion",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-14T09:34:41.931637+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2310.03668",
  "prompt": "How does GoLLIE format NER data like CoNLL-2003? What code-based format does it use? Show the data schema/format for NER entities. How are entity types defined?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2310.03668",
    "prompt": "How does GoLLIE format NER data like CoNLL-2003? What code-based format does it use? Show the data schema/format for NER entities. How are entity types defined?"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-14T09:34:41.931830+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "YAYI-UIE GitHub Chinese NER unified information extraction data format",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "YAYI-UIE GitHub Chinese NER unified information extraction data format",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-14T09:34:41.932031+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLaMA-Factory GitHub NER dataset conversion processing",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLaMA-Factory GitHub NER dataset conversion processing",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T09:34:41.932235+00:00_

# CoNLL-2003 Dataset Summary

## Status & Availability
The dataset is **publicly available** on Hugging Face but has **licensing restrictions**. While freely downloadable from the Hugging Face platform, the underlying Reuters Corpus data requires signing legal agreements with NIST.

## Entity Types
The dataset contains **4 named entity types** (IOB2 tagging scheme):
- **PER** (Person): B-PER, I-PER
- **ORG** (Organization): B-ORG, I-ORG
- **LOC** (Location): B-LOC, I-LOC
- **MISC** (Miscellaneous): B-MISC, I-MISC
- **O** (Outside): Not part of any entity

## Dataset Splits & Sizes

| Split | Size |
|-------|------|
| Train | 14,041 sentences |
| Validation | 3,250 sentences |
| Test | 3,453 sentences |

**Total disk usage:** 15.11 MB

## Data Format
Each instance contains:
- `tokens`: list of words
- `ner_tags`: NER labels (indices 0-8)
- `pos_tags`: Part-of-speech tags (indices 0-46)
- `chunk_tags`: Syntactic chunk tags (indices 0-22)
- `id`: unique identifier

### Example
```python
{
    "tokens": ["The", "European", "Commission", "said", ...],
    "ner_tags": [0, 3, 4, 0, 0, ...],
    "pos_tags": [12, 22, 22, 38, 15, ...],
    "chunk_tags": [11, 12, 12, 21, 13, ...]
}
```

## Restrictions
**Copyright Notice:** 
- Data sourced from Reuters Corpus (Reuters Ltd/Thomson Reuters)
- Requires signed agreements:
  - **Organizational agreement** (for your institution)
  - **Individual agreement** (for each researcher)
- Must be obtained from NIST for research purposes

**Note:** The dataset viewer on Hugging Face is disabled because it requires Python code execution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-14T09:34:41.932432+00:00_

# CoNLL-2003 NER Dataset Overview

## Status & Availability
The dataset is **freely downloadable** from Hugging Face's datasets repository. However, note that the actual text comes from the Reuters Corpus, which requires signing agreements with NIST for research use (both organizational and individual agreements are required).

## Entity Types
The dataset contains **4 entity types**:
- `ORG` (Organization)
- `PER` (Person)
- `LOC` (Location)
- `MISC` (Miscellaneous)

## Dataset Size & Splits

| Split | Examples |
|-------|----------|
| **Train** | 14,041 |
| **Validation** | 3,250 |
| **Test** | 3,453 |
| **Total** | 20,744 |

## Data Format

The dataset uses a **token classification** format with two fields per example:

```python
{
  'tokens': ['EU', 'rejects', 'German', 'call', 'to', 'boycott', 'British', 'lamb', '.'],
  'tags': [1, 0, 2, 0, 0, 0, 2, 0, 0]
}
```

### Label IDs
```json
{
  "O": 0,           # Outside
  "B-ORG": 1,       # Begin Organization
  "B-MISC": 2,      # Begin Miscellaneous
  "B-PER": 3,       # Begin Person
  "I-PER": 4,       # Inside Person
  "B-LOC": 5,       # Begin Location
  "I-ORG": 6,       # Inside Organization
  "I-MISC": 7,      # Inside Miscellaneous
  "I-LOC": 8        # Inside Location
}
```

## Additional Details
- **Domain**: News wire articles (Reuters Corpus)
- **Language**: English
- **Format**: Available in Parquet and Hugging Face Datasets format
- **Total Size**: 3.95 MB

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-14T09:34:41.932587+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GENIA NER dataset HuggingFace entity types test set size biomedical NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GENIA NER dataset HuggingFace entity types test set size biomedical NER"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-14T09:34:41.932792+00:00_

# InstructUIE Data Format Information

Based on the provided GitHub page content, I cannot provide specific details about how InstructUIE formats NER data like CoNLL-2003 or its JSON schema for NER tasks.

## What the Documentation Shows

The page indicates that InstructUIE is "built based on the pretrained Flan T5 model, and finetuned on our data (**IE INSTRUCTIONS**)." However, the actual data format specifications, conversion scripts, and example schemas are not included in this GitHub repository overview.

## Where to Find This Information

To discover the actual data formatting details, you would need to:

1. **Download the training data** from Baidu NetDisk or Google Drive (linked in the repo)
2. **Examine the source code** in the `/data` and `/src` directories
3. **Review data processing scripts** in the `/scripts` folder
4. **Check the Hugging Face model card** for the released 11B checkpoint at `ZWK/InstructUIE`

The README focuses on setup, training, and evaluation instructions rather than data schema documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-14T09:34:41.932976+00:00_

Web search results for query: "InstructUIE BeyonderXX GitHub CoNLL-2003 OntoNotes data conversion unified format"

Links: [{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning","url":"https://github.com/beyonderxx/instructuie"},{"title":"GitHub - faker2cumtb/OntoNotes-5.0-NER-BIO: A BIO formatted Named Entity Recognition data set extracted from the OntoNotes 5.0 release.","url":"https://github.com/faker2cumtb/OntoNotes-5.0-NER-BIO"},{"title":"GitHub - taotao033/conll-formatted-ontonotes-5.0_for_chinese_language: conll-formatted-ontonotes-5.0 for chinese language","url":"https://github.com/taotao033/conll-formatted-ontonotes-5.0_for_chinese_language"},{"title":"GitHub - ontonotes/conll-formatted-ontonotes-5.0: This is a CoNLL formatted version of the OntoNotes 5.0 release. · GitHub","url":"https://github.com/ontonotes/conll-formatted-ontonotes-5.0"},{"title":"Using OntoNotes 5.0 to generate coNLL files · Issue #60 · huggingface/neuralcoref","url":"https://github.com/huggingface/neuralcoref/issues/60"},{"title":"GitHub - MaviccPRP/ger_ner_evals","url":"https://github.com/MaviccPRP/ger_ner_evals"},{"title":"GitHub - propbank/propbank-release: The official released annotations, both in .prop pointer format and as conll files. Does not contain the source texts","url":"https://github.com/propbank/propbank-release"},{"title":"Converting Ontonotes ( .gold_conll file format) to DocBins ( .spacy file format) · explosion/spaCy · Discussion #12222","url":"https://github.com/explosion/spaCy/discussions/12222"},{"title":"Using OntoNotes 5.0 to generate coNLL files · Issue #2 · ontonotes/conll-formatted-ontonotes-5.0","url":"https://github.com/ontonotes/conll-formatted-ontonotes-5.0/issues/2"},{"title":"GitHub - nicoladisabato/ner-with-transformers: Named Entity Recognition with Transformer-based models using SpaCy","url":"https://github.com/nicoladisabato/ner-with-transformers"}]

Based on the search results, here's what I found:


…[truncated 1262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-14T09:34:41.933157+00:00_

Web search results for query: "GoLLIE hitz-zentroa GitHub NER dataset processing CoNLL OntoNotes GENIA"

Links: [{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"cogcomp-nlp/ner at master · CogComp/cogcomp-nlp","url":"https://github.com/CogComp/cogcomp-nlp/tree/master/ner"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"Releases · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/releases"},{"title":"Issues · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/issues"},{"title":"GitHub - MaviccPRP/ger_ner_evals","url":"https://github.com/MaviccPRP/ger_ner_evals"},{"title":"is this using CoNll dataset for training NER tag ? dose the code support ontonotes as well? · Issue #58 · kamalkraj/BERT-NER","url":"https://github.com/kamalkraj/BERT-NER/issues/58"},{"title":"GitHub - ay94/NER-datasets · GitHub","url":"https://github.com/ay94/NER-datasets"},{"title":"flair/resources/docs/EXPERIMENTS.md at master · flairNLP/flair","url":"https://github.com/flairNLP/flair/blob/master/resources/docs/EXPERIMENTS.md"},{"title":"GitHub - manliu1225/mrc-for-flat-nested-ner · GitHub","url":"https://github.com/manliu1225/mrc-for-flat-nested-ner"}]

Based on the search results, here's what I found:

## GoLLIE Project Overview

GoLLIE is a Large Language Model trained to follow annotation guidelines, and it outperforms previous approaches on zero-shot Information Extraction while allowing users to perform inferences with annotation schemas defined on the fly.

## Dataset Processing

The GoLLIE project processes multiple NER datasets. The codebase includes configuration files f
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-14T09:34:41.933355+00:00_

Web search results for query: "UniversalNER GitHub dataset processing scripts CoNLL NER conversion"

Links: [{"title":"GitHub - universal-ner/universal-ner · GitHub","url":"https://github.com/universal-ner/universal-ner"},{"title":"Universal NER · GitHub","url":"https://github.com/UniversalNER"},{"title":"GitHub - UniversalNER/uner_code: Utility code (training, data munging) for Universal NER","url":"https://github.com/UniversalNER/uner_code"},{"title":"universal-ner - Overview","url":"https://github.com/universal-ner"},{"title":"cogcomp-nlp/ner at master · CogComp/cogcomp-nlp","url":"https://github.com/CogComp/cogcomp-nlp/tree/master/ner"},{"title":"universal-ner/README.md at main · mivanovitch/universal-ner","url":"https://github.com/mivanovitch/universal-ner/blob/main/README.md"},{"title":"GitHub - UniversalNER/UNER_English-PUD: NER Annotations on English Parallel Universal Dependencies (PUD)","url":"https://github.com/UniversalNER/UNER_English-PUD"},{"title":"GitHub - UniversalNER/UNER_Swedish-Talbanken: NER on Swedish Talbanken Dataset","url":"https://github.com/UniversalNER/UNER_Swedish-Talbanken"},{"title":"universal-ner/README.md at main · universal-ner/universal-ner","url":"https://github.com/universal-ner/universal-ner/blob/main/README.md"},{"title":"GitHub - congruence-engine/universal-ner-with-gliner: Repository of the \"Universal NER with GLiNER\" investigation · GitHub","url":"https://github.com/congruence-engine/universal-ner-with-gliner"}]

Based on the search results, I found several relevant resources related to UniversalNER:

## Key GitHub Repositories

There is a utility code repository (UniversalNER/uner_code) that contains training and data munging code for Universal NER.

The training code is adapted from FastChat, with documentation on how to finetune the LLama base model with UniversalNER data.

## Dataset Information

Due to licensing restrictions associated with many NER datasets used in the evaluation, only the CrossNER and MIT datasets a
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-14T09:34:41.933504+00:00_

# GoLLIE's Code-Based NER Format

GoLLIE uses Python code representation for Named Entity Recognition tasks. Here's how it structures NER data:

## Schema Definition

For NER datasets like CoNLL-2003, entity types are represented as Python classes. According to the paper, "classes for a NER dataset merely require an attribute to specify the text span that corresponds to the class."

## Format Components

The input consists of three parts:

1. **Schema Definition**: Python classes representing entity types with docstrings containing guidelines and code comments showing representative candidates

2. **Input Text**: The raw text to be annotated, represented as a Python string variable

3. **Output Annotations**: A list of entity instances following the class definitions, generated after `result =`

## Example Structure

For NER, each entity class would include:
- Class name (e.g., `Person`, `Organization`, `Location`)
- A docstring with the guideline definition
- An attribute for the text span
- Comments showing example candidates

The paper notes that "parsing the output is straightforward; executing the generated code in Python yields a list containing the result," making the structured format both human-readable and computationally efficient.

This approach enables GoLLIE to handle diverse annotation schemas while maintaining consistent formatting across different information extraction tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-14T09:34:41.933648+00:00_

Web search results for query: "DeepKE GitHub NER data processing BIO to JSON conversion"

Links: [{"title":"DeepKE/example/llm/InstructKGC/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/InstructKGC/README.md"},{"title":"DeepKE/example/ner/standard/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/ner/standard/README.md"},{"title":"DeepKE/example/ner/standard at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/tree/main/example/ner/standard"},{"title":"DeepKE/example/llm/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/README.md/"},{"title":"Releases · zjunlp/DeepKE","url":"https://github.com/zjunlp/deepke/releases"},{"title":"DeepKE/example/ner/few-shot at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot"},{"title":"How to convert simple NER format to spacy json · Issue #1966 · explosion/spaCy","url":"https://github.com/explosion/spaCy/issues/1966"},{"title":"GitHub - OpenKG-ORG/DeepKE: An Open Toolkit for Knowledge Graph Extraction and Construction published at EMNLP2022 System Demonstrations.","url":"https://github.com/OpenKG-ORG/DeepKE"},{"title":"DeepKE/tutorial-notebooks/ner/few-shot/fewshot_ner_tutorial.ipynb at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/ner/few-shot/fewshot_ner_tutorial.ipynb"},{"title":"DeepKE/example/llm/OneKE.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/OneKE.md"}]

Based on the search results, I found information about DeepKE and NER data processing. Here's what I discovered:

## DeepKE NER Data Processing Overview

DeepKE contains a unified framework for named entity recognition, relation extraction and attribute extraction. The toolkit supports various data formats and processing tasks.

## Data Format and JSON Conversion

DeepKE processes instruction
…[truncated 958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-14T09:34:41.933798+00:00_

Web search results for query: "LLaMA-Factory GitHub NER dataset conversion processing"

Links: [{"title":"Datasets · hiyouga/LLaMA-Factory Wiki · GitHub","url":"https://github.com/hiyouga/LLaMA-Factory/wiki/Datasets"},{"title":"GitHub - lbnlp/nerre-llama: Repository for training LLaMa 2 models using the NERRE format.","url":"https://github.com/lbnlp/nerre-llama"},{"title":"Sharegpt datasets not working. Error during dataset conversion: Unsupported cast from struct to utf8 · Issue #2471 · hiyouga/LLaMA-Factory","url":"https://github.com/hiyouga/LLaMA-Factory/issues/2471"},{"title":"hiyouga/LLaMA-Factory: Unified Efficient Fine-Tuning of ...","url":"https://github.com/hiyouga/LlamaFactory"},{"title":"ValueError: Processor was not found, please check and update your model file. · Issue #8855 · hiyouga/LlamaFactory","url":"https://github.com/hiyouga/LlamaFactory/issues/8855"},{"title":"Releases · hiyouga/LLaMA-Factory","url":"https://github.com/hiyouga/LLaMA-Factory/releases"},{"title":"GitHub - 4AI/LS-LLaMA: A Simple but Powerful SOTA NER Model | Official Code For Label Supervised LLaMA Finetuning","url":"https://github.com/4AI/LS-LLaMA"},{"title":"GitHub - mhardik003/LLaMA-Factory: Refactored code for more grip on training loss and labels in the original llama factory code","url":"https://github.com/mhardik003/LLaMA-Factory"},{"title":"GitHub - lathashree01/ClinicalRE_n2c2: LLaMA based Clinical RE for n2c2 2018 dataset · GitHub","url":"https://github.com/lathashree01/ClinicalRE_n2c2"},{"title":"Converting format of dataset not running · Issue #3109 · hiyouga/LLaMA-Factory","url":"https://github.com/hiyouga/LLaMA-Factory/issues/3109"}]

I've performed the web search for "LLaMA-Factory GitHub NER dataset conversion processing." Here are the key findings:

## LLaMA-Factory Overview

LLaMA-Factory is a unified efficient fine-tuning system for 100+ LLMs & VLMs (published at ACL 2024).

## Dataset Conversion and Processing

The search results reveal that LLaMA-Factory invol
…[truncated 1185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-14T09:34:41.933949+00:00_

Web search results for query: "GENIA NER dataset HuggingFace entity types test set size biomedical NER"

Links: [{"title":"OpenMed/OpenMed-NER-DNADetect-SuperClinical-184M · Hugging Face","url":"https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-SuperClinical-184M"},{"title":"d4data/biomedical-ner-all · Hugging Face","url":"https://huggingface.co/d4data/biomedical-ner-all"},{"title":"BioSynNER: Synthetic Data for Biomedical Named Entity Recognition","url":"https://openreview.net/pdf?id=tLfUZEGcL1"},{"title":"jnlpba · Datasets at Hugging Face","url":"https://huggingface.co/datasets/jnlpba"},{"title":"OpenMed/OpenMed-NER-GenomicDetect-PubMed-109M · Hugging Face","url":"https://huggingface.co/OpenMed/OpenMed-NER-GenomicDetect-PubMed-109M"},{"title":"OpenMed/OpenMed-NER-DNADetect-SuperClinical-434M · Hugging Face","url":"https://huggingface.co/OpenMed/OpenMed-NER-DNADetect-SuperClinical-434M"},{"title":"OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M · Hugging Face","url":"https://huggingface.co/OpenMed/OpenMed-NER-DiseaseDetect-BioMed-335M"},{"title":"EMBO/SourceData · Datasets at Hugging Face","url":"https://huggingface.co/datasets/EMBO/SourceData"},{"title":"Configuration of GENIA corpus. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Configuration-of-GENIA-corpus_fig1_10667350"},{"title":"OpenMed/OpenMed-NER-OncologyDetect-MultiMed-568M · Hugging Face","url":"https://huggingface.co/OpenMed/OpenMed-NER-OncologyDetect-MultiMed-568M"}]

Based on the search results, here's what I found about the GENIA NER dataset:

## GENIA Dataset Overview

The GENIA dataset consists of 1,999 Medline abstracts, annotated with multiple layers of linguistic and semantic information, aimed at supporting information extraction in molecular biology.

## Entity Types

The dataset contains annotations for five entity types: protein, DNA, RNA, cell line, and cell type, making it essential for molecular biology and genomics research applications. However, 36 terminal 
…[truncated 542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-14T09:34:41.934099+00:00_

Web search results for query: "YAYI-UIE GitHub Chinese NER unified information extraction data format"

Links: [{"title":"GitHub - wenge-research/YAYI-UIE: 雅意信息抽取大模型：在百万级人工构造的高质量信息抽取数据上进行指令微调，由中科闻歌算法团队研发。 (Repo for YAYI Unified Information Extraction Model)","url":"https://github.com/wenge-research/YAYI-UIE"},{"title":"YAYI-UIE/README_EN.md at main · wenge-research/YAYI-UIE","url":"https://github.com/wenge-research/YAYI-UIE/blob/main/README_EN.md"},{"title":"GitHub - ChocoWu/LasUIE: Universal Information Extraction, codes for the NeurIPS-2022 paper: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model. · GitHub","url":"https://github.com/ChocoWu/LasUIE"},{"title":"Activity · wenge-research/YAYI-UIE","url":"https://github.com/wenge-research/YAYI-UIE/activity"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"GitHub - universal-ie/UIE: Unified Structure Generation for Universal Information Extraction","url":"https://github.com/universal-ie/UIE"},{"title":"GitHub - zjunlp/IEPile: [ACL 2024] IEPile: A Large-Scale Information Extraction Corpus · GitHub","url":"https://github.com/zjunlp/IEPile"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"GitHub - taishan1994/awesome-chinese-ner: 中文命名实体识别。包含目前最新的中文命名实体识别论文、中文实体识别相关工具、数据集，以及中文预训练模型、词向量、实体识别综述等。","url":"https://github.com/taishan1994/awesome-chinese-ner"}]

I found the information about YAYI-UIE. Here are the key details:

## YAYI-UIE Overview

YAYI-UIE (雅意信息抽取统一大模型) is a unified information extraction model fine-tuned on millions 
…[truncated 1392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-14T09:34:41.934300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Few-NERD dataset HuggingFace entity types fine-grained NER test size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Few-NERD dataset HuggingFace entity types fine-grained NER test size"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-14T09:34:41.934438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE IE INSTRUCTIONS data format NER JSON example \"entity_list\" OR \"entities\" OR \"label\" site:github.com"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE IE INSTRUCTIONS data format NER JSON example \"entity_list\" OR \"entities\" OR \"label\" site:github.com"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-14T09:34:41.934571+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "USM \"Universal Structured Model\" NER CoNLL-2003 unified format JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "USM \"Universal Structured Model\" NER CoNLL-2003 unified format JSON"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-14T09:34:41.934699+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "conll2003 load_dataset error 2024 2025 \"FileNotFoundError\" OR \"ConnectionError\" OR \"gated\" OR \"deprecated\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "conll2003 load_dataset error 2024 2025 \"FileNotFoundError\" OR \"ConnectionError\" OR \"gated\" OR \"deprecated\""
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-14T09:34:41.934826+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE GitHub src/ie_instructions data converter NER CoNLL conll2003 site:github.com/BeyonderXX",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE GitHub src/ie_instructions data converter NER CoNLL conll2003 site:github.com/BeyonderXX",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-14T09:34:41.934998+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/BeyonderXX/InstructUIE/blob/master/data/NER/sample.json",
  "prompt": "Show the complete JSON format used by InstructUIE for NER data. What are the field names and structure?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/BeyonderXX/InstructUIE/blob/master/data/NER/sample.json",
    "prompt": "Show the complete JSON format used by InstructUIE for NER data. What are the field names and structure?"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-14T09:34:41.935196+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-14T09:34:41.935349+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE src/tasks conll2003 ontonotes data_loader reader github hitz-zentroa",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE src/tasks conll2003 ontonotes data_loader reader github hitz-zentroa",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-14T09:34:41.935486+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IEPile zjunlp GitHub NER dataset conversion CoNLL-2003 character offset JSON format",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IEPile zjunlp GitHub NER dataset conversion CoNLL-2003 character offset JSON format",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-14T09:34:41.935616+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UIE universal-ie GitHub data processing CoNLL NER entity extraction unified format converter",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UIE universal-ie GitHub data processing CoNLL NER entity extraction unified format converter",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-14T09:34:41.935751+00:00_

Web search results for query: "Few-NERD dataset HuggingFace entity types fine-grained NER test size"

Links: [{"title":"DFKI-SLT/few-nerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/DFKI-SLT/few-nerd"},{"title":"README.md · DFKI-SLT/few-nerd at main","url":"https://huggingface.co/datasets/DFKI-SLT/few-nerd/blob/main/README.md"},{"title":"dfki-nlp/few-nerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/dfki-nlp/few-nerd"},{"title":"GitHub - thunlp/Few-NERD: Code and data of ACL 2021 paper \"Few-NERD: A Few-shot Named Entity Recognition Dataset\" · GitHub","url":"https://github.com/thunlp/Few-NERD"},{"title":"Few-NERD","url":"https://ningding97.github.io/fewnerd/"},{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.248/"},{"title":"[2105.07464] Few-NERD: A Few-Shot Named Entity Recognition Dataset","url":"https://arxiv.org/abs/2105.07464"},{"title":"(PDF) Few-NERD: A Few-shot Named Entity Recognition Dataset","url":"https://www.academia.edu/78460366/Few_NERD_A_Few_shot_Named_Entity_Recognition_Dataset"},{"title":"FEW-NERD: A Few-shot Named Entity Recognition Dataset","url":"https://aclanthology.org/2021.acl-long.248.pdf"},{"title":"Few-NERD","url":"https://www.kaggle.com/datasets/nbroad/fewnerd"}]

Based on the search results, here's what I found about the Few-NERD dataset:

## Dataset Overview

Few-NERD is a large-scale, fine-grained manually annotated named entity recognition dataset, which contains 8 coarse-grained types, 66 fine-grained types, 188,200 sentences, 491,711 entities, and 4,601,223 tokens.

## Entity Types

The dataset includes coarse-grained entity types (O, art, building, event, location, organization, other, person, product) and fine-grained entity types that are more specific subcategories, such as art-broadcastprogram, art-film, art-music, art-other, art-painting, art-writtenart, building-airport, building-hospital, building-hotel
…[truncated 800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-14T09:34:41.935906+00:00_

Web search results for query: "USM "Universal Structured Model" NER CoNLL-2003 unified format JSON"

Links: [{"title":"NER/corpus/CoNLL-2003 at master · synalp/NER","url":"https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003"},{"title":"Universal Information Extraction as Unified Semantic Matching | Request PDF","url":"https://www.researchgate.net/publication/371922000_Universal_Information_Extraction_as_Unified_Semantic_Matching"},{"title":"Language-Independent Named Entity Recognition (II)","url":"https://www.clips.uantwerpen.be/conll2003/ner/"},{"title":"The Stanford Natural Language Processing Group","url":"https://nlp.stanford.edu/projects/project-ner.shtml"},{"title":"Named Entity Recognition (NER) for CoNLL dataset with Tensorflow 2.2.0 | by Bhuvana Kundumani | Analytics Vidhya | Medium","url":"https://medium.com/analytics-vidhya/ner-tensorflow-2-2-0-9f10dcf5a0a"},{"title":"GitHub - kyzhouhzau/BERT-NER: Use Google's BERT for named entity recognition （CoNLL-2003 as the dataset）.","url":"https://github.com/kyzhouhzau/BERT-NER"},{"title":"Named entity recognition | NLP-progress","url":"http://nlpprogress.com/english/named_entity_recognition.html"},{"title":"Fine Tuning BERT for NER on CoNLL 2003 dataset with TF 2.0 | by Bhuvana Kundumani | Analytics Vidhya | Medium","url":"https://medium.com/analytics-vidhya/fine-tuning-bert-for-ner-on-conll-2003-dataset-with-tf-2-2-0-2f242ca2ce06"},{"title":"GitHub - janmejaya-nanda/NER-CoNLL-2003: Named Entity Recognition using CoNLL 2003","url":"https://github.com/janmejaya-nanda/NER-CoNLL-2003"},{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"}]

Based on the search results, I found relevant information about the components of your query:

**USM (Universal Structured Model):**
USM is a Unified Semantic Matching framework that universally models various IE (Information Extraction) tasks with three unified token linking operations to model the abilities of
…[truncated 1206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-14T09:34:41.936071+00:00_

Web search results for query: "InstructUIE IE INSTRUCTIONS data format NER JSON example "entity_list" OR "entities" OR "label" site:github.com"

Links: [{"title":"GitHub - FareedKhan-dev/big-data-with-KG: Handling Big Data with Knowledge Graph: A Detailed Guide · GitHub","url":"https://github.com/FareedKhan-dev/big-data-with-KG"},{"title":"GitHub - tecoholic/ner-annotator: Named Entity Recognition (NER) Annotation tool for SpaCy. Generates Traning Data as a JSON which can be readily used. · GitHub","url":"https://github.com/tecoholic/ner-annotator"},{"title":"GitHub - fastino-ai/GLiNER2: Unified Schema-Based Information Extraction · GitHub","url":"https://github.com/fastino-ai/GLiNER2"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"GitHub - Kissabi/QuickEntity: A python library to train custom Namely Entity Recognition easily.","url":"https://github.com/kissabi/quickentity"},{"title":"GitHub - ZunainAliAzam/Medical-Data-NER-with-BERT: This project leverages BERT for Named Entity Recognition (NER) on a medical dataset. The notebook provides a step-by-step guide, from dataset preparation to fine-tuning and saving the trained model for medical NER tasks.","url":"https://github.com/ZunainAliAzam/Medical-Data-NER-with-BERT"},{"title":"How to convert simple NER format to spacy json · Issue #1966 · explosion/spaCy","url":"https://github.com/explosion/spaCy/issues/1966"},{"title":"How to train NER and Relation Extraction model together · explosion/spaCy · Discussion #9139","url":"https://github.com/explosion/spaCy/discussions/9139"},{"title":"amazon-custom-entity-recognition-textract-comprehend/Textract_Comprehend_Custom_Entity_Recognition.ipynb at master · aws-samples/amazon-custom-entity-recognition-textract-comp
…[truncated 1804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-14T09:34:41.936254+00:00_

Web search results for query: "conll2003 load_dataset error 2024 2025 "FileNotFoundError" OR "ConnectionError" OR "gated" OR "deprecated""

Links: [{"title":"Cannot load Conll2003 - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/cannot-load-conll2003/169142"},{"title":"conll 2003 dataset source url is no longer valid · Issue #3582 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/3582"},{"title":"CONLL2003 Dataset not available · Issue #3904 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/3904"},{"title":"eriktks/conll2003 · Have problem in loading data through load_dataset(), saying \"Dataset scripts are no longer supported, but found conll2003.py\"","url":"https://huggingface.co/datasets/eriktks/conll2003/discussions/13"},{"title":"eriktks/conll2003 · FileNotFoundError when trying to download","url":"https://huggingface.co/datasets/eriktks/conll2003/discussions/1"},{"title":"Source of RunTime Error conll2003 dataset - Course - Hugging Face Forums","url":"https://discuss.huggingface.co/t/source-of-runtime-error-conll2003-dataset/169900"},{"title":"Dataset scripts are no longer supported, but found superb.py · Issue #7693 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/7693"},{"title":"Loading Data - Recon","url":"https://kabirkhan.github.io/recon/tutorial/conll/loading/"},{"title":"Dataset scripts are no longer supported - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/dataset-scripts-are-no-longer-supported/163891"},{"title":"Loading Custom Datasets - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/loading-custom-datasets/6166"}]

Based on the search results, here are the main issues related to loading the conll2003 dataset with errors in 2024-2025:

## Recent Issues (2024-2025)

A common error is: "RuntimeError: Dataset scripts are no longer supported, but found conll2003.py". This was reported as rec
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-14T09:34:41.936422+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WNUT-17 NER dataset HuggingFace entity types test set size emerging entities"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WNUT-17 NER dataset HuggingFace entity types test set size emerging entities"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-14T09:34:41.936560+00:00_

Web search results for query: "GoLLIE src/tasks conll2003 ontonotes data_loader reader github hitz-zentroa"

Links: [{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"Releases · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/releases"},{"title":"Issues · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/issues"},{"title":"GoLLIE/notebooks/Create Custom Task.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Create%20Custom%20Task.ipynb"},{"title":"GoLLIE/notebooks/Relation Extraction.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb"},{"title":"Converting Ontonotes ( .gold_conll file format) to DocBins ( .spacy file format) · explosion/spaCy · Discussion #12222","url":"https://github.com/explosion/spaCy/discussions/12222"},{"title":"conll-2003 · GitHub Topics","url":"https://github.com/topics/conll-2003"},{"title":"HiTZ zentroa · GitHub","url":"https://github.com/hitz-zentroa"},{"title":"Using OntoNotes 5.0 to generate coNLL files · Issue #60 · huggingface/neuralcoref","url":"https://github.com/huggingface/neuralcoref/issues/60"},{"title":"Named-Entity-Recognition-NER-Papers/ner_dataset.md at master · pfliu-nlp/Named-Entity-Recognition-NER-Papers","url":"https://github.com/pfliu-nlp/Named-Entity-Recognition-NER-Papers/blob/master/ner_dataset.md"}]

Based on the search results, I found information about the GoLLIE project on GitHub:

## GoLLIE Repository Overview

GoLLIE is a Large Language Model trained to follow annotation guidelines that outperforms previous approaches on zero-shot Information Extraction and allows users to perform inferences with annotation schemas defined on the fly.

## Data Configuration and Tasks

Configuration files used to generate the GoLLIE dataset
…[truncated 794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-14T09:34:41.936717+00:00_

Web search results for query: "IEPile zjunlp GitHub NER dataset conversion CoNLL-2003 character offset JSON format"

Links: [{"title":"GitHub - zjunlp/IEPile: [ACL 2024] IEPile: A Large-Scale Information Extraction Corpus · GitHub","url":"https://github.com/zjunlp/IEPile"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"DeepKE/example/ner/few-shot at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot"},{"title":"GitHub - zjunlp/KnowLM: An Open-sourced Knowledgable Large Language Model Framework. · GitHub","url":"https://github.com/zjunlp/KnowLM"},{"title":"NER/corpus/CoNLL-2003 at master · synalp/NER","url":"https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003"},{"title":"GitHub - ay94/NER-datasets · GitHub","url":"https://github.com/ay94/NER-datasets"},{"title":"GitHub - MaviccPRP/ger_ner_evals","url":"https://github.com/MaviccPRP/ger_ner_evals"},{"title":"GitHub - kyzhouhzau/BERT-NER: Use Google's BERT for named entity recognition （CoNLL-2003 as the dataset）.","url":"https://github.com/kyzhouhzau/BERT-NER"},{"title":"GitHub - flairNLP/CleanCoNLL: The CleanCoNLL dataset from our EMNLP 2023 paper where we corrected annotation errors and inconsistencies in CoNLL-03.","url":"https://github.com/flairNLP/CleanCoNLL"},{"title":"DeepKE/example/llm/InstructKGC/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/InstructKGC/README.md"}]

Based on the search results, I found relevant information about IEPile and its relationship to CoNLL-2003 NER datasets:

## Key Findings

IEPile includes a structure with English Unified Format Data containing NER datasets, including CoNLL2003 with train.json, dev.json, test.json files, and 
…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-14T09:34:41.936885+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://discuss.huggingface.co/t/cannot-load-conll2003/169142",
  "prompt": "What is the current issue with loading conll2003? What is the recommended workaround or alternative dataset ID that works? What exact error message appears?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://discuss.huggingface.co/t/cannot-load-conll2003/169142",
    "prompt": "What is the current issue with loading conll2003? What is the recommended workaround or alternative dataset ID that works? What exact error message appears?"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-14T09:34:41.937045+00:00_

Web search results for query: "UIE universal-ie GitHub data processing CoNLL NER entity extraction unified format converter"

Links: [{"title":"GitHub - universal-ie/UIE: Unified Structure Generation for Universal Information Extraction","url":"https://github.com/universal-ie/UIE"},{"title":"GitHub - ChocoWu/LasUIE: Universal Information Extraction, codes for the NeurIPS-2022 paper: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model. · GitHub","url":"https://github.com/ChocoWu/LasUIE"},{"title":"UIE/docs/DATASETS.md at main · universal-ie/UIE","url":"https://github.com/universal-ie/UIE/blob/main/docs/DATASETS.md"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"UIE/run_uie_pretrain.py at main · universal-ie/UIE","url":"https://github.com/universal-ie/UIE/blob/main/run_uie_pretrain.py"},{"title":"UIE/inference.py at main · universal-ie/UIE","url":"https://github.com/universal-ie/UIE/blob/main/inference.py"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"GitHub - UniversalDependencies/tools: Various utilities for processing the data. · GitHub","url":"https://github.com/UniversalDependencies/tools"},{"title":"entity-recognition-datasets/README.rst at master · juand-r/entity-recognition-datasets","url":"https://github.com/juand-r/entity-recognition-datasets/blob/master/README.rst"},{"title":"universal-ie - Overview","url":"https://github.com/universal-ie"}]

Based on the search results, I found relevant information about UIE (Universal Information Extraction) and related projects:

## UIE - Unified Structure Generation for Universal Information E
…[truncated 1540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-14T09:34:41.937228+00:00_

Web search results for query: "WNUT-17 NER dataset HuggingFace entity types test set size emerging entities"

Links: [{"title":"leondz/wnut_17 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/leondz/wnut_17"},{"title":"GitHub - leondz/emerging_entities_17: Dataset for the Emerging & Novel Entity NER task (WNUT '17) · GitHub","url":"https://github.com/leondz/emerging_entities_17"},{"title":"Loading and Preparing a Dataset for Fine-Tuning the Pre-Trained bert-base-NER Model in Hugging Face for Named Entity Recognition (NER) | by Yuan An, PhD | Medium","url":"https://medium.com/@anyuanay/working-with-hugging-face-lesson-2-2-e1e53bdf6507"},{"title":"tner/wnut2017 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/wnut2017"},{"title":"Add WNUT 17 NER dataset by stefan-it · Pull Request #150 · huggingface/datasets","url":"https://github.com/huggingface/datasets/pull/150"},{"title":"NER with HuggingFace","url":"https://www.kaggle.com/code/tirendazacademy/ner-with-huggingface"},{"title":"wnut_17.py · leondz/wnut_17 at main","url":"https://huggingface.co/datasets/leondz/wnut_17/blame/main/wnut_17.py"},{"title":"Emerging and Rare Entity Recognition","url":"http://noisy-text.github.io/2017/emerging-rare-entities.html"},{"title":"wnut_17.py · wnut_17 at main","url":"https://huggingface.co/datasets/wnut_17/blame/main/wnut_17.py"},{"title":"WNUT’17 Emerging and Rare Entities task | noisy-text","url":"http://noisy-text.github.io/2017/files/"}]

Based on the search results, here's what I found about the WNUT-17 NER dataset:

## Entity Types

The 6 named entities in the WNUT-17 dataset are: Corporation, Creative-Work, Group, Location, Person, and Product.

## Dataset Purpose

The task evaluates the ability to detect and classify novel, emerging, singleton named entities in noisy text.

## Dataset Size

The search results indicate that the dataset size is between 1K and 10K examples, though specific test set size is not explicitly stated in thes
…[truncated 596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-14T09:34:41.937386+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/eriktks/conll2003/discussions/13",
  "prompt": "What is the error when loading eriktks/conll2003? What is the workaround? Is there a working alternative?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/eriktks/conll2003/discussions/13",
    "prompt": "What is the error when loading eriktks/conll2003? What is the workaround? Is there a working alternative?"
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-14T09:34:41.937527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE data format NER \"Instance\" OR \"instruction\" OR \"text_input\" OR \"text_output\" JSON schema BeyonderXX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE data format NER \"Instance\" OR \"instruction\" OR \"text_input\" OR \"text_output\" JSON schema BeyonderXX"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-14T09:34:41.937672+00:00_

Web search results for query: "InstructUIE GitHub src/ie_instructions data converter NER CoNLL conll2003 site:github.com/BeyonderXX"

Links: [{"title":"GitHub - BeyonderXX/MINER: MINER: Mutual Information based Named Entity Recognition · GitHub","url":"https://github.com/beyonderxx/miner"}]

The search returned results for a MINER project by BeyonderXX, which is about Named Entity Recognition. However, this doesn't match the specific InstructUIE project you're looking for. Let me search with a more targeted query for InstructUIE specifically.

Links: [{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"InstructUIE/setup.sh at master · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/blob/master/setup.sh"},{"title":"InstructUIE/Dockerfile at master · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/blob/master/Dockerfile"},{"title":"InstructUIE/scripts/eval_flan-t5.sh at master · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/blob/master/scripts/eval_flan-t5.sh"},{"title":"Issues · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/issues"},{"title":"BeyonderXX (Xiao Wang) · GitHub","url":"https://github.com/BeyonderXX"},{"title":"datasets.BuilderConfig does not work. · Issue #6868 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/6868"},{"title":"GitHub - taishan1994/awesome-chinese-ner: 中文命名实体识别。包含目前最新的中文命名实体识别论文、中文实体识别相关工具、数据集，以及中文预训练模型、词向量、实体识别综述等。","url":"https://github.com/taishan1994/awesome-chinese-ner"},{"title":"GitHub - BeyonderXX/TRACE: TRACE: A Comprehensive Benchmark for Continual Learning in Large Language Models · GitHub","url":"https://github.com/BeyonderXX/TRACE"},{"title":"Beyonders · GitHub","url":"https://github.com/Beyonders"}]

Great! I found the InstructUIE repository. Now let me search more specificall
…[truncated 2862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-14T09:34:41.937824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generative IE NER CoNLL-2003 JSON conversion \"Universal NER\" OR \"UniNER\" OR \"UniversalNER\" format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generative IE NER CoNLL-2003 JSON conversion \"Universal NER\" OR \"UniNER\" OR \"UniversalNER\" format"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-14T09:34:41.937956+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACE05 NER dataset LDC license public alternative availability 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACE05 NER dataset LDC license public alternative availability 2025"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-14T09:34:41.938079+00:00_

# Error Loading eriktks/conll2003 Dataset

## The Error
```
RuntimeError: Dataset scripts are no longer supported, but found conll2003.py
```

This occurs when trying to load the dataset with:
```python
from datasets import load_dataset
raw_datasets = load_dataset("conll2003")
```

## Workarounds

### Option 1: Use the Parquet Revision (Recommended)
```python
from datasets import load_dataset
raw_datasets = load_dataset("eriktks/conll2003", revision="convert/parquet")
```

### Option 2: Enable Remote Code Execution
```python
import os
from datasets import load_dataset

raw_datasets = load_dataset(
    "conll2003", 
    trust_remote_code=True, 
    token=os.getenv("HUGGING_FACE_TOKEN")
)
```
Requires `datasets==3.6.0`

### Option 3: Downgrade Package Versions
```
datasets==2.16.0
huggingface-hub==0.20.0
transformers==4.36.0
```

## Alternative Solution

**Use a maintained alternative:** The dataset has been republished with all credits preserved at:
```python
raw_datasets = load_dataset("BramVanroy/conll2003")
```

This alternative avoids the script compatibility issues entirely and is recommended for new projects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-14T09:34:41.938234+00:00_

# CoNLL2003 Loading Issue Summary

**Current Problem:**
The error occurs because "Dataset scripts are no longer supported" in datasets library version 4.0.0 and later. The original `load_dataset("conll2003")` call fails since it relies on a builder script.

**Exact Error Message:**
```
RuntimeError: Dataset scripts are no longer supported, but found conll2003.py
```

**Recommended Workaround:**
Use an alternative dataset identifier: `load_dataset("lhoestq/conll2003")`

This alternative works because it doesn't depend on builder scripts. Users can also downgrade to datasets version 3.6.0 or earlier if needed, though using the alternative dataset ID is the preferred modern solution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-14T09:34:41.938369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github.com/hitz-zentroa/GoLLIE/tree/main/src/tasks conll2003 data_loader.py",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github.com/hitz-zentroa/GoLLIE/tree/main/src/tasks conll2003 data_loader.py",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-14T09:34:41.938500+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "github.com/BeyonderXX/InstructUIE tree master src ie_instructions NER data converter",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "github.com/BeyonderXX/InstructUIE tree master src ie_instructions NER data converter",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-14T09:34:41.938629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IEPile data format example entity text type JSON NER schema OneKE",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IEPile data format example entity text type JSON NER schema OneKE",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-14T09:34:41.938756+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BIO token tags to character offset span conversion NER Python conll2003 generative LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BIO token tags to character offset span conversion NER Python conll2003 generative LLM"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-14T09:34:41.938886+00:00_

Web search results for query: "generative IE NER CoNLL-2003 JSON conversion "Universal NER" OR "UniNER" OR "UniversalNER" format"

Links: [{"title":"Language-Independent Named Entity Recognition (II)","url":"https://www.clips.uantwerpen.be/conll2003/ner/"},{"title":"Universal NER","url":"https://universal-ner.github.io/"},{"title":"ConLL-2003 Dataset: Named Entity Recognition (NER) | Innovatiana","url":"https://www.innovatiana.com/en/datasets/conll-2003"},{"title":"Universal-NER/UniNER-7B-all · Hugging Face","url":"https://huggingface.co/Universal-NER/UniNER-7B-all"},{"title":"GitHub - universal-ner/universal-ner · GitHub","url":"https://github.com/universal-ner/universal-ner"},{"title":"Ner format to CONLL - usage - Prodigy Support","url":"https://support.prodi.gy/t/ner-format-to-conll/1153"},{"title":"Named Entity Recognition (NER) for CoNLL dataset with Tensorflow 2.2.0 | by Bhuvana Kundumani | Analytics Vidhya | Medium","url":"https://medium.com/analytics-vidhya/ner-tensorflow-2-2-0-9f10dcf5a0a"},{"title":"universal-ner - Overview","url":"https://github.com/universal-ner"},{"title":"universal-ner/README.md at main · mivanovitch/universal-ner","url":"https://github.com/mivanovitch/universal-ner/blob/main/README.md"},{"title":"universalner (Universal NER)","url":"https://huggingface.co/universalner"}]

I found search results related to your query. Here's what the search revealed:

## CoNLL-2003 Format

The CoNLL-2003 shared task data files contain four columns separated by a single space, with each word on a separate line and empty lines after each sentence. The columns include a word, a part-of-speech (POS) tag, a syntactic chunk tag, and a named entity tag.

## Universal NER / UniNER

The search results show information about the **UniversalNER** project, which is a generative approach to NER. The UniversalNER approach tunes a language model to generate a structured output in the form of a JSON list containing all entities of the query type in the passage. This 
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-14T09:34:41.939039+00:00_

Web search results for query: "ACE05 NER dataset LDC license public alternative availability 2025"

Links: [{"title":"ACE 2005 Multilingual Training Corpus - LDC Catalog","url":"https://catalog.ldc.upenn.edu/LDC2006T06"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"ACE 2005 Dataset","url":"https://paperswithcode.com/dataset/ace-2005"},{"title":"Dataset links for ACE05-EN+ and ERE-EN · Issue #13 · luyaojie/Text2Event","url":"https://github.com/luyaojie/Text2Event/issues/13"},{"title":"Obtaining Data - Linguistic Data Consortium (LDC)","url":"https://www.ldc.upenn.edu/language-resources/data/obtaining"},{"title":"Home | Linguistic Data Consortium","url":"https://www.ldc.upenn.edu/"},{"title":"ACE05 dataset · Issue #145 · dice-group/gerbil","url":"https://github.com/dice-group/gerbil/issues/145"},{"title":"Universal NER","url":"https://universal-ner.github.io/"},{"title":"Datasets for Generic Relation Extraction (reACE) - LDC Catalog","url":"https://catalog.ldc.upenn.edu/LDC2011T08"},{"title":"GitHub - ay94/NER-datasets · GitHub","url":"https://github.com/ay94/NER-datasets"}]

Based on the search results, here's what I found about the ACE05 NER dataset:

## ACE 2005 Dataset Overview

ACE 2005 Multilingual Training Corpus was developed by the Linguistic Data Consortium (LDC) and contains approximately 1,800 files of mixed genre text in English, Arabic, and Chinese annotated for entities, relations, and events. The genres include newswire, broadcast news, broadcast conversation, weblog, discussion forums, and conversational telephone speech.

## Licensing and Access

Most corpora distributed by LDC are available to nonmember organizations under research-only licenses and are subject to a nonmember license fee. 
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-14T09:34:41.939204+00:00_

Web search results for query: "github.com/hitz-zentroa/GoLLIE/tree/main/src/tasks conll2003 data_loader.py"

Links: [{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"GoLLIE/notebooks/Relation Extraction.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Relation%20Extraction.ipynb"},{"title":"Releases · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/releases"},{"title":"Issues · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/issues"},{"title":"HiTZ zentroa · GitHub","url":"https://github.com/hitz-zentroa"},{"title":"ptxas fatal : Ptx assembly aborted due to errors · Issue #5 · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/issues/5"},{"title":"GoLLIE/notebooks/Create Custom Task.ipynb at main · hitz-zentroa/GoLLIE","url":"https://github.com/hitz-zentroa/GoLLIE/blob/main/notebooks/Create%20Custom%20Task.ipynb"},{"title":"conll-2003 · GitHub Topics","url":"https://github.com/topics/conll-2003"},{"title":"GitHub - hitz-zentroa/This-is-not-a-Dataset: We introduce a large semi-automatically generated dataset of ~400,000 descriptive sentences about commonsense knowledge that can be true or false in which negation is present in about 2/3 of the corpus in different forms that we use to evaluate LLMs · GitHub","url":"https://github.com/hitz-zentroa/This-is-not-a-Dataset"},{"title":"conll2003 dataset loads original data. · Issue #4248 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/4248"}]

I found search results related to the GoLLIE repository. The search results show general information about the GoLLIE project, but they don't directly show the specific file path you're looking for (the data_loader.py file in the conll2003 task directory).

Based on the search results, you can use the already implemented task
…[truncated 715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-14T09:34:41.939360+00:00_

Web search results for query: "github.com/BeyonderXX/InstructUIE tree master src ie_instructions NER data converter"

Links: [{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning","url":"https://github.com/beyonderxx/instructuie"},{"title":"InstructUIE/scripts/eval_flan-t5.sh at master · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/blob/master/scripts/eval_flan-t5.sh"},{"title":"InstructUIE/setup.sh at master · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/blob/master/setup.sh"},{"title":"InstructUIE/Dockerfile at master · BeyonderXX/InstructUIE","url":"https://github.com/BeyonderXX/InstructUIE/blob/master/Dockerfile"},{"title":"CoreNLP/src/edu/stanford/nlp/ie/ner at main · stanfordnlp/CoreNLP","url":"https://github.com/stanfordnlp/CoreNLP/tree/main/src/edu/stanford/nlp/ie/ner"},{"title":"GitHub - pyvandenbussche/transformers-ner: Experiment on NER task using Huggingface state-of-the-art Transformers Natural Language Models library · GitHub","url":"https://github.com/pyvandenbussche/transformers-ner"},{"title":"CoreNLP/doc/ner at main · stanfordnlp/CoreNLP","url":"https://github.com/stanfordnlp/CoreNLP/tree/main/doc/ner"},{"title":"cogcomp-nlp/ner at master · CogComp/cogcomp-nlp","url":"https://github.com/CogComp/cogcomp-nlp/tree/master/ner"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"language-models/adapters/token-classification/token_classification_adapter.ipynb at master · piegu/language-models","url":"https://github.com/piegu/language-models/blob/master/adapters/token-classification/token_classification_adapter.ipynb"}]

Based on the search results, here's what I found:

The InstructUIE repository 
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-14T09:34:41.939511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MultiNERD dataset HuggingFace entity types size NER benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MultiNERD dataset HuggingFace entity types size NER benchmark"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-14T09:34:41.939670+00:00_

Web search results for query: "InstructUIE data format NER "Instance" OR "instruction" OR "text_input" OR "text_output" JSON schema BeyonderXX"

Links: [{"title":"Structured Output Generation in LLMs: JSON Schema and Grammar-Based Decoding | by Emre Karatas | Medium","url":"https://medium.com/@emrekaratas-ai/structured-output-generation-in-llms-json-schema-and-grammar-based-decoding-6a5c58b698a6"},{"title":"Structured model outputs | OpenAI API","url":"https://developers.openai.com/api/docs/guides/structured-outputs"},{"title":"Structured Outputs | xAI Docs","url":"https://docs.x.ai/developers/model-capabilities/text/structured-outputs"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"AI-assisted JSON Schema Creation and Mapping Deutsche Forschungsgemeinschaft (DFG) under project numbers 528693298 (preECO), 358283783 (SFB1333), and 390740016 (EXC2075)","url":"https://arxiv.org/html/2508.05192v2"},{"title":"Synthesizing JSON Schema Transformers","url":"https://arxiv.org/html/2405.17681v2"},{"title":"Introduction to Schema Based Prompting: Structured inputs for Predictable outputs","url":"https://opper.ai/blog/schema-based-prompting"},{"title":"Practical Techniques to constraint LLM output in JSON format | by Minyang Chen | Medium","url":"https://mychen76.medium.com/practical-techniques-to-constraint-llm-output-in-json-format-e3e72396c670"},{"title":"Taming LLM Outputs: Your Guide to Structured Text Generation","url":"https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation"},{"title":"How To Ensure LLM Output Adheres to a JSON Schema | Modelmetry","url":"https://modelmetry.com/blog/how-to-ensure-llm-output-adheres-to-a-json-schema"}]

I found a GitHub repository for InstructUIE by BeyonderXX in the search results. Let me search for more specific information about the InstructUIE data format details.

Links: [{"title":"GitHu
…[truncated 4604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-14T09:34:41.939825+00:00_

Web search results for query: "IEPile data format example entity text type JSON NER schema OneKE"

Links: [{"title":"DeepKE/example/llm/InstructKGC/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/InstructKGC/README.md"},{"title":"GitHub - zjunlp/IEPile: [ACL 2024] IEPile: A Large-Scale Information Extraction Corpus · GitHub","url":"https://github.com/zjunlp/IEPile"},{"title":"GitHub - OpenSPG/OneKE: OneKE is a knowledge extraction framework based on a large model, with preliminary generalized knowledge extraction capabilities in both Chinese and English and in multiple fields and tasks. · GitHub","url":"https://github.com/OpenSPG/OneKE"},{"title":"GitHub - zjunlp/DeepKE: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction · GitHub","url":"https://github.com/zjunlp/DeepKE"},{"title":"GitHub - zjunlp/OneKE: [WWW 2025] A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System. · GitHub","url":"https://github.com/zjunlp/OneKE"},{"title":"GitHub - SizableShrimp/EntityModelJson: A Forge mod that allows entity models to be defined in JSON · GitHub","url":"https://github.com/SizableShrimp/EntityModelJson"},{"title":"GitHub - tecoholic/ner-annotator: Named Entity Recognition (NER) Annotation tool for SpaCy. Generates Traning Data as a JSON which can be readily used. · GitHub","url":"https://github.com/tecoholic/ner-annotator"},{"title":"How to convert simple NER format to spacy json · Issue #1966 · explosion/spaCy","url":"https://github.com/explosion/spaCy/issues/1966"},{"title":"IEPile/data/hard_negative/hard_dict.json at main · zjunlp/IEPile","url":"https://github.com/zjunlp/IEPile/blob/main/data/hard_negative/hard_dict.json"},{"title":"GitHub - OpenDataServices/erd-from-json-table-schema: Create an ERD for a database given as JSON-table-schema · GitHub","url":"https://github.com/OpenDataServices/erd-from-json-table-schema"}]

Based on the search results, here's what I found about the IE
…[truncated 1533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-14T09:34:41.939983+00:00_

Web search results for query: "BIO token tags to character offset span conversion NER Python conll2003 generative LLM"

Links: [{"title":"A Converting data to BIO format for NER B Metrics","url":"https://openreview.net/attachment?id=5mi-CkvEqj&name=supplementary_material"},{"title":"Named entity recognition | NLP-progress","url":"http://nlpprogress.com/english/named_entity_recognition.html"},{"title":"GitHub - rahinic/BIO-to-BIOES-tagger: Changes the encoding of CoNLL-03 NER datasets from BIO to BIOES tagging scheme · GitHub","url":"https://github.com/rahinic/BIO-to-BIOES-tagger"},{"title":"BIO Tagging: Encoding Entity Boundaries for Sequence Labeling - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/bio-tagging-sequence-labeling-ner"},{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"},{"title":"Inside–outside–beginning (tagging) - Wikipedia","url":"https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)"},{"title":"GitHub - taasmoe/BIO-to-BIOLU: Changes the encoding of CoNLL-03 NER datasets from BIO to BIOLU","url":"https://github.com/taasmoe/BIO-to-BIOLU"},{"title":"Ner format to CONLL - usage - Prodigy Support","url":"https://support.prodi.gy/t/ner-format-to-conll/1153"},{"title":"Named Entity Recognition (NER) for CoNLL dataset with Tensorflow 2.2.0 | by Bhuvana Kundumani | Analytics Vidhya | Medium","url":"https://medium.com/analytics-vidhya/ner-tensorflow-2-2-0-9f10dcf5a0a"},{"title":"Data Conversion to Conll2003 - Intermediate - Hugging Face Forums","url":"https://discuss.huggingface.co/t/data-conversion-to-conll2003/56879"}]

Based on the search results, here's what I found about BIO token tags to character offset span conversion for NER with Python and CoNLL2003:

## BIO Tagging Overview

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type. Approaches typically use BIO n
…[truncated 1323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-14T09:34:41.940148+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2304.08085",
  "prompt": "Find the exact data format/schema used by InstructUIE for NER tasks. Look for JSON examples, input-output format specifications, how NER entities are represented in the output. Show any concrete examples of how CoNLL-2003 NER data is formatted in their system."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ar5iv.labs.arxiv.org/html/2304.08085",
    "prompt": "Find the exact data format/schema used by InstructUIE for NER tasks. Look for JSON examples, input-output format specifications, how NER entities are represented in the output. Show any concrete examples of how CoNLL-2003 NER data is formatted in their system."
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-14T09:34:41.940290+00:00_

Web search results for query: "MultiNERD dataset HuggingFace entity types size NER benchmark"

Links: [{"title":"tner/multinerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/multinerd"},{"title":"README.md · tner/multinerd at main","url":"https://huggingface.co/datasets/tner/multinerd/blob/main/README.md"},{"title":"dslim/bert-base-NER · Hugging Face","url":"https://huggingface.co/dslim/bert-base-NER"},{"title":"GitHub - Babelscape/multinerd: Repository for the paper \"MultiNERD: A Multilingual, Multi-Genre and Fine-Grained Dataset for Named Entity Recognition (and Disambiguation)\" (NAACL 2022).","url":"https://github.com/Babelscape/multinerd"},{"title":"Babelscape/multinerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Babelscape/multinerd"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"A Multilingual, Multi-Genre and Fine-Grained Dataset for ...","url":"https://aclanthology.org/2022.findings-naacl.60.pdf"},{"title":"universalner/universal_ner · Datasets at Hugging Face","url":"https://huggingface.co/datasets/universalner/universal_ner"},{"title":"NER with HuggingFace","url":"https://www.kaggle.com/code/tirendazacademy/ner-with-huggingface"},{"title":"rjac/kaggle-entity-annotated-corpus-ner-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/rjac/kaggle-entity-annotated-corpus-ner-dataset"}]

Based on the web search results, here's what I found about the MultiNERD dataset on HuggingFace:

## Dataset Overview

MultiNERD is an NER benchmark dataset formatted as part of the TNER project. MultiNERD is the first language-agnostic methodology for automatically creating multilingual, multi-genre and fine-grained annotations for Named Entity Re
…[truncated 891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-14T09:34:41.940442+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/universal-ner/universal-ner",
  "prompt": "What is the exact data format used by UniNER for NER? Show the conversation/JSON format, especially how entity types and entity spans are structured in the input/output. How is CoNLL-2003 data converted?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/universal-ner/universal-ner",
    "prompt": "What is the exact data format used by UniNER for NER? Show the conversation/JSON format, especially how entity types and entity spans are structured in the input/output. How is CoNLL-2003 data converted?"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-14T09:34:41.940578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/hitz-zentroa/GoLLIE/blob/main/src/tasks conll2003",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/hitz-zentroa/GoLLIE/blob/main/src/tasks conll2003",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-14T09:34:41.940707+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CrossNER dataset HuggingFace entity types cross-domain NER benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CrossNER dataset HuggingFace entity types cross-domain NER benchmark"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-14T09:34:41.940831+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/lhoestq/conll2003",
  "prompt": "Is this dataset available and working? What format does it use? What are the columns/features? What are the split sizes?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/lhoestq/conll2003",
    "prompt": "Is this dataset available and working? What format does it use? What are the columns/features? What are the split sizes?"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-14T09:34:41.941001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/BeyonderXX/InstructUIE/blob/master src converter NER dataset conll",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/BeyonderXX/InstructUIE/blob/master src converter NER dataset conll",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-14T09:34:41.941154+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/zjunlp/IEPile NER output format entity example JSON",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/zjunlp/IEPile NER output format entity example JSON",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-14T09:34:41.941291+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/BramVanroy/conll2003",
  "prompt": "Is this dataset available and working? What format does it use? What are the features/columns and split sizes?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/BramVanroy/conll2003",
    "prompt": "Is this dataset available and working? What format does it use? What are the features/columns and split sizes?"
  }
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-14T09:34:41.941420+00:00_

# InstructUIE NER Data Format

Based on the paper, InstructUIE uses a **text-to-text format** for NER tasks with the following structure:

## Input Components:
1. **Task Instruction**: Descriptive prompt like "Please list all entity words in the text that fit the category"
2. **Options**: Entity type labels (e.g., PERSON, ORGANIZATION, LOCATION)
3. **Text**: The input sentence to process

## Output Format:
For NER specifically, the output follows: **"entity tag: entity span"**

Example representation: `"PERSON: John; LOCATION: Paris"`

## Processing Details:
The paper notes they convert labels into natural language formats. For instance, they renamed labels like "people person place_of_birth" to **"place of birth"** to improve semantic understanding.

## Data Handling:
For datasets with fewer than 10,000 examples, all samples were included. Larger datasets were sampled to 10,000 examples for balance during supervised training.

**Note**: The paper does not provide explicit JSON schemas or concrete CoNLL-2003 examples showing the exact formatted input-output pairs. The format description remains at the conceptual level rather than with code samples.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-14T09:34:41.941546+00:00_

Web search results for query: "site:github.com/hitz-zentroa/GoLLIE/blob/main/src/tasks conll2003"

No links found.

The search didn't return any results. This could be because:

1. The specific file path or content you're looking for may not be publicly indexed by search engines
2. The repository structure or path may have changed
3. The page may require authentication or have special access restrictions

To find this information, I'd recommend:
- Visiting the GitHub repository directly at `https://github.com/hitz-zentroa/GoLLIE/tree/main/src/tasks`
- Browsing the repository structure to locate files related to CoNLL2003
- Checking the repository's documentation or README for information about the CoNLL2003 task implementation

Would you like me to help you search for information about the GoLLIE project or CoNLL2003 task in a different way?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-14T09:34:41.941666+00:00_

# UniNER Data Format Information

Based on the GitHub repository content provided, **specific details about UniNER's exact JSON/conversation format, entity type structuring, and entity span representation are not included in the available documentation**.

The repository mentions:

- **Available datasets**: "Only the CrossNER and MIT datasets are included in this repository" due to licensing restrictions
- **Model variants**: References to models like UniNER-7B-type and UniNER-7B-all trained on "ChatGPT-generated data and 40 supervised datasets"
- **Data location**: Links to "[Data](https://huggingface.co/Universal-NER)" and "[Model](https://huggingface.co/Universal-NER)" on Hugging Face

However, the README does not provide:
- JSON schema documentation
- Input/output format specifications
- CoNLL-2003 conversion procedures
- Entity span/type encoding methods

To access this information, you would need to:
1. Check the [project page](https://universal-ner.github.io/)
2. Review the [research paper](https://arxiv.org/abs/2308.03279)
3. Examine actual dataset files on Hugging Face
4. Inspect the source code in the `/src` directory of the repository

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-14T09:34:41.941787+00:00_

Web search results for query: "site:github.com/BeyonderXX/InstructUIE/blob/master src converter NER dataset conll"

No links found.

The search returned no results. This could be because:

1. The specific GitHub repository path or file structure may have changed
2. The exact combination of terms with the "site:" operator didn't match any indexed pages
3. The repository or file may not be publicly indexed by search engines

If you're looking for information about the InstructUIE project on GitHub, you might try:
- Visiting the GitHub repository directly at: github.com/BeyonderXX/InstructUIE
- Searching for a simpler query without the site operator
- Checking if there's a different branch or path structure than "blob/master"

Would you like me to try a different search approach?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-14T09:34:41.941911+00:00_

# CoNLL2003 Dataset Overview

## Availability & Status
Yes, the dataset is **available and working**. It's hosted on Hugging Face at `lhoestq/conll2003`.

## Format
- **Primary Format**: Parquet (auto-converted)
- **Libraries**: Compatible with Datasets and pandas
- **Additional Format**: Croissant metadata available

## Columns/Features

The dataset contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `id` | string | Unique identifier (1-5 characters) |
| `tokens` | sequence | List of word tokens |
| `pos_tags` | sequence | Part-of-speech tags (numeric) |
| `chunk_tags` | sequence | Chunking/shallow parsing tags (numeric) |
| `ner_tags` | sequence | Named Entity Recognition tags (numeric) |

**Example row:**
```
tokens: ["EU", "rejects", "German", "call", "to", "boycott", "British", "lamb", "."]
pos_tags: [22, 42, 16, 21, 35, 37, 16, 21, 7]
chunk_tags: [11, 21, 11, 12, 21, 22, 11, 12, 0]
ner_tags: [3, 0, 7, 0, 0, 0, 7, 0, 0]
```

## Split Sizes

| Split | Rows |
|-------|------|
| **train** | 14,041 |
| **validation** | 3,250 |
| **test** | 3,453 |
| **Total** | 20,744 |

## Dataset Size
- **Total file size**: 1.62 MB
- **Category**: 10K - 100K rows
- **Modality**: Text

This is a classic NER (Named Entity Recognition) benchmark dataset widely used for training token classification models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-14T09:34:41.942047+00:00_

Web search results for query: "site:github.com/zjunlp/IEPile NER output format entity example JSON"

Links: [{"title":"GitHub - zjunlp/IEPile: [ACL 2024] IEPile: A Large-Scale Information Extraction Corpus · GitHub","url":"https://github.com/zjunlp/IEPile"},{"title":"DeepKE/example/llm/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/README.md/"},{"title":"IEPile/ft_scripts/fine_continue.bash at main · zjunlp/IEPile","url":"https://github.com/zjunlp/IEPile/blob/main/ft_scripts/fine_continue.bash"},{"title":"GitHub - zjunlp/KnowLM: An Open-sourced Knowledgable Large Language Model Framework. · GitHub","url":"https://github.com/zjunlp/KnowLM"},{"title":"DeepKE/example/llm/README_CN.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/README_CN.md"},{"title":"GitHub - zjunlp/DeepKE: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction · GitHub","url":"https://github.com/zjunlp/DeepKE"},{"title":"DeepKE/example/llm/InstructKGC/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/example/llm/InstructKGC/README.md"},{"title":"DeepKE/README.md at main · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/blob/main/README.md"},{"title":"GitHub - zjunlp/OneKE: [WWW 2025] A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System. · GitHub","url":"https://github.com/zjunlp/OneKE"},{"title":"GitHub - tecoholic/ner-annotator: Named Entity Recognition (NER) Annotation tool for SpaCy. Generates Traning Data as a JSON which can be readily used. · GitHub","url":"https://github.com/tecoholic/ner-annotator"}]

Based on the search results, here's information about the NER output format for IEPile:

## NER Output Format in IEPile

The output is in the format of a dictionary's JSON string, where the key is the schema, and the value is the extracted content.

### Example

For a data instance from the NER task in the CoNLL2003 dataset 
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-14T09:34:41.942209+00:00_

# CoNLL2003 Dataset Status and Details

## Availability and Status
**Yes, this dataset is available and working.** It's hosted on Hugging Face at `BramVanroy/conll2003` and is actively maintained with a Dataset Viewer interface.

## Format
The dataset uses **Parquet format** (auto-converted from original format for easy access).

## Features/Columns
The dataset contains 5 columns:

1. **id** (string): Unique identifier for each sequence
2. **tokens** (list): List of word tokens
3. **pos_tags** (list): Part-of-speech tags (numeric IDs)
4. **chunk_tags** (list): Chunking/shallow parsing tags (numeric IDs)
5. **ner_tags** (list): Named Entity Recognition tags (numeric IDs)

### Example:
```python
{
  "id": "0",
  "tokens": ["EU", "rejects", "German", "call", "to", "boycott", "British", "lamb", "."],
  "pos_tags": [22, 42, 16, 21, 35, 37, 16, 21, 7],
  "chunk_tags": [11, 21, 11, 12, 21, 22, 11, 12, 0],
  "ner_tags": [3, 0, 7, 0, 0, 0, 7, 0, 0]
}
```

## Split Sizes
The dataset is divided into three splits:

| Split | Rows |
|-------|------|
| **train** | 14,000 |
| **validation** | 3,250 |
| **test** | 3,450 |
| **Total** | 20,700 |

## Primary Tasks
- Named Entity Recognition (NER)
- Part-of-Speech (POS) Tagging
- Chunking/Shallow Parsing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-14T09:34:41.942351+00:00_

Web search results for query: "CrossNER dataset HuggingFace entity types cross-domain NER benchmark"

Links: [{"title":"DFKI-SLT/cross_ner · Datasets at Hugging Face","url":"https://huggingface.co/datasets/DFKI-SLT/cross_ner"},{"title":"DFKI-SLT/cross_re · Datasets at Hugging Face","url":"https://huggingface.co/datasets/DFKI-SLT/cross_re"},{"title":"GitHub - zliucr/CrossNER: CrossNER: Evaluating Cross-Domain Named Entity Recognition (AAAI-2021) · GitHub","url":"https://github.com/zliucr/CrossNER"},{"title":"eesuhn/crossner-ai · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eesuhn/crossner-ai"},{"title":"[2012.04373] CrossNER: Evaluating Cross-Domain Named Entity Recognition","url":"https://arxiv.org/abs/2012.04373"},{"title":"README.md · DFKI-SLT/cross_ner at f3c058abf7fc79723797d978e70bd3e1ffc79966","url":"https://huggingface.co/datasets/DFKI-SLT/cross_ner/blob/f3c058abf7fc79723797d978e70bd3e1ffc79966/README.md"},{"title":"GitHub - asahi417/tner: Language model fine-tuning on NER with an easy interface and cross-domain evaluation. \"T-NER: An All-Round Python Library for Transformer-based Named Entity Recognition, EACL 2021\" · GitHub","url":"https://github.com/asahi417/tner"},{"title":"CrossNER: Evaluating Cross-Domain Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/363410317_CrossNER_Evaluating_Cross-Domain_Named_Entity_Recognition"},{"title":"CrossNER: Evaluating Cross-Domain Named Entity Recognition","url":"https://cdn.aaai.org/ojs/17587/17587-13-21081-1-2-20210518.pdf"},{"title":"Universal-NER/UniNER-7B-all · Hugging Face","url":"https://huggingface.co/Universal-NER/UniNER-7B-all"}]

Based on the search results, here's what I found about the CrossNER dataset:

## Overview

CrossNER is a fully-labeled collected of named entity recognition (NER) data spanning over five diverse domains (Politics, Natural Science, Music, Literature, and Artificial Intelligence) with specialized entity categories for differ
…[truncated 1288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-14T09:34:41.942501+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-14T09:34:41.942620+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-14T09:34:41.942746+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WikiANN wikiann NER dataset HuggingFace panx entity types size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WikiANN wikiann NER dataset HuggingFace panx entity types size"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-14T09:34:41.942872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE github conll2003 NER Python class format code annotation guidelines hitz-zentroa"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GoLLIE github conll2003 NER Python class format code annotation guidelines hitz-zentroa"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-14T09:34:41.943000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UniNER conversation format NER \"entity_type\" OR \"entity_text\" OR \"json\" input output template arxiv 2308.03279"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UniNER conversation format NER \"entity_type\" OR \"entity_text\" OR \"json\" input output template arxiv 2308.03279"
  }
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-14T09:34:41.943142+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/hitz-zentroa/GoLLIE/tree/main/src/tasks",
  "prompt": "List all task directories/folders available under src/tasks. I want to know which NER datasets are supported (conll2003, ontonotes, genia, few-nerd, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/hitz-zentroa/GoLLIE/tree/main/src/tasks",
    "prompt": "List all task directories/folders available under src/tasks. I want to know which NER datasets are supported (conll2003, ontonotes, genia, few-nerd, etc.)"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-14T09:34:41.943280+00:00_

Web search results for query: "WikiANN wikiann NER dataset HuggingFace panx entity types size"

Links: [{"title":"SEACrowd/wikiann · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SEACrowd/wikiann"},{"title":"unimelb-nlp/wikiann · Datasets at Hugging Face","url":"https://huggingface.co/datasets/unimelb-nlp/wikiann"},{"title":"WikiANN (or PAN-X) | Kaggle","url":"https://www.kaggle.com/datasets/shivanshuman/wikiann-or-panx"},{"title":"tner/wikiann · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/wikiann"},{"title":"wikiann.py · unimelb-nlp/wikiann at 246843e0e128eec87a0a7c2518427f00be03dbfa","url":"https://huggingface.co/datasets/unimelb-nlp/wikiann/blob/246843e0e128eec87a0a7c2518427f00be03dbfa/wikiann.py"},{"title":"wikiann | TensorFlow Datasets","url":"https://www.tensorflow.org/datasets/catalog/wikiann"},{"title":"Davlan/xlm-roberta-base-wikiann-ner · Hugging Face","url":"https://huggingface.co/Davlan/xlm-roberta-base-wikiann-ner"},{"title":"unimelb-nlp/wikiann at main","url":"https://huggingface.co/datasets/unimelb-nlp/wikiann/tree/main"},{"title":"README.md · tner/wikineural at main","url":"https://huggingface.co/datasets/tner/wikineural/blob/main/README.md"},{"title":"CoCalc -- wikiann.md","url":"https://cocalc.com/github/tensorflow/docs-l10n/blob/master/site/en-snapshot/datasets/community_catalog/huggingface/wikiann.md"}]

Based on the search results, here's the information about the WikiANN NER dataset:

## Overview
WikiANN (sometimes called PAN-X) is a multilingual named entity recognition dataset consisting of Wikipedia articles annotated with LOC (location), PER (person), and ORG (organisation) tags in the IOB2 format.

## Entity Types
The dataset includes the following entity labels: O (0), B-PER (1), I-PER (2), B-ORG (3), I-ORG (4), B-LOC (5), I-LOC (6). This represents three main entity types: **PER** (person), **ORG** (organization), and **LOC** (location).

## Language Coverage
The dataset contains 176 languages
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-14T09:34:41.943435+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/src",
  "prompt": "List the directory structure. I want to find where NER dataset conversion/processing code lives, especially for CoNLL-2003, OntoNotes, GENIA, Few-NERD datasets. Show all directories and key files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/src",
    "prompt": "List the directory structure. I want to find where NER dataset conversion/processing code lives, especially for CoNLL-2003, OntoNotes, GENIA, Few-NERD datasets. Show all directories and key files."
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-14T09:34:41.943567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MIT Movie Restaurant NER dataset availability entity types size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MIT Movie Restaurant NER dataset availability entity types size"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-14T09:34:41.943685+00:00_

# NER Datasets Supported in GoLLIE

Based on the GitHub repository structure, the following task directories are available under `src/tasks`:

**Named Entity Recognition (NER) Datasets:**
- ace
- bc5cdr
- broadtwitter
- casie
- conll03
- crossner
- diann
- e3c
- fabner
- harveyner
- mitmovie
- mitrestaurant
- multiconer2
- multinerd
- ncbidisease
- ontonotes
- rams
- tacred
- wikievents
- wnut

The repository contains 20 distinct task directories. Notable datasets include **conll03** and **ontonotes**, which you mentioned. However, the page listing does not explicitly indicate support for GENIA or Few-NERD datasets—only the directories shown above are present in the `src/tasks` folder structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-14T09:34:41.943819+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/zjunlp/IEPile/blob/main/README.md",
  "prompt": "Find the exact output format for NER tasks. I need to know: does IEPile use character offsets (start/end) or just entity text strings? Show the exact JSON format of the NER output. Also list which NER datasets are included (CoNLL-2003, OntoNotes, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/zjunlp/IEPile/blob/main/README.md",
    "prompt": "Find the exact output format for NER tasks. I need to know: does IEPile use character offsets (start/end) or just entity text strings? Show the exact JSON format of the NER output. Also list which NER datasets are included (CoNLL-2003, OntoNotes, etc.)."
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-14T09:34:41.943953+00:00_

Web search results for query: "UniNER conversation format NER "entity_type" OR "entity_text" OR "json" input output template arxiv 2308.03279"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2308.03279"},{"title":"UniversalNER: targeted distillation from large language models for open named entity recognition","url":"https://arxiv.org/html/2308.03279"},{"title":"[2308.03279] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279"},{"title":"Universal-NER/UniNER-7B-all · Hugging Face","url":"https://huggingface.co/Universal-NER/UniNER-7B-all"},{"title":"Universal-NER/UniNER-7B-type · Hugging Face","url":"https://huggingface.co/Universal-NER/UniNER-7B-type"},{"title":"universal-ner/README.md at main · mivanovitch/universal-ner","url":"https://github.com/mivanovitch/universal-ner/blob/main/README.md"},{"title":"Universal NER","url":"https://universal-ner.github.io/"},{"title":"universal-ner/README.md at main · universal-ner/universal-ner","url":"https://github.com/universal-ner/universal-ner/blob/main/README.md"},{"title":"A Reasoning Paradigm for Named Entity Recognition","url":"https://arxiv.org/html/2511.11978v1"},{"title":"Show Less, Instruct More: Enriching Prompts with Definitions and Guidelines for Zero-Shot NER","url":"https://arxiv.org/html/2407.01272v3"}]

Based on the search results for arxiv paper 2308.03279 (UniNER), here's information about the UniNER conversation format for NER:

## UniNER Conversation Template

The prompting template follows a conversation format: "A virtual assistant answers questions from a user based on the provided text. USER: Text: {Fill the input text here} ASSISTANT: I've read this text. USER: What describes {Fill the entity type here} in the text? ASSISTANT: (model's predictions in JSON format)"

## Data Collection Format

For the training data generation from ChatGPT, the instruction used was: "Given 
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-14T09:34:41.944095+00:00_

# InstructUIE src/ Directory Structure

Based on the GitHub page content provided, the visible directory structure includes:

**Directories:**
- `evaluation/`
- `model/`
- `rouge/`

**Key Files:**
- `__init__.py`
- `calculate_f1.py`
- `compute_metrics.py`
- `convert_data_to_uie.py`
- `create_exps.py`
- `run_gpt3.py`
- `run_uie.py`
- `task_conf_gen.py`
- `uie_collator.py`
- `uie_dataset.py`
- `uie_trainer.py`

## NER Dataset Processing Location

The file `"convert_data_to_uie.py"` appears most relevant for dataset conversion tasks. However, the current page only shows the directory listing without file contents.

To locate CoNLL-2003, OntoNotes, GENIA, and Few-NERD dataset processing code, you would need to examine the contents of `convert_data_to_uie.py` and potentially explore the subdirectories (`evaluation/`, `model/`, `rouge/`) for additional dataset-handling modules.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-14T09:34:41.944249+00:00_

Web search results for query: "MIT Movie Restaurant NER dataset availability entity types size"

Links: [{"title":"tner/mit_restaurant · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/mit_restaurant"},{"title":"MIT Restaurant Review - CRF (NER) Model","url":"https://www.kaggle.com/code/marusagar/mit-restaurant-review-crf-ner-model"},{"title":"Template-Based Named Entity Recognition Using BART","url":"https://arxiv.org/pdf/2106.01760"},{"title":"MITRestaurant | Kaggle","url":"https://www.kaggle.com/datasets/artgor/mitrestaurant"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"Universal NER","url":"https://universal-ner.github.io/"},{"title":"tner/mit_movie_trivia · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/mit_movie_trivia"},{"title":"rungalileo/mit_movies_fixed_connll_format · Datasets at Hugging Face","url":"https://huggingface.co/datasets/rungalileo/mit_movies_fixed_connll_format"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/html/2412.10121v2"},{"title":"niruthiha/roberta-large-mit-restaurant-ner · Hugging Face","url":"https://huggingface.co/niruthiha/roberta-large-mit-restaurant-ner"}]

Based on the search results, here's what I found about the MIT Movie Restaurant NER dataset:

## MIT Restaurant Dataset

The MIT Restaurant NER dataset is formatted as part of the TNER project. 

**Entity Types:** The dataset includes 8 entity types: Rating, Amenity, Location, Restaurant_Name, Price, Hours, Dish, and Cuisine.

**Availability:** The dataset is available at https://groups.csail.mit.edu/sls/downloads/restaurant/, and it's also accessible through
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-14T09:34:41.944394+00:00_

# IEPile NER Output Format

## Output Format
IEPile uses **entity text strings only**, not character offsets. The NER output is a JSON object where keys are entity types and values are lists of extracted entity strings:

```json
{
  "person": ["Robert Allenby", "Allenby", "Miguel Angel Martin"],
  "organization": [],
  "else": [],
  "location": ["Australia", "Spain"]
}
```

As documented: "the output is `{"person": ["Robert Allenby", "Allenby", "Miguel Angel Martin"], "organization": [], "else": [], "location": ["Australia", "Spain"]}`"

## Included NER Datasets
The documentation lists these NER datasets:

- CoNLL2003
- AnatEM
- BC2GM
- BC4CHEMD
- NCBI-Disease
- BC5CDR
- HarveyNER
- GENIA
- ACE2005
- MIT Restaurant
- MIT Movie
- FabNER
- MultiNERD
- OntoNotes
- CrossNER
- MSRA NER
- Resume NER
- CLUE NER
- Weibo NER
- Boson

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-14T09:34:41.944547+00:00_

Web search results for query: "GoLLIE github conll2003 NER Python class format code annotation guidelines hitz-zentroa"

Links: [{"title":"conll-2003 · GitHub Topics","url":"https://github.com/topics/conll-2003"},{"title":"GitHub - senadkurtisi/pytorch-NER: Named Entity Recognition in PyTorch on CoNLL2003 dataset · GitHub","url":"https://github.com/senadkurtisi/pytorch-NER"},{"title":"GitHub - google/NeuroNER-CSPMC","url":"https://github.com/google/NeuroNER-CSPMC"},{"title":"GitHub - Franck-Dernoncourt/NeuroNER: Named-entity recognition using neural networks. Easy-to-use and state-of-the-art results. · GitHub","url":"https://github.com/Franck-Dernoncourt/NeuroNER"},{"title":"NER/corpus/CoNLL-2003 at master · synalp/NER","url":"https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003"},{"title":"GitHub - kyzhouhzau/BERT-NER: Use Google's BERT for named entity recognition （CoNLL-2003 as the dataset）.","url":"https://github.com/kyzhouhzau/BERT-NER"},{"title":"Language-Independent Named Entity Recognition (II)","url":"https://www.clips.uantwerpen.be/conll2003/ner/"},{"title":"flair-experiments/conll2003-ner-english/README.md at master · stefan-it/flair-experiments","url":"https://github.com/stefan-it/flair-experiments/blob/master/conll2003-ner-english/README.md"},{"title":"conll · GitHub Topics","url":"https://github.com/topics/conll?l=python&o=asc&s=updated"},{"title":"GitHub - MaviccPRP/ger_ner_evals","url":"https://github.com/MaviccPRP/ger_ner_evals"}]

The search results show general information about CoNLL2003 NER datasets and various tools, but don't specifically mention GoLLIE. Let me search more specifically for GoLLIE.

Links: [{"title":"GitHub - hitz-zentroa/GoLLIE: Guideline following Large Language Model for Information Extraction · GitHub","url":"https://github.com/hitz-zentroa/GoLLIE"},{"title":"GoLLIE | Guideline following Large Language Model for Information Extraction","url":"https://hitz-zentroa.github.io/GoLLIE/"},{"title":"GoLLIE/notebooks/Relatio
…[truncated 5785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-14T09:34:41.944696+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tner/ontonotes5",
  "prompt": "Extract: entity types/labels, dataset splits sizes (train/validation/test number of examples), license information, and any notes about data source or LDC requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tner/ontonotes5",
    "prompt": "Extract: entity types/labels, dataset splits sizes (train/validation/test number of examples), license information, and any notes about data source or LDC requirements."
  }
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-14T09:34:41.944841+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/BeyonderXX/InstructUIE/master/src/convert_data_to_uie.py",
  "prompt": "Show the full code. I want to see how it converts NER datasets (especially CoNLL-2003) to the UIE format. What is the target JSON format? Does it use character offsets (start/end) or just entity text? Show the key conversion functions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/BeyonderXX/InstructUIE/master/src/convert_data_to_uie.py",
    "prompt": "Show the full code. I want to see how it converts NER datasets (especially CoNLL-2003) to the UIE format. What is the target JSON format? Does it use character offsets (start/end) or just entity text? Show the key conversion functions."
  }
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-14T09:34:41.945070+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/hitz-zentroa/GoLLIE/main/src/tasks/conll03/data_loader.py",
  "prompt": "Show the full code. I want to see how it loads CoNLL-2003 data and converts BIO tags to entity spans. What format does it produce? Does it use character offsets? Show the key functions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/hitz-zentroa/GoLLIE/main/src/tasks/conll03/data_loader.py",
    "prompt": "Show the full code. I want to see how it loads CoNLL-2003 data and converts BIO tags to entity spans. What format does it produce? Does it use character offsets? Show the key functions."
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-14T09:34:41.945275+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/universal-ie/UIE/blob/main/docs/DATASETS.md",
  "prompt": "Show which datasets are supported and the data format used. Does UIE use character offsets for entities? What is the JSON format for NER data? List all supported NER datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/universal-ie/UIE/blob/main/docs/DATASETS.md",
    "prompt": "Show which datasets are supported and the data format used. Does UIE use character offsets for entities? What is the JSON format for NER data? List all supported NER datasets."
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-14T09:34:41.945422+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.researchgate.net/figure/GoLLIE-prompt-for-CoNLL03-which-includes-labels-such-as-PER-ORG-LOC-and-MISC_fig1_394081434",
  "prompt": "Show the exact GoLLIE prompt format for CoNLL-2003 NER. What Python classes are defined? What does the input/output look like?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.researchgate.net/figure/GoLLIE-prompt-for-CoNLL03-which-includes-labels-such-as-PER-ORG-LOC-and-MISC_fig1_394081434",
    "prompt": "Show the exact GoLLIE prompt format for CoNLL-2003 NER. What Python classes are defined? What does the input/output look like?"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-14T09:34:41.945553+00:00_

# Analysis of UIE Dataset Conversion Script

Based on the provided code snippet, I can only offer a **partial answer** since the full conversion implementation isn't shown.

## What's Visible

The script processes datasets through a `DataCollatorForUIE` class that:
- Takes raw examples and converts them into input/output pairs
- Produces two outputs per split:
  - **TSV files**: tab-separated with "inputs" and "labels"
  - **JSONL files**: enriched examples with added fields

## Missing Information

The code doesn't reveal:

1. **Target JSON format** - The actual NER-to-UIE schema isn't defined in this snippet
2. **Offset handling** - Whether character positions or just entity text is used remains unclear
3. **Key conversion functions** - The actual transformation logic lives in:
   - `uie_collator.py` (the `DataCollatorForUIE` class)
   - `uie_dataset.py` (the dataset loader)

## Observable Pattern

The script calls `"data_collator([example])"` which returns encoded examples with `["inputs"]` and `["labels"]` keys, then normalizes whitespace before writing to TSV format.

**To see the full conversion logic, you'd need to examine the referenced `uie_collator.py` and `uie_dataset.py` files**, as they contain the actual CoNLL-2003 → UIE transformation implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-14T09:34:41.945685+00:00_

Request failed with status code 403

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-14T09:34:41.945812+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2308.03279",
  "prompt": "Find the exact conversation template format used by UniNER. Show the input-output format including JSON structure for entity extraction. How are entity types and spans formatted?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2308.03279",
    "prompt": "Find the exact conversation template format used by UniNER. Show the input-output format including JSON structure for entity extraction. How are entity types and spans formatted?"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-14T09:34:41.945936+00:00_

# CoNLL-2003 Data Loading and BIO Tag Processing

## Key Loading Functions

The code provides two main loading paths:

1. **`get_conll_hf()`** - Loads from Hugging Face's `conll2003` dataset
2. **`load_conll_tsv()`** - Loads from local TSV files in CoNLL format

## BIO to Entity Span Conversion

Both functions convert BIO tags to entity spans using this logic:

```python
spans = []
for i, label in enumerate(labels):
    if label == "O":
        continue
    elif label.startswith("B-"):
        spans.append([label[2:], i, i + 1])
    elif label.startswith("I-"):
        spans[-1][2] += 1
```

The process:
- **B- tags** initiate new spans with `[entity_type, start_index, end_index]`
- **I- tags** extend the previous span's end index
- **O tags** are skipped

## Output Format

The spans are **token-based indices, not character offsets**. Each span stores:
- Entity type (e.g., "PER", "ORG", "LOC")
- Start token index
- End token index (exclusive)

Entity objects are created by joining tokens: `"span=" ".join(words[start:end])`

## Final Data Structure

The `CoNLLDatasetLoader` produces dictionaries with:
- `"text"` - space-joined tokens
- `"entities"` - list of Entity objects with text spans
- `"gold"` - reference annotations

This represents a **text-based, token-indexed format** rather than character-level offsets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-14T09:34:41.946077+00:00_

# OntoNotes 5 Dataset - Key Information

## Entity Types/Labels

The dataset includes **18 entity types**:
- `CARDINAL`, `DATE`, `PERSON`, `NORP`, `GPE`, `LAW`, `PERCENT`, `ORDINAL`, `MONEY`, `WORK_OF_ART`, `FAC`, `TIME`, `QUANTITY`, `PRODUCT`, `LANGUAGE`, `ORG`, `LOC`, `EVENT`

Each entity uses BIO (Begin-Inside-Outside) tagging scheme. Complete label2id mapping:

```json
{
    "O": 0,
    "B-CARDINAL": 1, "I-CARDINAL": 22,
    "B-DATE": 2, "I-DATE": 3,
    "B-PERSON": 4, "I-PERSON": 5,
    "B-NORP": 6, "I-NORP": 26,
    "B-GPE": 7, "I-GPE": 8,
    "B-LAW": 9, "I-LAW": 10,
    "B-ORG": 11, "I-ORG": 12,
    "B-PERCENT": 13, "I-PERCENT": 14,
    "B-ORDINAL": 15, "I-ORDINAL": 35,
    "B-MONEY": 16, "I-MONEY": 17,
    "B-WORK_OF_ART": 18, "I-WORK_OF_ART": 19,
    "B-FAC": 20, "I-FAC": 32,
    "B-TIME": 21, "I-TIME": 29,
    "B-QUANTITY": 24, "I-QUANTITY": 25,
    "B-LOC": 23, "I-LOC": 27,
    "B-PRODUCT": 28, "I-PRODUCT": 34,
    "B-EVENT": 30, "I-EVENT": 31,
    "B-LANGUAGE": 33, "I-LANGUAGE": 36
}
```

## Dataset Splits

| Split | Size |
|-------|------|
| **Train** | 59,924 examples |
| **Validation** | 8,528 examples |
| **Test** | 8,262 examples |
| **Total** | 76,714 examples |

## License

**License Type:** `other` (non-standard license)

## Data Source & Notes

- **Source:** OntoNotes 5 dataset formatted as part of the [TNER](https://github.com/asahi417/tner) project
- **Domain:** News articles
- **Task:** Named Entity Recognition (Token Classification)
- **Format:** Tokens and BIO-tagged labels
- **Total File Size:** 17.5 MB

## Citation

```bibtex
@inproceedings{hovy-etal-2006-ontonotes,
    title = "{O}nto{N}otes: The 90{\%} Solution",
    author = "Hovy, Eduard and Marcus, Mitchell and Palmer, Martha and Ramshaw, Lance and Weischedel, Ralph",
    booktitle = "Proceedings of the Human Language Technology Conference of the {NAACL}, Companion Volume: Short Papers",
    month = jun,
    year = "2006",
    address = "New York City, USA",
    publisher = "Associa
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-14T09:34:41.946242+00:00_

# UIE Dataset Format Analysis

## Character Offsets for Entities

Yes, UIE uses character offsets. The data format includes an `"offset"` field within entity objects, as shown in the example: `{"type": "geographical social political", "offset": [0], "text": "MULTAN"}`.

## JSON Format for NER Data

The NER structure includes:
- **text**: Raw input text
- **tokens**: Tokenized version for evaluation
- **entity**: Array with type, offset, and text fields
- **spot**: Positive entity types for single-task fine-tuning

Example entity structure: `"offset": [2], "text": "Pakistan"` indicates position within the tokenized sequence.

## Supported NER Datasets

The provided documentation does not list specific supported NER datasets. It only demonstrates the unified data format with "a structured extraction language instance" but doesn't enumerate which particular NER datasets are compatible with UIE.

The document emphasizes the **unified format** rather than cataloging individual datasets, focusing on how entities, relations, and events are represented consistently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-14T09:34:41.946374+00:00_

# UniNER Conversation Template Format

## Core Template Structure

UniNER uses a **conversation-style instruction tuning template** where the model engages in a multi-turn dialogue:

**Input Format:**
```
User: Text: [passage]
Assistant: I've read this text.
User: What describes [entity_type] in the text?
Assistant: [entity_list]
```

## Entity Output Format

Entities are returned as **JSON lists**. According to the paper: "the model is tuned to generate a structured output in the form of a JSON list containing all entities" of the queried type.

**Example Output Structure:**
```json
["entity1", "entity2", "entity3"]
```

## Key Characteristics

- **Per-type queries**: Each entity type receives a separate natural language question
- **Structured responses**: Answers use JSON array format listing matched entities
- **Loss computation**: Only the assistant's response tokens contribute to training loss
- **Entity representation**: Entities are listed as strings within JSON arrays, with exact span matching required for evaluation

The approach prioritizes **semantic diversity** through varied input passages rather than instruction variations, treating each entity type query as a focused subtask.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-14T09:34:41.946508+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/DFKI-SLT/few-nerd",
  "prompt": "Extract: entity types (coarse and fine-grained), dataset splits sizes (train/validation/test number of examples), license, and evaluation setup (supervised vs few-shot)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/DFKI-SLT/few-nerd",
    "prompt": "Extract: entity types (coarse and fine-grained), dataset splits sizes (train/validation/test number of examples), license, and evaluation setup (supervised vs few-shot)."
  }
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-14T09:34:41.946639+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/hitz-zentroa/GoLLIE/main/src/tasks/conll03/data_loader.py",
  "prompt": "Show the COMPLETE code file, every line. I need to see all imports, all functions, and especially how entities are constructed and what the final output format looks like."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/hitz-zentroa/GoLLIE/main/src/tasks/conll03/data_loader.py",
    "prompt": "Show the COMPLETE code file, every line. I need to see all imports, all functions, and especially how entities are constructed and what the final output format looks like."
  }
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-14T09:34:41.946768+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/BeyonderXX/InstructUIE/master/src/uie_collator.py",
  "prompt": "Show the COMPLETE code. I need to see the DataCollatorForUIE class and how NER entities are formatted. Does it produce character offsets or just entity text strings? Show the exact output format for NER tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/BeyonderXX/InstructUIE/master/src/uie_collator.py",
    "prompt": "Show the COMPLETE code. I need to see the DataCollatorForUIE class and how NER entities are formatted. Does it produce character offsets or just entity text strings? Show the exact output format for NER tasks."
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-14T09:34:41.946894+00:00_

# Code Analysis: CoNLL03 Dataset Loader

## Overview
This Python module implements dataset loading and sampling for the CoNLL03 Named Entity Recognition task. It provides two main entry points: `CoNLLDatasetLoader` and `CoNLL03Sampler`.

## Key Components

**Data Loading Functions:**

1. `get_conll_hf()` - Retrieves data from Hugging Face's datasets library, supporting train/validation/test splits. It converts IOB1 labels to IOB2 format and extracts entity spans.

2. `read_tsv()` - Parses CoNLL-formatted TSV files, handling sentence boundaries marked by "-DOCSTART-" or blank lines.

3. `load_conll_tsv()` - Wraps `read_tsv()` to produce structured entity objects.

## Entity Construction

Entities are instantiated using an `ENTITY_TO_CLASS_MAPPING` dictionary that maps label strings to entity classes:
- "LOC" → Location
- "ORG" → Organization  
- "PER" → Person
- "MISC" → Miscellaneous (optional)

Each entity is created with a `span` parameter containing the concatenated word text: `ENTITY_TO_CLASS_MAPPING[label](span=" ".join(words[start:end]))`

## Output Format

The final structure stored in `CoNLLDatasetLoader.elements` is:
```
{id: {"id": int, "doc_id": int, "text": str, "entities": List[Entity], "gold": List[Entity]}}
```

Where entities are typed objects from the prompts module and the text represents the complete sentence with space-joined words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-14T09:34:41.947034+00:00_

# DataCollatorForUIE Analysis

Based on the provided code, I cannot definitively determine the NER output format because **the code shown is incomplete**.

## What the Code Does

The `DataCollatorForUIE` class processes batch data for two model types:

1. **Seq2seq models** (T5, FLAN-T5): Tokenizes sources and labels separately
2. **Decoder models** (CodeGen, BLOOMZ, GPT-NeoX): Concatenates input and label for training

## Critical Limitation

The code displays "instructions \n options \n {0} \n Answer:" as a comment but **doesn't show**:
- How entity labels are structured
- Whether offsets are included
- The actual label formatting mechanism

The `get_instruction()` method formats text using `instruction.format(content)`, but the actual label structure—whether it's plain text, character offsets, or entity boundaries—**is not visible in this excerpt**.

## Recommendation

To determine NER output format, you would need:
- The actual instance data structure (the 'label' field content)
- Task configuration files
- Example training data
- The complete pipeline that creates these instances

The provided code handles tokenization and batching but obscures the underlying entity representation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-14T09:34:41.947187+00:00_

# Few-NERD Dataset Overview

## Entity Types

### Coarse-grained Types (8)
1. `art` (1)
2. `building` (2)
3. `event` (3)
4. `location` (4)
5. `organization` (5)
6. `other` (6)
7. `person` (7)
8. `product` (8)

### Fine-grained Types (66)
The dataset includes 66 fine-grained entity types, such as:
- `art-broadcastprogram` (1)
- `art-film` (2)
- And 64 others (mapped to numeric IDs 0-65)

Examples from the data show fine-grained tags like:
- 29 (person-related)
- 37 (organization/team-related)
- 51 (person-artist)
- 21 (location-region)

## Dataset Splits

| Task | Train | Validation | Test | Total |
|------|-------|-----------|------|-------|
| **SUP (Supervised)** | 131,767 | 18,824 | 37,648 | 188,239 |
| **INTRA (Few-shot)** | 99,519 | 19,358 | 44,059 | 162,936 |
| **INTER (Few-shot)** | 130,112 | 18,817 | 14,007 | 162,936 |

**Total dataset:** 188,200 sentences, 491,711 entities, 4,601,223 tokens

## License

**CC BY-SA 4.0** - Creative Commons Attribution-ShareAlike 4.0 International

## Evaluation Setup

### Three Benchmark Tasks

1. **Few-NERD (SUP)** - Supervised Learning
   - Standard NER task with full training data
   - Used for evaluating supervised NER models

2. **Few-NERD (INTRA)** - Few-shot Learning (Intra-domain)
   - Few-shot NER with entity types from the same domain
   - Tests generalization within domain

3. **Few-NERD (INTER)** - Few-shot Learning (Inter-domain)
   - Few-shot NER with entity types from different domains
   - Tests cross-domain generalization and transfer learning

### Tagging Scheme
- **IO format** (Inside-Outside): No BIO or BIOES, just `O` (0) for non-entities and entity type labels for entities

### Data Format
```python
{
    'id': '1',
    'tokens': ['It', 'starred', 'Hicks', "'s", ...],
    'ner_tags': [0, 0, 7, 0, ...],           # coarse-grained tags
    'fine_ner_tags': [0, 0, 51, 0, ...]     # fine-grained tags
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-14T09:34:41.947340+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/IE_INSTRUCTIONS",
  "prompt": "List all directories and files. I want to see which NER datasets are included in the IE_INSTRUCTIONS directory and how the data is organized."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/IE_INSTRUCTIONS",
    "prompt": "List all directories and files. I want to see which NER datasets are included in the IE_INSTRUCTIONS directory and how the data is organized."
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-14T09:34:41.947460+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-14T09:34:41.947581+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/leondz/wnut_17",
  "prompt": "Extract: entity types, dataset splits sizes (train/validation/test number of examples), license information, data source/domain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/leondz/wnut_17",
    "prompt": "Extract: entity types, dataset splits sizes (train/validation/test number of examples), license information, data source/domain."
  }
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-14T09:34:41.947708+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/hitz-zentroa/GoLLIE/main/src/tasks/conll03/prompts.py",
  "prompt": "Show the COMPLETE code. I want to see the entity class definitions (Person, Location, Organization, Miscellaneous) and their structure. How are entities represented - with character offsets or just text spans?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/hitz-zentroa/GoLLIE/main/src/tasks/conll03/prompts.py",
    "prompt": "Show the COMPLETE code. I want to see the entity class definitions (Person, Location, Organization, Miscellaneous) and their structure. How are entities represented - with character offsets or just text spans?"
  }
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-14T09:34:41.947837+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/wenge-research/YAYI-UIE/tree/main/data",
  "prompt": "List all directories and files. I want to see which NER datasets are included and how the data is organized. What format is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/wenge-research/YAYI-UIE/tree/main/data",
    "prompt": "List all directories and files. I want to see which NER datasets are included and how the data is organized. What format is used?"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-14T09:34:41.947951+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-14T09:34:41.948064+00:00_

# Entity Structure Analysis

Based on the provided code, here's how entities are represented:

## Entity Classes

The code defines four entity types using Python dataclasses:

1. **Person** - Represents individual names
2. **Organization** - Represents company/institutional names
3. **Location** - Represents geographic locations
4. **Miscellaneous** - Represents other named entities

## Data Representation

Each entity class follows this structure:

```python
@dataclass
class [EntityType](Entity):
    span: str
```

**Key finding**: Entities are represented using **text spans only**, not character offsets. The `span` attribute stores the actual text string of the entity.

## Entity Collections

The code provides two predefined lists:
- `ENTITY_DEFINITIONS` - All four entity types
- `ENTITY_DEFINITIONS_woMISC` - Excludes Miscellaneous entities

## Standards Compliance

These definitions derive from the "ConLL2003 guidelines" and follow the 1999 Named Entity Task Definition specifications established by MITRE and SAIC, ensuring compatibility with standard NER evaluation frameworks.

The minimal structure (single `span` field) suggests this is a lightweight representation suitable for annotation or basic NER tasks, with positional information likely handled elsewhere in the system.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-14T09:34:41.948213+00:00_

# WNUT-17 Dataset Summary

## Entity Types
The dataset uses IOB2 format with the following entity types:
- **Corporation** (B-corporation, I-corporation)
- **Creative Work** (B-creative-work, I-creative-work)
- **Group** (B-group, I-group)
- **Location** (B-location, I-location)
- **Person** (B-person, I-person)
- **Product** (B-product, I-product)
- **O** (Outside/no entity)

## Dataset Split Sizes
| Split | Number of Examples |
|-------|-------------------|
| Train | 3,394 |
| Validation | 1,009 |
| Test | 1,287 |

## License Information
**cc-by-4.0** (Creative Commons Attribution 4.0 International)

## Data Source/Domain
**Domain:** Noisy, user-generated text (primarily Twitter/tweets)

The dataset focuses on **emerging and rare entity recognition** in the context of novel, previously-unseen entities in noisy text. Examples include informal social media discussions where entities have unusual surface forms.

### Citation
```bibtex
@inproceedings{derczynski-etal-2017-results,
    title = "Results of the {WNUT}2017 Shared Task on Novel and Emerging Entity Recognition",
    author = "Derczynski, Leon and Nichols, Eric and van Erp, Marieke and Limsopatham, Nut",
    booktitle = "Proceedings of the 3rd Workshop on Noisy User-generated Text",
    year = "2017",
    publisher = "Association for Computational Linguistics"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-14T09:34:41.948349+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/wenge-research/YAYI-UIE",
  "prompt": "Show the repository structure and data format. I want to know: what JSON format does YAYI-UIE use for NER? Does it include character offsets? Which NER datasets does it include conversion scripts for?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/wenge-research/YAYI-UIE",
    "prompt": "Show the repository structure and data format. I want to know: what JSON format does YAYI-UIE use for NER? Does it include character offsets? Which NER datasets does it include conversion scripts for?"
  }
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-14T09:34:41.948477+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/jnlpba",
  "prompt": "Extract: entity types, dataset splits sizes (train/validation/test number of examples), license, relation to GENIA corpus, and whether it's commonly used for biomedical NER benchmarking."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/jnlpba",
    "prompt": "Extract: entity types, dataset splits sizes (train/validation/test number of examples), license, relation to GENIA corpus, and whether it's commonly used for biomedical NER benchmarking."
  }
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-14T09:34:41.948603+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/universal-ie/UIE/tree/main/dataset_processing",
  "prompt": "List all files and directories. I want to see which datasets have processing scripts, especially NER datasets like CoNLL-2003, OntoNotes, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/universal-ie/UIE/tree/main/dataset_processing",
    "prompt": "List all files and directories. I want to see which datasets have processing scripts, especially NER datasets like CoNLL-2003, OntoNotes, etc."
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-14T09:34:41.948725+00:00_

# JNLPBA Dataset Information

Based on the web page content provided, here's what can be extracted:

## Available Information

| Field | Value |
|-------|-------|
| **Dataset Name** | jnlpba/jnlpba |
| **Last Updated** | Jan 18, 2024 |
| **Size** | 1.03k |
| **Downloads** | 9 |
| **Organization** | jnlpba |
| **Team Lead** | Albert Villanova del Moral |

## Information Not Available in Content

The web page snippet provided does **not contain** the following details:

- ❌ **Entity types** (not specified)
- ❌ **Dataset splits and sizes** (train/validation/test examples not listed)
- ❌ **License information** (not displayed)
- ❌ **Relation to GENIA corpus** (not mentioned)
- ❌ **Biomedical NER benchmark status** (not indicated)

## Recommendation

To obtain the missing information (entity types, split sizes, license, GENIA corpus relation, and NER benchmarking use), you would need to:

1. Visit the full dataset page at `huggingface.co/datasets/jnlpba/jnlpba`
2. Check the dataset card/README section
3. Review the dataset documentation tab
4. Examine the dataset configuration details

The current page only shows the organization profile overview, not the complete dataset metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-14T09:34:41.948875+00:00_

# YAYI-UIE JSON Format and Dataset Information

Based on the provided documentation, here's what I found:

## JSON Format for NER

The repository shows this instruction example for entity extraction:

> "抽取文本中可能存在的实体，并以json{人物/机构/地点：[实体]}格式输出"

This translates to a format like `{entity_type: [entities]}`. However, **the documentation does not specify whether character offsets are included** in the output format.

## Datasets Mentioned

The page lists NER datasets used for evaluation:
- **English**: AI, Literature, Music, Politics, Science
- **Chinese**: boson, clue, weibo

## Important Limitation

The repository was **archived on March 30, 2025** and is now read-only. The provided content focuses on model evaluation results rather than detailed implementation specifications. 

To find specific information about JSON schema including offsets and conversion scripts, you would need to:
1. Check the actual code in the repository's `/test` directory
2. Review the full technical paper referenced: "YAYI-UIE: A Chat-Enhanced Instruction Tuning Framework for Universal Information Extraction"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-14T09:34:41.949036+00:00_

# Dataset Processing Scripts Available

Based on the GitHub repository structure, here are the datasets with available processing scripts:

## Datasets with Processing Scripts

**Entity/NER:**
- CoNLL03
- ACE04
- ACE05
- CoNLL04 (via relation processing)

**Relation:**
- NYT
- CoNLL04
- ACE05-Rel
- SciERC

**Event:**
- ACE05-Evt
- CASIE

**Aspect-Based Sentiment Analysis (ABSA):**
- 14lap, l4res, 15res, 16res

## Important Note

The documentation does not mention OntoNotes or other common NER datasets. The README states: "We follows the preprocessing methods with the following works" and then lists specific sources for each dataset. The scripts primarily focus on converting existing datasets into a unified format rather than providing original preprocessing for all major NER benchmarks.

The conversion workflow involves reading configuration files and using task-specific classes to "automatically find the task_format class that reads the data," suggesting the system is designed for datasets already preprocessed by referenced external projects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-14T09:34:41.949189+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "JNLPBA GENIA NER dataset entity types train test split size protein DNA RNA cell_line cell_type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "JNLPBA GENIA NER dataset entity types train test split size protein DNA RNA cell_line cell_type"
  }
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-14T09:34:41.949325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"conll2003\" \"character offset\" OR \"char_start\" OR \"char_end\" NER json conversion python github 2024 2025",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"conll2003\" \"character offset\" OR \"char_start\" OR \"char_end\" NER json conversion python github 2024 2025",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-14T09:34:41.949455+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE IE_INSTRUCTIONS NER data format huggingface dataset ner_conll conll2003"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE IE_INSTRUCTIONS NER data format huggingface dataset ner_conll conll2003"
  }
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-14T09:34:41.949583+00:00_

Web search results for query: ""conll2003" "character offset" OR "char_start" OR "char_end" NER json conversion python github 2024 2025"

Links: [{"title":"conll-2003 · GitHub Topics","url":"https://github.com/topics/conll-2003"},{"title":"NER/corpus/CoNLL-2003 at master · synalp/NER","url":"https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003"},{"title":"Build software better, together","url":"https://github.com/topics/conll-2003?l=python"},{"title":"GitHub - pranabsarkar/Conll_task: In this Repository you will find 3 different NLP models trained on the English CoNLL-2003 dataset, which can tag the sentences into their respective POS tags, Syntactic chunk tags, and NER tags.","url":"https://github.com/pranabsarkar/Conll_task"},{"title":"GitHub - shahrukhgellani/CNN-NER-Conll2003: Named Entity recognition Using Python","url":"https://github.com/shahrukhgellani/CNN-NER-Conll2003"},{"title":"GitHub - Franck-Dernoncourt/NeuroNER: Named-entity recognition using neural networks. Easy-to-use and state-of-the-art results. · GitHub","url":"https://github.com/Franck-Dernoncourt/NeuroNER"},{"title":"GitHub - ningshixian/NER-CONLL2003: Entity recognition of CONLL2003 corpus using Keras · GitHub","url":"https://github.com/ningshixian/NER-CONLL2003"},{"title":"GitHub - microsoft/presidio-research: This package features data-science related tasks for developing new recognizers for Presidio. It is used for the evaluation of the entire system, as well as for evaluating specific PII recognizers or PII detection models. · GitHub","url":"https://github.com/microsoft/presidio-research"},{"title":"convert from conll2003 to ner-json loses tags · explosion/spaCy · Discussion #8738","url":"https://github.com/explosion/spaCy/discussions/8738"},{"title":"GitHub - janmejaya-nanda/NER-CoNLL-2003: Named Entity Recognition using CoNLL 2003","url":"https://github.com/janmejaya-nanda/NER-CoNLL-2003"}]

Based on the web search results, I found some relevant information about CoNLL-2003 NER d
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-14T09:34:41.949739+00:00_

Web search results for query: "JNLPBA GENIA NER dataset entity types train test split size protein DNA RNA cell_line cell_type"

Links: [{"title":"1 Revised JNLPBA Corpus: A Revised Version of Biomedical NER","url":"https://arxiv.org/pdf/1901.10219"},{"title":"jnlpba/jnlpba · Datasets at Hugging Face","url":"https://huggingface.co/datasets/jnlpba/jnlpba"},{"title":"jnlpba · Datasets at Hugging Face","url":"https://huggingface.co/datasets/jnlpba"},{"title":"README.md · jnlpba/jnlpba at main","url":"https://huggingface.co/datasets/jnlpba/jnlpba/blob/main/README.md"},{"title":"Biomedical named entity extraction: some issues of corpus compatibilities - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3837077/"},{"title":"Nested Named Entity Recognition Jenny Rose Finkel and Christopher D. Manning","url":"https://nlp.stanford.edu/pubs/nested-ner.pdf"},{"title":"Seeking Advice on Stratifying a Multi-label NER Dataset for Balanced Train/Test Split - Beginners - Hugging Face Forums","url":"https://discuss.huggingface.co/t/seeking-advice-on-stratifying-a-multi-label-ner-dataset-for-balanced-train-test-split/67980"},{"title":"Attending to Characters in Neural Sequence Labeling Models","url":"https://hyunyoung2.github.io/2020/05/28/Attending_to_Characters_in_Neural_Sequence_Labeling_Models/"},{"title":"JNLPBA Dataset · Issue #3089 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/3089"},{"title":"Basic statistics of the JNLPBA dataset | Download Table","url":"https://www.researchgate.net/figure/Basic-statistics-of-the-JNLPBA-dataset_tbl2_7273777"}]

Based on the search results, here's detailed information about the JNLPBA GENIA NER dataset:

## Entity Types

The JNLPBA dataset preserves five entity types: protein, DNA, RNA, cell line and cell type.

## Dataset Structure and Split Sizes

The dataset contains 22.4k rows total, with a train split of 18.5k rows and a validation split of 3.86k rows. More specifically, the train set has 18,546 example
…[truncated 913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-14T09:34:41.949906+00:00_

Web search results for query: "InstructUIE IE_INSTRUCTIONS NER data format huggingface dataset ner_conll conll2003"

Links: [{"title":"dslim/bert-base-NER · Hugging Face","url":"https://huggingface.co/dslim/bert-base-NER"},{"title":"olgaduchovny/t5-base-ner-conll · Hugging Face","url":"https://huggingface.co/olgaduchovny/t5-base-ner-conll"},{"title":"How to Fine-Tune BERT for NER Using HuggingFace","url":"https://www.freecodecamp.org/news/getting-started-with-ner-models-using-huggingface/"},{"title":"How to build custom NER HuggingFace dataset for receipts and train with HuggingFace Transformers library? | by Mageswaran D | Medium","url":"https://mageswaran1989.medium.com/how-to-build-custom-ner-huggingface-dataset-for-receipts-and-train-with-huggingface-transformers-6c954b84473c"},{"title":"arubenruben/NER-PT-BERT-CRF-Conll2003 · Hugging Face","url":"https://huggingface.co/arubenruben/NER-PT-BERT-CRF-Conll2003"},{"title":"sfarrukhm/bert-conll-ner · Hugging Face","url":"https://huggingface.co/sfarrukhm/bert-conll-ner"},{"title":"Named Entity Recognition with Transformers - Chris Tran","url":"https://chriskhanhtran.github.io/posts/named-entity-recognition-with-transformers/"},{"title":"Tutorial: How to Fine-Tune BERT for Named Entity Recognition (NER)","url":"https://skimai.com/how-to-fine-tune-bert-for-named-entity-recognition-ner/"},{"title":"Solving NER with RL | Israel Adewuyi","url":"https://israel-adewuyi.github.io/blog/2025/ner_with_rl/"},{"title":"How to Train an NER model with HuggingFace? - Analytics Vidhya","url":"https://www.analyticsvidhya.com/blog/2022/06/how-to-train-an-ner-model-with-huggingface/"}]

I found some relevant information about NER datasets and frameworks. Let me search specifically for InstructUIE to get more detailed information about the IE_INSTRUCTIONS data format.

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://ar5iv.labs.arxiv.org/html/2304.08085"},{"title"
…[truncated 3229 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-14T09:34:41.950064+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/Babelscape/multinerd",
  "prompt": "Extract: entity types (full list), dataset splits sizes for English (train/validation/test number of examples), license information, and total dataset size."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/Babelscape/multinerd",
    "prompt": "Extract: entity types (full list), dataset splits sizes for English (train/validation/test number of examples), license information, and total dataset size."
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-14T09:34:41.950359+00:00_

Now I have comprehensive information. Here is the consolidated report.

---

## 1. HuggingFace Availability

**`load_dataset("conll2003")` is BROKEN** with `datasets>=4.0.0`. The error is:
```
RuntimeError: Dataset scripts are no longer supported, but found conll2003.py
```

**Working alternatives (tested/confirmed):**

| Dataset ID | Status | Notes |
|---|---|---|
| `load_dataset("lhoestq/conll2003")` | Working | Parquet-native, no script dependency |
| `load_dataset("BramVanroy/conll2003")` | Working | Maintained republication with credits preserved |
| `load_dataset("eriktks/conll2003", revision="convert/parquet")` | Working | Must specify parquet revision |
| `load_dataset("tner/conll2003")` | Working | Simplified format (tokens + tags only, no POS/chunk) |
| `load_dataset("conll2003", trust_remote_code=True)` | Works only with `datasets<=3.6.0` | Requires HF token |

**Recommendation for your experiment:** Use `load_dataset("BramVanroy/conll2003")` or `load_dataset("lhoestq/conll2003")`. Both are Parquet-backed and don't need legacy script support.

## 2. Entity Types

4 NER entity types (IOB2 tagging):

| Tag ID | Label | Description |
|---|---|---|
| 0 | O | Outside any entity |
| 1 | B-PER | Begin Person |
| 2 | I-PER | Inside Person |
| 3 | B-ORG | Begin Organization |
| 4 | I-ORG | Inside Organization |
| 5 | B-LOC | Begin Location |
| 6 | I-LOC | Inside Location |
| 7 | B-MISC | Begin Miscellaneous |
| 8 | I-MISC | Inside Miscellaneous |

**Note:** The `eriktks/conll2003` version uses a different label ordering: `{O:0, B-ORG:1, B-MISC:2, B-PER:3, I-PER:4, B-LOC:5, I-ORG:6, I-MISC:7, I-LOC:8}`. Be careful about which dataset ID you use -- label-to-index mappings differ.

## 3. Dataset Size

| Split | Sentences |
|---|---|
| train | 14,041 |
| validation | 3,250 |
| test | 3,453 |
| **Total** | **20,744** |

Total disk: ~1.6-15 MB depending on format (Parquet vs original).

## 4. Data Format

HuggingFace structure per example:
```python
{
    "id": "0",
   
…[truncated 3881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-14T09:34:41.950566+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/IE_INSTRUCTIONS/NER",
  "prompt": "List all directories and files. I want to see which NER datasets have conversion scripts or data files here."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/IE_INSTRUCTIONS/NER",
    "prompt": "List all directories and files. I want to see which NER datasets have conversion scripts or data files here."
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-14T09:34:41.950708+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-14T09:34:41.950898+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/zjunlp/IEPile/main/ie2instruction/convert_func.py",
  "prompt": "Show the COMPLETE code. I want to see how IEPile converts NER datasets to its instruction format. What is the input format expected? Does it handle BIO-tagged CoNLL data? How are entities represented?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/zjunlp/IEPile/main/ie2instruction/convert_func.py",
    "prompt": "Show the COMPLETE code. I want to see how IEPile converts NER datasets to its instruction format. What is the input format expected? Does it handle BIO-tagged CoNLL data? How are entities represented?"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-14T09:34:41.951044+00:00_

# MultiNERD Dataset Summary

## Entity Types (Full List)

The dataset includes **15 fine-grained NER categories**:

1. **PER** - Person
2. **LOC** - Location
3. **ORG** - Organization
4. **ANIM** - Animal
5. **BIO** - Biological entity
6. **CEL** - Celestial Body
7. **DIS** - Disease
8. **EVE** - Event
9. **FOOD** - Food
10. **INST** - Instrument
11. **MEDIA** - Media
12. **PLANT** - Plant
13. **MYTH** - Mythological entity
14. **TIME** - Time
15. **VEHI** - Vehicle

Each entity type uses BIO tagging scheme (B- for beginning, I- for inside, O for outside).

## Dataset Splits

The complete dataset contains **3.35M rows** across 3 splits:

- **Train**: 2.68M rows
- **Validation**: 335K rows
- **Test**: 336K rows

*Note: The web page displays German language examples. English-specific split sizes are not explicitly provided in the excerpt, but the total split distribution applies across all 10 languages.*

## License Information

**CC-BY-NC-SA-4.0** (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License)

- Restricted to non-commercial research purposes only
- Copyright belongs to original copyright holders

## Total Dataset Size

**542 MB** (total file size across all languages and splits)

## Coverage

- **10 Languages**: Chinese, Dutch, English, French, German, Italian, Polish, Portuguese, Russian, Spanish
- **2 Genres**: Wikipedia and WikiNews

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-14T09:34:41.951231+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/DFKI-SLT/cross_ner",
  "prompt": "Extract: all domains and their entity types, dataset splits sizes per domain (train/dev/test), license, and total number of entity types across all domains."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/DFKI-SLT/cross_ner",
    "prompt": "Extract: all domains and their entity types, dataset splits sizes per domain (train/dev/test), license, and total number of entity types across all domains."
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-14T09:34:41.951386+00:00_

# IEPile NER Conversion Analysis

Based on the provided code, here's what I can determine about the conversion process:

## Input Format

The script expects JSON data via `--src_path`, reading records that contain a `'text'` field. The exact structure of task-specific annotations isn't shown in this excerpt, as those details are handled by the `processer.get_task_record()` method.

## Processing Pipeline

The code doesn't directly show BIO-tagged CoNLL handling. Instead, it abstracts data processing through:

- **Processer**: Reads data and extracts task records from raw input
- **Converter**: Transforms annotations into output text based on schemas

## Entity Representation

Entities are represented through **schemas** - the code references `"schema":schema1` in instructions. The exact entity format depends on the task type (NER, RE, SPO, etc.), determined by:

```
processer.get_schemas(task_record)
```

## Key Operations

1. Data is split into batches: `"single instruction max schema quantity. Default 4"`
2. Instructions combine: `"instruction", "schema", "input"` (the text)
3. Training data adds `"output"` via the converter

The actual entity format specifics—whether supporting BIO tags or other schemes—isn't detailed in this code excerpt. That logic resides in task-specific processer and converter implementations not shown here.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 210 · 2026-05-14T09:34:41.951537+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/zjunlp/IEPile/tree/main/ie2instruction",
  "prompt": "List all files and directories. I want to see all the conversion scripts available, especially NER-related ones."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/zjunlp/IEPile/tree/main/ie2instruction",
    "prompt": "List all files and directories. I want to see all the conversion scripts available, especially NER-related ones."
  }
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-14T09:34:41.951690+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/data",
  "prompt": "List all directories. I want to see how datasets are organized - which NER datasets are included."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/BeyonderXX/InstructUIE/tree/master/data",
    "prompt": "List all directories. I want to see how datasets are organized - which NER datasets are included."
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-14T09:34:41.951858+00:00_

# CrossNER Dataset Overview

## Domains and Entity Types

The CrossNER dataset spans **6 domains** with specialized entity categories:

1. **Politics** - Political entities
2. **Natural Science** - Scientific entities
3. **Music** - Music-related entities
4. **Literature** - Literary entities
5. **Artificial Intelligence** - AI/tech entities
6. **CoNLL2003** - General news domain (benchmark)

## Dataset Split Sizes (per domain)

| Domain | Train | Dev | Test |
|--------|-------|-----|------|
| conll2003 | 14,987 | 3,466 | 3,684 |
| politics | 200 | 541 | 651 |
| science | 200 | 450 | 543 |
| music | 100 | 380 | 456 |
| literature | 100 | 400 | 416 |
| ai | 100 | 350 | 431 |
| **TOTAL** | **15,687** | **5,587** | **5,781** |

## Total Entity Types

**79 entity types** across all domains (78 specialized + 1 O/Outside tag)

The entity schema uses BIO (Begin-Inside-Outside) tagging format with tags including:
- B-/I- prefixes for entity boundaries
- Domain-specific categories like: `academicjournal`, `album`, `algorithm`, `award`, `band`, `book`, `chemicalcompound`, `person`, `organisation`, `product`, `programlang`, `researcher`, `scientist`, `task`, `theory`, `university`, `writer`, etc.

## License

**[More Information Needed]** - Not explicitly specified in the dataset card

## Key Metadata

- **Total Rows**: 26,071 sentences
- **Language**: English (en)
- **Task**: Token Classification / Named Entity Recognition
- **Size**: 38.9 kB (Parquet format)
- **ArXiv**: [2012.04373](https://arxiv.org/abs/2012.04373)
- **Citation Year**: 2020

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-14T09:34:41.951999+00:00_

# IEPile ie2instruction Directory Contents

Based on the webpage, the `ie2instruction` directory contains:

## Folders
- **convert** - Contains conversion-related scripts
- **eval** - Contains evaluation-related scripts

## Files
- `__init__.py` - Python package initialization
- `convert_func.py` - Conversion functions
- `eval_data_convert.bash` - Bash script for evaluation data conversion
- `eval_func.py` - Evaluation functions

## Limitation

The webpage only shows the directory structure and file names without revealing the specific contents of each conversion script or confirming which ones are NER-related. To identify the NER-specific conversion scripts, you would need to examine the actual code within the `convert` folder and the `convert_func.py` file directly in the repository.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-14T09:34:41.952163+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WikiNER dataset HuggingFace availability NER benchmark freely available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WikiNER dataset HuggingFace availability NER benchmark freely available"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-14T09:34:41.952320+00:00_

Based on the web page content provided, I can see the directory structure is limited in what's displayed. The page shows:

1. **gpt2tokenizer** - a subdirectory
2. **generate_labels.py** - a Python file

Unfortunately, the webpage content doesn't provide a complete listing of all datasets or NER (Named Entity Recognition) datasets included in the repository. The page appears to be a GitHub directory view of the `/data` folder in the InstructUIE project, but the full file listing isn't rendered in the provided HTML.

To see the complete dataset organization and identify which NER datasets are available, you would need to:
- Visit the GitHub repository directly at https://github.com/BeyonderXX/InstructUIE/tree/master/data
- Check the project's README documentation
- Explore the repository's structure through GitHub's interface

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-14T09:34:41.952458+00:00_

Web search results for query: "WikiNER dataset HuggingFace availability NER benchmark freely available"

Links: [{"title":"cmarkea/distilcamembert-base-ner · Hugging Face","url":"https://huggingface.co/cmarkea/distilcamembert-base-ner"},{"title":"Jean-Baptiste/wikiner_fr · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Jean-Baptiste/wikiner_fr"},{"title":"Jean-Baptiste/camembert-ner · Hugging Face","url":"https://huggingface.co/Jean-Baptiste/camembert-ner"},{"title":"danrun/WikiNER-fr-gold · Datasets at Hugging Face","url":"https://huggingface.co/datasets/danrun/WikiNER-fr-gold"},{"title":"GitHub - juand-r/entity-recognition-datasets: A collection of corpora for named entity recognition (NER) and entity recognition tasks. These annotated datasets cover a variety of languages, domains and entity types. · GitHub","url":"https://github.com/juand-r/entity-recognition-datasets"},{"title":"CATIE-AQ/wikiner_fr_prompt_ner · Datasets at Hugging Face","url":"https://huggingface.co/datasets/CATIE-AQ/wikiner_fr_prompt_ner"},{"title":"mnaguib/WikiNER · Datasets at Hugging Face","url":"https://huggingface.co/datasets/mnaguib/WikiNER"},{"title":"turkish-nlp-suite/turkish-wikiNER · Datasets at Hugging Face","url":"https://huggingface.co/datasets/turkish-nlp-suite/turkish-wikiNER"},{"title":"Paper page - WikiNER-fr-gold: A Gold-Standard NER Corpus","url":"https://huggingface.co/papers/2411.00030"},{"title":"NER with HuggingFace","url":"https://www.kaggle.com/code/tirendazacademy/ner-with-huggingface"}]

Based on the search results, here's what I found about the WikiNER dataset's availability:

## WikiNER Dataset Availability

WikiNER is a multilingual silver-standard annotated NER dataset consisting of a late-2010 snapshot of Wikipedia in nine languages, with hyperlinks referring to persons, locations or organizations automatically annotated.

The dataset is **available on HuggingFace**. WikiNER is available on HuggingFace at the dataset page mnaguib/WikiNER, and t
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-14T09:34:41.952615+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/zjunlp/IEPile/tree/main/ie2instruction/convert",
  "prompt": "List ALL files in this directory. I need to see the converter scripts for different tasks, especially NER."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/zjunlp/IEPile/tree/main/ie2instruction/convert",
    "prompt": "List ALL files in this directory. I need to see the converter scripts for different tasks, especially NER."
  }
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-14T09:34:41.952749+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "zjunlp IEPile ie2instruction converter NER processer conll2003 entity text format input JSON",
  "allowed_domains": "['github.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "zjunlp IEPile ie2instruction converter NER processer conll2003 entity text format input JSON",
    "allowed_domains": "['github.com']"
  }
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-14T09:34:41.952948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoNLL2003 NER dataset HuggingFace availability test set size 2025 freely available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoNLL2003 NER dataset HuggingFace availability test set size 2025 freely available"
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-14T09:34:41.953081+00:00_

Based on the webpage content provided, I can see the directory structure for `/ie2instruction/convert`, but the page doesn't display the complete file listing with all converter scripts.

What's visible:
- **converter** (folder)
- **processer** (folder)
- **utils** (folder)
- **__init__.py** (file)

The content indicates there are subdirectories, but the actual converter scripts for specific tasks like NER are not enumerated in this view. To access the NER converter and other task-specific scripts, you would need to navigate into the **converter** folder, as that's likely where task-specific implementations are stored.

The page shows "View all files" link is available, suggesting additional files exist but aren't displayed in the current rendering.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-14T09:34:41.953237+00:00_

Web search results for query: "CoNLL2003 NER dataset HuggingFace availability test set size 2025 freely available"

Links: [{"title":"tner/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/conll2003"},{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"},{"title":"ZihanWangKi/conllpp · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ZihanWangKi/conllpp"},{"title":"philschmid/distilroberta-base-ner-conll2003 · Hugging Face","url":"https://huggingface.co/philschmid/distilroberta-base-ner-conll2003"},{"title":"README.md · conll2003 at main","url":"https://huggingface.co/datasets/conll2003/blob/main/README.md"},{"title":"tner/roberta-large-conll2003 · Hugging Face","url":"https://huggingface.co/tner/roberta-large-conll2003"},{"title":"conll2003.py · conll2003 at main","url":"https://huggingface.co/datasets/conll2003/blob/main/conll2003.py"},{"title":"README.md · eriktks/conll2003 at main","url":"https://huggingface.co/datasets/eriktks/conll2003/blob/main/README.md"},{"title":"Language-Independent Named Entity Recognition (II)","url":"https://www.clips.uantwerpen.be/conll2003/ner/"},{"title":"conll2003 at main","url":"https://huggingface.co/datasets/conll2003/tree/main"}]

Based on the search results, here's what I found about the CoNLL2003 NER dataset on HuggingFace:

## Dataset Availability on HuggingFace

The CoNLL2003 NER dataset is available on HuggingFace with 3 splits: training set with 14k rows, validation set with 3.25k rows, and test set with 3.45k rows.

## Test Set Size

The test set contains 3.45k (3,450) rows.

## Free Availability with Important Caveats

While the dataset is freely available on HuggingFace, there's an important licensing consideration: Because of copyright reasons only the annotations are made available; to build the complete datasets you need access to the Reuters Corpus, which can be obtained for research purposes without any cha
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-14T09:34:41.953394+00:00_

Web search results for query: "zjunlp IEPile ie2instruction converter NER processer conll2003 entity text format input JSON"

Links: [{"title":"GitHub - zjunlp/IEPile: [ACL 2024] IEPile: A Large-Scale Information Extraction Corpus · GitHub","url":"https://github.com/zjunlp/IEPile"},{"title":"IEPile/README_CN.md at main · zjunlp/IEPile","url":"https://github.com/zjunlp/IEPile/blob/main/README_CN.md"},{"title":"GitHub - zjunlp/KnowLM: An Open-sourced Knowledgable Large Language Model Framework. · GitHub","url":"https://github.com/zjunlp/KnowLM"},{"title":"NER/corpus/CoNLL-2003 at master · synalp/NER","url":"https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003"},{"title":"GitHub - zjunlp/DeepKE: [EMNLP 2022] An Open Toolkit for Knowledge Graph Extraction and Construction · GitHub","url":"https://github.com/zjunlp/DeepKE"},{"title":"Replicating CoNLL 2003 NER training · Issue #2219 · allenai/allennlp","url":"https://github.com/allenai/allennlp/issues/2219"},{"title":"[Request] NER Scripts on CoNLL 2003 dataset · Issue #4250 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/4250"},{"title":"NER/corpus/CoNLL-2003/eng.train at master · synalp/NER","url":"https://github.com/synalp/NER/blob/master/corpus/CoNLL-2003/eng.train"},{"title":"Fine-tune a model trained on conll2003 for mit-movie/mit-restaurant/other dataset? · Issue #87 · zjunlp/DeepKE","url":"https://github.com/zjunlp/DeepKE/issues/87"},{"title":"GitHub - pranabsarkar/Conll_task: In this Repository you will find 3 different NLP models trained on the English CoNLL-2003 dataset, which can tag the sentences into their respective POS tags, Syntactic chunk tags, and NER tags.","url":"https://github.com/pranabsarkar/Conll_task"}]

Based on the search results, I found relevant information about the zjunlp IEPile project and its ie2instruction converter for NER with CoNLL2003 data:

## IEPile Project Overview

IEPile has collected and cleaned existing Information Extraction (IE) 
…[truncated 1236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-14T09:34:41.953546+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tner/mit_movie_trivia",
  "prompt": "Extract: entity types, dataset splits sizes (train/test number of examples), license information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tner/mit_movie_trivia",
    "prompt": "Extract: entity types, dataset splits sizes (train/test number of examples), license information."
  }
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-14T09:34:41.953680+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/zjunlp/IEPile/main/ie2instruction/convert/processer/ner_processer.py",
  "prompt": "Show the COMPLETE code. I need to see the NER processer - what input format does it expect? Does it read BIO-tagged CoNLL files directly, or does it expect pre-converted JSON with entity annotations? What fields does it look for in the input data?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/zjunlp/IEPile/main/ie2instruction/convert/processer/ner_processer.py",
    "prompt": "Show the COMPLETE code. I need to see the NER processer - what input format does it expect? Does it read BIO-tagged CoNLL files directly, or does it expect pre-converted JSON with entity annotations? What fields does it look for in the input data?"
  }
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-14T09:34:41.953818+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://raw.githubusercontent.com/zjunlp/IEPile/main/ie2instruction/convert/processer/ee_processer.py",
  "prompt": "Show just the first 30 lines and any get_task_record method. I want to understand the input data format IEPile expects."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://raw.githubusercontent.com/zjunlp/IEPile/main/ie2instruction/convert/processer/ee_processer.py",
    "prompt": "Show just the first 30 lines and any get_task_record method. I want to understand the input data format IEPile expects."
  }
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-14T09:34:41.953946+00:00_

# MIT Movie Trivia Dataset - Key Information

## Entity Types

The dataset contains **12 entity types** for Named Entity Recognition:

1. **Actor** (B-Actor, I-Actor)
2. **Plot** (B-Plot, I-Plot)
3. **Opinion** (B-Opinion, I-Opinion)
4. **Award** (B-Award, I-Award)
5. **Year** (B-Year, I-Year)
6. **Genre** (B-Genre, I-Genre)
7. **Origin** (B-Origin, I-Origin)
8. **Director** (B-Director, I-Director)
9. **Soundtrack** (B-Soundtrack, I-Soundtrack)
10. **Relationship** (B-Relationship, I-Relationship)
11. **Character_Name** (B-Character_Name, I-Character_Name)
12. **Quote** (B-Quote, I-Quote)

## Dataset Splits

| Split | Size |
|-------|------|
| **Train** | 6,816 examples |
| **Validation** | 1,000 examples |
| **Test** | 1,953 examples |
| **Total** | 9,769 examples |

## License Information

**License:** `other` (non-standard license - refer to the [label.json](https://huggingface.co/datasets/tner/mit_movie_trivia/raw/main/dataset/label.json) and repository for specific terms)

## Example Data Format

```json
{
    "tokens": ["a", "steven", "spielberg", "film", "featuring", ...],
    "tags": [0, 13, 14, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4]
}
```

Where tag `0` = "O" (Outside), `13` = "B-Director" (Begin), `14` = "I-Director" (Inside), etc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-14T09:34:41.954074+00:00_

# NERProcesser Input Format Analysis

Based on the provided code snippet, the NERProcesser expects **pre-converted JSON format** with entity annotations rather than raw BIO-tagged CoNLL files.

## Expected Input Fields

The processor looks for these key fields in input data:

1. **`'entity'`** - The primary field containing entity annotations. Retrieved via `record.get('entity', None)`, this should be a list of entity objects.

2. **`'entity_type'`** - Each entity object requires this field, indicating the entity classification.

3. **`'entity'`** (within each annotation) - The actual entity text string.

## Data Structure

Each record should follow this structure:
```
{
  'entity': [
    {'entity': 'text', 'entity_type': 'TYPE'},
    ...
  ]
}
```

## Key Processing Behaviors

The `filter_lable` method deduplicates entities using `"(label['entity'], label['entity_type']) in already"`, removing duplicate entity-type pairs from the same record.

The processor **does not directly parse CoNLL or BIO-tagged files**. Instead, it expects data already converted to JSON with explicit entity and entity_type fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-14T09:34:41.954220+00:00_

# IEPile Input Data Format

Based on the code provided, here's what we can determine:

## First 30 Lines
The class imports random/numpy seeds and inherits from a `Processer` base class, initializing with type lists, role lists, and type-role dictionaries.

## Data Format Expectations

The `get_task_record` method reveals the input structure:

```python
def get_task_record(self, record):
    return record.get('event', None)
```

This indicates that input records expect an **'event' key** containing event extraction data.

## Event Structure

From the `get_positive_type_role` method, events should contain:
- **event_type**: classification of the event (string)
- **arguments**: list of argument objects, each with:
  - **role**: the argument role/type (string)

Example structure:
```
{
  'event': [
    {
      'event_type': 'Attack',
      'arguments': [
        {'role': 'attacker'},
        {'role': 'target'}
      ]
    }
  ]
}
```

This format supports event extraction tasks where the processor identifies event types and their associated argument roles from input text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-14T09:34:41.954361+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://huggingface.co/datasets/tner/mit_restaurant",
  "prompt": "Extract: entity types, dataset splits sizes (train/test number of examples), license information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://huggingface.co/datasets/tner/mit_restaurant",
    "prompt": "Extract: entity types, dataset splits sizes (train/test number of examples), license information."
  }
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-14T09:34:41.954485+00:00_

# MIT Restaurant NER Dataset - Key Information

## Entity Types
The dataset contains **8 entity types** for Named Entity Recognition:
1. **Rating** - Restaurant ratings/reviews
2. **Amenity** - Restaurant features/facilities
3. **Location** - Geographic locations
4. **Restaurant_Name** - Names of restaurants
5. **Price** - Price-related information
6. **Hours** - Operating hours
7. **Dish** - Food items/dishes
8. **Cuisine** - Cuisine types

## Dataset Splits

| Split | Number of Examples |
|-------|------------------|
| **Train** | 6,900 |
| **Validation** | 760 |
| **Test** | 1,521 |
| **Total** | 9,181 |

## License
**Other** (Custom license - refer to the [T-NER repository](https://github.com/asahi417/tner) for specific terms)

## Label IDs Reference
```json
{
    "O": 0,
    "B-Rating": 1, "I-Rating": 2,
    "B-Amenity": 3, "I-Amenity": 4,
    "B-Location": 5, "I-Location": 6,
    "B-Restaurant_Name": 7, "I-Restaurant_Name": 8,
    "B-Price": 9, "I-Price": 15,
    "B-Hours": 10, "I-Hours": 11,
    "B-Dish": 12, "I-Dish": 13,
    "B-Cuisine": 14, "I-Cuisine": 16
}
```

The dataset contains conversational utterances about restaurant queries, with BIO (Begin-Inside-Outside) tagging for token-level entity classification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-14T09:34:41.954621+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/zjunlp/IEPile/blob/main/README.md",
  "prompt": "Find the section about data format. I need the EXACT JSON format for NER input data before conversion to instructions. Specifically: what does a single NER training example look like? Show the entity field structure. Also: does IEPile provide the pre-converted CoNLL-2003 data or do users need to convert from BIO themselves?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/zjunlp/IEPile/blob/main/README.md",
    "prompt": "Find the section about data format. I need the EXACT JSON format for NER input data before conversion to instructions. Specifically: what does a single NER training example look like? Show the entity field structure. Also: does IEPile provide the pre-converted CoNLL-2003 data or do users need to convert from BIO themselves?"
  }
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-14T09:34:41.954753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "huggingface datasets \"conll2003\" load_dataset token to character offset span python code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "huggingface datasets \"conll2003\" load_dataset token to character offset span python code"
  }
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-14T09:34:41.954879+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WikiANN English NER test set size wikiann en train validation test examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WikiANN English NER test set size wikiann en train validation test examples"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-14T09:34:41.955005+00:00_

Web search results for query: "WikiANN English NER test set size wikiann en train validation test examples"

Links: [{"title":"GitHub - JHH11/Named_Entity_Recognition: Fine-tuning BERT for Named Entity Recognition with WikiANN Dataset","url":"https://github.com/JHH11/Named_Entity_Recognition"},{"title":"unimelb-nlp/wikiann · Datasets at Hugging Face","url":"https://huggingface.co/datasets/unimelb-nlp/wikiann"},{"title":"GitHub - jowitapodolak/finetuning_BERT_NER · GitHub","url":"https://github.com/jowitapodolak/finetuning_BERT_NER"},{"title":"datasets/docs/catalog/wikiann.md at master · tensorflow/datasets","url":"https://github.com/tensorflow/datasets/blob/master/docs/catalog/wikiann.md"},{"title":"tner/wikiann · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/wikiann"},{"title":"Toward More Meaningful Resources for Lower-resourced Languages","url":"https://arxiv.org/pdf/2202.12288"},{"title":"wikiann | TensorFlow Datasets","url":"https://www.tensorflow.org/datasets/catalog/wikiann"},{"title":"A Multilingual, Multi-Genre and Fine-Grained Dataset for ...","url":"https://aclanthology.org/2022.findings-naacl.60.pdf"},{"title":"Comparison between WikiNEuRal, WikiNER and WikiANN across different... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Comparison-between-WikiNEuRal-WikiNER-and-WikiANN-across-different-languages-and_fig1_355913464"},{"title":"SEACrowd/wikiann · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SEACrowd/wikiann"}]

Based on the search results, I found information about the WikiANN English NER dataset splits:

For the English (en) language in WikiANN, the train, validation, and test dataset sizes are 20,000, 10,000, and 10,000 examples respectively.

The search results also confirm that WikiANN is a multilingual named entity recognition dataset consisting of Wikipedia articles annotated with LOC (location), PER (person), and ORG (organisation) tags in the IOB2 format.

Additionally, t
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-14T09:34:41.955172+00:00_

# IEPile NER Data Format

## Pre-Conversion NER Input Structure

The README doesn't explicitly show the pre-conversion NER data format. However, it references a `/data` directory structure where you should "refer to `sample.json` to understand the format of the data before conversion."

The document states: **"Before using the convert_func.py script, please make sure to refer to the data directory."** It indicates that `sample.json` contains the input format, but the actual JSON structure isn't displayed in this README.

## Post-Conversion NER Example

The README does provide a converted NER instance:

```json
{
  "task": "NER",
  "source": "CoNLL2003",
  "instruction": "{\"instruction\": \"...\", \"schema\": [\"person\", \"organization\", \"else\", \"location\"], \"input\": \"...\"}",
  "output": "{\"person\": [\"Robert Allenby\", \"Allenby\", \"Miguel Angel Martin\"], \"organization\": [], \"else\": [], \"location\": [\"Australia\", \"Spain\"]}"
}
```

## Regarding Pre-Converted Data

The README indicates **IEPile provides pre-processed unified format data**. It states: "The file tree...IE-en/NER/CoNLL2003/" shows that dataset includes `train.json`, `dev.json`, and `test.json` files. Users do not need to convert from BIO themselves—the corpus provides ready-to-use instruction-formatted data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-14T09:34:41.955328+00:00_

Web search results for query: "huggingface datasets "conll2003" load_dataset token to character offset span python code"

Links: [{"title":"eriktks/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/eriktks/conll2003"},{"title":"Loading Custom Datasets - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/loading-custom-datasets/6166"},{"title":"conll2003.py · conll2003 at main","url":"https://huggingface.co/datasets/conll2003/blob/main/conll2003.py"},{"title":"conll2003 dataset loads original data. · Issue #4248 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/4248"},{"title":"eriktks/conll2003 · Have problem in loading data through load_dataset(), saying \"Dataset scripts are no longer supported, but found conll2003.py\"","url":"https://huggingface.co/datasets/eriktks/conll2003/discussions/13"},{"title":"tner/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tner/conll2003"},{"title":"conll2003.py · eriktks/conll2003 at main","url":"https://huggingface.co/datasets/eriktks/conll2003/blob/main/conll2003.py"},{"title":"README.md · conll2003 at main","url":"https://huggingface.co/datasets/conll2003/blob/main/README.md"},{"title":"Load · Hugging Face","url":"https://huggingface.co/docs/datasets/loading"},{"title":"pie/conll2003 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/pie/conll2003"}]

I found search results related to loading the CoNLL2003 dataset with Hugging Face. Here's what I discovered:

## Loading CoNLL2003 Dataset

You can load the dataset using `from datasets import load_dataset` and then `dataset = load_dataset("conll2003")`. If you encounter issues, you may need to use `load_dataset("conll2003", trust_remote_code=True, token=os.getenv("HUGGING_FACE_TOKEN"))`.

## Dataset Structure

A sample example from the 'train' split includes fields like "chunk_tags", "id", "ner_tags", "pos_tags", and "tokens". The dataset provides token-level 
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-14T09:34:41.955493+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"universalner\" OR \"universal_ner\" NER dataset HuggingFace freely available benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"universalner\" OR \"universal_ner\" NER dataset HuggingFace freely available benchmark 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-14T09:34:41.955626+00:00_

Web search results for query: ""universalner" OR "universal_ner" NER dataset HuggingFace freely available benchmark 2024 2025"

Links: [{"title":"universalner/universal_ner · Datasets at Hugging Face","url":"https://huggingface.co/datasets/universalner/universal_ner"},{"title":"Universal-NER/UniNER-7B-all · Hugging Face","url":"https://huggingface.co/Universal-NER/UniNER-7B-all"},{"title":"README.md · universalner/universal_ner at main","url":"https://huggingface.co/datasets/universalner/universal_ner/blob/main/README.md"},{"title":"Paper page - Universal NER: A Gold-Standard Multilingual Named Entity Recognition Benchmark","url":"https://huggingface.co/papers/2311.09122"},{"title":"Universal-NER/UniNER-7B-type · Hugging Face","url":"https://huggingface.co/Universal-NER/UniNER-7B-type"},{"title":"universalner (Universal NER)","url":"https://huggingface.co/universalner"},{"title":"GitHub - universal-ner/universal-ner · GitHub","url":"https://github.com/universal-ner/universal-ner"},{"title":"Universal NER","url":"https://universal-ner.github.io/"},{"title":"Universal-NER (Universal-NER)","url":"https://huggingface.co/Universal-NER"},{"title":"Universal NER - Universal NER","url":"http://www.universalner.org/"}]

Based on the search results, here's what I found about the Universal NER dataset:

## Universal NER (UNER) - NER Dataset

Universal NER (UNER) is an open, community-driven initiative aimed at creating gold-standard benchmarks for Named Entity Recognition (NER) across multiple languages.

### Dataset Availability
The Universal NER dataset is available on HuggingFace at the repository `universalner/universal_ner`. The data, code, and fitted models are released to the public.

### Dataset Composition
UNER v1 contains 18 datasets annotated with named entities in a cross-lingual consistent schema across 12 diverse languages. Additionally, the Universal NER benchmark consists of 43 academic datasets across 9 domains.

### Project Status
Universal NER v2 has been re
…[truncated 551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 239 · 2026-05-14T09:34:41.955783+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Few-NERD supervised NER IO tagging format not BIO standard evaluation recent papers citing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Few-NERD supervised NER IO tagging format not BIO standard evaluation recent papers citing"
  }
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-14T09:34:41.955922+00:00_

Web search results for query: "Few-NERD supervised NER IO tagging format not BIO standard evaluation recent papers citing"

Links: [{"title":"DFKI-SLT/few-nerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/DFKI-SLT/few-nerd"},{"title":"GitHub - thunlp/Few-NERD: Code and data of ACL 2021 paper \"Few-NERD: A Few-shot Named Entity Recognition Dataset\" · GitHub","url":"https://github.com/thunlp/Few-NERD"},{"title":"dfki-nlp/few-nerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/dfki-nlp/few-nerd"},{"title":"Named entity recognition | NLP-progress","url":"http://nlpprogress.com/english/named_entity_recognition.html"},{"title":"Few-NERD","url":"https://ningding97.github.io/fewnerd/"},{"title":"Few-NERD: A Few-Shot Named Entity Recognition Dataset | Request PDF","url":"https://www.researchgate.net/publication/351656375_Few-NERD_A_Few-Shot_Named_Entity_Recognition_Dataset"},{"title":"The impact of using different annotation schemes on named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1110866520301596"},{"title":"Named Entity Recognition — DaNLP documentation","url":"https://danlp-alexandra.readthedocs.io/en/latest/docs/tasks/ner.html"},{"title":"Label Studio — NER Tagging for Invoices (BIO Format) Data Labeling Template","url":"https://labelstud.io/templates/ner_tagging_invoices_bio_format"},{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.248/"}]

Based on my search, here are the key findings about Few-NERD and its tagging format:

## Few-NERD Dataset Overview

Few-NERD is a large-scale, fine-grained manually annotated named entity recognition dataset, which contains 8 coarse-grained types, 66 fine-grained types, 188,200 sentences, 491,711 entities, and 4,601,223 tokens.

## Tagging Format

A crucial distinction from standard NER practice is that NER tags use the IO tagging scheme. This is notably differe
…[truncated 772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-14T09:34:41.956072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MultiNERD English split size train test validation examples Babelscape"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MultiNERD English split size train test validation examples Babelscape"
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-14T09:34:41.956264+00:00_

Web search results for query: "MultiNERD English split size train test validation examples Babelscape"

Links: [{"title":"Babelscape/multinerd · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Babelscape/multinerd"},{"title":"Babelscape/multinerd · Error while downloading the dataset","url":"https://huggingface.co/datasets/Babelscape/multinerd/discussions/1"},{"title":"GitHub - Babelscape/multinerd: Repository for the paper \"MultiNERD: A Multilingual, Multi-Genre and Fine-Grained Dataset for Named Entity Recognition (and Disambiguation)\" (NAACL 2022).","url":"https://github.com/Babelscape/multinerd"},{"title":"multinerd/README.md at master · Babelscape/multinerd","url":"https://github.com/Babelscape/multinerd/blob/master/README.md"},{"title":"Train Test Validation Split: Best Practices & Examples","url":"https://www.lightly.ai/blog/train-test-validation-split"},{"title":"Babelscape/multinerd at main","url":"https://huggingface.co/datasets/Babelscape/multinerd/tree/main"},{"title":"Huggingface","url":"https://huggingface.co/datasets/Babelscape/multinerd/resolve/main/README.md?download=true"},{"title":"Train Test Validation Split: How To & Best Practices [2024]","url":"https://www.v7darwin.com/blog/train-validation-test-set"},{"title":"19. Model Evaluation Basics: Train, Validation, and Test Splits | by Kiran vutukuri | Medium","url":"https://medium.com/@kiranvutukuri/19-model-evaluation-basics-train-validation-and-test-splits-ed5bb26b088d"},{"title":"Train, Validation, Test Split for Machine Learning","url":"https://blog.roboflow.com/train-test-split/"}]

Based on the search results, I found information about the MultiNERD dataset from Babelscape. Here's what I found regarding the dataset structure:

The MultiNERD dataset covers 10 languages (including English), 15 NER categories, and 2 textual genres (Wikipedia and WikiNews).

Regarding the specific split sizes for the English data, the search results don't contain detailed information about the e
…[truncated 836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-14T09:34:41.956440+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/Babelscape/multinerd/blob/master/README.md",
  "prompt": "Extract the English-specific split sizes (train/validation/test) and number of sentences/examples. Also extract the full list of entity types and their counts if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/Babelscape/multinerd/blob/master/README.md",
    "prompt": "Extract the English-specific split sizes (train/validation/test) and number of sentences/examples. Also extract the full list of entity types and their counts if available."
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-14T09:34:41.956569+00:00_

# MultiNERD English Dataset Summary

Based on the README content provided, here's what I found:

## Dataset Size
The English split contains **164.1K sentences** and **3.6M tokens**. However, the document does not specify separate train/validation/test split proportions.

## Entity Type Counts
The 15 named entity categories and their English counts are:

| Entity Type | Count |
|---|---|
| Person (PER) | 75.8K |
| Location (LOC) | 78.5K |
| Organization (ORG) | 33.7K |
| Animal (ANIM) | 15.5K |
| Event (EVE) | 11.2K |
| Media (MEDIA) | 7.5K |
| Time (TIME) | 9.5K |
| Food (FOOD) | 3.2K |
| Instrument (INST) | 11.0K |
| Mythological entity (MYTH) | 0.7K |
| Celestial Body (CEL) | 2.8K |
| Disease (DIS) | 0.4K |
| Biological entity (BIO) | 0.2K |
| Plant (PLANT) | 3.2K |
| Vehicle (VEHI) | 0.5K |

## Important Note
"The datasets are automatically created, and, therefore, they may contain errors." Higher quality classes include PER, ORG, LOC, CEL, DIS, EVE, and MEDIA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-14T09:34:41.956751+00:00_

I now have comprehensive information. Here is the consolidated report.

---

## Findings Summary

### 1. InstructUIE (BeyonderXX/InstructUIE)

- **Datasets**: Covers CoNLL-2003, OntoNotes, ACE2005, tweetNER7, and others (32 datasets total across NER/RE/EE).
- **Output format**: Text-to-text. NER output is natural language like `"PER: Robert Allenby; LOC: Australia; ..."` -- no character offsets, no structured JSON with start/end.
- **Converter**: `src/convert_data_to_uie.py` delegates to `uie_collator.py` (DataCollatorForUIE). It converts datasets to instruction-response pairs (TSV/JSONL), not to your target `{entities: [{text, type, start, end}]}` format.
- **Verdict**: Not directly usable for your target format. The conversion produces instruction-tuning text pairs, not structured JSON with character offsets.

### 2. GoLLIE (hitz-zentroa/GoLLIE)

- **Datasets supported** (in `src/tasks/`): conll03, ontonotes, ace, bc5cdr, broadtwitter, casie, crossner, diann, e3c, fabner, harveyner, mitmovie, mitrestaurant, multiconer2, multinerd, ncbidisease, rams, tacred, wikievents, wnut. **No GENIA, no Few-NERD.**
- **Output format**: Python dataclass objects with a single `span: str` field (entity text only). Example: `Person(span="Barack Obama")`. **No character offsets.**
- **Converter**: `src/tasks/conll03/data_loader.py` has `get_conll_hf()` (loads from HuggingFace) and `load_conll_tsv()` (loads local CoNLL files). It correctly converts BIO tags to token-span indices, then joins tokens with spaces. But the final representation is `Entity(span="text string")`, not `{text, type, start, end}`.
- **Verdict**: Has solid BIO-to-span conversion logic for 20 datasets, but outputs Python objects with text only, not character-offset JSON. The data_loader code could be adapted.

### 3. IEPile (zjunlp/IEPile) + OneKE/DeepKE

- **Datasets**: 26 English + 7 Chinese IE datasets. NER includes: CoNLL2003, AnatEM, BC2GM, BC4CHEMD, NCBI-Disease, BC5CDR, HarveyNER, GENIA, ACE2005, MIT Restau
…[truncated 3909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-14T09:34:41.956991+00:00_

Now I have comprehensive data on all datasets. Here is the consolidated report.

---

## NER Dataset Research Report

### 1. OntoNotes 5.0

| Field | Detail |
|---|---|
| **Availability** | Officially requires LDC license (LDC2013T19). However, community-uploaded versions exist on HuggingFace. |
| **HF dataset IDs** | `tner/ontonotes5` (recommended, ready-to-use BIO format), `ontonotes/conll2012_ontonotesv5`, `djagatiya/ner-ontonotes-v5-eng-v4` |
| **Entity types** | **18**: CARDINAL, DATE, PERSON, NORP, GPE, LAW, PERCENT, ORDINAL, MONEY, WORK_OF_ART, FAC, TIME, QUANTITY, PRODUCT, LANGUAGE, ORG, LOC, EVENT |
| **Splits** | Train: 59,924 / Val: 8,528 / Test: **8,262** |
| **Deadline feasibility** | `tner/ontonotes5` is directly loadable via `datasets.load_dataset("tner/ontonotes5")` right now. No LDC needed for this mirror. Use at your own risk regarding licensing. |
| **Citation frequency** | Extremely high -- one of the top-3 most cited NER benchmarks alongside CoNLL-2003. |

### 2. GENIA (via JNLPBA)

| Field | Detail |
|---|---|
| **Availability** | Free. The NER task is distributed as the JNLPBA shared task dataset (2004). |
| **HF dataset ID** | `jnlpba` (also `jnlpba/jnlpba`) |
| **Entity types** | **5 biomedical**: protein, DNA, RNA, cell_line, cell_type |
| **Splits** | Train: 18,546 / Val: 3,856 / Test: **~3,856** (the original JNLPBA test set has ~404 abstracts; HF provides train+validation only -- the test set may need to be obtained separately from the shared task page) |
| **Commonly cited?** | Yes, still the standard biomedical NER benchmark. Widely cited in domain-adaptation and cross-domain NER papers. |
| **Caveat** | HF `jnlpba` only has train and validation splits. The original test set from the 2004 shared task may need manual download. Verify with `load_dataset("jnlpba")` to check available splits. |

### 3. Few-NERD

| Field | Detail |
|---|---|
| **Availability** | Free, CC BY-SA 4.0 |
| **HF dataset ID** | `DFKI-SLT/few-nerd` (also `dfki-nlp/
…[truncated 5655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "Agent",
  "elapsed_ms": 29
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-14T09:34:41.957262+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-14T09:34:41.957423+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-14T09:34:41.957563+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-14T09:34:41.957685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 251 · 2026-05-14T09:34:41.957810+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-14T09:34:41.957974+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 经验教训\\n\\n### Offset hallucination\\nFine-tuned generative IE 模型输出正确 entity text 但 hallucinate character offsets（准确率仅 16.7%）。必须用 span realignment 后处理修复。这是 generative IE 的已知问题，不影响 paper claim。\\n\\n### Qwen3 think block vs XGrammar\\nQwen3 默认输出 `&lt;think>...&lt;/think>` 再接 JSON，但 XGrammar 强制 `{` 为第一个 token。必须在 `apply_chat_template` 中设 `enable_thinking=False`。\\n\\n### Train/inference prompt alignment\\n训练用 unified template \\\"Extract all structured information...\\\"，推理必须用完全一致的 template + schema hints。不对齐会导致模型不识别指令。\\n\\n### Parse failures from max_tokens truncation (2026-05-14)\\nmax_tokens=512 导致 3.7% stochastic + 5.3% greedy parse failures。max_tokens=1024 完全消除了 parse failures (0/4408)。\\n\\n### submit_training_job 需要 tmux (2026-05-14)\\nAutoDL 5090 服务器默认无 tmux。已安装 tmux 3.2a。\\n\\n### ft_002 nohup 崩溃教训 (2026-05-14)\\nWorker 用 nohup 启动训练后退出，训练在 step 70/585 崩溃，无日志、无 checkpoint、无监控。必须用 submit_training_job（tmux + cron）确保持久化和监控。\\n\\n### OOM 修复：batch_size + gradient_checkpointing (2026-05-14)\\nQwen3-8B LoRA r=32 在 RTX 5090 32GB 上 batch_size=4 会 OOM（step 73 崩溃）。修复：batch_size=2 + gradient_accumulation_steps=8 + gradient_checkpointing=true → 显存 82% (26.8/32.6 GB)，成功完成 585 steps。\\n\\n### vLLM 不能直接加载 LoRA adapter (2026-05-14)\\nvLLM 需要加载 merged model（有 config.json），不能直接加载 LoRA adapter 目录。必须先用 LLaMA Factory export 或 PEFT merge 合并 adapter 到基座模型。\\n\\n### 训练配置必须保留 best checkpoint (2026-05-14)\\nft_002_v2 的 best eval 在 ~step 300 但被 save_total_limit=3 删掉了。未来 SFT 训练配置必须加：\\n```yaml\\nload_best_model_at_end: true\\nmetric_for_best_model: eval_loss\\nsave_total_limit: 5  # 至少保证 best checkpoint 不被删\\n```\\n\\n### E1 否定乘性惩罚假说——RE SJ 问题是根本性的 (2026-05-14)\\nComponent-wise 分解结果：\\n- head_sj ρ=0.210 **远低于** NER ρ_sj=0.383（Δ=-0.173）\\n- **每个 component 单独都比乘性组合差**——乘性组合实际在整合三个弱信号，不是在伤害\\n- ad
…[truncated 1518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-14T09:34:41.958191+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "content": "# Memory — struct_self_consist_ie\n\n## 经验教训\n\n### Offset hallucination\nFine-tuned generative IE 模型输出正确 entity text 但 hallucinate character offsets（准确率仅 16.7%）。必须用 span realignment 后处理修复。这是 generative IE 的已知问题，不影响 paper claim。\n\n### Qwen3 think block vs XGrammar\nQwen3 默认输出 `&lt;think>...&lt;/think>` 再接 JSON，但 XGrammar 强制 `{` 为第一个 token。必须在 `apply_chat_template` 中设 `enable_thinking=False`。\n\n### Train/inference prompt alignment\n训练用 unified template \"Extract all structured information...\"，推理必须用完全一致的 template + schema hints。不对齐会导致模型不识别指令。\n\n### Parse failures from max_tokens truncation (2026-05-14)\nmax_tokens=512 导致 3.7% stochastic + 5.3% greedy parse failures。max_tokens=1024 完全消除了 parse failures (0/4408)。\n\n### submit_training_job 需要 tmux (2026-05-14)\nAutoDL 5090 服务器默认无 tmux。已安装 tmux 3.2a。\n\n### ft_002 nohup 崩溃教训 (2026-05-14)\nWorker 用 nohup 启动训练后退出，训练在 step 70/585 崩溃，无日志、无 checkpoint、无监控。必须用 submit_training_job（tmux + cron）确保持久化和监控。\n\n### OOM 修复：batch_size + gradient_checkpointing (2026-05-14)\nQwen3-8B LoRA r=32 在 RTX 5090 32GB 上 batch_size=4 会 OOM（step 73 崩溃）。修复：batch_size=2 + gradient_accumulation_steps=8 + gradient_checkpointing=true → 显存 82% (26.8/32.6 GB)，成功完成 585 steps。\n\n### vLLM 不能直接加载 LoRA adapter (2026-05-14)\nvLLM 需要加载 merged model（有 config.json），不能直接加载 LoRA adapter 目录。必须先用 LLaMA Factory export 或 PEFT merge 合并 adapter 到基座模型。\n\n### 训练配置必须保留 best checkpoint (2026-05-14)\nft_002_v2 的 best eval 在 ~step 300 但被 save_total_limit=3 删掉了。未来 SFT 训练配置必须加：\n```yaml\nload_best_model_at_end: true\nmetric_for_best_model: eval_loss\nsave_total_limit: 5  # 至少保证 best checkpoint 不被删\n```\n\n### E1 否定乘性惩罚假说——RE SJ 问题是根本性的 (2026-05-14)\nComponent-wise 分解结果：\n- head_sj ρ=0.210 **远低于** NER ρ_sj=0.383（Δ=-0.173）\n- **每个 component 单独都比乘性组合差**——乘性组合实际在整合三个弱信号，不是在伤害\n- additive fix 无效（additive ρ ≈ multiplicative ρ，差 0.001）\n- **根因修正**：不是\"乘性惩罚导致 RE SJ 差\"，而是 span-level SJ 对 RE 任务**根本缺乏区分力**\n- Fleiss' κ 的 surface matching 在 RE 上反而更鲁棒\n- **决策影响**：方案 B（度量分解 pivot）被排除，fallback 方案 A（NER-primary + RE 诊断）\n\n### SJ vs κ 在 NER 和 RE 上表现不对称——核心发现 (2026-05-14)\n跨 3 轮 pilot 的稳定规律：\n- **NER**: SJ 一致且显著优于 κ（delta +0.01→+0.12，p=7e-20），ρ_sj 稳定在 0.36-0.38\n- **RE**: SJ 在 full set 上 2/3 次不如 κ，ρ_sj 锁死在 ~0.24，模型质量提升（F1 35→42%）未改善 ρ\n- E1 证实：问题不在度量公式，而在 span-level SJ 对 RE 的根本适用性\n\n### RE pct_zero 统计范围 bug (2026-05-14)\nrun_mvp_pilot.py 的 `compute_sample_f1_distribution` 在 gold-empty 过滤前调用，导致 gold-empty 实例（RE 28%）被计入 pct_zero，从实际 55% 虚高到 67.6%。已修复：先按 subtask 过滤 gold-nonempty 再算 F1 分布。\n\n## 服务器环境\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\n- conda: /root/miniconda3/\n- 环境初始化: `source /etc/network_turbo && source /root/autodl-tmp/struct_self_consist_ie/env.sh`\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ (不是 /root/autodl-tmp/models/Qwen3-8B/)\n- ft_001 merged: checkpoints/qwen3-8b-scierc-merged/\n- ft_002_v2 adapter: checkpoints/qwen3-8b-scierc-lora-v2/\n- ft_002_v2 merged (final): checkpoints/qwen3-8b-scierc-merged-v2/\n- ft_002_v2 merged (ckpt400): checkpoints/qwen3-8b-scierc-merged-v2-ckpt400/ (待确认)\n- SciERC data: data/scierc/ (train.json, dev.json, test.json)\n\n## E4 NER 多数据集泛化调研报告 (2026-05-14)\n\n### 候选数据集对比表\n\n| 数据集 | 可用性 | HF Dataset ID | Entity Types | Train | Test | 领域 | 转换复杂度 | 推荐？ |\n|--------|--------|---------------|-------------|-------|------|------|-----------|--------|\n| **CoNLL-2003** | ✅ 免费 | `BramVanroy/conll2003` 或 `lhoestq/conll2003` | 4: PER, ORG, LOC, MISC | 14,041 | 3,453 | 新闻 | 简单 | ✅ **强推** |\n| **WNUT-17** | ✅ CC BY 4.0 | `leondz/wnut_17` | 6: corporation, creative-work, group, location, person, product | 3,394 | 1,287 | 社交媒体 | 简单 | ✅ **强推** |\n| **OntoNotes 5.0** | ⚠️ 官方需 LDC | `tner/ontonotes5` (社区镜像) | 18: PERSON, ORG, GPE, DATE, CARDINAL... | 59,924 | 8,262 | 新闻/广播 | 简单 | ⚠️ 许可风险 |\n| **GENIA/JNLPBA** | ✅ 免费 | `jnlpba` | 5: protein, DNA, RNA, cell_line, cell_type | 18,546 | ~3,856 | 生物医学 | 简单 | ✅ 可选 |\n| **Few-NERD** | ✅ CC BY-SA 4.0 | `DFKI-SLT/few-nerd` | 8 coarse / 66 fine | 131,767 | 37,648 | 维基百科 | 中等(IO→BIO) | ⚠️ 格式特殊 |\n| **CrossNER** | ✅ 免费 | `DFKI-SLT/cross_ner` | 5域各不同(~79 total) | 100-200/域 | 400-650/域 | 多领域 | 中等 | ⚠️ 训练集太小 |\n| **MIT Movie** | ✅ 免费 | `tner/mit_movie_trivia` | 12: Actor, Plot, Genre... | 6,816 | 1,953 | 电影查询 | 简单 | ✅ 可选 |\n| **MIT Restaurant** | ✅ 免费 | `tner/mit_restaurant` | 8: Rating, Cuisine, Dish... | 6,900 | 1,521 | 餐厅查询 | 简单 | ✅ 可选 |\n| **ACE05** | ❌ LDC | 无 | 7 | - | - | 新闻 | - | ❌ 不可行 |\n| **MultiNERD** | ⚠️ NC 许可 | `Babelscape/multinerd` | 15 | ~16K(en) | ~3.3K(en) | 维基百科 | 简单 | ⚠️ 银标+NC |\n\n### 注意事项\n\n**CoNLL-2003 HF 兼容性**：原始 `conll2003` ID 在 `datasets>=4.0` 已失效（script-based 不再支持）。必须用 `BramVanroy/conll2003` 或 `lhoestq/conll2003`（Parquet-native）。\n\n**OntoNotes 许可风险**：`tner/ontonotes5` 是社区上传的非官方镜像，严格来说侵犯 LDC 许可。reviewer 可能质疑。如果用，需要在论文中小心措辞。\n\n**数据格式统一**：所有 HF NER 数据集都是 token-level BIO 格式。转换到 UIE char-offset JSON 需要：(1) tokens → text（空格拼接），(2) 累积 char offset 追踪，(3) BIO span 提取。逻辑与现有 `data_utils.py` 的 `_token_offsets()` 一致，每个数据集 ~50 行 Python。\n\n**无现成转换器**：调研了 InstructUIE、GoLLIE、IEPile、UIE、UniversalNER、YAYI-UIE——没有任何项目输出我们需要的 `{text, type, start, end}` char-offset JSON 格式。都是 text-only 或 token-offset。需要自己写转换脚本。\n\n### 推荐方案\n\n**方案：SciERC + CoNLL-2003 + WNUT-17（3 数据集，3 领域）**\n\n| 维度 | SciERC | CoNLL-2003 | WNUT-17 |\n|------|--------|------------|---------|\n| 领域 | 科学论文 | 新闻 | 社交媒体 |\n| Entity Types | 6 (科学) | 4 (通用) | 6 (新兴) |\n| Test Size | 551 | 3,453 | 1,287 |\n| 难度 | 中 | 低 | 高(噪声) |\n\n**选择理由**：\n1. **领域多样性**：科学 → 新闻 → 社交媒体，三个完全不同的文本分布\n2. **全部免费无许可风险**：CoNLL-2003 虽然理论上有 Reuters 限制，但实践中所有 NER 论文都直接用，reviewer 不会质疑\n3. **Entity type 多样性**：科学术语 vs 通用实体 vs 新兴/噪声实体\n4. **CoNLL-2003 是 NER 标杆**：不用它反而会被 reviewer 质疑\n5. **WNUT-17 增加挑战性**：社交媒体噪声文本 + 新兴实体，如果 SJ 在这种难设定下仍有效，说服力极强\n6. **可选第 4 个**：如果时间允许，加 GENIA（生物医学）做第 4 领域\n\n### Evaluation 兼容性\n\n现有 `entity_strict_match` 完全通用——用 `(start, end, type)` 元组匹配，不绑定任何特定 entity type。无需修改。\n\n需要修改的：\n- `sampling.py` 中的 **schema hint**：每个数据集需要自己的 entity type 列表（类似 `SCIERC_SCHEMA_HINT`）\n- **prompt template**：可复用现有 unified template，只换 schema hint 行\n- `data_utils.py`：新增 `convert_conll2003()` 和 `convert_wnut17()` 函数\n\n### Fine-tuning 策略\n\n**Per-dataset fine-tune**（推荐）：\n- 每个数据集独立训练 Qwen3-8B LoRA adapter\n- 这样每个数据集的 SJ correlation 是独立证据，更有说服力\n- CoNLL-2003 训练集 14K 条，比 SciERC 1.8K 大很多，可能需要 subsample 或更多 steps\n\n**Zero-shot 不可行**：SciERC entity types (Method, Task...) 与 CoNLL (PER, ORG...) 完全不同，zero-shot 没有意义。\n\n### 时间估算\n\n| 步骤 | 耗时 | 备注 |\n|------|------|------|\n| 写 BIO→UIE 转换脚本 | 2-3h | CoNLL + WNUT 共用框架 |\n| 生成 sharegpt 训练数据 | 1-2h | 复用现有 sharegpt 生成逻辑 |\n| CoNLL fine-tune | 3-5h | 14K 条，可能需 2-3 epoch |\n| WNUT fine-tune | 1-2h | 3.4K 条，类似 SciERC |\n| Model merge (×2) | 0.5h | |\n| Sampling + eval (×2) | 3-4h | 每数据集 8 samples × test set |\n| 分析 SJ correlation | 1-2h | 复用现有分析脚本 |\n| **总计** | **~2-3 天** | 可并行训练 |\n\n### 风险/Blockers\n\n1. **CoNLL-2003 训练集过大 (14K)**：可能导致训练时间长。可 subsample 到 ~5K 或减少 epoch。\n2. **WNUT-17 噪声文本**：社交媒体缩写/hashtag/非标准拼写可能导致 NER F1 较低，但这正是我们想测的。\n3. **Schema hint 设计**：每个数据集的 entity type 命名需要统一规范（如 CoNLL 用 PER/ORG/LOC/MISC 还是 Person/Organization/Location/Miscellaneous）。\n4. **Offset hallucination 可能更严重**：CoNLL 的长句子可能导致更多 offset 错误，但 span realignment 应能处理。\n5. **时间紧张**：DDL 2026-05-25，只剩 11 天。2-3 天做多数据集实验是可行的，但需要并行操作。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "content": "# Memory — struct_self_consist_ie\n\n## 经验教训\n\n### Offset hallucination\nFine-tuned generative IE 模型输出正确 entity text 但 hallucinate character offsets（准确率仅 16.7%）。必须用 span realignment 后处理修复。这是 generative IE 的已知问题，不影响 paper claim。\n\n### Qwen3 think block vs XGrammar\nQwen3 默认输出 `&lt;think>...&lt;/think>` 再接 JSON，但 XGrammar 强制 `{` 为第一个 token。必须在 `apply_chat_template` 中设 `enable_thinking=False`。\n\n### Train/inference prompt alignment\n训练用 unified template \"Extract all structured information...\"，推理必须用完全一致的 template + schema hints。不对齐会导致模型不识别指令。\n\n### Parse failures from max_tokens truncation (2026-05-14)\nmax_tokens=512 导致 3.7% stochastic + 5.3% greedy parse failures。max_tokens=1024 完全消除了 parse failures (0/4408)。\n\n### submit_training_job 需要 tmux (2026-05-14)\nAutoDL 5090 服务器默认无 tmux。已安装 tmux 3.2a。\n\n### ft_002 nohup 崩溃教训 (2026-05-14)\nWorker 用 nohup 启动训练后退出，训练在 step 70/585 崩溃，无日志、无 checkpoint、无监控。必须用 submit_training_job（tmux + cron）确保持久化和监控。\n\n### OOM 修复：batch_size + gradient_checkpointing (2026-05-14)\nQwen3-8B LoRA r=32 在 RTX 5090 32GB 上 batch_size=4 会 OOM（step 73 崩溃）。修复：batch_size=2 + gradient_accumulation_steps=8 + gradient_checkpointing=true → 显存 82% (26.8/32.6 GB)，成功完成 585 steps。\n\n### vLLM 不能直接加载 LoRA adapter (2026-05-14)\nvLLM 需要加载 merged model（有 config.json），不能直接加载 LoRA adapter 目录。必须先用 LLaMA Factory export 或 PEFT merge 合并 adapter 到基座模型。\n\n### 训练配置必须保留 best checkpoint (2026-05-14)\nft_002_v2 的 best eval 在 ~step 300 但被 save_total_limit=3 删掉了。未来 SFT 训练配置必须加：\n```yaml\nload_best_model_at_end: true\nmetric_for_best_model: eval_loss\nsave_total_limit: 5  # 至少保证 best checkpoint 不被删\n```\n\n### E1 否定乘性惩罚假说——RE SJ 问题是根本性的 (2026-05-14)\nComponent-wise 分解结果：\n- head_sj ρ=0.210 **远低于** NER ρ_sj=0.383（Δ=-0.173）\n- **每个 component 单独都比乘性组合差**——乘性组合实际在整合三个弱信号，不是在伤害\n- additive fix 无效（additive ρ ≈ multiplicative ρ，差 0.001）\n- **根因修正**：不是\"乘性惩罚导致 RE SJ 差\"，而是 span-level SJ 对 RE 任务**根本缺乏区分力**\n- Fleiss' κ 的 surface matching 在 RE 上反而更鲁棒\n- **决策影响**：方案 B（度量分解 pivot）被排除，fallback 方案 A（NER-primary + RE 诊断）\n\n### SJ vs κ 在 NER 和 RE 上表现不对称——核心发现 (2026-05-14)\n跨 3 轮 pilot 的稳定规律：\n- **NER**: SJ 一致且显著优于 κ（delta +0.01→+0.12，p=7e-20），ρ_sj 稳定在 0.36-0.38\n- **RE**: SJ 在 full set 上 2/3 次不如 κ，ρ_sj 锁死在 ~0.24，模型质量提升（F1 35→42%）未改善 ρ\n- E1 证实：问题不在度量公式，而在 span-level SJ 对 RE 的根本适用性\n\n### RE pct_zero 统计范围 bug (2026-05-14)\nrun_mvp_pilot.py 的 `compute_sample_f1_distribution` 在 gold-empty 过滤前调用，导致 gold-empty 实例（RE 28%）被计入 pct_zero，从实际 55% 虚高到 67.6%。已修复：先按 subtask 过滤 gold-nonempty 再算 F1 分布。\n\n## 服务器环境\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\n- conda: /root/miniconda3/\n- 环境初始化: `source /etc/network_turbo && source /root/autodl-tmp/struct_self_consist_ie/env.sh`\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ (不是 /root/autodl-tmp/models/Qwen3-8B/)\n- ft_001 merged: checkpoints/qwen3-8b-scierc-merged/\n- ft_002_v2 adapter: checkpoints/qwen3-8b-scierc-lora-v2/\n- ft_002_v2 merged (final): checkpoints/qwen3-8b-scierc-merged-v2/\n- ft_002_v2 merged (ckpt400): checkpoints/qwen3-8b-scierc-merged-v2-ckpt400/ (待确认)\n- SciERC data: data/scierc/ (train.json, dev.json, test.json)\n\n## E4 NER 多数据集泛化调研报告 (2026-05-14)\n\n### 候选数据集对比表\n\n| 数据集 | 可用性 | HF Dataset ID | Entity Types | Train | Test | 领域 | 转换复杂度 | 推荐？ |\n|--------|--------|---------------|-------------|-------|------|------|-----------|--------|\n| **CoNLL-2003** | ✅ 免费 | `BramVanroy/conll2003` 或 `lhoestq/conll2003` | 4: PER, ORG, LOC, MISC | 14,041 | 3,453 | 新闻 | 简单 | ✅ **强推** |\n| **WNUT-17** | ✅ CC BY 4.0 | `leondz/wnut_17` | 6: corporation, creative-work, group, location, person, product | 3,394 | 1,287 | 社交媒体 | 简单 | ✅ **强推** |\n| **OntoNotes 5.0** | ⚠️ 官方需 LDC | `tner/ontonotes5` (社区镜像) | 18: PERSON, ORG, GPE, DATE, CARDINAL... | 59,924 | 8,262 | 新闻/广播 | 简单 | ⚠️ 许可风险 |\n| **GENIA/JNLPBA** | ✅ 免费 | `jnlpba` | 5: protein, DNA, RNA, cell_line, cell_type | 18,546 | ~3,856 | 生物医学 | 简单 | ✅ 可选 |\n| **Few-NERD** | ✅ CC BY-SA 4.0 | `DFKI-SLT/few-nerd` | 8 coarse / 66 fine | 131,767 | 37,648 | 维基百科 | 中等(IO→BIO) | ⚠️ 格式特殊 |\n| **CrossNER** | ✅ 免费 | `DFKI-SLT/cross_ner` | 5域各不同(~79 total) | 100-200/域 | 400-650/域 | 多领域 | 中等 | ⚠️ 训练集太小 |\n| **MIT Movie** | ✅ 免费 | `tner/mit_movie_trivia` | 12: Actor, Plot, Genre... | 6,816 | 1,953 | 电影查询 | 简单 | ✅ 可选 |\n| **MIT Restaurant** | ✅ 免费 | `tner/mit_restaurant` | 8: Rating, Cuisine, Dish... | 6,900 | 1,521 | 餐厅查询 | 简单 | ✅ 可选 |\n| **ACE05** | ❌ LDC | 无 | 7 | - | - | 新闻 | - | ❌ 不可行 |\n| **MultiNERD** | ⚠️ NC 许可 | `Babelscape/multinerd` | 15 | ~16K(en) | ~3.3K(en) | 维基百科 | 简单 | ⚠️ 银标+NC |\n\n### 注意事项\n\n**CoNLL-2003 HF 兼容性**：原始 `conll2003` ID 在 `datasets>=4.0` 已失效（script-based 不再支持）。必须用 `BramVanroy/conll2003` 或 `lhoestq/conll2003`（Parquet-native）。\n\n**OntoNotes 许可风险**：`tner/ontonotes5` 是社区上传的非官方镜像，严格来说侵犯 LDC 许可。reviewer 可能质疑。如果用，需要在论文中小心措辞。\n\n**数据格式统一**：所有 HF NER 数据集都是 token-level BIO 格式。转换到 UIE char-offset JSON 需要：(1) tokens → text（空格拼接），(2) 累积 char offset 追踪，(3) BIO span 提取。逻辑与现有 `data_utils.py` 的 `_token_offsets()` 一致，每个数据集 ~50 行 Python。\n\n**无现成转换器**：调研了 InstructUIE、GoLLIE、IEPile、UIE、UniversalNER、YAYI-UIE——没有任何项目输出我们需要的 `{text, type, start, end}` char-offset JSON 格式。都是 text-only 或 token-offset。需要自己写转换脚本。\n\n### 推荐方案\n\n**方案：SciERC + CoNLL-2003 + WNUT-17（3 数据集，3 领域）**\n\n| 维度 | SciERC | CoNLL-2003 | WNUT-17 |\n|------|--------|------------|---------|\n| 领域 | 科学论文 | 新闻 | 社交媒体 |\n| Entity Types | 6 (科学) | 4 (通用) | 6 (新兴) |\n| Test Size | 551 | 3,453 | 1,287 |\n| 难度 | 中 | 低 | 高(噪声) |\n\n**选择理由**：\n1. **领域多样性**：科学 → 新闻 → 社交媒体，三个完全不同的文本分布\n2. **全部免费无许可风险**：CoNLL-2003 虽然理论上有 Reuters 限制，但实践中所有 NER 论文都直接用，reviewer 不会质疑\n3. **Entity type 多样性**：科学术语 vs 通用实体 vs 新兴/噪声实体\n4. **CoNLL-2003 是 NER 标杆**：不用它反而会被 reviewer 质疑\n5. **WNUT-17 增加挑战性**：社交媒体噪声文本 + 新兴实体，如果 SJ 在这种难设定下仍有效，说服力极强\n6. **可选第 4 个**：如果时间允许，加 GENIA（生物医学）做第 4 领域\n\n### Evaluation 兼容性\n\n现有 `entity_strict_match` 完全通用——用 `(start, end, type)` 元组匹配，不绑定任何特定 entity type。无需修改。\n\n需要修改的：\n- `sampling.py` 中的 **schema hint**：每个数据集需要自己的 entity type 列表（类似 `SCIERC_SCHEMA_HINT`）\n- **prompt template**：可复用现有 unified template，只换 schema hint 行\n- `data_utils.py`：新增 `convert_conll2003()` 和 `convert_wnut17()` 函数\n\n### Fine-tuning 策略\n\n**Per-dataset fine-tune**（推荐）：\n- 每个数据集独立训练 Qwen3-8B LoRA adapter\n- 这样每个数据集的 SJ correlation 是独立证据，更有说服力\n- CoNLL-2003 训练集 14K 条，比 SciERC 1.8K 大很多，可能需要 subsample 或更多 steps\n\n**Zero-shot 不可行**：SciERC entity types (Method, Task...) 与 CoNLL (PER, ORG...) 完全不同，zero-shot 没有意义。\n\n### 时间估算\n\n| 步骤 | 耗时 | 备注 |\n|------|------|------|\n| 写 BIO→UIE 转换脚本 | 2-3h | CoNLL + WNUT 共用框架 |\n| 生成 sharegpt 训练数据 | 1-2h | 复用现有 sharegpt 生成逻辑 |\n| CoNLL fine-tune | 3-5h | 14K 条，可能需 2-3 epoch |\n| WNUT fine-tune | 1-2h | 3.4K 条，类似 SciERC |\n| Model merge (×2) | 0.5h | |\n| Sampling + eval (×2) | 3-4h | 每数据集 8 samples × test set |\n| 分析 SJ correlation | 1-2h | 复用现有分析脚本 |\n| **总计** | **~2-3 天** | 可并行训练 |\n\n### 风险/Blockers\n\n1. **CoNLL-2003 训练集过大 (14K)**：可能导致训练时间长。可 subsample 到 ~5K 或减少 epoch。\n2. **WNUT-17 噪声文本**：社交媒体缩写/hashtag/非标准拼写可能导致 NER F1 较低，但这正是我们想测的。\n3. **Schema hint 设计**：每个数据集的 entity type 命名需要统一规范（如 CoNLL 用 PER/ORG/LOC/MISC 还是 Person/Organization/Location/Miscellaneous）。\n4. **Offset hallucination 可能更严重**：CoNLL 的长句子可能导致更多 offset 错误，但 span realignment 应能处理。\n5. **时间紧张**：DDL 2026-05-25，只剩 11 天。2-3 天做多数据集实验是可行的，但需要并行操作。\n"
  }
}
````

</details>

---

### Tool result

_source line 254 · 2026-05-14T09:34:41.958428+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_e4_dataset_survey_20260514T092619",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 255 · 2026-05-14T09:34:41.958598+00:00_

报告已保存到 `memory.md`。核心结论：

**推荐方案：SciERC + CoNLL-2003 + WNUT-17**

- **CoNLL-2003**（新闻，4 types，3.4K test）— NER 标杆数据集，免费，HF 用 `BramVanroy/conll2003`
- **WNUT-17**（社交媒体，6 types，1.3K test）— 噪声文本+新兴实体，SJ 在此设定有效则说服力极强

三个数据集覆盖科学/新闻/社交媒体三个领域，entity types 完全不同。

**关键发现**：
- 现有 `entity_strict_match` 完全通用，无需改
- 无现成 char-offset JSON 转换器（调研了 6 个项目），需自写 ~50 行/数据集
- Per-dataset fine-tune 是唯一合理策略（entity types 不重叠）
- **总工时 ~2-3 天**，DDL 前可完成

**风险**：CoNLL 训练集 14K 条偏大（可 subsample）；OntoNotes 有许可风险不推荐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_e4_dataset_survey_20260514T092619"
}
```

</details>

---
