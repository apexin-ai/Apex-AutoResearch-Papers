# Research conversation: Search the codebase for "submit_dream_review_report" — it might be a Python function, an MCP tool handler, or referenced

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab2395d53af5bcdca.jsonl`
- **Structured JSON:** [`2e60ee343da0ea862e36.json`](../../sessions/2e/2e60ee343da0ea862e36.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-12T20:38:09.776Z_

Search the codebase for "submit_dream_review_report" — it might be a Python function, an MCP tool handler, or referenced in any config/skill file. Search in /home/ubuntu/agent-ml-research/ and /home/ubuntu/.agent-ml-research-idea_gen_0509_7/. Return all file paths and the relevant code snippets showing how this function works (what it writes, where, what parameters it takes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "c1704c28-4b23-4ab0-bb0b-b724cb83c995",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-12T20:38:11.107Z_

I'll search for "submit_dream_review_report" across the specified directories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1704c28-4b23-4ab0-bb0b-b724cb83c995",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSL6jGUtsQUZZjUYUH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "259f133d-2f57-4b50-a6df-3ac058415341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LnE2GsvdTSBjYHQZWMhLuq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 35367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 524,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T20:38:11.733Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012NVMutH3LbeUr9iTruWSwP`</summary>

```json
{
  "pattern": "submit_dream_review_report",
  "path": "/home/ubuntu/agent-ml-research",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "259f133d-2f57-4b50-a6df-3ac058415341",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSL6jGUtsQUZZjUYUH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eaad22eb-c0ac-45fb-9ff8-57854ddb2416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LnE2GsvdTSBjYHQZWMhLuq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 35367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 524,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T20:38:11.790Z_

<details><summary>↩ Tool result · `toolu_012NVMutH3LbeUr9iTruWSwP`</summary>

```text
Found 19 files
/home/ubuntu/agent-ml-research/tests/test_dream_isolation_full.py
/home/ubuntu/agent-ml-research/docs/plans/DREAM_FEEDBACK_ACTION_PROTOCOL.md
/home/ubuntu/agent-ml-research/core/tools/dream.py
/home/ubuntu/agent-ml-research/core/session_server.py
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/session_claude_md.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_visible.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_artifacts_isolation.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_report_delivery.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py
/home/ubuntu/agent-ml-research/tests/test_dream_review_simple.py
/home/ubuntu/agent-ml-research/skills/global/dream-review-full.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-review-simple.skill.md
/home/ubuntu/agent-ml-research/docs/plans/DREAM_AGENT_DESIGN.md
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py
/home/ubuntu/agent-ml-research/core/tool_registry.py
/home/ubuntu/agent-ml-research/TEST.md
/home/ubuntu/agent-ml-research/PROGRESS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaad22eb-c0ac-45fb-9ff8-57854ddb2416",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "920fd509-8bbe-4c71-8398-818a1aba8f3f",
  "sourceToolAssistantUUID": "eaad22eb-c0ac-45fb-9ff8-57854ddb2416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T20:38:11.929Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GKwQq5ZmzYurbCuv3ZUZTF`</summary>

```json
{
  "pattern": "submit_dream_review_report",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "920fd509-8bbe-4c71-8398-818a1aba8f3f",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSL6jGUtsQUZZjUYUH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f27b2970-e3ad-40c3-a47a-dbace7a8d7c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LnE2GsvdTSBjYHQZWMhLuq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 35367,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 524
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 225,
          "cache_read_input_tokens": 35367,
          "cache_creation_input_tokens": 524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 524,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T20:38:11.958Z_

<details><summary>↩ Tool result · `toolu_01GKwQq5ZmzYurbCuv3ZUZTF`</summary>

```text
Found 1 file
artifacts/dream_reports/dream_20260512T200328/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f27b2970-e3ad-40c3-a47a-dbace7a8d7c1",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "d09abff6-ba02-41d6-a1ad-91760b7e8c30",
  "sourceToolAssistantUUID": "f27b2970-e3ad-40c3-a47a-dbace7a8d7c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-12T20:38:13.122Z_

Now let me read the key implementation files to understand how this function works:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d09abff6-ba02-41d6-a1ad-91760b7e8c30",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSVDfQ6xQs2WTAgfSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f660a707-cda9-4373-946d-3cf766805046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPcJFfgqcepRUdqMyyVVBd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 35891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1575,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T20:38:13.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KNe2Tj24zWtDGuNFvCyyh1`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/dream.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f660a707-cda9-4373-946d-3cf766805046",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSVDfQ6xQs2WTAgfSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be082f04-2318-4df4-bbce-a71f8fa62c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPcJFfgqcepRUdqMyyVVBd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 35891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1575,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T20:38:13.597Z_

<details><summary>↩ Tool result · `toolu_01KNe2Tj24zWtDGuNFvCyyh1`</summary>

````text
1	"""Dream Tool — async two-phase imagined-experiment simulator.
2	
3	End-to-end pipeline (see ``docs/plans/DREAM_AGENT_DESIGN.md`` §7.1):
4	
5	    dream_simulate()          # sync entry — registers + spawns orchestrator,
6	        │                     # returns DreamHandle immediately
7	        ▼
8	    _run_dream_pipeline()     # async orchestrator (independent OS process):
9	        │
10	        ├─ _collect_context()      # framing.md + plan + registry → str
11	        ├─ _define_tiers()         # Phase 1 — 1 subprocess, 3 tier defs
12	        ├─ for tier in tiers:
13	        │     ├─ _elaborate_scenario()  # Phase 2 per-tier subprocess
14	        │     ├─ _write_dream_paper()   # Paper Agent (Dream mode) — emits PDF
15	        │     └─ _submit_to_review()    # Group C Dream review
16	        ├─ _persist_report()       # writes meta.yaml + symlink latest →
17	        └─ dispatch_dream_done()   # inject Director session + A-group summary
18	
19	Status is mirrored at every step into ``dream_registry.yaml`` so callers can
20	poll via :func:`get_dream_status` even across BE restarts. Failures inside any
21	sub-step degrade the corresponding tier (set ``error`` on its
22	``DreamScenarioResult``) but keep the remaining tiers running — never abort
23	the whole pipeline because one subprocess crashed.
24	
25	This module deliberately keeps the LLM calls behind small functions so tests
26	can stub them with :func:`unittest.mock.patch`. Anything that hits the file
27	system goes through :mod:`core.paths` — no hard-coded ``~/.agent-ml-research``.
28	"""
29	
30	from __future__ import annotations
31	
32	import asyncio
33	import hashlib
34	import json
35	import logging
36	import os
37	import re
38	import sys
39	import threading
40	from contextlib import suppress
41	from datetime import datetime, timezone
42	from pathlib import Path
43	from typing import Any, Iterable
44	
45	import yaml
46	
47	from core import dream_registry as _registry
48	from core import paths as _paths
49	from core.dream_types import (
50	    DreamHandle,
51	    DreamInput,
52	    DreamOutput,
53	    DreamScenarioResult,
54	    ImaginedExperiment,
55	    ImaginedScenario,
56	    TierDefinition,
57	    TierDefinitions,
58	    WhatIfExperiment,
59	)
60	from core.tools.result import ToolResult
61	
62	logger = logging.getLogger(__name__)
63	
64	
65	# ---------------------------------------------------------------------------
66	# Constants
67	# ---------------------------------------------------------------------------
68	
69	TIERS: tuple[str, str, str] = ("best", "median", "worst")
70	
71	# Hard timeouts so a stuck Claude subprocess never freezes the pipeline.
72	_PHASE1_TIMEOUT_S = 600     # 10 min: defining three tiers is short-form
73	_PHASE2_TIMEOUT_S = 1800    # 30 min: per-tier elaboration is longer
74	_WRITE_TIMEOUT_S = 5400     # 90 min: Paper Agent Dream mode
75	_REVIEW_TIMEOUT_S = 3600    # 60 min: Group C Dream review
76	
77	# Cap on YAML retries when the LLM emits malformed output.
78	_YAML_PARSE_RETRIES = 1
79	
80	
81	# ---------------------------------------------------------------------------
82	# Helpers
83	# ---------------------------------------------------------------------------
84	
85	
86	def _now_iso() -> str:
87	    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
88	
89	
90	def _new_dream_id() -> str:
91	    return f"dream_{_now_iso()}"
92	
93	
94	def _extract_yaml_block(text: str) -> str:
95	    """Pull the first ```yaml fenced block (or the raw text) out of a string.
96	
97	    LLM output often wraps YAML in markdown fences; without stripping them
98	    ``yaml.safe_load`` fails on the leading "```yaml" line.
99	    """
100	    if not text:
101	        return ""
102	    m = re.search(r"```(?:yaml|yml)?\s*\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
103	    if m:
104	        return m.group(1).strip()
105	    return text.strip()
106	
107	
108	def _read_framing(project: str) -> str:
109	    """Return the contents of ``paper_framing.md`` or an empty string."""
110	    path = _paths.resolve_project_file(project, "paper_framing.md")
111	    if not path.exists():
112	        return ""
113	    try:
114	        return path.read_text(encoding="utf-8")
115	    except OSError:
116	        logger.warning("[dream] could not read framing %s", path, exc_info=True)
117	        return ""
118	
119	
120	def _read_plan(project: str) -> list[dict[str, Any]]:
121	    """Read experiment_plan.yaml entries with live registry status overlaid."""
122	    try:
123	        from core.tools.experiment_plan import read_experiment_plan_with_status
124	    except Exception:
125	        return []
126	    res = read_experiment_plan_with_status(project)
127	    if not res.success or not res.data:
128	        return []
129	    return list(res.data.get("experiments") or [])
130	
131	
132	def _read_registry_summary(project: str) -> list[dict[str, Any]]:
133	    """Compact registry view for context — only the fields Dream needs."""
134	    try:
135	        from core.tools.registry import get_registry_path
136	    except Exception:
137	        return []
138	    path = get_registry_path(project)
139	    if not path.exists():
140	        return []
141	    try:
142	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
143	    except Exception:
144	        logger.warning("[dream] could not parse registry %s", path, exc_info=True)
145	        return []
146	    out: list[dict[str, Any]] = []
147	    for exp_id, entry in (data.get("experiments") or {}).items():
148	        if not isinstance(entry, dict):
149	            continue
150	        out.append({
151	            "exp_id": exp_id,
152	            "name": entry.get("name", ""),
153	            "status": entry.get("status", ""),
154	            "conclusion": entry.get("conclusion", ""),
155	            "metrics": entry.get("metrics", {}),
156	        })
157	    return out
158	
159	
160	def _project_dream_config(project: str) -> dict[str, Any]:
161	    """Best-effort fetch of project-level Dream defaults (review_visible etc.)."""
162	    try:
163	        from core.tools.project_config import get_dream_config
164	    except Exception:
165	        return {}
166	    try:
167	        return get_dream_config(project) or {}
168	    except Exception:
169	        return {}
170	
171	
172	# ---------------------------------------------------------------------------
173	# Smart skip + trend tracking (DREAM_AGENT_DESIGN §8.4 + §4-5/4-6)
174	# ---------------------------------------------------------------------------
175	
176	# Experiment statuses whose presence/results "count" as research progress for
177	# smart_skip purposes. Anything earlier in the pipeline (PREPARING/QUEUED) is
178	# still in-flight and doesn't change the conclusions a Dream would draw.
179	_SMART_SKIP_RELEVANT_STATUSES = ("ANALYZING", "DONE", "DEPLOYING", "DEPLOYED")
180	
181	
182	def _canonical_metric_fingerprint(metrics: Any) -> Any:
183	    """Return a JSON-safe, deterministic view of an experiment's metrics.
184	
185	    YAML reads can yield ``None`` / nested dicts in arbitrary key order; the
186	    hash must not flip just because the YAML writer reordered keys. We sort
187	    keys recursively and coerce non-primitive values to ``repr`` so the
188	    fingerprint is stable across runs and Python versions.
189	    """
190	    if metrics is None:
191	        return None
192	    if isinstance(metrics, dict):
193	        return {k: _canonical_metric_fingerprint(metrics[k]) for k in sorted(metrics)}
194	    if isinstance(metrics, (list, tuple)):
195	        return [_canonical_metric_fingerprint(v) for v in metrics]
196	    if isinstance(metrics, (str, int, float, bool)):
197	        return metrics
198	    return repr(metrics)
199	
200	
201	def _context_fingerprint(
202	    *,
203	    project: str,
204	    what_if: list[WhatIfExperiment] | list[dict] | None = None,
205	) -> dict[str, Any]:
206	    """Build the structured input that ``_compute_context_hash`` hashes.
207	
208	    Includes only the fields a Dream actually reads:
209	      • paper_framing.md raw text
210	      • experiment_plan.yaml entries (read via plan helper so registry status
211	        is overlaid)
212	      • registry entries in statuses that affect Dream conclusions (ANALYZING
213	        and later); their metrics fingerprint is included
214	      • the what_if list (so two cron calls with identical framing but
215	        different what_if don't accidentally share a hash)
216	    """
217	    framing = _read_framing(project)
218	    plan = _read_plan(project)
219	    registry = _read_registry_summary(project)
220	    relevant_reg = [
221	        {
222	            "exp_id": e.get("exp_id", ""),
223	            "status": e.get("status", ""),
224	            "conclusion": e.get("conclusion", ""),
225	            "metrics": _canonical_metric_fingerprint(e.get("metrics")),
226	        }
227	        for e in registry
228	        if str(e.get("status", "")).upper() in _SMART_SKIP_RELEVANT_STATUSES
229	    ]
230	    relevant_reg.sort(key=lambda e: e["exp_id"])
231	
232	    what_if_list: list[dict[str, Any]] = []
233	    for w in (what_if or []):
234	        if isinstance(w, WhatIfExperiment):
235	            what_if_list.append(w.to_dict())
236	        elif isinstance(w, dict):
237	            what_if_list.append(dict(w))
238	    what_if_list.sort(key=lambda d: d.get("name", ""))
239	
240	    return {
241	        "framing": framing,
242	        "experiment_plan": plan,
243	        "registry": relevant_reg,
244	        "what_if": what_if_list,
245	    }
246	
247	
248	def _compute_context_hash(
249	    project: str,
250	    *,
251	    what_if: list[WhatIfExperiment] | list[dict] | None = None,
252	) -> str:
253	    """SHA-256 of the canonical context fingerprint.
254	
255	    Used for smart_skip: when this hash equals the hash recorded on the most
256	    recent ``done`` dream, the research state hasn't changed and a re-run
257	    would just burn pool quota.
258	    """
259	    fp = _context_fingerprint(project=project, what_if=what_if)
260	    blob = json.dumps(fp, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
261	    return hashlib.sha256(blob).hexdigest()
262	
263	
264	def should_skip_dream(
265	    project: str,
266	    *,
267	    what_if: list[dict] | None = None,
268	) -> ToolResult:
269	    """Decide whether to skip a Dream run because nothing has changed.
270	
271	    Compares the current context hash against the most recent ``done`` dream
272	    in the registry. Mirrors the heuristic in ``dream-cron.skill.md``:
273	
274	      • No prior ``done`` dream → don't skip (let the cron run).
275	      • Prior dream's ``context_hash`` matches → skip; surface its id so the
276	        Director can reuse its report.
277	      • Hash differs → don't skip.
278	
279	    Returns:
280	        ToolResult.data = {
281	            "skip": bool,
282	            "reason": "context_unchanged" | "context_changed" | "no_prior_dream"
283	                      | "smart_skip_disabled",
284	            "current_hash": str,
285	            "last_dream_id": str,         # populated when skip=True
286	            "last_dream_dir": str,        # absolute path
287	            "last_completed_at": str,
288	        }
289	    """
290	    if not project:
291	        return ToolResult(success=False, error="project is required")
292	
293	    cfg = _project_dream_config(project)
294	    if not bool(cfg.get("smart_skip", True)):
295	        return ToolResult(
296	            success=True,
297	            data={
298	                "skip": False,
299	                "reason": "smart_skip_disabled",
300	                "current_hash": "",
301	            },
302	        )
303	
304	    current_hash = _compute_context_hash(project, what_if=[
305	        WhatIfExperiment.from_dict(w) for w in (what_if or [])
306	    ])
307	
308	    # Find the latest 'done' dream — list_dreams returns newest first.
309	    dreams = _registry.list_dreams(project, status="done")
310	    if not dreams:
311	        return ToolResult(
312	            success=True,
313	            data={
314	                "skip": False,
315	                "reason": "no_prior_dream",
316	                "current_hash": current_hash,
317	            },
318	        )
319	    prior = dreams[0]
320	    prior_hash = prior.get("context_hash") or ""
321	
322	    if prior_hash and prior_hash == current_hash:
323	        return ToolResult(
324	            success=True,
325	            data={
326	                "skip": True,
327	                "reason": "context_unchanged",
328	                "current_hash": current_hash,
329	                "last_dream_id": prior.get("dream_id", ""),
330	                "last_dream_dir": str(
331	                    _paths.dream_report_dir(project, prior.get("dream_id", ""))
332	                ) if prior.get("dream_id") else "",
333	                "last_completed_at": prior.get("updated_at") or prior.get("started_at") or "",
334	            },
335	        )
336	
337	    return ToolResult(
338	        success=True,
339	        data={
340	            "skip": False,
341	            "reason": "context_changed",
342	            "current_hash": current_hash,
343	            "last_dream_id": prior.get("dream_id", ""),
344	            "last_completed_at": prior.get("updated_at") or prior.get("started_at") or "",
345	        },
346	    )
347	
348	
349	def _summarize_meta_for_trend(meta: dict[str, Any]) -> dict[str, Any]:
350	    """Strip a dream's meta.yaml to the fields that matter for trend tracking.
351	
352	    Predictions are reduced to ``{tier: {experiment_name: expected_results}}``
353	    so the delta diff can highlight which numbers moved between dreams.
354	    """
355	    scenarios = meta.get("scenarios") or []
356	    per_tier: dict[str, dict[str, Any]] = {}
357	    for s in scenarios:
358	        if not isinstance(s, dict):
359	            continue
360	        tier = s.get("tier") or ""
361	        if not tier:
362	            continue
363	        exps_pred: dict[str, dict[str, Any]] = {}
364	        for exp in s.get("imagined_experiments") or []:
365	            if not isinstance(exp, dict):
366	                continue
367	            name = exp.get("name") or ""
368	            if not name:
369	                continue
370	            exps_pred[name] = dict(exp.get("expected_results") or {})
371	        per_tier[tier] = {
372	            "n_experiments": len(s.get("imagined_experiments") or []),
373	            "pdf_path": s.get("pdf_path", ""),
374	            "error": s.get("error", ""),
375	            "predictions": exps_pred,
376	        }
377	    return {
378	        "dream_id": meta.get("dream_id", ""),
379	        "created_at": meta.get("created_at", ""),
380	        "venue": meta.get("venue", ""),
381	        "focus": meta.get("focus", ""),
382	        "review_mode": meta.get("review_mode", ""),
383	        "what_if": meta.get("what_if") or [],
384	        "tiers": per_tier,
385	    }
386	
387	
388	def _diff_predictions(prev: dict[str, Any], curr: dict[str, Any]) -> dict[str, Any]:
389	    """Compare two ``_summarize_meta_for_trend`` results, return per-tier deltas.
390	
391	    For each tier, returns the experiments whose ``expected_results`` differ
392	    between the two dreams (added / removed / changed). Useful to see "what
393	    moved" without re-reading two full meta.yaml files.
394	    """
395	    out: dict[str, Any] = {}
396	    tiers = set(prev.get("tiers", {})) | set(curr.get("tiers", {}))
397	    for tier in sorted(tiers):
398	        prev_preds = (prev.get("tiers", {}).get(tier) or {}).get("predictions", {})
399	        curr_preds = (curr.get("tiers", {}).get(tier) or {}).get("predictions", {})
400	        added = sorted(set(curr_preds) - set(prev_preds))
401	        removed = sorted(set(prev_preds) - set(curr_preds))
402	        changed: list[dict[str, Any]] = []
403	        for name in sorted(set(prev_preds) & set(curr_preds)):
404	            if prev_preds[name] != curr_preds[name]:
405	                changed.append({
406	                    "experiment": name,
407	                    "before": prev_preds[name],
408	                    "after": curr_preds[name],
409	                })
410	        if added or removed or changed:
411	            out[tier] = {"added": added, "removed": removed, "changed": changed}
412	    return out
413	
414	
415	def get_dream_trend(project: str, limit: int = 5) -> ToolResult:
416	    """Return the last ``limit`` completed dreams + per-tier prediction deltas.
417	
418	    Reads each dream's persisted ``meta.yaml`` so the trend reflects the
419	    actual reports, not just registry status. Failed / incomplete dreams are
420	    included so the Director can see "predictions stalled here".
421	
422	    Returns:
423	        ToolResult.data = {
424	            "trend": [&lt;summary>, ...],   # newest first
425	            "deltas": [                   # consecutive-pair diffs
426	                {"from": &lt;older_id>, "to": &lt;newer_id>, "diff": {...}}, ...
427	            ],
428	        }
429	    """
430	    if not project:
431	        return ToolResult(success=False, error="project is required")
432	    if not isinstance(limit, int) or limit <= 0:
433	        return ToolResult(success=False, error="limit must be a positive int")
434	
435	    # Pull all dreams (any status), keep registry order which is newest-first.
436	    dreams = _registry.list_dreams(project)
437	    trend: list[dict[str, Any]] = []
438	    for entry in dreams:
439	        if len(trend) >= limit:
440	            break
441	        dream_id = entry.get("dream_id", "")
442	        if not dream_id:
443	            continue
444	        meta_path = _paths.dream_report_dir(project, dream_id) / "meta.yaml"
445	        if not meta_path.exists():
446	            # Dream registered but report not yet written (still imagining,
447	            # or crashed). Surface the registry state so the trend is honest.
448	            trend.append({
449	                "dream_id": dream_id,
450	                "created_at": entry.get("started_at", ""),
451	                "status": entry.get("status", ""),
452	                "error": entry.get("error") or "",
453	                "tiers": {},
454	            })
455	            continue
456	        try:
457	            meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
458	        except Exception:
459	            logger.warning("[dream] could not parse meta.yaml for %s", dream_id, exc_info=True)
460	            continue
461	        summary = _summarize_meta_for_trend(meta)
462	        summary["status"] = entry.get("status", "done")
463	        trend.append(summary)
464	
465	    # Consecutive deltas: pair newer (index i) with older (index i+1).
466	    deltas: list[dict[str, Any]] = []
467	    for i in range(len(trend) - 1):
468	        newer, older = trend[i], trend[i + 1]
469	        if not newer.get("tiers") or not older.get("tiers"):
470	            continue
471	        diff = _diff_predictions(older, newer)
472	        if diff:
473	            deltas.append({
474	                "from": older.get("dream_id", ""),
475	                "to": newer.get("dream_id", ""),
476	                "diff": diff,
477	            })
478	
479	    return ToolResult(success=True, data={"trend": trend, "deltas": deltas})
480	
481	
482	# ---------------------------------------------------------------------------
483	# Step 1 — _collect_context (2-3)
484	# ---------------------------------------------------------------------------
485	
486	
487	def _collect_context(
488	    *,
489	    project: str,
490	    what_if: list[WhatIfExperiment] | None = None,
491	    venue: str = "",
492	    focus: str = "",
493	) -> dict[str, Any]:
494	    """Assemble all read-only inputs for Phase 1/2.
495	
496	    Returns a dict so callers can pass it to the LLM prompts verbatim and so
497	    tests can assert on individual fields. Never raises — missing files
498	    degrade to empty strings/lists. Validation (e.g. "framing must exist") is
499	    the caller's job, not this collector's.
500	    """
501	    framing = _read_framing(project)
502	    plan = _read_plan(project)
503	    registry = _read_registry_summary(project)
504	    dream_cfg = _project_dream_config(project)
505	
506	    return {
507	        "project": project,
508	        "venue": venue or "",
509	        "focus": focus or "",
510	        "framing": framing,
511	        "experiment_plan": plan,
512	        "registry": registry,
513	        "what_if": [w.to_dict() if isinstance(w, WhatIfExperiment) else dict(w) for w in (what_if or [])],
514	        "dream_config": dream_cfg,
515	    }
516	
517	
518	# ---------------------------------------------------------------------------
519	# Prompts (kept as module-level constants so they can be inspected in tests)
520	# ---------------------------------------------------------------------------
521	
522	
523	_PHASE1_PROMPT = """你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。
524	
525	你需要同时定义 best / median / worst 三档：
526	1. 每档的核心假设（哪些假设成立/不成立）
527	2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
528	3. 每档的论文叙事方向——
529	   - best: 原始 framing 可以支撑
530	   - median: 需要怎么调整 claims
531	   - worst: 需要怎么重构 story（可能从 method paper 变成 analysis paper）
532	
533	三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
534	自行判断。但必须确保三档之间的数字和叙事逻辑一致。
535	
536	# Project context
537	{context_block}
538	
539	# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）
540	
541	```yaml
542	tiers:
543	  best:
544	    meaning: "..."
545	    key_assumptions: [...]
546	    number_ranges: {{metric_a: [low, high], metric_b: [...]}}
547	    narrative_direction: "..."
548	  median:
549	    meaning: "..."
550	    ...
551	  worst:
552	    meaning: "..."
553	    ...
554	```
555	"""
556	
557	
558	_PHASE2_PROMPT = """你是一位经验丰富的 ML 研究者。Phase 1 已定义了 {tier} 档的含义：
559	
560	含义：{meaning}
561	核心假设：{assumptions}
562	关键指标范围：{number_ranges}
563	叙事方向：{narrative_direction}
564	
565	基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
566	每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。
567	
568	# Project context
569	{context_block}
570	
571	# 输出格式（YAML，仅输出一个 ```yaml 块）
572	
573	```yaml
574	tier: {tier}
575	narrative_guidance: "..."
576	imagined_experiments:
577	  - name: "..."
578	    plan_id: "..."
579	    description: "..."
580	    expected_results: {{metric: value, ...}}
581	    result_rationale: "..."
582	    tables: []
583	    figures_description: []
584	    analysis: "..."
585	```
586	"""
587	
588	
589	def _context_block(context: dict[str, Any]) -> str:
590	    """Serialize the collected context into a single LLM-readable block."""
591	    lines: list[str] = []
592	    lines.append(f"project: {context.get('project', '')}")
593	    if context.get("venue"):
594	        lines.append(f"venue: {context['venue']}")
595	    if context.get("focus"):
596	        lines.append(f"focus: {context['focus']}")
597	    framing = context.get("framing") or ""
598	    if framing:
599	        lines.append("\n## paper_framing.md\n")
600	        lines.append(framing)
601	    plan = context.get("experiment_plan") or []
602	    if plan:
603	        lines.append("\n## experiment_plan (with registry status)\n")
604	        lines.append(yaml.safe_dump(plan, allow_unicode=True, sort_keys=False))
605	    registry = context.get("registry") or []
606	    if registry:
607	        lines.append("\n## registry (completed experiments)\n")
608	        lines.append(yaml.safe_dump(registry, allow_unicode=True, sort_keys=False))
609	    what_if = context.get("what_if") or []
610	    if what_if:
611	        lines.append("\n## what_if (hypothetical experiments — additive)\n")
612	        lines.append(yaml.safe_dump(what_if, allow_unicode=True, sort_keys=False))
613	    return "\n".join(lines).strip()
614	
615	
616	# ---------------------------------------------------------------------------
617	# LLM subprocess (Claude-pool aware)
618	# ---------------------------------------------------------------------------
619	
620	
621	def _run_llm(prompt: str, *, project: str, timeout_s: int, log_path: Path | None = None) -> str:
622	    """Run a Claude subprocess with the same Pool/Backend wiring as workers.
623	
624	    Returns the raw stdout text. Subprocess timeout is enforced; on timeout
625	    the process is killed and an empty string is returned (callers should
626	    treat empty output as a parse failure).
627	
628	    The function is synchronous so tests can patch it without dealing with
629	    asyncio; the orchestrator wraps it with ``asyncio.to_thread`` to keep
630	    Phase 2 parallelism cheap.
631	    """
632	    from core.backends import get_backend
633	    from core.model_resolver import resolve_model_for_session
634	
635	    backend = get_backend(project=project or None)
636	    if not backend.pool_enabled():
637	        raise RuntimeError("Dream requires Claude pool to be enabled.")
638	    config_dir = backend.pool_select()
639	    if not config_dir:
640	        raise RuntimeError("Dream could not acquire a pool account — none healthy.")
641	    cmd = backend.build_command(
642	        prompt=prompt,
643	        mcp_config=None,
644	        model=resolve_model_for_session(project=project or None),
645	    )
646	    env = backend.make_env(config_dir=config_dir)
647	    backend.prepare_mcp(None, env=env, cwd=str(_paths.WORKSPACE_ROOT))
648	
649	    if log_path is not None:
650	        log_path.parent.mkdir(parents=True, exist_ok=True)
651	        log_fh = log_path.open("wb")
652	    else:
653	        log_fh = None
654	
655	    try:
656	        import subprocess  # local import keeps top-of-file noise down
657	        proc = subprocess.Popen(
658	            cmd,
659	            stdout=subprocess.PIPE if log_fh is None else log_fh,
660	            stderr=subprocess.STDOUT,
661	            env=env,
662	            cwd=str(_paths.WORKSPACE_ROOT),
663	            start_new_session=True,
664	        )
665	        try:
666	            stdout_bytes, _ = proc.communicate(timeout=timeout_s)
667	        except subprocess.TimeoutExpired:
668	            logger.warning("[dream] LLM subprocess pid=%s timed out after %ds", proc.pid, timeout_s)
669	            with suppress(ProcessLookupError):
670	                proc.kill()
671	                proc.communicate()
672	            return ""
673	        if log_fh is not None:
674	            # log was streamed directly to the file — read it back
675	            with suppress(OSError):
676	                stdout_bytes = log_path.read_bytes()
677	    finally:
678	        if log_fh is not None:
679	            log_fh.close()
680	
681	    text = (stdout_bytes or b"").decode("utf-8", errors="replace")
682	    # The backend writes stream-json; extract the final assistant text so the
683	    # caller's YAML parser sees the actual content, not envelope frames.
684	    final = backend.extract_last_assistant_text(text) if text else ""
685	    return final or text
686	
687	
688	# ---------------------------------------------------------------------------
689	# Phase 1 — _define_tiers (2-4)
690	# ---------------------------------------------------------------------------
691	
692	
693	def _validate_tier_definitions(data: Any) -> TierDefinitions:
694	    """Strict parse for Phase 1 output — raises ValueError on shape errors."""
695	    if not isinstance(data, dict):
696	        raise ValueError("Phase 1 output must be a mapping")
697	    tiers_raw = data.get("tiers")
698	    if not isinstance(tiers_raw, dict):
699	        raise ValueError("Phase 1 output missing 'tiers' mapping")
700	    tiers: dict[str, TierDefinition] = {}
701	    for name in TIERS:
702	        entry = tiers_raw.get(name)
703	        if not isinstance(entry, dict):
704	            raise ValueError(f"Phase 1 missing tier '{name}'")
705	        tiers[name] = TierDefinition.from_dict({"tier": name, **entry})
706	    return TierDefinitions(tiers=tiers)
707	
708	
709	def _define_tiers(context: dict[str, Any], *, log_dir: Path | None = None) -> TierDefinitions:
710	    """Phase 1: single subprocess, three coherent tier definitions.
711	
712	    Retries once on YAML parse failure. On persistent failure raises
713	    ``ValueError`` so the orchestrator can mark the dream as failed without
714	    burning further token budget.
715	    """
716	    prompt = _PHASE1_PROMPT.format(context_block=_context_block(context))
717	    last_err: Exception | None = None
718	    for attempt in range(_YAML_PARSE_RETRIES + 1):
719	        log_path = (log_dir / f"phase1_attempt{attempt}.log") if log_dir else None
720	        try:
721	            raw = _run_llm(
722	                prompt,
723	                project=context.get("project", ""),
724	                timeout_s=_PHASE1_TIMEOUT_S,
725	                log_path=log_path,
726	            )
727	        except Exception as e:
728	            last_err = e
729	            logger.warning("[dream] Phase 1 subprocess failed (attempt %d): %s", attempt, e)
730	            continue
731	        if not raw:
732	            last_err = ValueError("Phase 1 LLM returned empty output")
733	            continue
734	        try:
735	            data = yaml.safe_load(_extract_yaml_block(raw))
736	            return _validate_tier_definitions(data)
737	        except Exception as e:
738	            last_err = e
739	            logger.warning("[dream] Phase 1 parse failed (attempt %d): %s", attempt, e)
740	    raise ValueError(f"Phase 1 failed: {last_err}")
741	
742	
743	# ---------------------------------------------------------------------------
744	# Phase 2 — _elaborate_scenario (2-5)
745	# ---------------------------------------------------------------------------
746	
747	
748	def _validate_imagined_scenario(data: Any, *, tier: str) -> ImaginedScenario:
749	    if not isinstance(data, dict):
750	        raise ValueError("Phase 2 output must be a mapping")
751	    if data.get("tier") and data["tier"] != tier:
752	        raise ValueError(f"Phase 2 tier mismatch (expected {tier!r}, got {data.get('tier')!r})")
753	    exps_raw = data.get("imagined_experiments")
754	    if not isinstance(exps_raw, list) or not exps_raw:
755	        raise ValueError("Phase 2 missing 'imagined_experiments'")
756	    experiments: list[ImaginedExperiment] = []
757	    for entry in exps_raw:
758	        if not isinstance(entry, dict):
759	            raise ValueError("imagined_experiments contains non-dict entry")
760	        if not entry.get("name"):
761	            raise ValueError("imagined_experiment missing 'name'")
762	        if not entry.get("result_rationale"):
763	            raise ValueError(f"imagined_experiment '{entry.get('name')}' missing result_rationale")
764	        experiments.append(ImaginedExperiment.from_dict(entry))
765	    return ImaginedScenario(
766	        tier=tier,
767	        imagined_experiments=experiments,
768	        narrative_guidance=data.get("narrative_guidance", "") or "",
769	    )
770	
771	
772	def _elaborate_scenario(
773	    context: dict[str, Any],
774	    tier_def: TierDefinition,
775	    *,
776	    log_dir: Path | None = None,
777	) -> ImaginedScenario:
778	    """Phase 2: expand one tier into a full ImaginedScenario.
779	
780	    Raises on persistent parse failure — orchestrator catches and marks the
781	    tier's DreamScenarioResult.error, the other tiers continue.
782	    """
783	    prompt = _PHASE2_PROMPT.format(
784	        tier=tier_def.tier,
785	        meaning=tier_def.meaning,
786	        assumptions=tier_def.key_assumptions,
787	        number_ranges=tier_def.number_ranges,
788	        narrative_direction=tier_def.narrative_direction,
789	        context_block=_context_block(context),
790	    )
791	    last_err: Exception | None = None
792	    for attempt in range(_YAML_PARSE_RETRIES + 1):
793	        log_path = (log_dir / f"phase2_{tier_def.tier}_attempt{attempt}.log") if log_dir else None
794	        try:
795	            raw = _run_llm(
796	                prompt,
797	                project=context.get("project", ""),
798	                timeout_s=_PHASE2_TIMEOUT_S,
799	                log_path=log_path,
800	            )
801	        except Exception as e:
802	            last_err = e
803	            continue
804	        if not raw:
805	            last_err = ValueError("Phase 2 LLM returned empty output")
806	            continue
807	        try:
808	            data = yaml.safe_load(_extract_yaml_block(raw))
809	            return _validate_imagined_scenario(data, tier=tier_def.tier)
810	        except Exception as e:
811	            last_err = e
812	            logger.warning("[dream] Phase 2 %s parse failed (attempt %d): %s", tier_def.tier, attempt, e)
813	    raise ValueError(f"Phase 2 ({tier_def.tier}) failed: {last_err}")
814	
815	
816	# ---------------------------------------------------------------------------
817	# Step 3 — _write_dream_paper (2-6)
818	# ---------------------------------------------------------------------------
819	
820	
821	def _imagined_to_experiment_data(scenario: ImaginedScenario) -> list[dict[str, Any]]:
822	    """Convert ImaginedExperiments into ExperimentData-shaped dicts.
823	
824	    Paper Agent treats real + imagined identically (see Dream design §5.5), so
825	    we expose them through the same shape. ``analysis`` rolls together the
826	    rationale plus any free-form notes; per design ``result_rationale`` is
827	    Director-facing not paper-facing.
828	    """
829	    out: list[dict[str, Any]] = []
830	    for e in scenario.imagined_experiments:
831	        analysis_parts = [e.analysis or "", e.result_rationale or ""]
832	        out.append({
833	            "name": e.name,
834	            "description": e.description,
835	            "results": dict(e.expected_results or {}),
836	            "tables": list(e.tables or []),
837	            "figures": [],  # Dream skips conceptual figures; matplotlib renders inside Paper Agent
838	            "analysis": "\n\n".join(p for p in analysis_parts if p),
839	        })
840	    return out
841	
842	
843	def _write_dream_paper(
844	    *,
845	    dream_id: str,
846	    project: str,
847	    tier: str,
848	    scenario: ImaginedScenario,
849	    framing: str,
850	    venue: str,
851	    real_experiments: list[dict[str, Any]] | None = None,
852	    writing_visible: bool = True,
853	) -> Path:
854	    """Spawn a Paper Agent (Dream mode) subprocess and return the PDF path.
855	
856	    The Paper Agent is a Claude subprocess with a reduced MCP tool whitelist
857	    (no provenance, no Reviewer). It writes into ``$DREAM_OUTPUT_DIR``, which
858	    is set by this function and consumed by paper-agent.md's prompt logic.
859	
860	    Returns the *expected* PDF path even on failure — caller checks existence.
861	    """
862	    output_dir = _paths.dream_report_dir(project, dream_id) / tier
863	    output_dir.mkdir(parents=True, exist_ok=True)
864	
865	    # Persist the imagined scenario alongside the eventual PDF so reviewers
866	    # can audit Dream's predictions independent of the rendered paper.
867	    (output_dir / "imagined_experiments.yaml").write_text(
868	        yaml.safe_dump(
869	            {
870	                "tier": scenario.tier,
871	                "narrative_guidance": scenario.narrative_guidance,
872	                "imagined_experiments": [e.to_dict() for e in scenario.imagined_experiments],
873	            },
874	            allow_unicode=True,
875	            sort_keys=False,
876	        ),
877	        encoding="utf-8",
878	    )
879	
880	    experiment_data = _imagined_to_experiment_data(scenario)
881	    if real_experiments:
882	        experiment_data = list(real_experiments) + experiment_data
883	
884	    # Hand the data to Paper Agent via a sidecar JSON so we don't blow up the
885	    # CLI prompt size. paper-agent.md is updated to look for this file.
886	    (output_dir / "experiment_data.json").write_text(
887	        json.dumps(experiment_data, ensure_ascii=False, indent=2),
888	        encoding="utf-8",
889	    )
890	
891	    # Resolve LaTeX template for the venue so Paper Agent can \input it.
892	    template_hint = ""
893	    if venue:
894	        tpl_dir = Path("templates/latex") / venue.lower().replace(" ", "")
895	        matches = sorted(tpl_dir.glob("*.sty")) + sorted(tpl_dir.glob("*.cls")) if tpl_dir.exists() else []
896	        if matches:
897	            template_hint = f"LaTeX 模板目录：{tpl_dir}（包含 {', '.join(m.name for m in matches[:3])}）\n"
898	
899	    prompt = (
900	        f"你是 Paper Agent（Dream 模式）。任务：为 dream_id={dream_id} tier={tier} "
901	        f"生成一篇完整的模拟论文。\n\n"
902	        f"## 关键规则\n"
903	        f"1. 用 **Write 工具** 把 LaTeX 源码写入 `{output_dir}/paper.tex`\n"
904	        f"2. 用 **Bash 工具** 编译：`cd {output_dir} && pdflatex -interaction=nonstopmode paper.tex && "
905	        f"pdflatex -interaction=nonstopmode paper.tex`\n"
906	        f"3. 所有文件只写入 `{output_dir}/`，禁止写入其他目录\n"
907	        f"4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{{document}}），不要输出 YAML/JSON/Markdown\n"
908	        f"5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n\n"
909	        f"## 输入\n"
910	        f"- 实验数据（JSON）：`{output_dir / 'experiment_data.json'}`（先 Read 此文件）\n"
911	        f"- Venue：{venue or '默认'}\n"
912	        f"{template_hint}"
913	        f"- Narrative guidance：{scenario.narrative_guidance}\n"
914	        f"- paper_framing.md 节选：\n{framing[:4000]}\n\n"
915	        f"## 质量目标\n"
916	        f"\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。"
917	        f"包含 Abstract、Introduction、Method、Experiments、Conclusion。"
918	        f"每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
919	    )
920	
921	    # Re-uses the worker subprocess path because Paper Agent in Dream mode is
922	    # ergonomically a Worker (one-shot, no Director routing) — but the env
923	    # var DREAM_OUTPUT_DIR keys the Dream-mode behavior in paper-agent.md.
924	    os.environ.pop("DREAM_OUTPUT_DIR", None)  # never leak across calls
925	    env_overrides = {
926	        "DREAM_OUTPUT_DIR": str(output_dir),
927	        "DREAM_WRITING_VISIBLE": "true" if writing_visible else "false",
928	    }
929	    log_path = _paths.dream_report_dir(project, dream_id) / "logs" / f"paper_agent_{tier}.log"
930	    log_path.parent.mkdir(parents=True, exist_ok=True)
931	
932	    try:
933	        _run_paper_agent_subprocess(
934	            prompt=prompt,
935	            project=project,
936	            env_overrides=env_overrides,
937	            log_path=log_path,
938	            timeout_s=_WRITE_TIMEOUT_S,
939	        )
940	    except Exception:
941	        logger.exception("[dream] paper agent subprocess failed for tier=%s", tier)
942	
943	    return output_dir / "paper.pdf"
944	
945	
946	def _run_paper_agent_subprocess(
947	    *,
948	    prompt: str,
949	    project: str,
950	    env_overrides: dict[str, str],
951	    log_path: Path,
952	    timeout_s: int,
953	) -> None:
954	    """Thin wrapper around _run_llm that injects extra env vars.
955	
956	    Paper Agent mode requires DREAM_OUTPUT_DIR; we don't want to pollute the
957	    process-wide env, so this helper exposes the override mechanism while
958	    keeping _run_llm reusable for plain LLM calls.
959	    """
960	    from core.backends import get_backend
961	    from core.model_resolver import resolve_model_for_session
962	    import subprocess
963	
964	    backend = get_backend(project=project or None)
965	    if not backend.pool_enabled():
966	        raise RuntimeError("Paper Agent (Dream) requires Claude pool to be enabled.")
967	    config_dir = backend.pool_select()
968	    if not config_dir:
969	        raise RuntimeError("Paper Agent (Dream) could not acquire a pool account — none healthy.")
970	    cmd = backend.build_command(
971	        prompt=prompt,
972	        mcp_config=None,
973	        model=resolve_model_for_session(project=project or None),
974	        max_turns=30,
975	    )
976	    env = backend.make_env(config_dir=config_dir)
977	    env.update(env_overrides)
978	    backend.prepare_mcp(None, env=env, cwd=str(_paths.project_dir(project) if project else _paths.WORKSPACE_ROOT))
979	
980	    log_path.parent.mkdir(parents=True, exist_ok=True)
981	    with log_path.open("wb") as log_fh:
982	        proc = subprocess.Popen(
983	            cmd, stdout=log_fh, stderr=subprocess.STDOUT,
984	            env=env, cwd=str(_paths.project_dir(project) if project else _paths.WORKSPACE_ROOT),
985	            start_new_session=True,
986	        )
987	        try:
988	            proc.wait(timeout=timeout_s)
989	        except subprocess.TimeoutExpired:
990	            with suppress(ProcessLookupError):
991	                proc.kill()
992	                proc.wait()
993	            raise RuntimeError(f"Paper Agent (Dream) timed out after {timeout_s}s")
994	
995	
996	# ---------------------------------------------------------------------------
997	# Step 4 — _submit_to_review (placeholder until Phase 3 lands)
998	# ---------------------------------------------------------------------------
999	
1000	
1001	def _build_dream_review_dispatch_prompt(
1002	    *,
1003	    dream_id: str,
1004	    project: str,
1005	    tier: str,
1006	    pdf_path: Path,
1007	    review_mode: str,
1008	    review_visible: bool,
1009	) -> str:
1010	    """Compose the Dream Review Director boot prompt.
1011	
1012	    Includes everything the Director needs without an extra Director-to-
1013	    Reviewer chat round: dream_id (sans prefix for the submission tool),
1014	    PDF path, tier, mode, visibility, and the exact submission call so the
1015	    subprocess can complete in one Claude turn.
1016	    """
1017	    dream_id_bare = dream_id.removeprefix("dream_")
1018	    if review_mode == "simple":
1019	        skill_hint = (
1020	            " 使用 `dream-review-simple` skill 的 dispatch 模板（1 Reviewer 全面覆盖，"
1021	            "跳过 Step 2 交叉分享 + Step 3 收敛）。"
1022	        )
1023	    else:
1024	        skill_hint = (
1025	            " 使用 `dream-review-full` skill 的 dispatch 模板（2 Reviewers：R1 方法+实验、"
1026	            "R2 新颖性+相关工作；完整 roundtable：Step 1 独立 → Step 2 交叉分享 → "
1027	            "Step 3 收敛 → Step 4 综合）。"
1028	        )
1029	    return (
1030	        f"[DREAM Review Director — {tier} 档]\n"
1031	        f"dream_id={dream_id_bare} | tier={tier} | review_mode={review_mode} | "
1032	        f"review_visible={review_visible}\n"
1033	        f"PDF: {pdf_path}\n\n"
1034	        f"任务：对上述 PDF 进行 {review_mode} 模式审稿。{skill_hint}\n"
1035	        f"完成后必须调用 `submit_dream_review_report(report, project="
1036	        f"\"{project}\", tier=\"{tier}\", dream_id=\"{dream_id_bare}\", "
1037	        f"review_visible={review_visible})` —— 报告会写入 "
1038	        f"dream_reports/{dream_id}/{tier}/review_report.md，编排进程通过 "
1039	        f"subprocess 退出读取它。\n"
1040	        f"不要调用 submit_review_report_to_research_director / update_review_issues / "
1041	        f"request_external_review —— 这些工具不在 Dream Review Director 白名单内。\n"
1042	    )
1043	
1044	
1045	def _run_dream_review_director_subprocess(
1046	    *,
1047	    prompt: str,
1048	    project: str,
1049	    dream_id: str,
1050	    tier: str,
1051	    log_path: Path,
1052	    timeout_s: int,
1053	) -> None:
1054	    """Spawn a Dream-mode Review Director subprocess for one tier.
1055	
1056	    Mirrors ``_run_paper_agent_subprocess``: pool-aware Claude CLI, isolated
1057	    session via env, output streamed to ``log_path``. Returns when the
1058	    subprocess exits (success or timeout). The submitted review report is
1059	    persisted to disk by the subprocess via ``submit_dream_review_report``;
1060	    the caller reads that file after we return.
1061	    """
1062	    from core.backends import get_backend
1063	    from core.model_resolver import resolve_model_for_session
1064	    from core.session_server import _ensure_dream_review_director_mcp_config
1065	    import subprocess
1066	
1067	    backend = get_backend(project=project or None)
1068	    if not backend.pool_enabled():
1069	        raise RuntimeError("Dream Review Director requires Claude pool to be enabled.")
1070	    config_dir = backend.pool_select()
1071	    if not config_dir:
1072	        raise RuntimeError("Dream Review Director could not acquire a pool account — none healthy.")
1073	    mcp_config = _ensure_dream_review_director_mcp_config()
1074	    cmd = backend.build_command(
1075	        prompt=prompt,
1076	        mcp_config=mcp_config,
1077	        model=resolve_model_for_session(project=project or None),
1078	    )
1079	    env = backend.make_env(config_dir=config_dir)
1080	    # Surface key context to the subprocess for any tool that wants to read it
1081	    env["DREAM_ID"] = dream_id
1082	    env["DREAM_TIER"] = tier
1083	    backend.prepare_mcp(
1084	        mcp_config,
1085	        env=env,
1086	        cwd=str(_paths.project_dir(project) if project else _paths.WORKSPACE_ROOT),
1087	    )
1088	
1089	    log_path.parent.mkdir(parents=True, exist_ok=True)
1090	    with log_path.open("wb") as log_fh:
1091	        proc = subprocess.Popen(
1092	            cmd, stdout=log_fh, stderr=subprocess.STDOUT,
1093	            env=env,
1094	            cwd=str(_paths.project_dir(project) if project else _paths.WORKSPACE_ROOT),
1095	            start_new_session=True,
1096	        )
1097	        try:
1098	            proc.wait(timeout=timeout_s)
1099	        except subprocess.TimeoutExpired:
1100	            with suppress(ProcessLookupError):
1101	                proc.kill()
1102	                proc.wait()
1103	            raise RuntimeError(f"Dream Review Director timed out after {timeout_s}s")
1104	
1105	
1106	def _ensure_review_chat_id(project: str) -> str:
1107	    """Ensure project has a review_chat_id (Group C), creating one if needed.
1108	
1109	    Mirrors the Group C bootstrap logic in ``core/approvals/hooks.py``.
1110	    Returns the review_chat_id (existing or newly created). Returns empty
1111	    string if creation fails (caller degrades gracefully).
1112	    """
1113	    from core.tools.project_config import load_review_chat_id, save_project_submission_config
1114	
1115	    existing = load_review_chat_id(project)
1116	    if existing:
1117	        return existing
1118	
1119	    from core.tools.feishu import create_chat, get_chat_members
1120	    from core.tools.project_config import load_project_config
1121	
1122	    result = load_project_config(project, section="feishu")
1123	    feishu = result.data.get("config", {}).get("feishu", {}) if result.success else {}
1124	    research_chat_id = feishu.get("chat_id", "")
1125	
1126	    group_name = f"{project}-审稿群"
1127	    member_ids = get_chat_members(research_chat_id) if research_chat_id else []
1128	    review_chat_id = create_chat(group_name, user_id_list=member_ids or None)
1129	    if not review_chat_id:
1130	        logger.error("[dream] failed to create Group C for project=%s", project)
1131	        return ""
1132	
1133	    save_result = save_project_submission_config(project, review_chat_id)
1134	    if not save_result.success:
1135	        logger.error(
1136	            "[dream] created Group C (chat_id=%s) but failed to save config: %s",
1137	            review_chat_id, save_result.error,
1138	        )
1139	    else:
1140	        logger.info("[dream] auto-created Group C for project=%s: %s", project, review_chat_id)
1141	    return review_chat_id
1142	
1143	
1144	def _submit_to_review(
1145	    *,
1146	    dream_id: str,
1147	    project: str,
1148	    tier: str,
1149	    pdf_path: Path,
1150	    review_mode: str,
1151	    review_visible: bool,
1152	) -> str:
1153	    """Submit one Dream PDF to Group C review and return the report text.
1154	
1155	    Spawns a Dream-mode Review Director subprocess (independent session_key
1156	    in the ``feishu:group:{review_chat_id}:dream_{id}:director`` namespace).
1157	    The subprocess writes the consolidated report to
1158	    ``dream_reports/{dream_id}/{tier}/review_report.md`` via
1159	    ``submit_dream_review_report``; we read that file once the subprocess
1160	    exits and return its content.
1161	
1162	    Falls back to a stub report if (a) no PDF was produced or (b) we cannot
1163	    acquire a pool account. The pipeline can still continue for the other
1164	    tiers either way — ``_persist_report`` records the missing review as an
1165	    error on the tier's ``DreamScenarioResult``.
1166	    """
1167	    if review_visible:
1168	        _ensure_review_chat_id(project)
1169	
1170	    output_dir = _paths.dream_report_dir(project, dream_id) / tier
1171	    report_path = output_dir / "review_report.md"
1172	    output_dir.mkdir(parents=True, exist_ok=True)
1173	
1174	    if not pdf_path.exists():
1175	        report_path.write_text(
1176	            f"# [Dream Review — {tier}]\n\n"
1177	            f"Status: skipped (paper PDF not produced)\n",
1178	            encoding="utf-8",
1179	        )
1180	        return report_path.read_text(encoding="utf-8")
1181	
1182	    prompt = _build_dream_review_dispatch_prompt(
1183	        dream_id=dream_id, project=project, tier=tier, pdf_path=pdf_path,
1184	        review_mode=review_mode, review_visible=review_visible,
1185	    )
1186	    log_path = _paths.dream_report_dir(project, dream_id) / "logs" / f"review_{tier}.log"
1187	    try:
1188	        _run_dream_review_director_subprocess(
1189	            prompt=prompt, project=project, dream_id=dream_id, tier=tier,
1190	            log_path=log_path, timeout_s=_REVIEW_TIMEOUT_S,
1191	        )
1192	    except Exception as exc:
1193	        logger.exception("[dream] review subprocess failed for tier=%s", tier)
1194	        # Persist a minimal failure stub so callers always have something
1195	        # to read. The orchestrator records the error on the scenario via
1196	        # the calling ``_run_dream_pipeline`` exception handler.
1197	        if not report_path.exists():
1198	            report_path.write_text(
1199	                f"# [Dream Review — {tier}]\n\n"
1200	                f"Status: failed ({exc})\n",
1201	                encoding="utf-8",
1202	            )
1203	        return report_path.read_text(encoding="utf-8")
1204	
1205	    # Subprocess exited cleanly. If submit_dream_review_report was called the
1206	    # file is on disk; otherwise leave a clear marker for the orchestrator.
1207	    if not report_path.exists():
1208	        report_path.write_text(
1209	            f"# [Dream Review — {tier}]\n\n"
1210	            f"Status: subprocess exited but no report was submitted\n",
1211	            encoding="utf-8",
1212	        )
1213	    return report_path.read_text(encoding="utf-8")
1214	
1215	
1216	# ---------------------------------------------------------------------------
1217	# Step 5 — _persist_report (2-7)
1218	# ---------------------------------------------------------------------------
1219	
1220	
1221	def _persist_report(
1222	    *,
1223	    dream_id: str,
1224	    project: str,
1225	    dream_input: DreamInput,
1226	    scenarios: dict[str, ImaginedScenario],
1227	    pdf_paths: dict[str, Path],
1228	    reviews: dict[str, str],
1229	    errors: dict[str, str],
1230	    tier_defs: TierDefinitions | None = None,
1231	) -> DreamOutput:
1232	    """Write meta.yaml + per-tier review files; build the DreamOutput.
1233	
1234	    Symlink ``latest`` → this dream's directory so callers (Director, A-group
1235	    summary) can always point at the most recent run without knowing its id.
1236	    """
1237	    root = _paths.dream_report_dir(project, dream_id)
1238	    root.mkdir(parents=True, exist_ok=True)
1239	    (root / "logs").mkdir(exist_ok=True)
1240	
1241	    results: list[DreamScenarioResult] = []
1242	    for tier in TIERS:
1243	        scenario = scenarios.get(tier)
1244	        pdf = pdf_paths.get(tier)
1245	        results.append(
1246	            DreamScenarioResult(
1247	                tier=tier,
1248	                pdf_path=str(pdf) if pdf and pdf.exists() else "",
1249	                imagined_experiments=list(scenario.imagined_experiments) if scenario else [],
1250	                review_report=reviews.get(tier, ""),
1251	                error=errors.get(tier, ""),
1252	            )
1253	        )
1254	
1255	    meta = {
1256	        "dream_id": dream_id,
1257	        "project": project,
1258	        "venue": dream_input.venue,
1259	        "focus": dream_input.focus,
1260	        "review_mode": dream_input.review_mode,
1261	        "review_visible": dream_input.review_visible,
1262	        "writing_visible": dream_input.writing_visible,
1263	        "what_if": [w.to_dict() for w in dream_input.what_if],
1264	        "tier_definitions": tier_defs.to_dict() if tier_defs else {},
1265	        "scenarios": [r.to_dict() for r in results],
1266	        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
1267	    }
1268	    (root / "meta.yaml").write_text(
1269	        yaml.safe_dump(meta, allow_unicode=True, sort_keys=False),
1270	        encoding="utf-8",
1271	    )
1272	
1273	    # `latest` symlink — best-effort; non-POSIX FS without symlinks is fine.
1274	    latest = _paths.dream_reports_dir(project) / "latest"
1275	    with suppress(OSError):
1276	        if latest.is_symlink() or latest.exists():
1277	            latest.unlink()
1278	        latest.symlink_to(root)
1279	
1280	    return DreamOutput(dream_id=dream_id, scenarios=results)
1281	
1282	
1283	# ---------------------------------------------------------------------------
1284	# Pipeline (2-9)
1285	# ---------------------------------------------------------------------------
1286	
1287	
1288	def _run_dream_pipeline(
1289	    dream_input: DreamInput,
1290	    dream_id: str,
1291	    *,
1292	    director_session_key: str = "",
1293	    chat_id: str = "",
1294	    operational_chat_id: str = "",
1295	) -> DreamOutput:
1296	    """Run the full Dream pipeline (sync, runs inside the orchestrator process).
1297	
1298	    The orchestrator is started by ``dream_simulate`` via ``multiprocessing``
1299	    (start_new_session=True) so it survives BE restarts. ``dream_registry``
1300	    is the only state shared with the parent — every transition is committed
1301	    there so ``get_dream_status`` returns truthful progress.
1302	    """
1303	    project = dream_input.project
1304	    log_dir = _paths.dream_report_dir(project, dream_id) / "logs"
1305	    log_dir.mkdir(parents=True, exist_ok=True)
1306	
1307	    scenarios: dict[str, ImaginedScenario] = {}
1308	    pdf_paths: dict[str, Path] = {}
1309	    reviews: dict[str, str] = {}
1310	    errors: dict[str, str] = {}
1311	    tier_defs: TierDefinitions | None = None
1312	
1313	    _card_kwargs = dict(
1314	        dream_id=dream_id, project=project,
1315	        venue=dream_input.venue, focus=dream_input.focus,
1316	        review_mode=dream_input.review_mode,
1317	    )
1318	    _activity: list[tuple[str, str]] = []
1319	
1320	    def _log_activity(label: str, detail: str) -> None:
1321	        _activity.append((label, detail))
1322	
1323	    def _patch_card(phase: str, stages: list[str] | None = None, error: str = "") -> None:
1324	        try:
1325	            from core.tools.dream_card import patch_dream_card
1326	            patch_dream_card(
1327	                phase=phase, stages_completed=stages, error=error,
1328	                activity=_activity, **_card_kwargs,
1329	            )
1330	        except Exception:
1331	            logger.debug("[dream:%s] card patch failed", dream_id, exc_info=True)
1332	
1333	    _PHASE_LABEL = {
1334	        "pending": "⏳ 启动",
1335	        "imagining": "🔮 想象中",
1336	        "writing": "✍️ 写作中",
1337	        "reviewing": "🔍 审阅中",
1338	        "done": "✅ 完成",
1339	        "failed": "❌ 失败",
1340	    }
1341	    _ops_notified_phases: set[str] = set()
1342	
1343	    def _notify_ops(phase: str, error: str = "") -> None:
1344	        if not operational_chat_id or phase in _ops_notified_phases:
1345	            return
1346	        _ops_notified_phases.add(phase)
1347	        label = _PHASE_LABEL.get(phase, phase)
1348	        text = f"[Dream {dream_id}] {project} — {label}"
1349	        if error:
1350	            text += f"\n{error[:300]}"
1351	        try:
1352	            from core.tools.feishu import send_message
1353	            send_message(chat_id=operational_chat_id, text=text)
1354	        except Exception:
1355	            logger.debug("[dream:%s] ops notify failed", dream_id, exc_info=True)
1356	
1357	    # --- 0. Collect context ---
1358	    _log_activity("Context", "收集项目上下文 (framing + plan + registry)")
1359	    _patch_card("pending")
1360	    _notify_ops("pending")
1361	    try:
1362	        context = _collect_context(
1363	            project=project,
1364	            what_if=dream_input.what_if,
1365	            venue=dream_input.venue,
1366	            focus=dream_input.focus,
1367	        )
1368	        framing = context.get("framing", "") or ""
1369	        real_experiments = []  # real ExperimentData injection deferred to Phase 5 mapping
1370	        _log_activity("Context", "上下文收集完成")
1371	    except Exception as e:
1372	        logger.exception("[dream:%s] context collection failed", dream_id)
1373	        _registry.mark_status(project, dream_id, "failed", error=f"context: {e}")
1374	        _patch_card("failed", error=f"context: {e}")
1375	        _notify_ops("failed", error=f"context: {e}")
1376	        return _persist_report(
1377	            dream_id=dream_id, project=project, dream_input=dream_input,
1378	            scenarios={}, pdf_paths={}, reviews={}, errors={"_pipeline": str(e)},
1379	        )
1380	
1381	    # --- 1. Phase 1: tier definitions ---
1382	    _registry.mark_status(project, dream_id, "imagining")
1383	    _log_activity("Phase1", "LLM 生成三档场景定义 (best/median/worst) …")
1384	    _patch_card("imagining")
1385	    _notify_ops("imagining")
1386	    try:
1387	        tier_defs = _define_tiers(context, log_dir=log_dir)
1388	        _log_activity("Phase1", "三档场景定义完成 ✓")
1389	        _patch_card("imagining")
1390	    except Exception as e:
1391	        logger.exception("[dream:%s] Phase 1 failed", dream_id)
1392	        _registry.mark_status(project, dream_id, "failed", error=f"phase1: {e}")
1393	        _patch_card("failed", error=f"phase1: {e}")
1394	        _notify_ops("failed", error=f"phase1: {e}")
1395	        return _persist_report(
1396	            dream_id=dream_id, project=project, dream_input=dream_input,
1397	            scenarios={}, pdf_paths={}, reviews={},
1398	            errors={t: f"phase1: {e}" for t in TIERS},
1399	        )
1400	
1401	    # --- 2. Phase 2 per tier (sequential is fine here; parallelism is a perf
1402	    #       optimization, not a correctness requirement; pool can be tight). ---
1403	    for tier in TIERS:
1404	        tdef = tier_defs.get(tier)
1405	        if tdef is None:
1406	            errors[tier] = "tier definition missing"
1407	            continue
1408	        _log_activity("Phase2", f"展开 {tier} 场景 …")
1409	        _patch_card("imagining")
1410	        try:
1411	            scenarios[tier] = _elaborate_scenario(context, tdef, log_dir=log_dir)
1412	            n_exp = len(scenarios[tier].imagined_experiments)
1413	            _log_activity("Phase2", f"{tier} 场景完成 ({n_exp} experiments) ✓")
1414	        except Exception as e:
1415	            errors[tier] = f"phase2: {e}"
1416	            _log_activity("Phase2", f"{tier} 场景失败: {str(e)[:80]}")
1417	            logger.warning("[dream:%s] Phase 2 %s failed: %s", dream_id, tier, e)
1418	
1419	    _registry.mark_stage_complete(project, dream_id, "imagine")
1420	
1421	    # --- 3. Write papers ---
1422	    _registry.mark_status(project, dream_id, "writing")
1423	    _patch_card("writing", ["imagine"])
1424	    _notify_ops("writing")
1425	    for tier, scenario in scenarios.items():
1426	        _log_activity("Paper", f"写作 {tier} 模拟论文 …")
1427	        _patch_card("writing", ["imagine"])
1428	        try:
1429	            pdf_paths[tier] = _write_dream_paper(
1430	                dream_id=dream_id,
1431	                project=project,
1432	                tier=tier,
1433	                scenario=scenario,
1434	                framing=framing,
1435	                venue=dream_input.venue,
1436	                real_experiments=real_experiments,
1437	                writing_visible=dream_input.writing_visible,
1438	            )
1439	            _log_activity("Paper", f"{tier} 论文完成 ✓")
1440	        except Exception as e:
1441	            errors[tier] = (errors.get(tier, "") + f" | write: {e}").strip(" |")
1442	            _log_activity("Paper", f"{tier} 写作失败: {str(e)[:80]}")
1443	            logger.warning("[dream:%s] write %s failed: %s", dream_id, tier, e)
1444	    _registry.mark_stage_complete(project, dream_id, "write")
1445	
1446	    # --- 4. Review ---
1447	    _registry.mark_status(project, dream_id, "reviewing")
1448	    _patch_card("reviewing", ["imagine", "write"])
1449	    _notify_ops("reviewing")
1450	    for tier, pdf in pdf_paths.items():
1451	        _log_activity("Review", f"审阅 {tier} 论文 ({dream_input.review_mode}) …")
1452	        _patch_card("reviewing", ["imagine", "write"])
1453	        try:
1454	            reviews[tier] = _submit_to_review(
1455	                dream_id=dream_id, project=project, tier=tier,
1456	                pdf_path=pdf,
1457	                review_mode=dream_input.review_mode,
1458	                review_visible=dream_input.review_visible,
1459	            )
1460	            _log_activity("Review", f"{tier} 审阅完成 ✓")
1461	        except Exception as e:
1462	            errors[tier] = (errors.get(tier, "") + f" | review: {e}").strip(" |")
1463	            _log_activity("Review", f"{tier} 审阅失败: {str(e)[:80]}")
1464	            logger.warning("[dream:%s] review %s failed: %s", dream_id, tier, e)
1465	    _registry.mark_stage_complete(project, dream_id, "review")
1466	
1467	    # --- 5. Persist + done ---
1468	    out = _persist_report(
1469	        dream_id=dream_id, project=project, dream_input=dream_input,
1470	        scenarios=scenarios, pdf_paths=pdf_paths, reviews=reviews,
1471	        errors=errors, tier_defs=tier_defs,
1472	    )
1473	    has_any_success = any(s.pdf_path and not s.error for s in out.scenarios)
1474	    final_status = "done" if has_any_success else "failed"
1475	    _registry.mark_status(
1476	        project, dream_id, final_status,
1477	        error=None if final_status == "done" else "all tiers failed",
1478	    )
1479	    _log_activity("Done" if final_status == "done" else "Failed",
1480	                  "3-tier 模拟完成" if final_status == "done" else "全部 tier 失败")
1481	    _patch_card(
1482	        final_status,
1483	        ["imagine", "write", "review"],
1484	        error="" if final_status == "done" else "all tiers failed",
1485	    )
1486	    _notify_ops(final_status, error="" if final_status == "done" else "all tiers failed")
1487	
1488	    try:
1489	        dispatch_dream_done(
1490	            dream_id=dream_id, project=project,
1491	            director_session_key=director_session_key, chat_id=chat_id,
1492	            operational_chat_id=operational_chat_id,
1493	            output=out,
1494	        )
1495	    except Exception:
1496	        logger.exception("[dream:%s] dispatch_dream_done failed", dream_id)
1497	
1498	    return out
1499	
1500	
1501	# ---------------------------------------------------------------------------
1502	# dispatch_dream_done (2-10)
1503	# ---------------------------------------------------------------------------
1504	
1505	
1506	_DREAM_ACTION_PROTOCOL = """\
1507	## 行动要求（硬约束，收到本消息后必须执行，不得"已知悉"跳过）
1508	
1509	### 1. 阅读完整报告
1510	逐一 read_local_file 上述三份 review_report.md。不要只看本消息的评分摘要——\
1511	完整审稿意见在报告文件中。
1512	
1513	### 2. 分析审稿意见
1514	Read skills/global/dream-report-action.skill.md，按 skill 中的分类方法处理。
1515	
1516	核心原则——Dream 的实验数据是想象的，审稿意见分两类：
1517	- **通用建议**（缺 baseline/benchmark、引用不足、方法描述不清、framing 逻辑漏洞）\
1518	——不依赖实验数据，直接有效，应认真对待
1519	- **数据依赖建议**（claim 太强/太弱、实验效果不 convincing）\
1520	——高度依赖想象数据，必须跨三档对比后再判断
1521	
1522	### 3. 跨档对比（数据依赖建议的判定规则）
1523	- **三档一致**指出的问题 → 结构性问题，必须处理
1524	- **三档不一致** → 该意见取决于实验结果好坏，\
1525	不要因某一档的想象数据就急于调整 claim——先记录为观察项
1526	- **仅单档出现**的 claim 强弱意见 → 记录但不行动
1527	
1528	### 4. 持久化
1529	- **确认行动项**（通用建议 + 三档一致的结构性问题）：\
1530	直接修改 paper_framing.md / experiment_plan.yaml + 更新 ROADMAP 近期任务
1531	- **整体判断**：log_decision 记录（proceed / adjust / re-dream + 完整分析）
1532	- **观察项**（模棱两可、待真实实验验证的）：\
1533	log_decision 中写明"待验证"，ROADMAP 近期任务加 [Dream 观察] 条目，\
1534	标注具体观察什么指标、关联哪个实验、什么条件下需要行动
1535	
1536	### 5. 向 A 群汇报
1537	director_reply_to_user 发送分析结论：
1538	1. 三档评分总结
1539	2. 发现了哪些必须处理的问题 + 已采取/计划采取的行动
1540	3. 记录了哪些观察项
1541	4. 下一步行动计划
1542	
1543	### 处理态度
1544	该处理的果断处理，模棱两可的先记录等真实实验再定。\
1545	但也不要因为"数据是想象的"就全盘忽视——通用建议和三档一致的问题是实打实的。
1546	"""
1547	
1548	
1549	def _extract_overall_score(review_report: str) -> str:
1550	    """Extract overall_score from review_report.md YAML frontmatter.
1551	
1552	    Returns the score string, or "N/A" if not found or parse fails.
1553	    """
1554	    if not review_report or "---" not in review_report:
1555	        return "N/A"
1556	    parts = review_report.split("---", 2)
1557	    if len(parts) < 3:
1558	        return "N/A"
1559	    try:
1560	        fm = yaml.safe_load(parts[1])
1561	        if isinstance(fm, dict):
1562	            score = fm.get("overall_score", "")
1563	            return score if score else "N/A"
1564	    except Exception:
1565	        pass
1566	    return "N/A"
1567	
1568	
1569	def _summarize_for_director(output: DreamOutput, project: str) -> str:
1570	    """Structured summary + action protocol for Director session injection."""
1571	    lines = [f"[DREAM {output.dream_id}] 完成 — 三档审稿报告就绪", ""]
1572	
1573	    lines.append("## 评分概览")
1574	    for s in output.scenarios:
1575	        if s.error:
1576	            lines.append(f"- {s.tier}: 失败 ({s.error})")
1577	            continue
1578	        n = len(s.imagined_experiments)
1579	        score = _extract_overall_score(s.review_report)
1580	        lines.append(f"- {s.tier}: {score}（{n} 个想象实验）")
1581	    lines.append("")
1582	
1583	    lines.append("## 完整报告路径")
1584	    for tier in TIERS:
1585	        lines.append(
1586	            f"- projects/{project}/artifacts/"
1587	            f"dream_reports/{output.dream_id}/{tier}/review_report.md"
1588	        )
1589	    lines.append("")
1590	
1591	    lines.append(_DREAM_ACTION_PROTOCOL)
1592	
1593	    return "\n".join(lines)
1594	
1595	
1596	def _group_a_brief(output: DreamOutput) -> str:
1597	    """Brief completion notification for Group A (user-facing)."""
1598	    lines = [f"[DREAM {output.dream_id}] 模拟完成"]
1599	    for s in output.scenarios:
1600	        if s.error:
1601	            lines.append(f"  {s.tier}: 失败")
1602	            continue
1603	        score = _extract_overall_score(s.review_report)
1604	        lines.append(f"  {s.tier}: {score}")
1605	    lines.append("")
1606	    lines.append("Director 正在分析审稿意见，稍后汇报行动方案。")
1607	    return "\n".join(lines)
1608	
1609	
1610	def dispatch_dream_done(
1611	    *,
1612	    dream_id: str,
1613	    project: str,
1614	    director_session_key: str = "",
1615	    chat_id: str = "",
1616	    operational_chat_id: str = "",
1617	    output: DreamOutput,
1618	) -> None:
1619	    """Inject the Dream summary back to Director + post to Group A + Group B.
1620	
1621	    Director receives a structured summary with action protocol;
1622	    Group A receives a brief notification (detailed analysis comes
1623	    later via director_reply_to_user).
1624	    """
1625	    # 1. Director session injection — detailed summary with action protocol.
1626	    if director_session_key:
1627	        director_msg = _summarize_for_director(output, project)
1628	        try:
1629	            from core.session_server import get_server
1630	            server = get_server()
1631	            if server._started:
1632	                server.send_sync(
1633	                    project=project,
1634	                    message=director_msg,
1635	                    reply_fn=lambda _t: None,
1636	                    session_key=director_session_key,
1637	                    source="dream",
1638	                )
1639	        except Exception:
1640	            logger.exception("[dream:%s] director injection failed", dream_id)
1641	
1642	    # 2. Group A — brief notification.
1643	    if chat_id:
1644	        brief = _group_a_brief(output)
1645	        try:
1646	            from core.tools.feishu import send_message
1647	            send_message(chat_id=chat_id, text=brief)
1648	        except Exception:
1649	            logger.exception("[dream:%s] feishu summary failed", dream_id)
1650	
1651	    # 3. Group B — brief notification (ops-facing).
1652	    if operational_chat_id and operational_chat_id != chat_id:
1653	        brief = _group_a_brief(output)
1654	        try:
1655	            from core.tools.feishu import send_message
1656	            send_message(chat_id=operational_chat_id, text=brief)
1657	        except Exception:
1658	            logger.exception("[dream:%s] ops summary failed", dream_id)
1659	
1660	
1661	# ---------------------------------------------------------------------------
1662	# Public entry points
1663	# ---------------------------------------------------------------------------
1664	
1665	
1666	def dream_simulate(
1667	    project: str,
1668	    *,
1669	    what_if: list[dict[str, Any]] | None = None,
1670	    venue: str = "",
1671	    focus: str = "",
1672	    review_mode: str = "simple",
1673	    review_visible: bool | None = None,
1674	    writing_visible: bool | None = None,
1675	    smart_skip: bool = False,
1676	    director_session_key: str = "",
1677	    chat_id: str = "",
1678	    operational_chat_id: str = "",
1679	) -> ToolResult:
1680	    """Kick off a Dream run. Returns a DreamHandle immediately.
1681	
1682	    Pre-flight checks (see DREAM_AGENT_DESIGN.md §8.3 / §8.4):
1683	      • ``paper_framing.md`` exists
1684	      • ``experiment_plan.yaml`` exists
1685	      • no over-the-limit concurrent dream is running
1686	      • when ``smart_skip=True``, reuse the last completed dream if the
1687	        research context (framing + plan + registry metrics) is unchanged
1688	
1689	    On success, registers the dream in ``dream_registry`` and spawns a
1690	    detached orchestrator process (``start_new_session=True``) that runs
1691	    ``_run_dream_pipeline``. The orchestrator is independent of the BE — a
1692	    BE restart does not abort the dream, and ``get_dream_status`` keeps
1693	    working across restarts because state lives in the registry.
1694	    """
1695	    if not project:
1696	        return ToolResult(success=False, error="project is required")
1697	
1698	    # Pre-flight: framing + plan must exist (Director hasn't done Post-MVP).
1699	    framing_path = _paths.resolve_project_file(project, "paper_framing.md")
1700	    plan_path = _paths.resolve_project_file(project, "experiment_plan.yaml")
1701	    if not framing_path.exists():
1702	        return ToolResult(
1703	            success=False,
1704	            error="paper_framing.md 不存在，请先完成 Post-MVP framing。",
1705	        )
1706	    if not plan_path.exists():
1707	        return ToolResult(
1708	            success=False,
1709	            error="experiment_plan.yaml 不存在，请先制定 plan。",
1710	        )
1711	
1712	    if not operational_chat_id:
1713	        try:
1714	            from core.session_claude_md import _load_operational_chat_id
1715	            operational_chat_id = _load_operational_chat_id(project)
1716	        except Exception:
1717	            pass
1718	
1719	    # Concurrency: respect dream config `max_concurrent_dreams`.
1720	    cfg = _project_dream_config(project)
1721	    max_concurrent = int(cfg.get("max_concurrent_dreams", 1) or 1)
1722	    if _registry.count_active(project) >= max_concurrent:
1723	        return ToolResult(
1724	            success=False,
1725	            error=f"已有 {_registry.count_active(project)} 个 Dream 在运行（上限 {max_concurrent}）",
1726	        )
1727	
1728	    # Smart-skip: if the caller opted in (cron / heuristic Director) and the
1729	    # research context hasn't changed since the last `done` dream, return that
1730	    # dream's handle instead of spawning a new orchestrator.
1731	    if smart_skip:
1732	        skip_result = should_skip_dream(project, what_if=what_if)
1733	        if skip_result.success and (skip_result.data or {}).get("skip"):
1734	            data = skip_result.data or {}
1735	            handle = DreamHandle(
1736	                dream_id=data.get("last_dream_id", ""),
1737	                status="done",
1738	            )
1739	            payload = handle.to_dict()
1740	            payload["skipped"] = True
1741	            payload["skip_reason"] = data.get("reason", "")
1742	            payload["last_dream_dir"] = data.get("last_dream_dir", "")
1743	            return ToolResult(success=True, data=payload)
1744	
1745	    # Resolve defaults from project config.
1746	    if review_visible is None:
1747	        review_visible = bool(cfg.get("review_visible", True))
1748	    if writing_visible is None:
1749	        writing_visible = bool(cfg.get("writing_visible", True))
1750	
1751	    what_if_objs = [WhatIfExperiment.from_dict(w) for w in (what_if or [])]
1752	    dream_input = DreamInput(
1753	        project=project,
1754	        what_if=what_if_objs,
1755	        venue=venue,
1756	        focus=focus,
1757	        review_mode=review_mode,
1758	        review_visible=review_visible,
1759	        writing_visible=writing_visible,
1760	    )
1761	
1762	    # Capture the context hash up front so trend/skip checks have a stable
1763	    # baseline even if framing/plan files change while the dream is running.
1764	    context_hash = _compute_context_hash(project, what_if=what_if_objs)
1765	
1766	    dream_id = _new_dream_id()
1767	    _registry.register(
1768	        dream_id=dream_id,
1769	        project=project,
1770	        review_mode=review_mode,
1771	        review_visible=review_visible,
1772	        writing_visible=writing_visible,
1773	        venue=venue,
1774	        focus=focus,
1775	        what_if=[w.to_dict() for w in what_if_objs],
1776	        status="pending",
1777	        chat_id=chat_id,
1778	    )
1779	    _registry.update(project, dream_id, context_hash=context_hash)
1780	
1781	    # Send live progress card to Group A.
1782	    try:
1783	        from core.tools.dream_card import send_dream_card
1784	        entry = _registry.get(project, dream_id)
1785	        send_dream_card(
1786	            dream_id=dream_id,
1787	            project=project,
1788	            chat_id=chat_id,
1789	            phase="pending",
1790	            venue=venue,
1791	            focus=focus,
1792	            review_mode=review_mode,
1793	            started_at=(entry or {}).get("started_at", ""),
1794	        )
1795	    except Exception:
1796	        logger.warning("[dream:%s] failed to send initial card", dream_id, exc_info=True)
1797	
1798	    # Launch orchestrator in a detached process. We use multiprocessing so the
1799	    # child inherits the module state (registry path, workspace root) without
1800	    # re-discovering them from env. ``start_new_session=True`` is the Python
1801	    # multiprocessing analog — `daemon=False` + detached session keeps it
1802	    # alive after BE shutdown.
1803	    pid = _spawn_pipeline_process(
1804	        dream_input=dream_input,
1805	        dream_id=dream_id,
1806	        director_session_key=director_session_key,
1807	        chat_id=chat_id,
1808	        operational_chat_id=operational_chat_id,
1809	    )
1810	    _registry.update(project, dream_id, pid=pid)
1811	
1812	    handle = DreamHandle(dream_id=dream_id, status="pending")
1813	    return ToolResult(success=True, data=handle.to_dict())
1814	
1815	
1816	def _spawn_pipeline_process(
1817	    *,
1818	    dream_input: DreamInput,
1819	    dream_id: str,
1820	    director_session_key: str,
1821	    chat_id: str,
1822	    operational_chat_id: str = "",
1823	) -> int | None:
1824	    """Spawn the orchestrator. Returns the child pid (or None in tests).
1825	
1826	    Implemented with ``subprocess.Popen`` (not multiprocessing) so the child
1827	    is a fully detached OS process — multiprocessing would attach signal
1828	    handlers to the parent loop and tear the child down on BE exit.
1829	    """
1830	    import subprocess
1831	
1832	    payload = {
1833	        "dream_id": dream_id,
1834	        "dream_input": dream_input.to_dict(),
1835	        "director_session_key": director_session_key,
1836	        "chat_id": chat_id,
1837	        "operational_chat_id": operational_chat_id,
1838	    }
1839	    runner = _paths.REPO_ROOT / "core" / "tools" / "dream_runner.py"
1840	    if not runner.exists():
1841	        # Fall back to in-process thread when the runner script is missing
1842	        # (used by unit tests that mock _run_dream_pipeline).
1843	        t = threading.Thread(
1844	            target=_run_dream_pipeline,
1845	            args=(dream_input, dream_id),
1846	            kwargs={
1847	                "director_session_key": director_session_key,
1848	                "chat_id": chat_id,
1849	                "operational_chat_id": operational_chat_id,
1850	            },
1851	            daemon=True,
1852	            name=f"dream-{dream_id}",
1853	        )
1854	        t.start()
1855	        return None
1856	
1857	    py = sys.executable
1858	    proc = subprocess.Popen(
1859	        [py, str(runner)],
1860	        stdin=subprocess.PIPE,
1861	        stdout=subprocess.DEVNULL,
1862	        stderr=subprocess.DEVNULL,
1863	        start_new_session=True,
1864	        env={**os.environ},
1865	    )
1866	    proc.stdin.write(json.dumps(payload).encode("utf-8"))
1867	    proc.stdin.close()
1868	    return proc.pid
1869	
1870	
1871	def get_dream_status(project: str, dream_id: str) -> ToolResult:
1872	    """Read the current state of one Dream from the registry.
1873	
1874	    Returns the full registry entry (status / stages_completed / error / pid)
1875	    so Director can decide whether to wait, cancel, or move on. Does not
1876	    block — the orchestrator updates the registry asynchronously.
1877	    """
1878	    if not project or not dream_id:
1879	        return ToolResult(success=False, error="project and dream_id are required")
1880	    entry = _registry.get(project, dream_id)
1881	    if not entry:
1882	        return ToolResult(success=False, error=f"dream_id {dream_id!r} not found in {project!r}")
1883	    return ToolResult(success=True, data=entry)
1884	
1885	
1886	__all__ = [
1887	    "dream_simulate",
1888	    "get_dream_status",
1889	    "should_skip_dream",
1890	    "get_dream_trend",
1891	    "dispatch_dream_done",
1892	    "_collect_context",
1893	    "_compute_context_hash",
1894	    "_context_fingerprint",
1895	    "_define_tiers",
1896	    "_elaborate_scenario",
1897	    "_write_dream_paper",
1898	    "_submit_to_review",
1899	    "_persist_report",
1900	    "_run_dream_pipeline",
1901	    "_extract_yaml_block",
1902	    "_imagined_to_experiment_data",
1903	    "_summarize_for_director",
1904	    "_summarize_meta_for_trend",
1905	    "_diff_predictions",
1906	]
1907	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be082f04-2318-4df4-bbce-a71f8fa62c1a",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "e5786485-1eea-444a-a89b-6515b9ec3232",
  "sourceToolAssistantUUID": "be082f04-2318-4df4-bbce-a71f8fa62c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T20:38:13.647Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CXTyksAd1EdiDWnXzuv2TJ`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5786485-1eea-444a-a89b-6515b9ec3232",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSVDfQ6xQs2WTAgfSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1a0856f-b042-4020-99f2-8dccf078cf36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPcJFfgqcepRUdqMyyVVBd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 35891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1575,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T20:38:13.655Z_

<details><summary>↩ Tool result · `toolu_01CXTyksAd1EdiDWnXzuv2TJ`</summary>

```text
1	"""MCP Server — exposes SSH, W&B, and Registry tools via the Model Context Protocol.
2	
3	Usage:
4	    python -m core.mcp_server          # stdio transport (default, for Claude Code)
5	    python -m core.mcp_server --sse    # SSE transport (for remote clients)
6	"""
7	
8	from __future__ import annotations
9	
10	import json
11	import logging
12	import os
13	from dataclasses import asdict
14	from pathlib import Path
15	from typing import Any
16	
17	logger = logging.getLogger(__name__)
18	
19	from mcp.server.fastmcp import FastMCP
20	
21	from core.tools import (
22	    artifacts as artifacts_mod,
23	    architecture as architecture_mod,
24	    clone_repo as clone_repo_mod,
25	    cron, feishu, feishu_group as feishu_group_mod,
26	    external_review as external_review_mod,
27	    file_parser as file_parser_mod,
28	    gpu_monitor as gpu_monitor_mod,
29	    image_tools as image_tools_mod,
30	    model_registry as model_registry_mod,
31	    oss_backup, pai_eas, s3_backup,
32	    project_config, registry, ssh, wandb_client, workspace,
33	    worker as worker_mod,
34	)
35	
36	# ---------------------------------------------------------------------------
37	# Server instance
38	# ---------------------------------------------------------------------------
39	
40	mcp = FastMCP(
41	    "agent-ml-research",
42	    instructions="ML research experiment management tools",
43	)
44	
45	
46	def _tool_result_to_str(result: ssh.ToolResult) -> str:
47	    """Convert a ToolResult dataclass to a JSON string for MCP response."""
48	    return json.dumps(asdict(result), ensure_ascii=False, default=str)
49	
50	
51	# ---------------------------------------------------------------------------
52	# Chat routing helpers — resolve target chat_id from env + project config
53	# ---------------------------------------------------------------------------
54	
55	def _get_session_chat_id() -> str:
56	    """获取当前 session 绑定的群 chat_id（环境变量注入）。"""
57	    return os.environ.get("AGENT_ML_SESSION_CHAT_ID", "")
58	
59	
60	def _get_session_project() -> str:
61	    """获取当前 session 绑定的项目名。"""
62	    return os.environ.get("AGENT_ML_SESSION_PROJECT", "")
63	
64	
65	def _resolve_user_group_chat(project: str = "") -> str:
66	    """解析 A群 (user-facing group) chat_id。
67	
68	    用于目标固定发到 A群 的工具（approval_card, result_card 等）。
69	    无项目或单群模式时 fallback 到 session 所在群。
70	    """
71	    if not project:
72	        project = _get_session_project()
73	    if project:
74	        try:
75	            from core.tools.project_config import load_project_config
76	            result = load_project_config(project)
77	            if result.success:
78	                user_chat = result.data.get("config", {}).get("feishu", {}).get("chat_id", "")
79	                if user_chat:
80	                    return user_chat
81	        except Exception:
82	            pass
83	    return _get_session_chat_id()
84	
85	
86	def _resolve_ops_chat(project: str = "") -> str:
87	    """解析 B群 (operational_chat_id)，无则 fallback 到 A群。"""
88	    if not project:
89	        project = _get_session_project()
90	    if project:
91	        try:
92	            from core.tools.project_config import load_project_config
93	            result = load_project_config(project)
94	            if result.success:
95	                feishu_cfg = result.data.get("config", {}).get("feishu", {})
96	                return (
97	                    feishu_cfg.get("operational_chat_id")
98	                    or feishu_cfg.get("chat_id", "")
99	                )
100	        except Exception:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1a0856f-b042-4020-99f2-8dccf078cf36",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "efc3a0c2-82c4-4363-83cc-df56ec791121",
  "sourceToolAssistantUUID": "a1a0856f-b042-4020-99f2-8dccf078cf36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T20:38:14.069Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01P9Hj7TnPfqx5GK7n1yr4mo`</summary>

```json
{
  "pattern": "def submit_dream_review_report",
  "path": "/home/ubuntu/agent-ml-research/core",
  "output_mode": "content",
  "context": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc3a0c2-82c4-4363-83cc-df56ec791121",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSVDfQ6xQs2WTAgfSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1192decd-b5ed-410b-aee0-a8c7f6e5d1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPcJFfgqcepRUdqMyyVVBd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 35891,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1575
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 263,
          "cache_read_input_tokens": 35891,
          "cache_creation_input_tokens": 1575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1575,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T20:38:14.092Z_

<details><summary>↩ Tool result · `toolu_01P9Hj7TnPfqx5GK7n1yr4mo`</summary>

```text
/home/ubuntu/agent-ml-research/core/mcp_server.py-4883-            This guard prevents the "I forgot R3" attention-drift bug.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4884-        cross_response_reviewer_ids: REQUIRED list of integer reviewer IDs
/home/ubuntu/agent-ml-research/core/mcp_server.py-4885-            who have completed Step 2 cross-sharing — i.e. received other
/home/ubuntu/agent-ml-research/core/mcp_server.py-4886-            reviewers' reports and submitted [AGREE]/[REBUT] responses
/home/ubuntu/agent-ml-research/core/mcp_server.py-4887-            (e.g. [1, 2, 3]).  The tool rejects submission if any active
/home/ubuntu/agent-ml-research/core/mcp_server.py-4888-            reviewer is missing, ensuring cross-validation happened before
/home/ubuntu/agent-ml-research/core/mcp_server.py-4889-            the report is finalized.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4890-        overall_score: Overall assessment (e.g. "strong reject", "borderline").
/home/ubuntu/agent-ml-research/core/mcp_server.py-4891-        review_chat_id: Group C chat_id for visibility (optional).
/home/ubuntu/agent-ml-research/core/mcp_server.py-4892-        force_resubmit: Default False — if a report for the current round
/home/ubuntu/agent-ml-research/core/mcp_server.py-4893-            already exists (i.e. you previously called this tool successfully
/home/ubuntu/agent-ml-research/core/mcp_server.py-4894-            for the same round), the call is REJECTED with the existing
/home/ubuntu/agent-ml-research/core/mcp_server.py-4895-            report's path so you don't re-trigger Director's processing
/home/ubuntu/agent-ml-research/core/mcp_server.py-4896-            protocol with conflicting content.  Pass True ONLY when you
/home/ubuntu/agent-ml-research/core/mcp_server.py-4897-            intentionally want to replace the prior submission (e.g. caught
/home/ubuntu/agent-ml-research/core/mcp_server.py-4898-            a Step 2 gap and re-synthesized).  When in doubt, do NOT force —
/home/ubuntu/agent-ml-research/core/mcp_server.py-4899-            the original submission stands and Director is processing it.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4900-    """
/home/ubuntu/agent-ml-research/core/mcp_server.py-4901-    result = feishu_group_mod.submit_review_report_to_research_director(
/home/ubuntu/agent-ml-research/core/mcp_server.py-4902-        report=report, project=project,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4903-        reviewer_ids_acknowledged=reviewer_ids_acknowledged,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4904-        cross_response_reviewer_ids=cross_response_reviewer_ids,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4905-        overall_score=overall_score,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4906-        review_chat_id=review_chat_id,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4907-        force_resubmit=force_resubmit,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4908-    )
/home/ubuntu/agent-ml-research/core/mcp_server.py-4909-    return _tool_result_to_str(result)
/home/ubuntu/agent-ml-research/core/mcp_server.py-4910-
/home/ubuntu/agent-ml-research/core/mcp_server.py-4911-
/home/ubuntu/agent-ml-research/core/mcp_server.py-4912-@mcp.tool()
/home/ubuntu/agent-ml-research/core/mcp_server.py:4913:def submit_dream_review_report(
/home/ubuntu/agent-ml-research/core/mcp_server.py-4914-    report: str,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4915-    project: str,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4916-    tier: str,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4917-    dream_id: str,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4918-    overall_score: str = "",
/home/ubuntu/agent-ml-research/core/mcp_server.py-4919-    review_chat_id: str = "",
/home/ubuntu/agent-ml-research/core/mcp_server.py-4920-    review_visible: bool = True,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4921-) -> str:
/home/ubuntu/agent-ml-research/core/mcp_server.py-4922-    """Deliver a Dream-mode review report (Dream Review Director only).
/home/ubuntu/agent-ml-research/core/mcp_server.py-4923-
/home/ubuntu/agent-ml-research/core/mcp_server.py-4924-    Persists the review to ``dream_reports/{dream_id}/{tier}/review_report.md``
/home/ubuntu/agent-ml-research/core/mcp_server.py-4925-    and (optionally) posts a Group C visibility card. The Dream Tool reads
/home/ubuntu/agent-ml-research/core/mcp_server.py-4926-    the file once your subprocess exits — there is NO Research Director
/home/ubuntu/agent-ml-research/core/mcp_server.py-4927-    delivery, NO ``review_reports/round_N.md``, NO ``review_issues.yaml``,
/home/ubuntu/agent-ml-research/core/mcp_server.py-4928-    and NO 5-step protocol attached.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4929-
/home/ubuntu/agent-ml-research/core/mcp_server.py-4930-    Use this in place of ``submit_review_report_to_research_director`` for
/home/ubuntu/agent-ml-research/core/mcp_server.py-4931-    Dream-mode roundtable Step 4. See DREAM_AGENT_DESIGN.md §6.4.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4932-
/home/ubuntu/agent-ml-research/core/mcp_server.py-4933-    Args:
/home/ubuntu/agent-ml-research/core/mcp_server.py-4934-        report: Consolidated review report text (covers all Dream reviewers).
/home/ubuntu/agent-ml-research/core/mcp_server.py-4935-        project: Current project name.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4936-        tier: Which Dream tier this report covers — ``best`` / ``median``
/home/ubuntu/agent-ml-research/core/mcp_server.py-4937-            / ``worst``.
/home/ubuntu/agent-ml-research/core/mcp_server.py-4938-        dream_id: Dream invocation id (with or without the ``dream_`` prefix —
/home/ubuntu/agent-ml-research/core/mcp_server.py-4939-            both accepted).
/home/ubuntu/agent-ml-research/core/mcp_server.py-4940-        overall_score: Optional headline assessment ("strong reject",
/home/ubuntu/agent-ml-research/core/mcp_server.py-4941-            "borderline accept", etc.).
/home/ubuntu/agent-ml-research/core/mcp_server.py-4942-        review_chat_id: Group C chat_id (loaded from project config when empty).
/home/ubuntu/agent-ml-research/core/mcp_server.py-4943-        review_visible: When True (default) posts a visibility card to Group C
--
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1214-    except Exception:
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1215-        # MCP subprocess path: SessionServer not available — use HTTP internal API.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1216-        try:
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1217-            import urllib.request as _req
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1218-            import json as _json
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1219-            payload = _json.dumps({
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1220-                "session_key": research_director_key,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1221-                "project": project,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1222-                "message": report_msg,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1223-                "reply_chat_id": research_chat_id,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1224-                "source": "submission_review_report",
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1225-            }).encode()
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1226-            r = _req.urlopen(
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1227-                _req.Request(
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1228-                    f"http://localhost:{_API_PORT}/api/internal/session-send",
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1229-                    data=payload,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1230-                    headers={"Content-Type": "application/json"},
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1231-                ),
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1232-                timeout=30,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1233-            )
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1234-            resp_body = _json.loads(r.read())
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1235-            if resp_body.get("status") not in ("queued", "sent"):
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1236-                return ToolResult(success=False, data={}, error=f"session-send API error: {resp_body}")
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1237-            logger.info("[submit_review_report→research_director] HTTP-routed to %s", research_director_key)
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1238-            return ToolResult(success=True, data={"research_director_key": research_director_key})
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1239-        except Exception as exc2:
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1240-            logger.exception("[submit_review_report] failed for project=%s", project)
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1241-            return ToolResult(success=False, data={}, error=str(exc2))
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1242-
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1243-
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py:1244:def submit_dream_review_report(
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1245-    report: str,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1246-    project: str,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1247-    tier: str,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1248-    dream_id: str,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1249-    overall_score: str = "",
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1250-    review_chat_id: str = "",
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1251-    review_visible: bool = True,
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1252-) -> ToolResult:
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1253-    """Persist a Dream-mode review report and signal completion.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1254-
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1255-    Used by the Dream Review Director in place of
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1256-    ``submit_review_report_to_research_director``. Differences from the real
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1257-    submission tool (DREAM_AGENT_DESIGN.md §6.4):
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1258-
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1259-    * Writes only to ``dream_reports/{dream_id}/{tier}/review_report.md`` —
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1260-      no ``review_reports/round_N.md``, no ``review_issues.yaml``.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1261-    * Does NOT send the report to Research Director. The Dream Tool
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1262-      orchestrator reads the file once the subprocess exits.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1263-    * Skips the roster / cross-sharing guards — those are Research-side
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1264-      protocol that Dream's simplified pipeline doesn't enforce.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1265-    * ``review_visible=False`` suppresses the Group C visibility card.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1266-
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1267-    Args:
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1268-        report: Full review report text (consolidated from all reviewers).
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1269-        project: Project name.
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1270-        tier: Which Dream tier this report covers (best/median/worst).
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1271-        dream_id: Dream invocation id (must include the ``dream_`` prefix
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1272-            stripped — caller passes the raw id, not the ``dream_xxx``
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1273-            segment).
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py-1274-        overall_score: Optional headline assessment ("strong reject", etc.).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1192decd-b5ed-410b-aee0-a8c7f6e5d1fd",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "915dfb52-4218-44e0-b1ff-ad99bb61da58",
  "sourceToolAssistantUUID": "1192decd-b5ed-410b-aee0-a8c7f6e5d1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-12T20:38:15.889Z_

Let me get more details from the implementation in feishu_group.py:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "915dfb52-4218-44e0-b1ff-ad99bb61da58",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSeUmwPhXSWp1rKqNf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f0a5bb1-1830-4279-a4a9-eea1425775e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A9tqSKFqN5uT6ojj3wEsCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 32683,
      "cache_read_input_tokens": 37466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T20:38:16.156Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YNyUDM3RbT1bBg3WqptT7C`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/feishu_group.py",
  "offset": 1244,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f0a5bb1-1830-4279-a4a9-eea1425775e8",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSeUmwPhXSWp1rKqNf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b96a25e3-e4e2-4759-a740-e137d2db7ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A9tqSKFqN5uT6ojj3wEsCw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 32683,
      "cache_read_input_tokens": 37466,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 127,
          "cache_read_input_tokens": 37466,
          "cache_creation_input_tokens": 32683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32683,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T20:38:16.161Z_

<details><summary>↩ Tool result · `toolu_01YNyUDM3RbT1bBg3WqptT7C`</summary>

```text
1244	def submit_dream_review_report(
1245	    report: str,
1246	    project: str,
1247	    tier: str,
1248	    dream_id: str,
1249	    overall_score: str = "",
1250	    review_chat_id: str = "",
1251	    review_visible: bool = True,
1252	) -> ToolResult:
1253	    """Persist a Dream-mode review report and signal completion.
1254	
1255	    Used by the Dream Review Director in place of
1256	    ``submit_review_report_to_research_director``. Differences from the real
1257	    submission tool (DREAM_AGENT_DESIGN.md §6.4):
1258	
1259	    * Writes only to ``dream_reports/{dream_id}/{tier}/review_report.md`` —
1260	      no ``review_reports/round_N.md``, no ``review_issues.yaml``.
1261	    * Does NOT send the report to Research Director. The Dream Tool
1262	      orchestrator reads the file once the subprocess exits.
1263	    * Skips the roster / cross-sharing guards — those are Research-side
1264	      protocol that Dream's simplified pipeline doesn't enforce.
1265	    * ``review_visible=False`` suppresses the Group C visibility card.
1266	
1267	    Args:
1268	        report: Full review report text (consolidated from all reviewers).
1269	        project: Project name.
1270	        tier: Which Dream tier this report covers (best/median/worst).
1271	        dream_id: Dream invocation id (must include the ``dream_`` prefix
1272	            stripped — caller passes the raw id, not the ``dream_xxx``
1273	            segment).
1274	        overall_score: Optional headline assessment ("strong reject", etc.).
1275	        review_chat_id: Group C chat_id (loaded from project config if empty).
1276	        review_visible: When False, skip Group C post.
1277	    """
1278	    if not project:
1279	        return ToolResult(success=False, data={}, error="project is required")
1280	    if not dream_id:
1281	        return ToolResult(success=False, data={}, error="dream_id is required")
1282	    if tier not in {"best", "median", "worst"}:
1283	        return ToolResult(
1284	            success=False, data={},
1285	            error=f"tier must be one of best/median/worst, got {tier!r}",
1286	        )
1287	    if not report or not report.strip():
1288	        return ToolResult(success=False, data={}, error="report must be non-empty")
1289	
1290	    from core import paths as _paths_mod
1291	
1292	    # Normalize: callers occasionally pass the full session segment.
1293	    dream_id = dream_id.removeprefix("dream_")
1294	    canonical_id = f"dream_{dream_id}"
1295	
1296	    output_dir = _paths_mod.dream_report_dir(project, canonical_id) / tier
1297	    output_dir.mkdir(parents=True, exist_ok=True)
1298	    report_path = output_dir / "review_report.md"
1299	
1300	    import datetime as _dt
1301	    header = (
1302	        f"---\n"
1303	        f"dream_id: {canonical_id}\n"
1304	        f"tier: {tier}\n"
1305	        f"overall_score: {overall_score}\n"
1306	        f"timestamp: {_dt.datetime.now(_dt.timezone.utc).isoformat()}\n"
1307	        f"---\n\n"
1308	    )
1309	    try:
1310	        report_path.write_text(header + report, encoding="utf-8")
1311	        logger.info(
1312	            "[submit_dream_review_report] wrote %s (%d bytes)",
1313	            report_path, report_path.stat().st_size,
1314	        )
1315	    except Exception as exc:
1316	        logger.exception(
1317	            "[submit_dream_review_report] failed to write %s", report_path,
1318	        )
1319	        return ToolResult(success=False, data={}, error=str(exc))
1320	
1321	    # Optional Group C visibility — mirrors the real submission tool but
1322	    # without the Research Director routing step.
1323	    if review_visible:
1324	        if not review_chat_id:
1325	            try:
1326	                from core.tools.project_config import load_review_chat_id
1327	                review_chat_id = load_review_chat_id(project)
1328	            except Exception:
1329	                review_chat_id = ""
1330	        if review_chat_id:
1331	            try:
1332	                from core.tools.feishu import send_message as _send_msg
1333	                header_line = (
1334	                    f"🌙 **[Dream Review Report — {tier}]**"
1335	                    f"{(' · Overall: ' + overall_score) if overall_score else ''}"
1336	                )
1337	                _send_msg(chat_id=review_chat_id, text=f"{header_line}\n{report}")
1338	            except Exception:
1339	                logger.exception(
1340	                    "[submit_dream_review_report] Group C visibility post failed",
1341	                )
1342	
1343	    return ToolResult(
1344	        success=True,
1345	        data={
1346	            "report_path": str(report_path),
1347	            "dream_id": canonical_id,
1348	            "tier": tier,
1349	            "review_visible": review_visible,
1350	        },
1351	    )
1352	
1353	
1354	def update_review_issues(project: str, issues_yaml: str) -> ToolResult:
1355	    """Update the cross-round review issue tracker.
1356	
1357	    Both Review Director and Research Director call this — Review Director
1358	    after synthesizing a report (mark new/recurring/possibly-resolved
1359	    issues), Research Director after locking the Action Matrix (flip
1360	    open → in_progress, in_progress → resolved).
1361	
1362	    The caller passes the FULL YAML content; the tool overwrites
1363	    `projects/{project}/artifacts/review_issues.yaml` atomically.  Reading
1364	    the existing tracker is via `read_local_file` — no separate read tool
1365	    is needed.
1366	
1367	    Args:
1368	        project: Current project name.
1369	        issues_yaml: Complete YAML content for the issue tracker.  Must
1370	            be valid YAML (validated before write — invalid YAML is
1371	            rejected to avoid silently corrupting the tracker).
1372	    """
1373	    try:
1374	        import yaml as _yaml
1375	    except Exception as exc:
1376	        return ToolResult(success=False, data={}, error=f"PyYAML unavailable: {exc}")
1377	    try:
1378	        _yaml.safe_load(issues_yaml)
1379	    except Exception as exc:
1380	        return ToolResult(
1381	            success=False, data={},
1382	            error=f"issues_yaml is not valid YAML: {exc}",
1383	        )
1384	    try:
1385	        from core import paths as _paths_mod
1386	        artifacts_dir = _paths_mod.project_dir(project) / "artifacts"
1387	        artifacts_dir.mkdir(parents=True, exist_ok=True)
1388	        target = artifacts_dir / "review_issues.yaml"
1389	        # Atomic write: tmp-then-rename so a crash mid-write doesn't
1390	        # leave a half-written tracker.
1391	        tmp = target.with_suffix(".yaml.tmp")
1392	        tmp.write_text(issues_yaml, encoding="utf-8")
1393	        tmp.replace(target)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b96a25e3-e4e2-4759-a740-e137d2db7ca8",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "5f56484e-9f45-4c31-84a9-df3054b912d7",
  "sourceToolAssistantUUID": "b96a25e3-e4e2-4759-a740-e137d2db7ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T20:38:17.211Z_

Now let me search for more test files to see usage patterns:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f56484e-9f45-4c31-84a9-df3054b912d7",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSoNK9SoNZdUJEqrHo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "24e1d37a-e298-4094-89d4-739168644439",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LXW5bXLKAqbDgFQtZGZg6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2261,
      "cache_read_input_tokens": 70149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2261,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T20:38:17.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J9WVPjAm3rMAFM9MUVmQPP`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/tests/test_dream_review_report_delivery.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e1d37a-e298-4094-89d4-739168644439",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSoNK9SoNZdUJEqrHo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b0b3bb67-599d-4227-a4b6-cb15e2eceede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LXW5bXLKAqbDgFQtZGZg6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2261,
      "cache_read_input_tokens": 70149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2261,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T20:38:17.869Z_

<details><summary>↩ Tool result · `toolu_01J9WVPjAm3rMAFM9MUVmQPP`</summary>

```text
1	"""Dream review report delivery (Phase 3 task 3-T7).
2	
3	Pins the contract that ``submit_dream_review_report`` in Dream mode
4	**does NOT** route through the real-review 5-step delivery protocol.
5	DREAM_AGENT_DESIGN.md §6.5 sets the contrast:
6	
7	  | 报告送达 | → Research Director（5-step protocol） | → Dream Tool → Director（无 protocol） |
8	
9	The 5-step protocol normally injected with the real ``submit_review_report_
10	to_research_director`` flow (item-by-item triage, post-to-reviewer for
11	independent review, issue tracker sync, etc.) is irrelevant to Dream —
12	the orchestrator reads the report file directly and surfaces the
13	DreamScenarioResult to the Director. If a regression copies the protocol
14	into the Dream path, the Dream Director suddenly gets a 5-step "rebuttal
15	plan" injection for a *simulated* paper, which is both noisy and wrong.
16	
17	Pillars:
18	
19	  D1. **No 5-step protocol append** — the saved report file contains the
20	      raw report (with a small Dream-specific header) and nothing
21	      resembling the real ``_REVIEW_REPORT_PROTOCOL`` text.
22	  D2. **Does not call Research Director routing** — the function never
23	      calls ``_find_research_director_for_project`` / ``send_sync`` to
24	      the Research Director session.
25	  D3. **Direct file-based delivery** — the orchestrator reads the report
26	      via the filesystem (``review_report.md``), not via an in-memory
27	      MCP callback, matching the design's "subprocess exit is the signal"
28	      pattern.
29	  D4. **No issue tracker write** — Dream does not touch
30	      ``review_issues.yaml`` (cross-round tracker).
31	  D5. **No 'round_N.md' artifact** — Dream writes to ``dream_reports/{id}
32	      /{tier}/review_report.md``, never to ``review_reports/round_N.md``.
33	"""
34	
35	from __future__ import annotations
36	
37	from pathlib import Path
38	from unittest.mock import MagicMock, patch
39	
40	import pytest
41	
42	
43	PROJECT = "proj_delivery"
44	DREAM_ID = "dd_delivery"
45	TIER = "best"
46	CHAT_ID = "oc_review"
47	
48	
49	# ---------------------------------------------------------------------------
50	# D1. No 5-step protocol appended to the persisted report
51	# ---------------------------------------------------------------------------
52	
53	
54	class TestNoFiveStepProtocolInPersistedReport:
55	    """The on-disk Dream review report is exactly what the Director wrote,
56	    plus a small Dream header. No 5-step "must call post_to_reviewer /
57	    update_review_issues" text gets appended."""
58	
59	    def test_persisted_report_has_no_5_step_protocol(self, workspace):
60	        from core.tools.feishu_group import submit_dream_review_report
61	        from core import paths as _paths
62	        with (
63	            patch("core.tools.project_config.load_review_chat_id", return_value=""),
64	        ):
65	            res = submit_dream_review_report(
66	                report="The paper is solid. Score: weak accept.",
67	                project=PROJECT, tier=TIER, dream_id=DREAM_ID,
68	                overall_score="weak accept",
69	                review_visible=False,
70	            )
71	        assert res.success is True
72	        report_path = (
73	            _paths.dream_report_dir(PROJECT, f"dream_{DREAM_ID}") / TIER /
74	            "review_report.md"
75	        )
76	        body = report_path.read_text(encoding="utf-8")
77	        # The 5-step protocol's anchor phrases — none must appear.
78	        forbidden_phrases = [
79	            "处理协议",
80	            "逐条编号通读",
81	            "post_to_reviewer 让 Research Reviewer 补充意见",
82	            "同步 Issue Tracker",
83	            "Action Matrix",
84	            "review_issues.yaml",
85	        ]
86	        for phrase in forbidden_phrases:
87	            assert phrase not in body, (
88	                f"5-step protocol phrase leaked into Dream report: {phrase!r}"
89	            )
90	
91	    def test_persisted_report_keeps_raw_review_body(self, workspace):
92	        """The raw body the Director passed in must appear verbatim
93	        (modulo a Dream header prefix)."""
94	        from core.tools.feishu_group import submit_dream_review_report
95	        from core import paths as _paths
96	        body = "The methodology is novel. Reviewer 2 raised X. Score: borderline."
97	        with patch(
98	            "core.tools.project_config.load_review_chat_id", return_value="",
99	        ):
100	            res = submit_dream_review_report(
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0b3bb67-599d-4227-a4b6-cb15e2eceede",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "c6c6bf40-ff7a-45b1-a973-1ee04b14ab6b",
  "sourceToolAssistantUUID": "b0b3bb67-599d-4227-a4b6-cb15e2eceede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-12T20:38:18.296Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015GMP5ih5oW4WaXaVnMTRuD`</summary>

```json
{
  "pattern": "submit_dream_review_report.*\\(",
  "path": "/home/ubuntu/agent-ml-research/tests",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c6bf40-ff7a-45b1-a973-1ee04b14ab6b",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSoNK9SoNZdUJEqrHo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "284685e6-f74b-491a-aec4-b3a27e48592d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LXW5bXLKAqbDgFQtZGZg6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2261,
      "cache_read_input_tokens": 70149,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2261
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 215,
          "cache_read_input_tokens": 70149,
          "cache_creation_input_tokens": 2261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2261,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T20:38:18.324Z_

<details><summary>↩ Tool result · `toolu_015GMP5ih5oW4WaXaVnMTRuD`</summary>

```text
&lt;persisted-output>
Output too large (27.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3/tool-results/toolu_015GMP5ih5oW4WaXaVnMTRuD.txt

Preview (first 2KB):
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-91-    def test_dispatch_signals_converge_step(self):
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-92-        prompt = self._dispatch()
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-93-        assert "Step 3" in prompt
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-94-        assert "收敛" in prompt or "converge" in prompt.lower()
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-95-
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py:96:    def test_dispatch_names_submit_dream_review_report(self):
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-97-        prompt = self._dispatch()
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-98-        assert "submit_dream_review_report" in prompt
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-99-
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-100-    def test_dispatch_carries_dream_id_and_tier(self):
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-101-        prompt = self._dispatch()
--
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-179-        """Dispatch templates must explicitly target both reviewer_id="1"
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-180-        and reviewer_id="2"."""
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-181-        assert 'reviewer_id="1"' in skill_text
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-182-        assert 'reviewer_id="2"' in skill_text
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-183-
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py:184:    def test_skill_names_submit_dream_review_report(self, skill_text):
/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py-185-        assert "submit_dream_review_report" in skill_text
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "284685e6-f74b-491a-aec4-b3a27e48592d",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "390cba15-ef1d-4734-a7f9-270817af708d",
  "sourceToolAssistantUUID": "284685e6-f74b-491a-aec4-b3a27e48592d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T20:38:19.894Z_

Perfect! Now let me check the MCP server registration to see the full tool definition:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "390cba15-ef1d-4734-a7f9-270817af708d",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSxTkohJA7UVmgeh1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4937f547-cfe2-4613-b11d-2fb2f0bd9a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016FdUc4yB2oJFTu21F1m4RK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 72410,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2549,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T20:38:20.389Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WJa5CawbndNJVhQxSUvyfX`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "offset": 4912,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4937f547-cfe2-4613-b11d-2fb2f0bd9a50",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKSxTkohJA7UVmgeh1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "869d60a4-ae14-4294-9b9f-c766062fe62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016FdUc4yB2oJFTu21F1m4RK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2549,
      "cache_read_input_tokens": 72410,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 125,
          "cache_read_input_tokens": 72410,
          "cache_creation_input_tokens": 2549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2549,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T20:38:20.394Z_

<details><summary>↩ Tool result · `toolu_01WJa5CawbndNJVhQxSUvyfX`</summary>

```text
4912	@mcp.tool()
4913	def submit_dream_review_report(
4914	    report: str,
4915	    project: str,
4916	    tier: str,
4917	    dream_id: str,
4918	    overall_score: str = "",
4919	    review_chat_id: str = "",
4920	    review_visible: bool = True,
4921	) -> str:
4922	    """Deliver a Dream-mode review report (Dream Review Director only).
4923	
4924	    Persists the review to ``dream_reports/{dream_id}/{tier}/review_report.md``
4925	    and (optionally) posts a Group C visibility card. The Dream Tool reads
4926	    the file once your subprocess exits — there is NO Research Director
4927	    delivery, NO ``review_reports/round_N.md``, NO ``review_issues.yaml``,
4928	    and NO 5-step protocol attached.
4929	
4930	    Use this in place of ``submit_review_report_to_research_director`` for
4931	    Dream-mode roundtable Step 4. See DREAM_AGENT_DESIGN.md §6.4.
4932	
4933	    Args:
4934	        report: Consolidated review report text (covers all Dream reviewers).
4935	        project: Current project name.
4936	        tier: Which Dream tier this report covers — ``best`` / ``median``
4937	            / ``worst``.
4938	        dream_id: Dream invocation id (with or without the ``dream_`` prefix —
4939	            both accepted).
4940	        overall_score: Optional headline assessment ("strong reject",
4941	            "borderline accept", etc.).
4942	        review_chat_id: Group C chat_id (loaded from project config when empty).
4943	        review_visible: When True (default) posts a visibility card to Group C
4944	            with a ``[Dream]`` prefix. Set False for silent submission.
4945	    """
4946	    result = feishu_group_mod.submit_dream_review_report(
4947	        report=report,
4948	        project=project,
4949	        tier=tier,
4950	        dream_id=dream_id,
4951	        overall_score=overall_score,
4952	        review_chat_id=review_chat_id,
4953	        review_visible=review_visible,
4954	    )
4955	    return _tool_result_to_str(result)
4956	
4957	
4958	@mcp.tool()
4959	def request_external_review(
4960	    project: str,
4961	    paper_pdf_path: str,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "869d60a4-ae14-4294-9b9f-c766062fe62c",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "e52033bc-057a-480b-a9e4-9ff7339601db",
  "sourceToolAssistantUUID": "869d60a4-ae14-4294-9b9f-c766062fe62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-12T20:38:21.922Z_

Perfect! Now let me get a summary of the artifact directory where it writes:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e52033bc-057a-480b-a9e4-9ff7339601db",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKT7MJLFqrBdTFtBSTP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3af5bbe8-5eb6-48aa-ac11-9f04f3c70fa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016zNQw5k3H2EApqBZV7Kjtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 74959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 820,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-12T20:38:22.204Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013ZXzF3TFDzyjdAqCkhYtQ1`</summary>

```json
{
  "command": "cd /home/ubuntu && find . -path \"*dream_reports*\" -type d 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3af5bbe8-5eb6-48aa-ac11-9f04f3c70fa5",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKT7MJLFqrBdTFtBSTP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0121f43-8e61-43b7-8938-4d9133a065bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016zNQw5k3H2EApqBZV7Kjtf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 74959,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 820
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 97,
          "cache_read_input_tokens": 74959,
          "cache_creation_input_tokens": 820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 820,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T20:38:22.477Z_

<details><summary>↩ Tool result · `toolu_013ZXzF3TFDzyjdAqCkhYtQ1`</summary>

```text
./.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports
./.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328
./.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median
./.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/logs
./.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst
./.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0121f43-8e61-43b7-8938-4d9133a065bc",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "c130b3a5-4580-42fd-985c-f593d46e3790",
  "sourceToolAssistantUUID": "a0121f43-8e61-43b7-8938-4d9133a065bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-12T20:38:23.649Z_

Let me check the paths module to understand the paths structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c130b3a5-4580-42fd-985c-f593d46e3790",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKTGDM7pq2ELGHdPvzY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a75c256-b83d-44bc-8915-cef638b156c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzqgoCBomKGTgKJSPsBQdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 75779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 352,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T20:38:24.109Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QdA9dvceC7y9tbSLntreet`</summary>

```json
{
  "command": "cd /home/ubuntu && grep -n \"dream_report_dir\\|dream_reports_dir\" agent-ml-research/core/paths.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a75c256-b83d-44bc-8915-cef638b156c8",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKTGDM7pq2ELGHdPvzY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b45fcb7d-f10b-4ec3-9319-f1a7b0edc328",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HzqgoCBomKGTgKJSPsBQdw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 75779,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 352
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 102,
          "cache_read_input_tokens": 75779,
          "cache_creation_input_tokens": 352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 352,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T20:38:24.163Z_

<details><summary>↩ Tool result · `toolu_01QdA9dvceC7y9tbSLntreet`</summary>

```text
443:def dream_reports_dir(project: str) -> Path:
453:def dream_report_dir(project: str, dream_id: str) -> Path:
461:    return dream_reports_dir(project) / dream_id
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b45fcb7d-f10b-4ec3-9319-f1a7b0edc328",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "61643306-c0ab-444a-8567-ba509a0f6161",
  "sourceToolAssistantUUID": "b45fcb7d-f10b-4ec3-9319-f1a7b0edc328",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T20:38:25.611Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q9WFCoKAwUFAQ47vhF8YfH`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/paths.py",
  "offset": 443,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61643306-c0ab-444a-8567-ba509a0f6161",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKTPPhduPwiDtiXLmJB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd9188da-acf8-43b5-9146-6adeec5f9e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LSCoxZziDva5vLpgoDKwtS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 76131,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 170
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 102,
          "cache_read_input_tokens": 76131,
          "cache_creation_input_tokens": 170,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 170,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T20:38:25.627Z_

<details><summary>↩ Tool result · `toolu_01Q9WFCoKAwUFAQ47vhF8YfH`</summary>

```text
443	def dream_reports_dir(project: str) -> Path:
444	    """Root directory for all Dream Tool reports of a project.
445	
446	    Layout: projects/{project}/artifacts/dream_reports/{dream_id}/...
447	    Kept inside ``artifacts/`` so Dream outputs flow through the same
448	    backup/cleanup paths as other run artifacts.
449	    """
450	    return project_artifacts_dir(project) / "dream_reports"
451	
452	
453	def dream_report_dir(project: str, dream_id: str) -> Path:
454	    """Per-dream report directory.
455	
456	    Holds three tier subdirectories (best/median/worst), the synthesized
457	    meta.yaml, and ``logs/`` for subprocess stdout/stderr.
458	    """
459	    if not dream_id:
460	        raise ValueError("dream_id is required")
461	    return dream_reports_dir(project) / dream_id
462	
463	
464	def dream_registry_path(project: str) -> Path:
465	    """Persistent state for in-flight Dream runs."""
466	    return project_dir(project) / "dream_registry.yaml"
467	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd9188da-acf8-43b5-9146-6adeec5f9e68",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "84518c9d-f22a-4920-9083-b06b69dc660a",
  "sourceToolAssistantUUID": "dd9188da-acf8-43b5-9146-6adeec5f9e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-12T20:38:26.989Z_

Now let me look for any documentation or additional context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84518c9d-f22a-4920-9083-b06b69dc660a",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKTVof3wyT3mxZ9H56b",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6eeeae7-70e0-4e33-9a9d-1bad8cc218bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QkmAYA4Tb9MCL1WB3F6QZs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 76301,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 91,
          "cache_read_input_tokens": 76301,
          "cache_creation_input_tokens": 413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 413,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-12T20:38:27.055Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QASZE4kbJmKUdxMhhCEYVD`</summary>

```json
{
  "command": "cd /home/ubuntu && find agent-ml-research -name \"*DREAM*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6eeeae7-70e0-4e33-9a9d-1bad8cc218bd",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKTVof3wyT3mxZ9H56b",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "20c6af73-d05c-4be9-b1c2-57ea3e85a66e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QkmAYA4Tb9MCL1WB3F6QZs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 413,
      "cache_read_input_tokens": 76301,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 91,
          "cache_read_input_tokens": 76301,
          "cache_creation_input_tokens": 413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 413,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T20:38:27.229Z_

<details><summary>↩ Tool result · `toolu_01QASZE4kbJmKUdxMhhCEYVD`</summary>

```text
agent-ml-research/docs/plans/DREAM_FEEDBACK_ACTION_PROTOCOL.md
agent-ml-research/docs/plans/DREAM_AGENT_DESIGN.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20c6af73-d05c-4be9-b1c2-57ea3e85a66e",
  "isSidechain": true,
  "promptId": "a542fdf3-735d-4549-af74-dd35edd5f0cc",
  "agentId": "ab2395d53af5bcdca",
  "type": "user",
  "uuid": "f46c315b-cd2f-4206-888c-be9b2fcafa06",
  "sourceToolAssistantUUID": "20c6af73-d05c-4be9-b1c2-57ea3e85a66e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-12T20:38:38.562Z_

Perfect! Now I have enough information. Let me compile my findings:

## Summary

I found **`submit_dream_review_report`** — it's a Python function that exists as both an MCP tool handler and a core implementation. Here's the complete picture:

### File Locations

1. **MCP Tool Handler (exported)**: `/home/ubuntu/agent-ml-research/core/mcp_server.py:4913-4955`
2. **Core Implementation**: `/home/ubuntu/agent-ml-research/core/tools/feishu_group.py:1244-1351`
3. **Referenced in Tests**: Multiple test files including:
   - `/home/ubuntu/agent-ml-research/tests/test_dream_review_report_delivery.py`
   - `/home/ubuntu/agent-ml-research/tests/test_dream_review_full.py`
   - `/home/ubuntu/agent-ml-research/tests/test_dream_review_simple.py`

### Function Signature

```python
def submit_dream_review_report(
    report: str,
    project: str,
    tier: str,
    dream_id: str,
    overall_score: str = "",
    review_chat_id: str = "",
    review_visible: bool = True,
) -> ToolResult:
```

### Parameters

- **`report`**: Full review report text (consolidated from all reviewers) — must be non-empty
- **`project`**: Current project name (required)
- **`tier`**: Which Dream tier this report covers — must be one of `best`, `median`, or `worst` (required)
- **`dream_id`**: Dream invocation id (with or without the `dream_` prefix — both accepted; required)
- **`overall_score`**: Optional headline assessment (e.g., "strong reject", "borderline accept")
- **`review_chat_id`**: Group C Feishu chat_id; auto-loaded from project config if empty
- **`review_visible`**: When `True` (default), posts a visibility card to Group C with a `[Dream]` prefix; when `False`, suppresses the post

### What It Writes

The function writes to the file system at this location:

```
projects/{project}/artifacts/dream_reports/{dream_id}/{tier}/review_report.md
```

Example path: `projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/review_report.md`

The file is persisted with a YAML frontmatter header containing:

```yaml
---
dream_id: {canonical_id}
tier: {tier}
overall_score: {score}
timestamp: {iso_timestamp}
---

{report_body}
```

### Key Design Characteristics

1. **No 5-step Protocol**: Unlike the real `submit_review_report_to_research_director`, this function does NOT append any review handling protocol, Action Matrix, or workflow text.

2. **No Research Director Routing**: The report is NOT sent to the Research Director session. Instead, the Dream Tool orchestrator reads the file directly from disk once the Dream Review Director subprocess exits.

3. **No Issue Tracker Updates**: Does not touch `review_issues.yaml` (the cross-round review tracker).

4. **No round_N.md Artifacts**: Writes only to `dream_reports/{id}/{tier}/review_report.md`, never to `review_reports/round_N.md`.

5. **Optional Group C Visibility**: When `review_visible=True`, posts the report to Group C Feishu chat. When `False`, submission is silent.

### Return Value

Returns a `ToolResult` with:
- **`success`**: boolean
- **`data`**: dict containing:
  - `report_path`: absolute path to the written file
  - `dream_id`: canonical dream_id with `dream_` prefix
  - `tier`: the tier processed
  - `review_visible`: whether visibility was posted
- **`error`**: error message if failed

### Integration Flow (from dream.py)

The function is called by the Dream pipeline at line 1035 in `/home/ubuntu/agent-ml-research/core/tools/dream.py`:

```python
submit_dream_review_report(report, project="{project}", tier="{tier}", 
                          dream_id="{dream_id_bare}", review_visible={review_visible})
```

This happens in the Dream Review Director subprocess (`_run_dream_review_director_subprocess`), which is spawned for each tier during the review phase of the dream pipeline. Once the subprocess exits, the orchestrator reads the persisted report file and includes it in the `DreamOutput`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f46c315b-cd2f-4206-888c-be9b2fcafa06",
  "isSidechain": true,
  "agentId": "ab2395d53af5bcdca",
  "requestId": "req_011CayKTcVzLmWL2fnUrX2DV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4f7e920-d69c-4a29-9c41-33e3c4222583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7bbb8f4a-1a6d-47fd-bcb4-79574df0a9b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R3pYc4H7DEdgAmASpvxRAH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 146,
      "cache_read_input_tokens": 76714,
      "output_tokens": 1109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1109,
          "cache_read_input_tokens": 76714,
          "cache_creation_input_tokens": 146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 146,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
