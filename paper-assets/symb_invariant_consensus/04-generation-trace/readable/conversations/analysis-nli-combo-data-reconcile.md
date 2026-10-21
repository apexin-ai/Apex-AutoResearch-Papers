# analysis nli combo data reconcile

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_analysis_nli-combo-data-reconcile_20260522T145105.jsonl`
- **Structured JSON:** [`2dab30d52da56d162337.json`](../../sessions/2d/2dab30d52da56d162337.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-22T14:54:03.303647+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T14:54:03.304055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T14:54:03.304252+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp-090'}",
  "project": "symb_invariant_consensus",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp-090'}",
    "project": "symb_invariant_consensus",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T14:54:03.304394+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4874}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T14:54:03.304522+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp-048'}",
  "project": "symb_invariant_consensus",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp-048'}",
    "project": "symb_invariant_consensus",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T14:54:03.304647+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4346}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T14:54:03.304768+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": "0",
  "fields": "['exp_id', 'hypothesis', 'status', 'conclusion', 'metrics', 'notes', 'tags']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "limit": "0",
    "fields": "['exp_id', 'hypothesis', 'status', 'conclusion', 'metrics', 'notes', 'tags']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T14:54:03.304996+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T14:54:03.305751+00:00_

Error: result (117,040 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T14:54:03.306350+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md\", \"content\": \"# Paper Framing — symb_invariant_consensus\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25)\\n- Deadline: May 25, 2026 (ARR submission)\\n\\n## D063 Direction: Entropy Decomposition + Quality Ladder — 目标 4.0\\n\\n**从 D060 \\\"Pure Analysis / negative result\\\" 升级为 \\\"Regime-Dependent Mechanism Analysis with Entropy Decomposition\\\"。** 用户决定冲 4.0。\\n\\n### Entropy Breakdown 验证结果 (2026-05-19 completed)\\n\\n**跨模型 entropy mechanism 一致性: 不成立。Selective SICA 非 universal 方案。**\\n\\n但 entropy decomposition 揭示了更有价值的 regime mechanism：\\n\\n| Experiment | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |\\n|-----------|-------|---------|----------|-----------|---------|----------|\\n| exp-033 s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |\\n| exp-052 s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |\\n| exp-053 s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |\\n| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |\\n| exp-036 | Qwen2.5-14B | FOLIO | 37 | **-8.2** | 167 | -0.6 |\\n| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |\\n| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |\\n| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |\\n\\n(注: SC/Δ 使用 pre-tiebreaking 值，entropy grouping 不受 tiebreaking 影响。D064 修正后 deltas 会略有变化但 pattern 不变。)\\n\\n**三个核心发现：**\\n1. **Low-entropy: SICA≈SC 跨模型一致** (8/8 experiments Δ≈0) → traces 一致时 constraints 无新信息\\n2. **High-entropy 方向因 regime 而异**：Goldilocks +12.8pp vs Type A -8.2pp vs Type C -4.9pp\\n3. **Mechanism 解释**：\\n   - Goldilocks (SC~55%, κ~0.46): 真实不确定性 → constraints 打破平局正确方向\\n   - Type A (SC>75%, κ>0.65): 偶发错误 → constraints 放大 confirmation bias\\n   - Type C (SC<40%, κ~0.20): 系统性错误 → constraints 是噪声\\n\\n### 调整后核心转变\\n\\n论文以 \\\"entropy decomposition 揭示 regime-dependent mechanism\\\" 为核心分析贡献（不是 
…[truncated 40407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T14:54:03.306597+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Search for NLI, combo, cross-arch, deberta, wave3, 090, 048\nkeywords = ['nli', 'combo', 'cross-arch', 'deberta', 'wave3', 'wave3-dir-r', '090', '048', '+6.67', '+3.50', '6.67', '3.50']\nfor exp_id, exp_data in exps.items():\n    exp_str = json.dumps(exp_data, default=str).lower()\n    for kw in keywords:\n        if kw.lower() in exp_str:\n            print(f'=== {exp_id} matches [{kw}] ===')\n            print(json.dumps(exp_data, indent=2, default=str)[:2000])\n            print('---')\n            break\n\" 2>&1 | head -500",
  "description": "Search registry for NLI/combo/deberta related experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/259e8c74-cee8-43ee-8c2a-b39b28aafca2/tool-results/mcp-agent-ml-research-read_registry-1779461485443.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n# Search for NLI, combo, cross-arch, deberta, wave3, 090, 048\nkeywords = ['nli', 'combo', 'cross-arch', 'deberta', 'wave3', 'wave3-dir-r', '090', '048', '+6.67', '+3.50', '6.67', '3.50']\nfor exp_id, exp_data in exps.items():\n    exp_str = json.dumps(exp_data, default=str).lower()\n    for kw in keywords:\n        if kw.lower() in exp_str:\n            print(f'=== {exp_id} matches [{kw}] ===')\n            print(json.dumps(exp_data, indent=2, default=str)[:2000])\n            print('---')\n            break\n\" 2>&1 | head -500",
    "description": "Search registry for NLI/combo/deberta related experiments"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T14:54:03.306998+00:00_

=== exp-multi-seed-llama-pw matches [048] ===
{
  "status": "PREPARING",
  "hypothesis": "Multi-seed replication (seeds 42,123,456) of LLaMA-3.1-8B \u00d7 ProofWriter-600 adds cross-dataset evidence for the third model family. If \u0394(SICA-SC)\u22640 holds on PW as well as FOLIO, it confirms SCB is dataset-invariant within LLaMA-8B. Addresses W4 reviewer concern.",
  "notes": "PID 614142 on westd-16639 cuda:3 port 8004. vLLM PID 613151 (LLaMA-3.1-8B, max-model-len=8192, max_tokens=2048). 3-seed sequence: 42\u2192123\u2192456. Each seed ~600 problems. Model: /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct. Script: scripts/multiseed_llama8b_pw_cuda3.sh",
  "metrics": {
    "pw_seed42": {
      "status": "running",
      "progress": "60/600"
    },
    "pw_seed123": {
      "status": "pending"
    },
    "pw_seed456": {
      "status": "pending"
    }
  }
}
---
=== exp-multi-seed-llama-folio matches [048] ===
{
  "status": "PREPARING",
  "hypothesis": "Multi-seed replication (seeds 123,456,789) of LLaMA-3.1-8B \u00d7 FOLIO-204 shows consistent \u0394(SICA-SC) direction across seeds, adding a third model family (beyond Qwen2.5 and Mistral) for cross-family consistency evidence. Addresses W4 reviewer concern.",
  "notes": "PID 596151 on westd-16639 cuda:1 port 8002. vLLM PID 595261 (max-model-len=8192, max_tokens=2048). Previous attempt failed: max-model-len=4096 caused HTTP 400 on all requests. Fixed by increasing to 8192 + reducing max_tokens to 2048. ~70s/prob, 3 seeds sequential, ETA ~12h (~23:00 UTC May 22). Output: results/multi_seed/llama8b_folio_seed{123,456,789}/",
  "metrics": {
    "seed123": {
      "sc_acc": 67.16,
      "sica_acc": 63.73,
      "delta": -3.43,
      "n": 204,
      "extraction_rate": 0.959,
      "status": "COMPLETE"
    },
    "seed456": {
      "status": "running",
      "progress": "125/204"
    },
    "seed789": {
      "status": "pending"
    }
  }
}
---
=== exp-multi-seed-mistral-pw matches [6.67] ===
{
  "status": "PREPARING",
 
…[truncated 19139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T14:54:03.307188+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/nli_multi_verifier*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/nli_multi_verifier*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T14:54:03.307320+00:00_

artifacts/_project/data/nli_multi_verifier_recomputed.json
artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json
artifacts/nli_multi_verifier_recomputed.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T14:54:03.307441+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*nli*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*nli*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T14:54:03.307562+00:00_

artifacts/direction_r_nli_large/data/direction_r_nli_large_pointer.txt
artifacts/dir_j2_nli_qwen3.py
artifacts/dir_j3_nli_multi_verifier.py
artifacts/push_b_stronger_nli.py
artifacts/_project/report/nli_tiebreaking_audit.json
artifacts/nli_tiebreaking_audit.json
artifacts/_project/data/nli_combo_recomputed.json
artifacts/nli_combo_recomputed.json
artifacts/_project/data/nli_multi_verifier_recomputed.json
artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json
artifacts/nli_multi_verifier_recomputed.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T14:54:03.307727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_multi_verifier_recomputed.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_multi_verifier_recomputed.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T14:54:03.307973+00:00_

1	{
2	  "roberta_mnli": {
3	    "standalone_acc": 37.67,
4	    "standalone_correct": 226,
5	    "n": 600,
6	    "mistral_pw_combo": {
7	      "w1": {
8	        "acc": 39.17,
9	        "correct": 235,
10	        "delta_pp": -0.17,
11	        "mcnemar_p": 1.0,
12	        "b": 8,
13	        "c": 7
14	      },
15	      "w3": {
16	        "acc": 43.5,
17	        "correct": 261,
18	        "delta_pp": 4.17,
19	        "mcnemar_p": 0.002626,
20	        "b": 20,
21	        "c": 45
22	      },
23	      "w5": {
24	        "acc": 43.67,
25	        "correct": 262,
26	        "delta_pp": 4.33,
27	        "mcnemar_p": 0.036852,
28	        "b": 59,
29	        "c": 85
30	      }
31	    }
32	  },
33	  "bart_mnli": {
34	    "standalone_acc": 46.17,
35	    "standalone_correct": 277,
36	    "n": 600,
37	    "mistral_pw_combo": {
38	      "w1": {
39	        "acc": 39.33,
40	        "correct": 236,
41	        "delta_pp": 0.0,
42	        "mcnemar_p": 1.0,
43	        "b": 9,
44	        "c": 9
45	      },
46	      "w3": {
47	        "acc": 44.5,
48	        "correct": 267,
49	        "delta_pp": 5.17,
50	        "mcnemar_p": 0.000244,
51	        "b": 19,
52	        "c": 50
53	      },
54	      "w5": {
55	        "acc": 45.67,
56	        "correct": 274,
57	        "delta_pp": 6.33,
58	        "mcnemar_p": 0.002749,
59	        "b": 58,
60	        "c": 96
61	      }
62	    }
63	  },
64	  "deberta_mnli_crosscheck": {
65	    "standalone_acc": 55.0,
66	    "standalone_correct": 330,
67	    "w3_combo_acc": 46.0,
68	    "w3_combo_correct": 276,
69	    "w3_gain": 6.67,
70	    "matches_recomputed": true
71	  },
72	  "sc_baseline_crosscheck": {
73	    "alpha_sc_acc": 39.33,
74	    "alpha_sc_correct": 236,
75	    "expected": 39.33,
76	    "matches": true
77	  },
78	  "spearman_pw6": {
79	    "description": "6 ProofWriter points, all w=3",
80	    "points": [
81	      {
82	        "label": "DeBERTa-L \u00d7 Mistral-7B",
83	        "gap": 15.67,
84	        "gain": 6.67
85	      },
86	      {
87	        "la
…[truncated 2250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T14:54:03.308161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T14:54:03.308418+00:00_

1	{
2	  "proofwriter": {
3	    "Mistral-7B": {
4	      "n": 600,
5	      "sc": {
6	        "acc": 39.33,
7	        "n_correct": 236
8	      },
9	      "w1": {
10	        "acc": 40.17,
11	        "n_correct": 241,
12	        "delta_pp": 0.83,
13	        "mcnemar_p": 0.359283447265625,
14	        "b": 12,
15	        "c": 7
16	      },
17	      "w3": {
18	        "acc": 46.0,
19	        "n_correct": 276,
20	        "delta_pp": 6.67,
21	        "mcnemar_p": 1.1296023055413025e-05,
22	        "b": 61,
23	        "c": 21
24	      },
25	      "w5": {
26	        "acc": 50.33,
27	        "n_correct": 302,
28	        "delta_pp": 11.0,
29	        "mcnemar_p": 6.178035816936483e-07,
30	        "b": 120,
31	        "c": 54
32	      }
33	    },
34	    "LLaMA-3.1-8B": {
35	      "n": 600,
36	      "sc": {
37	        "acc": 72.5,
38	        "n_correct": 435
39	      },
40	      "w1": {
41	        "acc": 73.33,
42	        "n_correct": 440,
43	        "delta_pp": 0.83,
44	        "mcnemar_p": 0.359283447265625,
45	        "b": 12,
46	        "c": 7
47	      },
48	      "w3": {
49	        "acc": 73.33,
50	        "n_correct": 440,
51	        "delta_pp": 0.83,
52	        "mcnemar_p": 0.6646454904132133,
53	        "b": 45,
54	        "c": 40
55	      },
56	      "w5": {
57	        "acc": 72.0,
58	        "n_correct": 432,
59	        "delta_pp": -0.5,
60	        "mcnemar_p": 0.8707787409560847,
61	        "b": 74,
62	        "c": 77
63	      }
64	    },
65	    "Qwen2.5-14B": {
66	      "n": 600,
67	      "sc": {
68	        "acc": 74.0,
69	        "n_correct": 444
70	      },
71	      "w1": {
72	        "acc": 74.17,
73	        "n_correct": 445,
74	        "delta_pp": 0.17,
75	        "mcnemar_p": 1.0,
76	        "b": 3,
77	        "c": 2
78	      },
79	      "w3": {
80	        "acc": 74.67,
81	        "n_correct": 448,
82	        "delta_pp": 0.67,
83	        "mcnemar_p": 0.5034446716308594,
84	        "b": 12,
85	        "c": 8
86	      },
87	      "w5": {
88	        "acc": 75.17,
89	  
…[truncated 4491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T14:54:03.308612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed.json"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T14:54:03.308805+00:00_

1	{
2	  "roberta_mnli": {
3	    "standalone_acc": 37.67,
4	    "standalone_correct": 226,
5	    "n": 600,
6	    "mistral_pw_combo": {
7	      "w1": {
8	        "acc": 39.17,
9	        "correct": 235,
10	        "delta_pp": -0.17,
11	        "mcnemar_p": 1.0,
12	        "b": 8,
13	        "c": 7
14	      },
15	      "w3": {
16	        "acc": 43.5,
17	        "correct": 261,
18	        "delta_pp": 4.17,
19	        "mcnemar_p": 0.002626,
20	        "b": 20,
21	        "c": 45
22	      },
23	      "w5": {
24	        "acc": 43.67,
25	        "correct": 262,
26	        "delta_pp": 4.33,
27	        "mcnemar_p": 0.036852,
28	        "b": 59,
29	        "c": 85
30	      }
31	    }
32	  },
33	  "bart_mnli": {
34	    "standalone_acc": 46.17,
35	    "standalone_correct": 277,
36	    "n": 600,
37	    "mistral_pw_combo": {
38	      "w1": {
39	        "acc": 39.33,
40	        "correct": 236,
41	        "delta_pp": 0.0,
42	        "mcnemar_p": 1.0,
43	        "b": 9,
44	        "c": 9
45	      },
46	      "w3": {
47	        "acc": 44.5,
48	        "correct": 267,
49	        "delta_pp": 5.17,
50	        "mcnemar_p": 0.000244,
51	        "b": 19,
52	        "c": 50
53	      },
54	      "w5": {
55	        "acc": 45.67,
56	        "correct": 274,
57	        "delta_pp": 6.33,
58	        "mcnemar_p": 0.002749,
59	        "b": 58,
60	        "c": 96
61	      }
62	    }
63	  },
64	  "deberta_mnli_crosscheck": {
65	    "standalone_acc": 55.0,
66	    "standalone_correct": 330,
67	    "w3_combo_acc": 46.0,
68	    "w3_combo_correct": 276,
69	    "w3_gain": 6.67,
70	    "matches_recomputed": true
71	  },
72	  "sc_baseline_crosscheck": {
73	    "alpha_sc_acc": 39.33,
74	    "alpha_sc_correct": 236,
75	    "expected": 39.33,
76	    "matches": true
77	  },
78	  "spearman_pw6": {
79	    "description": "6 ProofWriter points, all w=3",
80	    "points": [
81	      {
82	        "label": "DeBERTa-L \u00d7 Mistral-7B",
83	        "gap": 15.67,
84	        "gain": 6.67
85	      },
86	      {
87	        "la
…[truncated 2250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T14:54:03.309122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_tiebreaking_audit.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_tiebreaking_audit.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T14:54:03.309333+00:00_

1	{
2	  "investigation": {
3	    "affected_scripts": [
4	      "direction_r_deberta_proofwriter.py",
5	      "dir_j3_nli_multi_verifier.py",
6	      "dir_k_nli_qwen3_pw600.py",
7	      "direction_rg_combo.py",
8	      "direction_r_nli_verifier.py (FOLIO)"
9	    ],
10	    "tiebreaking_method": "Counter.most_common(1)[0][0] — insertion-order tiebreaking under ties",
11	    "correct_method": "sorted(tied_candidates)[0] — alphabetical (consistent with SC baseline standard)",
12	    "drc_cascade_pilot_method": "alphabetical (correct, in scripts/drc_cascade_pilot.py)",
13	    "code_snippet": "combo_answer = votes.most_common(1)[0][0]  # BUG: non-alphabetical tiebreaking"
14	  },
15	  "experiments": {
16	    "exp-090 (Mistral-7B PW)": {
17	      "n": 600,
18	      "sc_baseline_alpha": "39.33% (236/600)",
19	      "sc_baseline_counter": "39.33% (236/600)",
20	      "sc_tiebreak_diffs": 11,
21	      "combo_w1": {
22	        "current_counter": "40.17% (241/600)",
23	        "corrected_alpha": "40.17% (241/600)",
24	        "delta": "0.00pp",
25	        "changed_questions": 17,
26	        "mcnemar_alpha_vs_sc": {"p": 0.359283, "b": 7, "c": 12},
27	        "mcnemar_counter_vs_sc": {"p": 0.266846, "b": 4, "c": 9}
28	      },
29	      "combo_w3": {
30	        "current_counter": "42.83% (257/600)",
31	        "corrected_alpha": "46.00% (276/600)",
32	        "delta": "+3.17pp",
33	        "changed_questions": 30,
34	        "mcnemar_alpha_vs_sc": {"p": 1.1e-05, "b": 21, "c": 61},
35	        "mcnemar_counter_vs_sc": {"p": 0.012503, "b": 22, "c": 43}
36	      },
37	      "combo_w5": {
38	        "current_counter": "50.00% (300/600)",
39	        "corrected_alpha": "50.33% (302/600)",
40	        "delta": "+0.33pp",
41	        "changed_questions": 53,
42	        "mcnemar_alpha_vs_sc": {"p": 1e-06, "b": 54, "c": 120},
43	        "mcnemar_counter_vs_sc": {"p": 0.0, "b": 35, "c": 99}
44	      }
45	    },
46	    "exp-091 (Qwen3 PW)": {
47	      "status": "NEEDS_RECOMPUTATION",
48	      "da
…[truncated 2402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T14:54:03.309493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/nli_multi_verifier_recomputed_b79bf3.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T14:54:03.309680+00:00_

1	{
2	  "roberta_mnli": {
3	    "standalone_acc": 37.67,
4	    "standalone_correct": 226,
5	    "n": 600,
6	    "mistral_pw_combo": {
7	      "w1": {
8	        "acc": 39.17,
9	        "correct": 235,
10	        "delta_pp": -0.17,
11	        "mcnemar_p": 1.0,
12	        "b": 8,
13	        "c": 7
14	      },
15	      "w3": {
16	        "acc": 43.5,
17	        "correct": 261,
18	        "delta_pp": 4.17,
19	        "mcnemar_p": 0.002626,
20	        "b": 20,
21	        "c": 45
22	      },
23	      "w5": {
24	        "acc": 43.67,
25	        "correct": 262,
26	        "delta_pp": 4.33,
27	        "mcnemar_p": 0.036852,
28	        "b": 59,
29	        "c": 85
30	      }
31	    }
32	  },
33	  "bart_mnli": {
34	    "standalone_acc": 46.17,
35	    "standalone_correct": 277,
36	    "n": 600,
37	    "mistral_pw_combo": {
38	      "w1": {
39	        "acc": 39.33,
40	        "correct": 236,
41	        "delta_pp": 0.0,
42	        "mcnemar_p": 1.0,
43	        "b": 9,
44	        "c": 9
45	      },
46	      "w3": {
47	        "acc": 44.5,
48	        "correct": 267,
49	        "delta_pp": 5.17,
50	        "mcnemar_p": 0.000244,
51	        "b": 19,
52	        "c": 50
53	      },
54	      "w5": {
55	        "acc": 45.67,
56	        "correct": 274,
57	        "delta_pp": 6.33,
58	        "mcnemar_p": 0.002749,
59	        "b": 58,
60	        "c": 96
61	      }
62	    }
63	  },
64	  "deberta_mnli_crosscheck": {
65	    "standalone_acc": 55.0,
66	    "standalone_correct": 330,
67	    "w3_combo_acc": 46.0,
68	    "w3_combo_correct": 276,
69	    "w3_gain": 6.67,
70	    "matches_recomputed": true
71	  },
72	  "sc_baseline_crosscheck": {
73	    "alpha_sc_acc": 39.33,
74	    "alpha_sc_correct": 236,
75	    "expected": 39.33,
76	    "matches": true
77	  },
78	  "spearman_pw6": {
79	    "description": "6 ProofWriter points, all w=3",
80	    "points": [
81	      {
82	        "label": "DeBERTa-L \u00d7 Mistral-7B",
83	        "gap": 15.67,
84	        "gain": 6.67
85	      },
86	      {
87	        "la
…[truncated 2250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-22T14:54:03.309936+00:00_

完整的证据链已找到。根因是 **tiebreaking bug**。

---

## 排查结果

### 1. +6.67pp 来自哪个实验

来自 `nli_combo_recomputed.json`（tiebreaking 修正后的版本）：
- **配置**: DeBERTa-large-MNLI × Mistral-7B × ProofWriter-600, w=3, n=600
- **SC baseline**: 39.33% (236/600)
- **combo w=3**: 46.00% (276/600), **+6.67pp**, McNemar p=1.13e-05
- **tiebreaking**: 字母序（alphabetical），与 SC baseline 一致

### 2. exp-090 是什么实验

`exp-090-r-nli-proofwriter`，**同一实验的原始版本**（未修正 tiebreaking）：
- 完全相同的模型、数据集、配置
- **combo w=3**: 42.83% (257/600), **+3.50pp**, McNemar p=0.0125
- **tiebreaking**: `Counter.most_common(1)[0][0]`——插入序（insertion-order），与 SC baseline 不一致

### 3. 数据不一致的根因

**Tiebreaking bug**。详见 `nli_tiebreaking_audit.json`：

| 项目 | exp-090 (buggy) | recomputed (corrected) |
|------|-----------------|----------------------|
| tiebreaking | `Counter.most_common()` 插入序 | `sorted(tied)[0]` 字母序 |
| combo w3 correct | 257/600 | 276/600 |
| delta | +3.50pp | +6.67pp |
| McNemar p | 0.0125 | 1.13e-05 |
| 受影响题数 | — | 30题 |

combo 脚本用 `votes.most_common(1)[0][0]` 做 tie resolution，而 SC baseline 用字母序。两套 tiebreaking 标准导致 combo 在 30 个平票问题上选了不同答案。DRC cascade pilot 独立使用字母序也得到 46.0%，交叉验证了修正值。

### 4. 论文应引用哪组数据

**+6.67pp (recomputed)**。理由：
- 字母序 tiebreaking 与 SC baseline convention 一致（同一 comparand 同一标准）
- DRC cascade pilot 独立确认 46.0%
- BH 校正后 p=6.78e-05，仍 <0.001
- tiebreaking audit 明确建议更新到修正值

**需要做的**：将 exp-090 registry 的 metrics 更新为修正后数值，避免未来再次产生混淆。exp-091/092/093 也需要同步 recompute（audit 标记为 `NEEDS_RECOMPUTATION`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_nli-combo-data-reconcile_20260522T145105"
}
```

</details>

---
