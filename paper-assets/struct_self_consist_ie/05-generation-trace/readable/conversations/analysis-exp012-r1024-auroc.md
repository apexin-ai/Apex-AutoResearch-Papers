# analysis exp012 r1024 auroc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_analysis_exp012_r1024_auroc_20260514T224900.jsonl`
- **Structured JSON:** [`7a00ab27772ac7c5cc6a.json`](../../sessions/7a/7a00ab27772ac7c5cc6a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-14T22:51:54.703278+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T22:51:54.703652+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T22:51:54.703820+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T22:51:54.703972+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 3848\\ndrwxr-xr-x  2 root root     104 May 15 06:18 .\\ndrwxr-xr-x 65 root root    4096 May 15 06:21 ..\\n-rw-r--r--  1 root root     395 May 15 06:18 comparison.json\\n-rw-r--r--  1 root root    3376 May 15 06:17 report.json\\n-rw-r--r--  1 root root  100164 May 15 06:17 run.log\\n-rw-r--r--  1 root root 3820412 May 15 06:17 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T22:51:54.704106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/code/compute_*.py /root/autodl-tmp/struct_self_consist_ie/code/run_bootstrap*.py /root/autodl-tmp/struct_self_consist_ie/code/eval*.py 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/code/compute_*.py /root/autodl-tmp/struct_self_consist_ie/code/run_bootstrap*.py /root/autodl-tmp/struct_self_consist_ie/code/eval*.py 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:51:54.704303+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T22:51:54.704431+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "filters": "{'exp_id': 'exp_012_rerun_1024'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "filters": "{'exp_id': 'exp_012_rerun_1024'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T22:51:54.704557+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2068}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T22:51:54.704688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/code -name \"compute_*.py\" -o -name \"run_bootstrap*.py\" -o -name \"eval*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/code -name \"compute_*.py\" -o -name \"run_bootstrap*.py\" -o -name \"eval*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T22:51:54.704814+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n16_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/eval_s456_5signal.py\\n/root/autodl-tmp/struct_self_consist_ie/code/compute_re_conditional.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T22:51:54.704977+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T22:51:54.705255+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6632805497460412,\\n  \\\"ner_oracle_f1\\\": 0.7775133848899465,\\n  \\\"ner_oracle_headroom\\\": 0.11423283514390525,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.3932668065534345,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6963097751953397,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2665109373463269,\\n    \\\"p_value\\\": 4.716829112137585e-10,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3598905669976535,\\n    \\\"p_value\\\": 1.2752281196882738e-17,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.17607370722783125,\\n    \\\"p_value\\\": 0.00011078924939793821,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3113352549686453,\\n    \\\"p_value\\\": 3.5148620246813462e-12,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.09337962965132657,\\n  \\\"ner_sample_f1_mean\\\": 0.6077394535406134,\\n  \\\"ner_sample_f1_std\\\": 0.3177849195309394,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.594517958412098,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.20517413101613924,\\n      \\\"p_rho\\\": 1.9498006196855416e-06,\\n      \\\"tau\\\": 0.14782758668777154,\\n      \\\"p_tau\\\": 1.2434769103035355e-06,\\n      \\\"auroc\\\": 0.6115722797477874,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.1537825418721844,\\n      \\\"p_rho\\\": 0.0007519115126420073,\\n      \\\"tau\\\": 0.111054535706
…[truncated 2345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T22:51:54.705432+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T22:51:54.705821+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 9068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T22:51:54.705991+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": "5",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "limit": "5",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T22:51:54.706197+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-14T22:47:52.836Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.\", \"parent\": \"exp_017_llama_conll_n16_s456\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 456, \"server\": \"autodl-5090\"}, \"conclusion\": \"killed\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-14T22:47:52.219Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.\", \"parent\": \"exp_017_llama_conll_n16\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\"}, \"conclusion\": \"killed\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-14T22:47:51.191Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed123.\", \"parent\": \"exp_001_seed123_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed123_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529}, \"conclusion\": \"killed\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"RUNNING\", \"retry_count\": 
…[truncated 1763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T22:51:54.706394+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/eval_n8_5signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T22:51:54.706616+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"5-signal evaluation for N=8 experiments (baseline for N=8 vs N=16 comparison).\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nEXPERIMENTS = {\\n    \\\"exp_002_conll_n8\\\": {\\n        \\\"path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl\\\",\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"dataset\\\": \\\"conll2003\\\",\\n    },\\n    \\\"exp_007_llama_n8\\\": {\\n        \\\"path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl\\\",\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"dataset\\\": \\\"scierc\\\",\\n    },\\n}\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"he
…[truncated 4945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T22:51:54.706772+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -1 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T22:51:54.707096+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"
…[truncated 8656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T22:51:54.707318+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2 -name \"*.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2 -name \"*.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T22:51:54.707458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T22:51:54.707582+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/consistency.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/consistency.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T22:51:54.707831+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Consistency metrics for structured information extraction with self-consistency.\\n\\nImplements three complementary consistency measures over N sampled extractions:\\n1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence\\n2. Structural soft Jaccard — span-level soft overlap with Hungarian matching\\n3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance\\n\\nKey dependencies: numpy, scipy (linear_sum_assignment).\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nfrom itertools import combinations\\nfrom typing import TYPE_CHECKING\\n\\nimport numpy as np\\nfrom scipy.optimize import linear_sum_assignment\\n\\nif TYPE_CHECKING:\\n    pass\\n\\n# ---------------------------------------------------------------------------\\n# Type aliases (mirrors shared data format)\\n# ---------------------------------------------------------------------------\\nEntity = dict       # {\\\"text\\\", \\\"type\\\", \\\"start\\\", \\\"end\\\"}\\nRelation = dict     # {\\\"head\\\", \\\"tail\\\", \\\"type\\\", ...}\\nEvent = dict        # {\\\"trigger\\\": {...}, \\\"arguments\\\": [...]}\\nExtraction = dict   # {\\\"entities\\\", \\\"relations\\\", \\\"events\\\"}\\n\\n\\n# ===================================================================\\n# 1. Fleiss' Kappa — surface-level entity agreement\\n# ===================================================================\\n\\ndef _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:\\n    \\\"\\\"\\\"Extract surface-level keys from a sample for Fleiss' Kappa computation.\\\"\\\"\\\"\\n    if subtask == \\\"ner\\\":\\n        return {(e[\\\"text\\\"], e[\\\"type\\\"]) for e in sample.get(\\\"entities\\\", [])}\\n    elif subtask == \\\"re\\\":\\n        return {(r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in sample.get(\\\"relations\\\", [])}\\n    elif subtask == \\\"eae\\\":\\n   
…[truncated 7248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T22:51:54.708072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -80 /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -80 /root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T22:51:54.708340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc_n8_logprob_ner\\\": {\\n    \\\"metrics\\\": {\\n      \\\"SJ\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.7151643358013084,\\n          \\\"ci_95\\\": [\\n            0.6584056764120945,\\n            0.7682940600519558\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.3565325519208428,\\n          \\\"ci_95\\\": [\\n            0.27093589913089045,\\n            0.43847517254753815\\n          ]\\n        },\\n        \\\"Kendall_tau\\\": {\\n          \\\"value\\\": 0.2657836835394407,\\n          \\\"ci_95\\\": [\\n            0.20308584802623142,\\n            0.32764058791077727\\n          ]\\n        },\\n        \\\"ECE\\\": {\\n          \\\"value\\\": 0.45194957670806446\\n        }\\n      },\\n      \\\"FK\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.628716652955694,\\n          \\\"ci_95\\\": [\\n            0.5673132538124828,\\n            0.6923820223647049\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.2651050577998432,\\n          \\\"ci_95\\\": [\\n            0.1682875300012899,\\n            0.35268256172379303\\n          ]\\n        },\\n        \\\"Kendall_tau\\\": {\\n          \\\"value\\\": 0.20273442316972345,\\n          \\\"ci_95\\\": [\\n            0.13006411469552326,\\n            0.27188613541902706\\n          ]\\n        },\\n        \\\"ECE\\\": {\\n          \\\"value\\\": 0.4511674846945833\\n        }\\n      },\\n      \\\"logprob\\\": {\\n        \\\"AUROC\\\": {\\n          \\\"value\\\": 0.5805813452422924,\\n          \\\"ci_95\\\": [\\n            0.5218723422636723,\\n            0.6426371957852407\\n          ]\\n        },\\n        \\\"Spearman_rho\\\": {\\n          \\\"value\\\": 0.1396010152197563,\\n          \\\"ci_95\\\": [\\n            0.05136070196928419,\\n            0.2238566300960571\\n          ]\\n        },\\n 
…[truncated 392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T22:51:54.708598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/eval_n16_5signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/eval_n16_5signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T22:51:54.708823+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"5-signal evaluation for N=16 experiments (exp_002_conll_n16, exp_007_llama_n16).\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nEXPERIMENTS = {\\n    \\\"exp_002_conll_n16\\\": {\\n        \\\"path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl\\\",\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"dataset\\\": \\\"conll2003\\\",\\n    },\\n    \\\"exp_007_llama_n16\\\": {\\n        \\\"path\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl\\\",\\n        \\\"subtask\\\": \\\"ner\\\",\\n        \\\"dataset\\\": \\\"scierc\\\",\\n    },\\n}\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    if subtask == \\\"ner\\\":\\n        keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    else:\\n        keys = [frozenset((r[\\\"head\\\"], r[\\\"tail\\\"], r[\\\"type\\\"]) for r in s.get(\\\"relations\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    if subtask == \\\"ner\\\":\\n        for s in samples:\\n            for e in s.get(\\\"entities\\\", []):\\n                counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    else:\\n        for s in samples:\\n            for r in s.get(\\\"relations\\\", []):\\n                counter[(r[\\\"he
…[truncated 4946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T22:51:54.709076+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\"\"\"\nimport json, sys\nimport numpy as np\nfrom scipy.stats import spearmanr, rankdata\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\nDATA_PATH = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\"\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\ndef compute_exact_match_rate(samples, subtask):\n    if subtask == \"ner\":\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    else:\n        keys = [frozenset((r[\"head\"], r[\"tail\"], r[\"type\"]) for r in s.get(\"relations\", [])) for s in samples]\n    if not keys: return 0.0\n    c = Counter(keys)\n    return c.most_common(1)[0][1] / len(samples)\n\ndef compute_voting_confidence(samples, subtask):\n    N = len(samples)\n    if N == 0: return 0.0\n    counter = Counter()\n    if subtask == \"ner\":\n        for s in samples:\n            for e in s.get(\"entities\", []):\n                counter[(e[\"text\"], e[\"type\"])] += 1\n    else:\n        for s in samples:\n            for r in s.get(\"relations\", []):\n                counter[(r[\"head\"], r[\"tail\"], r[\"type\"])] += 1\n    if not counter: return 0.0\n    return float(np.mean([v / N for v in counter.values()]))\n\ndef compute_mean_logprob(samples):\n    lps = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    lps = [lp for lp in lps if np.isfinite(lp)]\n    return float(np.mean(lps)) if lps else float(\"nan\")\n\ndef safe_auroc(scores, labels):\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\n    mask = np.isfinite(scores)\n    scores, labels = scores[mask], labels[mask]\n    if len(np.unique(labels)) < 2: return float(\"nan\")\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\n    if n_pos == 0 or n_neg == 0: return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\n    return float(u / (n_pos * n_neg))\n\ndef analyze(instances, subtask):\n    entity_key = \"entities\" if subtask == \"ner\" else \"relations\"\n    valid = [inst for inst in instances if len(inst[\"gold\"].get(entity_key, [])) > 0]\n\n    greedy_f1s = []\n    for inst in valid:\n        greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n        greedy_f1s.append(per_instance_f1(greedy, inst[\"gold\"], subtask=subtask))\n    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\n    conditional_f1s = [f1 for f1 in greedy_f1s if f1 > 0]\n\n    results = {\"n_total\": len(instances), \"n_valid\": len(valid), \"n_conditional\": len(conditional)}\n\n    for split_name, split_insts, split_f1s in [\n        (\"full\", valid, greedy_f1s),\n        (\"cond\", conditional, conditional_f1s),\n    ]:\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\n        sj = cons[\"soft_jaccard\"]\n        fk = cons[\"fleiss_kappa\"]\n\n        lp, em, vc = [], [], []\n        for inst in split_insts:\n            samples = inst[\"samples\"]\n            lp.append(compute_mean_logprob(samples))\n            em.append(compute_exact_match_rate(samples, subtask))\n            vc.append(compute_voting_confidence(samples, subtask))\n\n        signals = {\"sj\": np.array(sj), \"fk\": np.array(fk), \"logprob\": np.array(lp),\n                    \"em\": np.array(em), \"voting_conf\": np.array(vc)}\n        f1_arr = np.array(split_f1s)\n        binary = (f1_arr > 0).astype(int)\n\n        split_res = {\"n\": len(split_insts), \"n_pos\": int(binary.sum()), \"n_neg\": int((1-binary).sum())}\n        for name, vals in signals.items():\n            auroc = safe_auroc(vals, binary)\n            split_res[f\"auroc_{name}\"] = round(auroc, 6) if np.isfinite(auroc) else None\n        results[split_name] = split_res\n    return results\n\ninstances = load_data(DATA_PATH)\nprint(f\"Loaded {len(instances)} instances\")\n\nall_results = {}\nfor subtask in [\"ner\", \"re\"]:\n    print(f\"\\nProcessing {subtask}...\")\n    all_results[subtask] = analyze(instances, subtask)\n    r = all_results[subtask]\n    print(f\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\")\n    for split in [\"full\", \"cond\"]:\n        sr = r[split]\n        print(f\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\")\n        for sig in [\"sj\", \"fk\", \"em\", \"voting_conf\", \"logprob\"]:\n            print(f\"    {sig}: {sr[f'auroc_{sig}']}\")\n\nout_path = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(all_results, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\ncd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python code/eval_exp012_rerun_auroc.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\"\"\"\nimport json, sys\nimport numpy as np\nfrom scipy.stats import spearmanr, rankdata\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\nDATA_PATH = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\"\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\ndef compute_exact_match_rate(samples, subtask):\n    if subtask == \"ner\":\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    else:\n        keys = [frozenset((r[\"head\"], r[\"tail\"], r[\"type\"]) for r in s.get(\"relations\", [])) for s in samples]\n    if not keys: return 0.0\n    c = Counter(keys)\n    return c.most_common(1)[0][1] / len(samples)\n\ndef compute_voting_confidence(samples, subtask):\n    N = len(samples)\n    if N == 0: return 0.0\n    counter = Counter()\n    if subtask == \"ner\":\n        for s in samples:\n            for e in s.get(\"entities\", []):\n                counter[(e[\"text\"], e[\"type\"])] += 1\n    else:\n        for s in samples:\n            for r in s.get(\"relations\", []):\n                counter[(r[\"head\"], r[\"tail\"], r[\"type\"])] += 1\n    if not counter: return 0.0\n    return float(np.mean([v / N for v in counter.values()]))\n\ndef compute_mean_logprob(samples):\n    lps = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    lps = [lp for lp in lps if np.isfinite(lp)]\n    return float(np.mean(lps)) if lps else float(\"nan\")\n\ndef safe_auroc(scores, labels):\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\n    mask = np.isfinite(scores)\n    scores, labels = scores[mask], labels[mask]\n    if len(np.unique(labels)) < 2: return float(\"nan\")\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\n    if n_pos == 0 or n_neg == 0: return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\n    return float(u / (n_pos * n_neg))\n\ndef analyze(instances, subtask):\n    entity_key = \"entities\" if subtask == \"ner\" else \"relations\"\n    valid = [inst for inst in instances if len(inst[\"gold\"].get(entity_key, [])) > 0]\n\n    greedy_f1s = []\n    for inst in valid:\n        greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n        greedy_f1s.append(per_instance_f1(greedy, inst[\"gold\"], subtask=subtask))\n    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\n    conditional_f1s = [f1 for f1 in greedy_f1s if f1 > 0]\n\n    results = {\"n_total\": len(instances), \"n_valid\": len(valid), \"n_conditional\": len(conditional)}\n\n    for split_name, split_insts, split_f1s in [\n        (\"full\", valid, greedy_f1s),\n        (\"cond\", conditional, conditional_f1s),\n    ]:\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\n        sj = cons[\"soft_jaccard\"]\n        fk = cons[\"fleiss_kappa\"]\n\n        lp, em, vc = [], [], []\n        for inst in split_insts:\n            samples = inst[\"samples\"]\n            lp.append(compute_mean_logprob(samples))\n            em.append(compute_exact_match_rate(samples, subtask))\n            vc.append(compute_voting_confidence(samples, subtask))\n\n        signals = {\"sj\": np.array(sj), \"fk\": np.array(fk), \"logprob\": np.array(lp),\n                    \"em\": np.array(em), \"voting_conf\": np.array(vc)}\n        f1_arr = np.array(split_f1s)\n        binary = (f1_arr > 0).astype(int)\n\n        split_res = {\"n\": len(split_insts), \"n_pos\": int(binary.sum()), \"n_neg\": int((1-binary).sum())}\n        for name, vals in signals.items():\n            auroc = safe_auroc(vals, binary)\n            split_res[f\"auroc_{name}\"] = round(auroc, 6) if np.isfinite(auroc) else None\n        results[split_name] = split_res\n    return results\n\ninstances = load_data(DATA_PATH)\nprint(f\"Loaded {len(instances)} instances\")\n\nall_results = {}\nfor subtask in [\"ner\", \"re\"]:\n    print(f\"\\nProcessing {subtask}...\")\n    all_results[subtask] = analyze(instances, subtask)\n    r = all_results[subtask]\n    print(f\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\")\n    for split in [\"full\", \"cond\"]:\n        sr = r[split]\n        print(f\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\")\n        for sig in [\"sj\", \"fk\", \"em\", \"voting_conf\", \"logprob\"]:\n            print(f\"    {sig}: {sr[f'auroc_{sig}']}\")\n\nout_path = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(all_results, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\ncd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python code/eval_exp012_rerun_auroc.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T22:51:54.709312+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 551 instances\\n\\nProcessing ner...\\n  n_valid=529, n_conditional=477\\n  full (n=529, pos=477, neg=52):\\n    sj: 0.717989\\n    fk: 0.747783\\n    em: 0.499819\\n    voting_conf: 0.772093\\n    logprob: 0.654773\\n  cond (n=477, pos=477, neg=0):\\n    sj: None\\n    fk: None\\n    em: None\\n    voting_conf: None\\n    logprob: None\\n\\nProcessing re...\\n  n_valid=397, n_conditional=238\\n  full (n=397, pos=238, neg=159):\\n    sj: 0.609931\\n    fk: 0.663813\\n    em: 0.488597\\n    voting_conf: 0.68202\\n    logprob: 0.67803\\n  cond (n=238, pos=238, neg=0):\\n    sj: None\\n    fk: None\\n    em: None\\n    voting_conf: None\\n    logprob: None\\n\\nSaved to /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T22:51:54.709512+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\"\"\"\nimport json, sys\nimport numpy as np\nfrom scipy.stats import spearmanr, rankdata\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\nDATA_PATH = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\"\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\ndef compute_exact_match_rate(samples, subtask):\n    if subtask == \"ner\":\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    else:\n        keys = [frozenset((r[\"head\"], r[\"tail\"], r[\"type\"]) for r in s.get(\"relations\", [])) for s in samples]\n    if not keys: return 0.0\n    c = Counter(keys)\n    return c.most_common(1)[0][1] / len(samples)\n\ndef compute_voting_confidence(samples, subtask):\n    N = len(samples)\n    if N == 0: return 0.0\n    counter = Counter()\n    if subtask == \"ner\":\n        for s in samples:\n            for e in s.get(\"entities\", []):\n                counter[(e[\"text\"], e[\"type\"])] += 1\n    else:\n        for s in samples:\n            for r in s.get(\"relations\", []):\n                counter[(r[\"head\"], r[\"tail\"], r[\"type\"])] += 1\n    if not counter: return 0.0\n    return float(np.mean([v / N for v in counter.values()]))\n\ndef compute_mean_logprob(samples):\n    lps = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    lps = [lp for lp in lps if np.isfinite(lp)]\n    return float(np.mean(lps)) if lps else float(\"nan\")\n\ndef safe_auroc(scores, labels):\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\n    mask = np.isfinite(scores)\n    scores, labels = scores[mask], labels[mask]\n    if len(np.unique(labels)) < 2: return float(\"nan\")\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\n    if n_pos == 0 or n_neg == 0: return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\n    return float(u / (n_pos * n_neg))\n\ndef analyze(instances, subtask):\n    entity_key = \"entities\" if subtask == \"ner\" else \"relations\"\n    valid = [inst for inst in instances if len(inst[\"gold\"].get(entity_key, [])) > 0]\n\n    greedy_f1s = []\n    for inst in valid:\n        greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n        greedy_f1s.append(per_instance_f1(greedy, inst[\"gold\"], subtask=subtask))\n    \n    conditional_pairs = [(inst, f1) for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\n    conditional_insts = [p[0] for p in conditional_pairs]\n    conditional_f1s = [p[1] for p in conditional_pairs]\n\n    results = {\"n_total\": len(instances), \"n_valid\": len(valid), \"n_conditional\": len(conditional_insts)}\n\n    for split_name, split_insts, split_f1s in [\n        (\"full\", valid, greedy_f1s),\n        (\"cond\", conditional_insts, conditional_f1s),\n    ]:\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\n        sj = cons[\"soft_jaccard\"]\n        fk = cons[\"fleiss_kappa\"]\n\n        lp, em, vc = [], [], []\n        for inst in split_insts:\n            samples = inst[\"samples\"]\n            lp.append(compute_mean_logprob(samples))\n            em.append(compute_exact_match_rate(samples, subtask))\n            vc.append(compute_voting_confidence(samples, subtask))\n\n        signals = {\"sj\": np.array(sj), \"fk\": np.array(fk), \"logprob\": np.array(lp),\n                    \"em\": np.array(em), \"voting_conf\": np.array(vc)}\n        f1_arr = np.array(split_f1s)\n        binary = (f1_arr >= 1.0).astype(int)\n\n        split_res = {\"n\": len(split_insts), \"n_pos\": int(binary.sum()), \"n_neg\": int((1-binary).sum())}\n        for name, vals in signals.items():\n            auroc = safe_auroc(vals, binary)\n            split_res[f\"auroc_{name}\"] = round(auroc, 6) if np.isfinite(auroc) else None\n        results[split_name] = split_res\n    return results\n\ninstances = load_data(DATA_PATH)\nprint(f\"Loaded {len(instances)} instances\")\n\nall_results = {}\nfor subtask in [\"ner\", \"re\"]:\n    print(f\"\\nProcessing {subtask}...\")\n    all_results[subtask] = analyze(instances, subtask)\n    r = all_results[subtask]\n    print(f\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\")\n    for split in [\"full\", \"cond\"]:\n        sr = r[split]\n        print(f\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\")\n        for sig in [\"sj\", \"fk\", \"em\", \"voting_conf\", \"logprob\"]:\n            print(f\"    {sig}: {sr[f'auroc_{sig}']}\")\n\nout_path = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(all_results, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\ncd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python code/eval_exp012_rerun_auroc.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/eval_exp012_rerun_auroc.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Compute 5-signal AUROC for exp_012_rerun_1024 (joint NER+RE).\"\"\"\nimport json, sys\nimport numpy as np\nfrom scipy.stats import spearmanr, rankdata\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\nDATA_PATH = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\"\n\ndef load_data(path):\n    with open(path) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\ndef compute_exact_match_rate(samples, subtask):\n    if subtask == \"ner\":\n        keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    else:\n        keys = [frozenset((r[\"head\"], r[\"tail\"], r[\"type\"]) for r in s.get(\"relations\", [])) for s in samples]\n    if not keys: return 0.0\n    c = Counter(keys)\n    return c.most_common(1)[0][1] / len(samples)\n\ndef compute_voting_confidence(samples, subtask):\n    N = len(samples)\n    if N == 0: return 0.0\n    counter = Counter()\n    if subtask == \"ner\":\n        for s in samples:\n            for e in s.get(\"entities\", []):\n                counter[(e[\"text\"], e[\"type\"])] += 1\n    else:\n        for s in samples:\n            for r in s.get(\"relations\", []):\n                counter[(r[\"head\"], r[\"tail\"], r[\"type\"])] += 1\n    if not counter: return 0.0\n    return float(np.mean([v / N for v in counter.values()]))\n\ndef compute_mean_logprob(samples):\n    lps = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    lps = [lp for lp in lps if np.isfinite(lp)]\n    return float(np.mean(lps)) if lps else float(\"nan\")\n\ndef safe_auroc(scores, labels):\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\n    mask = np.isfinite(scores)\n    scores, labels = scores[mask], labels[mask]\n    if len(np.unique(labels)) < 2: return float(\"nan\")\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\n    if n_pos == 0 or n_neg == 0: return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\n    return float(u / (n_pos * n_neg))\n\ndef analyze(instances, subtask):\n    entity_key = \"entities\" if subtask == \"ner\" else \"relations\"\n    valid = [inst for inst in instances if len(inst[\"gold\"].get(entity_key, [])) > 0]\n\n    greedy_f1s = []\n    for inst in valid:\n        greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n        greedy_f1s.append(per_instance_f1(greedy, inst[\"gold\"], subtask=subtask))\n    \n    conditional_pairs = [(inst, f1) for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\n    conditional_insts = [p[0] for p in conditional_pairs]\n    conditional_f1s = [p[1] for p in conditional_pairs]\n\n    results = {\"n_total\": len(instances), \"n_valid\": len(valid), \"n_conditional\": len(conditional_insts)}\n\n    for split_name, split_insts, split_f1s in [\n        (\"full\", valid, greedy_f1s),\n        (\"cond\", conditional_insts, conditional_f1s),\n    ]:\n        cons = compute_all_consistency_scores(split_insts, subtask=subtask)\n        sj = cons[\"soft_jaccard\"]\n        fk = cons[\"fleiss_kappa\"]\n\n        lp, em, vc = [], [], []\n        for inst in split_insts:\n            samples = inst[\"samples\"]\n            lp.append(compute_mean_logprob(samples))\n            em.append(compute_exact_match_rate(samples, subtask))\n            vc.append(compute_voting_confidence(samples, subtask))\n\n        signals = {\"sj\": np.array(sj), \"fk\": np.array(fk), \"logprob\": np.array(lp),\n                    \"em\": np.array(em), \"voting_conf\": np.array(vc)}\n        f1_arr = np.array(split_f1s)\n        binary = (f1_arr >= 1.0).astype(int)\n\n        split_res = {\"n\": len(split_insts), \"n_pos\": int(binary.sum()), \"n_neg\": int((1-binary).sum())}\n        for name, vals in signals.items():\n            auroc = safe_auroc(vals, binary)\n            split_res[f\"auroc_{name}\"] = round(auroc, 6) if np.isfinite(auroc) else None\n        results[split_name] = split_res\n    return results\n\ninstances = load_data(DATA_PATH)\nprint(f\"Loaded {len(instances)} instances\")\n\nall_results = {}\nfor subtask in [\"ner\", \"re\"]:\n    print(f\"\\nProcessing {subtask}...\")\n    all_results[subtask] = analyze(instances, subtask)\n    r = all_results[subtask]\n    print(f\"  n_valid={r['n_valid']}, n_conditional={r['n_conditional']}\")\n    for split in [\"full\", \"cond\"]:\n        sr = r[split]\n        print(f\"  {split} (n={sr['n']}, pos={sr['n_pos']}, neg={sr['n_neg']}):\")\n        for sig in [\"sj\", \"fk\", \"em\", \"voting_conf\", \"logprob\"]:\n            print(f\"    {sig}: {sr[f'auroc_{sig}']}\")\n\nout_path = \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(all_results, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF\ncd /root/autodl-tmp/struct_self_consist_ie && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python code/eval_exp012_rerun_auroc.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T22:51:54.709701+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 551 instances\\n\\nProcessing ner...\\n  n_valid=529, n_conditional=477\\n  full (n=529, pos=132, neg=397):\\n    sj: 0.691741\\n    fk: 0.628998\\n    em: 0.749265\\n    voting_conf: 0.684099\\n    logprob: 0.578334\\n  cond (n=477, pos=132, neg=345):\\n    sj: 0.677163\\n    fk: 0.607839\\n    em: 0.755578\\n    voting_conf: 0.661814\\n    logprob: 0.563329\\n\\nProcessing re...\\n  n_valid=397, n_conditional=238\\n  full (n=397, pos=76, neg=321):\\n    sj: 0.670233\\n    fk: 0.608932\\n    em: 0.705853\\n    voting_conf: 0.693474\\n    logprob: 0.600467\\n  cond (n=238, pos=76, neg=162):\\n    sj: 0.64628\\n    fk: 0.551048\\n    em: 0.751462\\n    voting_conf: 0.641975\\n    logprob: 0.5186\\n\\nSaved to /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/auroc_5signal.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.85}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T22:51:54.709865+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": "0",
  "fields": "['exp_id', 'status', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "limit": "0",
    "fields": "['exp_id', 'status', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T22:51:54.710702+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"PREPARING\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"PREPARING\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"RUNNING\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"RUNNING\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"RUNNING\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"RUNNING\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"RUNNING\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}}, \"exp_012_rerun_1024\": {\"status\": \"PREPARING\", \"metrics\": {\"ner_full_rho_sj\": 0.36, \"ner_full_rho_fk\": 0.267, \"ner_full_rho_em\": 0.295, \"ner_full_rho_voting_conf\": 0.379, \"ner_full_rho_logprob\": 0.205, \"delta_vs_512\": {\"sj\": 0.003, \"fk\": 0.001, \"em\": 0.038, \"voting_conf\": -0.123, \"logprob\": 0.066}}}, \"exp_001_n16_seed123_full\": {\"status\": \"PREPARING\"}, \"exp_001_n16_seed456_full\": {\"status\": \"PREPARING\"}, \"exp001_seed123\": {\"status\": \"PREPARING\"}, \"exp001_seed456\": {\"status\": \"PREPARING\"}, \"exp_007_ner_llama\": {\"status\": \"PREPARING\"}, \"exp_002_merge_conll2003\": {\"status\": \"PREPARING\"}, \"exp008_re_n16\": {\"status\": \"PREPARING\"}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, 
…[truncated 38200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T22:51:54.710951+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_012_rerun_1024",
  "field": "metrics",
  "value": "{'ner_full_rho_sj': 0.36, 'ner_full_rho_fk': 0.267, 'ner_full_rho_em': 0.295, 'ner_full_rho_voting_conf': 0.379, 'ner_full_rho_logprob': 0.205, 'ner_auroc_sj': 0.6917, 'ner_auroc_fk': 0.629, 'ner_auroc_em': 0.7493, 'ner_auroc_voting_conf': 0.6841, 'ner_auroc_logprob': 0.5783, 'ner_auroc_sj_cond': 0.6772, 'ner_auroc_fk_cond': 0.6078, 'ner_auroc_em_cond': 0.7556, 'ner_auroc_voting_conf_cond': 0.6618, 'ner_auroc_logprob_cond': 0.5633, 're_auroc_sj': 0.6702, 're_auroc_fk': 0.6089, 're_auroc_em': 0.7059, 're_auroc_voting_conf': 0.6935, 're_auroc_logprob': 0.6005, 're_auroc_sj_cond': 0.6463, 're_auroc_fk_cond': 0.551, 're_auroc_em_cond': 0.7515, 're_auroc_voting_conf_cond': 0.642, 're_auroc_logprob_cond': 0.5186, 'auroc_note': 'binary=F1>=1.0, full=gold_nonempty, cond=greedy_F1>0', 'ner_full_n': 529, 'ner_cond_n': 477, 're_full_n': 397, 're_cond_n': 238, 'delta_vs_512': {'sj': 0.003, 'fk': 0.001, 'em': 0.038, 'voting_conf': -0.123, 'logprob': 0.066}}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_012_rerun_1024",
    "field": "metrics",
    "value": "{'ner_full_rho_sj': 0.36, 'ner_full_rho_fk': 0.267, 'ner_full_rho_em': 0.295, 'ner_full_rho_voting_conf': 0.379, 'ner_full_rho_logprob': 0.205, 'ner_auroc_sj': 0.6917, 'ner_auroc_fk': 0.629, 'ner_auroc_em': 0.7493, 'ner_auroc_voting_conf': 0.6841, 'ner_auroc_logprob': 0.5783, 'ner_auroc_sj_cond': 0.6772, 'ner_auroc_fk_cond': 0.6078, 'ner_auroc_em_cond': 0.7556, 'ner_auroc_voting_conf_cond': 0.6618, 'ner_auroc_logprob_cond': 0.5633, 're_auroc_sj': 0.6702, 're_auroc_fk': 0.6089, 're_auroc_em': 0.7059, 're_auroc_voting_conf': 0.6935, 're_auroc_logprob': 0.6005, 're_auroc_sj_cond': 0.6463, 're_auroc_fk_cond': 0.551, 're_auroc_em_cond': 0.7515, 're_auroc_voting_conf_cond': 0.642, 're_auroc_logprob_cond': 0.5186, 'auroc_note': 'binary=F1>=1.0, full=gold_nonempty, cond=greedy_F1>0', 'ner_full_n': 529, 'ner_cond_n': 477, 're_full_n': 397, 're_cond_n': 238, 'delta_vs_512': {'sj': 0.003, 'fk': 0.001, 'em': 0.038, 'voting_conf': -0.123, 'logprob': 0.066}}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T22:51:54.711172+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_012_rerun_1024\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-14T22:51:47.276Z\", \"spec\": {\"hypothesis\": \"Verify if max_tokens=512 truncation inflated Table 1 N=8 SciERC signal values. Rerun with max_tokens=1024 for clean comparison.\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"parent\": \"exp_012_logprob_baseline\", \"data_count\": 551, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024\", \"checkpoint_path\": \"output/exp_012_rerun_1024/\", \"log_path\": \"output/exp_012_rerun_1024/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"ner_full_rho_sj\": 0.36, \"ner_full_rho_fk\": 0.267, \"ner_full_rho_em\": 0.295, \"ner_full_rho_voting_conf\": 0.379, \"ner_full_rho_logprob\": 0.205, \"ner_auroc_sj\": 0.6917, \"ner_auroc_fk\": 0.629, \"ner_auroc_em\": 0.7493, \"ner_auroc_voting_conf\": 0.6841, \"ner_auroc_logprob\": 0.5783, \"ner_auroc_sj_cond\": 0.6772, \"ner_auroc_fk_cond\": 0.6078, \"ner_auroc_em_cond\": 0.7556, \"ner_auroc_voting_conf_cond\": 0.6618, \"ner_auroc_logprob_cond\": 0.5633, \"re_auroc_sj\": 0.6702, \"re_auroc_fk\": 0.6089, \"re_auroc_em\": 0.7059, \"re_auroc_voting_conf\": 0.6935, \"re_auroc_logprob\": 0.6005, \"re_auroc_sj_cond\": 0.6463, \"re_auroc_fk_cond\": 0.551, \"re_auroc_em_cond\": 0.7515, \"re_auroc_voting_conf_cond\": 0.642, \"re_auroc_logprob_cond\": 0.5186, \"auroc_note\": \"binary=F1>=1.0, full=gold_nonempty, cond=greedy_F1>0\", \"ner_full_n\": 529, \"ner_cond_n\": 477, \"re_full_n\": 397, \"re_cond_n\": 238, \"delta_vs_512\": {\"sj\": 0.
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T22:51:54.711371+00:00_

Registry 已更新。以下是 exp_012_rerun_1024 的 5-signal AUROC 完整结果（binary threshold: F1≥1.0）：

### NER

| Signal | Full (n=529) | Conditional (n=477) |
|--------|-------------|---------------------|
| **EM** | **0.7493** | **0.7556** |
| SJ | 0.6917 | 0.6772 |
| voting_conf | 0.6841 | 0.6618 |
| FK | 0.6290 | 0.6078 |
| logprob | 0.5783 | 0.5633 |

### RE

| Signal | Full (n=397) | Conditional (n=238) |
|--------|-------------|---------------------|
| **EM** | **0.7059** | **0.7515** |
| voting_conf | 0.6935 | 0.6420 |
| SJ | 0.6702 | 0.6463 |
| FK | 0.6089 | 0.5510 |
| logprob | 0.6005 | 0.5186 |

EM 在所有 split 上 AUROC 最高。结构化信号（SJ、voting_conf、EM）全部优于 logprob baseline。排序稳定：EM > voting_conf ≈ SJ > FK > logprob。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp012_r1024_auroc_20260514T224900"
}
```

</details>

---
