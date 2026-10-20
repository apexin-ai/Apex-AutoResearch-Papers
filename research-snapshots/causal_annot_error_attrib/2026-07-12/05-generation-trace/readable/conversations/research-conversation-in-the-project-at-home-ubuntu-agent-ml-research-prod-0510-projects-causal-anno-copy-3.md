# Research conversation: In the project at /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/, I need to find code tha

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aac218afbfff5d245.jsonl`
- **Structured JSON:** [`c87912a1c8d95278f0eb.json`](../../sessions/c8/c87912a1c8d95278f0eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-24T05:50:37.355Z_

In the project at /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/, I need to find code that computes 7-topology analytical bias from confusion matrices. Look at:
1. `artifacts/compute_updated_empirical.py` - how it computes biases
2. `artifacts/compute_all_tasks.py` - similar
3. `annot_sensitivity/` package - look for bias computation functions, ASV computation, topology definitions
4. Any other script that does the 7-topology bias analysis

I need to understand:
- What function computes analytical bias given a confusion matrix and topology?
- What are the 7 topologies and their parameter configs?
- How is ASV computed?
- How are sign flips counted?

Report the key function signatures, file paths, and how to call them. Be thorough - read the relevant source files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "e28222cb-e4ed-4cb9-886c-58c71e3dde33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T05:50:44.727Z_

I'll help you find and understand the code for computing 7-topology analytical bias. Let me start by exploring the project structure and then examine the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e28222cb-e4ed-4cb9-886c-58c71e3dde33",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsTrKkNVw167dLJzJMT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0e572d0-6735-4d27-8293-79c11d189731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146eftoY5eGhVajpXJsnous",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 636,
      "cache_read_input_tokens": 15920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 636,
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

_source line 3 · 2026-05-24T05:50:45.218Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UwQ5USQ4Re7zW58L2MvxWu`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -type f -name \"*.py\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0e572d0-6735-4d27-8293-79c11d189731",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsTrKkNVw167dLJzJMT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31dee1af-2949-4c59-a21b-5f730040d167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146eftoY5eGhVajpXJsnous",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 636,
      "cache_read_input_tokens": 15920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 636,
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

_source line 4 · 2026-05-24T05:50:45.273Z_

<details><summary>↩ Tool result · `toolu_01UwQ5USQ4Re7zW58L2MvxWu`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_010_ppi_empirical_validation.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig1.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig7.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig2.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_diagnostic_plots.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig3.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/figures/paper/gen_fig4.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/_globals.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/_pytesttester.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/hermite_e.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/polynomial.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_legendre.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_polyutils.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_symbol.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_hermite_e.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_hermite.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_polynomial.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_laguerre.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_printing.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/__init__.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_classes.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/tests/test_chebyshev.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/hermite.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/laguerre.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/_polybase.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/chebyshev.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/legendre.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/__init__.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.venv/lib/python3.14/site-packages/numpy/polynomial/polyutils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31dee1af-2949-4c59-a21b-5f730040d167",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "e832a134-4724-4d16-bae9-349a92c2c4d9",
  "sourceToolAssistantUUID": "31dee1af-2949-4c59-a21b-5f730040d167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T05:50:46.755Z_

Let me look at the project structure more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e832a134-4724-4d16-bae9-349a92c2c4d9",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUSM8nhFZc1qqSPTXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b725bf65-893a-4ed0-9708-e09d7c07015e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012b1G3UuJcgMtZGH8HFyNfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 16556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2482,
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

_source line 6 · 2026-05-24T05:50:47.138Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BoHadVcNHzfzHJdBjEBU2n`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/ | grep -E \"^d|^-\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b725bf65-893a-4ed0-9708-e09d7c07015e",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUSM8nhFZc1qqSPTXz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38243439-e3b9-442a-b8ac-c73651b4e083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012b1G3UuJcgMtZGH8HFyNfN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 16556,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 109,
          "cache_read_input_tokens": 16556,
          "cache_creation_input_tokens": 2482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2482,
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

_source line 7 · 2026-05-24T05:50:47.193Z_

<details><summary>↩ Tool result · `toolu_01BoHadVcNHzfzHJdBjEBU2n`</summary>

```text
drwxr-xr-x 16 ubuntu ubuntu  4096 May 24 05:42 .
drwxrwxr-x  7 ubuntu ubuntu  4096 May 20 07:07 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 07:07 .claude
drwxr-xr-x  7 ubuntu ubuntu  4096 May 24 04:48 .git
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 23:37 .pytest_cache
drwxr-xr-x  6 ubuntu ubuntu  4096 May 22 15:25 .venv
-rw-r--r--  1 ubuntu ubuntu 15206 May 24 05:48 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 07:10 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  3300 May 24 05:42 ROADMAP.md
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 08:07 __pycache__
-rw-r--r--  1 ubuntu ubuntu    91 May 24 04:03 _last_visual_review.json
-rw-r--r--  1 ubuntu ubuntu 26659 May 22 03:48 _paper_audit_result.json
drwxr-xr-x  5 ubuntu ubuntu  4096 May 20 23:52 annot_sensitivity
drwxr-xr-x 44 ubuntu ubuntu 12288 May 24 04:29 artifacts
drwxr-xr-x  2 ubuntu ubuntu 12288 May 21 01:40 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 20 07:25 decisions.lock
-rw-------  1 ubuntu ubuntu 18128 May 24 05:42 decisions.yaml
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 09:54 distill_tmp
drwxr-xr-x  4 ubuntu ubuntu  4096 May 23 16:13 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 07:29 dream_registry.lock
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38243439-e3b9-442a-b8ac-c73651b4e083",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "ace04f09-19f8-4403-9fd1-eb727ecc4d55",
  "sourceToolAssistantUUID": "38243439-e3b9-442a-b8ac-c73651b4e083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T05:50:49.197Z_

Now let me examine the key files mentioned:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ace04f09-19f8-4403-9fd1-eb727ecc4d55",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUaKMmzVyXXXGri6Ew",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17be6eee-b371-4714-ad29-afd8310af95d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SAZoLVuVFbi4kn1z9Wf5yt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 19038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 712,
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

_source line 9 · 2026-05-24T05:50:49.716Z_

<details open><summary>🔧 Tool call — Read · `toolu_012baoJDkHq7aBYafLvVbkPH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_updated_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17be6eee-b371-4714-ad29-afd8310af95d",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUaKMmzVyXXXGri6Ew",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "87424b91-3559-4840-8849-140226e657a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SAZoLVuVFbi4kn1z9Wf5yt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 19038,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 101,
          "cache_read_input_tokens": 19038,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 712,
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

_source line 10 · 2026-05-24T05:50:49.728Z_

<details><summary>↩ Tool result · `toolu_012baoJDkHq7aBYafLvVbkPH`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Compute bias for all available confusion matrices (plan006 + plan011 frontier).
4	Merges HumAID K=10 (from plan006), VAST K=3 and CivilComments K=2 (from plan011
5	frontier extractions + existing 7B data) and computes 7-topology biases.
6	
7	Fixes applied (Reviewer CRITICAL):
8	  1. Label consistency validation: all CMs for same (dataset, K) must share label order
9	  2. Exclude vast_deepseek_zero-shot (1000 samples, near-degenerate neutral recall)
10	  3. Exposure sign flip checks ALL K-1 coefficients (not just coefs[1])
11	  4. Per-coefficient sign flip details recorded for exposure topology
12	
13	Output: artifacts/updated_empirical_results.json
14	"""
15	
16	import json
17	import sys
18	import numpy as np
19	from pathlib import Path
20	from collections import defaultdict
21	
22	PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
23	sys.path.insert(0, str(PROJ))
24	
25	import importlib.util
26	spec = importlib.util.spec_from_file_location(
27	    "plan_006",
28	    str(PROJ / "plan_006_asv_empirical.py")
29	)
30	plan_006 = importlib.util.module_from_spec(spec)
31	spec.loader.exec_module(plan_006)
32	
33	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
34	              'mbias', 'iv', 'frontdoor']
35	
36	MIN_SAMPLES = 500
37	
38	EXCLUDE_CONFIGS = {
39	    "vast/deepseek_zero-shot",
40	}
41	
42	
43	def validate_label_consistency(frontier_data):
44	    """Assert all CMs for same (dataset, K) have identical label ordering."""
45	    by_group = defaultdict(list)
46	    for raw_key, entry in frontier_data.items():
47	        labels = entry.get("labels", [])
48	        K = np.array(entry["confusion_matrix_normalized"]).shape[0]
49	        dataset = raw_key.split("/")[0] if "/" in raw_key else "unknown"
50	        by_group[(dataset, K)].append((raw_key, labels))
51	
52	    for (dataset, K), items in by_group.items():
53	        ref_labels = items[0][1]
54	        for raw_key, labels in items[1:]:
55	            if labels != ref_labels:
56	                raise ValueError(
57	                    f"Label mismatch in ({dataset}, K={K}): "
58	                    f"{items[0][0]} has {ref_labels}, {raw_key} has {labels}"
59	                )
60	        if ref_labels:
61	            print(f"  Label check OK: ({dataset}, K={K}) → {ref_labels} ({len(items)} CMs)")
62	
63	
64	def load_all_cms():
65	    """Load confusion matrices from plan006 (HumAID) + plan011 frontier extractions."""
66	    all_cms = {}
67	    meta = {}
68	
69	    # 1. HumAID K=10 from plan006 (authoritative, full matrices)
70	    with open(PROJ / "artifacts/plan006/asv_empirical_results.json") as f:
71	        plan006 = json.load(f)
72	    for key, cm in plan006["confusion_matrices"].items():
73	        C = np.array(cm)
74	        if np.min(np.diag(C)) > 0:
75	            all_cms[key] = C
76	            parts = key.split("_", 1)
77	            model_prompt = parts[1] if len(parts) > 1 else key
78	            meta[key] = {"dataset": "humaid", "model_prompt": model_prompt, "K": 10,
79	                         "source": "plan006"}
80	
81	    # 2. Plan011 frontier extractions (VAST + CivilComments + any new)
82	    with open(PROJ / "artifacts/plan011_frontier_cms.json") as f:
83	        frontier = json.load(f)
84	
85	    validate_label_consistency(frontier)
86	
87	    for raw_key, entry in frontier.items():
88	        if raw_key in EXCLUDE_CONFIGS:
89	            print(f"  EXCLUDE {raw_key}: in exclusion list (degenerate)")
90	            continue
91	
92	        C = np.array(entry["confusion_matrix_normalized"])
93	        n_valid = entry.get("n_valid", entry.get("n_samples", 0))
94	        labels = entry.get("labels", [])
95	        K = C.shape[0]
96	
97	        if n_valid < MIN_SAMPLES:
98	            print(f"  SKIP {raw_key}: n_valid={n_valid} < {MIN_SAMPLES}")
99	            continue
100	
101	        norm_key = raw_key.replace("/", "_")
102	
103	        col_sums = C.sum(axis=0)
104	        if not np.allclose(col_sums, 1.0, atol=0.05):
105	            row_sums = C.sum(axis=1)
106	            if np.allclose(row_sums, 1.0, atol=0.05):
107	                C = C.T
108	            else:
109	                print(f"  WARN {raw_key}: neither row nor col stochastic, normalizing columns")
110	                C = C / C.sum(axis=0, keepdims=True)
111	
112	        if norm_key in all_cms:
113	            print(f"  SKIP {norm_key}: already in plan006")
114	            continue
115	
116	        if raw_key.startswith("civil_comments/"):
117	            dataset = "civil_comments"
118	            model_prompt = raw_key[len("civil_comments/"):]
119	        elif raw_key.startswith("vast/"):
120	            dataset = "vast"
121	            model_prompt = raw_key[len("vast/"):]
122	        elif raw_key.startswith("humaid/"):
123	            dataset = "humaid"
124	            model_prompt = raw_key[len("humaid/"):]
125	        else:
126	            dataset = "unknown"
127	            model_prompt = raw_key
128	
129	        all_cms[norm_key] = C
130	        meta[norm_key] = {
131	            "dataset": dataset, "model_prompt": model_prompt, "K": K,
132	            "source": "plan011_frontier", "n_valid": n_valid,
133	            "labels": labels,
134	            "accuracy": entry.get("accuracy", None),
135	        }
136	
137	    return all_cms, meta
138	
139	
140	def check_exposure_sign_flips(plim_true, plim_biased, K):
141	    """Check ALL K-1 exposure coefficients for sign reversal.
142	
143	    Returns (any_flip: bool, details: list of per-coefficient results).
144	    Coefficients are at indices 1..K-1 (index 0 is the intercept).
145	    """
146	    details = []
147	    any_flip = False
148	    for i in range(1, K):
149	        true_val = float(plim_true[i])
150	        biased_val = float(plim_biased[i])
151	        if not (np.isfinite(true_val) and np.isfinite(biased_val)):
152	            details.append({"coef_idx": i, "true": true_val, "biased": biased_val,
153	                            "sign_flip": False, "note": "non-finite"})
154	            continue
155	        sf = bool(np.sign(biased_val) != np.sign(true_val)) if abs(true_val) > 1e-10 else False
156	        if sf:
157	            any_flip = True
158	        details.append({
159	            "coef_idx": i,
160	            "true": round(true_val, 6),
161	            "biased": round(biased_val, 6),
162	            "sign_flip": sf,
163	        })
164	    return any_flip, details
165	
166	
167	def compute_biases(all_cms, config_meta):
168	    """Compute plim bias for all (config, topology) pairs.
169	
170	    For exposure topology: checks ALL K-1 coefficients for sign flips.
171	    For IV: scalar Wald estimator (sign flip on tau).
172	    For others: tau = plim_result[1] (treatment coefficient).
173	    """
174	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
175	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
176	    suff_stats = {}
177	    tau_true_cache = {}
178	    plim_true_cache = {}
179	
180	    for K in Ks_used:
181	        for topo in TOPOLOGIES:
182	            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
183	            suff_stats[(K, topo)] = st
184	            plim_I = plan_006.compute_plim(np.eye(K), st, K)
185	            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
186	            plim_true_cache[(K, topo)] = plim_I
187	
188	    bias_records = []
189	    sign_flips = 0
190	    exposure_coef_sign_flips = 0
191	    total = 0
192	
193	    for config_key, C in sorted(all_cms.items()):
194	        m = config_meta[config_key]
195	        K = m["K"]
196	        dataset = m["dataset"]
197	        model_prompt = m["model_prompt"]
198	
199	        parts = model_prompt.rsplit("_", 1)
200	        if len(parts) == 2 and parts[1] in ["zero-shot", "few-shot-3", "few-shot-5"]:
201	            model, prompt = parts
202	        else:
203	            for p in ["zero-shot", "few-shot-3", "few-shot-5"]:
204	                if model_prompt.endswith(p):
205	                    model = model_prompt[:-(len(p)+1)]
206	                    prompt = p
207	                    break
208	            else:
209	                model = model_prompt
210	                prompt = "unknown"
211	
212	        for topo in TOPOLOGIES:
213	            tau_true = tau_true_cache[(K, topo)]
214	            st = suff_stats[(K, topo)]
215	
216	            try:
217	                plim_C = plan_006.compute_plim(C, st, K)
218	            except Exception:
219	                continue
220	
221	            if topo == 'exposure':
222	                plim_I = plim_true_cache[(K, topo)]
223	                if isinstance(plim_C, np.ndarray) and isinstance(plim_I, np.ndarray):
224	                    any_flip, coef_details = check_exposure_sign_flips(plim_I, plim_C, K)
225	                    tau_biased = plan_006.extract_tau(plim_C, topo)
226	                    if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
227	                        continue
228	                    bias = tau_biased - tau_true
229	                    bias_pct = abs(bias / tau_true) if abs(tau_true) > 1e-10 else float('inf')
230	                    if any_flip:
231	                        sign_flips += 1
232	                        exposure_coef_sign_flips += sum(1 for d in coef_details if d["sign_flip"])
233	                    total += 1
234	                    bias_records.append({
235	                        "dataset": dataset, "model": model, "prompt": prompt,
236	                        "K": K, "topology": topo,
237	                        "tau_true": float(tau_true), "tau_hat": float(tau_biased),
238	                        "bias": float(bias), "bias_pct": float(bias_pct),
239	                        "sign_flip": any_flip,
240	                        "exposure_coef_details": coef_details,
241	                        "source": m.get("source", "unknown"),
242	                    })
243	                    continue
244	
245	            tau_biased = plan_006.extract_tau(plim_C, topo)
246	            if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
247	                continue
248	
249	            bias = tau_biased - tau_true
250	            bias_pct = abs(bias / tau_true) if abs(tau_true) > 1e-10 else float('inf')
251	            sf = bool(np.sign(tau_biased) != np.sign(tau_true)) if abs(tau_true) > 1e-10 else False
252	
253	            if sf:
254	                sign_flips += 1
255	            total += 1
256	
257	            bias_records.append({
258	                "dataset": dataset, "model": model, "prompt": prompt,
259	                "K": K, "topology": topo,
260	                "tau_true": float(tau_true), "tau_hat": float(tau_biased),
261	                "bias": float(bias), "bias_pct": float(bias_pct),
262	                "sign_flip": sf,
263	                "source": m.get("source", "unknown"),
264	            })
265	
266	    return bias_records, sign_flips, total, exposure_coef_sign_flips
267	
268	
269	def main():
270	    print("Loading confusion matrices...")
271	    all_cms, config_meta = load_all_cms()
272	    print(f"\nTotal configs: {len(all_cms)}")
273	    for k, m in sorted(config_meta.items()):
274	        C = all_cms[k]
275	        print(f"  {k}: K={m['K']}, diag_mean={np.diag(C).mean():.3f}, src={m.get('source', '?')}")
276	
277	    print(f"\nComputing biases across {len(TOPOLOGIES)} topologies...")
278	    bias_records, sign_flips, total, exposure_coef_sf = compute_biases(all_cms, config_meta)
279	
280	    datasets = set(r["dataset"] for r in bias_records)
281	    models = set(r["model"] for r in bias_records)
282	    n_configs = len(all_cms)
283	
284	    by_dataset = defaultdict(list)
285	    by_topology = defaultdict(list)
286	    for r in bias_records:
287	        by_dataset[r["dataset"]].append(r)
288	        by_topology[r["topology"]].append(r)
289	
290	    print(f"\n{'='*70}")
291	    print(f"RESULTS SUMMARY")
292	    print(f"{'='*70}")
293	    print(f"Total configs: {n_configs}")
294	    print(f"Total scenarios: {total}")
295	    print(f"Sign flips (any coef): {sign_flips}")
296	    print(f"Exposure coefficient-level sign flips: {exposure_coef_sf}")
297	    print(f"Datasets: {sorted(datasets)}")
298	    print(f"Models: {sorted(models)}")
299	
300	    # Exposure coefficient details
301	    print(f"\nExposure coefficient-level details:")
302	    for r in bias_records:
303	        if r["topology"] == "exposure" and "exposure_coef_details" in r:
304	            details = r["exposure_coef_details"]
305	            flipped = [d for d in details if d["sign_flip"]]
306	            if flipped:
307	                print(f"  ⚠️ {r['dataset']}/{r['model']}_{r['prompt']}: "
308	                      f"{len(flipped)}/{len(details)} coefs flipped: {flipped}")
309	            else:
310	                vals = [(d["coef_idx"], d["true"], d["biased"]) for d in details]
311	                print(f"  ✓ {r['dataset']}/{r['model']}_{r['prompt']}: no flip {vals}")
312	
313	    print(f"\nPer-dataset:")
314	    for ds in sorted(datasets):
315	        recs = by_dataset[ds]
316	        n_cfg = len(set(f"{r['model']}_{r['prompt']}" for r in recs))
317	        mean_bias = np.mean([r['bias_pct'] for r in recs])
318	        sf = sum(r['sign_flip'] for r in recs)
319	        print(f"  {ds}: {n_cfg} configs, {len(recs)} scenarios, mean_abs_bias={mean_bias:.3f}, sign_flips={sf}")
320	
321	    print(f"\nPer-topology:")
322	    for topo in TOPOLOGIES:
323	        recs = by_topology[topo]
324	        mean_bias = np.mean([r['bias_pct'] for r in recs])
325	        max_bias = max([r['bias_pct'] for r in recs])
326	        sf = sum(r['sign_flip'] for r in recs)
327	        print(f"  {topo}: mean_bias_pct={mean_bias:.3f}, max={max_bias:.3f}, sign_flips={sf}")
328	
329	    # Model tier comparison
330	    print(f"\nFrontier vs 7B comparison:")
331	    frontier_biases = [r['bias_pct'] for r in bias_records if 'qwen2.5-7b' not in r['model']]
332	    sevb_biases = [r['bias_pct'] for r in bias_records if 'qwen2.5-7b' in r['model']]
333	    if frontier_biases and sevb_biases:
334	        print(f"  Frontier mean abs bias: {np.mean(frontier_biases):.3f}")
335	        print(f"  7B mean abs bias: {np.mean(sevb_biases):.3f}")
336	        print(f"  Ratio 7B/frontier: {np.mean(sevb_biases)/np.mean(frontier_biases):.2f}")
337	
338	    output = {
339	        "confusion_matrices": {k: all_cms[k].tolist() for k in sorted(all_cms.keys())},
340	        "config_meta": {k: v for k, v in config_meta.items()},
341	        "biases": bias_records,
342	        "summary": {
343	            "total_configs": n_configs,
344	            "total_scenarios": total,
345	            "sign_flips": sign_flips,
346	            "exposure_coef_level_sign_flips": exposure_coef_sf,
347	            "datasets": sorted(datasets),
348	            "models": sorted(models),
349	            "excluded_configs": list(EXCLUDE_CONFIGS),
350	            "per_dataset": {
351	                ds: {
352	                    "n_configs": len(set(f"{r['model']}_{r['prompt']}" for r in recs)),
353	                    "n_scenarios": len(recs),
354	                    "mean_abs_bias_pct": float(np.mean([r['bias_pct'] for r in recs])),
355	                    "sign_flips": sum(r['sign_flip'] for r in recs),
356	                }
357	                for ds, recs in by_dataset.items()
358	            },
359	            "per_topology": {
360	                topo: {
361	                    "mean_abs_bias_pct": float(np.mean([r['bias_pct'] for r in recs])),
362	                    "max_abs_bias_pct": float(max(r['bias_pct'] for r in recs)),
363	                    "sign_flips": sum(r['sign_flip'] for r in recs),
364	                }
365	                for topo, recs in by_topology.items()
366	            },
367	        }
368	    }
369	
370	    out_path = PROJ / "artifacts/updated_empirical_results.json"
371	    with open(out_path, "w") as f:
372	        json.dump(output, f, indent=2)
373	    print(f"\nSaved: {out_path}")
374	
375	
376	if __name__ == "__main__":
377	    main()
378	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87424b91-3559-4840-8849-140226e657a5",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "27e2d2e8-d295-487e-9e85-dc5edccb899e",
  "sourceToolAssistantUUID": "87424b91-3559-4840-8849-140226e657a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T05:50:51.168Z_

Now let me look at the annot_sensitivity package to understand the bias computation functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27e2d2e8-d295-487e-9e85-dc5edccb899e",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUm9ybcrCzqg1acCZL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f73dad5a-c9cc-48e1-bf01-afb32093860a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fz57XYaVTwm8mKEdfC8Kaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5781,
      "cache_read_input_tokens": 19750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5781,
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

_source line 12 · 2026-05-24T05:50:51.934Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jv4T5DbMctr4SzBT4BM5NE`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity -type f -name \"*.py\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f73dad5a-c9cc-48e1-bf01-afb32093860a",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUm9ybcrCzqg1acCZL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d005ebe6-a2e7-410f-a2e1-20c332a5d8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fz57XYaVTwm8mKEdfC8Kaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5781,
      "cache_read_input_tokens": 19750,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 113,
          "cache_read_input_tokens": 19750,
          "cache_creation_input_tokens": 5781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5781,
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

_source line 13 · 2026-05-24T05:50:51.978Z_

<details><summary>↩ Tool result · `toolu_01Jv4T5DbMctr4SzBT4BM5NE`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/examples/confounding_k3.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/__init__.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d005ebe6-a2e7-410f-a2e1-20c332a5d8ac",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "cad3f14f-6995-44a1-bf2d-fd41e6b31a3d",
  "sourceToolAssistantUUID": "d005ebe6-a2e7-410f-a2e1-20c332a5d8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-24T05:50:53.200Z_

Let me examine the core files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad3f14f-6995-44a1-bf2d-fd41e6b31a3d",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUvjvunDHzkjiK1KT4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b474dc3a-47fe-4337-bcaf-f7df62991059",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MjMbq6mSVp88jzMws4DLzg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 25531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 517,
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

_source line 15 · 2026-05-24T05:50:53.787Z_

<details open><summary>🔧 Tool call — Read · `toolu_0117XDZBzroXS82zLBth6Jbu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b474dc3a-47fe-4337-bcaf-f7df62991059",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUvjvunDHzkjiK1KT4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2bdefd2-a898-4377-b49a-f9259cc5b42b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MjMbq6mSVp88jzMws4DLzg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 25531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 517,
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

_source line 16 · 2026-05-24T05:50:53.793Z_

<details><summary>↩ Tool result · `toolu_0117XDZBzroXS82zLBth6Jbu`</summary>

```text
1	"""Annotation Sensitivity Value (ASV) computation.
2	
3	ASV measures how much misclassification is needed to cross a bias threshold,
4	using the C(delta) = (1-delta)*I + delta*C0 interpolation path.
5	"""
6	
7	import numpy as np
8	from .bias import _precompute, _get_tau
9	from .confusion import validate_confusion_matrix, interpolate_confusion, delta_range
10	from .dgp import DEFAULT_PARAMS, TOPOLOGIES
11	
12	
13	def _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):
14	    dmin, dmax = delta_range(C0)
15	    deltas = np.linspace(dmin, dmax, n_grid)
16	    tau_curve = np.zeros(n_grid)
17	    for i, d in enumerate(deltas):
18	        C_d = interpolate_confusion(C0, d)
19	        tau_curve[i] = _get_tau(topology, C_d, stats, K)
20	    bias_abs = np.abs(tau_curve - tau_true)
21	    return deltas, bias_abs, tau_curve
22	
23	
24	def _compute_envelope(bias_abs):
25	    env = np.zeros_like(bias_abs)
26	    running_max = 0.0
27	    for i in range(len(bias_abs)):
28	        v = bias_abs[i]
29	        if not np.isnan(v):
30	            running_max = max(running_max, v)
31	        env[i] = running_max
32	    return env
33	
34	
35	def _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,
36	                             threshold_type, threshold_value):
37	    if threshold_type == "magnitude":
38	        if abs(tau_true) < 1e-12:
39	            return None
40	        thresh = threshold_value * abs(tau_true)
41	        for i in range(len(deltas)):
42	            if envelope[i] > thresh:
43	                return float(deltas[i])
44	        return None
45	    elif threshold_type == "sign_flip":
46	        if abs(tau_true) < 1e-12:
47	            return None
48	        baseline_sign = np.sign(tau_true)
49	        for i in range(len(deltas)):
50	            if np.isnan(tau_curve[i]):
51	                continue
52	            if np.sign(tau_curve[i]) != baseline_sign:
53	                return float(deltas[i])
54	        return None
55	    elif threshold_type == "significance":
56	        z_crit = 1.96
57	        for i in range(len(deltas)):
58	            if np.isnan(tau_curve[i]):
59	                continue
60	            if abs(tau_curve[i]) < z_crit * threshold_value:
61	                return float(deltas[i])
62	        return None
63	    else:
64	        raise ValueError(
65	            f"Unknown threshold_type: {threshold_type}. "
66	            f"Choose from 'magnitude', 'significance', 'sign_flip'"
67	        )
68	
69	
70	def compute_asv(topology, C0, params=None, threshold_type="magnitude",
71	                threshold_value=0.1, n_grid=1500):
72	    """Compute Annotation Sensitivity Value for a topology and base confusion matrix.
73	
74	    ASV is the minimum interpolation delta at which a bias threshold is crossed
75	    along the path C(delta) = (1-delta)*I + delta*C0.
76	
77	    Args:
78	        topology: one of 7 DAG types
79	        C0: (K, K) base confusion matrix
80	        params: optional DGP parameters dict
81	        threshold_type: "magnitude" (relative to tau_true),
82	                        "significance" (threshold_value = SE),
83	                        "sign_flip" (sign of tau changes)
84	        threshold_value: threshold parameter (meaning depends on threshold_type)
85	        n_grid: number of delta grid points
86	
87	    Returns:
88	        dict with asv, bias_curve, envelope, deltas, tau_true
89	    """
90	    if topology not in TOPOLOGIES:
91	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
92	    if not validate_confusion_matrix(C0):
93	        raise ValueError("C0 must be a valid column-stochastic matrix")
94	
95	    K = C0.shape[0]
96	    merged = dict(DEFAULT_PARAMS[topology])
97	    if params is not None:
98	        merged.update(params)
99	
100	    stats = _precompute(topology, merged, K)
101	    tau_true = _get_tau(topology, np.eye(K), stats, K)
102	
103	    deltas, bias_abs, tau_curve = _compute_bias_curve(
104	        topology, C0, stats, K, tau_true, n_grid
105	    )
106	    envelope = _compute_envelope(bias_abs)
107	
108	    asv = _find_threshold_crossing(
109	        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value
110	    )
111	
112	    return {
113	        "asv": asv,
114	        "bias_curve": bias_abs,
115	        "envelope": envelope,
116	        "deltas": deltas,
117	        "tau_true": float(tau_true),
118	    }
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2bdefd2-a898-4377-b49a-f9259cc5b42b",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "c9682550-0f3b-400d-bf05-f4aa66944812",
  "sourceToolAssistantUUID": "d2bdefd2-a898-4377-b49a-f9259cc5b42b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T05:50:53.941Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T6dySovpoQAAc93SkW2eAK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9682550-0f3b-400d-bf05-f4aa66944812",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUvjvunDHzkjiK1KT4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "56ec2ac6-070d-4fbb-ad78-fe1c225a813d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MjMbq6mSVp88jzMws4DLzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 25531,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 517
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 242,
          "cache_read_input_tokens": 25531,
          "cache_creation_input_tokens": 517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 517,
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

_source line 18 · 2026-05-24T05:50:53.946Z_

<details><summary>↩ Tool result · `toolu_01T6dySovpoQAAc93SkW2eAK`</summary>

```text
1	"""Compute annotation-error bias via probability limit calculations.
2	
3	Uses precomputed sufficient statistics from large-sample DGP simulations
4	to compute OLS plim as a function of confusion matrix C, avoiding MC.
5	"""
6	
7	import warnings
8	import numpy as np
9	from .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
10	from .confusion import validate_confusion_matrix
11	
12	_N_PRECOMP = 2_000_000
13	_precomp_cache = {}
14	
15	
16	def _params_key(params):
17	    items = []
18	    for k, v in sorted(params.items()):
19	        if isinstance(v, np.ndarray):
20	            items.append((k, tuple(v.flat)))
21	        else:
22	            items.append((k, v))
23	    return tuple(items)
24	
25	
26	def _precompute(topology, params, K, seed=999):
27	    """Precompute sufficient statistics for plim calculation."""
28	    cache_key = (topology, _params_key(params), K)
29	    if cache_key in _precomp_cache:
30	        return _precomp_cache[cache_key]
31	
32	    rng = np.random.default_rng(seed)
33	    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)
34	    Y = data["Y"]
35	    A = data["A"]
36	
37	    DA = np.zeros((_N_PRECOMP, K))
38	    for k in range(K):
39	        DA[:, k] = (A == k).astype(float)
40	
41	    stats = {
42	        "E_Y": Y.mean(),
43	        "E_DA": DA.mean(0),
44	        "E_DA_Y": (DA * Y[:, None]).mean(0),
45	    }
46	
47	    if topology in HAS_TREATMENT:
48	        T = data["T"]
49	        stats.update({
50	            "E_T": T.mean(),
51	            "E_T2": (T ** 2).mean(),
52	            "E_TY": (T * Y).mean(),
53	            "E_DA_T": (DA * T[:, None]).mean(0),
54	        })
55	
56	    if topology == "iv":
57	        Z = data["Z"]
58	        Zc = Z - Z.mean()
59	        var_Z = (Zc ** 2).mean()
60	        stats["RF"] = (Zc * (Y - Y.mean())).mean() / var_Z
61	        FS = np.zeros(K)
62	        for k in range(K):
63	            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z
64	        stats["FS"] = FS
65	
66	    _precomp_cache[cache_key] = stats
67	    return stats
68	
69	
70	def _plim_with_T(C, stats, K):
71	    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
72	    ds = C @ stats["E_DA"]
73	    dst = C @ stats["E_DA_T"]
74	    dsy = C @ stats["E_DA_Y"]
75	    ET, ET2 = stats["E_T"], stats["E_T2"]
76	    EY, ETY = stats["E_Y"], stats["E_TY"]
77	
78	    dim = 1 + K  # intercept + T + (K-1) dummies
79	    EZZ = np.zeros((dim, dim))
80	    EZZ[0, 0] = 1.0
81	    EZZ[0, 1] = EZZ[1, 0] = ET
82	    EZZ[1, 1] = ET2
83	    for j in range(1, K):
84	        idx = j + 1
85	        EZZ[0, idx] = EZZ[idx, 0] = ds[j]
86	        EZZ[1, idx] = EZZ[idx, 1] = dst[j]
87	        EZZ[idx, idx] = ds[j]
88	
89	    EZY = np.zeros(dim)
90	    EZY[0] = EY
91	    EZY[1] = ETY
92	    for j in range(1, K):
93	        EZY[j + 1] = dsy[j]
94	
95	    cond = np.linalg.cond(EZZ)
96	    if cond > 1e12:
97	        warnings.warn(
98	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
99	        )
100	
101	    return np.linalg.solve(EZZ, EZY)
102	
103	
104	def _plim_no_T(C, stats, K):
105	    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""
106	    ds = C @ stats["E_DA"]
107	    dsy = C @ stats["E_DA_Y"]
108	    EY = stats["E_Y"]
109	
110	    dim = K  # intercept + (K-1) dummies
111	    EZZ = np.zeros((dim, dim))
112	    EZZ[0, 0] = 1.0
113	    for j in range(1, K):
114	        EZZ[0, j] = EZZ[j, 0] = ds[j]
115	        EZZ[j, j] = ds[j]
116	
117	    EZY = np.zeros(dim)
118	    EZY[0] = EY
119	    for j in range(1, K):
120	        EZY[j] = dsy[j]
121	
122	    cond = np.linalg.cond(EZZ)
123	    if cond > 1e12:
124	        warnings.warn(
125	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
126	        )
127	
128	    return np.linalg.solve(EZZ, EZY)
129	
130	
131	def _plim_iv(C, stats, K):
132	    """Wald estimator plim: RF / (C @ FS)[1]."""
133	    FS_star = C @ stats["FS"]
134	    denom = FS_star[1]
135	    if abs(denom) < 1e-15:
136	        return np.nan
137	    return stats["RF"] / denom
138	
139	
140	def _get_tau(topology, C, stats, K):
141	    """Extract target coefficient from plim vector.
142	
143	    For IV: Wald estimator RF / (C @ FS)[1].
144	    For topologies with T: OLS coefficient index 1 (treatment effect).
145	    For topologies without T: OLS coefficient index 1 (first dummy).
146	    """
147	    if topology == "iv":
148	        return _plim_iv(C, stats, K)
149	    if topology in HAS_TREATMENT:
150	        coefs = _plim_with_T(C, stats, K)
151	    else:
152	        coefs = _plim_no_T(C, stats, K)
153	    return coefs[1]
154	
155	
156	def compute_bias(topology, C, params=None):
157	    """Compute annotation-error bias for a given topology and confusion matrix.
158	
159	    Args:
160	        topology: one of "confounding", "mediation", "collider", "exposure",
161	                  "mbias", "iv", "frontdoor"
162	        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
163	        params: optional DGP parameters dict, None uses defaults
164	
165	    Returns:
166	        dict with tau_true, tau_biased, bias, bias_pct, topology
167	    """
168	    if topology not in TOPOLOGIES:
169	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
170	    if not validate_confusion_matrix(C):
171	        raise ValueError("C must be a square, non-negative, column-stochastic matrix")
172	
173	    K = C.shape[0]
174	    merged = dict(DEFAULT_PARAMS[topology])
175	    if params is not None:
176	        merged.update(params)
177	
178	    stats = _precompute(topology, merged, K)
179	    tau_true = _get_tau(topology, np.eye(K), stats, K)
180	    tau_biased = _get_tau(topology, C, stats, K)
181	    bias = tau_biased - tau_true
182	    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float("nan")
183	
184	    return {
185	        "tau_true": float(tau_true),
186	        "tau_biased": float(tau_biased),
187	        "bias": float(bias),
188	        "bias_pct": float(bias_pct),
189	        "topology": topology,
190	    }
191	
192	
193	def clear_cache():
194	    """Clear the precomputed statistics cache."""
195	    _precomp_cache.clear()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56ec2ac6-070d-4fbb-ad78-fe1c225a813d",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "f2a22f33-c2c4-40bb-a6b3-60ba528cb5d5",
  "sourceToolAssistantUUID": "56ec2ac6-070d-4fbb-ad78-fe1c225a813d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T05:50:54.006Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MukmNhC9yLck1vkSkTbyqU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a22f33-c2c4-40bb-a6b3-60ba528cb5d5",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsUvjvunDHzkjiK1KT4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ee026166-84cf-4c7f-a65a-c37b19a36bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MjMbq6mSVp88jzMws4DLzg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 25531,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 517
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 242,
          "cache_read_input_tokens": 25531,
          "cache_creation_input_tokens": 517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 517,
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

_source line 20 · 2026-05-24T05:50:54.014Z_

<details><summary>↩ Tool result · `toolu_01MukmNhC9yLck1vkSkTbyqU`</summary>

```text
1	"""Confusion matrix utilities: validation, generation, interpolation.
2	
3	Convention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).
4	"""
5	
6	import numpy as np
7	
8	
9	def validate_confusion_matrix(C):
10	    """Check if C is a valid column-stochastic confusion matrix.
11	
12	    Args:
13	        C: array to validate
14	
15	    Returns:
16	        True if valid, False otherwise
17	    """
18	    if not isinstance(C, np.ndarray):
19	        return False
20	    if C.ndim != 2 or C.shape[0] != C.shape[1]:
21	        return False
22	    if C.shape[0] < 2:
23	        return False
24	    if (C < -1e-10).any():
25	        return False
26	    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):
27	        return False
28	    return True
29	
30	
31	def random_confusion_matrix(K, diag_dominance=0.8, rng=None):
32	    """Generate a random column-stochastic confusion matrix.
33	
34	    Args:
35	        K: number of categories
36	        diag_dominance: controls diagonal strength (0 to 1)
37	        rng: numpy random Generator (created if None)
38	
39	    Returns:
40	        (K, K) column-stochastic matrix
41	    """
42	    if rng is None:
43	        rng = np.random.default_rng()
44	    diag_alpha = diag_dominance * 10
45	    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)
46	    C = np.zeros((K, K))
47	    for k in range(K):
48	        alphas = np.full(K, offdiag_alpha)
49	        alphas[k] = diag_alpha
50	        C[:, k] = rng.dirichlet(alphas)
51	    return C
52	
53	
54	def interpolate_confusion(C0, delta):
55	    """Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.
56	
57	    Args:
58	        C0: (K, K) base confusion matrix
59	        delta: interpolation parameter (0 = identity, 1 = C0)
60	
61	    Returns:
62	        (K, K) interpolated column-stochastic matrix
63	    """
64	    K = C0.shape[0]
65	    C = (1 - delta) * np.eye(K) + delta * C0
66	    C = np.maximum(C, 0.0)
67	    col_sums = C.sum(axis=0)
68	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
69	    return C / col_sums
70	
71	
72	def delta_range(C0):
73	    """Compute valid delta range for interpolation.
74	
75	    Args:
76	        C0: (K, K) base confusion matrix
77	
78	    Returns:
79	        (delta_min, delta_max) tuple
80	    """
81	    min_diag = np.diag(C0).min()
82	    if min_diag >= 1.0:
83	        return (0.0, 10.0)
84	    delta_max = min(1.0 / (1.0 - min_diag), 10.0)
85	    return (0.0, delta_max)
86	
87	
88	def predefined_matrices(K=3):
89	    """Return a dict of predefined K x K confusion matrices.
90	
91	    Args:
92	        K: number of categories (only K=3 supported)
93	
94	    Returns:
95	        dict mapping name to (K, K) confusion matrix
96	    """
97	    if K != 3:
98	        raise ValueError(f"Predefined matrices only available for K=3, got K={K}")
99	    return {
100	        "symmetric_high": np.array([
101	            [0.80, 0.10, 0.10],
102	            [0.10, 0.80, 0.10],
103	            [0.10, 0.10, 0.80]]),
104	        "mild_uniform": np.array([
105	            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],
106	            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],
107	            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),
108	        "moderate_uniform": np.array([
109	            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],
110	            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],
111	            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),
112	        "severe_uniform": np.array([
113	            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],
114	            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],
115	            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),
116	        "asymmetric": np.array([
117	            [0.75, 0.05, 0.05],
118	            [0.20, 0.80, 0.10],
119	            [0.05, 0.15, 0.85]]),
120	        "near_permutation": np.array([
121	            [0.05, 0.05, 0.90],
122	            [0.90, 0.05, 0.05],
123	            [0.05, 0.90, 0.05]]),
124	        "realistic_llm": np.array([
125	            [0.78, 0.15, 0.03],
126	            [0.18, 0.72, 0.18],
127	            [0.04, 0.13, 0.79]]),
128	    }
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee026166-84cf-4c7f-a65a-c37b19a36bc4",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "1217cb98-62b9-4660-a010-4de57255144c",
  "sourceToolAssistantUUID": "ee026166-84cf-4c7f-a65a-c37b19a36bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-24T05:50:55.385Z_

Now let me examine the DGP file to understand the 7 topologies and their parameters:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1217cb98-62b9-4660-a010-4de57255144c",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsV5UnsxXmC9LQ4QEKJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "255b4b7a-19b2-45e0-8ce1-9e4f028f244c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ALQBi3pLWcmE8EcY8obbXB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 26048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6213,
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

_source line 22 · 2026-05-24T05:50:56.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GzZrx9QWRPgGpsaMZYwCKX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "255b4b7a-19b2-45e0-8ce1-9e4f028f244c",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsV5UnsxXmC9LQ4QEKJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1fdb2cd3-2cec-49b0-b760-31e0a500756a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ALQBi3pLWcmE8EcY8obbXB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6213,
      "cache_read_input_tokens": 26048,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 112,
          "cache_read_input_tokens": 26048,
          "cache_creation_input_tokens": 6213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6213,
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

_source line 23 · 2026-05-24T05:50:56.195Z_

<details><summary>↩ Tool result · `toolu_01GzZrx9QWRPgGpsaMZYwCKX`</summary>

```text
1	"""Data generation processes for 7 DAG topologies.
2	
3	Each topology generates synthetic data with a known causal structure.
4	The variable A (or M for frontdoor) is the one subject to misclassification.
5	"""
6	
7	import numpy as np
8	from .utils import softmax_sample, make_dummies
9	
10	DEFAULT_PARAMS = {
11	    "confounding": dict(
12	        p_A=np.array([0.40, 0.35, 0.25]),
13	        alpha=np.array([1.5, -1.0]),
14	        beta_A=np.array([1.0, -0.5]),
15	        beta_T=2.0, sigma_T=1.0),
16	    "mediation": dict(
17	        tau=0.5,
18	        gamma=np.array([0.0, 0.5, -0.3]),
19	        delta=np.array([0.0, 0.8, -0.6]),
20	        beta=np.array([0.0, 1.0, -0.5])),
21	    "collider": dict(
22	        tau=1.0,
23	        g=np.array([0.0, 0.0, 0.0]),
24	        dT=np.array([0.0, 0.5, -0.3]),
25	        dY=np.array([0.0, 0.8, 0.6])),
26	    "exposure": dict(
27	        beta=np.array([0.0, 1.0, -0.5]),
28	        p_A=np.array([0.40, 0.35, 0.25])),
29	    "mbias": dict(
30	        tau=1.0, delta_coef=1.0, lam=1.0,
31	        g=np.array([0.0, 0.0, 0.0]),
32	        a1=np.array([0.0, 0.8, -0.5]),
33	        a2=np.array([0.0, 0.6, 0.9])),
34	    "iv": dict(
35	        lam=1.0,
36	        g=np.array([0.0, 0.0, 0.0]),
37	        dZ=np.array([0.0, 1.0, -0.5]),
38	        dU=np.array([0.0, 0.8, 0.6]),
39	        beta=np.array([0.0, 1.0, -0.5])),
40	    "frontdoor": dict(
41	        alpha_U=1.0, lam_U=1.0,
42	        gamma=np.array([0.0, 0.5, -0.3]),
43	        delta=np.array([0.0, 1.0, -0.8]),
44	        beta=np.array([0.0, 1.0, -0.5])),
45	}
46	
47	TOPOLOGIES = list(DEFAULT_PARAMS.keys())
48	
49	HAS_TREATMENT = {"confounding", "mediation", "collider", "mbias", "frontdoor"}
50	NO_TREATMENT = {"exposure", "iv"}
51	
52	
53	def _get_rng(rng, seed):
54	    if rng is not None:
55	        return rng
56	    return np.random.default_rng(seed)
57	
58	
59	def _get_params(topology, params):
60	    p = dict(DEFAULT_PARAMS[topology])
61	    if params is not None:
62	        p.update(params)
63	    return p
64	
65	
66	def gen_confounding(N, params=None, rng=None, seed=None):
67	    """A->T, A->Y, T->Y. Researcher controls for A*.
68	
69	    Returns:
70	        dict with keys T, Y, A
71	    """
72	    rng = _get_rng(rng, seed)
73	    p = _get_params("confounding", params)
74	    K = len(p["p_A"])
75	    A = rng.choice(K, size=N, p=p["p_A"])
76	    D = make_dummies(A, K)
77	    T = D @ p["alpha"] + rng.normal(0, p["sigma_T"], N)
78	    Y = p["beta_T"] * T + D @ p["beta_A"] + rng.normal(0, 1, N)
79	    return {"T": T, "Y": Y, "A": A}
80	
81	
82	def gen_mediation(N, params=None, rng=None, seed=None):
83	    """T->A->Y. A mediates; researcher controls for A*.
84	
85	    Returns:
86	        dict with keys T, Y, A
87	    """
88	    rng = _get_rng(rng, seed)
89	    p = _get_params("mediation", params)
90	    T = rng.binomial(1, 0.5, N).astype(float)
91	    K = len(p["gamma"])
92	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
93	    A = softmax_sample(logits, rng)
94	    D = make_dummies(A, K)
95	    Y = p["beta"][0] + D @ p["beta"][1:] + p["tau"] * T + rng.normal(0, 1, N)
96	    return {"T": T, "Y": Y, "A": A}
97	
98	
99	def gen_collider(N, params=None, rng=None, seed=None):
100	    """T->A<-Y. Researcher wrongly controls for A*.
101	
102	    Returns:
103	        dict with keys T, Y, A
104	    """
105	    rng = _get_rng(rng, seed)
106	    p = _get_params("collider", params)
107	    T = rng.normal(0, 1, N)
108	    Y = p["tau"] * T + rng.normal(0, 1, N)
109	    logits = (p["g"][None, :] + p["dT"][None, :] * T[:, None]
110	              + p["dY"][None, :] * Y[:, None])
111	    A = softmax_sample(logits, rng)
112	    return {"T": T, "Y": Y, "A": A}
113	
114	
115	def gen_exposure(N, params=None, rng=None, seed=None):
116	    """A->Y (direct exposure, no treatment T).
117	
118	    Returns:
119	        dict with keys Y, A
120	    """
121	    rng = _get_rng(rng, seed)
122	    p = _get_params("exposure", params)
123	    K = len(p["p_A"])
124	    A = rng.choice(K, size=N, p=p["p_A"])
125	    D = make_dummies(A, K)
126	    Y = p["beta"][0] + D @ p["beta"][1:] + rng.normal(0, 1, N)
127	    return {"Y": Y, "A": A}
128	
129	
130	def gen_mbias(N, params=None, rng=None, seed=None):
131	    """U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.
132	
133	    Returns:
134	        dict with keys T, Y, A
135	    """
136	    rng = _get_rng(rng, seed)
137	    p = _get_params("mbias", params)
138	    N_out = N
139	    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)
140	    T = p["delta_coef"] * U1 + rng.normal(0, 1, N_out)
141	    logits = (p["g"][None, :] + p["a1"][None, :] * U1[:, None]
142	              + p["a2"][None, :] * U2[:, None])
143	    A = softmax_sample(logits, rng)
144	    Y = p["tau"] * T + p["lam"] * U2 + rng.normal(0, 1, N_out)
145	    return {"T": T, "Y": Y, "A": A}
146	
147	
148	def gen_iv(N, params=None, rng=None, seed=None):
149	    """Z->A->Y, U->{A,Y}. IV topology with endogenous A.
150	
151	    Returns:
152	        dict with keys Z, Y, A
153	    """
154	    rng = _get_rng(rng, seed)
155	    p = _get_params("iv", params)
156	    K = len(p["g"])
157	    Z = rng.normal(0, 1, N)
158	    U = rng.normal(0, 1, N)
159	    logits = (p["g"][None, :] + p["dZ"][None, :] * Z[:, None]
160	              + p["dU"][None, :] * U[:, None])
161	    A = softmax_sample(logits, rng)
162	    D = make_dummies(A, K)
163	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam"] * U + rng.normal(0, 1, N)
164	    return {"Z": Z, "Y": Y, "A": A}
165	
166	
167	def gen_frontdoor(N, params=None, rng=None, seed=None):
168	    """T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).
169	
170	    Returns:
171	        dict with keys T, Y, A (A is the mediator M)
172	    """
173	    rng = _get_rng(rng, seed)
174	    p = _get_params("frontdoor", params)
175	    U = rng.normal(0, 1, N)
176	    T = p["alpha_U"] * U + rng.normal(0, 1, N)
177	    K = len(p["gamma"])
178	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
179	    A = softmax_sample(logits, rng)
180	    D = make_dummies(A, K)
181	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam_U"] * U + rng.normal(0, 1, N)
182	    return {"T": T, "Y": Y, "A": A}
183	
184	
185	GEN_FUNCS = {
186	    "confounding": gen_confounding,
187	    "mediation": gen_mediation,
188	    "collider": gen_collider,
189	    "exposure": gen_exposure,
190	    "mbias": gen_mbias,
191	    "iv": gen_iv,
192	    "frontdoor": gen_frontdoor,
193	}
194	
195	
196	def generate_data(topology, N, params=None, rng=None, seed=None):
197	    """Generate synthetic data for a given topology.
198	
199	    Args:
200	        topology: one of "confounding", "mediation", "collider", "exposure",
201	                  "mbias", "iv", "frontdoor"
202	        N: sample size
203	        params: optional DGP parameter overrides
204	        rng: numpy random Generator
205	        seed: random seed (used if rng is None)
206	
207	    Returns:
208	        dict with generated variables (topology-dependent keys)
209	    """
210	    if topology not in GEN_FUNCS:
211	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
212	    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fdb2cd3-2cec-49b0-b760-31e0a500756a",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "4795dfe0-2ff7-4998-84b6-0fa8a51bd016",
  "sourceToolAssistantUUID": "1fdb2cd3-2cec-49b0-b760-31e0a500756a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-24T05:50:57.928Z_

Now let me check the plan_006_asv_empirical.py file to see how it's used:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4795dfe0-2ff7-4998-84b6-0fa8a51bd016",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVFJ9Vc8eQknKnzByg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "371b8478-4cd7-4d5c-a4fd-da5c746c6a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VtcqzaKYwYJxNNKmCvTGcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 32261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3371,
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

_source line 25 · 2026-05-24T05:50:58.478Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W75qjrDJ5KuXCRdHLR5VPj`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -name \"plan_006*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "371b8478-4cd7-4d5c-a4fd-da5c746c6a68",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVFJ9Vc8eQknKnzByg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5786ca50-a389-46cf-9201-6ba7521c4e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VtcqzaKYwYJxNNKmCvTGcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3371,
      "cache_read_input_tokens": 32261,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 116,
          "cache_read_input_tokens": 32261,
          "cache_creation_input_tokens": 3371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3371,
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

_source line 26 · 2026-05-24T05:50:58.546Z_

<details><summary>↩ Tool result · `toolu_01W75qjrDJ5KuXCRdHLR5VPj`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/__pycache__/plan_006_asv_empirical.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5786ca50-a389-46cf-9201-6ba7521c4e34",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "42555338-f836-4cd7-914e-7d789b0af448",
  "sourceToolAssistantUUID": "5786ca50-a389-46cf-9201-6ba7521c4e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T05:50:59.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R9e76Tzm9hgKcYRYt8jNyi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42555338-f836-4cd7-914e-7d789b0af448",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVQptCHEQwdd2YxePy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e8e806c-a585-4c2c-8ad2-78bc52472b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNnfQgAxarWAq7GAAoXuKv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 35632,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 109,
          "cache_read_input_tokens": 35632,
          "cache_creation_input_tokens": 219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 219,
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

_source line 28 · 2026-05-24T05:50:59.927Z_

<details><summary>↩ Tool result · `toolu_01R9e76Tzm9hgKcYRYt8jNyi`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices
4	
5	Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
6	= 27 C matrices) to compute:
7	  1. Downstream causal bias across 7 DAG topologies
8	  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
9	  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
10	  4. Type I/II error rates before/after ASV filtering
11	  5. Inter-model error correlation
12	
13	Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
14	        Each line: {"true_label": int, "predicted_label": int}
15	
16	Output: artifacts/plan006/asv_empirical_results.json
17	
18	Dependencies: numpy (required), matplotlib (optional for plots)
19	"""
20	
21	import numpy as np
22	import json
23	import argparse
24	import os
25	import time
26	from collections import OrderedDict
27	
28	try:
29	    import matplotlib
30	    matplotlib.use('Agg')
31	    import matplotlib.pyplot as plt
32	    HAS_MPL = True
33	except ImportError:
34	    HAS_MPL = False
35	
36	# ============================================================================
37	# Constants
38	# ============================================================================
39	
40	DATASETS = OrderedDict([
41	    ('civil_comments', {'K': 2}),
42	    ('vast', {'K': 3}),
43	    ('humaid', {'K': 10}),
44	])
45	
46	MODELS = ['llama4', 'qwen3', 'deepseek']
47	PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']
48	
49	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
50	              'mbias', 'iv', 'frontdoor']
51	
52	N_PRECOMP = 2_000_000
53	
54	# Parameter pools — K=3 values match plan_001/plan_005
55	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
56	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
57	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
58	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
59	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
60	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
61	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]
62	
63	
64	# ============================================================================
65	# Utility Functions
66	# ============================================================================
67	
68	def softmax_rows(logits):
69	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
70	    return e / e.sum(axis=1, keepdims=True)
71	
72	
73	def sample_cat(probs, rng):
74	    cum = np.cumsum(probs, axis=1)
75	    u = rng.uniform(size=probs.shape[0])[:, None]
76	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
77	
78	
79	def generate_Astar(A, C, rng):
80	    probs = C[:, A]
81	    cum = np.cumsum(probs, axis=0)
82	    u = rng.uniform(size=len(A))
83	    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)
84	
85	
86	def ols_with_dummies(Y, T, Astar, K):
87	    N = len(Y)
88	    D = np.zeros((N, K - 1))
89	    for k in range(1, K):
90	        D[:, k - 1] = (Astar == k).astype(float)
91	    X = np.column_stack([np.ones(N), T, D])
92	    try:
93	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
94	        resid = Y - X @ beta
95	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
96	        XtX_inv = np.linalg.inv(X.T @ X)
97	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
98	    except np.linalg.LinAlgError:
99	        beta = np.full(X.shape[1], np.nan)
100	        se = np.full(X.shape[1], np.nan)
101	    return beta, se
102	
103	
104	def ols_no_T(Y, Astar, K):
105	    N = len(Y)
106	    D = np.zeros((N, K - 1))
107	    for k in range(1, K):
108	        D[:, k - 1] = (Astar == k).astype(float)
109	    X = np.column_stack([np.ones(N), D])
110	    try:
111	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
112	        resid = Y - X @ beta
113	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
114	        XtX_inv = np.linalg.inv(X.T @ X)
115	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
116	    except np.linalg.LinAlgError:
117	        beta = np.full(X.shape[1], np.nan)
118	        se = np.full(X.shape[1], np.nan)
119	    return beta, se
120	
121	
122	def wald_estimator(Z, Y, Astar, k=1):
123	    z1 = Z == 1; z0 = Z == 0
124	    n1, n0 = float(z1.sum()), float(z0.sum())
125	    if n1 < 2 or n0 < 2:
126	        return np.nan, np.nan
127	    RF = Y[z1].mean() - Y[z0].mean()
128	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
129	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
130	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
131	    FS = Dk_z1 - Dk_z0
132	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
133	    if abs(FS) < 1e-8:
134	        return np.nan, np.nan
135	    W = RF / FS
136	    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4
137	    return W, np.sqrt(max(var_W, 0))
138	
139	
140	# ============================================================================
141	# DGP Parameters (general K, K=3 matches plan_001/plan_005)
142	# ============================================================================
143	
144	def make_p_A(K):
145	    if K == 2:
146	        return np.array([0.55, 0.45])
147	    elif K == 3:
148	        return np.array([0.40, 0.35, 0.25])
149	    else:
150	        raw = np.array([1.0 / (i + 1) for i in range(K)])
151	        return raw / raw.sum()
152	
153	
154	def make_dgp_params(K):
155	    p_A = make_p_A(K)
156	    params = {
157	        'confounding': {
158	            'p_A': p_A,
159	            'alpha': np.array(_ALPHA_POOL[:K - 1]),
160	            'beta_A': np.array(_BETA_A_POOL[:K - 1]),
161	            'beta_T': 2.0,
162	            'sigma_T': 1.0,
163	        },
164	        'mediation': {
165	            'tau': 0.5,
166	            'gamma': np.array(_GAMMA_POOL[:K]),
167	            'delta': np.array(_DELTA_POOL[:K]),
168	            'beta': np.array(_BETA_POOL[:K]),
169	        },
170	        'collider': {
171	            'tau': 1.0,
172	            'g': np.zeros(K),
173	            'dT': np.array(_DT_POOL[:K]),
174	            'dY': np.array(_DY_POOL[:K]),
175	        },
176	        'exposure': {
177	            'beta': np.array(_BETA_POOL[:K]),
178	            'p_A': p_A,
179	        },
180	    }
181	    if K == 3:
182	        params['mbias'] = {
183	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
184	            'g': np.zeros(3),
185	            'a_U1': np.array([0.0, 0.8, -0.5]),
186	            'a_U2': np.array([0.0, 0.6, 0.9]),
187	        }
188	        params['iv'] = {
189	            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
190	            'g': np.zeros(3),
191	            'dZ': np.array([0.0, 1.0, -0.5]),
192	            'dU': np.array([0.0, 0.8, 0.6]),
193	        }
194	        params['frontdoor'] = {
195	            'alpha_U': 1.0, 'lambda_U': 1.0,
196	            'gamma': np.array([0.0, 0.5, -0.3]),
197	            'delta_fd': np.array([0.0, 1.0, -0.8]),
198	            'beta': np.array([0.0, 1.0, -0.5]),
199	        }
200	    else:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e8e806c-a585-4c2c-8ad2-78bc52472b17",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "ee41d450-61b9-4432-b6a5-2afeb0a08683",
  "sourceToolAssistantUUID": "8e8e806c-a585-4c2c-8ad2-78bc52472b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-24T05:51:01.084Z_

Let me continue reading plan_006:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee41d450-61b9-4432-b6a5-2afeb0a08683",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVWka6iUssahzXDsky",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7adeade-b407-48a6-82b3-5d2b02c7b101",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Efrq1T4dKQGXAAKHP9JnhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 3290,
      "cache_read_input_tokens": 35851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3290,
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

_source line 30 · 2026-05-24T05:51:02.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ShL8ViXXdb6ug6kTQxCbqK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 400,
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7adeade-b407-48a6-82b3-5d2b02c7b101",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVWka6iUssahzXDsky",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c76fd02f-3f4e-4e8f-9cb8-f480229abd4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Efrq1T4dKQGXAAKHP9JnhV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 3290,
      "cache_read_input_tokens": 35851,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3290
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 135,
          "cache_read_input_tokens": 35851,
          "cache_creation_input_tokens": 3290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3290,
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

_source line 31 · 2026-05-24T05:51:02.083Z_

<details><summary>↩ Tool result · `toolu_01ShL8ViXXdb6ug6kTQxCbqK`</summary>

```text
200	    else:
201	        params['mbias'] = {
202	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
203	            'g': np.zeros(K),
204	            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),
205	            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),
206	        }
207	        iv_beta = np.array(_BETA_POOL[:K]) * 0.5
208	        iv_beta[0] = 0.0
209	        params['iv'] = {
210	            'lam': 1.0, 'beta': iv_beta,
211	            'g': np.zeros(K),
212	            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
213	            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
214	        }
215	        fd_delta = np.array(_DELTA_POOL[:K])
216	        fd_delta[0] = 0.0
217	        params['frontdoor'] = {
218	            'alpha_U': 1.0, 'lambda_U': 1.0,
219	            'gamma': np.array(_GAMMA_POOL[:K]),
220	            'delta_fd': fd_delta,
221	            'beta': np.array(_BETA_POOL[:K]),
222	        }
223	    return params
224	
225	
226	def make_dgp_params_H0(K, params):
227	    p0 = {}
228	    for topo, p in params.items():
229	        if topo == 'confounding':
230	            p0[topo] = dict(p, beta_T=0.0)
231	        elif topo == 'mediation':
232	            p0[topo] = dict(p, tau=0.0)
233	        elif topo == 'collider':
234	            p0[topo] = dict(p, tau=0.0)
235	        elif topo == 'exposure':
236	            p0[topo] = dict(p, beta=np.zeros(K))
237	        elif topo == 'mbias':
238	            p0[topo] = dict(p, tau=0.0)
239	        elif topo == 'iv':
240	            p0[topo] = dict(p, beta=np.zeros(K))
241	        elif topo == 'frontdoor':
242	            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,
243	                            delta_fd=np.zeros(K), beta=np.zeros(K))
244	    return p0
245	
246	
247	# ============================================================================
248	# DGP Generators (general K)
249	# ============================================================================
250	
251	def gen_confounding(K, N, p, rng):
252	    A = rng.choice(K, size=N, p=p['p_A'])
253	    D = np.zeros((N, K - 1))
254	    for j in range(K - 1):
255	        D[:, j] = (A == j + 1).astype(float)
256	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
257	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
258	    return T, Y, A
259	
260	
261	def gen_mediation(K, N, p, rng):
262	    T = rng.binomial(1, 0.5, N).astype(float)
263	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
264	    probs = softmax_rows(logits)
265	    A = sample_cat(probs, rng)
266	    D = np.zeros((N, K - 1))
267	    for j in range(K - 1):
268	        D[:, j] = (A == j + 1).astype(float)
269	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
270	    return T, Y, A
271	
272	
273	def gen_collider(K, N, p, rng):
274	    T = rng.normal(0, 1, N)
275	    Y = p['tau'] * T + rng.normal(0, 1, N)
276	    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
277	              + p['dY'][None, :] * Y[:, None])
278	    probs = softmax_rows(logits)
279	    A = sample_cat(probs, rng)
280	    return T, Y, A
281	
282	
283	def gen_exposure(K, N, p, rng):
284	    A = rng.choice(K, size=N, p=p['p_A'])
285	    D = np.zeros((N, K - 1))
286	    for j in range(K - 1):
287	        D[:, j] = (A == j + 1).astype(float)
288	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
289	    return None, Y, A
290	
291	
292	def gen_mbias(K, N, p, rng):
293	    U1 = rng.normal(0, 1, N)
294	    U2 = rng.normal(0, 1, N)
295	    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
296	    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
297	    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]
298	              + p['a_U2'][None, :] * U2[:, None])
299	    probs = softmax_rows(logits)
300	    A = sample_cat(probs, rng)
301	    return T, Y, A
302	
303	
304	def gen_iv(K, N, p, rng):
305	    Z = rng.binomial(1, 0.5, N).astype(float)
306	    U = rng.normal(0, 1, N)
307	    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]
308	              + p['dU'][None, :] * U[:, None])
309	    probs = softmax_rows(logits)
310	    A = sample_cat(probs, rng)
311	    D = np.zeros((N, K - 1))
312	    for j in range(K - 1):
313	        D[:, j] = (A == j + 1).astype(float)
314	    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)
315	    return Z, Y, A
316	
317	
318	def gen_frontdoor(K, N, p, rng):
319	    U = rng.normal(0, 1, N)
320	    T = p['alpha_U'] * U + rng.normal(0, 1, N)
321	    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]
322	    probs = softmax_rows(logits)
323	    M = sample_cat(probs, rng)
324	    D = np.zeros((N, K - 1))
325	    for j in range(K - 1):
326	        D[:, j] = (M == j + 1).astype(float)
327	    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)
328	    return T, Y, M
329	
330	
331	GEN_FNS = {
332	    'confounding': gen_confounding, 'mediation': gen_mediation,
333	    'collider': gen_collider, 'exposure': gen_exposure,
334	    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,
335	}
336	
337	
338	# ============================================================================
339	# Sufficient Statistics & Plim (general K)
340	# ============================================================================
341	
342	def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
343	    rng = np.random.default_rng(seed)
344	    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
345	    DA = np.zeros((N, K))
346	    for k in range(K):
347	        DA[:, k] = (A == k).astype(float)
348	
349	    if topology == 'iv':
350	        Z = first_var
351	        z1 = Z == 1; z0 = Z == 0
352	        RF = Y[z1].mean() - Y[z0].mean()
353	        FS = np.zeros(K)
354	        for k in range(K):
355	            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
356	        return dict(RF=RF, FS=FS, topology='iv')
357	    elif topology == 'exposure':
358	        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
359	                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
360	    else:
361	        T = first_var
362	        return dict(
363	            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),
364	            E_Y=Y.mean(), E_TY=(T * Y).mean(),
365	            E_TD=(DA * T[:, None]).mean(0),
366	            E_YD=(DA * Y[:, None]).mean(0), topology=topology)
367	
368	
369	def compute_plim(C, st, K):
370	    if st['topology'] == 'iv':
371	        FS_star = C @ st['FS']
372	        if abs(FS_star[1]) < 1e-8:
373	            return np.nan
374	        return st['RF'] / FS_star[1]
375	    elif st['topology'] == 'exposure':
376	        q = C @ st['p_A']
377	        cy = C @ st['E_YD']
378	        EZZ = np.zeros((K, K))
379	        EZZ[0, 0] = 1.0
380	        for j in range(1, K):
381	            EZZ[0, j] = EZZ[j, 0] = q[j]
382	            EZZ[j, j] = q[j]
383	        EZY = np.zeros(K)
384	        EZY[0] = st['E_Y']
385	        for j in range(1, K):
386	            EZY[j] = cy[j]
387	        try:
388	            return np.linalg.solve(EZZ, EZY)
389	        except np.linalg.LinAlgError:
390	            return np.full(K, np.nan)
391	    else:
392	        q = C @ st['p_A']
393	        ct = C @ st['E_TD']
394	        cy = C @ st['E_YD']
395	        dim = K + 1
396	        EZZ = np.zeros((dim, dim))
397	        EZZ[0, 0] = 1.0
398	        EZZ[0, 1] = EZZ[1, 0] = st['E_T']
399	        EZZ[1, 1] = st['E_T2']
400	        for j in range(1, K):
401	            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]
402	            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]
403	            EZZ[j + 1, j + 1] = q[j]
404	        EZY = np.zeros(dim)
405	        EZY[0] = st['E_Y']
406	        EZY[1] = st['E_TY']
407	        for j in range(1, K):
408	            EZY[j + 1] = cy[j]
409	        try:
410	            return np.linalg.solve(EZZ, EZY)
411	        except np.linalg.LinAlgError:
412	            return np.full(dim, np.nan)
413	
414	
415	def extract_tau(plim_result, topology):
416	    if topology == 'iv':
417	        return float(plim_result) if np.isfinite(plim_result) else np.nan
418	    if isinstance(plim_result, np.ndarray):
419	        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
420	    return np.nan
421	
422	
423	# ============================================================================
424	# 1. Data Loading & Confusion Matrix
425	# ============================================================================
426	
427	def load_confusion_matrix_npz(data_dir, dataset, model, prompt, K):
428	    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_confusion_matrix.npz")
429	    d = np.load(path, allow_pickle=True)
430	    C = d['C']
431	    assert C.shape == (K, K), f"Expected ({K},{K}), got {C.shape}"
432	    return C
433	
434	
435	def load_annotations(data_dir, dataset, model, prompt):
436	    for suffix in ['_annotations.jsonl', '.jsonl']:
437	        path = os.path.join(data_dir, dataset, f"{model}_{prompt}{suffix}")
438	        if os.path.exists(path):
439	            break
440	    else:
441	        raise FileNotFoundError(f"No annotation file for {dataset}/{model}_{prompt}")
442	    records = []
443	    label_set = set()
444	    with open(path) as f:
445	        for line in f:
446	            rec = json.loads(line.strip())
447	            gl = rec.get('true_label', rec.get('gold_label'))
448	            pl = rec.get('predicted_label', rec.get('pred_label'))
449	            if gl is not None and pl is not None:
450	                label_set.add(gl)
451	                label_set.add(pl)
452	                records.append((gl, pl))
453	    if records and isinstance(records[0][0], str):
454	        sorted_labels = sorted(label_set)
455	        label_map = {l: i for i, l in enumerate(sorted_labels)}
456	        records = [(label_map[g], label_map[p]) for g, p in records]
457	    else:
458	        records = [(int(g), int(p)) for g, p in records]
459	    return records
460	
461	
462	def build_confusion_matrix(records, K):
463	    counts = np.zeros((K, K))
464	    for true_k, pred_k in records:
465	        if 0 <= true_k < K and 0 <= pred_k < K:
466	            counts[pred_k, true_k] += 1
467	    col_sums = counts.sum(axis=0)
468	    col_sums = np.where(col_sums < 1, 1, col_sums)
469	    return counts / col_sums
470	
471	
472	def load_all_confusion_matrices(data_dir, dataset_filter=None):
473	    matrices = {}
474	    for dataset, info in DATASETS.items():
475	        if dataset_filter and dataset not in dataset_filter:
476	            continue
477	        K = info['K']
478	        for model in MODELS:
479	            for prompt in PROMPTS:
480	                try:
481	                    C = load_confusion_matrix_npz(data_dir, dataset, model, prompt, K)
482	                    matrices[(dataset, model, prompt)] = C
483	                except (FileNotFoundError, Exception):
484	                    try:
485	                        records = load_annotations(data_dir, dataset, model, prompt)
486	                        C = build_confusion_matrix(records, K)
487	                        matrices[(dataset, model, prompt)] = C
488	                    except FileNotFoundError:
489	                        print(f"  [WARN] Missing: {dataset}/{model}_{prompt}")
490	    return matrices
491	
492	
493	# ============================================================================
494	# 2. Downstream Causal Bias
495	# ============================================================================
496	
497	def compute_bias_for_topology(C, K, topology, st, tau_true):
498	    plim_result = compute_plim(C, st, K)
499	    tau_hat = extract_tau(plim_result, topology)
500	    if np.isnan(tau_hat) or np.isnan(tau_true):
501	        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}
502	    bias = tau_hat - tau_true
503	    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None
504	    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)
505	    return {
506	        'tau_hat': float(tau_hat), 'bias': float(bias),
507	        'bias_pct': float(bias_pct) if bias_pct is not None else None,
508	        'sign_flip': sign_flip,
509	    }
510	
511	
512	def compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):
513	    results = []
514	    for (dataset, model, prompt), C in confusion_matrices.items():
515	        K = DATASETS[dataset]['K']
516	        for topology in TOPOLOGIES:
517	            st = all_suff_stats[(K, topology)]
518	            tau_true = all_tau_true[(K, topology)]
519	            info = compute_bias_for_topology(C, K, topology, st, tau_true)
520	            results.append({
521	                'dataset': dataset, 'model': model, 'prompt': prompt,
522	                'K': K, 'topology': topology, **info,
523	            })
524	    return results
525	
526	
527	# ============================================================================
528	# 3. ASV Computation
529	# ============================================================================
530	
531	def C_interpolated(C0, delta, K):
532	    C_d = (1 - delta) * np.eye(K) + delta * C0
533	    C_d = np.maximum(C_d, 0.0)
534	    col_sums = C_d.sum(axis=0)
535	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
536	    return C_d / col_sums
537	
538	
539	def compute_delta_max(C0):
540	    min_diag = np.diag(C0).min()
541	    if min_diag >= 1.0:
542	        return 10.0
543	    return min(1.0 / (1.0 - min_diag), 10.0)
544	
545	
546	def compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,
547	                           n_grid=1500, se_ref=None):
548	    dmax = compute_delta_max(C0)
549	    deltas = np.linspace(0, dmax, n_grid)
550	    tau_curve = np.zeros(n_grid)
551	    for i, d in enumerate(deltas):
552	        C_d = C_interpolated(C0, d, K)
553	        plim_result = compute_plim(C_d, st, K)
554	        tau_curve[i] = extract_tau(plim_result, topology)
555	
556	    bias_abs = np.abs(tau_curve - tau_true)
557	    envelope = np.zeros(n_grid)
558	    running_max = 0.0
559	    for i in range(n_grid):
560	        if np.isfinite(bias_abs[i]):
561	            running_max = max(running_max, bias_abs[i])
562	        envelope[i] = running_max
563	
564	    if asv_type == 'sign_flip':
565	        if abs(tau_true) < 1e-12:
566	            return None
567	        baseline_sign = np.sign(tau_true)
568	        for i in range(n_grid):
569	            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:
570	                return float(deltas[i])
571	        return None
572	    elif asv_type == 'magnitude':
573	        if abs(tau_true) < 1e-12:
574	            return None
575	        thresh = 0.1 * abs(tau_true)
576	        for i in range(n_grid):
577	            if envelope[i] > thresh:
578	                return float(deltas[i])
579	        return None
580	    elif asv_type == 'significance':
581	        if se_ref is None or se_ref < 1e-12:
582	            return None
583	        for i in range(n_grid):
584	            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:
585	                return float(deltas[i])
586	        return None
587	    return None
588	
589	
590	def estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):
591	    gen_fn = GEN_FNS[topology]
592	    rng = np.random.default_rng(seed)
593	    tau_hats = []
594	    for _ in range(n_mc):
595	        first_var, Y, A = gen_fn(K, N_ref, params, rng)
596	        if topology == 'iv':
597	            th, _ = wald_estimator(first_var, Y, A, k=1)
598	        elif topology == 'exposure':
599	            b, _ = ols_no_T(Y, A, K)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c76fd02f-3f4e-4e8f-9cb8-f480229abd4a",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "7e2306ca-730c-4e78-9888-193a17afd854",
  "sourceToolAssistantUUID": "c76fd02f-3f4e-4e8f-9cb8-f480229abd4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-24T05:51:03.553Z_

Now let me look at compute_all_tasks.py to see how it uses the bias computation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2306ca-730c-4e78-9888-193a17afd854",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVg4upq6TtV2A9S4JB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01f82d88-132a-4a4d-b7da-26e6b88cfd8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LkGbQ5J7fVfq9zG9Lxp3Zi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6384,
      "cache_read_input_tokens": 39141,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6384,
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

_source line 33 · 2026-05-24T05:51:04.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U2Hqdwo12869bPqzFRx2mK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01f82d88-132a-4a4d-b7da-26e6b88cfd8a",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVg4upq6TtV2A9S4JB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "acc03d0a-6c04-4662-8345-9a10fdb18f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LkGbQ5J7fVfq9zG9Lxp3Zi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6384,
      "cache_read_input_tokens": 39141,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6384,
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

_source line 34 · 2026-05-24T05:51:04.307Z_

<details><summary>↩ Tool result · `toolu_01U2Hqdwo12869bPqzFRx2mK`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Three computational tasks for the causal annotation error attribution paper.
4	
5	Task 1: Theory-Empirical MAPE (extend existing humaid-only to all 18 valid configs)
6	Task 2: PPI++ Empirical Validation (simulate gold labels, apply PPI++ correction)
7	Task 3: Dirichlet Subspace Overlay (regenerated with improved styling)
8	
9	Author: auto-generated for paper artifacts
10	"""
11	
12	import json
13	import sys
14	import time
15	import numpy as np
16	from pathlib import Path
17	from collections import defaultdict
18	
19	PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
20	sys.path.insert(0, str(PROJ))
21	
22	# Import the plan_006 module for DGP generators matching the paper's setup
23	import importlib.util
24	spec = importlib.util.spec_from_file_location(
25	    "plan_006",
26	    str(PROJ / "plan_006_asv_empirical.py")
27	)
28	plan_006 = importlib.util.module_from_spec(spec)
29	spec.loader.exec_module(plan_006)
30	
31	from annot_sensitivity.correction import correct_ppi, correct_naive_plugin, correct_mla
32	from annot_sensitivity.utils import misclassify
33	
34	# ============================================================================
35	# Common data loading
36	# ============================================================================
37	
38	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
39	              'mbias', 'iv', 'frontdoor']
40	HAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}
41	
42	
43	def load_all_data():
44	    """Load confusion matrices and bias records for all 18 valid configs."""
45	    # Load humaid confusion matrices (full 10x10)
46	    with open(PROJ / "artifacts/plan006/asv_empirical_results.json") as f:
47	        plan006 = json.load(f)
48	    humaid_cms = {k: np.array(v) for k, v in plan006["confusion_matrices"].items()}
49	    bias_records = plan006["biases"]
50	
51	    # Load filter info
52	    with open(PROJ / "artifacts/plan006_full_filtered_stats.json") as f:
53	        filter_data = json.load(f)
54	    zero_configs = set(filter_data["zero_configs"])
55	
56	    # Valid humaid configs (8 of 9, excluding qwen3_few-shot-5)
57	    humaid_valid = {k: humaid_cms[k] for k in humaid_cms if k not in zero_configs}
58	
59	    # Build bias lookup for humaid
60	    bias_lookup = {}
61	    for b in bias_records:
62	        ck = f"{b['dataset']}_{b['model']}_{b['prompt']}"
63	        if ck not in zero_configs and b.get('bias') is not None:
64	            bias_lookup[(ck, b['topology'])] = b
65	
66	    # VAST confusion matrices: we only have per-class recall (diagonal).
67	    # For VAST we need to construct approximate confusion matrices from the
68	    # diagonal data. The VAST per-class recall gives us C_kk for each class.
69	    # We distribute off-diagonal mass uniformly (best available approximation).
70	    vast_per_class_recall = filter_data["filtered_stats"]["vast_per_class_recall"]
71	    vast_cms = {}
72	    for key, diag in vast_per_class_recall.items():
73	        # key format: "vast_llama4_zero-shot"
74	        config_key = key  # already has "vast_" prefix
75	        K = 3
76	        C = np.zeros((K, K))
77	        for i in range(K):
78	            C[i, i] = diag[i]
79	            off_diag_mass = 1.0 - diag[i]
80	            for j in range(K):
81	                if j != i:
82	                    C[j, i] = off_diag_mass / (K - 1)
83	        vast_cms[config_key] = C
84	
85	    # CivilComments: we have trace/macro_recall from filtered_stats
86	    # For K=2, trace = C[0,0] + C[1,1], macro_recall = trace/2
87	    # We use the CC diagonal values from gen_fig7.py (extracted from the pipeline)
88	    civil_diag = {
89	        "civil_comments_qwen2.5-7b_zero-shot":  [0.7481536189069424, 0.684931506849315],
90	        "civil_comments_qwen2.5-7b_few-shot-3": [0.6787296898079763, 0.7808219178082192],
91	        "civil_comments_qwen2.5-7b_few-shot-5": [0.7370753323485968, 0.7602739726027398],
92	    }
93	    civil_cms = {}
94	    for key, diag in civil_diag.items():
95	        K = 2
96	        C = np.zeros((K, K))
97	        C[0, 0] = diag[0]
98	        C[1, 1] = diag[1]
99	        C[1, 0] = 1.0 - diag[0]
100	        C[0, 1] = 1.0 - diag[1]
101	        civil_cms[key] = C
102	
103	    # Merge all confusion matrices
104	    all_cms = {}
105	    all_cms.update(humaid_valid)
106	    all_cms.update(vast_cms)
107	    all_cms.update(civil_cms)
108	
109	    # Config metadata
110	    config_meta = {}
111	    for k, C in all_cms.items():
112	        parts = k.split("_", 1)
113	        dataset = parts[0]
114	        if dataset == "civil":
115	            dataset = "civil_comments"
116	            model_prompt = k[len("civil_comments_"):]
117	        elif dataset == "vast":
118	            model_prompt = k[len("vast_"):]
119	        else:
120	            model_prompt = k[len("humaid_"):]
121	        K = C.shape[0]
122	        config_meta[k] = {
123	            "dataset": dataset,
124	            "model_prompt": model_prompt,
125	            "K": K,
126	            "min_diag": float(np.min(np.diag(C))),
127	            "trace": float(np.trace(C)),
128	            "macro_recall": float(np.trace(C) / K),
129	        }
130	
131	    return all_cms, config_meta, bias_lookup, filter_data
132	
133	
134	# ============================================================================
135	# Task 1: Theory-Empirical MAPE
136	# ============================================================================
137	
138	def task1_mape(all_cms, config_meta, bias_lookup):
139	    """Compute MAPE between analytical plim bias and finite-sample MC bias."""
140	    print("=" * 80)
141	    print("TASK 1: Theory-Empirical MAPE")
142	    print("=" * 80)
143	    t0 = time.time()
144	
145	    N_MC = 200
146	    N_SAMPLES = 10_000
147	
148	    # Precompute sufficient stats and tau_true for each K
149	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
150	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acc03d0a-6c04-4662-8345-9a10fdb18f20",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "78824c94-ce6b-4f10-afea-20010d308535",
  "sourceToolAssistantUUID": "acc03d0a-6c04-4662-8345-9a10fdb18f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-24T05:51:05.797Z_

Let me check how the functions are actually called and what the final structure looks like:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78824c94-ce6b-4f10-afea-20010d308535",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVqvExdETBERnvPgmp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25710db0-b6fc-4655-a4a4-acae00ea4712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PMBbtYEKwWyXNeVY63va58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2285,
      "cache_read_input_tokens": 45525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2285,
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

_source line 36 · 2026-05-24T05:51:06.880Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NiZBsqKWCkNC1HQs6U4dtW`</summary>

```json
{
  "pattern": "^def (compute_plim|extract_tau|precompute_suff_stats|compute_bias)",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25710db0-b6fc-4655-a4a4-acae00ea4712",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsVqvExdETBERnvPgmp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05a622a5-ce6d-4c6a-a3b5-fa24ab2dae9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PMBbtYEKwWyXNeVY63va58",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2285,
      "cache_read_input_tokens": 45525,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 160,
          "cache_read_input_tokens": 45525,
          "cache_creation_input_tokens": 2285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2285,
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

_source line 37 · 2026-05-24T05:51:06.952Z_

<details><summary>↩ Tool result · `toolu_01NiZBsqKWCkNC1HQs6U4dtW`</summary>

```text
Found 11 files
artifacts/bootstrap_ci_convergence.py
artifacts/analyze_epsilon_sign_structure.py
artifacts/analyze_epsilon_bound.py
artifacts/exp_d_conjecture_verify_v2.py
artifacts/exp_d_conjecture_verify.py
artifacts/exp_c_bootstrap_asv.py
artifacts/compute_updated_empirical.py
annot_sensitivity/bias.py
plan_006_asv_empirical.py
artifacts/plan_005_asv_extended_fixed.py
plan_005_asv_extended.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05a622a5-ce6d-4c6a-a3b5-fa24ab2dae9a",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "64b691a7-82a2-4ec3-a61d-f413fd5df205",
  "sourceToolAssistantUUID": "05a622a5-ce6d-4c6a-a3b5-fa24ab2dae9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-24T05:51:08.185Z_

Let me check the key initialization file to see how functions are exported:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64b691a7-82a2-4ec3-a61d-f413fd5df205",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsW2n6rTawBwgD2Rfbe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da927692-882e-4824-9a5a-6162c2a642f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Rr6krYRK3K61JWTcftvzdr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 47810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 310,
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

_source line 39 · 2026-05-24T05:51:08.476Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DZ4ZVjqUF5ouEgZje1JBUL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da927692-882e-4824-9a5a-6162c2a642f0",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsW2n6rTawBwgD2Rfbe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe60944a-bf41-49db-a8e3-7e951400d0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Rr6krYRK3K61JWTcftvzdr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 47810,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 104,
          "cache_read_input_tokens": 47810,
          "cache_creation_input_tokens": 310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 310,
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

_source line 40 · 2026-05-24T05:51:08.481Z_

<details><summary>↩ Tool result · `toolu_01DZ4ZVjqUF5ouEgZje1JBUL`</summary>

```text
1	"""annot_sensitivity: Annotation-error sensitivity analysis for causal inference.
2	
3	Computes how LLM annotation misclassification propagates bias through
4	7 DAG topologies, with ASV sensitivity measures and 5 correction methods.
5	"""
6	
7	from .bias import compute_bias, clear_cache
8	from .asv import compute_asv
9	from .correction import (
10	    recommend_correction,
11	    correct_naive_plugin,
12	    correct_dsl,
13	    correct_ppi,
14	    correct_mcsimex,
15	    correct_mla,
16	    METHODS,
17	)
18	from .confusion import (
19	    validate_confusion_matrix,
20	    random_confusion_matrix,
21	    interpolate_confusion,
22	    predefined_matrices,
23	    delta_range,
24	)
25	from .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS
26	from .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify
27	
28	__all__ = [
29	    "compute_bias",
30	    "compute_asv",
31	    "recommend_correction",
32	    "correct_naive_plugin",
33	    "correct_dsl",
34	    "correct_ppi",
35	    "correct_mcsimex",
36	    "correct_mla",
37	    "validate_confusion_matrix",
38	    "random_confusion_matrix",
39	    "interpolate_confusion",
40	    "predefined_matrices",
41	    "delta_range",
42	    "generate_data",
43	    "clear_cache",
44	    "TOPOLOGIES",
45	    "DEFAULT_PARAMS",
46	    "METHODS",
47	    "GEN_FUNCS",
48	    "ols",
49	    "ols_with_se",
50	    "make_dummies",
51	    "softmax_sample",
52	    "misclassify",
53	]
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe60944a-bf41-49db-a8e3-7e951400d0b4",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "5a7c45e1-d40d-4819-b1e4-31bb2860732f",
  "sourceToolAssistantUUID": "fe60944a-bf41-49db-a8e3-7e951400d0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-24T05:51:10.128Z_

Now let me look at the correction module to understand the full pipeline better:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a7c45e1-d40d-4819-b1e4-31bb2860732f",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsW9f6Y2BC4FTcp71Sh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "578642c4-c806-44a5-ab53-8ebf2be8d70d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Esh5ibt9DRZFkRn9oyEFDF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 48120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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

_source line 42 · 2026-05-24T05:51:10.417Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YSoJT6m2SHcep8FxYrg7Ez`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "578642c4-c806-44a5-ab53-8ebf2be8d70d",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsW9f6Y2BC4FTcp71Sh",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af57435c-5956-48e9-a9ec-fa65ea5b69f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Esh5ibt9DRZFkRn9oyEFDF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 48120,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 122,
          "cache_read_input_tokens": 48120,
          "cache_creation_input_tokens": 660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 660,
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

_source line 43 · 2026-05-24T05:51:10.421Z_

<details><summary>↩ Tool result · `toolu_01YSoJT6m2SHcep8FxYrg7Ez`</summary>

```text
1	"""Correction methods and recommendation engine for annotation-error bias.
2	
3	Five correction methods:
4	  - naive_plugin: C^{-1} correction of dummy indicators
5	  - dsl: EM-based joint estimation of regression params and C
6	  - ppi: PPI++ combining gold-standard and full-sample estimates
7	  - mcsimex: MC-SIMEX extrapolation to lambda=-1
8	  - mla: Matrix-based label adjustment via D*_full @ C^{-1}
9	
10	Key finding (FWL theorem): naive_plugin and mla correct dummy coefficients
11	but NOT the treatment coefficient in regressions with a separate treatment T.
12	"""
13	
14	import numpy as np
15	from .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify
16	
17	METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]
18	
19	_EM_MAX_ITER = 100
20	_EM_TOL = 1e-6
21	_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]
22	_SIMEX_B = 50
23	
24	
25	def correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):
26	    """Correct using C^{-1} applied per-observation to dummy indicators.
27	
28	    Args:
29	        X_other: (N, p) non-A regressors (includes intercept)
30	        Y: (N,) outcome
31	        Astar: (N,) misclassified labels
32	        C: (K, K) confusion matrix
33	        tau_idx: index of target coefficient in full design
34	
35	    Returns:
36	        (tau_hat, se, success) tuple
37	    """
38	    cond = np.linalg.cond(C)
39	    if cond > 1e12:
40	        return np.nan, np.nan, False
41	    try:
42	        C_inv = np.linalg.inv(C)
43	    except np.linalg.LinAlgError:
44	        return np.nan, np.nan, False
45	    D_corrected = C_inv[:, Astar].T[:, 1:]
46	    X = np.column_stack([X_other, D_corrected])
47	    try:
48	        beta, se = ols_with_se(X, Y)
49	        return float(beta[tau_idx]), float(se[tau_idx]), True
50	    except Exception:
51	        return np.nan, np.nan, False
52	
53	
54	def correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):
55	    """EM-based joint estimation of regression params and C.
56	
57	    Args:
58	        X_other: (N, p) non-A regressors (includes intercept)
59	        Y: (N,) outcome
60	        Astar: (N,) misclassified labels
61	        A_gold: (N,) gold-standard labels (only gold_mask positions used)
62	        gold_mask: (N,) boolean mask for gold-standard observations
63	        tau_idx: index of target coefficient
64	
65	    Returns:
66	        (tau_hat, se, success) tuple
67	    """
68	    N = len(Y)
69	    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
70	    n_other = X_other.shape[1]
71	
72	    C_est = np.zeros((K, K))
73	    for j in range(K):
74	        for k in range(K):
75	            C_est[k, j] = (
76	                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)
77	            ).sum()
78	    col_sums = C_est.sum(axis=0)
79	    col_sums[col_sums == 0] = 1.0
80	    C_est /= col_sums
81	    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))
82	
83	    D_star = make_dummies(Astar, K)
84	    X_init = np.column_stack([X_other, D_star])
85	    try:
86	        beta = ols(X_init, Y)
87	    except Exception:
88	        return np.nan, np.nan, False
89	    sigma2 = 1.0
90	
91	    for _ in range(_EM_MAX_ITER):
92	        base = X_other @ beta[:n_other]
93	        resp = np.zeros((N, K))
94	        for j in range(K):
95	            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)
96	            resp[:, j] = (
97	                -0.5 * (Y - mu_j) ** 2 / sigma2
98	                + np.log(np.clip(C_est[Astar, j], 1e-15, None))
99	            )
100	        resp -= resp.max(axis=1, keepdims=True)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af57435c-5956-48e9-a9ec-fa65ea5b69f9",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "1ab21f70-cbf0-44c1-99bf-77bfcefdac4a",
  "sourceToolAssistantUUID": "af57435c-5956-48e9-a9ec-fa65ea5b69f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-24T05:51:11.739Z_

Now let me look at how plan_006 is structured to understand the full chain:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ab21f70-cbf0-44c1-99bf-77bfcefdac4a",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsWHbqD8pig9eN8MpGv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37bd01e4-80a4-416a-9cb2-09f6440b39a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BgBCjgBKrdBupfJtDZj57t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 48780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1566,
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

_source line 45 · 2026-05-24T05:51:12.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P8575Qe4sCFgtUvrnp1frv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 600,
  "offset": 415
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37bd01e4-80a4-416a-9cb2-09f6440b39a0",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsWHbqD8pig9eN8MpGv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93eae332-e8ea-42a0-ae62-9d19dc47a65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BgBCjgBKrdBupfJtDZj57t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 48780,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1566
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 48780,
          "cache_creation_input_tokens": 1566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1566,
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

_source line 46 · 2026-05-24T05:51:12.665Z_

<details><summary>↩ Tool result · `toolu_01P8575Qe4sCFgtUvrnp1frv`</summary>

```text
415	def extract_tau(plim_result, topology):
416	    if topology == 'iv':
417	        return float(plim_result) if np.isfinite(plim_result) else np.nan
418	    if isinstance(plim_result, np.ndarray):
419	        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
420	    return np.nan
421	
422	
423	# ============================================================================
424	# 1. Data Loading & Confusion Matrix
425	# ============================================================================
426	
427	def load_confusion_matrix_npz(data_dir, dataset, model, prompt, K):
428	    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_confusion_matrix.npz")
429	    d = np.load(path, allow_pickle=True)
430	    C = d['C']
431	    assert C.shape == (K, K), f"Expected ({K},{K}), got {C.shape}"
432	    return C
433	
434	
435	def load_annotations(data_dir, dataset, model, prompt):
436	    for suffix in ['_annotations.jsonl', '.jsonl']:
437	        path = os.path.join(data_dir, dataset, f"{model}_{prompt}{suffix}")
438	        if os.path.exists(path):
439	            break
440	    else:
441	        raise FileNotFoundError(f"No annotation file for {dataset}/{model}_{prompt}")
442	    records = []
443	    label_set = set()
444	    with open(path) as f:
445	        for line in f:
446	            rec = json.loads(line.strip())
447	            gl = rec.get('true_label', rec.get('gold_label'))
448	            pl = rec.get('predicted_label', rec.get('pred_label'))
449	            if gl is not None and pl is not None:
450	                label_set.add(gl)
451	                label_set.add(pl)
452	                records.append((gl, pl))
453	    if records and isinstance(records[0][0], str):
454	        sorted_labels = sorted(label_set)
455	        label_map = {l: i for i, l in enumerate(sorted_labels)}
456	        records = [(label_map[g], label_map[p]) for g, p in records]
457	    else:
458	        records = [(int(g), int(p)) for g, p in records]
459	    return records
460	
461	
462	def build_confusion_matrix(records, K):
463	    counts = np.zeros((K, K))
464	    for true_k, pred_k in records:
465	        if 0 <= true_k < K and 0 <= pred_k < K:
466	            counts[pred_k, true_k] += 1
467	    col_sums = counts.sum(axis=0)
468	    col_sums = np.where(col_sums < 1, 1, col_sums)
469	    return counts / col_sums
470	
471	
472	def load_all_confusion_matrices(data_dir, dataset_filter=None):
473	    matrices = {}
474	    for dataset, info in DATASETS.items():
475	        if dataset_filter and dataset not in dataset_filter:
476	            continue
477	        K = info['K']
478	        for model in MODELS:
479	            for prompt in PROMPTS:
480	                try:
481	                    C = load_confusion_matrix_npz(data_dir, dataset, model, prompt, K)
482	                    matrices[(dataset, model, prompt)] = C
483	                except (FileNotFoundError, Exception):
484	                    try:
485	                        records = load_annotations(data_dir, dataset, model, prompt)
486	                        C = build_confusion_matrix(records, K)
487	                        matrices[(dataset, model, prompt)] = C
488	                    except FileNotFoundError:
489	                        print(f"  [WARN] Missing: {dataset}/{model}_{prompt}")
490	    return matrices
491	
492	
493	# ============================================================================
494	# 2. Downstream Causal Bias
495	# ============================================================================
496	
497	def compute_bias_for_topology(C, K, topology, st, tau_true):
498	    plim_result = compute_plim(C, st, K)
499	    tau_hat = extract_tau(plim_result, topology)
500	    if np.isnan(tau_hat) or np.isnan(tau_true):
501	        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}
502	    bias = tau_hat - tau_true
503	    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None
504	    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)
505	    return {
506	        'tau_hat': float(tau_hat), 'bias': float(bias),
507	        'bias_pct': float(bias_pct) if bias_pct is not None else None,
508	        'sign_flip': sign_flip,
509	    }
510	
511	
512	def compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):
513	    results = []
514	    for (dataset, model, prompt), C in confusion_matrices.items():
515	        K = DATASETS[dataset]['K']
516	        for topology in TOPOLOGIES:
517	            st = all_suff_stats[(K, topology)]
518	            tau_true = all_tau_true[(K, topology)]
519	            info = compute_bias_for_topology(C, K, topology, st, tau_true)
520	            results.append({
521	                'dataset': dataset, 'model': model, 'prompt': prompt,
522	                'K': K, 'topology': topology, **info,
523	            })
524	    return results
525	
526	
527	# ============================================================================
528	# 3. ASV Computation
529	# ============================================================================
530	
531	def C_interpolated(C0, delta, K):
532	    C_d = (1 - delta) * np.eye(K) + delta * C0
533	    C_d = np.maximum(C_d, 0.0)
534	    col_sums = C_d.sum(axis=0)
535	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
536	    return C_d / col_sums
537	
538	
539	def compute_delta_max(C0):
540	    min_diag = np.diag(C0).min()
541	    if min_diag >= 1.0:
542	        return 10.0
543	    return min(1.0 / (1.0 - min_diag), 10.0)
544	
545	
546	def compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,
547	                           n_grid=1500, se_ref=None):
548	    dmax = compute_delta_max(C0)
549	    deltas = np.linspace(0, dmax, n_grid)
550	    tau_curve = np.zeros(n_grid)
551	    for i, d in enumerate(deltas):
552	        C_d = C_interpolated(C0, d, K)
553	        plim_result = compute_plim(C_d, st, K)
554	        tau_curve[i] = extract_tau(plim_result, topology)
555	
556	    bias_abs = np.abs(tau_curve - tau_true)
557	    envelope = np.zeros(n_grid)
558	    running_max = 0.0
559	    for i in range(n_grid):
560	        if np.isfinite(bias_abs[i]):
561	            running_max = max(running_max, bias_abs[i])
562	        envelope[i] = running_max
563	
564	    if asv_type == 'sign_flip':
565	        if abs(tau_true) < 1e-12:
566	            return None
567	        baseline_sign = np.sign(tau_true)
568	        for i in range(n_grid):
569	            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:
570	                return float(deltas[i])
571	        return None
572	    elif asv_type == 'magnitude':
573	        if abs(tau_true) < 1e-12:
574	            return None
575	        thresh = 0.1 * abs(tau_true)
576	        for i in range(n_grid):
577	            if envelope[i] > thresh:
578	                return float(deltas[i])
579	        return None
580	    elif asv_type == 'significance':
581	        if se_ref is None or se_ref < 1e-12:
582	            return None
583	        for i in range(n_grid):
584	            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:
585	                return float(deltas[i])
586	        return None
587	    return None
588	
589	
590	def estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):
591	    gen_fn = GEN_FNS[topology]
592	    rng = np.random.default_rng(seed)
593	    tau_hats = []
594	    for _ in range(n_mc):
595	        first_var, Y, A = gen_fn(K, N_ref, params, rng)
596	        if topology == 'iv':
597	            th, _ = wald_estimator(first_var, Y, A, k=1)
598	        elif topology == 'exposure':
599	            b, _ = ols_no_T(Y, A, K)
600	            th = b[1]
601	        else:
602	            b, _ = ols_with_dummies(Y, first_var, A, K)
603	            th = b[1]
604	        if np.isfinite(th):
605	            tau_hats.append(th)
606	    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan
607	
608	
609	def compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):
610	    results = []
611	    for (dataset, model, prompt), C in confusion_matrices.items():
612	        K = DATASETS[dataset]['K']
613	        for topology in TOPOLOGIES:
614	            st = all_suff_stats[(K, topology)]
615	            tau_true = all_tau_true[(K, topology)]
616	            se_ref = all_se_ref.get((K, topology))
617	            for asv_type in ['magnitude', 'significance', 'sign_flip']:
618	                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,
619	                                             asv_type, se_ref=se_ref)
620	                results.append({
621	                    'dataset': dataset, 'model': model, 'prompt': prompt,
622	                    'K': K, 'topology': topology, 'asv_type': asv_type,
623	                    'asv': asv,
624	                })
625	    return results
626	
627	
628	# ============================================================================
629	# 4. F1 vs Downstream Bias
630	# ============================================================================
631	
632	def compute_f1_from_C(C, K, p_A=None):
633	    if p_A is None:
634	        p_A = np.ones(K) / K
635	    precision = np.zeros(K)
636	    recall = np.zeros(K)
637	    f1 = np.zeros(K)
638	    for i in range(K):
639	        recall[i] = C[i, i]
640	        denom = sum(C[i, j] * p_A[j] for j in range(K))
641	        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0
642	        if precision[i] + recall[i] > 1e-12:
643	            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])
644	    return {
645	        'macro_f1': float(f1.mean()),
646	        'weighted_f1': float((p_A * f1).sum()),
647	        'per_class_f1': f1.tolist(),
648	    }
649	
650	
651	def f1_vs_bias_analysis(confusion_matrices, biases):
652	    results = []
653	    for b in biases:
654	        key = (b['dataset'], b['model'], b['prompt'])
655	        if key not in confusion_matrices:
656	            continue
657	        C = confusion_matrices[key]
658	        K = b['K']
659	        p_A = make_p_A(K)
660	        f1_info = compute_f1_from_C(C, K, p_A)
661	        abs_bias = abs(b['bias']) if b['bias'] is not None else None
662	        results.append({
663	            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],
664	            'K': K, 'topology': b['topology'],
665	            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],
666	            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],
667	            'sign_flip': b['sign_flip'],
668	        })
669	    return results
670	
671	
672	# ============================================================================
673	# 5. Type I/II Error Rates
674	# ============================================================================
675	
676	def compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,
677	                              st_H1, tau_true,
678	                              n_sim=100, N_sample=5000, seed=42):
679	    gen_fn = GEN_FNS[topology]
680	    rng = np.random.default_rng(seed)
681	
682	    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')
683	    asv_safe = (masv is None or masv > 1.0)
684	
685	    def _run_mc(params_t, n):
686	        valid = 0; rej = 0
687	        for _ in range(n):
688	            fv, Y, A = gen_fn(K, N_sample, params_t, rng)
689	            Astar = generate_Astar(A, C, rng)
690	            if topology == 'iv':
691	                th, se = wald_estimator(fv, Y, Astar, k=1)
692	            elif topology == 'exposure':
693	                b, svec = ols_no_T(Y, Astar, K)
694	                th, se = b[1], svec[1]
695	            else:
696	                b, svec = ols_with_dummies(Y, fv, Astar, K)
697	                th, se = b[1], svec[1]
698	            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:
699	                valid += 1
700	                if abs(th / se) > 1.96:
701	                    rej += 1
702	        return rej / max(valid, 1), valid
703	
704	    type1_before, v0 = _run_mc(params_H0[topology], n_sim)
705	    power_before, v1 = _run_mc(params_H1[topology], n_sim)
706	    type1_after = type1_before if asv_safe else 0.0
707	    power_after = power_before if asv_safe else 0.0
708	
709	    return {
710	        'type1_before': float(type1_before), 'type1_after': float(type1_after),
711	        'power_before': float(power_before), 'power_after': float(power_after),
712	        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,
713	        'valid_h0': int(v0), 'valid_h1': int(v1),
714	    }
715	
716	
717	# ============================================================================
718	# 6. Inter-model Error Correlation
719	# ============================================================================
720	
721	def compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,
722	                                    n_samples=1000, seed=42):
723	    rng = np.random.default_rng(seed)
724	    p_A = make_p_A(K)
725	    true_labels = rng.choice(K, size=n_samples, p=p_A)
726	
727	    predictions = {}
728	    for model in MODELS:
729	        key = (dataset, model, prompt)
730	        if key in confusion_matrices:
731	            predictions[model] = generate_Astar(true_labels,
732	                                                confusion_matrices[key], rng)
733	        else:
734	            predictions[model] = true_labels.copy()
735	
736	    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]
737	    results = {}
738	    for m1, m2 in pairs:
739	        p1, p2 = predictions[m1], predictions[m2]
740	        agreement = float((p1 == p2).mean())
741	        observed = agreement
742	        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))
743	        kappa = float((observed - expected) / (1 - expected)
744	                      ) if expected < 1 - 1e-10 else 0.0
745	        err1 = (p1 != true_labels).astype(float)
746	        err2 = (p2 != true_labels).astype(float)
747	        if err1.std() > 1e-10 and err2.std() > 1e-10:
748	            error_corr = float(np.corrcoef(err1, err2)[0, 1])
749	        else:
750	            error_corr = 0.0
751	        results[f"{m1}-{m2}"] = {
752	            'agreement': agreement,
753	            'kappa': kappa,
754	            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,
755	        }
756	    return results
757	
758	
759	# ============================================================================
760	# Mock Data Generation
761	# ============================================================================
762	
763	def generate_mock_C(K, rng, diag_range):
764	    C = np.zeros((K, K))
765	    for j in range(K):
766	        diag_val = rng.uniform(diag_range[0], diag_range[1])
767	        remaining = 1.0 - diag_val
768	        if K > 2:
769	            dists = np.abs(np.arange(K) - j).astype(float)
770	            dists[j] = np.inf
771	            weights = 1.0 / dists
772	            weights[j] = 0
773	            noise = rng.uniform(0.5, 1.5, K)
774	            noise[j] = 0
775	            weights = weights * noise
776	            weights /= weights.sum()
777	            C[:, j] = remaining * weights
778	        else:
779	            C[1 - j, j] = remaining
780	        C[j, j] = diag_val
781	    return C
782	
783	
784	def generate_mock_confusion_matrices(seed=12345):
785	    rng = np.random.default_rng(seed)
786	    matrices = {}
787	    diag_ranges = {
788	        'civil_comments': (0.85, 0.95),
789	        'vast': (0.70, 0.90),
790	        'humaid': (0.60, 0.85),
791	    }
792	    for dataset, info in DATASETS.items():
793	        K = info['K']
794	        dr = diag_ranges[dataset]
795	        for model in MODELS:
796	            for prompt in PROMPTS:
797	                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)
798	    return matrices
799	
800	
801	# ============================================================================
802	# Diagnostic Plots (optional)
803	# ============================================================================
804	
805	def save_f1_vs_bias_plot(f1_bias, output_dir):
806	    if not HAS_MPL:
807	        return
808	    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
809	    axes = axes.flatten()
810	    for idx, topo in enumerate(TOPOLOGIES):
811	        ax = axes[idx]
812	        subset = [r for r in f1_bias if r['topology'] == topo
813	                  and r['abs_bias'] is not None]
814	        if not subset:
815	            ax.set_title(topo)
816	            continue
817	        f1s = [r['macro_f1'] for r in subset]
818	        biases = [r['abs_bias'] for r in subset]
819	        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]
820	        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)
821	        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)
822	        ax.set_xlabel('Macro F1')
823	        ax.set_ylabel('|bias|')
824	        ax.set_title(topo)
825	    if len(TOPOLOGIES) < 8:
826	        axes[-1].axis('off')
827	    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)
828	    fig.tight_layout(rect=[0, 0, 1, 0.96])
829	    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)
830	    plt.close(fig)
831	
832	
833	def save_asv_heatmap(asvs, output_dir):
834	    if not HAS_MPL:
835	        return
836	    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']
837	    datasets_list = list(DATASETS.keys())
838	    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
839	    for didx, dataset in enumerate(datasets_list):
840	        ax = axes[didx]
841	        subset = [r for r in mag_asvs if r['dataset'] == dataset]
842	        configs = sorted(set((r['model'], r['prompt']) for r in subset))
843	        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)
844	        for r in subset:
845	            ti = TOPOLOGIES.index(r['topology'])
846	            ci = configs.index((r['model'], r['prompt']))
847	            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan
848	        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',
849	                       vmin=0, vmax=2)
850	        ax.set_xticks(range(len(configs)))
851	        ax.set_xticklabels([f"{m[:3]}_{p[:3]}" for m, p in configs],
852	                           rotation=45, ha='right', fontsize=7)
853	        ax.set_yticks(range(len(TOPOLOGIES)))
854	        ax.set_yticklabels(TOPOLOGIES, fontsize=8)
855	        ax.set_title(f'{dataset} (K={DATASETS[dataset]["K"]})')
856	        plt.colorbar(im, ax=ax, shrink=0.8)
857	    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)
858	    fig.tight_layout(rect=[0, 0, 1, 0.96])
859	    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)
860	    plt.close(fig)
861	
862	
863	# ============================================================================
864	# JSON Serialization
865	# ============================================================================
866	
867	def _to_json_safe(obj):
868	    if isinstance(obj, np.integer):
869	        return int(obj)
870	    elif isinstance(obj, np.floating):
871	        v = float(obj)
872	        return None if (np.isnan(v) or np.isinf(v)) else v
873	    elif isinstance(obj, np.ndarray):
874	        return _to_json_safe(obj.tolist())
875	    elif isinstance(obj, dict):
876	        return {str(k): _to_json_safe(v) for k, v in obj.items()}
877	    elif isinstance(obj, list):
878	        return [_to_json_safe(v) for v in obj]
879	    elif isinstance(obj, (bool, np.bool_)):
880	        return bool(obj)
881	    elif isinstance(obj, float):
882	        return None if (np.isnan(obj) or np.isinf(obj)) else obj
883	    return obj
884	
885	
886	# ============================================================================
887	# Main
888	# ============================================================================
889	
890	def main():
891	    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')
892	    parser.add_argument('--data-dir', default='data/')
893	    parser.add_argument('--output-dir', default='artifacts/plan006/')
894	    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')
895	    parser.add_argument('--datasets', type=str, default=None,
896	                        help='Comma-separated dataset filter (e.g. humaid,vast)')
897	    parser.add_argument('--n-sim', type=int, default=1000)
898	    parser.add_argument('--device', type=str, default='cpu')
899	    args = parser.parse_args()
900	
901	    os.makedirs(args.output_dir, exist_ok=True)
902	    t_total = time.time()
903	    n_precomp = 500_000 if args.mock else N_PRECOMP
904	
905	    dataset_filter = None
906	    if args.datasets:
907	        dataset_filter = [d.strip() for d in args.datasets.split(',')]
908	
909	    print("=" * 70)
910	    print("plan_006: Empirical ASV Calibration")
911	    if dataset_filter:
912	        print(f"  Dataset filter: {dataset_filter}")
913	    print("=" * 70)
914	
915	    # --- 1. Confusion matrices ---
916	    if args.mock:
917	        print("\n[1/6] Generating mock confusion matrices...")
918	        confusion_matrices = generate_mock_confusion_matrices()
919	        if dataset_filter:
920	            confusion_matrices = {k: v for k, v in confusion_matrices.items()
921	                                  if k[0] in dataset_filter}
922	    else:
923	        print("\n[1/6] Loading confusion matrices...")
924	        confusion_matrices = load_all_confusion_matrices(args.data_dir,
925	                                                         dataset_filter=dataset_filter)
926	
927	    print(f"  {len(confusion_matrices)} matrices loaded")
928	    for (ds, m, p), C in list(confusion_matrices.items())[:3]:
929	        K = DATASETS[ds]['K']
930	        print(f"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}")
931	
932	    # --- 2. Precompute sufficient statistics ---
933	    print("\n[2/6] Precomputing sufficient statistics...")
934	    active_datasets = dataset_filter if dataset_filter else list(DATASETS.keys())
935	    K_values = sorted(set(DATASETS[ds]['K'] for ds in active_datasets if ds in DATASETS))
936	    all_suff_stats = {}
937	    all_tau_true = {}
938	    all_params = {}
939	    all_params_H0 = {}
940	    all_se_ref = {}
941	
942	    for K in K_values:
943	        params = make_dgp_params(K)
944	        params_H0 = make_dgp_params_H0(K, params)
945	        all_params[K] = params
946	        all_params_H0[K] = params_H0
947	        for topology in TOPOLOGIES:
948	            seed = K * 1000 + abs(hash(topology)) % 1000
949	            st = precompute_suff_stats(K, topology, params[topology],
950	                                       N=n_precomp, seed=seed)
951	            plim_I = compute_plim(np.eye(K), st, K)
952	            tau_true = extract_tau(plim_I, topology)
953	            all_suff_stats[(K, topology)] = st
954	            all_tau_true[(K, topology)] = tau_true
955	
956	            se = estimate_reference_se(K, topology, params[topology],
957	                                       N_ref=5000,
958	                                       n_mc=min(args.n_sim, 30),
959	                                       seed=seed + 500)
960	            all_se_ref[(K, topology)] = se
961	            se_s = f"{se:.4f}" if np.isfinite(se) else "N/A"
962	            print(f"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}")
963	
964	    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)
965	    n_sign_flips = sum(1 for b in biases if b['sign_flip'])
966	    print(f"  {len(biases)} bias values ({n_sign_flips} sign flips)")
967	
968	    # --- 3. ASV ---
969	    print("\n[3/6] Computing ASV values...")
970	    t3 = time.time()
971	    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,
972	                            all_tau_true, all_se_ref)
973	    print(f"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)")
974	    for at in ['magnitude', 'sign_flip', 'significance']:
975	        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]
976	        if sub:
977	            print(f"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} "
978	                  f"max={max(sub):.3f} ({len(sub)} non-None)")
979	
980	    # --- 4. F1 vs bias ---
981	    print("\n[4/6] F1 vs bias analysis...")
982	    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)
983	    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]
984	    high_f1_high_bias = [r for r in total_high_f1
985	                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]
986	    if total_high_f1:
987	        pct = len(high_f1_high_bias) / len(total_high_f1) * 100
988	        print(f"  Baumann check: F1>0.93 with |bias|>0.05: "
989	              f"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%")
990	    # Sample rows
991	    for r in f1_bias[:3]:
992	        print(f"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: "
993	              f"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}")
994	
995	    # --- 5. Type I/II ---
996	    print("\n[5/6] Type I/II error rates...")
997	    t5 = time.time()
998	    type1_type2_results = []
999	    n_configs = len(confusion_matrices) * len(TOPOLOGIES)
1000	    idx = 0
1001	    for (dataset, model, prompt), C in confusion_matrices.items():
1002	        K = DATASETS[dataset]['K']
1003	        for topology in TOPOLOGIES:
1004	            idx += 1
1005	            st = all_suff_stats[(K, topology)]
1006	            tau_true = all_tau_true[(K, topology)]
1007	            r = compute_type1_type2_for_C(
1008	                C, K, topology, all_params[K], all_params_H0[K],
1009	                st, tau_true,
1010	                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)
1011	            type1_type2_results.append({
1012	                'dataset': dataset, 'model': model, 'prompt': prompt,
1013	                'K': K, 'topology': topology, **r,
1014	            })
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93eae332-e8ea-42a0-ae62-9d19dc47a65f",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "3fce8e11-971e-49d4-87da-27a5128fe82b",
  "sourceToolAssistantUUID": "93eae332-e8ea-42a0-ae62-9d19dc47a65f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-24T05:51:14.105Z_

Perfect! Now let me create a comprehensive summary. Let me check one more file to understand the utils module:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fce8e11-971e-49d4-87da-27a5128fe82b",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsWTGWG8GPTWhctULjn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c839a60e-c35a-4412-b2c7-9719492d4c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BcqbRrWsQPUCfvshMoKBvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9365,
      "cache_read_input_tokens": 50346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9365,
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

_source line 48 · 2026-05-24T05:51:14.917Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EJSLykA7sZhPw8M1qerFjo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c839a60e-c35a-4412-b2c7-9719492d4c1c",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsWTGWG8GPTWhctULjn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cce26171-29e4-418a-bdd9-2fa97d2e5b1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BcqbRrWsQPUCfvshMoKBvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9365,
      "cache_read_input_tokens": 50346,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 50346,
          "cache_creation_input_tokens": 9365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9365,
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

_source line 49 · 2026-05-24T05:51:14.924Z_

<details><summary>↩ Tool result · `toolu_01EJSLykA7sZhPw8M1qerFjo`</summary>

```text
1	"""Shared utilities: OLS, dummy encoding, softmax sampling."""
2	
3	import numpy as np
4	
5	
6	def softmax_sample(logits, rng):
7	    """Sample categorical variable from row-wise softmax probabilities.
8	
9	    Args:
10	        logits: (N, K) array of logits
11	        rng: numpy random Generator
12	
13	    Returns:
14	        (N,) integer array with values in {0, ..., K-1}
15	    """
16	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
17	    p = e / e.sum(axis=1, keepdims=True)
18	    cum = np.cumsum(p, axis=1)
19	    u = rng.uniform(size=logits.shape[0])
20	    K = logits.shape[1]
21	    result = np.zeros(logits.shape[0], dtype=int)
22	    for k in range(K - 1):
23	        result += (u >= cum[:, k]).astype(int)
24	    return result
25	
26	
27	def misclassify(A, C, rng):
28	    """Apply misclassification: A*_i ~ Cat(C[:, A_i]).
29	
30	    Args:
31	        A: (N,) true labels in {0, ..., K-1}
32	        C: (K, K) column-stochastic confusion matrix
33	        rng: numpy random Generator
34	
35	    Returns:
36	        (N,) misclassified labels
37	    """
38	    K = C.shape[0]
39	    probs = C[:, A]
40	    cum = np.cumsum(probs, axis=0)
41	    u = rng.uniform(size=len(A))
42	    result = np.zeros(len(A), dtype=int)
43	    for k in range(K - 1):
44	        result += (u >= cum[k]).astype(int)
45	    return result
46	
47	
48	def make_dummies(A, K=None):
49	    """Create K-1 dummy variables (reference category 0).
50	
51	    Args:
52	        A: (N,) categorical labels in {0, ..., K-1}
53	        K: number of categories (inferred from A if None)
54	
55	    Returns:
56	        (N, K-1) dummy matrix
57	    """
58	    if K is None:
59	        K = int(A.max()) + 1
60	    N = len(A)
61	    D = np.zeros((N, K - 1))
62	    for j in range(K - 1):
63	        D[:, j] = (A == j + 1).astype(float)
64	    return D
65	
66	
67	def make_full_dummies(A, K=None):
68	    """Create full K one-hot encoding.
69	
70	    Args:
71	        A: (N,) categorical labels in {0, ..., K-1}
72	        K: number of categories (inferred from A if None)
73	
74	    Returns:
75	        (N, K) one-hot matrix
76	    """
77	    if K is None:
78	        K = int(A.max()) + 1
79	    N = len(A)
80	    D = np.zeros((N, K))
81	    for j in range(K):
82	        D[:, j] = (A == j).astype(float)
83	    return D
84	
85	
86	def ols(X, Y):
87	    """OLS point estimate via least-squares.
88	
89	    Args:
90	        X: (N, p) design matrix
91	        Y: (N,) response
92	
93	    Returns:
94	        (p,) coefficient vector
95	    """
96	    return np.linalg.lstsq(X, Y, rcond=None)[0]
97	
98	
99	def ols_with_se(X, Y):
100	    """OLS point estimate with homoskedastic standard errors.
101	
102	    Args:
103	        X: (N, p) design matrix
104	        Y: (N,) response
105	
106	    Returns:
107	        (beta, se) tuple of (p,) arrays
108	    """
109	    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
110	    resid = Y - X @ beta
111	    n, p = X.shape
112	    s2 = resid @ resid / max(n - p, 1)
113	    try:
114	        XtX_inv = np.linalg.inv(X.T @ X)
115	        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))
116	    except np.linalg.LinAlgError:
117	        se = np.full(p, np.nan)
118	    return beta, se
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce26171-29e4-418a-bdd9-2fa97d2e5b1b",
  "isSidechain": true,
  "promptId": "5b74c029-15ae-4e30-b5da-d11d9fdeb357",
  "agentId": "aac218afbfff5d245",
  "type": "user",
  "uuid": "01ccd1f5-d3bd-4186-8378-1e9cb1942c54",
  "sourceToolAssistantUUID": "cce26171-29e4-418a-bdd9-2fa97d2e5b1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-24T05:51:43.167Z_

Excellent! Now I have all the information needed. Let me create a comprehensive report.

## Summary: 7-Topology Analytical Bias Computation

I've thoroughly analyzed the codebase and identified the complete framework for computing 7-topology analytical bias from confusion matrices. Here are the key findings:

### **Core Function Signatures**

#### **1. Main Bias Computation Function**

**File:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py`

```python
def compute_bias(topology, C, params=None):
    """Compute annotation-error bias for a given topology and confusion matrix.

    Args:
        topology: one of "confounding", "mediation", "collider", "exposure",
                  "mbias", "iv", "frontdoor"
        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
        params: optional DGP parameters dict, None uses defaults

    Returns:
        dict with tau_true, tau_biased, bias, bias_pct, topology
    """
```

This is the high-level API. It internally uses:

**Internal workflow:**
1. `_precompute(topology, params, K)` - Generates 2M samples, computes sufficient statistics (E_Y, E_DA, E_DA_Y, etc.)
2. `_get_tau(topology, C, stats, K)` - Extracts target coefficient from plim vector
3. Returns: `{tau_true, tau_biased, bias, bias_pct}`

---

#### **2. Low-Level Plim Computation Functions**

**File:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py`

```python
def _precompute(topology, params, K, seed=999):
    """Precompute sufficient statistics using large-sample DGP simulation (N=2M)."""
    # Returns: {E_Y, E_DA, E_DA_Y, E_T, E_T2, E_TY, E_DA_T, ...}

def _get_tau(topology, C, stats, K):
    """Extract target coefficient from plim vector."""
    # For IV: Wald estimator RF / (C @ FS)[1]
    # For topologies with T: OLS coefficient index 1
    # For topologies without T: OLS coefficient index 1

def _plim_with_T(C, stats, K):
    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
    # Computes (E[ZZ'])^{-1} E[ZY']

def _plim_no_T(C, stats, K):
    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""

def _plim_iv(C, stats, K):
    """Wald estimator plim: RF / (C @ FS)[1]."""
```

---

#### **3. ASV (Annotation Sensitivity Value) Computation**

**File:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py`

```python
def compute_asv(topology, C0, params=None, threshold_type="magnitude",
                threshold_value=0.1, n_grid=1500):
    """Compute Annotation Sensitivity Value for a topology and base confusion matrix.

    ASV is the minimum interpolation delta at which a bias threshold is crossed
    along the path C(delta) = (1-delta)*I + delta*C0.

    Args:
        topology: one of 7 DAG types
        C0: (K, K) base confusion matrix
        params: optional DGP parameters dict
        threshold_type: "magnitude" (relative to tau_true),
                        "significance" (threshold_value = SE),
                        "sign_flip" (sign of tau changes)
        threshold_value: threshold parameter (meaning depends on threshold_type)
        n_grid: number of delta grid points (default 1500)

    Returns:
        dict with asv, bias_curve, envelope, deltas, tau_true
    """
```

Supporting functions:
```python
def _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):
    """Compute bias along interpolation path C(delta) = (1-delta)*I + delta*C0."""
    # Returns: (deltas, bias_abs, tau_curve)

def _compute_envelope(bias_abs):
    """Compute running maximum (envelope) of absolute bias."""

def _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,
                             threshold_type, threshold_value):
    """Find delta at which envelope crosses threshold."""
```

---

### **The 7 Topologies and Their Parameter Configs**

**File:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py`

The 7 topologies are defined in `DEFAULT_PARAMS` and `GEN_FUNCS`:

```python
TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']

DEFAULT_PARAMS = {
    "confounding": {
        p_A: [0.40, 0.35, 0.25],       # Distribution over A
        alpha: [1.5, -1.0],              # A->T effect
        beta_A: [1.0, -0.5],             # A->Y effect
        beta_T: 2.0,                     # T->Y effect
        sigma_T: 1.0                     # Error variance
    },
    "mediation": {
        tau: 0.5,                        # T->Y effect (direct)
        gamma: [0.0, 0.5, -0.3],         # Baseline logits for A
        delta: [0.0, 0.8, -0.6],         # T->A effect
        beta: [0.0, 1.0, -0.5]           # A->Y effect
    },
    "collider": {
        tau: 1.0,                        # T->Y effect
        g: [0.0, 0.0, 0.0],              # Baseline logits
        dT: [0.0, 0.5, -0.3],            # T->A effect
        dY: [0.0, 0.8, 0.6]              # Y->A effect
    },
    "exposure": {
        beta: [0.0, 1.0, -0.5],          # A->Y effect
        p_A: [0.40, 0.35, 0.25]          # Distribution over A
    },
    "mbias": {
        tau: 1.0,                        # T->Y effect
        delta_coef: 1.0,                 # U1->T coefficient
        lam: 1.0,                        # U2->Y coefficient
        g: [0.0, 0.0, 0.0],              # Baseline A logits
        a1: [0.0, 0.8, -0.5],            # U1->A effect
        a2: [0.0, 0.6, 0.9]              # U2->A effect
    },
    "iv": {
        lam: 1.0,                        # U->Y effect
        g: [0.0, 0.0, 0.0],              # Baseline A logits
        dZ: [0.0, 1.0, -0.5],            # Z->A effect
        dU: [0.0, 0.8, 0.6],             # U->A effect
        beta: [0.0, 1.0, -0.5]           # A->Y effect
    },
    "frontdoor": {
        alpha_U: 1.0,                    # U->T coefficient
        lam_U: 1.0,                      # U->Y coefficient
        gamma: [0.0, 0.5, -0.3],         # Baseline M logits
        delta: [0.0, 1.0, -0.8],         # T->M effect
        beta: [0.0, 1.0, -0.5]           # M->Y effect
    }
}

# Topologies with treatment T
HAS_TREATMENT = {"confounding", "mediation", "collider", "mbias", "frontdoor"}
# Topologies without treatment T
NO_TREATMENT = {"exposure", "iv"}
```

---

### **How Sign Flips Are Counted**

**In compute_updated_empirical.py:**

```python
def check_exposure_sign_flips(plim_true, plim_biased, K):
    """Check ALL K-1 exposure coefficients for sign reversal.
    
    Returns (any_flip: bool, details: list of per-coefficient results).
    Coefficients are at indices 1..K-1 (index 0 is the intercept).
    """
    details = []
    any_flip = False
    for i in range(1, K):
        true_val = float(plim_true[i])
        biased_val = float(plim_biased[i])
        if not (np.isfinite(true_val) and np.isfinite(biased_val)):
            continue
        sf = bool(np.sign(biased_val) != np.sign(true_val)) if abs(true_val) > 1e-10 else False
        if sf:
            any_flip = True
        details.append({
            "coef_idx": i,
            "true": round(true_val, 6),
            "biased": round(biased_val, 6),
            "sign_flip": sf,
        })
    return any_flip, details
```

**For other topologies:**
```python
sf = bool(np.sign(tau_biased) != np.sign(tau_true)) if abs(tau_true) > 1e-10 else False
```

---

### **Key File Locations**

| File | Purpose |
|------|---------|
| `/annot_sensitivity/bias.py` | Core bias computation via plim |
| `/annot_sensitivity/asv.py` | ASV sensitivity measures |
| `/annot_sensitivity/dgp.py` | 7 topology DGPs and default parameters |
| `/annot_sensitivity/confusion.py` | Confusion matrix validation & interpolation |
| `/plan_006_asv_empirical.py` | Reference implementation used in papers |
| `/artifacts/compute_updated_empirical.py` | Empirical bias computation from real CMs |
| `/artifacts/compute_all_tasks.py` | Theory-empirical MAPE and PPI++ validation |

---

### **How to Call These Functions**

**Basic usage (from annot_sensitivity package):**

```python
import numpy as np
from annot_sensitivity import compute_bias, compute_asv, TOPOLOGIES, DEFAULT_PARAMS

# Load or define your confusion matrix
C = np.array([[0.8, 0.1, 0.05],
              [0.1, 0.8, 0.15],
              [0.1, 0.1, 0.8]])  # (3, 3) column-stochastic

# Compute bias for a single topology
result = compute_bias("confounding", C)
# Returns: {tau_true, tau_biased, bias, bias_pct, topology}

# Compute ASV
asv_result = compute_asv("confounding", C, threshold_type="magnitude", 
                         threshold_value=0.1, n_grid=1500)
# Returns: {asv, bias_curve, envelope, deltas, tau_true}
```

**Advanced usage (from plan_006):**

```python
from plan_006_asv_empirical import (
    make_dgp_params, precompute_suff_stats, compute_plim, extract_tau
)

K = 3
topology = "confounding"
params = make_dgp_params(K)[topology]

# Precompute sufficient stats from 2M samples
st = precompute_suff_stats(K, topology, params, N=2_000_000, seed=42)

# Compute plim with identity matrix (true case)
plim_I = compute_plim(np.eye(K), st, K)
tau_true = extract_tau(plim_I, topology)

# Compute plim with confusion matrix
plim_C = compute_plim(C, st, K)
tau_biased = extract_tau(plim_C, topology)
bias = tau_biased - tau_true
```

---

### **Confusion Matrix Convention**

- **C[j, i] = P(A*=j | A=i)** (column-stochastic: columns sum to 1)
- Each column represents the distribution of misclassified labels for a true label category
- Built via: `C = counts / col_sums` where `counts[predicted_k, true_k] += 1`

---

### **Interpolation Path for ASV**

```python
# C(delta) = (1-delta)*I + delta*C0
# delta=0 → perfect classification (identity matrix)
# delta=1 → full confusion matrix C0
# delta>1 → extrapolation of misclassification
```

Valid delta range is determined by:
```python
min_diag = min(diagonal(C0))
if min_diag >= 1.0:
    delta_max = 10.0
else:
    delta_max = min(1.0 / (1.0 - min_diag), 10.0)
```

This ensures column-stochasticity is maintained during interpolation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01ccd1f5-d3bd-4186-8378-1e9cb1942c54",
  "isSidechain": true,
  "agentId": "aac218afbfff5d245",
  "requestId": "req_011CbLsWcyQJ88eRnAWiWyoA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "032ccdc4-d902-475b-839c-ad51debb647f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a2fbfd3c-e945-434b-884f-78a68d8f84e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X3oDwGCqDjfHFz9Q3bDAB5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1467,
      "cache_read_input_tokens": 59711,
      "output_tokens": 3497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1467
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3497,
          "cache_read_input_tokens": 59711,
          "cache_creation_input_tokens": 1467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1467,
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
