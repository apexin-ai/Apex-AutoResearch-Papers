# code analyze expanded

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_code_analyze-expanded_20260516T080105.jsonl`
- **Structured JSON:** [`41d6802e69cafcc66afc.json`](../../sessions/41/41d6802e69cafcc66afc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-16T08:04:40.330275+00:00_

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
  "session": "worker_code_analyze-expanded_20260516T080105",
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

_source line 2 · 2026-05-16T08:04:40.330691+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T08:04:40.330934+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls -la /root/symb_invariant_consensus/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls -la /root/symb_invariant_consensus/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T08:04:40.331142+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/symb_invariant_consensus/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/symb_invariant_consensus/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T08:04:40.331308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1040\\ndrwxr-xr-x  2 root root   4096 May 16 14:50 .\\ndrwxr-xr-x 13 root root   4096 May 16 13:30 ..\\n-rw-r--r--  1 root root   1947 May 15 21:08 aime30_t07.json\\n-rw-r--r--  1 root root  27082 May 16 03:06 aime30_v2.json\\n-rw-r--r--  1 root root   5571 May 15 23:48 aime30_v2_partial_backup.json\\n-rw-r--r--  1 root root   2677 May 16 00:56 aime30_v2_rescore_analysis.json\\n-rw-r--r--  1 root root  10770 May 16 11:34 c0_precheck_qwen14b.json\\n-rw-r--r--  1 root root  37812 May 16 14:50 constraint_ablation.json\\n-rw-r--r--  1 root root   3048 May 16 11:36 d016_smoke_test.json\\n-rw-r--r--  1 root root   7147 May 15 20:12 diversity_diagnosis.json\\n-rw-r--r--  1 root root   2554 May 16 06:27 folio_livetest.json\\n-rw-r--r--  1 root root  31655 May 16 09:35 proofwriter_30_v2.json\\n-rw-r--r--  1 root root   9679 May 16 10:56 proofwriter_5_l3l1_fix.json\\n-rw-r--r--  1 root root   5993 May 16 13:29 qwq_operating_regime.json\\n-rw-r--r--  1 root root   3946 May 16 13:30 qwq_operating_regime.md\\n-rw-r--r--  1 root root   8004 May 16 01:27 rescore_pure_results.json\\n-rw-r--r--  1 root root 236672 May 16 13:03 sica_d012_14b.json\\n-rw-r--r--  1 root root 629241 May 16 16:01 sica_expanded_14b.json\\n-rw-r--r--  1 root root   1855 May 15 19:19 smoke_test_5q.json\\n-rw-r--r--  1 root root   1479 May 16 13:14 tiebreak_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T08:04:40.331454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README_experiments.md\\n__pycache__\\nconstraint_ablation.py\\neval_gsm8k.py\\nprepare_gsm8k.py\\nrun_k_ablation.py\\nstart_vllm_72b_awq.sh\\nstart_vllm_7b.sh\\nstart_vllm_deepseek_r1_7b.sh\\nstart_vllm_deepseek_r1_8b.sh\\nstart_vllm_llama_8b.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T08:04:40.331610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "head -200 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "head -200 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T08:04:40.331733+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "head -100 /root/symb_invariant_consensus/results/sica_d012_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "head -100 /root/symb_invariant_consensus/results/sica_d012_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T08:04:40.332012+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 155,\\n    \\\"sica_accuracy\\\": 0.7548387096774194,\\n    \\\"sc_accuracy\\\": 0.7677419354838709,\\n    \\\"sica_correct\\\": 117,\\n    \\\"sc_correct\\\": 119,\\n    \\\"extraction_rate\\\": 0.8349462365591398,\\n    \\\"answer_extraction_rate\\\": 1.0,\\n    \\\"answer_extraction_counts\\\": {\\n      \\\"boxed\\\": 1860,\\n      \\\"fallback\\\": 0,\\n      \\\"none\\\": 0\\n    },\\n    \\\"truncated_traces\\\": 0,\\n    \\\"total_constraints_extracted\\\": 17718,\\n    \\\"total_unique_constraints\\\": 3163,\\n    \\\"contradiction_rate\\\": 0.024660132785330382,\\n    \\\"problems_with_contradictions\\\": 66,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"D5\\\": {\\n        \\\"sica\\\": 0.7548387096774194,\\n        \\\"sc\\\": 0.7677419354838709,\\n        \\\"n\\\": 155\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.7548387096774194,\\n        \\\"sc\\\": 0.7677419354838709,\\n        \\\"n\\\": 155\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 9950.1\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Given the following facts and rules:\\\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie 
…[truncated 6255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T08:04:40.332251+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 60,\\n    \\\"sica_accuracy\\\": 0.7333333333333333,\\n    \\\"sc_accuracy\\\": 0.7,\\n    \\\"sica_correct\\\": 44,\\n    \\\"sc_correct\\\": 42,\\n    \\\"extraction_rate\\\": 0.95,\\n    \\\"answer_extraction_rate\\\": 1.0,\\n    \\\"answer_extraction_counts\\\": {\\n      \\\"boxed\\\": 720,\\n      \\\"fallback\\\": 0,\\n      \\\"none\\\": 0\\n    },\\n    \\\"truncated_traces\\\": 0,\\n    \\\"total_constraints_extracted\\\": 5849,\\n    \\\"total_unique_constraints\\\": 1735,\\n    \\\"contradiction_rate\\\": 0.025936599423631124,\\n    \\\"problems_with_contradictions\\\": 34,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"D5\\\": {\\n        \\\"sica\\\": 0.6666666666666666,\\n        \\\"sc\\\": 0.6666666666666666,\\n        \\\"n\\\": 30\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.8,\\n        \\\"sc\\\": 0.7333333333333333,\\n        \\\"n\\\": 30\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.6666666666666666,\\n        \\\"sc\\\": 0.6666666666666666,\\n        \\\"n\\\": 30\\n      },\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.8,\\n        \\\"sc\\\": 0.7333333333333333,\\n        \\\"n\\\": 30\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 3499.6\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNeg-OWA-D5-979_Q9\\\",\\n      \\\"problem\\\": \\\"Given the following facts and rules:\\\\nCharlie is red. Dave is red. Dave is rough. Dave is round. Dave is young. Fiona is quiet. Fiona is red. Harry is furry. Harry is kind. Harry is young. All rough things are round. All rough things are round. All round, rough things are young. All red things are young. If Fiona is young and Fiona is not furry then Fiona is kind. If something is fur
…[truncated 1905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T08:04:40.332415+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/results/tiebreak_analysis.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/results/tiebreak_analysis.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T08:04:40.332593+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_total\\\": 60,\\n  \\\"n_tie\\\": 5,\\n  \\\"tie_problem_indices\\\": [\\n    3,\\n    11,\\n    29,\\n    42,\\n    59\\n  ],\\n  \\\"strategies\\\": {\\n    \\\"sica\\\": {\\n      \\\"accuracy\\\": 0.8,\\n      \\\"correct\\\": 4,\\n      \\\"total\\\": 5\\n    },\\n    \\\"random\\\": {\\n      \\\"accuracy_mean\\\": 0.4998,\\n      \\\"ci_95\\\": [\\n        0.0,\\n        1.0\\n      ]\\n    },\\n    \\\"alphabetical\\\": {\\n      \\\"accuracy\\\": 0.6,\\n      \\\"correct\\\": 3,\\n      \\\"total\\\": 5\\n    },\\n    \\\"first_seen\\\": {\\n      \\\"accuracy\\\": 0.4,\\n      \\\"correct\\\": 2,\\n      \\\"total\\\": 5\\n    },\\n    \\\"majority_first_6\\\": {\\n      \\\"accuracy\\\": 0.6,\\n      \\\"correct\\\": 3,\\n      \\\"total\\\": 5\\n    }\\n  },\\n  \\\"sica_wins\\\": [\\n    {\\n      \\\"problem_idx\\\": 11,\\n      \\\"scores\\\": {\\n        \\\"False\\\": 145.5,\\n        \\\"True\\\": 101.5,\\n        \\\"Unknown\\\": 127.0\\n      },\\n      \\\"ground_truth\\\": \\\"False\\\"\\n    },\\n    {\\n      \\\"problem_idx\\\": 29,\\n      \\\"scores\\\": {\\n        \\\"False\\\": 3.0,\\n        \\\"Unknown\\\": 33.0\\n      },\\n      \\\"ground_truth\\\": \\\"Unknown\\\"\\n    },\\n    {\\n      \\\"problem_idx\\\": 42,\\n      \\\"scores\\\": {\\n        \\\"Unknown\\\": 45.0,\\n        \\\"False\\\": 46.0\\n      },\\n      \\\"ground_truth\\\": \\\"False\\\"\\n    },\\n    {\\n      \\\"problem_idx\\\": 59,\\n      \\\"scores\\\": {\\n        \\\"False\\\": 61.0,\\n        \\\"Unknown\\\": 64.0\\n      },\\n      \\\"ground_truth\\\": \\\"Unknown\\\"\\n    }\\n  ],\\n  \\\"sica_losses\\\": [\\n    {\\n      \\\"problem_idx\\\": 3,\\n      \\\"scores\\\": {\\n        \\\"True\\\": 102.0,\\n        \\\"Unknown\\\": 105.0\\n      },\\n      \\\"ground_truth\\\": \\\"True\\\",\\n      \\\"sica_answer\\\": \\\"Unknown\\\"\\n    }\\n  ],\\n  \\\"near_ties\\\": {\\n    \\\"n
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:04:40.332750+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/scripts/constraint_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/scripts/constraint_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T08:04:40.333024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nexp-013: Constraint Ablation Study\\n\\nCompares three constraint aggregation methods on exp-001 (sica_expanded_14b) data\\nto demonstrate that MaxSAT satisfiability checking outperforms simple counting.\\n\\nMethods:\\n  A) SICA-MaxSAT     — weighted partial MaxSAT + A+C scorer (current pipeline)\\n  B) SICA-count-only  — sum all constraint weights per answer, no SAT filtering\\n  C) SICA-random-weight — MaxSAT with randomized constraint weights (seed=42)\\n\\nInput:\\n  - exp-001 results file (results/sica_expanded_14b.json)\\n  - Optional: constraint cache JSON for exact count-only / random-weight computation\\n\\nWhen no constraint cache is available:\\n  - Method A reads stored MaxSAT results (exact)\\n  - Method B uses proportional excluded-weight approximation\\n  - Method C uses score-perturbation simulation\\n  Results are flagged as approximate (~) in the output.\\n\\nUsage:\\n  python scripts/constraint_ablation.py --data-dir results\\n  python scripts/constraint_ablation.py --data-dir results --constraint-cache results/constraints_cache.json\\n  python scripts/constraint_ablation.py --help\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport math\\nimport os\\nimport random\\nimport sys\\nfrom collections import Counter\\n\\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\nALPHA = 0.5  # scorer penalty weight for excluded constraints\\n\\ntry:\\n    from sica.z3_maxsat import (\\n        ConstraintDeduplicator, MaxSATSolver, UniqueConstraint, MaxSATResult,\\n    )\\n    from sica.scorer import InvariantScorer\\n    HAS_Z3 = True\\nexcept ImportError:\\n    HAS_Z3
…[truncated 7284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T08:04:40.333217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); s=d['summary']; print(f'n={s[\\\"n_problems\\\"]}'); print('datasets:', s.get('per_dataset_accuracy',{}).keys()); print('levels:', s.get('per_level_accuracy',{}).keys()); [print(f'  {k}: n={v[\\\"n\\\"]}') for k,v in s.get('per_dataset_accuracy',{}).items()]\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); s=d['summary']; print(f'n={s[\\\"n_problems\\\"]}'); print('datasets:', s.get('per_dataset_accuracy',{}).keys()); print('levels:', s.get('per_level_accuracy',{}).keys()); [print(f'  {k}: n={v[\\\"n\\\"]}') for k,v in s.get('per_dataset_accuracy',{}).items()]\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T08:04:40.333358+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T08:04:40.333480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); r=d['results'][-1]; print(json.dumps({k:r[k] for k in ['problem_idx','problem_id','dataset','level','ground_truth','sica_answer','sica_correct','sc_answer','sc_vote_distribution','sc_correct']}, indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); r=d['results'][-1]; print(json.dumps({k:r[k] for k in ['problem_idx','problem_id','dataset','level','ground_truth','sica_answer','sica_correct','sc_answer','sc_vote_distribution','sc_correct']}, indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T08:04:40.333602+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T08:04:40.333718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); s=d['summary']; print(s['n_problems']); print(s.get('per_dataset_accuracy',{})); print(s.get('per_level_accuracy',{}))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/sica_expanded_14b.json')); s=d['summary']; print(s['n_problems']); print(s.get('per_dataset_accuracy',{})); print(s.get('per_level_accuracy',{}))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T08:04:40.333845+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T08:04:40.333987+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "grep -o '\"n_problems\": [0-9]*' /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "grep -o '\"n_problems\": [0-9]*' /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T08:04:40.334106+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"n_problems\\\": 155\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T08:04:40.334218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "grep '\"per_dataset_accuracy\"' -A 20 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "grep '\"per_dataset_accuracy\"' -A 20 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T08:04:40.334355+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.7548387096774194,\\n        \\\"sc\\\": 0.7677419354838709,\\n        \\\"n\\\": 155\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 9950.1\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Given the following facts and rules:\\\\nBob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie is kind.\\\",\\n      \\\"dataset\\\": \\\"proofwriter\\\",\\n      \\\"level\\\": \\\"D5\\\",\\n      \\\"ground_truth\\\": \\\"True\\\",\\n      \\\"sica_answer\\\": \\\"True\\\",\\n      \\\"sica_scores\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T08:04:40.334487+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "tail -5 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "tail -5 /root/symb_invariant_consensus/results/sica_expanded_14b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T08:04:40.334607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"        }\\n      ]\\n    }\\n  ]\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T08:04:40.334763+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "find /root/symb_invariant_consensus -name \"run_full_mvp.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "find /root/symb_invariant_consensus -name \"run_full_mvp.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T08:04:40.334907+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/run_full_mvp.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T08:04:40.335245+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "grep -n \"sc_vote\\|tie\\|vote_distribution\\|majority\" /root/symb_invariant_consensus/run_full_mvp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "grep -n \"sc_vote\\|tie\\|vote_distribution\\|majority\" /root/symb_invariant_consensus/run_full_mvp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T08:04:40.335435+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T08:04:40.335574+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "grep -n \"sc_vote\\|tie\\|vote_distribution\\|majority\" /root/symb_invariant_consensus/run_full_mvp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "grep -n \"sc_vote\\|tie\\|vote_distribution\\|majority\" /root/symb_invariant_consensus/run_full_mvp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T08:04:40.335693+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T08:04:40.335808+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "grep -n \"sc_vote\" /root/symb_invariant_consensus/run_full_mvp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "grep -n \"sc_vote\" /root/symb_invariant_consensus/run_full_mvp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T08:04:40.335945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "grep -n \"tie\" /root/symb_invariant_consensus/run_full_mvp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "grep -n \"tie\" /root/symb_invariant_consensus/run_full_mvp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T08:04:40.336070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"360:            \\\"sc_vote_count\\\": sc_result.get(\\\"vote_count\\\", 0),\\n361:            \\\"sc_vote_distribution\\\": sc_result.get(\\\"vote_distribution\\\", {}),\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T08:04:40.336185+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T08:04:40.336387+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/analyze_expanded.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nexp-001 expanded analysis: per-dataset accuracy, tiebreak stats, McNemar tests.\n\nInput:  results/sica_expanded_14b.json (single JSON with summary + results array)\nOutput: markdown summary table (stdout) + analysis.json\n\nDependencies: Python 3.8+ (no external packages required; scipy optional for chi2 McNemar)\n\nUsage:\n  python scripts/analyze_expanded.py\n  python scripts/analyze_expanded.py --results-dir results/sica_expanded_14b.json\n  python scripts/analyze_expanded.py --results-dir results/ --output results/analysis.json\n  python scripts/analyze_expanded.py --d012 results/sica_d012_14b.json\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nfrom collections import Counter, defaultdict\n\n\n# ── Answer normalization ─────────────────────────────────────────\n\ndef _normalize_logic(ans: str) -> str:\n    s = str(ans).strip().lower()\n    mapping = {\n        \"true\": \"True\", \"t\": \"True\", \"yes\": \"True\",\n        \"false\": \"False\", \"f\": \"False\", \"no\": \"False\",\n        \"unknown\": \"Unknown\", \"u\": \"Unknown\", \"uncertain\": \"Unknown\",\n    }\n    return mapping.get(s, str(ans).strip())\n\n\n# ── McNemar's test (exact binomial, no scipy needed) ─────────────\n\ndef mcnemar_pvalue(a_correct: list[bool], b_correct: list[bool]) -> float:\n    \"\"\"Two-sided McNemar's test using exact binomial distribution.\"\"\"\n    n10 = sum(a and not b for a, b in zip(a_correct, b_correct))\n    n01 = sum(not a and b for a, b in zip(a_correct, b_correct))\n    n = n10 + n01\n    if n == 0:\n        return 1.0\n    k = min(n10, n01)\n    p = sum(math.comb(n, i) * 0.5 ** n for i in range(k + 1))\n    return min(2.0 * p, 1.0)\n\n\n# ── Core analysis ────────────────────────────────────────────────\n\ndef is_sc_tie(vote_dist: dict) -> bool:\n    \"\"\"SC tie: ≥2 answers share the maximum vote count.\"\"\"\n    if not vote_dist or len(vote_dist) < 2:\n        return False\n    counts = sorted(vote_dist.values(), reverse=True)\n    return counts[0] == counts[1]\n\n\ndef analyze_group(problems: list[dict], label: str) -> dict:\n    n = len(problems)\n    if n == 0:\n        return {\"label\": label, \"n\": 0}\n\n    sica_correct = [bool(p[\"sica_correct\"]) for p in problems]\n    sc_correct = [bool(p[\"sc_correct\"]) for p in problems]\n\n    # C0: multi-candidate rate (≥2 distinct answers in vote distribution)\n    c0_count = sum(1 for p in problems if len(p.get(\"sc_vote_distribution\", {})) >= 2)\n\n    # Tiebreak analysis\n    tie_indices = []\n    tie_sica_correct = []\n    tie_sc_correct = []\n    for i, p in enumerate(problems):\n        if is_sc_tie(p.get(\"sc_vote_distribution\", {})):\n            tie_indices.append(p.get(\"problem_idx\", i))\n            tie_sica_correct.append(bool(p[\"sica_correct\"]))\n            tie_sc_correct.append(bool(p[\"sc_correct\"]))\n\n    sica_acc = sum(sica_correct) / n\n    sc_acc = sum(sc_correct) / n\n    delta_pp = (sica_acc - sc_acc) * 100\n    pval = mcnemar_pvalue(sica_correct, sc_correct)\n\n    # Disagreement breakdown\n    sica_only = sum(a and not b for a, b in zip(sica_correct, sc_correct))\n    sc_only = sum(not a and b for a, b in zip(sica_correct, sc_correct))\n\n    result = {\n        \"label\": label,\n        \"n\": n,\n        \"c0_multi_candidate\": c0_count,\n        \"c0_rate\": c0_count / n,\n        \"sica_accuracy\": sica_acc,\n        \"sica_correct\": sum(sica_correct),\n        \"sc_accuracy\": sc_acc,\n        \"sc_correct\": sum(sc_correct),\n        \"delta_pp\": delta_pp,\n        \"mcnemar_p\": pval,\n        \"sica_only_correct\": sica_only,\n        \"sc_only_correct\": sc_only,\n        \"n_ties\": len(tie_indices),\n        \"tie_indices\": tie_indices,\n    }\n\n    if tie_indices:\n        result[\"tie_sica_correct\"] = sum(tie_sica_correct)\n        result[\"tie_sica_accuracy\"] = sum(tie_sica_correct) / len(tie_indices)\n        result[\"tie_sc_correct\"] = sum(tie_sc_correct)\n    else:\n        result[\"tie_sica_correct\"] = 0\n        result[\"tie_sica_accuracy\"] = None\n        result[\"tie_sc_correct\"] = 0\n\n    return result\n\n\ndef load_d012_tiebreak(d012_path: str) -> dict | None:\n    \"\"\"Load D012 pilot tiebreak stats for comparison.\"\"\"\n    if not d012_path or not os.path.exists(d012_path):\n        return None\n    with open(d012_path) as f:\n        data = json.load(f)\n\n    # Could be tiebreak_analysis.json or sica_d012_14b.json\n    if \"strategies\" in data:\n        # tiebreak_analysis.json format\n        return {\n            \"n_total\": data[\"n_total\"],\n            \"n_tie\": data[\"n_tie\"],\n            \"sica_tie_accuracy\": data[\"strategies\"][\"sica\"][\"accuracy\"],\n            \"sica_tie_correct\": data[\"strategies\"][\"sica\"][\"correct\"],\n        }\n    elif \"results\" in data:\n        # sica_d012_14b.json format — compute tiebreak from raw data\n        problems = data[\"results\"]\n        ties = [p for p in problems if is_sc_tie(p.get(\"sc_vote_distribution\", {}))]\n        if not ties:\n            return {\"n_total\": len(problems), \"n_tie\": 0, \"sica_tie_accuracy\": None, \"sica_tie_correct\": 0}\n        return {\n            \"n_total\": len(problems),\n            \"n_tie\": len(ties),\n            \"sica_tie_accuracy\": sum(p[\"sica_correct\"] for p in ties) / len(ties),\n            \"sica_tie_correct\": sum(p[\"sica_correct\"] for p in ties),\n        }\n    return None\n\n\n# ── Output formatting ────────────────────────────────────────────\n\ndef print_markdown(groups: list[dict], overall: dict, d012_tb: dict | None):\n    print(\"\\n## exp-001 Expanded Analysis (sica_expanded_14b)\\n\")\n\n    # Main table\n    header = \"| Dataset | N | C0% | SICA Acc | SC Acc | Δ (pp) | McNemar p |\"\n    sep    = \"|---------|---|-----|----------|--------|--------|-----------|\"\n    print(header)\n    print(sep)\n    for g in groups:\n        sig = \"*\" if g[\"mcnemar_p\"] < 0.05 else \"\"\n        print(f\"| {g['label']:15s} | {g['n']:3d} | {g['c0_rate']*100:5.1f} | \"\n              f\"{g['sica_accuracy']*100:6.2f}% | {g['sc_accuracy']*100:6.2f}% | \"\n              f\"{g['delta_pp']:+5.2f} | {g['mcnemar_p']:.4f}{sig} |\")\n    # Overall\n    sig = \"*\" if overall[\"mcnemar_p\"] < 0.05 else \"\"\n    print(f\"| {'**Overall**':15s} | {overall['n']:3d} | {overall['c0_rate']*100:5.1f} | \"\n          f\"{overall['sica_accuracy']*100:6.2f}% | {overall['sc_accuracy']*100:6.2f}% | \"\n          f\"{overall['delta_pp']:+5.2f} | {overall['mcnemar_p']:.4f}{sig} |\")\n\n    # Disagreement\n    print(f\"\\nDisagreements: SICA-only correct = {overall['sica_only_correct']}, \"\n          f\"SC-only correct = {overall['sc_only_correct']}\")\n\n    # Tiebreak table\n    print(\"\\n### Tiebreak Analysis\\n\")\n    print(\"| Dataset | SC Ties | SICA Win | SICA Tie-Acc |\")\n    print(\"|---------|---------|----------|--------------|\")\n    for g in groups:\n        if g[\"n_ties\"] > 0:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} | \"\n                  f\"{g['tie_sica_correct']:8d} | {g['tie_sica_accuracy']*100:10.1f}% |\")\n        else:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} |      n/a |          n/a |\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} | \"\n              f\"{overall['tie_sica_correct']:8d} | {overall['tie_sica_accuracy']*100:10.1f}% |\")\n    else:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} |      n/a |          n/a |\")\n\n    # D012 comparison\n    if d012_tb and d012_tb.get(\"n_tie\", 0) > 0 and overall[\"n_ties\"] > 0:\n        print(f\"\\nD012 pilot comparison (n={d012_tb['n_total']}):\")\n        print(f\"  D012 ties: {d012_tb['n_tie']}, \"\n              f\"SICA tie-acc: {d012_tb['sica_tie_accuracy']*100:.1f}%\")\n        print(f\"  Expanded ties: {overall['n_ties']}, \"\n              f\"SICA tie-acc: {overall['tie_sica_accuracy']*100:.1f}%\")\n        d012_rate = d012_tb[\"n_tie\"] / d012_tb[\"n_total\"] * 100\n        exp_rate = overall[\"n_ties\"] / overall[\"n\"] * 100\n        print(f\"  Tie rate: D012 {d012_rate:.1f}% → Expanded {exp_rate:.1f}%\")\n\n    # Key numbers\n    print(\"\\n### Key Numbers\\n\")\n    print(f\"- Total problems: {overall['n']}\")\n    print(f\"- SICA accuracy: {overall['sica_accuracy']*100:.2f}% ({overall['sica_correct']}/{overall['n']})\")\n    print(f\"- SC accuracy: {overall['sc_accuracy']*100:.2f}% ({overall['sc_correct']}/{overall['n']})\")\n    print(f\"- Delta: {overall['delta_pp']:+.2f} pp (McNemar p={overall['mcnemar_p']:.4f})\")\n    print(f\"- SC ties: {overall['n_ties']} ({overall['n_ties']/overall['n']*100:.1f}%)\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"- SICA tie-accuracy: {overall['tie_sica_accuracy']*100:.1f}% \"\n              f\"({overall['tie_sica_correct']}/{overall['n_ties']})\")\n\n\n# ── File discovery ───────────────────────────────────────────────\n\ndef find_results_file(path: str) -> str:\n    if os.path.isfile(path):\n        return path\n    if os.path.isdir(path):\n        candidate = os.path.join(path, \"sica_expanded_14b.json\")\n        if os.path.exists(candidate):\n            return candidate\n        jsons = [f for f in os.listdir(path) if f.endswith(\".json\") and \"expanded\" in f]\n        if len(jsons) == 1:\n            return os.path.join(path, jsons[0])\n        if jsons:\n            raise FileNotFoundError(\n                f\"Multiple expanded JSON files in {path}: {jsons}. Specify exact path.\")\n    raise FileNotFoundError(f\"Cannot find results file at {path}\")\n\n\n# ── Main ─────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Analyze exp-001 (sica_expanded_14b) results: per-dataset accuracy, \"\n                    \"tiebreak stats, McNemar significance tests.\",\n    )\n    parser.add_argument(\n        \"--results-dir\", default=\"results/sica_expanded_14b.json\",\n        help=\"Path to results JSON file or directory (default: results/sica_expanded_14b.json)\",\n    )\n    parser.add_argument(\n        \"--output\", default=None,\n        help=\"Output JSON path (default: &lt;results-dir>/analysis.json or alongside input file)\",\n    )\n    parser.add_argument(\n        \"--d012\", default=None,\n        help=\"Path to D012 pilot data for tiebreak comparison \"\n             \"(tries results/tiebreak_analysis.json and results/sica_d012_14b.json if not set)\",\n    )\n    args = parser.parse_args()\n\n    # Find and load results\n    results_path = find_results_file(args.results_dir)\n    with open(results_path) as f:\n        data = json.load(f)\n    problems = data[\"results\"]\n    n = len(problems)\n    print(f\"Loaded {n} problems from {results_path}\")\n\n    # Group by dataset\n    by_dataset: dict[str, list[dict]] = defaultdict(list)\n    for p in problems:\n        ds = p.get(\"dataset\", \"unknown\")\n        by_dataset[ds].append(p)\n\n    # Per-dataset analysis\n    dataset_order = [\"proofwriter\", \"folio\"]\n    groups = []\n    for ds in dataset_order:\n        if ds in by_dataset:\n            groups.append(analyze_group(by_dataset[ds], ds))\n    for ds in sorted(by_dataset.keys()):\n        if ds not in dataset_order:\n            groups.append(analyze_group(by_dataset[ds], ds))\n\n    overall = analyze_group(problems, \"overall\")\n\n    # D012 tiebreak comparison\n    d012_tb = None\n    if args.d012:\n        d012_tb = load_d012_tiebreak(args.d012)\n    else:\n        results_dir = os.path.dirname(results_path)\n        for candidate in [\"tiebreak_analysis.json\", \"sica_d012_14b.json\"]:\n            cpath = os.path.join(results_dir, candidate)\n            if os.path.exists(cpath):\n                d012_tb = load_d012_tiebreak(cpath)\n                if d012_tb:\n                    break\n\n    # Print markdown\n    print_markdown(groups, overall, d012_tb)\n\n    # Save JSON\n    output_path = args.output\n    if output_path is None:\n        base = os.path.dirname(results_path)\n        output_path = os.path.join(base or \".\", \"sica_expanded_14b\", \"analysis.json\")\n        # If input was a flat file in results/, save alongside it\n        if not os.path.isdir(os.path.join(base, \"sica_expanded_14b\")):\n            output_path = os.path.join(base or \".\", \"analysis_expanded.json\")\n\n    json_out = {\n        \"experiment\": \"exp-001_sica_expanded_14b\",\n        \"source_file\": results_path,\n        \"n_problems\": n,\n        \"per_dataset\": {g[\"label\"]: g for g in groups},\n        \"overall\": overall,\n        \"d012_tiebreak_comparison\": d012_tb,\n    }\n\n    # Clean non-serializable and verbose fields\n    for section in list(json_out[\"per_dataset\"].values()) + [json_out[\"overall\"]]:\n        section.pop(\"tie_indices\", None)\n\n    os.makedirs(os.path.dirname(output_path) or \".\", exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(json_out, f, indent=2)\n    print(f\"\\nDetailed results saved to {output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/analyze_expanded.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nexp-001 expanded analysis: per-dataset accuracy, tiebreak stats, McNemar tests.\n\nInput:  results/sica_expanded_14b.json (single JSON with summary + results array)\nOutput: markdown summary table (stdout) + analysis.json\n\nDependencies: Python 3.8+ (no external packages required; scipy optional for chi2 McNemar)\n\nUsage:\n  python scripts/analyze_expanded.py\n  python scripts/analyze_expanded.py --results-dir results/sica_expanded_14b.json\n  python scripts/analyze_expanded.py --results-dir results/ --output results/analysis.json\n  python scripts/analyze_expanded.py --d012 results/sica_d012_14b.json\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nfrom collections import Counter, defaultdict\n\n\n# ── Answer normalization ─────────────────────────────────────────\n\ndef _normalize_logic(ans: str) -> str:\n    s = str(ans).strip().lower()\n    mapping = {\n        \"true\": \"True\", \"t\": \"True\", \"yes\": \"True\",\n        \"false\": \"False\", \"f\": \"False\", \"no\": \"False\",\n        \"unknown\": \"Unknown\", \"u\": \"Unknown\", \"uncertain\": \"Unknown\",\n    }\n    return mapping.get(s, str(ans).strip())\n\n\n# ── McNemar's test (exact binomial, no scipy needed) ─────────────\n\ndef mcnemar_pvalue(a_correct: list[bool], b_correct: list[bool]) -> float:\n    \"\"\"Two-sided McNemar's test using exact binomial distribution.\"\"\"\n    n10 = sum(a and not b for a, b in zip(a_correct, b_correct))\n    n01 = sum(not a and b for a, b in zip(a_correct, b_correct))\n    n = n10 + n01\n    if n == 0:\n        return 1.0\n    k = min(n10, n01)\n    p = sum(math.comb(n, i) * 0.5 ** n for i in range(k + 1))\n    return min(2.0 * p, 1.0)\n\n\n# ── Core analysis ────────────────────────────────────────────────\n\ndef is_sc_tie(vote_dist: dict) -> bool:\n    \"\"\"SC tie: ≥2 answers share the maximum vote count.\"\"\"\n    if not vote_dist or len(vote_dist) < 2:\n        return False\n    counts = sorted(vote_dist.values(), reverse=True)\n    return counts[0] == counts[1]\n\n\ndef analyze_group(problems: list[dict], label: str) -> dict:\n    n = len(problems)\n    if n == 0:\n        return {\"label\": label, \"n\": 0}\n\n    sica_correct = [bool(p[\"sica_correct\"]) for p in problems]\n    sc_correct = [bool(p[\"sc_correct\"]) for p in problems]\n\n    # C0: multi-candidate rate (≥2 distinct answers in vote distribution)\n    c0_count = sum(1 for p in problems if len(p.get(\"sc_vote_distribution\", {})) >= 2)\n\n    # Tiebreak analysis\n    tie_indices = []\n    tie_sica_correct = []\n    tie_sc_correct = []\n    for i, p in enumerate(problems):\n        if is_sc_tie(p.get(\"sc_vote_distribution\", {})):\n            tie_indices.append(p.get(\"problem_idx\", i))\n            tie_sica_correct.append(bool(p[\"sica_correct\"]))\n            tie_sc_correct.append(bool(p[\"sc_correct\"]))\n\n    sica_acc = sum(sica_correct) / n\n    sc_acc = sum(sc_correct) / n\n    delta_pp = (sica_acc - sc_acc) * 100\n    pval = mcnemar_pvalue(sica_correct, sc_correct)\n\n    # Disagreement breakdown\n    sica_only = sum(a and not b for a, b in zip(sica_correct, sc_correct))\n    sc_only = sum(not a and b for a, b in zip(sica_correct, sc_correct))\n\n    result = {\n        \"label\": label,\n        \"n\": n,\n        \"c0_multi_candidate\": c0_count,\n        \"c0_rate\": c0_count / n,\n        \"sica_accuracy\": sica_acc,\n        \"sica_correct\": sum(sica_correct),\n        \"sc_accuracy\": sc_acc,\n        \"sc_correct\": sum(sc_correct),\n        \"delta_pp\": delta_pp,\n        \"mcnemar_p\": pval,\n        \"sica_only_correct\": sica_only,\n        \"sc_only_correct\": sc_only,\n        \"n_ties\": len(tie_indices),\n        \"tie_indices\": tie_indices,\n    }\n\n    if tie_indices:\n        result[\"tie_sica_correct\"] = sum(tie_sica_correct)\n        result[\"tie_sica_accuracy\"] = sum(tie_sica_correct) / len(tie_indices)\n        result[\"tie_sc_correct\"] = sum(tie_sc_correct)\n    else:\n        result[\"tie_sica_correct\"] = 0\n        result[\"tie_sica_accuracy\"] = None\n        result[\"tie_sc_correct\"] = 0\n\n    return result\n\n\ndef load_d012_tiebreak(d012_path: str) -> dict | None:\n    \"\"\"Load D012 pilot tiebreak stats for comparison.\"\"\"\n    if not d012_path or not os.path.exists(d012_path):\n        return None\n    with open(d012_path) as f:\n        data = json.load(f)\n\n    # Could be tiebreak_analysis.json or sica_d012_14b.json\n    if \"strategies\" in data:\n        # tiebreak_analysis.json format\n        return {\n            \"n_total\": data[\"n_total\"],\n            \"n_tie\": data[\"n_tie\"],\n            \"sica_tie_accuracy\": data[\"strategies\"][\"sica\"][\"accuracy\"],\n            \"sica_tie_correct\": data[\"strategies\"][\"sica\"][\"correct\"],\n        }\n    elif \"results\" in data:\n        # sica_d012_14b.json format — compute tiebreak from raw data\n        problems = data[\"results\"]\n        ties = [p for p in problems if is_sc_tie(p.get(\"sc_vote_distribution\", {}))]\n        if not ties:\n            return {\"n_total\": len(problems), \"n_tie\": 0, \"sica_tie_accuracy\": None, \"sica_tie_correct\": 0}\n        return {\n            \"n_total\": len(problems),\n            \"n_tie\": len(ties),\n            \"sica_tie_accuracy\": sum(p[\"sica_correct\"] for p in ties) / len(ties),\n            \"sica_tie_correct\": sum(p[\"sica_correct\"] for p in ties),\n        }\n    return None\n\n\n# ── Output formatting ────────────────────────────────────────────\n\ndef print_markdown(groups: list[dict], overall: dict, d012_tb: dict | None):\n    print(\"\\n## exp-001 Expanded Analysis (sica_expanded_14b)\\n\")\n\n    # Main table\n    header = \"| Dataset | N | C0% | SICA Acc | SC Acc | Δ (pp) | McNemar p |\"\n    sep    = \"|---------|---|-----|----------|--------|--------|-----------|\"\n    print(header)\n    print(sep)\n    for g in groups:\n        sig = \"*\" if g[\"mcnemar_p\"] < 0.05 else \"\"\n        print(f\"| {g['label']:15s} | {g['n']:3d} | {g['c0_rate']*100:5.1f} | \"\n              f\"{g['sica_accuracy']*100:6.2f}% | {g['sc_accuracy']*100:6.2f}% | \"\n              f\"{g['delta_pp']:+5.2f} | {g['mcnemar_p']:.4f}{sig} |\")\n    # Overall\n    sig = \"*\" if overall[\"mcnemar_p\"] < 0.05 else \"\"\n    print(f\"| {'**Overall**':15s} | {overall['n']:3d} | {overall['c0_rate']*100:5.1f} | \"\n          f\"{overall['sica_accuracy']*100:6.2f}% | {overall['sc_accuracy']*100:6.2f}% | \"\n          f\"{overall['delta_pp']:+5.2f} | {overall['mcnemar_p']:.4f}{sig} |\")\n\n    # Disagreement\n    print(f\"\\nDisagreements: SICA-only correct = {overall['sica_only_correct']}, \"\n          f\"SC-only correct = {overall['sc_only_correct']}\")\n\n    # Tiebreak table\n    print(\"\\n### Tiebreak Analysis\\n\")\n    print(\"| Dataset | SC Ties | SICA Win | SICA Tie-Acc |\")\n    print(\"|---------|---------|----------|--------------|\")\n    for g in groups:\n        if g[\"n_ties\"] > 0:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} | \"\n                  f\"{g['tie_sica_correct']:8d} | {g['tie_sica_accuracy']*100:10.1f}% |\")\n        else:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} |      n/a |          n/a |\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} | \"\n              f\"{overall['tie_sica_correct']:8d} | {overall['tie_sica_accuracy']*100:10.1f}% |\")\n    else:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} |      n/a |          n/a |\")\n\n    # D012 comparison\n    if d012_tb and d012_tb.get(\"n_tie\", 0) > 0 and overall[\"n_ties\"] > 0:\n        print(f\"\\nD012 pilot comparison (n={d012_tb['n_total']}):\")\n        print(f\"  D012 ties: {d012_tb['n_tie']}, \"\n              f\"SICA tie-acc: {d012_tb['sica_tie_accuracy']*100:.1f}%\")\n        print(f\"  Expanded ties: {overall['n_ties']}, \"\n              f\"SICA tie-acc: {overall['tie_sica_accuracy']*100:.1f}%\")\n        d012_rate = d012_tb[\"n_tie\"] / d012_tb[\"n_total\"] * 100\n        exp_rate = overall[\"n_ties\"] / overall[\"n\"] * 100\n        print(f\"  Tie rate: D012 {d012_rate:.1f}% → Expanded {exp_rate:.1f}%\")\n\n    # Key numbers\n    print(\"\\n### Key Numbers\\n\")\n    print(f\"- Total problems: {overall['n']}\")\n    print(f\"- SICA accuracy: {overall['sica_accuracy']*100:.2f}% ({overall['sica_correct']}/{overall['n']})\")\n    print(f\"- SC accuracy: {overall['sc_accuracy']*100:.2f}% ({overall['sc_correct']}/{overall['n']})\")\n    print(f\"- Delta: {overall['delta_pp']:+.2f} pp (McNemar p={overall['mcnemar_p']:.4f})\")\n    print(f\"- SC ties: {overall['n_ties']} ({overall['n_ties']/overall['n']*100:.1f}%)\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"- SICA tie-accuracy: {overall['tie_sica_accuracy']*100:.1f}% \"\n              f\"({overall['tie_sica_correct']}/{overall['n_ties']})\")\n\n\n# ── File discovery ───────────────────────────────────────────────\n\ndef find_results_file(path: str) -> str:\n    if os.path.isfile(path):\n        return path\n    if os.path.isdir(path):\n        candidate = os.path.join(path, \"sica_expanded_14b.json\")\n        if os.path.exists(candidate):\n            return candidate\n        jsons = [f for f in os.listdir(path) if f.endswith(\".json\") and \"expanded\" in f]\n        if len(jsons) == 1:\n            return os.path.join(path, jsons[0])\n        if jsons:\n            raise FileNotFoundError(\n                f\"Multiple expanded JSON files in {path}: {jsons}. Specify exact path.\")\n    raise FileNotFoundError(f\"Cannot find results file at {path}\")\n\n\n# ── Main ─────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Analyze exp-001 (sica_expanded_14b) results: per-dataset accuracy, \"\n                    \"tiebreak stats, McNemar significance tests.\",\n    )\n    parser.add_argument(\n        \"--results-dir\", default=\"results/sica_expanded_14b.json\",\n        help=\"Path to results JSON file or directory (default: results/sica_expanded_14b.json)\",\n    )\n    parser.add_argument(\n        \"--output\", default=None,\n        help=\"Output JSON path (default: &lt;results-dir>/analysis.json or alongside input file)\",\n    )\n    parser.add_argument(\n        \"--d012\", default=None,\n        help=\"Path to D012 pilot data for tiebreak comparison \"\n             \"(tries results/tiebreak_analysis.json and results/sica_d012_14b.json if not set)\",\n    )\n    args = parser.parse_args()\n\n    # Find and load results\n    results_path = find_results_file(args.results_dir)\n    with open(results_path) as f:\n        data = json.load(f)\n    problems = data[\"results\"]\n    n = len(problems)\n    print(f\"Loaded {n} problems from {results_path}\")\n\n    # Group by dataset\n    by_dataset: dict[str, list[dict]] = defaultdict(list)\n    for p in problems:\n        ds = p.get(\"dataset\", \"unknown\")\n        by_dataset[ds].append(p)\n\n    # Per-dataset analysis\n    dataset_order = [\"proofwriter\", \"folio\"]\n    groups = []\n    for ds in dataset_order:\n        if ds in by_dataset:\n            groups.append(analyze_group(by_dataset[ds], ds))\n    for ds in sorted(by_dataset.keys()):\n        if ds not in dataset_order:\n            groups.append(analyze_group(by_dataset[ds], ds))\n\n    overall = analyze_group(problems, \"overall\")\n\n    # D012 tiebreak comparison\n    d012_tb = None\n    if args.d012:\n        d012_tb = load_d012_tiebreak(args.d012)\n    else:\n        results_dir = os.path.dirname(results_path)\n        for candidate in [\"tiebreak_analysis.json\", \"sica_d012_14b.json\"]:\n            cpath = os.path.join(results_dir, candidate)\n            if os.path.exists(cpath):\n                d012_tb = load_d012_tiebreak(cpath)\n                if d012_tb:\n                    break\n\n    # Print markdown\n    print_markdown(groups, overall, d012_tb)\n\n    # Save JSON\n    output_path = args.output\n    if output_path is None:\n        base = os.path.dirname(results_path)\n        output_path = os.path.join(base or \".\", \"sica_expanded_14b\", \"analysis.json\")\n        # If input was a flat file in results/, save alongside it\n        if not os.path.isdir(os.path.join(base, \"sica_expanded_14b\")):\n            output_path = os.path.join(base or \".\", \"analysis_expanded.json\")\n\n    json_out = {\n        \"experiment\": \"exp-001_sica_expanded_14b\",\n        \"source_file\": results_path,\n        \"n_problems\": n,\n        \"per_dataset\": {g[\"label\"]: g for g in groups},\n        \"overall\": overall,\n        \"d012_tiebreak_comparison\": d012_tb,\n    }\n\n    # Clean non-serializable and verbose fields\n    for section in list(json_out[\"per_dataset\"].values()) + [json_out[\"overall\"]]:\n        section.pop(\"tie_indices\", None)\n\n    os.makedirs(os.path.dirname(output_path) or \".\", exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(json_out, f, indent=2)\n    print(f\"\\nDetailed results saved to {output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T08:04:40.336709+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/analyze_expanded.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T08:04:40.336925+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cat > /root/symb_invariant_consensus/scripts/analyze_expanded.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"\nexp-001 expanded analysis: per-dataset accuracy, tiebreak stats, McNemar tests.\n\nInput:  results/sica_expanded_14b.json (single JSON with summary + results array)\nOutput: markdown summary table (stdout) + analysis.json\n\nDependencies: Python 3.8+ (no external packages required; scipy optional for chi2 McNemar)\n\nUsage:\n  python scripts/analyze_expanded.py\n  python scripts/analyze_expanded.py --results-dir results/sica_expanded_14b.json\n  python scripts/analyze_expanded.py --results-dir results/ --output results/analysis.json\n  python scripts/analyze_expanded.py --d012 results/sica_d012_14b.json\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nfrom collections import Counter, defaultdict\n\n\n# ── Answer normalization ─────────────────────────────────────────\n\ndef _normalize_logic(ans: str) -> str:\n    s = str(ans).strip().lower()\n    mapping = {\n        \"true\": \"True\", \"t\": \"True\", \"yes\": \"True\",\n        \"false\": \"False\", \"f\": \"False\", \"no\": \"False\",\n        \"unknown\": \"Unknown\", \"u\": \"Unknown\", \"uncertain\": \"Unknown\",\n    }\n    return mapping.get(s, str(ans).strip())\n\n\n# ── McNemar's test (exact binomial, no scipy needed) ─────────────\n\ndef mcnemar_pvalue(a_correct: list[bool], b_correct: list[bool]) -> float:\n    \"\"\"Two-sided McNemar's test using exact binomial distribution.\"\"\"\n    n10 = sum(a and not b for a, b in zip(a_correct, b_correct))\n    n01 = sum(not a and b for a, b in zip(a_correct, b_correct))\n    n = n10 + n01\n    if n == 0:\n        return 1.0\n    k = min(n10, n01)\n    p = sum(math.comb(n, i) * 0.5 ** n for i in range(k + 1))\n    return min(2.0 * p, 1.0)\n\n\n# ── Core analysis ────────────────────────────────────────────────\n\ndef is_sc_tie(vote_dist: dict) -> bool:\n    \"\"\"SC tie: >=2 answers share the maximum vote count.\"\"\"\n    if not vote_dist or len(vote_dist) < 2:\n        return False\n    counts = sorted(vote_dist.values(), reverse=True)\n    return counts[0] == counts[1]\n\n\ndef analyze_group(problems: list[dict], label: str) -> dict:\n    n = len(problems)\n    if n == 0:\n        return {\"label\": label, \"n\": 0}\n\n    sica_correct = [bool(p[\"sica_correct\"]) for p in problems]\n    sc_correct = [bool(p[\"sc_correct\"]) for p in problems]\n\n    # C0: multi-candidate rate (>=2 distinct answers in vote distribution)\n    c0_count = sum(1 for p in problems if len(p.get(\"sc_vote_distribution\", {})) >= 2)\n\n    # Tiebreak analysis\n    tie_indices = []\n    tie_sica_correct = []\n    tie_sc_correct = []\n    for i, p in enumerate(problems):\n        if is_sc_tie(p.get(\"sc_vote_distribution\", {})):\n            tie_indices.append(p.get(\"problem_idx\", i))\n            tie_sica_correct.append(bool(p[\"sica_correct\"]))\n            tie_sc_correct.append(bool(p[\"sc_correct\"]))\n\n    sica_acc = sum(sica_correct) / n\n    sc_acc = sum(sc_correct) / n\n    delta_pp = (sica_acc - sc_acc) * 100\n    pval = mcnemar_pvalue(sica_correct, sc_correct)\n\n    # Disagreement breakdown\n    sica_only = sum(a and not b for a, b in zip(sica_correct, sc_correct))\n    sc_only = sum(not a and b for a, b in zip(sica_correct, sc_correct))\n\n    result = {\n        \"label\": label,\n        \"n\": n,\n        \"c0_multi_candidate\": c0_count,\n        \"c0_rate\": c0_count / n,\n        \"sica_accuracy\": sica_acc,\n        \"sica_correct\": sum(sica_correct),\n        \"sc_accuracy\": sc_acc,\n        \"sc_correct\": sum(sc_correct),\n        \"delta_pp\": delta_pp,\n        \"mcnemar_p\": pval,\n        \"sica_only_correct\": sica_only,\n        \"sc_only_correct\": sc_only,\n        \"n_ties\": len(tie_indices),\n        \"tie_indices\": tie_indices,\n    }\n\n    if tie_indices:\n        result[\"tie_sica_correct\"] = sum(tie_sica_correct)\n        result[\"tie_sica_accuracy\"] = sum(tie_sica_correct) / len(tie_indices)\n        result[\"tie_sc_correct\"] = sum(tie_sc_correct)\n    else:\n        result[\"tie_sica_correct\"] = 0\n        result[\"tie_sica_accuracy\"] = None\n        result[\"tie_sc_correct\"] = 0\n\n    return result\n\n\ndef load_d012_tiebreak(d012_path: str) -> dict | None:\n    \"\"\"Load D012 pilot tiebreak stats for comparison.\"\"\"\n    if not d012_path or not os.path.exists(d012_path):\n        return None\n    with open(d012_path) as f:\n        data = json.load(f)\n\n    # Could be tiebreak_analysis.json or sica_d012_14b.json\n    if \"strategies\" in data:\n        return {\n            \"n_total\": data[\"n_total\"],\n            \"n_tie\": data[\"n_tie\"],\n            \"sica_tie_accuracy\": data[\"strategies\"][\"sica\"][\"accuracy\"],\n            \"sica_tie_correct\": data[\"strategies\"][\"sica\"][\"correct\"],\n        }\n    elif \"results\" in data:\n        problems = data[\"results\"]\n        ties = [p for p in problems if is_sc_tie(p.get(\"sc_vote_distribution\", {}))]\n        if not ties:\n            return {\"n_total\": len(problems), \"n_tie\": 0, \"sica_tie_accuracy\": None, \"sica_tie_correct\": 0}\n        return {\n            \"n_total\": len(problems),\n            \"n_tie\": len(ties),\n            \"sica_tie_accuracy\": sum(p[\"sica_correct\"] for p in ties) / len(ties),\n            \"sica_tie_correct\": sum(p[\"sica_correct\"] for p in ties),\n        }\n    return None\n\n\n# ── Output formatting ────────────────────────────────────────────\n\ndef print_markdown(groups: list[dict], overall: dict, d012_tb: dict | None):\n    print(\"\\n## exp-001 Expanded Analysis (sica_expanded_14b)\\n\")\n\n    # Main table\n    header = \"| Dataset         |   N | C0%   | SICA Acc | SC Acc  | D (pp) | McNemar p |\"\n    sep    = \"|-----------------|-----|-------|----------|---------|--------|-----------|\"\n    print(header)\n    print(sep)\n    for g in groups:\n        sig = \"*\" if g[\"mcnemar_p\"] < 0.05 else \"\"\n        print(f\"| {g['label']:15s} | {g['n']:3d} | {g['c0_rate']*100:5.1f} | \"\n              f\"{g['sica_accuracy']*100:6.2f}% | {g['sc_accuracy']*100:6.2f}% | \"\n              f\"{g['delta_pp']:+5.2f} | {g['mcnemar_p']:.4f}{sig} |\")\n    sig = \"*\" if overall[\"mcnemar_p\"] < 0.05 else \"\"\n    print(f\"| {'**Overall**':15s} | {overall['n']:3d} | {overall['c0_rate']*100:5.1f} | \"\n          f\"{overall['sica_accuracy']*100:6.2f}% | {overall['sc_accuracy']*100:6.2f}% | \"\n          f\"{overall['delta_pp']:+5.2f} | {overall['mcnemar_p']:.4f}{sig} |\")\n\n    # Disagreement\n    print(f\"\\nDisagreements: SICA-only correct = {overall['sica_only_correct']}, \"\n          f\"SC-only correct = {overall['sc_only_correct']}\")\n\n    # Tiebreak table\n    print(\"\\n### Tiebreak Analysis\\n\")\n    print(\"| Dataset         | SC Ties | SICA Win | SICA Tie-Acc |\")\n    print(\"|-----------------|---------|----------|--------------|\")\n    for g in groups:\n        if g[\"n_ties\"] > 0:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} | \"\n                  f\"{g['tie_sica_correct']:8d} | {g['tie_sica_accuracy']*100:10.1f}% |\")\n        else:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} |      n/a |          n/a |\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} | \"\n              f\"{overall['tie_sica_correct']:8d} | {overall['tie_sica_accuracy']*100:10.1f}% |\")\n    else:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} |      n/a |          n/a |\")\n\n    # D012 comparison\n    if d012_tb and d012_tb.get(\"n_tie\", 0) > 0 and overall[\"n_ties\"] > 0:\n        print(f\"\\nD012 pilot comparison (n={d012_tb['n_total']}):\")\n        print(f\"  D012 ties: {d012_tb['n_tie']}, \"\n              f\"SICA tie-acc: {d012_tb['sica_tie_accuracy']*100:.1f}%\")\n        print(f\"  Expanded ties: {overall['n_ties']}, \"\n              f\"SICA tie-acc: {overall['tie_sica_accuracy']*100:.1f}%\")\n        d012_rate = d012_tb[\"n_tie\"] / d012_tb[\"n_total\"] * 100\n        exp_rate = overall[\"n_ties\"] / overall[\"n\"] * 100\n        print(f\"  Tie rate: D012 {d012_rate:.1f}% -> Expanded {exp_rate:.1f}%\")\n\n    # Key numbers\n    print(\"\\n### Key Numbers\\n\")\n    print(f\"- Total problems: {overall['n']}\")\n    print(f\"- SICA accuracy: {overall['sica_accuracy']*100:.2f}% ({overall['sica_correct']}/{overall['n']})\")\n    print(f\"- SC accuracy: {overall['sc_accuracy']*100:.2f}% ({overall['sc_correct']}/{overall['n']})\")\n    print(f\"- Delta: {overall['delta_pp']:+.2f} pp (McNemar p={overall['mcnemar_p']:.4f})\")\n    print(f\"- SC ties: {overall['n_ties']} ({overall['n_ties']/overall['n']*100:.1f}%)\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"- SICA tie-accuracy: {overall['tie_sica_accuracy']*100:.1f}% \"\n              f\"({overall['tie_sica_correct']}/{overall['n_ties']})\")\n\n\n# ── File discovery ───────────────────────────────────────────────\n\ndef find_results_file(path: str) -> str:\n    if os.path.isfile(path):\n        return path\n    if os.path.isdir(path):\n        candidate = os.path.join(path, \"sica_expanded_14b.json\")\n        if os.path.exists(candidate):\n            return candidate\n        jsons = [f for f in os.listdir(path) if f.endswith(\".json\") and \"expanded\" in f]\n        if len(jsons) == 1:\n            return os.path.join(path, jsons[0])\n        if jsons:\n            raise FileNotFoundError(\n                f\"Multiple expanded JSON files in {path}: {jsons}. Specify exact path.\")\n    raise FileNotFoundError(f\"Cannot find results file at {path}\")\n\n\n# ── Main ─────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Analyze exp-001 (sica_expanded_14b) results: per-dataset accuracy, \"\n                    \"tiebreak stats, McNemar significance tests.\",\n    )\n    parser.add_argument(\n        \"--results-dir\", default=\"results/sica_expanded_14b.json\",\n        help=\"Path to results JSON file or directory (default: results/sica_expanded_14b.json)\",\n    )\n    parser.add_argument(\n        \"--output\", default=None,\n        help=\"Output JSON path (default: alongside input file as analysis_expanded.json)\",\n    )\n    parser.add_argument(\n        \"--d012\", default=None,\n        help=\"Path to D012 pilot data for tiebreak comparison \"\n             \"(auto-detects tiebreak_analysis.json or sica_d012_14b.json if not set)\",\n    )\n    args = parser.parse_args()\n\n    # Find and load results\n    results_path = find_results_file(args.results_dir)\n    with open(results_path) as f:\n        data = json.load(f)\n    problems = data[\"results\"]\n    n = len(problems)\n    print(f\"Loaded {n} problems from {results_path}\")\n\n    # Group by dataset\n    by_dataset: dict[str, list[dict]] = defaultdict(list)\n    for p in problems:\n        ds = p.get(\"dataset\", \"unknown\")\n        by_dataset[ds].append(p)\n\n    # Per-dataset analysis\n    dataset_order = [\"proofwriter\", \"folio\"]\n    groups = []\n    for ds in dataset_order:\n        if ds in by_dataset:\n            groups.append(analyze_group(by_dataset[ds], ds))\n    for ds in sorted(by_dataset.keys()):\n        if ds not in dataset_order:\n            groups.append(analyze_group(by_dataset[ds], ds))\n\n    overall = analyze_group(problems, \"overall\")\n\n    # D012 tiebreak comparison\n    d012_tb = None\n    if args.d012:\n        d012_tb = load_d012_tiebreak(args.d012)\n    else:\n        results_dir = os.path.dirname(results_path)\n        for candidate in [\"tiebreak_analysis.json\", \"sica_d012_14b.json\"]:\n            cpath = os.path.join(results_dir, candidate)\n            if os.path.exists(cpath):\n                d012_tb = load_d012_tiebreak(cpath)\n                if d012_tb:\n                    break\n\n    # Print markdown\n    print_markdown(groups, overall, d012_tb)\n\n    # Save JSON\n    output_path = args.output\n    if output_path is None:\n        base = os.path.dirname(results_path)\n        output_path = os.path.join(base or \".\", \"sica_expanded_14b\", \"analysis.json\")\n        if not os.path.isdir(os.path.join(base, \"sica_expanded_14b\")):\n            output_path = os.path.join(base or \".\", \"analysis_expanded.json\")\n\n    json_out = {\n        \"experiment\": \"exp-001_sica_expanded_14b\",\n        \"source_file\": results_path,\n        \"n_problems\": n,\n        \"per_dataset\": {g[\"label\"]: g for g in groups},\n        \"overall\": overall,\n        \"d012_tiebreak_comparison\": d012_tb,\n    }\n\n    for section in list(json_out[\"per_dataset\"].values()) + [json_out[\"overall\"]]:\n        section.pop(\"tie_indices\", None)\n\n    os.makedirs(os.path.dirname(output_path) or \".\", exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(json_out, f, indent=2)\n    print(f\"\\nDetailed results saved to {output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat > /root/symb_invariant_consensus/scripts/analyze_expanded.py << 'SCRIPT_EOF'\n#!/usr/bin/env python3\n\"\"\"\nexp-001 expanded analysis: per-dataset accuracy, tiebreak stats, McNemar tests.\n\nInput:  results/sica_expanded_14b.json (single JSON with summary + results array)\nOutput: markdown summary table (stdout) + analysis.json\n\nDependencies: Python 3.8+ (no external packages required; scipy optional for chi2 McNemar)\n\nUsage:\n  python scripts/analyze_expanded.py\n  python scripts/analyze_expanded.py --results-dir results/sica_expanded_14b.json\n  python scripts/analyze_expanded.py --results-dir results/ --output results/analysis.json\n  python scripts/analyze_expanded.py --d012 results/sica_d012_14b.json\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport math\nimport os\nimport sys\nfrom collections import Counter, defaultdict\n\n\n# ── Answer normalization ─────────────────────────────────────────\n\ndef _normalize_logic(ans: str) -> str:\n    s = str(ans).strip().lower()\n    mapping = {\n        \"true\": \"True\", \"t\": \"True\", \"yes\": \"True\",\n        \"false\": \"False\", \"f\": \"False\", \"no\": \"False\",\n        \"unknown\": \"Unknown\", \"u\": \"Unknown\", \"uncertain\": \"Unknown\",\n    }\n    return mapping.get(s, str(ans).strip())\n\n\n# ── McNemar's test (exact binomial, no scipy needed) ─────────────\n\ndef mcnemar_pvalue(a_correct: list[bool], b_correct: list[bool]) -> float:\n    \"\"\"Two-sided McNemar's test using exact binomial distribution.\"\"\"\n    n10 = sum(a and not b for a, b in zip(a_correct, b_correct))\n    n01 = sum(not a and b for a, b in zip(a_correct, b_correct))\n    n = n10 + n01\n    if n == 0:\n        return 1.0\n    k = min(n10, n01)\n    p = sum(math.comb(n, i) * 0.5 ** n for i in range(k + 1))\n    return min(2.0 * p, 1.0)\n\n\n# ── Core analysis ────────────────────────────────────────────────\n\ndef is_sc_tie(vote_dist: dict) -> bool:\n    \"\"\"SC tie: >=2 answers share the maximum vote count.\"\"\"\n    if not vote_dist or len(vote_dist) < 2:\n        return False\n    counts = sorted(vote_dist.values(), reverse=True)\n    return counts[0] == counts[1]\n\n\ndef analyze_group(problems: list[dict], label: str) -> dict:\n    n = len(problems)\n    if n == 0:\n        return {\"label\": label, \"n\": 0}\n\n    sica_correct = [bool(p[\"sica_correct\"]) for p in problems]\n    sc_correct = [bool(p[\"sc_correct\"]) for p in problems]\n\n    # C0: multi-candidate rate (>=2 distinct answers in vote distribution)\n    c0_count = sum(1 for p in problems if len(p.get(\"sc_vote_distribution\", {})) >= 2)\n\n    # Tiebreak analysis\n    tie_indices = []\n    tie_sica_correct = []\n    tie_sc_correct = []\n    for i, p in enumerate(problems):\n        if is_sc_tie(p.get(\"sc_vote_distribution\", {})):\n            tie_indices.append(p.get(\"problem_idx\", i))\n            tie_sica_correct.append(bool(p[\"sica_correct\"]))\n            tie_sc_correct.append(bool(p[\"sc_correct\"]))\n\n    sica_acc = sum(sica_correct) / n\n    sc_acc = sum(sc_correct) / n\n    delta_pp = (sica_acc - sc_acc) * 100\n    pval = mcnemar_pvalue(sica_correct, sc_correct)\n\n    # Disagreement breakdown\n    sica_only = sum(a and not b for a, b in zip(sica_correct, sc_correct))\n    sc_only = sum(not a and b for a, b in zip(sica_correct, sc_correct))\n\n    result = {\n        \"label\": label,\n        \"n\": n,\n        \"c0_multi_candidate\": c0_count,\n        \"c0_rate\": c0_count / n,\n        \"sica_accuracy\": sica_acc,\n        \"sica_correct\": sum(sica_correct),\n        \"sc_accuracy\": sc_acc,\n        \"sc_correct\": sum(sc_correct),\n        \"delta_pp\": delta_pp,\n        \"mcnemar_p\": pval,\n        \"sica_only_correct\": sica_only,\n        \"sc_only_correct\": sc_only,\n        \"n_ties\": len(tie_indices),\n        \"tie_indices\": tie_indices,\n    }\n\n    if tie_indices:\n        result[\"tie_sica_correct\"] = sum(tie_sica_correct)\n        result[\"tie_sica_accuracy\"] = sum(tie_sica_correct) / len(tie_indices)\n        result[\"tie_sc_correct\"] = sum(tie_sc_correct)\n    else:\n        result[\"tie_sica_correct\"] = 0\n        result[\"tie_sica_accuracy\"] = None\n        result[\"tie_sc_correct\"] = 0\n\n    return result\n\n\ndef load_d012_tiebreak(d012_path: str) -> dict | None:\n    \"\"\"Load D012 pilot tiebreak stats for comparison.\"\"\"\n    if not d012_path or not os.path.exists(d012_path):\n        return None\n    with open(d012_path) as f:\n        data = json.load(f)\n\n    # Could be tiebreak_analysis.json or sica_d012_14b.json\n    if \"strategies\" in data:\n        return {\n            \"n_total\": data[\"n_total\"],\n            \"n_tie\": data[\"n_tie\"],\n            \"sica_tie_accuracy\": data[\"strategies\"][\"sica\"][\"accuracy\"],\n            \"sica_tie_correct\": data[\"strategies\"][\"sica\"][\"correct\"],\n        }\n    elif \"results\" in data:\n        problems = data[\"results\"]\n        ties = [p for p in problems if is_sc_tie(p.get(\"sc_vote_distribution\", {}))]\n        if not ties:\n            return {\"n_total\": len(problems), \"n_tie\": 0, \"sica_tie_accuracy\": None, \"sica_tie_correct\": 0}\n        return {\n            \"n_total\": len(problems),\n            \"n_tie\": len(ties),\n            \"sica_tie_accuracy\": sum(p[\"sica_correct\"] for p in ties) / len(ties),\n            \"sica_tie_correct\": sum(p[\"sica_correct\"] for p in ties),\n        }\n    return None\n\n\n# ── Output formatting ────────────────────────────────────────────\n\ndef print_markdown(groups: list[dict], overall: dict, d012_tb: dict | None):\n    print(\"\\n## exp-001 Expanded Analysis (sica_expanded_14b)\\n\")\n\n    # Main table\n    header = \"| Dataset         |   N | C0%   | SICA Acc | SC Acc  | D (pp) | McNemar p |\"\n    sep    = \"|-----------------|-----|-------|----------|---------|--------|-----------|\"\n    print(header)\n    print(sep)\n    for g in groups:\n        sig = \"*\" if g[\"mcnemar_p\"] < 0.05 else \"\"\n        print(f\"| {g['label']:15s} | {g['n']:3d} | {g['c0_rate']*100:5.1f} | \"\n              f\"{g['sica_accuracy']*100:6.2f}% | {g['sc_accuracy']*100:6.2f}% | \"\n              f\"{g['delta_pp']:+5.2f} | {g['mcnemar_p']:.4f}{sig} |\")\n    sig = \"*\" if overall[\"mcnemar_p\"] < 0.05 else \"\"\n    print(f\"| {'**Overall**':15s} | {overall['n']:3d} | {overall['c0_rate']*100:5.1f} | \"\n          f\"{overall['sica_accuracy']*100:6.2f}% | {overall['sc_accuracy']*100:6.2f}% | \"\n          f\"{overall['delta_pp']:+5.2f} | {overall['mcnemar_p']:.4f}{sig} |\")\n\n    # Disagreement\n    print(f\"\\nDisagreements: SICA-only correct = {overall['sica_only_correct']}, \"\n          f\"SC-only correct = {overall['sc_only_correct']}\")\n\n    # Tiebreak table\n    print(\"\\n### Tiebreak Analysis\\n\")\n    print(\"| Dataset         | SC Ties | SICA Win | SICA Tie-Acc |\")\n    print(\"|-----------------|---------|----------|--------------|\")\n    for g in groups:\n        if g[\"n_ties\"] > 0:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} | \"\n                  f\"{g['tie_sica_correct']:8d} | {g['tie_sica_accuracy']*100:10.1f}% |\")\n        else:\n            print(f\"| {g['label']:15s} | {g['n_ties']:7d} |      n/a |          n/a |\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} | \"\n              f\"{overall['tie_sica_correct']:8d} | {overall['tie_sica_accuracy']*100:10.1f}% |\")\n    else:\n        print(f\"| {'**Overall**':15s} | {overall['n_ties']:7d} |      n/a |          n/a |\")\n\n    # D012 comparison\n    if d012_tb and d012_tb.get(\"n_tie\", 0) > 0 and overall[\"n_ties\"] > 0:\n        print(f\"\\nD012 pilot comparison (n={d012_tb['n_total']}):\")\n        print(f\"  D012 ties: {d012_tb['n_tie']}, \"\n              f\"SICA tie-acc: {d012_tb['sica_tie_accuracy']*100:.1f}%\")\n        print(f\"  Expanded ties: {overall['n_ties']}, \"\n              f\"SICA tie-acc: {overall['tie_sica_accuracy']*100:.1f}%\")\n        d012_rate = d012_tb[\"n_tie\"] / d012_tb[\"n_total\"] * 100\n        exp_rate = overall[\"n_ties\"] / overall[\"n\"] * 100\n        print(f\"  Tie rate: D012 {d012_rate:.1f}% -> Expanded {exp_rate:.1f}%\")\n\n    # Key numbers\n    print(\"\\n### Key Numbers\\n\")\n    print(f\"- Total problems: {overall['n']}\")\n    print(f\"- SICA accuracy: {overall['sica_accuracy']*100:.2f}% ({overall['sica_correct']}/{overall['n']})\")\n    print(f\"- SC accuracy: {overall['sc_accuracy']*100:.2f}% ({overall['sc_correct']}/{overall['n']})\")\n    print(f\"- Delta: {overall['delta_pp']:+.2f} pp (McNemar p={overall['mcnemar_p']:.4f})\")\n    print(f\"- SC ties: {overall['n_ties']} ({overall['n_ties']/overall['n']*100:.1f}%)\")\n    if overall[\"n_ties\"] > 0:\n        print(f\"- SICA tie-accuracy: {overall['tie_sica_accuracy']*100:.1f}% \"\n              f\"({overall['tie_sica_correct']}/{overall['n_ties']})\")\n\n\n# ── File discovery ───────────────────────────────────────────────\n\ndef find_results_file(path: str) -> str:\n    if os.path.isfile(path):\n        return path\n    if os.path.isdir(path):\n        candidate = os.path.join(path, \"sica_expanded_14b.json\")\n        if os.path.exists(candidate):\n            return candidate\n        jsons = [f for f in os.listdir(path) if f.endswith(\".json\") and \"expanded\" in f]\n        if len(jsons) == 1:\n            return os.path.join(path, jsons[0])\n        if jsons:\n            raise FileNotFoundError(\n                f\"Multiple expanded JSON files in {path}: {jsons}. Specify exact path.\")\n    raise FileNotFoundError(f\"Cannot find results file at {path}\")\n\n\n# ── Main ─────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Analyze exp-001 (sica_expanded_14b) results: per-dataset accuracy, \"\n                    \"tiebreak stats, McNemar significance tests.\",\n    )\n    parser.add_argument(\n        \"--results-dir\", default=\"results/sica_expanded_14b.json\",\n        help=\"Path to results JSON file or directory (default: results/sica_expanded_14b.json)\",\n    )\n    parser.add_argument(\n        \"--output\", default=None,\n        help=\"Output JSON path (default: alongside input file as analysis_expanded.json)\",\n    )\n    parser.add_argument(\n        \"--d012\", default=None,\n        help=\"Path to D012 pilot data for tiebreak comparison \"\n             \"(auto-detects tiebreak_analysis.json or sica_d012_14b.json if not set)\",\n    )\n    args = parser.parse_args()\n\n    # Find and load results\n    results_path = find_results_file(args.results_dir)\n    with open(results_path) as f:\n        data = json.load(f)\n    problems = data[\"results\"]\n    n = len(problems)\n    print(f\"Loaded {n} problems from {results_path}\")\n\n    # Group by dataset\n    by_dataset: dict[str, list[dict]] = defaultdict(list)\n    for p in problems:\n        ds = p.get(\"dataset\", \"unknown\")\n        by_dataset[ds].append(p)\n\n    # Per-dataset analysis\n    dataset_order = [\"proofwriter\", \"folio\"]\n    groups = []\n    for ds in dataset_order:\n        if ds in by_dataset:\n            groups.append(analyze_group(by_dataset[ds], ds))\n    for ds in sorted(by_dataset.keys()):\n        if ds not in dataset_order:\n            groups.append(analyze_group(by_dataset[ds], ds))\n\n    overall = analyze_group(problems, \"overall\")\n\n    # D012 tiebreak comparison\n    d012_tb = None\n    if args.d012:\n        d012_tb = load_d012_tiebreak(args.d012)\n    else:\n        results_dir = os.path.dirname(results_path)\n        for candidate in [\"tiebreak_analysis.json\", \"sica_d012_14b.json\"]:\n            cpath = os.path.join(results_dir, candidate)\n            if os.path.exists(cpath):\n                d012_tb = load_d012_tiebreak(cpath)\n                if d012_tb:\n                    break\n\n    # Print markdown\n    print_markdown(groups, overall, d012_tb)\n\n    # Save JSON\n    output_path = args.output\n    if output_path is None:\n        base = os.path.dirname(results_path)\n        output_path = os.path.join(base or \".\", \"sica_expanded_14b\", \"analysis.json\")\n        if not os.path.isdir(os.path.join(base, \"sica_expanded_14b\")):\n            output_path = os.path.join(base or \".\", \"analysis_expanded.json\")\n\n    json_out = {\n        \"experiment\": \"exp-001_sica_expanded_14b\",\n        \"source_file\": results_path,\n        \"n_problems\": n,\n        \"per_dataset\": {g[\"label\"]: g for g in groups},\n        \"overall\": overall,\n        \"d012_tiebreak_comparison\": d012_tb,\n    }\n\n    for section in list(json_out[\"per_dataset\"].values()) + [json_out[\"overall\"]]:\n        section.pop(\"tie_indices\", None)\n\n    os.makedirs(os.path.dirname(output_path) or \".\", exist_ok=True)\n    with open(output_path, \"w\") as f:\n        json.dump(json_out, f, indent=2)\n    print(f\"\\nDetailed results saved to {output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T08:04:40.337199+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T08:04:40.337332+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cd /root/symb_invariant_consensus && python scripts/analyze_expanded.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cd /root/symb_invariant_consensus && python scripts/analyze_expanded.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T08:04:40.337459+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python scripts/analyze_expanded.py --help'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T08:04:40.337579+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cd /root/symb_invariant_consensus && python3 scripts/analyze_expanded.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cd /root/symb_invariant_consensus && python3 scripts/analyze_expanded.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T08:04:40.337703+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python3 scripts/analyze_expanded.py --help'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.03}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T08:04:40.337837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "which python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "which python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T08:04:40.337974+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T08:04:40.338090+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/miniconda3/bin/python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/miniconda3/bin/python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T08:04:40.338204+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.89}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T08:04:40.338314+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/analyze_expanded.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/analyze_expanded.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T08:04:40.338437+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: analyze_expanded.py [-h] [--results-dir RESULTS_DIR] [--output OUTPUT]\\n                           [--d012 D012]\\n\\nAnalyze exp-001 (sica_expanded_14b) results: per-dataset accuracy, tiebreak\\nstats, McNemar significance tests.\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --results-dir RESULTS_DIR\\n                        Path to results JSON file or directory (default:\\n                        results/sica_expanded_14b.json)\\n  --output OUTPUT       Output JSON path (default: alongside input file as\\n                        analysis_expanded.json)\\n  --d012 D012           Path to D012 pilot data for tiebreak comparison (auto-\\n                        detects tiebreak_analysis.json or sica_d012_14b.json\\n                        if not set)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T08:04:40.338571+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/analyze_expanded.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "command": "cd /root/symb_invariant_consensus && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python scripts/analyze_expanded.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T08:04:40.338708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 157 problems from results/sica_expanded_14b.json\\n\\n## exp-001 Expanded Analysis (sica_expanded_14b)\\n\\n| Dataset         |   N | C0%   | SICA Acc | SC Acc  | D (pp) | McNemar p |\\n|-----------------|-----|-------|----------|---------|--------|-----------|\\n| proofwriter     | 157 |  40.1 |  75.80% |  77.07% | -1.27 | 0.7266 |\\n| **Overall**     | 157 |  40.1 |  75.80% |  77.07% | -1.27 | 0.7266 |\\n\\nDisagreements: SICA-only correct = 3, SC-only correct = 5\\n\\n### Tiebreak Analysis\\n\\n| Dataset         | SC Ties | SICA Win | SICA Tie-Acc |\\n|-----------------|---------|----------|--------------|\\n| proofwriter     |       8 |        4 |       50.0% |\\n| **Overall**     |       8 |        4 |       50.0% |\\n\\nD012 pilot comparison (n=60):\\n  D012 ties: 5, SICA tie-acc: 80.0%\\n  Expanded ties: 8, SICA tie-acc: 50.0%\\n  Tie rate: D012 8.3% -> Expanded 5.1%\\n\\n### Key Numbers\\n\\n- Total problems: 157\\n- SICA accuracy: 75.80% (119/157)\\n- SC accuracy: 77.07% (121/157)\\n- Delta: -1.27 pp (McNemar p=0.7266)\\n- SC ties: 8 (5.1%)\\n- SICA tie-accuracy: 50.0% (4/8)\\n\\nDetailed results saved to results/analysis_expanded.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.61}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_analyze-expanded_20260516T080105",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-16T08:04:40.338893+00:00_

脚本已部署并验证通过。当前157题（全部proofwriter，FOLIO还没进来）的快照：

```
| Dataset     |   N | C0%  | SICA Acc | SC Acc  | Δ (pp) | McNemar p |
|-------------|-----|------|----------|---------|--------|-----------|
| proofwriter | 157 | 40.1 |  75.80%  |  77.07% | -1.27  | 0.7266    |
```

- SC ties: 8 (5.1%), SICA tie-acc: 50.0%
- D012 对比：tie率从8.3%降到5.1%，tie-acc从80%降到50%
- JSON详细结果已保存到 `results/analysis_expanded.json`

产出文件：`/root/symb_invariant_consensus/scripts/analyze_expanded.py`，`--help` 和实际运行均正常。804题跑完后直接执行即可出报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_analyze-expanded_20260516T080105"
}
```

</details>

---
