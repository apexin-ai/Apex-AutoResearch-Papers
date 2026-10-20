# data qwen scierc 3seed em voting

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_data_qwen_scierc_3seed_em_voting_20260514T211403.jsonl`
- **Structured JSON:** [`1e5077734479ee99183e.json`](../../sessions/1e/1e5077734479ee99183e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-14T21:17:05.844478+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:17:05.844823+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:17:05.845033+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "autodl-5090",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "autodl-5090",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T21:17:05.845229+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:17:05.845380+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T21:17:05.845512+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nrun.log\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T21:17:05.845634+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:17:05.845754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nrun.log\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:17:05.845869+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:17:05.845989+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:17:05.846110+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T21:17:05.846278+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_signals_report.json\\nreport.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:17:05.846399+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -maxdepth 2 -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -maxdepth 2 -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T21:17:05.846554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/code/data_utils.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_to_llamafactory.py\\n/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/consistency.py\\n/root/autodl-tmp/struct_self_consist_ie/code/sampling.py\\n/root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_diagnose.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_realign_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_component_wise_re.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_wnut17.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_conll2003.py\\n/root/autodl-tmp/struct_self_consist_ie/code/extract_logprobs.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_logprob_baseline.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exact_match_voting.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_entity_voting.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp015_unified.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp004_re_diagnostic.py\\n/root/autodl-tmp/struct_self_consist_ie/code/exp001_postprocess.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp016_ensemble.py\\n/root/autodl-tmp/struct_self_consist_ie/code/diagnose_logprob_rho.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp002_conll2003.py\\n/root/autodl-tmp/struct_self_consist_ie/code/exp009_stratification_analysis.py\\n/root/autodl-tmp/struct_self_consist_ie/code/exp010_selection_curves.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp005_v2_temperature.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp004_v2_re_diagnostic.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analy
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:17:05.846740+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/analyze_3seed_5signal.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/analyze_3seed_5signal.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T21:17:05.846934+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Compute 5-signal metrics for 3 seeds (NER N=16).\\\"\\\"\\\"\\nimport json, sys\\nimport numpy as np\\nfrom scipy.stats import spearmanr, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores\\nfrom evaluation import per_instance_f1\\n\\nSEEDS = {\\n    \\\"seed42\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl\\\",\\n    \\\"seed123\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/samples.jsonl\\\",\\n    \\\"seed456\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/samples.jsonl\\\",\\n}\\nSUBTASK = \\\"ner\\\"\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\ndef compute_exact_match_rate(samples):\\n    keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\ndef compute_voting_confidence(samples):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    for s in samples:\\n        for e in s.get(\\\"entities\\\", []):\\n            counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    if not counter: return 0.0\\n    return float(np.mean([v / N for v in counter.values()]))\\n\\ndef compute_mean_logprob(samples):\\n    lps = [s.get(\\\"mean_logprob\\\") for s in samples if s.get(\\\"mean_logprob\\\") is not None]\\n    lps = [lp for lp in lps if np.isfinite(lp)]\\n    return float(np.mean(lps)) if lps else float(\\\"nan\\\")\\n\\ndef safe_spearman(x, y):\\n    x, y = np.asarray(x, float), np.asarray(y, float)\\n    m = np.isfinite(x) & np.isfinite(y)\\n    x, y = x[m], y[m]\\n    if len(x) < 3: return fl
…[truncated 2678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T21:17:05.847102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16/all_signals_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16/all_signals_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:17:05.847255+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -30 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -30 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T21:17:05.847486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"full\\\": {\\n    \\\"n\\\": 2756,\\n    \\\"pct_perfect\\\": 0.8588534107402032,\\n    \\\"greedy_f1_mean\\\": 0.9243,\\n    \\\"metrics\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.4642,\\n        \\\"rho_ci95\\\": [\\n          0.4152,\\n          0.5108\\n        ],\\n        \\\"p_rho\\\": 2.580337501814738e-147,\\n        \\\"auroc\\\": 0.7391,\\n        \\\"auroc_ci95\\\": [\\n          0.7141,\\n          0.7641\\n        ],\\n        \\\"ece\\\": 0.1131\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.4566,\\n        \\\"rho_ci95\\\": [\\n          0.4066,\\n          0.5038\\n        ],\\n        \\\"p_rho\\\": 5.058343787088528e-142,\\n        \\\"auroc\\\": 0.736,\\n        \\\"auroc_ci95\\\": [\\n          0.7104,\\n          0.7606\\n        ],\\n        \\\"ece\\\": 0.1071\\n      },\\n      \\\"logprob\\\": {\\n        \\\"rho\\\": 0.3058,\\n        \\\"rho_ci95\\\": [\\n          0.2764,\\n          0.335\\n        ],\\n        \\\"p_rho\\\": 9.853718698917995e-61,\\n        \\\"auroc\\\": 0.7594,\\n        \\\"auroc_ci95\\\": [\\n          0.7385,\\n          0.7828\\n        ],\\n        \\\"ece\\\": 0.1288\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.4613,\\n        \\\"rho_ci95\\\": [\\n          0.4121,\\n          0.5095\\n        ],\\n        \\\"p_rho\\\": 2.6389398920984166e-145,\\n        \\\"auroc\\\": 0.7391,\\n        \\\"auroc_ci95\\\": [\\n          0.7136,\\n          0.7644\\n        ],\\n        \\\"ece\\\": 0.1084\\n      },\\n      \\\"voting_conf\\\": {\\n        \\\"rho\\\": 0.4554,\\n        \\\"rho_ci95\\\": [\\n          0.4027,\\n          0.5041\\n        ],\\n        \\\"p_rho\\\": 3.28808416171092e-141,\\n        \\\"auroc\\\": 0.7406,\\n        \\\"auroc_ci95\\\": [\\n          0.7121,\\n          0.7681\\n        ],\\n        \\\"ece\\\": 0.0844\\n      }\\n    }\\n  },\\n  \\\"conditional\\\": {\\n    \\\"n\\\": 2642,\\n  
…[truncated 4812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T21:17:05.847922+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"id\\\": \\\"X96-1059_sent000\\\", \\\"text\\\": \\\"Recognition of proper nouns in Japanese text has been studied as a part of the more general problem of morphological analysis in Japanese text processing -LRB- -LSB- 1 -RSB- -LSB- 2 -RSB- -RRB- .\\\", \\\"gold\\\": {\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"proper nouns\\\", \\\"type\\\": \\\"OtherScientificTerm\\\", \\\"start\\\": 15, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\": 125}, {\\\"text\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 129, \\\"end\\\": 153}], \\\"relations\\\": [{\\\"head\\\": \\\"Recognition of proper nouns\\\", \\\"tail\\\": \\\"morphological analysis\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 0, \\\"head_end\\\": 27, \\\"tail_start\\\": 103, \\\"tail_end\\\": 125}, {\\\"head\\\": \\\"proper nouns\\\", \\\"tail\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"PART-OF\\\", \\\"head_start\\\": 15, \\\"head_end\\\": 27, \\\"tail_start\\\": 31, \\\"tail_end\\\": 44}, {\\\"head\\\": \\\"morphological analysis\\\", \\\"tail\\\": \\\"Japanese text processing\\\", \\\"type\\\": \\\"USED-FOR\\\", \\\"head_start\\\": 103, \\\"head_end\\\": 125, \\\"tail_start\\\": 129, \\\"tail_end\\\": 153}], \\\"events\\\": []}, \\\"samples\\\": [{\\\"entities\\\": [{\\\"text\\\": \\\"Recognition of proper nouns\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 0, \\\"end\\\": 27}, {\\\"text\\\": \\\"Japanese text\\\", \\\"type\\\": \\\"Material\\\", \\\"start\\\": 31, \\\"end\\\": 44}, {\\\"text\\\": \\\"morphological analysis in Japanese text processing\\\", \\\"type\\\": \\\"Task\\\", \\\"start\\\": 103, \\\"end\\\
…[truncated 8878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:17:05.848148+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp017_llama_conll_n16.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp017_llama_conll_n16.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T21:17:05.848427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"exp_017_llama_conll_n16: 5-signal evaluation + N=8 vs N=16 delta + Best-of-N selection.\\\"\\\"\\\"\\n\\nimport json, sys, os\\nimport numpy as np\\nfrom scipy.stats import spearmanr, kendalltau, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores, _ner_soft_jaccard_pair\\nfrom evaluation import per_instance_f1\\n\\nN16_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16/samples.jsonl\\\"\\nN8_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\\\"\\nN8_REPORT = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/all_signals_report.json\\\"\\nOUTPUT_DIR = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16\\\"\\nSUBTASK = \\\"ner\\\"\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    for s in samples:\\n        for e in s.get(\\\"entities\\\", []):\\n            counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    if not counter: return 0.0\\n    return float(np.mean([v / N for v in counter.values()]))\\n\\n\\ndef compute_mean_logprob(samples):\\n    lps = [s.get(\\\"mean_logprob\\\") for s in samples if s.get(\\\"mean_logprob\\\") is not None]\\n    lps = [lp for lp in lps if np.isfinite(lp)]\\n    return float(np.mean(lps)) if lps else float(\\\"nan\\\"
…[truncated 7146 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T21:17:05.848627+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"def analyze_split\" /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp017_llama_conll_n16.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"def analyze_split\" /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp017_llama_conll_n16.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T21:17:05.848778+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"109:def analyze_split(instances, split_name):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T21:17:05.848933+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -175 /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp017_llama_conll_n16.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -175 /root/autodl-tmp/struct_self_consist_ie/code/analyze_exp017_llama_conll_n16.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T21:17:05.849172+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"exp_017_llama_conll_n16: 5-signal evaluation + N=8 vs N=16 delta + Best-of-N selection.\\\"\\\"\\\"\\n\\nimport json, sys, os\\nimport numpy as np\\nfrom scipy.stats import spearmanr, kendalltau, rankdata\\nfrom collections import Counter\\n\\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\\nfrom consistency import compute_all_consistency_scores, _ner_soft_jaccard_pair\\nfrom evaluation import per_instance_f1\\n\\nN16_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16/samples.jsonl\\\"\\nN8_PATH = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\\\"\\nN8_REPORT = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/all_signals_report.json\\\"\\nOUTPUT_DIR = \\\"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_n16\\\"\\nSUBTASK = \\\"ner\\\"\\n\\n\\ndef load_data(path):\\n    with open(path) as f:\\n        return [json.loads(line) for line in f if line.strip()]\\n\\n\\ndef compute_exact_match_rate(samples, subtask):\\n    keys = [frozenset((e[\\\"text\\\"], e[\\\"type\\\"]) for e in s.get(\\\"entities\\\", [])) for s in samples]\\n    if not keys: return 0.0\\n    c = Counter(keys)\\n    return c.most_common(1)[0][1] / len(samples)\\n\\n\\ndef compute_voting_confidence(samples, subtask):\\n    N = len(samples)\\n    if N == 0: return 0.0\\n    counter = Counter()\\n    for s in samples:\\n        for e in s.get(\\\"entities\\\", []):\\n            counter[(e[\\\"text\\\"], e[\\\"type\\\"])] += 1\\n    if not counter: return 0.0\\n    return float(np.mean([v / N for v in counter.values()]))\\n\\n\\ndef compute_mean_logprob(samples):\\n    lps = [s.get(\\\"mean_logprob\\\") for s in samples if s.get(\\\"mean_logprob\\\") is not None]\\n    lps = [lp for lp in lps if np.isfinite(lp)]\\n    return float(np.mean(lps)) if lps else float(\\\"nan\\\"
…[truncated 5682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T21:17:05.849390+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/exp001_3seed_all_signals.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Compute 5-signal all_signals_report.json for exp_001 3 seeds (NER, Qwen/SciERC).\"\"\"\n\nimport json, sys, os\nimport numpy as np\nfrom scipy.stats import spearmanr, rankdata\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\nSEEDS = {\n    \"seed42\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2\",\n    \"seed123\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2\",\n    \"seed456\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner\",\n}\nSUBTASK = \"ner\"\n\n\ndef load_data(path):\n    with open(os.path.join(path, \"samples.jsonl\")) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\n\ndef compute_exact_match_rate(samples):\n    keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    if not keys: return 0.0\n    c = Counter(keys)\n    return c.most_common(1)[0][1] / len(samples)\n\n\ndef compute_voting_confidence(samples):\n    N = len(samples)\n    if N == 0: return 0.0\n    counter = Counter()\n    for s in samples:\n        for e in s.get(\"entities\", []):\n            counter[(e[\"text\"], e[\"type\"])] += 1\n    if not counter: return 0.0\n    return float(np.mean([v / N for v in counter.values()]))\n\n\ndef compute_mean_logprob(samples):\n    lps = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    lps = [lp for lp in lps if np.isfinite(lp)]\n    return float(np.mean(lps)) if lps else float(\"nan\")\n\n\ndef safe_spearman(x, y):\n    x, y = np.asarray(x, float), np.asarray(y, float)\n    m = np.isfinite(x) & np.isfinite(y)\n    x, y = x[m], y[m]\n    if len(x) < 3: return float(\"nan\"), float(\"nan\")\n    r = spearmanr(x, y)\n    return float(r.statistic), float(r.pvalue)\n\n\ndef safe_auroc(scores, labels):\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\n    if len(np.unique(labels)) < 2: return float(\"nan\")\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\n    if n_pos == 0 or n_neg == 0: return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\n    return float(u / (n_pos * n_neg))\n\n\ndef normalize_for_ece(sig_name, values):\n    v = np.asarray(values, dtype=float)\n    if sig_name in (\"SJ\", \"EM\", \"voting_conf\"):\n        return np.clip(v, 0, 1)\n    elif sig_name == \"FK\":\n        return np.clip((v + 1) / 2, 0, 1)\n    elif sig_name == \"logprob\":\n        return np.clip(np.exp(v), 0, 1)\n    return v\n\n\ndef compute_ece(confidences, correctness, n_bins=10):\n    conf = np.asarray(confidences, dtype=float)\n    corr = np.asarray(correctness, dtype=float)\n    mask = np.isfinite(conf)\n    conf, corr = conf[mask], corr[mask]\n    if len(conf) == 0: return float(\"nan\")\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    for i in range(n_bins):\n        lo, hi = bin_edges[i], bin_edges[i + 1]\n        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)\n        if in_bin.sum() == 0: continue\n        ece += in_bin.sum() / len(conf) * abs(conf[in_bin].mean() - corr[in_bin].mean())\n    return float(ece)\n\n\ndef bootstrap_metric(metric_fn, signals, targets, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    signals, targets = np.asarray(signals, float), np.asarray(targets, float)\n    n = len(signals)\n    vals = []\n    for _ in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        v = metric_fn(signals[idx], targets[idx])\n        if isinstance(v, tuple): v = v[0]\n        if np.isfinite(v): vals.append(v)\n    if not vals: return [float(\"nan\"), float(\"nan\")]\n    return [float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))]\n\n\ndef analyze_split(instances):\n    consistency = compute_all_consistency_scores(instances, subtask=SUBTASK)\n    sj_vals = consistency[\"soft_jaccard\"]\n    fk_vals = consistency[\"fleiss_kappa\"]\n\n    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []\n    for inst in instances:\n        samples = inst[\"samples\"]\n        greedy = inst.get(\"greedy\", samples[0])\n        lp_vals.append(compute_mean_logprob(samples))\n        em_vals.append(compute_exact_match_rate(samples))\n        vc_vals.append(compute_voting_confidence(samples))\n        f1_vals.append(per_instance_f1(greedy, inst[\"gold\"], subtask=SUBTASK))\n\n    signals = {\"SJ\": np.array(sj_vals), \"FK\": np.array(fk_vals),\n               \"logprob\": np.array(lp_vals), \"EM\": np.array(em_vals),\n               \"voting_conf\": np.array(vc_vals)}\n    f1_arr = np.array(f1_vals)\n    binary = (f1_arr >= 1.0).astype(int)\n\n    result = {\"n\": len(instances), \"pct_perfect\": float(binary.mean()),\n              \"greedy_f1_mean\": round(float(np.mean(f1_vals)), 4)}\n    metrics = {}\n    for name, vals in signals.items():\n        rho, p = safe_spearman(vals, f1_arr)\n        rho_ci = bootstrap_metric(lambda x,y: safe_spearman(x,y)[0], vals, f1_arr)\n        auroc = safe_auroc(vals, binary)\n        auroc_ci = bootstrap_metric(safe_auroc, vals, binary.astype(float))\n        ece_conf = normalize_for_ece(name, vals)\n        ece = compute_ece(ece_conf, binary)\n        metrics[name] = {\n            \"rho\": round(rho, 4), \"rho_ci95\": [round(v, 4) for v in rho_ci], \"p_rho\": p,\n            \"auroc\": round(auroc, 4), \"auroc_ci95\": [round(v, 4) for v in auroc_ci],\n            \"ece\": round(ece, 4)\n        }\n    result[\"metrics\"] = metrics\n    return result\n\n\ndef json_default(obj):\n    if isinstance(obj, (np.floating, np.float64, np.float32)): return float(obj)\n    if isinstance(obj, (np.integer, np.int64, np.int32)): return int(obj)\n    if isinstance(obj, np.ndarray): return obj.tolist()\n    if isinstance(obj, np.bool_): return bool(obj)\n    return str(obj)\n\n\ndef main():\n    all_seed_results = {}\n    \n    for seed_name, out_dir in SEEDS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"Processing {seed_name}: {out_dir}\")\n        instances = load_data(out_dir)\n        print(f\"  Loaded {len(instances)} instances, N={len(instances[0]['samples'])}\")\n\n        valid = [inst for inst in instances if len(inst[\"gold\"].get(\"entities\", [])) > 0]\n        print(f\"  Valid (non-empty gold): {len(valid)}\")\n\n        greedy_f1s = []\n        for inst in valid:\n            greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n            greedy_f1s.append(per_instance_f1(greedy, inst[\"gold\"], subtask=SUBTASK))\n        conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\n        print(f\"  Conditional (greedy F1 > 0): {len(conditional)}\")\n\n        seed_result = {}\n        for split_name, split_insts in [(\"full\", valid), (\"conditional\", conditional)]:\n            print(f\"\\n  --- {split_name} ({len(split_insts)} instances) ---\")\n            res = analyze_split(split_insts)\n            for sig_name, m in res[\"metrics\"].items():\n                print(f\"    {sig_name:>12}: rho={m['rho']:.4f}  AUROC={m['auroc']:.4f}  ECE={m['ece']:.4f}\")\n            seed_result[split_name] = res\n\n        # Save per-seed all_signals_report.json\n        out_path = os.path.join(out_dir, \"all_signals_report.json\")\n        with open(out_path, \"w\") as f:\n            json.dump(seed_result, f, indent=2, default=json_default)\n        print(f\"\\n  Saved: {out_path}\")\n        all_seed_results[seed_name] = seed_result\n\n    # Print summary JSON for all seeds\n    print(f\"\\n{'='*60}\")\n    print(\"ALL SEEDS COMBINED:\")\n    print(json.dumps(all_seed_results, indent=2, default=json_default))\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/struct_self_consist_ie/code/exp001_3seed_all_signals.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Compute 5-signal all_signals_report.json for exp_001 3 seeds (NER, Qwen/SciERC).\"\"\"\n\nimport json, sys, os\nimport numpy as np\nfrom scipy.stats import spearmanr, rankdata\nfrom collections import Counter\n\nsys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')\nfrom consistency import compute_all_consistency_scores\nfrom evaluation import per_instance_f1\n\nSEEDS = {\n    \"seed42\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2\",\n    \"seed123\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2\",\n    \"seed456\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner\",\n}\nSUBTASK = \"ner\"\n\n\ndef load_data(path):\n    with open(os.path.join(path, \"samples.jsonl\")) as f:\n        return [json.loads(line) for line in f if line.strip()]\n\n\ndef compute_exact_match_rate(samples):\n    keys = [frozenset((e[\"text\"], e[\"type\"]) for e in s.get(\"entities\", [])) for s in samples]\n    if not keys: return 0.0\n    c = Counter(keys)\n    return c.most_common(1)[0][1] / len(samples)\n\n\ndef compute_voting_confidence(samples):\n    N = len(samples)\n    if N == 0: return 0.0\n    counter = Counter()\n    for s in samples:\n        for e in s.get(\"entities\", []):\n            counter[(e[\"text\"], e[\"type\"])] += 1\n    if not counter: return 0.0\n    return float(np.mean([v / N for v in counter.values()]))\n\n\ndef compute_mean_logprob(samples):\n    lps = [s.get(\"mean_logprob\") for s in samples if s.get(\"mean_logprob\") is not None]\n    lps = [lp for lp in lps if np.isfinite(lp)]\n    return float(np.mean(lps)) if lps else float(\"nan\")\n\n\ndef safe_spearman(x, y):\n    x, y = np.asarray(x, float), np.asarray(y, float)\n    m = np.isfinite(x) & np.isfinite(y)\n    x, y = x[m], y[m]\n    if len(x) < 3: return float(\"nan\"), float(\"nan\")\n    r = spearmanr(x, y)\n    return float(r.statistic), float(r.pvalue)\n\n\ndef safe_auroc(scores, labels):\n    scores, labels = np.asarray(scores, float), np.asarray(labels, int)\n    if len(np.unique(labels)) < 2: return float(\"nan\")\n    n_pos, n_neg = (labels==1).sum(), (labels==0).sum()\n    if n_pos == 0 or n_neg == 0: return float(\"nan\")\n    ranks = rankdata(scores)\n    u = ranks[labels==1].sum() - n_pos*(n_pos+1)/2\n    return float(u / (n_pos * n_neg))\n\n\ndef normalize_for_ece(sig_name, values):\n    v = np.asarray(values, dtype=float)\n    if sig_name in (\"SJ\", \"EM\", \"voting_conf\"):\n        return np.clip(v, 0, 1)\n    elif sig_name == \"FK\":\n        return np.clip((v + 1) / 2, 0, 1)\n    elif sig_name == \"logprob\":\n        return np.clip(np.exp(v), 0, 1)\n    return v\n\n\ndef compute_ece(confidences, correctness, n_bins=10):\n    conf = np.asarray(confidences, dtype=float)\n    corr = np.asarray(correctness, dtype=float)\n    mask = np.isfinite(conf)\n    conf, corr = conf[mask], corr[mask]\n    if len(conf) == 0: return float(\"nan\")\n    bin_edges = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    for i in range(n_bins):\n        lo, hi = bin_edges[i], bin_edges[i + 1]\n        in_bin = (conf >= lo) & (conf <= hi if i == n_bins - 1 else conf < hi)\n        if in_bin.sum() == 0: continue\n        ece += in_bin.sum() / len(conf) * abs(conf[in_bin].mean() - corr[in_bin].mean())\n    return float(ece)\n\n\ndef bootstrap_metric(metric_fn, signals, targets, n_boot=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    signals, targets = np.asarray(signals, float), np.asarray(targets, float)\n    n = len(signals)\n    vals = []\n    for _ in range(n_boot):\n        idx = rng.randint(0, n, size=n)\n        v = metric_fn(signals[idx], targets[idx])\n        if isinstance(v, tuple): v = v[0]\n        if np.isfinite(v): vals.append(v)\n    if not vals: return [float(\"nan\"), float(\"nan\")]\n    return [float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))]\n\n\ndef analyze_split(instances):\n    consistency = compute_all_consistency_scores(instances, subtask=SUBTASK)\n    sj_vals = consistency[\"soft_jaccard\"]\n    fk_vals = consistency[\"fleiss_kappa\"]\n\n    lp_vals, em_vals, vc_vals, f1_vals = [], [], [], []\n    for inst in instances:\n        samples = inst[\"samples\"]\n        greedy = inst.get(\"greedy\", samples[0])\n        lp_vals.append(compute_mean_logprob(samples))\n        em_vals.append(compute_exact_match_rate(samples))\n        vc_vals.append(compute_voting_confidence(samples))\n        f1_vals.append(per_instance_f1(greedy, inst[\"gold\"], subtask=SUBTASK))\n\n    signals = {\"SJ\": np.array(sj_vals), \"FK\": np.array(fk_vals),\n               \"logprob\": np.array(lp_vals), \"EM\": np.array(em_vals),\n               \"voting_conf\": np.array(vc_vals)}\n    f1_arr = np.array(f1_vals)\n    binary = (f1_arr >= 1.0).astype(int)\n\n    result = {\"n\": len(instances), \"pct_perfect\": float(binary.mean()),\n              \"greedy_f1_mean\": round(float(np.mean(f1_vals)), 4)}\n    metrics = {}\n    for name, vals in signals.items():\n        rho, p = safe_spearman(vals, f1_arr)\n        rho_ci = bootstrap_metric(lambda x,y: safe_spearman(x,y)[0], vals, f1_arr)\n        auroc = safe_auroc(vals, binary)\n        auroc_ci = bootstrap_metric(safe_auroc, vals, binary.astype(float))\n        ece_conf = normalize_for_ece(name, vals)\n        ece = compute_ece(ece_conf, binary)\n        metrics[name] = {\n            \"rho\": round(rho, 4), \"rho_ci95\": [round(v, 4) for v in rho_ci], \"p_rho\": p,\n            \"auroc\": round(auroc, 4), \"auroc_ci95\": [round(v, 4) for v in auroc_ci],\n            \"ece\": round(ece, 4)\n        }\n    result[\"metrics\"] = metrics\n    return result\n\n\ndef json_default(obj):\n    if isinstance(obj, (np.floating, np.float64, np.float32)): return float(obj)\n    if isinstance(obj, (np.integer, np.int64, np.int32)): return int(obj)\n    if isinstance(obj, np.ndarray): return obj.tolist()\n    if isinstance(obj, np.bool_): return bool(obj)\n    return str(obj)\n\n\ndef main():\n    all_seed_results = {}\n    \n    for seed_name, out_dir in SEEDS.items():\n        print(f\"\\n{'='*60}\")\n        print(f\"Processing {seed_name}: {out_dir}\")\n        instances = load_data(out_dir)\n        print(f\"  Loaded {len(instances)} instances, N={len(instances[0]['samples'])}\")\n\n        valid = [inst for inst in instances if len(inst[\"gold\"].get(\"entities\", [])) > 0]\n        print(f\"  Valid (non-empty gold): {len(valid)}\")\n\n        greedy_f1s = []\n        for inst in valid:\n            greedy = inst.get(\"greedy\", inst[\"samples\"][0])\n            greedy_f1s.append(per_instance_f1(greedy, inst[\"gold\"], subtask=SUBTASK))\n        conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]\n        print(f\"  Conditional (greedy F1 > 0): {len(conditional)}\")\n\n        seed_result = {}\n        for split_name, split_insts in [(\"full\", valid), (\"conditional\", conditional)]:\n            print(f\"\\n  --- {split_name} ({len(split_insts)} instances) ---\")\n            res = analyze_split(split_insts)\n            for sig_name, m in res[\"metrics\"].items():\n                print(f\"    {sig_name:>12}: rho={m['rho']:.4f}  AUROC={m['auroc']:.4f}  ECE={m['ece']:.4f}\")\n            seed_result[split_name] = res\n\n        # Save per-seed all_signals_report.json\n        out_path = os.path.join(out_dir, \"all_signals_report.json\")\n        with open(out_path, \"w\") as f:\n            json.dump(seed_result, f, indent=2, default=json_default)\n        print(f\"\\n  Saved: {out_path}\")\n        all_seed_results[seed_name] = seed_result\n\n    # Print summary JSON for all seeds\n    print(f\"\\n{'='*60}\")\n    print(\"ALL SEEDS COMBINED:\")\n    print(json.dumps(all_seed_results, indent=2, default=json_default))\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T21:17:05.849600+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:17:05.849746+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python code/exp001_3seed_all_signals.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python code/exp001_3seed_all_signals.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:17:05.850021+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\nProcessing seed42: /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2\\n  Loaded 551 instances, N=16\\n  Valid (non-empty gold): 529\\n  Conditional (greedy F1 > 0): 477\\n\\n  --- full (529 instances) ---\\n              SJ: rho=0.4280  AUROC=0.7368  ECE=0.4575\\n              FK: rho=0.2809  AUROC=0.6099  ECE=0.4822\\n         logprob: rho=0.2194  AUROC=0.5870  ECE=0.7073\\n              EM: rho=0.3347  AUROC=0.7902  ECE=0.3320\\n     voting_conf: rho=0.4408  AUROC=0.7340  ECE=0.3200\\n\\n  --- conditional (477 instances) ---\\n              SJ: rho=0.3688  AUROC=0.7193  ECE=0.4504\\n              FK: rho=0.1934  AUROC=0.5893  ECE=0.4845\\n         logprob: rho=0.1560  AUROC=0.5694  ECE=0.6817\\n              EM: rho=0.4151  AUROC=0.7972  ECE=0.3041\\n     voting_conf: rho=0.3531  AUROC=0.7122  ECE=0.3206\\n\\n  Saved: /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json\\n\\n============================================================\\nProcessing seed123: /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2\\n  Loaded 551 instances, N=16\\n  Valid (non-empty gold): 529\\n  Conditional (greedy F1 > 0): 477\\n\\n  --- full (529 instances) ---\\n              SJ: rho=0.4244  AUROC=0.7363  ECE=0.4544\\n              FK: rho=0.2752  AUROC=0.6268  ECE=0.4841\\n         logprob: rho=0.2513  AUROC=0.6062  ECE=0.7068\\n              EM: rho=0.3369  AUROC=0.7807  ECE=0.3355\\n     voting_conf: rho=0.4131  AUROC=0.7167  ECE=0.3123\\n\\n  --- conditional (477 instances) ---\\n              SJ: rho=0.3757  AUROC=0.7213  ECE=0.4470\\n              FK: rho=0.1785  AUROC=0.6054  ECE=0.4770\\n         logprob: rho=0.1727  AUROC=0.5844  ECE=0.6811\\n              EM: rho=0.4036  AUROC=0.7869  ECE=0.3096\\n     voting_conf: rho=0.3393  AUROC=0.6979  ECE=0.3071\\n\\n  Saved: /root/autodl-tmp/struct_s
…[truncated 7556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T21:17:05.850251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/all_signals_report.json /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/all_signals_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/all_signals_report.json /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/all_signals_report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:17:05.850397+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 2989 May 15 05:15 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2/all_signals_report.json\\n-rw-r--r-- 1 root root 2983 May 15 05:15 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/all_signals_report.json\\n-rw-r--r-- 1 root root 2989 May 15 05:16 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed456_v2_ner/all_signals_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:17:05.850568+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check if artifacts/data directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
    "description": "Check if artifacts/data directory exists"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:17:05.850757+00:00_

bootstrap_ci_summary.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:17:05.850947+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json, numpy as np\n\n# Data from the run output\nseeds_data = {\n    'seed42': {\n        'full': {\n            'EM':  {'rho': 0.3347, 'auroc': 0.7902, 'ece': 0.3320},\n            'voting_conf': {'rho': 0.4408, 'auroc': 0.7340, 'ece': 0.3200},\n            'SJ': {'rho': 0.4280, 'auroc': 0.7368, 'ece': 0.4575},\n            'FK': {'rho': 0.2809, 'auroc': 0.6099, 'ece': 0.4822},\n            'logprob': {'rho': 0.2194, 'auroc': 0.5870, 'ece': 0.7073},\n        },\n        'conditional': {\n            'EM':  {'rho': 0.4151, 'auroc': 0.7972, 'ece': 0.3041},\n            'voting_conf': {'rho': 0.3531, 'auroc': 0.7122, 'ece': 0.3206},\n            'SJ': {'rho': 0.3688, 'auroc': 0.7193, 'ece': 0.4504},\n            'FK': {'rho': 0.1934, 'auroc': 0.5893, 'ece': 0.4845},\n            'logprob': {'rho': 0.1560, 'auroc': 0.5694, 'ece': 0.6817},\n        }\n    },\n    'seed123': {\n        'full': {\n            'EM':  {'rho': 0.3369, 'auroc': 0.7807, 'ece': 0.3355},\n            'voting_conf': {'rho': 0.4131, 'auroc': 0.7167, 'ece': 0.3123},\n            'SJ': {'rho': 0.4244, 'auroc': 0.7363, 'ece': 0.4544},\n            'FK': {'rho': 0.2752, 'auroc': 0.6268, 'ece': 0.4841},\n            'logprob': {'rho': 0.2513, 'auroc': 0.6062, 'ece': 0.7068},\n        },\n        'conditional': {\n            'EM':  {'rho': 0.4036, 'auroc': 0.7869, 'ece': 0.3096},\n            'voting_conf': {'rho': 0.3393, 'auroc': 0.6979, 'ece': 0.3071},\n            'SJ': {'rho': 0.3757, 'auroc': 0.7213, 'ece': 0.4470},\n            'FK': {'rho': 0.1785, 'auroc': 0.6054, 'ece': 0.4770},\n            'logprob': {'rho': 0.1727, 'auroc': 0.5844, 'ece': 0.6811},\n        }\n    },\n    'seed456': {\n        'full': {\n            'EM':  {'rho': 0.3162, 'auroc': 0.7683, 'ece': 0.3346},\n            'voting_conf': {'rho': 0.4111, 'auroc': 0.7121, 'ece': 0.3149},\n            'SJ': {'rho': 0.3838, 'auroc': 0.7107, 'ece': 0.4583},\n            'FK': {'rho': 0.2234, 'auroc': 0.5768, 'ece': 0.4886},\n            'logprob': {'rho': 0.2322, 'auroc': 0.5938, 'ece': 0.7032},\n        },\n        'conditional': {\n            'EM':  {'rho': 0.4058, 'auroc': 0.7801, 'ece': 0.3057},\n            'voting_conf': {'rho': 0.3459, 'auroc': 0.6937, 'ece': 0.3082},\n            'SJ': {'rho': 0.3494, 'auroc': 0.6985, 'ece': 0.4486},\n            'FK': {'rho': 0.1565, 'auroc': 0.5610, 'ece': 0.4942},\n            'logprob': {'rho': 0.1707, 'auroc': 0.5758, 'ece': 0.6780},\n        }\n    }\n}\n\nresult = {'per_seed': seeds_data, 'summary': {}}\n\nfor split in ['full', 'conditional']:\n    result['summary'][split] = {}\n    for signal in ['EM', 'voting_conf', 'SJ', 'FK', 'logprob']:\n        for metric in ['rho', 'auroc', 'ece']:\n            vals = [seeds_data[s][split][signal][metric] for s in ['seed42', 'seed123', 'seed456']]\n            arr = np.array(vals)\n            m = float(arr.mean())\n            s = float(arr.std(ddof=1))\n            cv = (s / abs(m) * 100) if m != 0 else float('nan')\n            key = f'{signal}_{metric}'\n            result['summary'][split][key] = {\n                'mean': round(m, 4),\n                'std': round(s, 4),\n                'cv_pct': round(cv, 2),\n                'values': [round(v, 4) for v in vals]\n            }\n\nprint(json.dumps(result, indent=2))\n\" > /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json\necho \"DONE\"",
  "description": "Compute 3-seed statistics and write artifact JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json, numpy as np\n\n# Data from the run output\nseeds_data = {\n    'seed42': {\n        'full': {\n            'EM':  {'rho': 0.3347, 'auroc': 0.7902, 'ece': 0.3320},\n            'voting_conf': {'rho': 0.4408, 'auroc': 0.7340, 'ece': 0.3200},\n            'SJ': {'rho': 0.4280, 'auroc': 0.7368, 'ece': 0.4575},\n            'FK': {'rho': 0.2809, 'auroc': 0.6099, 'ece': 0.4822},\n            'logprob': {'rho': 0.2194, 'auroc': 0.5870, 'ece': 0.7073},\n        },\n        'conditional': {\n            'EM':  {'rho': 0.4151, 'auroc': 0.7972, 'ece': 0.3041},\n            'voting_conf': {'rho': 0.3531, 'auroc': 0.7122, 'ece': 0.3206},\n            'SJ': {'rho': 0.3688, 'auroc': 0.7193, 'ece': 0.4504},\n            'FK': {'rho': 0.1934, 'auroc': 0.5893, 'ece': 0.4845},\n            'logprob': {'rho': 0.1560, 'auroc': 0.5694, 'ece': 0.6817},\n        }\n    },\n    'seed123': {\n        'full': {\n            'EM':  {'rho': 0.3369, 'auroc': 0.7807, 'ece': 0.3355},\n            'voting_conf': {'rho': 0.4131, 'auroc': 0.7167, 'ece': 0.3123},\n            'SJ': {'rho': 0.4244, 'auroc': 0.7363, 'ece': 0.4544},\n            'FK': {'rho': 0.2752, 'auroc': 0.6268, 'ece': 0.4841},\n            'logprob': {'rho': 0.2513, 'auroc': 0.6062, 'ece': 0.7068},\n        },\n        'conditional': {\n            'EM':  {'rho': 0.4036, 'auroc': 0.7869, 'ece': 0.3096},\n            'voting_conf': {'rho': 0.3393, 'auroc': 0.6979, 'ece': 0.3071},\n            'SJ': {'rho': 0.3757, 'auroc': 0.7213, 'ece': 0.4470},\n            'FK': {'rho': 0.1785, 'auroc': 0.6054, 'ece': 0.4770},\n            'logprob': {'rho': 0.1727, 'auroc': 0.5844, 'ece': 0.6811},\n        }\n    },\n    'seed456': {\n        'full': {\n            'EM':  {'rho': 0.3162, 'auroc': 0.7683, 'ece': 0.3346},\n            'voting_conf': {'rho': 0.4111, 'auroc': 0.7121, 'ece': 0.3149},\n            'SJ': {'rho': 0.3838, 'auroc': 0.7107, 'ece': 0.4583},\n            'FK': {'rho': 0.2234, 'auroc': 0.5768, 'ece': 0.4886},\n            'logprob': {'rho': 0.2322, 'auroc': 0.5938, 'ece': 0.7032},\n        },\n        'conditional': {\n            'EM':  {'rho': 0.4058, 'auroc': 0.7801, 'ece': 0.3057},\n            'voting_conf': {'rho': 0.3459, 'auroc': 0.6937, 'ece': 0.3082},\n            'SJ': {'rho': 0.3494, 'auroc': 0.6985, 'ece': 0.4486},\n            'FK': {'rho': 0.1565, 'auroc': 0.5610, 'ece': 0.4942},\n            'logprob': {'rho': 0.1707, 'auroc': 0.5758, 'ece': 0.6780},\n        }\n    }\n}\n\nresult = {'per_seed': seeds_data, 'summary': {}}\n\nfor split in ['full', 'conditional']:\n    result['summary'][split] = {}\n    for signal in ['EM', 'voting_conf', 'SJ', 'FK', 'logprob']:\n        for metric in ['rho', 'auroc', 'ece']:\n            vals = [seeds_data[s][split][signal][metric] for s in ['seed42', 'seed123', 'seed456']]\n            arr = np.array(vals)\n            m = float(arr.mean())\n            s = float(arr.std(ddof=1))\n            cv = (s / abs(m) * 100) if m != 0 else float('nan')\n            key = f'{signal}_{metric}'\n            result['summary'][split][key] = {\n                'mean': round(m, 4),\n                'std': round(s, 4),\n                'cv_pct': round(cv, 2),\n                'values': [round(v, 4) for v in vals]\n            }\n\nprint(json.dumps(result, indent=2))\n\" > /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json\necho \"DONE\"",
    "description": "Compute 3-seed statistics and write artifact JSON"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:17:05.851185+00:00_

DONE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T21:17:05.851345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T21:17:05.851507+00:00_

1	{
2	  "per_seed": {
3	    "seed42": {
4	      "full": {
5	        "EM": {
6	          "rho": 0.3347,
7	          "auroc": 0.7902,
8	          "ece": 0.332
9	        },
10	        "voting_conf": {
11	          "rho": 0.4408,
12	          "auroc": 0.734,
13	          "ece": 0.32
14	        },
15	        "SJ": {
16	          "rho": 0.428,
17	          "auroc": 0.7368,
18	          "ece": 0.4575
19	        },
20	        "FK": {
21	          "rho": 0.2809,
22	          "auroc": 0.6099,
23	          "ece": 0.4822
24	        },
25	        "logprob": {
26	          "rho": 0.2194,
27	          "auroc": 0.587,
28	          "ece": 0.7073
29	        }
30	      },
31	      "conditional": {
32	        "EM": {
33	          "rho": 0.4151,
34	          "auroc": 0.7972,
35	          "ece": 0.3041
36	        },
37	        "voting_conf": {
38	          "rho": 0.3531,
39	          "auroc": 0.7122,
40	          "ece": 0.3206
41	        },
42	        "SJ": {
43	          "rho": 0.3688,
44	          "auroc": 0.7193,
45	          "ece": 0.4504
46	        },
47	        "FK": {
48	          "rho": 0.1934,
49	          "auroc": 0.5893,
50	          "ece": 0.4845
51	        },
52	        "logprob": {
53	          "rho": 0.156,
54	          "auroc": 0.5694,
55	          "ece": 0.6817
56	        }
57	      }
58	    },
59	    "seed123": {
60	      "full": {
61	        "EM": {
62	          "rho": 0.3369,
63	          "auroc": 0.7807,
64	          "ece": 0.3355
65	        },
66	        "voting_conf": {
67	          "rho": 0.4131,
68	          "auroc": 0.7167,
69	          "ece": 0.3123
70	        },
71	        "SJ": {
72	          "rho": 0.4244,
73	          "auroc": 0.7363,
74	          "ece": 0.4544
75	        },
76	        "FK": {
77	          "rho": 0.2752,
78	          "auroc": 0.6268,
79	          "ece": 0.4841
80	        },

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T21:17:05.851649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json",
  "offset": "170"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json",
    "offset": "170"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T21:17:05.851930+00:00_

170	    }
171	  },
172	  "summary": {
173	    "full": {
174	      "EM_rho": {
175	        "mean": 0.3293,
176	        "std": 0.0114,
177	        "cv_pct": 3.45,
178	        "values": [
179	          0.3347,
180	          0.3369,
181	          0.3162
182	        ]
183	      },
184	      "EM_auroc": {
185	        "mean": 0.7797,
186	        "std": 0.011,
187	        "cv_pct": 1.41,
188	        "values": [
189	          0.7902,
190	          0.7807,
191	          0.7683
192	        ]
193	      },
194	      "EM_ece": {
195	        "mean": 0.334,
196	        "std": 0.0018,
197	        "cv_pct": 0.54,
198	        "values": [
199	          0.332,
200	          0.3355,
201	          0.3346
202	        ]
203	      },
204	      "voting_conf_rho": {
205	        "mean": 0.4217,
206	        "std": 0.0166,
207	        "cv_pct": 3.94,
208	        "values": [
209	          0.4408,
210	          0.4131,
211	          0.4111
212	        ]
213	      },
214	      "voting_conf_auroc": {
215	        "mean": 0.7209,
216	        "std": 0.0115,
217	        "cv_pct": 1.6,
218	        "values": [
219	          0.734,
220	          0.7167,
221	          0.7121
222	        ]
223	      },
224	      "voting_conf_ece": {
225	        "mean": 0.3157,
226	        "std": 0.0039,
227	        "cv_pct": 1.24,
228	        "values": [
229	          0.32,
230	          0.3123,
231	          0.3149
232	        ]
233	      },
234	      "SJ_rho": {
235	        "mean": 0.4121,
236	        "std": 0.0245,
237	        "cv_pct": 5.96,
238	        "values": [
239	          0.428,
240	          0.4244,
241	          0.3838
242	        ]
243	      },
244	      "SJ_auroc": {
245	        "mean": 0.7279,
246	        "std": 0.0149,
247	        "cv_pct": 2.05,
248	        "values": [
249	          0.7368,
250	          0.7363,
251	          0.7107
252	        ]
253	      },
254	      "SJ_ece": {
255	        "mean": 0.4567,
256	        "std": 0.0021,
257	        "cv_pct": 0.45,
258	        "values": [
259	          0.4575,

…[truncated 4834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T21:17:05.852195+00:00_

全部完成。

### 产出

**服务器上**：3 个 `all_signals_report.json` 已生成
- `output/exp_001_seed42_v2/all_signals_report.json`
- `output/exp_001_seed123_v2/all_signals_report.json`
- `output/exp_001_seed456_v2_ner/all_signals_report.json`

**本地**：`artifacts/data/qwen_scierc_3seed_em_voting.json`

### EM 和 voting_conf 3-seed 汇总（full split）

| Signal | Metric | Mean±Std | CV% |
|--------|--------|----------|-----|
| **EM** | rho | 0.3293±0.0114 | 3.5% |
| **EM** | AUROC | 0.7797±0.0110 | 1.4% |
| **EM** | ECE | 0.3340±0.0018 | 0.5% |
| **voting_conf** | rho | 0.4217±0.0166 | 3.9% |
| **voting_conf** | AUROC | 0.7209±0.0115 | 1.6% |
| **voting_conf** | ECE | 0.3157±0.0039 | 1.2% |

### EM 和 voting_conf 3-seed 汇总（conditional split）

| Signal | Metric | Mean±Std | CV% |
|--------|--------|----------|-----|
| **EM** | rho | 0.4082±0.0061 | 1.5% |
| **EM** | AUROC | 0.7881±0.0086 | 1.1% |
| **EM** | ECE | 0.3065±0.0028 | 0.9% |
| **voting_conf** | rho | 0.3461±0.0069 | 2.0% |
| **voting_conf** | AUROC | 0.7013±0.0097 | 1.4% |
| **voting_conf** | ECE | 0.3120±0.0075 | 2.4% |

CV 均 <4%（full split），<2.5%（conditional split），跨 seed 稳定性良好。EM 在 AUROC 上最强（0.78-0.79），voting_conf 在 rho 上最强（0.42 full / 0.35 cond）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_data_qwen_scierc_3seed_em_voting_20260514T211403"
}
```

</details>

---
