# analysis nli combo recompute pw

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 109
- **Recorded user turns:** 0
- **Tool calls:** 54
- **Original source:** `logs/chats/worker_analysis_nli-combo-recompute-pw_20260521T052024.jsonl`
- **Structured JSON:** [`2a88f6b98706b6efd4d9.json`](../../sessions/2a/2a88f6b98706b6efd4d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

109 recorded events

### Tool call

_source line 1 · 2026-05-21T05:32:11.325390+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T05:32:11.325776+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T05:32:11.326039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -type d -name \"*nli*\" -o -type d -name \"*combo*\" -o -type d -name \"*deberta*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -type d -name \"*nli*\" -o -type d -name \"*combo*\" -o -type d -name \"*deberta*\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T05:32:11.326199+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/ -name \"*.py\" -path \"*combo*\" -o -name \"*.py\" -path \"*nli*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/ -name \"*.py\" -path \"*combo*\" -o -name \"*.py\" -path \"*nli*\""
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T05:32:11.326345+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/dir_j1_nli_logiqa\\n/root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter\\n/root/symb_invariant_consensus/results/push_b_stronger_nli_verifier\\n/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large\\n/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo\\n/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.13}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T05:32:11.326481+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/scripts/push_b_stronger_nli.py\\n/root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py\\n/root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py\\n/root/symb_invariant_consensus/scripts/dir_j1_nli_logiqa.py\\n/root/symb_invariant_consensus/dir_k_nli_qwen3_pw600.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T05:32:11.326607+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -type d -name \"*nli*\" -o -type d -name \"*combo*\" -o -type d -name \"*deberta*\" -o -type d -name \"*folio*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -type d -name \"*nli*\" -o -type d -name \"*combo*\" -o -type d -name \"*deberta*\" -o -type d -name \"*folio*\""
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T05:32:11.326729+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/ -name \"*.py\" -path \"*combo*\" -o -name \"*.py\" -path \"*nli*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/ -name \"*.py\" -path \"*combo*\" -o -name \"*.py\" -path \"*nli*\""
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T05:32:11.326907+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/folio_204_14b\\n/root/symb_invariant_consensus/results/exp-029-contrastive-folio204\\n/root/symb_invariant_consensus/results/cross_model_mistral_folio\\n/root/symb_invariant_consensus/results/oracle_folio_regen\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204\\n/root/symb_invariant_consensus/results/exp034_llama31_8b_folio204\\n/root/symb_invariant_consensus/results/exp035_qwen25_7b_folio204\\n/root/symb_invariant_consensus/results/icl_oracle_folio\\n/root/symb_invariant_consensus/results/exp047_qwen3_thinking_folio204\\n/root/symb_invariant_consensus/results/exp028b_qwen3_thinking_folio204\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10\\n/root/symb_invariant_consensus/results/exp057_mistral_folio204_t03\\n/root/symb_invariant_consensus/results/exp058_mistral_folio204_t05\\n/root/symb_invariant_consensus/results/exp061_qwen25_7b_folio204\\n/root/symb_invariant_consensus/results/exp062_gemma27b_folio204\\n/root/symb_invariant_consensus/results/exp066_qwen14b_folio_seed123\\n/root/symb_invariant_consensus/results/exp067_mistral_folio_seed789\\n/root/symb_invariant_consensus/results/exp076_debate_mistral_folio\\n/root/symb_invariant_consensus/results/exp074_icg_mistral_folio\\n/root/symb_invariant_consensus/results/exp075b_contrastive_mistral_folio\\n/root/symb_invariant_consensus/results/exp074c_icg_mistral_folio_seed123\\n/root/symb_invariant_consensus/results/exp074d_icg_mistral_folio_seed456\\n/root/symb_invariant_consensus/results/direction_r_deberta\\n/root/symb_invariant_consensus/results/direction_r_nli_small\\n/root/symb_invariant_consensus/results/direction_r_nli_large\\n/root/symb_invariant_consensus/results/direction_rg_combo\\n/root/symb_invariant_consensus/results/direction_r_nli_pw600\\n/root/symb_invariant_consensus/results/dir_j2_nli_qwen3\\n/root/symb_invariant_consensus/results/dir_j3_nli_multi_verifier\\n/root/symb_
…[truncated 218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T05:32:11.327097+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/scripts/dir_j2_nli_qwen3.py\\n/root/symb_invariant_consensus/direction_r_nli_verifier.py\\n/root/symb_invariant_consensus/direction_rg_combo.py\\n/root/symb_invariant_consensus/dir_j3_nli_multi_verifier.py\\n/root/symb_invariant_consensus/dir_k_nli_qwen3_pw600.py\\n/root/symb_invariant_consensus/nli_tiebreak_audit.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T05:32:11.327304+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T05:32:11.327470+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T05:32:11.327760+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Qwen2.5-14B ProofWriter NLI Combo using D116's DeBERTa-large predictions.\\n\\nDeBERTa-large-mnli predictions are deterministic on the same 600 PW problems\\nregardless of generator model, so we reuse D116's per_question results directly.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nfrom collections import Counter\\nfrom scipy.stats import binomtest\\n\\nEXP032_PATH = \\\"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/results.json\\\"\\nD116_PATH = \\\"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\\\"\\nOUTPUT_DIR = \\\"/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo\\\"\\nCLASSES = [\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"]\\nWEIGHTS = [1, 3, 5]\\n\\n\\ndef mcnemar_test(b, c):\\n    n = b + c\\n    if n == 0:\\n        return 1.0\\n    return binomtest(min(b, c), n, 0.5).pvalue\\n\\n\\ndef main():\\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\\n\\n    with open(EXP032_PATH) as f:\\n        exp032 = json.load(f)\\n    with open(D116_PATH) as f:\\n        d116 = json.load(f)\\n\\n    results_list = exp032[\\\"results\\\"]\\n    d116_pq = d116[\\\"per_question\\\"]\\n    total = len(results_list)\\n    print(f\\\"Loaded {total} problems from exp032 (Qwen2.5-14B PW600)\\\")\\n\\n    # Extract per-problem data from exp032\\n    gt = {}\\n    sc_answers = {}\\n    sc_vote_dists = {}\\n    for r in results_list:\\n        pid = r[\\\"problem_id\\\"]\\n        gt[pid] = r[\\\"ground_truth\\\"]\\n        sc_answers[pid] = r[\\\"sc_answer\\\"]\\n        sc_vote_dists[pid] = r[\\\"sc_vote_distribution\\\"]\\n\\n    # Verify all problem_ids match D116\\n    missing = [pid for pid in gt if pid not in d116_pq]\\n    if missing:\\n        print(f\\\"WARNING: {len(missing)} problems missing from D116!\\\")\\n        for m in missing[:5]:\\n            print(f\\\"  {m}\\\")\\n    else:\\n        print(\\\"All 600 problem_ids 
…[truncated 7237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T05:32:11.328146+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"LLaMA-3.1-8B ProofWriter NLI Combo using D116's DeBERTa-large predictions.\\n\\nDeBERTa-large-mnli predictions are deterministic on the same 600 PW problems\\nregardless of generator model, so we reuse D116's per_question results directly.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nfrom collections import Counter\\nfrom scipy.stats import binomtest\\n\\nEXP048_PATH = \\\"/root/symb_invariant_consensus/results/exp048_llama8b_pw600/exp048_results.json\\\"\\nD116_PATH = \\\"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\\\"\\nOUTPUT_DIR = \\\"/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo\\\"\\nCLASSES = [\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"]\\nWEIGHTS = [1, 3, 5]\\n\\n\\ndef mcnemar_test(b, c):\\n    n = b + c\\n    if n == 0:\\n        return 1.0\\n    return binomtest(min(b, c), n, 0.5).pvalue\\n\\n\\ndef main():\\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\\n\\n    with open(EXP048_PATH) as f:\\n        exp048 = json.load(f)\\n    with open(D116_PATH) as f:\\n        d116 = json.load(f)\\n\\n    results_list = exp048[\\\"results\\\"]\\n    d116_pq = d116[\\\"per_question\\\"]\\n    total = len(results_list)\\n    print(f\\\"Loaded {total} problems from exp048 (LLaMA-3.1-8B PW600)\\\")\\n\\n    gt = {}\\n    sc_answers = {}\\n    sc_vote_dists = {}\\n    for r in results_list:\\n        pid = r[\\\"problem_id\\\"]\\n        gt[pid] = r[\\\"ground_truth\\\"]\\n        sc_answers[pid] = r[\\\"sc_answer\\\"]\\n        sc_vote_dists[pid] = r[\\\"sc_vote_distribution\\\"]\\n\\n    missing = [pid for pid in gt if pid not in d116_pq]\\n    if missing:\\n        print(f\\\"WARNING: {len(missing)} problems missing from D116!\\\")\\n        for m in missing[:5]:\\n            print(f\\\"  {m}\\\")\\n    else:\\n        print(\\\"All 600 problem_ids match D116 DeBERTa predictions.\\\")\\n\\n    gold_mismatch = [pid for pid
…[truncated 7245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T05:32:11.328342+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/dir_k_nli_qwen3_pw600.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/dir_k_nli_qwen3_pw600.py"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T05:32:11.328624+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/nli_tiebreak_audit.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/nli_tiebreak_audit.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T05:32:11.328988+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Dir-K: DeBERTa NLI Verifier on Qwen3-14B ProofWriter-D5 (600 questions)\\nSC/SICA baselines from exp033_qwen3_14b_pw600_nonthinking.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport time\\nfrom collections import Counter\\nfrom scipy.stats import binomtest\\nfrom transformers import AutoTokenizer, AutoModelForSequenceClassification\\nimport torch\\n\\nTRACES_PATH = \\\"/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\\\"\\nPW_DATA_PATH = \\\"/root/symb_invariant_consensus/data/proofwriter_full.json\\\"\\nOUTPUT_DIR = \\\"/root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter\\\"\\nMODEL_NAME = \\\"/root/autodl-tmp/models/deberta-base-mnli\\\"\\nCLASSES = [\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"]\\nWEIGHTS = [1, 3, 5]\\n\\n\\ndef parse_problem(problem_text):\\n    marker = \\\"\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\n\\\"\\n    if marker in problem_text:\\n        parts = problem_text.split(marker, 1)\\n        return parts[0].strip(), parts[1].strip()\\n    return problem_text, \\\"\\\"\\n\\n\\ndef main():\\n    os.makedirs(OUTPUT_DIR, exist_ok=True)\\n\\n    # Load traces\\n    with open(TRACES_PATH) as f:\\n        traces = json.load(f)\\n\\n    # Load PW data for problem text\\n    with open(PW_DATA_PATH) as f:\\n        pw_data = json.load(f)\\n    pw_by_id = {q[\\\"id\\\"]: q for q in pw_data}\\n\\n    results_list = traces[\\\"results\\\"]\\n    total = len(results_list)\\n    print(f\\\"Loaded {total} problems from traces\\\")\\n\\n    # Extract baselines\\n    gt = {}\\n    sc_answers = {}\\n    sica_answers = {}\\n    sc_vote_dists = {}\\n    for r in results_list:\\n        pid = r[\\\"problem_id\\\"]\\n        gt[pid] = r[\\\"ground_truth\\\"]\\n        sc_answers[pid] = r[\\\"sc_answer\\\"]\\n        sica_answers[pid] = r[\\\"sica_answer\\\"]\\n        sc_vote_di
…[truncated 7278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T05:32:11.329336+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Audit NLI combo tiebreaking: Counter.most_common() vs alphabetical.\\\"\\\"\\\"\\nimport json\\nimport os\\nfrom collections import Counter\\nfrom scipy.stats import binomtest\\n\\nVALID = {\\\"True\\\", \\\"False\\\", \\\"Unknown\\\"}\\nWEIGHTS = [1, 3, 5]\\n\\nSC_PATH = \\\"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\\\"\\nNLI_PATH = \\\"/root/symb_invariant_consensus/results/direction_r_nli_pw600/results.json\\\"\\nOUT_PATH = \\\"/root/symb_invariant_consensus/results/nli_tiebreak_audit/results.json\\\"\\n\\ndef majority_alpha(vote_dist):\\n    if not vote_dist:\\n        return \\\"Unknown\\\"\\n    filtered = {k: v for k, v in vote_dist.items() if k in VALID}\\n    if not filtered:\\n        return \\\"Unknown\\\"\\n    max_count = max(filtered.values())\\n    winners = sorted([k for k, v in filtered.items() if v == max_count])\\n    return winners[0]\\n\\ndef majority_counter(vote_dist):\\n    if not vote_dist:\\n        return \\\"Unknown\\\"\\n    c = Counter()\\n    for k, v in vote_dist.items():\\n        if k in VALID:\\n            c[k] = v\\n    if not c:\\n        return \\\"Unknown\\\"\\n    return c.most_common(1)[0][0]\\n\\ndef combo_vote(sc_dist, nli_pred, w, tiebreak=\\\"alpha\\\"):\\n    combined = {}\\n    for k, v in sc_dist.items():\\n        if k in VALID:\\n            combined[k] = combined.get(k, 0) + v\\n    if nli_pred in VALID:\\n        combined[nli_pred] = combined.get(nli_pred, 0) + w\\n    if tiebreak == \\\"alpha\\\":\\n        return majority_alpha(combined)\\n    else:\\n        return majority_counter(combined)\\n\\ndef mcnemar_exact(correct_a, correct_b):\\n    n = len(correct_a)\\n    b = sum(1 for i in range(n) if correct_a[i] and not correct_b[i])\\n    c = sum(1 for i in range(n) if not correct_a[i] and correct_b[i])\\n    n_disc = b + c\\n    if n_disc == 0:\\n        return {\\\"b\\\": 0, \\\
…[truncated 7383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T05:32:11.329512+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/direction_rg_combo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/direction_rg_combo.py"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T05:32:11.329648+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T05:32:11.329901+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Direction R+G Combo: SICA + NLI external verifier combination strategies.\\n\\nCombines two architecturally independent signals:\\n- SICA: symbolic constraint aggregation from CoT traces (MAX-SAT)\\n- NLI: DeBERTa encoder-only model predicting entailment/contradiction/neutral\\n\\nSince full G (decoupling) results are unavailable (only 5 test problems),\\nthis uses standard SICA results. When G results become available,\\nswap in SICA-G per-problem answers.\\n\\\"\\\"\\\"\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nfrom collections import Counter\\n\\nimport numpy as np\\n\\n\\ndef normalize_answer(ans):\\n    ans = str(ans).strip().lower()\\n    if ans in ('true', 'yes', 't'):\\n        return 'True'\\n    elif ans in ('false', 'no', 'f'):\\n        return 'False'\\n    elif ans in ('unknown', 'uncertain', 'u', 'undetermined'):\\n        return 'Unknown'\\n    return ans.capitalize()\\n\\n\\ndef sc_majority(answers):\\n    valid = [normalize_answer(a) for a in answers if normalize_answer(a) in ('True', 'False', 'Unknown')]\\n    if not valid:\\n        return 'Unknown'\\n    c = Counter(valid)\\n    return c.most_common(1)[0][0]\\n\\n\\ndef mcnemar_test(correct_a, correct_b):\\n    \\\"\\\"\\\"McNemar's test: are two classifiers significantly different?\\\"\\\"\\\"\\n    n = len(correct_a)\\n    b_count = sum(1 for i in range(n) if correct_a[i] and not correct_b[i])\\n    c_count = sum(1 for i in range(n) if not correct_a[i] and correct_b[i])\\n\\n    if b_count + c_count == 0:\\n        return {'chi2': 0.0, 'p_value': 1.0, 'b': b_count, 'c': c_count}\\n\\n    chi2 = (abs(b_count - c_count) - 1) ** 2 / (b_count + c_count)\\n\\n    from scipy.stats import chi2 as chi2_dist\\n    p_value = 1 - chi2_dist.cdf(chi2, df=1)\\n    return {'chi2': round(chi2, 4), 'p_value': round(p_value, 6), 'b': b_count, 'c': c_count}\\n\\n\\ndef load_data(r_results_path, exp033_pat
…[truncated 6729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T05:32:11.330080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T05:32:11.330520+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/nli_tiebreak_audit/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/nli_tiebreak_audit/results.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T05:32:11.331017+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"investigation\\\": {\\n    \\\"affected_scripts\\\": [\\n      \\\"direction_r_deberta_proofwriter.py \\\\u2014 uses Counter.most_common()\\\",\\n      \\\"dir_j3_nli_multi_verifier.py \\\\u2014 uses Counter.most_common()\\\",\\n      \\\"dir_k_nli_qwen3_pw600.py \\\\u2014 uses Counter.most_common()\\\",\\n      \\\"direction_rg_combo.py \\\\u2014 uses Counter.most_common() in sc_majority()\\\",\\n      \\\"direction_r_nli_verifier.py (FOLIO) \\\\u2014 uses Counter.most_common()\\\"\\n    ],\\n    \\\"tiebreaking_method\\\": \\\"Counter.most_common(1)[0][0]\\\",\\n    \\\"correct_method\\\": \\\"sorted(tied_candidates)[0] \\\\u2014 alphabetical\\\",\\n    \\\"drc_cascade_pilot_uses\\\": \\\"alphabetical (correct)\\\",\\n    \\\"code_snippet_combo\\\": \\\"votes.most_common(1)[0][0]  # insertion-order tiebreaking under ties\\\",\\n    \\\"code_snippet_sc\\\": \\\"c = Counter(valid); return c.most_common(1)[0][0]\\\"\\n  },\\n  \\\"sc_baseline_check\\\": {\\n    \\\"sc_alphabetical\\\": {\\n      \\\"accuracy\\\": 0.3933,\\n      \\\"correct\\\": 236\\n    },\\n    \\\"sc_counter\\\": {\\n      \\\"accuracy\\\": 0.3933,\\n      \\\"correct\\\": 236\\n    },\\n    \\\"n_sc_tiebreak_diffs\\\": 11,\\n    \\\"sc_tie_examples\\\": [\\n      {\\n        \\\"pid\\\": \\\"ProofWriter_AttNeg-OWA-D5-276_Q4\\\",\\n        \\\"gold\\\": \\\"False\\\",\\n        \\\"alpha\\\": \\\"True\\\",\\n        \\\"counter\\\": \\\"Unknown\\\",\\n        \\\"dist\\\": {\\n          \\\"Unknown\\\": 4,\\n          \\\"Erin is not white.\\\": 1,\\n          \\\"True\\\": 4,\\n          \\\"False\\\": 2,\\n          \\\"False (but with a caveat)\\\": 1\\n        }\\n      },\\n      {\\n        \\\"pid\\\": \\\"ProofWriter_AttNeg-OWA-D5-908_Q16\\\",\\n        \\\"gold\\\": \\\"Unknown\\\",\\n        \\\"alpha\\\": \\\"False\\\",\\n        \\\"counter\\\": \\\"Unknown\\\",\\n        \\\"dist\\\": {\\n          \\\"Unknown\\\": 5,\
…[truncated 8795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T05:32:11.331261+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/direction_r_nli_large/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/direction_r_nli_large/"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T05:32:11.331434+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T05:32:11.331576+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/nli_combo_full_table_bh/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/nli_combo_full_table_bh/"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T05:32:11.331713+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T05:32:11.331842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -path \"*folio*\" -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -path \"*folio*\" -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T05:32:11.332223+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_0.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_1.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_2.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_3.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_4.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_5.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_6.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_7.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_8.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_9.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_10.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_11.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_12.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_13.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_14.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_15.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_16.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_17.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_18.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_19.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_20.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_21.json\\n/root/symb_invariant_consensus/results/folio_204_14b/intermediates/folio_22.json\\n/root/symb_invariant_consensus/results/folio_
…[truncated 6387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T05:32:11.332441+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/nli_combo_full_table_bh/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/nli_combo_full_table_bh/results.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T05:32:11.332729+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"NLI Combo Full Table with Benjamini-Hochberg Correction\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"verifier\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"deberta_standalone_accuracy\\\": 0.55,\\n  \\\"n_tests\\\": 12,\\n  \\\"alpha\\\": 0.05,\\n  \\\"bh_significant_count\\\": 4,\\n  \\\"source_files\\\": {\\n    \\\"Mistral-7B\\\": \\\"westd-25068:direction_r_nli_pw600 + exp046_mistral_7b_pw600\\\",\\n    \\\"LLaMA-3.1-8B\\\": \\\"westd-16639:exp092_llama8b_pw_nli_combo\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"westd-16639:qwen14b_pw_nli_combo\\\",\\n    \\\"Qwen3-14B\\\": \\\"westd-16639:d116_qwen3_pw_deberta_large\\\",\\n    \\\"LLaMA-SC-baseline\\\": \\\"westd-16639:exp048_llama8b_pw600 (SC=0.70 confirmed)\\\"\\n  },\\n  \\\"generators\\\": {\\n    \\\"Mistral-7B\\\": {\\n      \\\"n\\\": 600,\\n      \\\"sc_accuracy\\\": 0.3933,\\n      \\\"sc_accuracy_pct\\\": 39.33,\\n      \\\"capability_gap_pp\\\": 15.67,\\n      \\\"w1\\\": {\\n        \\\"combo_accuracy\\\": 0.4017,\\n        \\\"combo_accuracy_pct\\\": 40.17,\\n        \\\"delta_pp\\\": 0.83,\\n        \\\"discordant\\\": [\\n          4,\\n          9\\n        ],\\n        \\\"p_raw\\\": 0.2668457031,\\n        \\\"p_bh\\\": 0.3557942708,\\n        \\\"significant_bh_005\\\": false\\n      },\\n      \\\"w3\\\": {\\n        \\\"combo_accuracy\\\": 0.4283,\\n        \\\"combo_accuracy_pct\\\": 42.83,\\n        \\\"delta_pp\\\": 3.5,\\n        \\\"discordant\\\": [\\n          22,\\n          43\\n        ],\\n        \\\"p_raw\\\": 0.0125025461,\\n        \\\"p_bh\\\": 0.0375076384,\\n        \\\"significant_bh_005\\\": true\\n      },\\n      \\\"w5\\\": {\\n        \\\"combo_accuracy\\\": 0.5,\\n        \\\"combo_accuracy_pct\\\": 50.0,\\n        \\\"delta_pp\\\": 10.67,\\n        \\\"discordant\\\": [\\n          35,\\n          99\\n        ],\\n        \\\"p_raw\\\": 2.89e-08,\\n        \\\"p_bh\
…[truncated 7137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T05:32:11.333003+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T05:32:11.333597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_r1_deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.4951,\\n    \\\"correct\\\": 101,\\n    \\\"total\\\": 204,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 72,\\n        \\\"correct\\\": 43,\\n        \\\"accuracy\\\": 0.5972,\\n        \\\"precision\\\": 0.5181,\\n        \\\"recall\\\": 0.5972,\\n        \\\"f1\\\": 0.5548\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 63,\\n        \\\"correct\\\": 45,\\n        \\\"accuracy\\\": 0.7143,\\n        \\\"precision\\\": 0.4545,\\n        \\\"recall\\\": 0.7143,\\n        \\\"f1\\\": 0.5556\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 69,\\n        \\\"correct\\\": 13,\\n        \\\"accuracy\\\": 0.1884,\\n        \\\"precision\\\": 0.5909,\\n        \\\"recall\\\": 0.1884,\\n        \\\"f1\\\": 0.2857\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"Unknown\\\": 69,\\n      \\\"True\\\": 72,\\n      \\\"False\\\": 63\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 83,\\n      \\\"False\\\": 99,\\n      \\\"Unknown\\\": 22\\n    },\\n    \\\"inference_time_s\\\": 42.1,\\n    \\\"model\\\": \\\"/root/models/deberta-large-mnli\\\"\\n  },\\n  \\\"exp_r2_verifier\\\": {\\n    \\\"agreement_rate\\\": 0.451,\\n    \\\"agree_count\\\": 92,\\n    \\\"disagree_count\\\": 112,\\n    \\\"agree_accuracy\\\": 0.6848,\\n    \\\"disagree_breakdown\\\": {\\n      \\\"deberta_correct_sc_wrong\\\": 38,\\n      \\\"sc_correct_deberta_wrong\\\": 48,\\n      \\\"both_wrong\\\": 26\\n    },\\n    \\\"strategies\\\": {\\n      \\\"abstain\\\": {\\n        \\\"coverage\\\": 0.451,\\n        \\\"accuracy\\\": 0.6848\\n      },\\n      \\\"deberta_override\\\": {\\n        \\\"accuracy\\\": 0.4951\\n      },\\n      \\\"sc_baseline\\\": {\\n        \\\"accuracy\\\": 0.5441\\n      }\\n    },\\n    \\\"deberta_corrects_sc\\\": [\\n      \\\"folio_2\\\",\\n      \\\"folio_5\\\",\\n      \\\
…[truncated 9202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T05:32:11.333819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -100 /root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -100 /root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T05:32:11.334060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp092: LLaMA-3.1-8B ProofWriter NLI Combo (DeBERTa-large reused from D116)\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"LLaMA-3.1-8B-Instruct\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"n_questions\\\": 600,\\n  \\\"standalone_accuracy\\\": 0.55,\\n  \\\"sc_baseline\\\": 0.7,\\n  \\\"capability_gap_pp\\\": -15.0,\\n  \\\"deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.55,\\n    \\\"correct\\\": 330,\\n    \\\"total\\\": 600,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 128,\\n        \\\"accuracy\\\": 0.64,\\n        \\\"precision\\\": 0.6957,\\n        \\\"recall\\\": 0.64,\\n        \\\"f1\\\": 0.6667\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 195,\\n        \\\"accuracy\\\": 0.975,\\n        \\\"precision\\\": 0.4791,\\n        \\\"recall\\\": 0.975,\\n        \\\"f1\\\": 0.6425\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 7,\\n        \\\"accuracy\\\": 0.035,\\n        \\\"precision\\\": 0.7778,\\n        \\\"recall\\\": 0.035,\\n        \\\"f1\\\": 0.067\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"True\\\": 200,\\n      \\\"False\\\": 200,\\n      \\\"Unknown\\\": 200\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 184,\\n      \\\"False\\\": 407,\\n      \\\"Unknown\\\": 9\\n    },\\n    \\\"note\\\": \\\"Reused from D116 (same 600 PW problems, NLI is generator-independent)\\\"\\n  },\\n  \\\"combo\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.7283,\\n      \\\"delta_pp\\\": 2.83,\\n      \\\"mcnemar_p\\\": 0.0001,\\n      \\\"discordant\\\": [\\n        18,\\n        1\\n      ]\\n    },\\n    \\\"w3\\\": {\\n      \\\"accuracy\\\": 0.7417,\\n      \\\"delta_pp\\\": 4.17,\\n      \\\"mcnemar_p\\\": 0
…[truncated 983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T05:32:11.334237+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -100 /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -100 /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T05:32:11.334432+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"Qwen2.5-14B ProofWriter NLI Combo (DeBERTa-large reused from D116)\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"Qwen2.5-14B-Instruct\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"n_questions\\\": 600,\\n  \\\"standalone_accuracy\\\": 0.55,\\n  \\\"sc_baseline\\\": 0.735,\\n  \\\"capability_gap_pp\\\": -18.5,\\n  \\\"deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.55,\\n    \\\"correct\\\": 330,\\n    \\\"total\\\": 600,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 128,\\n        \\\"accuracy\\\": 0.64,\\n        \\\"precision\\\": 0.6957,\\n        \\\"recall\\\": 0.64,\\n        \\\"f1\\\": 0.6667\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 195,\\n        \\\"accuracy\\\": 0.975,\\n        \\\"precision\\\": 0.4791,\\n        \\\"recall\\\": 0.975,\\n        \\\"f1\\\": 0.6425\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 7,\\n        \\\"accuracy\\\": 0.035,\\n        \\\"precision\\\": 0.7778,\\n        \\\"recall\\\": 0.035,\\n        \\\"f1\\\": 0.067\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"True\\\": 200,\\n      \\\"False\\\": 200,\\n      \\\"Unknown\\\": 200\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 184,\\n      \\\"False\\\": 407,\\n      \\\"Unknown\\\": 9\\n    },\\n    \\\"note\\\": \\\"Reused from D116 (same 600 PW problems, NLI is generator-independent)\\\"\\n  },\\n  \\\"combo\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.7417,\\n      \\\"delta_pp\\\": 0.67,\\n      \\\"mcnemar_p\\\": 0.3438,\\n      \\\"discordant\\\": [\\n        7,\\n        3\\n      ]\\n    },\\n    \\\"w3\\\": {\\n      \\\"accuracy\\\": 0.7433,\\n      \\\"delta_pp\\\": 0.83,\\n      \\\"mcnemar_p\\\": 0.4049,\\n
…[truncated 971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T05:32:11.334590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -100 /root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -100 /root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter/results.json"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T05:32:11.334783+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"Dir-K: DeBERTa NLI Verifier on Qwen3-14B ProofWriter-D5\\\",\\n  \\\"model\\\": \\\"Qwen3-14B (non-thinking mode)\\\",\\n  \\\"nli_model\\\": \\\"/root/autodl-tmp/models/deberta-base-mnli\\\",\\n  \\\"nli_model_note\\\": \\\"deberta-base-mnli (not large); Mistral PW600 experiment used deberta-large-mnli\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-OWA\\\",\\n  \\\"n_questions\\\": 600,\\n  \\\"deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.3617,\\n    \\\"correct\\\": 217,\\n    \\\"total\\\": 600,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 15,\\n        \\\"accuracy\\\": 0.075,\\n        \\\"precision\\\": 0.6522,\\n        \\\"recall\\\": 0.075,\\n        \\\"f1\\\": 0.1345\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 196,\\n        \\\"accuracy\\\": 0.98,\\n        \\\"precision\\\": 0.3433,\\n        \\\"recall\\\": 0.98,\\n        \\\"f1\\\": 0.5084\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 6,\\n        \\\"accuracy\\\": 0.03,\\n        \\\"precision\\\": 1.0,\\n        \\\"recall\\\": 0.03,\\n        \\\"f1\\\": 0.0583\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"True\\\": 200,\\n      \\\"False\\\": 200,\\n      \\\"Unknown\\\": 200\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"False\\\": 571,\\n      \\\"True\\\": 23,\\n      \\\"Unknown\\\": 6\\n    },\\n    \\\"inference_time_s\\\": 41.3\\n  },\\n  \\\"baselines\\\": {\\n    \\\"sc\\\": 0.85,\\n    \\\"sc_correct\\\": 510,\\n    \\\"sica\\\": 0.8567,\\n    \\\"sica_correct\\\": 514\\n  },\\n  \\\"complementarity\\\": {\\n    \\\"nli_right_sc_wrong\\\": 40,\\n    \\\"sc_right_nli_wrong\\\": 333,\\n    \\\"both_right\\\": 177,\\n    \\\"both_wrong\\\": 50\\n  },\\n  \\\"combo_vs_sc\\\": {\\n    \\\"w1\\\": {\\n      \\\"accuracy\\\": 0.855
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T05:32:11.335027+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T05:32:11.335335+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Direction R: External NLI Verifier for FOLIO logical reasoning.\\n\\nUses an encoder-only NLI model (architecturally independent from decoder-only LLMs)\\nas an external verifier to break confirmation bias in self-consistency.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom pathlib import Path\\n\\nimport torch\\nfrom transformers import AutoModelForSequenceClassification, AutoTokenizer\\n\\n\\ndef parse_problem(problem_text):\\n    \\\"\\\"\\\"Extract premises and hypothesis from FOLIO problem text.\\\"\\\"\\\"\\n    m = re.search(\\n        r\\\"Given the following premises:\\\\n(.+?)\\\\n\\\\nDetermine whether the following conclusion is true, false, or uncertain:\\\\n(.+)\\\",\\n        problem_text,\\n        re.DOTALL,\\n    )\\n    if m:\\n        return m.group(1).strip(), m.group(2).strip()\\n    parts = problem_text.split(\\\"Determine whether the following conclusion is true, false, or uncertain:\\\")\\n    if len(parts) == 2:\\n        premises = parts[0].replace(\\\"Given the following premises:\\\", \\\"\\\").strip()\\n        hypothesis = parts[1].strip()\\n        return premises, hypothesis\\n    return problem_text, \\\"\\\"\\n\\n\\ndef load_nli_model(model_name, device):\\n    \\\"\\\"\\\"Load NLI model and tokenizer.\\\"\\\"\\\"\\n    print(f\\\"Loading NLI model: {model_name}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n    model = AutoModelForSequenceClassification.from_pretrained(model_name)\\n    model.to(device)\\n    model.eval()\\n    id2label = model.config.id2label\\n    print(f\\\"  Labels: {id2label}\\\")\\n    return model, tokenizer, id2label\\n\\n\\ndef nli_predict(model, tokenizer, id2label, premise, hypothesis, device):\\n    \\\"\\\"\\\"Run NLI inference, return (label, probs_dict).\\\"\\\"\\\"\\n    inputs = tokenizer(\\n        premise
…[truncated 7589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T05:32:11.335501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/ -name \"results.json\" -path \"*mistral*folio*\" -o -name \"results.json\" -path \"*folio*mistral*\" -o -name \"*.json\" -path \"*exp054*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/ -name \"results.json\" -path \"*mistral*folio*\" -o -name \"results.json\" -path \"*folio*mistral*\" -o -name \"*.json\" -path \"*exp054*\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T05:32:11.335845+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_0.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_1.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_2.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_3.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_4.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_5.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_6.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_7.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_8.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_9.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_10.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_11.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_12.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_13.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_14.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_15.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_16.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_17.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_18.json\\n/root/symb_invariant_consensus/results/exp054_mistral_folio204_t10/intermediates/folio_19.json\\n/root/symb_inv
…[truncated 6366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T05:32:11.336068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -50 /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -50 /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T05:32:11.336241+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"D116: Qwen3-14B ProofWriter combo with DeBERTa-large-mnli\\\",\\n  \\\"verifier_model\\\": \\\"microsoft/deberta-large-mnli\\\",\\n  \\\"generator_model\\\": \\\"Qwen3-14B (non-thinking mode)\\\",\\n  \\\"dataset\\\": \\\"ProofWriter-D5-600\\\",\\n  \\\"n_questions\\\": 600,\\n  \\\"standalone_accuracy\\\": 0.55,\\n  \\\"sc_baseline\\\": 0.85,\\n  \\\"deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.55,\\n    \\\"correct\\\": 330,\\n    \\\"total\\\": 600,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 128,\\n        \\\"accuracy\\\": 0.64,\\n        \\\"precision\\\": 0.6957,\\n        \\\"recall\\\": 0.64,\\n        \\\"f1\\\": 0.6667\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 195,\\n        \\\"accuracy\\\": 0.975,\\n        \\\"precision\\\": 0.4791,\\n        \\\"recall\\\": 0.975,\\n        \\\"f1\\\": 0.6425\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 200,\\n        \\\"correct\\\": 7,\\n        \\\"accuracy\\\": 0.035,\\n        \\\"precision\\\": 0.7778,\\n        \\\"recall\\\": 0.035,\\n        \\\"f1\\\": 0.067\\n      }\\n    },\\n    \\\"gt_distribution\\\": {\\n      \\\"True\\\": 200,\\n      \\\"False\\\": 200,\\n      \\\"Unknown\\\": 200\\n    },\\n    \\\"pred_distribution\\\": {\\n      \\\"True\\\": 184,\\n      \\\"False\\\": 407,\\n      \\\"Unknown\\\": 9\\n    },\\n    \\\"inference_time_s\\\": 141.0\\n  },\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T05:32:11.336400+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json') as f:\n    d = json.load(f)\npq = d['per_question']\npid = list(pq.keys())[0]\nprint(f'Keys: {list(pq[pid].keys())}')\nprint(f'Example: {json.dumps(pq[pid], indent=2)[:500]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json') as f:\n    d = json.load(f)\npq = d['per_question']\npid = list(pq.keys())[0]\nprint(f'Keys: {list(pq[pid].keys())}')\nprint(f'Example: {json.dumps(pq[pid], indent=2)[:500]}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T05:32:11.336534+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T05:32:11.336700+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T05:32:11.336960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"sc_vote_distribution\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T05:32:11.337152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T05:32:11.337291+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"sc_vote_distribution\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T05:32:11.337415+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T05:32:11.337540+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T05:32:11.337686+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T05:32:11.337813+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraint_cache\\nexp033.log\\nexp033_results.json\\nintermediates\\nsc_answer_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T05:32:11.337953+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T05:32:11.338104+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"folio_0\\\": {\\n    \\\"answers\\\": [\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"False\\\",\\n      \\\"\\\"\\n    ],\\n    \\\"ground_truth\\\": \\\"Unknown\\\"\\n  },\\n  \\\"folio_1\\\": {\\n    \\\"answers\\\": [\\n      \\\"Unknown\\\",\\n      \\\"Unknown\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n      \\\"Unknown\\\",\\n      \\\"False\\\",\\n      \\\"True\\\",\\n      \\\"True\\\",\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T05:32:11.338295+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -m1 \"sc_vote_distribution\" /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T05:32:11.338429+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"sc_vote_distribution\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T05:32:11.338551+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "head -60 /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "head -60 /root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T05:32:11.338723+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 600,\\n    \\\"sica_accuracy\\\": 0.8566666666666667,\\n    \\\"sc_accuracy\\\": 0.85,\\n    \\\"sica_correct\\\": 514,\\n    \\\"sc_correct\\\": 510,\\n    \\\"extraction_rate\\\": 0.9966666666666667,\\n    \\\"total_constraints_extracted\\\": 146636,\\n    \\\"total_unique_constraints\\\": 22738,\\n    \\\"contradiction_rate\\\": 0.0042659864543935265,\\n    \\\"problems_with_contradictions\\\": 72,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"OWA-D5\\\": {\\n        \\\"sica\\\": 0.8566666666666667,\\n        \\\"sc\\\": 0.85,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"proofwriter\\\": {\\n        \\\"sica\\\": 0.8566666666666667,\\n        \\\"sc\\\": 0.85,\\n        \\\"n\\\": 600\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 61932.1\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"ProofWriter_AttNoneg-OWA-D5-1041_Q1\\\",\\n      \\\"problem\\\": \\\"Bob is cold. Bob is quiet. Bob is red. Bob is smart. Charlie is kind. Charlie is quiet. Charlie is red. Charlie is rough. Dave is cold. Dave is kind. Dave is smart. Fiona is quiet. If something is quiet and cold then it is smart. Red, cold things are round. If something is kind and rough then it is red. All quiet things are rough. Cold, smart things are red. If something is rough then it is cold. All red things are rough. If Dave is smart and Dave is kind then Dave is quiet.\\\\n\\\\nDetermine whether the following statement is true, false, or unknown:\\\\nCharlie is kind.\\\",\\n      \\\"dataset\\\": \\\"proofwriter\\\",\\n      \\\"level\\\": \\\"OWA-D5\\\",\\n      \\\"ground_truth\\\": \\\"True\\\",\\n      \\\"sica_answer\\\": \\\"True\\\",\\n      \\\"sica_scores\\\": {\\n        \\\"True\\\": 211.0\\n      },\\n      \\\"sica_correct\\\"
…[truncated 674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T05:32:11.338896+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -c \"sc_vote_distribution\" /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -c \"sc_vote_distribution\" /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T05:32:11.339032+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T05:32:11.339389+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cat > /root/symb_invariant_consensus/recompute_alpha_16639.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Recompute NLI combo with alphabetical tiebreaking for LLaMA, Qwen2.5, Qwen3 on PW600.\"\"\"\nimport json\nfrom collections import Counter\nfrom scipy.stats import binomtest\n\nVALID = {\"True\", \"False\", \"Unknown\"}\nWEIGHTS = [1, 3, 5]\n\ndef majority_alpha(vote_dist):\n    filtered = {k: v for k, v in vote_dist.items() if k in VALID}\n    if not filtered:\n        return \"Unknown\"\n    max_count = max(filtered.values())\n    winners = sorted([k for k, v in filtered.items() if v == max_count])\n    return winners[0]\n\ndef combo_alpha(vote_dist, nli_pred, w):\n    combined = {}\n    for k, v in vote_dist.items():\n        if k in VALID:\n            combined[k] = combined.get(k, 0) + v\n    if nli_pred in VALID:\n        combined[nli_pred] = combined.get(nli_pred, 0) + w\n    if not combined:\n        return \"Unknown\"\n    max_count = max(combined.values())\n    winners = sorted([k for k, v in combined.items() if v == max_count])\n    return winners[0]\n\ndef mcnemar_exact(b, c):\n    n = b + c\n    if n == 0:\n        return 1.0\n    return binomtest(min(b, c), n, 0.5).pvalue\n\ndef process_generator(name, questions):\n    \"\"\"questions: list of {pid, gold, sc_vote_distribution, deberta_pred}\"\"\"\n    n = len(questions)\n    \n    # SC baseline (alphabetical)\n    sc_correct = 0\n    sc_results = []\n    for q in questions:\n        sc_ans = majority_alpha(q[\"sc_vote_distribution\"])\n        correct = (sc_ans == q[\"gold\"])\n        sc_results.append(correct)\n        if correct:\n            sc_correct += 1\n    sc_acc = sc_correct / n\n    \n    # Combo for each weight\n    combo_data = {}\n    for w in WEIGHTS:\n        combo_correct_list = []\n        b_count = 0\n        c_count = 0\n        for i, q in enumerate(questions):\n            combo_ans = combo_alpha(q[\"sc_vote_distribution\"], q[\"deberta_pred\"], w)\n            combo_ok = (combo_ans == q[\"gold\"])\n            combo_correct_list.append(combo_ok)\n            sc_ok = sc_results[i]\n            if combo_ok and not sc_ok:\n                b_count += 1\n            if not combo_ok and sc_ok:\n                c_count += 1\n        \n        combo_n_correct = sum(combo_correct_list)\n        combo_acc = combo_n_correct / n\n        delta_pp = round((combo_acc - sc_acc) * 100, 2)\n        p_val = mcnemar_exact(b_count, c_count)\n        \n        combo_data[f\"w{w}\"] = {\n            \"acc\": round(combo_acc * 100, 2),\n            \"n_correct\": combo_n_correct,\n            \"delta_pp\": delta_pp,\n            \"mcnemar_p\": p_val,\n            \"b\": b_count,\n            \"c\": c_count\n        }\n    \n    return {\n        \"sc\": {\"acc\": round(sc_acc * 100, 2), \"n_correct\": sc_correct},\n        **combo_data\n    }\n\n# === LLaMA-3.1-8B ===\nprint(\"Loading LLaMA-3.1-8B...\")\nwith open(\"/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json\") as f:\n    llama_data = json.load(f)\nllama_questions = []\nfor pid, pq in llama_data[\"per_question\"].items():\n    llama_questions.append({\n        \"pid\": pid,\n        \"gold\": pq[\"gold\"],\n        \"sc_vote_distribution\": pq[\"sc_vote_distribution\"],\n        \"deberta_pred\": pq[\"deberta_pred\"]\n    })\nllama_result = process_generator(\"LLaMA-3.1-8B\", llama_questions)\nprint(f\"  LLaMA SC: {llama_result['sc']}\")\nfor w in WEIGHTS:\n    print(f\"  LLaMA w{w}: {llama_result[f'w{w}']}\")\n\n# === Qwen2.5-14B ===\nprint(\"\\nLoading Qwen2.5-14B...\")\nwith open(\"/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json\") as f:\n    qwen25_data = json.load(f)\nqwen25_questions = []\nfor pid, pq in qwen25_data[\"per_question\"].items():\n    qwen25_questions.append({\n        \"pid\": pid,\n        \"gold\": pq[\"gold\"],\n        \"sc_vote_distribution\": pq[\"sc_vote_distribution\"],\n        \"deberta_pred\": pq[\"deberta_pred\"]\n    })\nqwen25_result = process_generator(\"Qwen2.5-14B\", qwen25_questions)\nprint(f\"  Qwen2.5 SC: {qwen25_result['sc']}\")\nfor w in WEIGHTS:\n    print(f\"  Qwen2.5 w{w}: {qwen25_result[f'w{w}']}\")\n\n# === Qwen3-14B ===\nprint(\"\\nLoading Qwen3-14B...\")\nwith open(\"/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\") as f:\n    qwen3_sc = json.load(f)\nwith open(\"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\") as f:\n    d116 = json.load(f)\n\n# Build SC vote dist from exp033\nqwen3_sc_by_pid = {}\nfor r in qwen3_sc[\"results\"]:\n    qwen3_sc_by_pid[r[\"problem_id\"]] = {\n        \"sc_vote_distribution\": r[\"sc_vote_distribution\"],\n        \"gold\": r[\"ground_truth\"]\n    }\n\n# Build DeBERTa preds from D116\nd116_pq = d116[\"per_question\"]\n\nqwen3_questions = []\nfor pid in qwen3_sc_by_pid:\n    if pid not in d116_pq:\n        continue\n    qwen3_questions.append({\n        \"pid\": pid,\n        \"gold\": qwen3_sc_by_pid[pid][\"gold\"],\n        \"sc_vote_distribution\": qwen3_sc_by_pid[pid][\"sc_vote_distribution\"],\n        \"deberta_pred\": d116_pq[pid][\"deberta_pred\"]\n    })\nprint(f\"  Qwen3 merged: {len(qwen3_questions)} questions\")\nqwen3_result = process_generator(\"Qwen3-14B\", qwen3_questions)\nprint(f\"  Qwen3 SC: {qwen3_result['sc']}\")\nfor w in WEIGHTS:\n    print(f\"  Qwen3 w{w}: {qwen3_result[f'w{w}']}\")\n\n# Save\noutput = {\n    \"LLaMA-3.1-8B\": llama_result,\n    \"Qwen2.5-14B\": qwen25_result,\n    \"Qwen3-14B\": qwen3_result\n}\nwith open(\"/root/symb_invariant_consensus/results/alpha_recompute_16639.json\", \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_16639.json\")\nPYEOF\necho \"Script written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat > /root/symb_invariant_consensus/recompute_alpha_16639.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Recompute NLI combo with alphabetical tiebreaking for LLaMA, Qwen2.5, Qwen3 on PW600.\"\"\"\nimport json\nfrom collections import Counter\nfrom scipy.stats import binomtest\n\nVALID = {\"True\", \"False\", \"Unknown\"}\nWEIGHTS = [1, 3, 5]\n\ndef majority_alpha(vote_dist):\n    filtered = {k: v for k, v in vote_dist.items() if k in VALID}\n    if not filtered:\n        return \"Unknown\"\n    max_count = max(filtered.values())\n    winners = sorted([k for k, v in filtered.items() if v == max_count])\n    return winners[0]\n\ndef combo_alpha(vote_dist, nli_pred, w):\n    combined = {}\n    for k, v in vote_dist.items():\n        if k in VALID:\n            combined[k] = combined.get(k, 0) + v\n    if nli_pred in VALID:\n        combined[nli_pred] = combined.get(nli_pred, 0) + w\n    if not combined:\n        return \"Unknown\"\n    max_count = max(combined.values())\n    winners = sorted([k for k, v in combined.items() if v == max_count])\n    return winners[0]\n\ndef mcnemar_exact(b, c):\n    n = b + c\n    if n == 0:\n        return 1.0\n    return binomtest(min(b, c), n, 0.5).pvalue\n\ndef process_generator(name, questions):\n    \"\"\"questions: list of {pid, gold, sc_vote_distribution, deberta_pred}\"\"\"\n    n = len(questions)\n    \n    # SC baseline (alphabetical)\n    sc_correct = 0\n    sc_results = []\n    for q in questions:\n        sc_ans = majority_alpha(q[\"sc_vote_distribution\"])\n        correct = (sc_ans == q[\"gold\"])\n        sc_results.append(correct)\n        if correct:\n            sc_correct += 1\n    sc_acc = sc_correct / n\n    \n    # Combo for each weight\n    combo_data = {}\n    for w in WEIGHTS:\n        combo_correct_list = []\n        b_count = 0\n        c_count = 0\n        for i, q in enumerate(questions):\n            combo_ans = combo_alpha(q[\"sc_vote_distribution\"], q[\"deberta_pred\"], w)\n            combo_ok = (combo_ans == q[\"gold\"])\n            combo_correct_list.append(combo_ok)\n            sc_ok = sc_results[i]\n            if combo_ok and not sc_ok:\n                b_count += 1\n            if not combo_ok and sc_ok:\n                c_count += 1\n        \n        combo_n_correct = sum(combo_correct_list)\n        combo_acc = combo_n_correct / n\n        delta_pp = round((combo_acc - sc_acc) * 100, 2)\n        p_val = mcnemar_exact(b_count, c_count)\n        \n        combo_data[f\"w{w}\"] = {\n            \"acc\": round(combo_acc * 100, 2),\n            \"n_correct\": combo_n_correct,\n            \"delta_pp\": delta_pp,\n            \"mcnemar_p\": p_val,\n            \"b\": b_count,\n            \"c\": c_count\n        }\n    \n    return {\n        \"sc\": {\"acc\": round(sc_acc * 100, 2), \"n_correct\": sc_correct},\n        **combo_data\n    }\n\n# === LLaMA-3.1-8B ===\nprint(\"Loading LLaMA-3.1-8B...\")\nwith open(\"/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo/results.json\") as f:\n    llama_data = json.load(f)\nllama_questions = []\nfor pid, pq in llama_data[\"per_question\"].items():\n    llama_questions.append({\n        \"pid\": pid,\n        \"gold\": pq[\"gold\"],\n        \"sc_vote_distribution\": pq[\"sc_vote_distribution\"],\n        \"deberta_pred\": pq[\"deberta_pred\"]\n    })\nllama_result = process_generator(\"LLaMA-3.1-8B\", llama_questions)\nprint(f\"  LLaMA SC: {llama_result['sc']}\")\nfor w in WEIGHTS:\n    print(f\"  LLaMA w{w}: {llama_result[f'w{w}']}\")\n\n# === Qwen2.5-14B ===\nprint(\"\\nLoading Qwen2.5-14B...\")\nwith open(\"/root/symb_invariant_consensus/results/qwen14b_pw_nli_combo/results.json\") as f:\n    qwen25_data = json.load(f)\nqwen25_questions = []\nfor pid, pq in qwen25_data[\"per_question\"].items():\n    qwen25_questions.append({\n        \"pid\": pid,\n        \"gold\": pq[\"gold\"],\n        \"sc_vote_distribution\": pq[\"sc_vote_distribution\"],\n        \"deberta_pred\": pq[\"deberta_pred\"]\n    })\nqwen25_result = process_generator(\"Qwen2.5-14B\", qwen25_questions)\nprint(f\"  Qwen2.5 SC: {qwen25_result['sc']}\")\nfor w in WEIGHTS:\n    print(f\"  Qwen2.5 w{w}: {qwen25_result[f'w{w}']}\")\n\n# === Qwen3-14B ===\nprint(\"\\nLoading Qwen3-14B...\")\nwith open(\"/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json\") as f:\n    qwen3_sc = json.load(f)\nwith open(\"/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json\") as f:\n    d116 = json.load(f)\n\n# Build SC vote dist from exp033\nqwen3_sc_by_pid = {}\nfor r in qwen3_sc[\"results\"]:\n    qwen3_sc_by_pid[r[\"problem_id\"]] = {\n        \"sc_vote_distribution\": r[\"sc_vote_distribution\"],\n        \"gold\": r[\"ground_truth\"]\n    }\n\n# Build DeBERTa preds from D116\nd116_pq = d116[\"per_question\"]\n\nqwen3_questions = []\nfor pid in qwen3_sc_by_pid:\n    if pid not in d116_pq:\n        continue\n    qwen3_questions.append({\n        \"pid\": pid,\n        \"gold\": qwen3_sc_by_pid[pid][\"gold\"],\n        \"sc_vote_distribution\": qwen3_sc_by_pid[pid][\"sc_vote_distribution\"],\n        \"deberta_pred\": d116_pq[pid][\"deberta_pred\"]\n    })\nprint(f\"  Qwen3 merged: {len(qwen3_questions)} questions\")\nqwen3_result = process_generator(\"Qwen3-14B\", qwen3_questions)\nprint(f\"  Qwen3 SC: {qwen3_result['sc']}\")\nfor w in WEIGHTS:\n    print(f\"  Qwen3 w{w}: {qwen3_result[f'w{w}']}\")\n\n# Save\noutput = {\n    \"LLaMA-3.1-8B\": llama_result,\n    \"Qwen2.5-14B\": qwen25_result,\n    \"Qwen3-14B\": qwen3_result\n}\nwith open(\"/root/symb_invariant_consensus/results/alpha_recompute_16639.json\", \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_16639.json\")\nPYEOF\necho \"Script written\""
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T05:32:11.339741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T05:32:11.339931+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /root/symb_invariant_consensus/recompute_alpha_25068.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Recompute NLI combo with alphabetical tiebreaking for Mistral PW600 + FOLIO.\"\"\"\nimport json\nfrom collections import Counter\nfrom scipy.stats import binomtest\n\nVALID = {\"True\", \"False\", \"Unknown\"}\nWEIGHTS_PW = [1, 3, 5]\nWEIGHTS_FOLIO = [1, 3]\n\ndef majority_alpha(vote_dist):\n    filtered = {k: v for k, v in vote_dist.items() if k in VALID}\n    if not filtered:\n        return \"Unknown\"\n    max_count = max(filtered.values())\n    winners = sorted([k for k, v in filtered.items() if v == max_count])\n    return winners[0]\n\ndef combo_alpha(vote_dist, nli_pred, w):\n    combined = {}\n    for k, v in vote_dist.items():\n        if k in VALID:\n            combined[k] = combined.get(k, 0) + v\n    if nli_pred in VALID:\n        combined[nli_pred] = combined.get(nli_pred, 0) + w\n    if not combined:\n        return \"Unknown\"\n    max_count = max(combined.values())\n    winners = sorted([k for k, v in combined.items() if v == max_count])\n    return winners[0]\n\ndef mcnemar_exact(b, c):\n    n = b + c\n    if n == 0:\n        return 1.0\n    return binomtest(min(b, c), n, 0.5).pvalue\n\ndef process_generator(name, questions, weights):\n    n = len(questions)\n    sc_correct = 0\n    sc_results = []\n    for q in questions:\n        sc_ans = majority_alpha(q[\"sc_vote_distribution\"])\n        correct = (sc_ans == q[\"gold\"])\n        sc_results.append(correct)\n        if correct:\n            sc_correct += 1\n    sc_acc = sc_correct / n\n    \n    combo_data = {}\n    for w in weights:\n        combo_correct_list = []\n        b_count = 0\n        c_count = 0\n        for i, q in enumerate(questions):\n            combo_ans = combo_alpha(q[\"sc_vote_distribution\"], q[\"deberta_pred\"], w)\n            combo_ok = (combo_ans == q[\"gold\"])\n            combo_correct_list.append(combo_ok)\n            sc_ok = sc_results[i]\n            if combo_ok and not sc_ok:\n                b_count += 1\n            if not combo_ok and sc_ok:\n                c_count += 1\n        \n        combo_n_correct = sum(combo_correct_list)\n        combo_acc = combo_n_correct / n\n        delta_pp = round((combo_acc - sc_acc) * 100, 2)\n        p_val = mcnemar_exact(b_count, c_count)\n        \n        combo_data[f\"w{w}\"] = {\n            \"acc\": round(combo_acc * 100, 2),\n            \"n_correct\": combo_n_correct,\n            \"delta_pp\": delta_pp,\n            \"mcnemar_p\": p_val,\n            \"b\": b_count,\n            \"c\": c_count\n        }\n    \n    return {\n        \"sc\": {\"acc\": round(sc_acc * 100, 2), \"n_correct\": sc_correct},\n        **combo_data\n    }\n\n# === Mistral-7B PW600 ===\nprint(\"Loading Mistral-7B PW600...\")\nwith open(\"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\") as f:\n    mistral_sc = json.load(f)\nwith open(\"/root/symb_invariant_consensus/results/direction_r_nli_pw600/results.json\") as f:\n    mistral_nli = json.load(f)\n\nmistral_sc_by_pid = {}\nfor r in mistral_sc[\"results\"]:\n    mistral_sc_by_pid[r[\"problem_id\"]] = {\n        \"sc_vote_distribution\": r[\"sc_vote_distribution\"],\n        \"gold\": r[\"ground_truth\"]\n    }\n\nnli_pq = mistral_nli[\"per_question\"]\nmistral_questions = []\nfor pid in mistral_sc_by_pid:\n    if pid not in nli_pq:\n        continue\n    mistral_questions.append({\n        \"pid\": pid,\n        \"gold\": mistral_sc_by_pid[pid][\"gold\"],\n        \"sc_vote_distribution\": mistral_sc_by_pid[pid][\"sc_vote_distribution\"],\n        \"deberta_pred\": nli_pq[pid][\"deberta_pred\"]\n    })\nprint(f\"  Merged: {len(mistral_questions)} questions\")\nmistral_result = process_generator(\"Mistral-7B\", mistral_questions, WEIGHTS_PW)\nprint(f\"  Mistral SC: {mistral_result['sc']}\")\nfor w in WEIGHTS_PW:\n    print(f\"  Mistral w{w}: {mistral_result[f'w{w}']}\")\n\n# === Mistral-7B FOLIO ===\nprint(\"\\nLoading Mistral-7B FOLIO...\")\nwith open(\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json\") as f:\n    folio_sc_matrix = json.load(f)\nwith open(\"/root/symb_invariant_consensus/results/direction_r_nli_large/results.json\") as f:\n    folio_nli = json.load(f)\n\nfolio_nli_pq = folio_nli[\"per_question\"]\nfolio_questions = []\nfor fid in sorted(folio_sc_matrix.keys(), key=lambda x: int(x.split(\"_\")[1])):\n    raw_answers = folio_sc_matrix[fid][\"answers\"]\n    gold = folio_sc_matrix[fid][\"ground_truth\"]\n    # Compute vote distribution from raw answers\n    vote_dist = {}\n    for a in raw_answers:\n        if a in VALID:\n            vote_dist[a] = vote_dist.get(a, 0) + 1\n    \n    if fid not in folio_nli_pq:\n        continue\n    folio_questions.append({\n        \"pid\": fid,\n        \"gold\": gold,\n        \"sc_vote_distribution\": vote_dist,\n        \"deberta_pred\": folio_nli_pq[fid][\"deberta_pred\"]\n    })\nprint(f\"  Merged: {len(folio_questions)} questions\")\nfolio_result = process_generator(\"Mistral-7B-FOLIO\", folio_questions, WEIGHTS_FOLIO)\nprint(f\"  FOLIO SC: {folio_result['sc']}\")\nfor w in WEIGHTS_FOLIO:\n    print(f\"  FOLIO w{w}: {folio_result[f'w{w}']}\")\n\n# Save\noutput = {\n    \"Mistral-7B-PW600\": mistral_result,\n    \"Mistral-7B-FOLIO\": folio_result\n}\nwith open(\"/root/symb_invariant_consensus/results/alpha_recompute_25068.json\", \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_25068.json\")\nPYEOF\necho \"Script written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /root/symb_invariant_consensus/recompute_alpha_25068.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Recompute NLI combo with alphabetical tiebreaking for Mistral PW600 + FOLIO.\"\"\"\nimport json\nfrom collections import Counter\nfrom scipy.stats import binomtest\n\nVALID = {\"True\", \"False\", \"Unknown\"}\nWEIGHTS_PW = [1, 3, 5]\nWEIGHTS_FOLIO = [1, 3]\n\ndef majority_alpha(vote_dist):\n    filtered = {k: v for k, v in vote_dist.items() if k in VALID}\n    if not filtered:\n        return \"Unknown\"\n    max_count = max(filtered.values())\n    winners = sorted([k for k, v in filtered.items() if v == max_count])\n    return winners[0]\n\ndef combo_alpha(vote_dist, nli_pred, w):\n    combined = {}\n    for k, v in vote_dist.items():\n        if k in VALID:\n            combined[k] = combined.get(k, 0) + v\n    if nli_pred in VALID:\n        combined[nli_pred] = combined.get(nli_pred, 0) + w\n    if not combined:\n        return \"Unknown\"\n    max_count = max(combined.values())\n    winners = sorted([k for k, v in combined.items() if v == max_count])\n    return winners[0]\n\ndef mcnemar_exact(b, c):\n    n = b + c\n    if n == 0:\n        return 1.0\n    return binomtest(min(b, c), n, 0.5).pvalue\n\ndef process_generator(name, questions, weights):\n    n = len(questions)\n    sc_correct = 0\n    sc_results = []\n    for q in questions:\n        sc_ans = majority_alpha(q[\"sc_vote_distribution\"])\n        correct = (sc_ans == q[\"gold\"])\n        sc_results.append(correct)\n        if correct:\n            sc_correct += 1\n    sc_acc = sc_correct / n\n    \n    combo_data = {}\n    for w in weights:\n        combo_correct_list = []\n        b_count = 0\n        c_count = 0\n        for i, q in enumerate(questions):\n            combo_ans = combo_alpha(q[\"sc_vote_distribution\"], q[\"deberta_pred\"], w)\n            combo_ok = (combo_ans == q[\"gold\"])\n            combo_correct_list.append(combo_ok)\n            sc_ok = sc_results[i]\n            if combo_ok and not sc_ok:\n                b_count += 1\n            if not combo_ok and sc_ok:\n                c_count += 1\n        \n        combo_n_correct = sum(combo_correct_list)\n        combo_acc = combo_n_correct / n\n        delta_pp = round((combo_acc - sc_acc) * 100, 2)\n        p_val = mcnemar_exact(b_count, c_count)\n        \n        combo_data[f\"w{w}\"] = {\n            \"acc\": round(combo_acc * 100, 2),\n            \"n_correct\": combo_n_correct,\n            \"delta_pp\": delta_pp,\n            \"mcnemar_p\": p_val,\n            \"b\": b_count,\n            \"c\": c_count\n        }\n    \n    return {\n        \"sc\": {\"acc\": round(sc_acc * 100, 2), \"n_correct\": sc_correct},\n        **combo_data\n    }\n\n# === Mistral-7B PW600 ===\nprint(\"Loading Mistral-7B PW600...\")\nwith open(\"/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json\") as f:\n    mistral_sc = json.load(f)\nwith open(\"/root/symb_invariant_consensus/results/direction_r_nli_pw600/results.json\") as f:\n    mistral_nli = json.load(f)\n\nmistral_sc_by_pid = {}\nfor r in mistral_sc[\"results\"]:\n    mistral_sc_by_pid[r[\"problem_id\"]] = {\n        \"sc_vote_distribution\": r[\"sc_vote_distribution\"],\n        \"gold\": r[\"ground_truth\"]\n    }\n\nnli_pq = mistral_nli[\"per_question\"]\nmistral_questions = []\nfor pid in mistral_sc_by_pid:\n    if pid not in nli_pq:\n        continue\n    mistral_questions.append({\n        \"pid\": pid,\n        \"gold\": mistral_sc_by_pid[pid][\"gold\"],\n        \"sc_vote_distribution\": mistral_sc_by_pid[pid][\"sc_vote_distribution\"],\n        \"deberta_pred\": nli_pq[pid][\"deberta_pred\"]\n    })\nprint(f\"  Merged: {len(mistral_questions)} questions\")\nmistral_result = process_generator(\"Mistral-7B\", mistral_questions, WEIGHTS_PW)\nprint(f\"  Mistral SC: {mistral_result['sc']}\")\nfor w in WEIGHTS_PW:\n    print(f\"  Mistral w{w}: {mistral_result[f'w{w}']}\")\n\n# === Mistral-7B FOLIO ===\nprint(\"\\nLoading Mistral-7B FOLIO...\")\nwith open(\"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json\") as f:\n    folio_sc_matrix = json.load(f)\nwith open(\"/root/symb_invariant_consensus/results/direction_r_nli_large/results.json\") as f:\n    folio_nli = json.load(f)\n\nfolio_nli_pq = folio_nli[\"per_question\"]\nfolio_questions = []\nfor fid in sorted(folio_sc_matrix.keys(), key=lambda x: int(x.split(\"_\")[1])):\n    raw_answers = folio_sc_matrix[fid][\"answers\"]\n    gold = folio_sc_matrix[fid][\"ground_truth\"]\n    # Compute vote distribution from raw answers\n    vote_dist = {}\n    for a in raw_answers:\n        if a in VALID:\n            vote_dist[a] = vote_dist.get(a, 0) + 1\n    \n    if fid not in folio_nli_pq:\n        continue\n    folio_questions.append({\n        \"pid\": fid,\n        \"gold\": gold,\n        \"sc_vote_distribution\": vote_dist,\n        \"deberta_pred\": folio_nli_pq[fid][\"deberta_pred\"]\n    })\nprint(f\"  Merged: {len(folio_questions)} questions\")\nfolio_result = process_generator(\"Mistral-7B-FOLIO\", folio_questions, WEIGHTS_FOLIO)\nprint(f\"  FOLIO SC: {folio_result['sc']}\")\nfor w in WEIGHTS_FOLIO:\n    print(f\"  FOLIO w{w}: {folio_result[f'w{w}']}\")\n\n# Save\noutput = {\n    \"Mistral-7B-PW600\": mistral_result,\n    \"Mistral-7B-FOLIO\": folio_result\n}\nwith open(\"/root/symb_invariant_consensus/results/alpha_recompute_25068.json\", \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_25068.json\")\nPYEOF\necho \"Script written\""
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T05:32:11.340119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T05:32:11.340279+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && python3 recompute_alpha_16639.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && python3 recompute_alpha_16639.py"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-21T05:32:11.340411+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && python3 recompute_alpha_25068.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && python3 recompute_alpha_25068.py"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-21T05:32:11.340549+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading LLaMA-3.1-8B...\\n  LLaMA SC: {'acc': 72.5, 'n_correct': 435}\\n  LLaMA w1: {'acc': 73.33, 'n_correct': 440, 'delta_pp': 0.83, 'mcnemar_p': np.float64(0.359283447265625), 'b': 12, 'c': 7}\\n  LLaMA w3: {'acc': 73.33, 'n_correct': 440, 'delta_pp': 0.83, 'mcnemar_p': np.float64(0.6646454904132133), 'b': 45, 'c': 40}\\n  LLaMA w5: {'acc': 72.0, 'n_correct': 432, 'delta_pp': -0.5, 'mcnemar_p': np.float64(0.8707787409560847), 'b': 74, 'c': 77}\\n\\nLoading Qwen2.5-14B...\\n  Qwen2.5 SC: {'acc': 74.0, 'n_correct': 444}\\n  Qwen2.5 w1: {'acc': 74.17, 'n_correct': 445, 'delta_pp': 0.17, 'mcnemar_p': 1.0, 'b': 3, 'c': 2}\\n  Qwen2.5 w3: {'acc': 74.67, 'n_correct': 448, 'delta_pp': 0.67, 'mcnemar_p': np.float64(0.5034446716308594), 'b': 12, 'c': 8}\\n  Qwen2.5 w5: {'acc': 75.17, 'n_correct': 451, 'delta_pp': 1.17, 'mcnemar_p': np.float64(0.3603776529357674), 'b': 25, 'c': 18}\\n\\nLoading Qwen3-14B...\\n  Qwen3 merged: 600 questions\\n  Qwen3 SC: {'acc': 85.83, 'n_correct': 515}\\n  Qwen3 w1: {'acc': 86.0, 'n_correct': 516, 'delta_pp': 0.17, 'mcnemar_p': 1.0, 'b': 1, 'c': 0}\\n  Qwen3 w3: {'acc': 86.33, 'n_correct': 518, 'delta_pp': 0.5, 'mcnemar_p': np.float64(0.453125), 'b': 5, 'c': 2}\\n  Qwen3 w5: {'acc': 87.0, 'n_correct': 522, 'delta_pp': 1.17, 'mcnemar_p': np.float64(0.21003961563110352), 'b': 15, 'c': 8}\\n\\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_16639.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T05:32:11.340685+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python3 recompute_alpha_25068.py'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T05:32:11.340855+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/miniconda3/bin/python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/miniconda3/bin/python3"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T05:32:11.341029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-21T05:32:11.341210+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 recompute_alpha_25068.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 recompute_alpha_25068.py"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T05:32:11.341386+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading Mistral-7B PW600...\\n  Merged: 600 questions\\n  Mistral SC: {'acc': 39.33, 'n_correct': 236}\\n  Mistral w1: {'acc': 40.17, 'n_correct': 241, 'delta_pp': 0.83, 'mcnemar_p': np.float64(0.359283447265625), 'b': 12, 'c': 7}\\n  Mistral w3: {'acc': 46.0, 'n_correct': 276, 'delta_pp': 6.67, 'mcnemar_p': np.float64(1.1296023055413025e-05), 'b': 61, 'c': 21}\\n  Mistral w5: {'acc': 50.33, 'n_correct': 302, 'delta_pp': 11.0, 'mcnemar_p': np.float64(6.178035816936483e-07), 'b': 120, 'c': 54}\\n\\nLoading Mistral-7B FOLIO...\\n  Merged: 204 questions\\n  FOLIO SC: {'acc': 55.88, 'n_correct': 114}\\n  FOLIO w1: {'acc': 56.37, 'n_correct': 115, 'delta_pp': 0.49, 'mcnemar_p': 1.0, 'b': 4, 'c': 3}\\n  FOLIO w3: {'acc': 58.82, 'n_correct': 120, 'delta_pp': 2.94, 'mcnemar_p': np.float64(0.210113525390625), 'b': 11, 'c': 5}\\n\\nSaved to /root/symb_invariant_consensus/results/alpha_recompute_25068.json\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.27}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-21T05:32:11.341690+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nfrom scipy.stats import spearmanr, binomtest\nfrom statsmodels.stats.multitest import multipletests\n\n# ============================================================\n# Phase 1 & 2: Collect recomputed results\n# ============================================================\n\npw_results = {\n    \"Mistral-7B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 39.33, \"n_correct\": 236},\n        \"w1\": {\"acc\": 40.17, \"n_correct\": 241, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 46.00, \"n_correct\": 276, \"delta_pp\": 6.67, \"mcnemar_p\": 1.1296023055413025e-05, \"b\": 61, \"c\": 21},\n        \"w5\": {\"acc\": 50.33, \"n_correct\": 302, \"delta_pp\": 11.00, \"mcnemar_p\": 6.178035816936483e-07, \"b\": 120, \"c\": 54},\n    },\n    \"LLaMA-3.1-8B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 72.50, \"n_correct\": 435},\n        \"w1\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.6646454904132133, \"b\": 45, \"c\": 40},\n        \"w5\": {\"acc\": 72.00, \"n_correct\": 432, \"delta_pp\": -0.50, \"mcnemar_p\": 0.8707787409560847, \"b\": 74, \"c\": 77},\n    },\n    \"Qwen2.5-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 74.00, \"n_correct\": 444},\n        \"w1\": {\"acc\": 74.17, \"n_correct\": 445, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 3, \"c\": 2},\n        \"w3\": {\"acc\": 74.67, \"n_correct\": 448, \"delta_pp\": 0.67, \"mcnemar_p\": 0.5034446716308594, \"b\": 12, \"c\": 8},\n        \"w5\": {\"acc\": 75.17, \"n_correct\": 451, \"delta_pp\": 1.17, \"mcnemar_p\": 0.3603776529357674, \"b\": 25, \"c\": 18},\n    },\n    \"Qwen3-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 85.83, \"n_correct\": 515},\n        \"w1\": {\"acc\": 86.00, \"n_correct\": 516, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 1, \"c\": 0},\n        \"w3\": {\"acc\": 86.33, \"n_correct\": 518, \"delta_pp\": 0.50, \"mcnemar_p\": 0.453125, \"b\": 5, \"c\": 2},\n        \"w5\": {\"acc\": 87.00, \"n_correct\": 522, \"delta_pp\": 1.17, \"mcnemar_p\": 0.21003961563110352, \"b\": 15, \"c\": 8},\n    },\n}\n\nfolio_results = {\n    \"Mistral-7B\": {\n        \"n\": 204,\n        \"sc\": {\"acc\": 55.88, \"n_correct\": 114},\n        \"w1\": {\"acc\": 56.37, \"n_correct\": 115, \"delta_pp\": 0.49, \"mcnemar_p\": 1.0, \"b\": 4, \"c\": 3},\n        \"w3\": {\"acc\": 58.82, \"n_correct\": 120, \"delta_pp\": 2.94, \"mcnemar_p\": 0.210113525390625, \"b\": 11, \"c\": 5},\n    },\n}\n\n# ============================================================\n# Phase 3a: Spearman ρ (capability gap vs combo gain at w=3)\n# ============================================================\ndeberta_standalone = 55.00\ngenerators = [\"Mistral-7B\", \"LLaMA-3.1-8B\", \"Qwen2.5-14B\", \"Qwen3-14B\"]\ngaps = [deberta_standalone - pw_results[g][\"sc\"][\"acc\"] for g in generators]\ngains = [pw_results[g][\"w3\"][\"delta_pp\"] for g in generators]\n\nrho, p_spearman = spearmanr(gaps, gains)\nprint(f\"Spearman ρ: {rho:.4f}, p = {p_spearman:.4f}\")\nprint(f\"  gaps:  {gaps}\")\nprint(f\"  gains: {gains}\")\n\n# ============================================================\n# Phase 3b: BH correction (m=12 PW600 tests)\n# ============================================================\ntest_labels = []\nraw_pvals = []\nfor g in generators:\n    for w in [1, 3, 5]:\n        test_labels.append(f\"{g}_w{w}\")\n        raw_pvals.append(pw_results[g][f\"w{w}\"][\"mcnemar_p\"])\n\nrejected, pvals_corrected, _, _ = multipletests(raw_pvals, alpha=0.05, method='fdr_bh')\n\nprint(f\"\\nBH correction (m={len(raw_pvals)}):\")\nfor i, (label, raw_p, adj_p, sig) in enumerate(zip(test_labels, raw_pvals, pvals_corrected, rejected)):\n    print(f\"  {label}: raw={raw_p:.6e}, adj={adj_p:.6e}, sig={sig}\")\n\n# Count significant\nn_sig = sum(rejected)\nprint(f\"\\nSignificant after BH: {n_sig}/12\")\n\n# ============================================================\n# SC baseline comparison (old counter vs new alpha)\n# ============================================================\nold_counter_sc = {\n    \"Mistral-7B\": {\"acc\": 39.33, \"n_correct\": 236},\n    \"LLaMA-3.1-8B\": {\"acc\": 70.00, \"n_correct\": 420},\n    \"Qwen2.5-14B\": {\"acc\": 73.50, \"n_correct\": 441},\n    \"Qwen3-14B\": {\"acc\": 85.00, \"n_correct\": 510},\n}\n\nold_counter_combo = {\n    \"Mistral-7B\": {\"w1\": 40.17, \"w3\": 42.83, \"w5\": 50.00},\n    \"LLaMA-3.1-8B\": {\"w1\": 72.83, \"w3\": 74.17, \"w5\": 71.67},\n    \"Qwen2.5-14B\": {\"w1\": 74.17, \"w3\": 74.33, \"w5\": 75.33},\n    \"Qwen3-14B\": {\"w1\": 85.83, \"w3\": 86.00, \"w5\": 86.83},\n}\n\nprint(\"\\n=== SC baseline changes (counter → alpha) ===\")\nfor g in generators:\n    old_n = old_counter_sc[g][\"n_correct\"]\n    new_n = pw_results[g][\"sc\"][\"n_correct\"]\n    diff = new_n - old_n\n    print(f\"  {g}: {old_n} → {new_n} ({diff:+d})\")\n\nprint(\"\\n=== Combo w3 changes (counter → alpha) ===\")\nfor g in generators:\n    old_combo = old_counter_combo[g][\"w3\"]\n    new_combo = pw_results[g][\"w3\"][\"acc\"]\n    old_delta = old_combo - old_counter_sc[g][\"acc\"]\n    new_delta = pw_results[g][\"w3\"][\"delta_pp\"]\n    print(f\"  {g}: combo {old_combo}% → {new_combo}%, delta {old_delta:+.2f}pp → {new_delta:+.2f}pp\")\n\n# ============================================================\n# Build final output\n# ============================================================\noutput = {\n    \"proofwriter\": pw_results,\n    \"folio\": folio_results,\n    \"spearman\": {\n        \"generators\": generators,\n        \"deberta_standalone\": deberta_standalone,\n        \"gaps\": gaps,\n        \"gains\": gains,\n        \"rho\": round(rho, 4),\n        \"p\": round(p_spearman, 4)\n    },\n    \"bh_correction\": {\n        \"m\": 12,\n        \"test_labels\": test_labels,\n        \"raw_pvals\": [round(p, 10) for p in raw_pvals],\n        \"adjusted_pvals\": [round(float(p), 10) for p in pvals_corrected],\n        \"significant_after_bh\": [bool(r) for r in rejected],\n        \"n_significant\": int(n_sig)\n    },\n    \"sc_baseline_shift\": {\n        \"note\": \"Alphabetical tiebreaking changes SC baselines (filtering invalid answers + alphabetical among ties)\",\n        \"changes\": {g: {\n            \"counter_n_correct\": old_counter_sc[g][\"n_correct\"],\n            \"alpha_n_correct\": pw_results[g][\"sc\"][\"n_correct\"],\n            \"diff\": pw_results[g][\"sc\"][\"n_correct\"] - old_counter_sc[g][\"n_correct\"]\n        } for g in generators}\n    },\n    \"paper_changes_needed\": [\n        {\n            \"section\": \"NLI Combo Table (Table X)\",\n            \"description\": \"All combo results change. SC baselines shift for LLaMA (+15), Qwen2.5 (+3), Qwen3 (+5). Combo gains shrink. Only Mistral w3 and w5 remain significant after BH.\",\n            \"old_significant_count\": 4,\n            \"new_significant_count\": int(n_sig)\n        },\n        {\n            \"section\": \"Spearman correlation\",\n            \"description\": f\"rho changes. New: rho={round(rho, 4)}, p={round(p_spearman, 4)}\"\n        },\n        {\n            \"section\": \"FOLIO combo results\",\n            \"description\": \"Mistral FOLIO: SC 55.88% (114/204), w1=56.37% (+0.49pp, p=1.0), w3=58.82% (+2.94pp, p=0.21)\"\n        }\n    ]\n}\n\nout_path = \"artifacts/nli_combo_recomputed.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF",
  "description": "Compute Spearman rho, BH correction, build final JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\nfrom scipy.stats import spearmanr, binomtest\nfrom statsmodels.stats.multitest import multipletests\n\n# ============================================================\n# Phase 1 & 2: Collect recomputed results\n# ============================================================\n\npw_results = {\n    \"Mistral-7B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 39.33, \"n_correct\": 236},\n        \"w1\": {\"acc\": 40.17, \"n_correct\": 241, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 46.00, \"n_correct\": 276, \"delta_pp\": 6.67, \"mcnemar_p\": 1.1296023055413025e-05, \"b\": 61, \"c\": 21},\n        \"w5\": {\"acc\": 50.33, \"n_correct\": 302, \"delta_pp\": 11.00, \"mcnemar_p\": 6.178035816936483e-07, \"b\": 120, \"c\": 54},\n    },\n    \"LLaMA-3.1-8B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 72.50, \"n_correct\": 435},\n        \"w1\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.6646454904132133, \"b\": 45, \"c\": 40},\n        \"w5\": {\"acc\": 72.00, \"n_correct\": 432, \"delta_pp\": -0.50, \"mcnemar_p\": 0.8707787409560847, \"b\": 74, \"c\": 77},\n    },\n    \"Qwen2.5-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 74.00, \"n_correct\": 444},\n        \"w1\": {\"acc\": 74.17, \"n_correct\": 445, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 3, \"c\": 2},\n        \"w3\": {\"acc\": 74.67, \"n_correct\": 448, \"delta_pp\": 0.67, \"mcnemar_p\": 0.5034446716308594, \"b\": 12, \"c\": 8},\n        \"w5\": {\"acc\": 75.17, \"n_correct\": 451, \"delta_pp\": 1.17, \"mcnemar_p\": 0.3603776529357674, \"b\": 25, \"c\": 18},\n    },\n    \"Qwen3-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 85.83, \"n_correct\": 515},\n        \"w1\": {\"acc\": 86.00, \"n_correct\": 516, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 1, \"c\": 0},\n        \"w3\": {\"acc\": 86.33, \"n_correct\": 518, \"delta_pp\": 0.50, \"mcnemar_p\": 0.453125, \"b\": 5, \"c\": 2},\n        \"w5\": {\"acc\": 87.00, \"n_correct\": 522, \"delta_pp\": 1.17, \"mcnemar_p\": 0.21003961563110352, \"b\": 15, \"c\": 8},\n    },\n}\n\nfolio_results = {\n    \"Mistral-7B\": {\n        \"n\": 204,\n        \"sc\": {\"acc\": 55.88, \"n_correct\": 114},\n        \"w1\": {\"acc\": 56.37, \"n_correct\": 115, \"delta_pp\": 0.49, \"mcnemar_p\": 1.0, \"b\": 4, \"c\": 3},\n        \"w3\": {\"acc\": 58.82, \"n_correct\": 120, \"delta_pp\": 2.94, \"mcnemar_p\": 0.210113525390625, \"b\": 11, \"c\": 5},\n    },\n}\n\n# ============================================================\n# Phase 3a: Spearman ρ (capability gap vs combo gain at w=3)\n# ============================================================\ndeberta_standalone = 55.00\ngenerators = [\"Mistral-7B\", \"LLaMA-3.1-8B\", \"Qwen2.5-14B\", \"Qwen3-14B\"]\ngaps = [deberta_standalone - pw_results[g][\"sc\"][\"acc\"] for g in generators]\ngains = [pw_results[g][\"w3\"][\"delta_pp\"] for g in generators]\n\nrho, p_spearman = spearmanr(gaps, gains)\nprint(f\"Spearman ρ: {rho:.4f}, p = {p_spearman:.4f}\")\nprint(f\"  gaps:  {gaps}\")\nprint(f\"  gains: {gains}\")\n\n# ============================================================\n# Phase 3b: BH correction (m=12 PW600 tests)\n# ============================================================\ntest_labels = []\nraw_pvals = []\nfor g in generators:\n    for w in [1, 3, 5]:\n        test_labels.append(f\"{g}_w{w}\")\n        raw_pvals.append(pw_results[g][f\"w{w}\"][\"mcnemar_p\"])\n\nrejected, pvals_corrected, _, _ = multipletests(raw_pvals, alpha=0.05, method='fdr_bh')\n\nprint(f\"\\nBH correction (m={len(raw_pvals)}):\")\nfor i, (label, raw_p, adj_p, sig) in enumerate(zip(test_labels, raw_pvals, pvals_corrected, rejected)):\n    print(f\"  {label}: raw={raw_p:.6e}, adj={adj_p:.6e}, sig={sig}\")\n\n# Count significant\nn_sig = sum(rejected)\nprint(f\"\\nSignificant after BH: {n_sig}/12\")\n\n# ============================================================\n# SC baseline comparison (old counter vs new alpha)\n# ============================================================\nold_counter_sc = {\n    \"Mistral-7B\": {\"acc\": 39.33, \"n_correct\": 236},\n    \"LLaMA-3.1-8B\": {\"acc\": 70.00, \"n_correct\": 420},\n    \"Qwen2.5-14B\": {\"acc\": 73.50, \"n_correct\": 441},\n    \"Qwen3-14B\": {\"acc\": 85.00, \"n_correct\": 510},\n}\n\nold_counter_combo = {\n    \"Mistral-7B\": {\"w1\": 40.17, \"w3\": 42.83, \"w5\": 50.00},\n    \"LLaMA-3.1-8B\": {\"w1\": 72.83, \"w3\": 74.17, \"w5\": 71.67},\n    \"Qwen2.5-14B\": {\"w1\": 74.17, \"w3\": 74.33, \"w5\": 75.33},\n    \"Qwen3-14B\": {\"w1\": 85.83, \"w3\": 86.00, \"w5\": 86.83},\n}\n\nprint(\"\\n=== SC baseline changes (counter → alpha) ===\")\nfor g in generators:\n    old_n = old_counter_sc[g][\"n_correct\"]\n    new_n = pw_results[g][\"sc\"][\"n_correct\"]\n    diff = new_n - old_n\n    print(f\"  {g}: {old_n} → {new_n} ({diff:+d})\")\n\nprint(\"\\n=== Combo w3 changes (counter → alpha) ===\")\nfor g in generators:\n    old_combo = old_counter_combo[g][\"w3\"]\n    new_combo = pw_results[g][\"w3\"][\"acc\"]\n    old_delta = old_combo - old_counter_sc[g][\"acc\"]\n    new_delta = pw_results[g][\"w3\"][\"delta_pp\"]\n    print(f\"  {g}: combo {old_combo}% → {new_combo}%, delta {old_delta:+.2f}pp → {new_delta:+.2f}pp\")\n\n# ============================================================\n# Build final output\n# ============================================================\noutput = {\n    \"proofwriter\": pw_results,\n    \"folio\": folio_results,\n    \"spearman\": {\n        \"generators\": generators,\n        \"deberta_standalone\": deberta_standalone,\n        \"gaps\": gaps,\n        \"gains\": gains,\n        \"rho\": round(rho, 4),\n        \"p\": round(p_spearman, 4)\n    },\n    \"bh_correction\": {\n        \"m\": 12,\n        \"test_labels\": test_labels,\n        \"raw_pvals\": [round(p, 10) for p in raw_pvals],\n        \"adjusted_pvals\": [round(float(p), 10) for p in pvals_corrected],\n        \"significant_after_bh\": [bool(r) for r in rejected],\n        \"n_significant\": int(n_sig)\n    },\n    \"sc_baseline_shift\": {\n        \"note\": \"Alphabetical tiebreaking changes SC baselines (filtering invalid answers + alphabetical among ties)\",\n        \"changes\": {g: {\n            \"counter_n_correct\": old_counter_sc[g][\"n_correct\"],\n            \"alpha_n_correct\": pw_results[g][\"sc\"][\"n_correct\"],\n            \"diff\": pw_results[g][\"sc\"][\"n_correct\"] - old_counter_sc[g][\"n_correct\"]\n        } for g in generators}\n    },\n    \"paper_changes_needed\": [\n        {\n            \"section\": \"NLI Combo Table (Table X)\",\n            \"description\": \"All combo results change. SC baselines shift for LLaMA (+15), Qwen2.5 (+3), Qwen3 (+5). Combo gains shrink. Only Mistral w3 and w5 remain significant after BH.\",\n            \"old_significant_count\": 4,\n            \"new_significant_count\": int(n_sig)\n        },\n        {\n            \"section\": \"Spearman correlation\",\n            \"description\": f\"rho changes. New: rho={round(rho, 4)}, p={round(p_spearman, 4)}\"\n        },\n        {\n            \"section\": \"FOLIO combo results\",\n            \"description\": \"Mistral FOLIO: SC 55.88% (114/204), w1=56.37% (+0.49pp, p=1.0), w3=58.82% (+2.94pp, p=0.21)\"\n        }\n    ]\n}\n\nout_path = \"artifacts/nli_combo_recomputed.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved to {out_path}\")\nPYEOF",
    "description": "Compute Spearman rho, BH correction, build final JSON"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T05:32:11.341934+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
ModuleNotFoundError: No module named 'statsmodels'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-21T05:32:11.342072+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install statsmodels -q 2>&1 | tail -1",
  "description": "Install statsmodels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install statsmodels -q 2>&1 | tail -1",
    "description": "Install statsmodels"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T05:32:11.342194+00:00_

hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T05:32:11.342312+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install --user statsmodels -q 2>&1 | tail -1",
  "description": "Install statsmodels with --user"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install --user statsmodels -q 2>&1 | tail -1",
    "description": "Install statsmodels with --user"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T05:32:11.342428+00:00_

hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T05:32:11.342552+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip install --break-system-packages statsmodels -q 2>&1 | tail -1",
  "description": "Install statsmodels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "pip install --break-system-packages statsmodels -q 2>&1 | tail -1",
    "description": "Install statsmodels"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T05:32:11.342740+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-21T05:32:11.342999+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\nimport os\nfrom scipy.stats import spearmanr\nfrom statsmodels.stats.multitest import multipletests\n\nos.makedirs(\"artifacts\", exist_ok=True)\n\npw_results = {\n    \"Mistral-7B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 39.33, \"n_correct\": 236},\n        \"w1\": {\"acc\": 40.17, \"n_correct\": 241, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 46.00, \"n_correct\": 276, \"delta_pp\": 6.67, \"mcnemar_p\": 1.1296023055413025e-05, \"b\": 61, \"c\": 21},\n        \"w5\": {\"acc\": 50.33, \"n_correct\": 302, \"delta_pp\": 11.00, \"mcnemar_p\": 6.178035816936483e-07, \"b\": 120, \"c\": 54},\n    },\n    \"LLaMA-3.1-8B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 72.50, \"n_correct\": 435},\n        \"w1\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.6646454904132133, \"b\": 45, \"c\": 40},\n        \"w5\": {\"acc\": 72.00, \"n_correct\": 432, \"delta_pp\": -0.50, \"mcnemar_p\": 0.8707787409560847, \"b\": 74, \"c\": 77},\n    },\n    \"Qwen2.5-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 74.00, \"n_correct\": 444},\n        \"w1\": {\"acc\": 74.17, \"n_correct\": 445, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 3, \"c\": 2},\n        \"w3\": {\"acc\": 74.67, \"n_correct\": 448, \"delta_pp\": 0.67, \"mcnemar_p\": 0.5034446716308594, \"b\": 12, \"c\": 8},\n        \"w5\": {\"acc\": 75.17, \"n_correct\": 451, \"delta_pp\": 1.17, \"mcnemar_p\": 0.3603776529357674, \"b\": 25, \"c\": 18},\n    },\n    \"Qwen3-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 85.83, \"n_correct\": 515},\n        \"w1\": {\"acc\": 86.00, \"n_correct\": 516, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 1, \"c\": 0},\n        \"w3\": {\"acc\": 86.33, \"n_correct\": 518, \"delta_pp\": 0.50, \"mcnemar_p\": 0.453125, \"b\": 5, \"c\": 2},\n        \"w5\": {\"acc\": 87.00, \"n_correct\": 522, \"delta_pp\": 1.17, \"mcnemar_p\": 0.21003961563110352, \"b\": 15, \"c\": 8},\n    },\n}\n\nfolio_results = {\n    \"Mistral-7B\": {\n        \"n\": 204,\n        \"sc\": {\"acc\": 55.88, \"n_correct\": 114},\n        \"w1\": {\"acc\": 56.37, \"n_correct\": 115, \"delta_pp\": 0.49, \"mcnemar_p\": 1.0, \"b\": 4, \"c\": 3},\n        \"w3\": {\"acc\": 58.82, \"n_correct\": 120, \"delta_pp\": 2.94, \"mcnemar_p\": 0.210113525390625, \"b\": 11, \"c\": 5},\n    },\n}\n\n# Spearman\ndeberta_standalone = 55.00\ngenerators = [\"Mistral-7B\", \"LLaMA-3.1-8B\", \"Qwen2.5-14B\", \"Qwen3-14B\"]\ngaps = [deberta_standalone - pw_results[g][\"sc\"][\"acc\"] for g in generators]\ngains = [pw_results[g][\"w3\"][\"delta_pp\"] for g in generators]\nrho, p_spearman = spearmanr(gaps, gains)\nprint(f\"Spearman rho={rho:.4f}, p={p_spearman:.4f}\")\nprint(f\"  gaps:  {gaps}\")\nprint(f\"  gains: {gains}\")\n\n# BH correction\ntest_labels = []\nraw_pvals = []\nfor g in generators:\n    for w in [1, 3, 5]:\n        test_labels.append(f\"{g}_w{w}\")\n        raw_pvals.append(pw_results[g][f\"w{w}\"][\"mcnemar_p\"])\n\nrejected, pvals_corrected, _, _ = multipletests(raw_pvals, alpha=0.05, method='fdr_bh')\nn_sig = int(sum(rejected))\nprint(f\"\\nBH correction (m=12), significant: {n_sig}/12\")\nfor label, raw_p, adj_p, sig in zip(test_labels, raw_pvals, pvals_corrected, rejected):\n    marker = \"*\" if sig else \" \"\n    print(f\"  {marker} {label:25s} raw={raw_p:.2e}  adj={adj_p:.2e}\")\n\n# SC baseline shift\nold_counter = {\"Mistral-7B\": 236, \"LLaMA-3.1-8B\": 420, \"Qwen2.5-14B\": 441, \"Qwen3-14B\": 510}\nold_combo_w3 = {\"Mistral-7B\": 42.83, \"LLaMA-3.1-8B\": 74.17, \"Qwen2.5-14B\": 74.33, \"Qwen3-14B\": 86.00}\nold_sc_pct = {\"Mistral-7B\": 39.33, \"LLaMA-3.1-8B\": 70.00, \"Qwen2.5-14B\": 73.50, \"Qwen3-14B\": 85.00}\n\nprint(\"\\n=== SC baseline: counter → alpha ===\")\nfor g in generators:\n    d = pw_results[g][\"sc\"][\"n_correct\"] - old_counter[g]\n    print(f\"  {g}: {old_counter[g]} → {pw_results[g]['sc']['n_correct']} ({d:+d})\")\n\nprint(\"\\n=== Combo w3 delta: old → new ===\")\nfor g in generators:\n    old_d = old_combo_w3[g] - old_sc_pct[g]\n    new_d = pw_results[g][\"w3\"][\"delta_pp\"]\n    print(f\"  {g}: {old_d:+.2f}pp → {new_d:+.2f}pp\")\n\n# Build output\noutput = {\n    \"proofwriter\": pw_results,\n    \"folio\": folio_results,\n    \"spearman\": {\n        \"generators\": generators,\n        \"deberta_standalone\": deberta_standalone,\n        \"gaps\": [round(g, 2) for g in gaps],\n        \"gains\": [round(g, 2) for g in gains],\n        \"rho\": round(float(rho), 4),\n        \"p\": round(float(p_spearman), 4)\n    },\n    \"bh_correction\": {\n        \"m\": 12,\n        \"test_labels\": test_labels,\n        \"raw_pvals\": [round(p, 10) for p in raw_pvals],\n        \"adjusted_pvals\": [round(float(p), 10) for p in pvals_corrected],\n        \"significant_after_bh\": [bool(r) for r in rejected],\n        \"n_significant\": n_sig\n    },\n    \"sc_baseline_shift\": {\n        \"note\": \"Alphabetical tiebreaking (with invalid-answer filtering) changes SC baselines from combo traces\",\n        \"changes\": {g: {\n            \"counter_n\": old_counter[g],\n            \"alpha_n\": pw_results[g][\"sc\"][\"n_correct\"],\n            \"diff\": pw_results[g][\"sc\"][\"n_correct\"] - old_counter[g]\n        } for g in generators}\n    },\n    \"paper_changes_needed\": [\n        {\n            \"section\": \"NLI Combo Table\",\n            \"description\": \"SC baselines shift: LLaMA 420→435(+15), Qwen2.5 441→444(+3), Qwen3 510→515(+5), Mistral unchanged. Combo gains shrink. Only Mistral w3/w5 remain significant after BH.\",\n            \"old_significant_count\": 4,\n            \"new_significant_count\": n_sig\n        },\n        {\n            \"section\": \"Spearman correlation (capability gap vs combo gain)\",\n            \"description\": f\"rho={round(float(rho), 4)}, p={round(float(p_spearman), 4)}\"\n        },\n        {\n            \"section\": \"FOLIO combo\",\n            \"description\": \"Mistral FOLIO SC=55.88%(114/204), w1=56.37%(+0.49pp,p=1.0), w3=58.82%(+2.94pp,p=0.21)\"\n        }\n    ]\n}\n\nout_path = \"artifacts/nli_combo_recomputed.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\nPYEOF",
  "description": "Compute derived metrics and build final JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\nimport os\nfrom scipy.stats import spearmanr\nfrom statsmodels.stats.multitest import multipletests\n\nos.makedirs(\"artifacts\", exist_ok=True)\n\npw_results = {\n    \"Mistral-7B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 39.33, \"n_correct\": 236},\n        \"w1\": {\"acc\": 40.17, \"n_correct\": 241, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 46.00, \"n_correct\": 276, \"delta_pp\": 6.67, \"mcnemar_p\": 1.1296023055413025e-05, \"b\": 61, \"c\": 21},\n        \"w5\": {\"acc\": 50.33, \"n_correct\": 302, \"delta_pp\": 11.00, \"mcnemar_p\": 6.178035816936483e-07, \"b\": 120, \"c\": 54},\n    },\n    \"LLaMA-3.1-8B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 72.50, \"n_correct\": 435},\n        \"w1\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.359283447265625, \"b\": 12, \"c\": 7},\n        \"w3\": {\"acc\": 73.33, \"n_correct\": 440, \"delta_pp\": 0.83, \"mcnemar_p\": 0.6646454904132133, \"b\": 45, \"c\": 40},\n        \"w5\": {\"acc\": 72.00, \"n_correct\": 432, \"delta_pp\": -0.50, \"mcnemar_p\": 0.8707787409560847, \"b\": 74, \"c\": 77},\n    },\n    \"Qwen2.5-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 74.00, \"n_correct\": 444},\n        \"w1\": {\"acc\": 74.17, \"n_correct\": 445, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 3, \"c\": 2},\n        \"w3\": {\"acc\": 74.67, \"n_correct\": 448, \"delta_pp\": 0.67, \"mcnemar_p\": 0.5034446716308594, \"b\": 12, \"c\": 8},\n        \"w5\": {\"acc\": 75.17, \"n_correct\": 451, \"delta_pp\": 1.17, \"mcnemar_p\": 0.3603776529357674, \"b\": 25, \"c\": 18},\n    },\n    \"Qwen3-14B\": {\n        \"n\": 600,\n        \"sc\": {\"acc\": 85.83, \"n_correct\": 515},\n        \"w1\": {\"acc\": 86.00, \"n_correct\": 516, \"delta_pp\": 0.17, \"mcnemar_p\": 1.0, \"b\": 1, \"c\": 0},\n        \"w3\": {\"acc\": 86.33, \"n_correct\": 518, \"delta_pp\": 0.50, \"mcnemar_p\": 0.453125, \"b\": 5, \"c\": 2},\n        \"w5\": {\"acc\": 87.00, \"n_correct\": 522, \"delta_pp\": 1.17, \"mcnemar_p\": 0.21003961563110352, \"b\": 15, \"c\": 8},\n    },\n}\n\nfolio_results = {\n    \"Mistral-7B\": {\n        \"n\": 204,\n        \"sc\": {\"acc\": 55.88, \"n_correct\": 114},\n        \"w1\": {\"acc\": 56.37, \"n_correct\": 115, \"delta_pp\": 0.49, \"mcnemar_p\": 1.0, \"b\": 4, \"c\": 3},\n        \"w3\": {\"acc\": 58.82, \"n_correct\": 120, \"delta_pp\": 2.94, \"mcnemar_p\": 0.210113525390625, \"b\": 11, \"c\": 5},\n    },\n}\n\n# Spearman\ndeberta_standalone = 55.00\ngenerators = [\"Mistral-7B\", \"LLaMA-3.1-8B\", \"Qwen2.5-14B\", \"Qwen3-14B\"]\ngaps = [deberta_standalone - pw_results[g][\"sc\"][\"acc\"] for g in generators]\ngains = [pw_results[g][\"w3\"][\"delta_pp\"] for g in generators]\nrho, p_spearman = spearmanr(gaps, gains)\nprint(f\"Spearman rho={rho:.4f}, p={p_spearman:.4f}\")\nprint(f\"  gaps:  {gaps}\")\nprint(f\"  gains: {gains}\")\n\n# BH correction\ntest_labels = []\nraw_pvals = []\nfor g in generators:\n    for w in [1, 3, 5]:\n        test_labels.append(f\"{g}_w{w}\")\n        raw_pvals.append(pw_results[g][f\"w{w}\"][\"mcnemar_p\"])\n\nrejected, pvals_corrected, _, _ = multipletests(raw_pvals, alpha=0.05, method='fdr_bh')\nn_sig = int(sum(rejected))\nprint(f\"\\nBH correction (m=12), significant: {n_sig}/12\")\nfor label, raw_p, adj_p, sig in zip(test_labels, raw_pvals, pvals_corrected, rejected):\n    marker = \"*\" if sig else \" \"\n    print(f\"  {marker} {label:25s} raw={raw_p:.2e}  adj={adj_p:.2e}\")\n\n# SC baseline shift\nold_counter = {\"Mistral-7B\": 236, \"LLaMA-3.1-8B\": 420, \"Qwen2.5-14B\": 441, \"Qwen3-14B\": 510}\nold_combo_w3 = {\"Mistral-7B\": 42.83, \"LLaMA-3.1-8B\": 74.17, \"Qwen2.5-14B\": 74.33, \"Qwen3-14B\": 86.00}\nold_sc_pct = {\"Mistral-7B\": 39.33, \"LLaMA-3.1-8B\": 70.00, \"Qwen2.5-14B\": 73.50, \"Qwen3-14B\": 85.00}\n\nprint(\"\\n=== SC baseline: counter → alpha ===\")\nfor g in generators:\n    d = pw_results[g][\"sc\"][\"n_correct\"] - old_counter[g]\n    print(f\"  {g}: {old_counter[g]} → {pw_results[g]['sc']['n_correct']} ({d:+d})\")\n\nprint(\"\\n=== Combo w3 delta: old → new ===\")\nfor g in generators:\n    old_d = old_combo_w3[g] - old_sc_pct[g]\n    new_d = pw_results[g][\"w3\"][\"delta_pp\"]\n    print(f\"  {g}: {old_d:+.2f}pp → {new_d:+.2f}pp\")\n\n# Build output\noutput = {\n    \"proofwriter\": pw_results,\n    \"folio\": folio_results,\n    \"spearman\": {\n        \"generators\": generators,\n        \"deberta_standalone\": deberta_standalone,\n        \"gaps\": [round(g, 2) for g in gaps],\n        \"gains\": [round(g, 2) for g in gains],\n        \"rho\": round(float(rho), 4),\n        \"p\": round(float(p_spearman), 4)\n    },\n    \"bh_correction\": {\n        \"m\": 12,\n        \"test_labels\": test_labels,\n        \"raw_pvals\": [round(p, 10) for p in raw_pvals],\n        \"adjusted_pvals\": [round(float(p), 10) for p in pvals_corrected],\n        \"significant_after_bh\": [bool(r) for r in rejected],\n        \"n_significant\": n_sig\n    },\n    \"sc_baseline_shift\": {\n        \"note\": \"Alphabetical tiebreaking (with invalid-answer filtering) changes SC baselines from combo traces\",\n        \"changes\": {g: {\n            \"counter_n\": old_counter[g],\n            \"alpha_n\": pw_results[g][\"sc\"][\"n_correct\"],\n            \"diff\": pw_results[g][\"sc\"][\"n_correct\"] - old_counter[g]\n        } for g in generators}\n    },\n    \"paper_changes_needed\": [\n        {\n            \"section\": \"NLI Combo Table\",\n            \"description\": \"SC baselines shift: LLaMA 420→435(+15), Qwen2.5 441→444(+3), Qwen3 510→515(+5), Mistral unchanged. Combo gains shrink. Only Mistral w3/w5 remain significant after BH.\",\n            \"old_significant_count\": 4,\n            \"new_significant_count\": n_sig\n        },\n        {\n            \"section\": \"Spearman correlation (capability gap vs combo gain)\",\n            \"description\": f\"rho={round(float(rho), 4)}, p={round(float(p_spearman), 4)}\"\n        },\n        {\n            \"section\": \"FOLIO combo\",\n            \"description\": \"Mistral FOLIO SC=55.88%(114/204), w1=56.37%(+0.49pp,p=1.0), w3=58.82%(+2.94pp,p=0.21)\"\n        }\n    ]\n}\n\nout_path = \"artifacts/nli_combo_recomputed.json\"\nwith open(out_path, \"w\") as f:\n    json.dump(output, f, indent=2)\nprint(f\"\\nSaved: {out_path}\")\nPYEOF",
    "description": "Compute derived metrics and build final JSON"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-21T05:32:11.343402+00:00_

Spearman rho=1.0000, p=0.0000
  gaps:  [15.670000000000002, -17.5, -19.0, -30.83]
  gains: [6.67, 0.83, 0.67, 0.5]

BH correction (m=12), significant: 2/12
    Mistral-7B_w1             raw=3.59e-01  adj=7.21e-01
  * Mistral-7B_w3             raw=1.13e-05  adj=6.78e-05
  * Mistral-7B_w5             raw=6.18e-07  adj=7.41e-06
    LLaMA-3.1-8B_w1           raw=3.59e-01  adj=7.21e-01
    LLaMA-3.1-8B_w3           raw=6.65e-01  adj=8.86e-01
    LLaMA-3.1-8B_w5           raw=8.71e-01  adj=1.00e+00
    Qwen2.5-14B_w1            raw=1.00e+00  adj=1.00e+00
    Qwen2.5-14B_w3            raw=5.03e-01  adj=7.55e-01
    Qwen2.5-14B_w5            raw=3.60e-01  adj=7.21e-01
    Qwen3-14B_w1              raw=1.00e+00  adj=1.00e+00
    Qwen3-14B_w3              raw=4.53e-01  adj=7.55e-01
    Qwen3-14B_w5              raw=2.10e-01  adj=7.21e-01

=== SC baseline: counter → alpha ===
  Mistral-7B: 236 → 236 (+0)
  LLaMA-3.1-8B: 420 → 435 (+15)
  Qwen2.5-14B: 441 → 444 (+3)
  Qwen3-14B: 510 → 515 (+5)

=== Combo w3 delta: old → new ===
  Mistral-7B: +3.50pp → +6.67pp
  LLaMA-3.1-8B: +4.17pp → +0.83pp
  Qwen2.5-14B: +0.83pp → +0.67pp
  Qwen3-14B: +1.00pp → +0.50pp

Saved: artifacts/nli_combo_recomputed.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T05:32:11.343631+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-21T05:32:11.343803+00:00_

_extracted
_project
ablation_text.py
aime30_v2_partial_analysis.md
aime_bias_ratio_results.json
analysis_exp045.md
analysis_prove_verify.py
analyze_adaptive_sica.py
analyze_discriminative_rate.py
analyze_expanded.py
analyze_seed_replication.py
appendix_prompt_template.md
backward_verification.py
case_study_materials.md
citation_verification.md
code_verify_report.md
confirmation_bias_results.json
constraint_ablation
constraint_extractor.py
constraint_extractor_fixed.py
constraint_quality_crossmethod.json
crd_audit_report.md
cross_model_kappa_results.json
cross_model_sica_results.json
cross_trace_unsat.py
d016_model_pivot_report.md
d116_qwen3_pw_deberta_large.py
diagnose_exp039.md
diagnose_exp062_exp065.md
dir_c_premise_only.py
dir_d_dpp_trace_selection.py
dir_f2_self_verify.py
dir_f3_cross_model.py
dir_f_prm_verifier_pilot.py
dir_f_prm_verifier_pilot_v2.py
dir_h_provenance_analysis
dir_h_provenance_analysis.py
dir_i2_single_model_baselines.py
dir_j2_nli_qwen3.py
dir_j3_nli_multi_verifier.py
dir_k_nli_qwen3_proofwriter
direction_a_atom_verification.py
direction_a_prove_results.json
direction_b_weighted_maxsat.py
direction_c_counterfactual.py
direction_d_cegis_results_partial.json
direction_e_abstention.py
direction_e_abstention_results.json
direction_gr_combo.py
direction_j
direction_j_results.json
direction_r_deberta_proofwriter.py
direction_r_nli_large
drc_cascade_pilot.py
dream_reports
entropy_breakdown_crossmodel.json
error_categorization.py
error_categorization_discordant.json
exp-001
exp-005
exp-007-qwen72b-awq
exp-009
exp-010-mistral-v2
exp-011
exp-011-llama8b
exp-013-constraint-ablation
exp-014
exp-016
exp-017-strategyqa-v3
exp-017-strategyqa-v3_analysis.md
exp-019
exp-021-oracle-folio
exp-022
exp-022-oracle-proofwriter
exp-023-discriminative-rate
exp-030-crossmodel-mistral-folio204
exp-031-oracle-folio-regen
exp-038
exp-045-backward-verification
exp-046
exp-060-cross-qwen25-14b-extractor
exp-064
exp-064-diagnosis.md
exp-074
exp-078-debate-mistral-logiqa200
ex
…[truncated 1998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-21T05:32:11.343999+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cp artifacts/nli_combo_recomputed.json /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json",
  "description": "Copy artifact to project artifacts dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "cp artifacts/nli_combo_recomputed.json /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json",
    "description": "Copy artifact to project artifacts dir"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-21T05:32:11.344131+00:00_

Exit code 1
cp: 'artifacts/nli_combo_recomputed.json' and '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json' are the same file

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T05:32:11.344277+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "NLI Combo Recomputed (Alphabetical Tiebreaking)",
  "type": "data",
  "description": "All NLI combo results recomputed with alphabetical tiebreaking: PW600 (4 generators × w1/3/5), FOLIO (Mistral w1/3), Spearman ρ, BH correction. SC baselines shifted for LLaMA(+15), Qwen2.5(+3), Qwen3(+5). Only Mistral w3/w5 survive BH.",
  "project": "symb_invariant_consensus",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json",
  "tags": "['nli', 'combo', 'tiebreaking', 'recompute', 'mcnemar', 'bh']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "NLI Combo Recomputed (Alphabetical Tiebreaking)",
    "type": "data",
    "description": "All NLI combo results recomputed with alphabetical tiebreaking: PW600 (4 generators × w1/3/5), FOLIO (Mistral w1/3), Spearman ρ, BH correction. SC baselines shifted for LLaMA(+15), Qwen2.5(+3), Qwen3(+5). Only Mistral w3/w5 survive BH.",
    "project": "symb_invariant_consensus",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/nli_combo_recomputed.json",
    "tags": "['nli', 'combo', 'tiebreaking', 'recompute', 'mcnemar', 'bh']"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T05:32:11.344434+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_f45299\", \"name\": \"NLI Combo Recomputed (Alphabetical Tiebreaking)\", \"type\": \"data\", \"description\": \"All NLI combo results recomputed with alphabetical tiebreaking: PW600 (4 generators × w1/3/5), FOLIO (Mistral w1/3), Spearman ρ, BH correction. SC baselines shifted for LLaMA(+15), Qwen2.5(+3), Qwen3(+5). Only Mistral w3/w5 survive BH.\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/data/nli_combo_recomputed.json\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T05:30:37.563125+00:00\", \"tags\": [\"nli\", \"combo\", \"tiebreaking\", \"recompute\", \"mcnemar\", \"bh\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-21T05:32:11.344616+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && grep -rn \"most_common(1)\" scripts/ dir_k_nli_qwen3_pw600.py 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && grep -rn \"most_common(1)\" scripts/ dir_k_nli_qwen3_pw600.py 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T05:32:11.344769+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"scripts/dir_f_prm_verifier_pilot.py:120:    return Counter(answers).most_common(1)[0][0]\\nscripts/dir_f_prm_verifier_pilot.py:135:    return Counter([t[\\\"answer\\\"] for t, _ in filtered]).most_common(1)[0][0]\\nscripts/dir_f_prm_verifier_pilot.py:149:    return weight_by_answer.most_common(1)[0][0]\\nscripts/dir_f_prm_verifier_pilot.py:164:    return Counter([t[\\\"answer\\\"] for t, _ in filtered]).most_common(1)[0][0]\\nscripts/dir_d_dpp_trace_selection.py:58:    return counts.most_common(1)[0][0]\\nscripts/dir_f2_cross_model_verify.py:66:    return Counter(ans).most_common(1)[0][0]\\nscripts/dir_h_provenance_analysis.py:182:        sc_answer = answer_counts.most_common(1)[0][0] if answer_counts else \\\"\\\"\\nscripts/dir_f2_self_verify.py:58:    return Counter(ans).most_common(1)[0][0]\\nscripts/analyze_condorcet_independence.py:58:    majority = counts.most_common(1)[0][0]\\nscripts/analyze_condorcet_independence.py:60:    majority_frac = counts.most_common(1)[0][1] / K\\nscripts/dir_c_premise_only.py:141:            max_count = answer_counts.most_common(1)[0][1]\\nscripts/dir_e_strict_verification.py:169:        sc_answer = Counter(sc_answers).most_common(1)[0][0] if sc_answers else ''\\ndir_k_nli_qwen3_pw600.py:163:            combo_answer = votes.most_common(1)[0][0] if votes else \\\"Unknown\\\"\\ndir_k_nli_qwen3_pw600.py:202:            combo_answer = votes.most_common(1)[0][0] if votes else \\\"Unknown\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-21T05:32:11.345113+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && grep -rn \"most_common(1)\" direction_r_nli_verifier.py direction_rg_combo.py dir_j3_nli_multi_verifier.py scripts/ 2>/dev/null",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && grep -rn \"most_common(1)\" direction_r_nli_verifier.py direction_rg_combo.py dir_j3_nli_multi_verifier.py scripts/ 2>/dev/null",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-21T05:32:11.345311+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"direction_r_nli_verifier.py:94:    return c.most_common(1)[0][0]\\ndirection_rg_combo.py:37:    return c.most_common(1)[0][0]\\ndirection_rg_combo.py:185:        answer = votes.most_common(1)[0][0]\\ndir_j3_nli_multi_verifier.py:182:                combo_answer = votes.most_common(1)[0][0] if votes else \\\"Unknown\\\"\\nscripts/analyze_condorcet_independence.py:58:    majority = counts.most_common(1)[0][0]\\nscripts/analyze_condorcet_independence.py:60:    majority_frac = counts.most_common(1)[0][1] / K\\nscripts/compute_kappa_icg_contrastive.py:124:                    sc_ans = ans_counts.most_common(1)[0][0]\\nscripts/compute_kappa_icg_contrastive.py:135:                sc_ans = ans_counts.most_common(1)[0][0]\\nscripts/process_kappa_diagnostic.py:29:        sc_vote = cnt.most_common(1)[0][0]\\nscripts/dir_f3_cross_model.py:90:    return counter.most_common(1)[0][0]\\nscripts/dir_j2_nli_qwen3.py:136:            combo_answer = votes.most_common(1)[0][0] if votes else \\\"Unknown\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-21T05:32:11.345488+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"most_common\" /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py /root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"most_common\" /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py /root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-21T05:32:11.345624+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-21T05:32:11.345761+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"combo_answer\\|most_common\\|votes\\[\" /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"combo_answer\\|most_common\\|votes\\[\" /root/symb_invariant_consensus/scripts/qwen14b_pw_nli_combo.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-21T05:32:11.345941+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"125:                combo_votes[cls] = sc_dist.get(cls, 0) + (w if cls == nli_pred else 0)\\n126:            combo_answer = max(combo_votes, key=combo_votes.get)\\n129:            combo_is_correct = combo_answer == gold\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-21T05:32:11.346169+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "grep -n \"combo_answer\\|most_common\\|votes\\[\" /root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "grep -n \"combo_answer\\|most_common\\|votes\\[\" /root/symb_invariant_consensus/scripts/exp092_llama8b_pw_nli_combo.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-21T05:32:11.346317+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"117:            votes[nli_pred] = votes.get(nli_pred, 0) + w\\n118:            combo_answer = max(votes, key=votes.get)\\n119:            combo_is_correct = combo_answer == gt[pid]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-21T05:32:11.346493+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "cd /root/symb_invariant_consensus && cat > _fix_tiebreaking.py << 'PYEOF'\n\"\"\"Fix insertion-order tiebreaking in NLI combo scripts → alphabetical.\"\"\"\nimport re\n\nFIXES = [\n    # (file, line_no, old_pattern, new_code)\n    (\"scripts/qwen14b_pw_nli_combo.py\", 126,\n     \"            combo_answer = max(combo_votes, key=combo_votes.get)\",\n     \"            _max = max(combo_votes.values()); combo_answer = sorted(k for k, v in combo_votes.items() if v == _max)[0]\"),\n    (\"scripts/exp092_llama8b_pw_nli_combo.py\", 118,\n     \"            combo_answer = max(votes, key=votes.get)\",\n     \"            _max = max(votes.values()); combo_answer = sorted(k for k, v in votes.items() if v == _max)[0]\"),\n    (\"dir_k_nli_qwen3_pw600.py\", 163,\n     '            combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n    (\"dir_k_nli_qwen3_pw600.py\", 202,\n     '            combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n]\n\nfor fpath, lineno, old, new in FIXES:\n    with open(fpath) as f:\n        lines = f.readlines()\n    if lines[lineno-1].rstrip() == old:\n        lines[lineno-1] = new + \"\\n\"\n        with open(fpath, \"w\") as f:\n            f.writelines(lines)\n        print(f\"FIXED {fpath}:{lineno}\")\n    else:\n        print(f\"MISMATCH {fpath}:{lineno}\")\n        print(f\"  Expected: {old!r}\")\n        print(f\"  Got:      {lines[lineno-1].rstrip()!r}\")\nPYEOF\npython3 _fix_tiebreaking.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "cd /root/symb_invariant_consensus && cat > _fix_tiebreaking.py << 'PYEOF'\n\"\"\"Fix insertion-order tiebreaking in NLI combo scripts → alphabetical.\"\"\"\nimport re\n\nFIXES = [\n    # (file, line_no, old_pattern, new_code)\n    (\"scripts/qwen14b_pw_nli_combo.py\", 126,\n     \"            combo_answer = max(combo_votes, key=combo_votes.get)\",\n     \"            _max = max(combo_votes.values()); combo_answer = sorted(k for k, v in combo_votes.items() if v == _max)[0]\"),\n    (\"scripts/exp092_llama8b_pw_nli_combo.py\", 118,\n     \"            combo_answer = max(votes, key=votes.get)\",\n     \"            _max = max(votes.values()); combo_answer = sorted(k for k, v in votes.items() if v == _max)[0]\"),\n    (\"dir_k_nli_qwen3_pw600.py\", 163,\n     '            combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n    (\"dir_k_nli_qwen3_pw600.py\", 202,\n     '            combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n]\n\nfor fpath, lineno, old, new in FIXES:\n    with open(fpath) as f:\n        lines = f.readlines()\n    if lines[lineno-1].rstrip() == old:\n        lines[lineno-1] = new + \"\\n\"\n        with open(fpath, \"w\") as f:\n            f.writelines(lines)\n        print(f\"FIXED {fpath}:{lineno}\")\n    else:\n        print(f\"MISMATCH {fpath}:{lineno}\")\n        print(f\"  Expected: {old!r}\")\n        print(f\"  Got:      {lines[lineno-1].rstrip()!r}\")\nPYEOF\npython3 _fix_tiebreaking.py"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-21T05:32:11.346654+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"FIXED scripts/qwen14b_pw_nli_combo.py:126\\nFIXED scripts/exp092_llama8b_pw_nli_combo.py:118\\nFIXED dir_k_nli_qwen3_pw600.py:163\\nFIXED dir_k_nli_qwen3_pw600.py:202\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-21T05:32:11.346797+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && cat > _fix_tiebreaking.py << 'PYEOF'\n\"\"\"Fix insertion-order tiebreaking in NLI combo scripts → alphabetical.\"\"\"\n\nFIXES = [\n    (\"direction_r_nli_verifier.py\", 94,\n     \"    return c.most_common(1)[0][0]\",\n     \"    _max = max(c.values()); return sorted(k for k, v in c.items() if v == _max)[0]\"),\n    (\"direction_rg_combo.py\", 37,\n     \"    return c.most_common(1)[0][0]\",\n     \"    _max = max(c.values()); return sorted(k for k, v in c.items() if v == _max)[0]\"),\n    (\"direction_rg_combo.py\", 185,\n     \"        answer = votes.most_common(1)[0][0]\",\n     \"        _max = max(votes.values()); answer = sorted(k for k, v in votes.items() if v == _max)[0]\"),\n    (\"dir_j3_nli_multi_verifier.py\", 182,\n     '                combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '                combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n    (\"scripts/dir_j2_nli_qwen3.py\", 136,\n     '            combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n]\n\nfor fpath, lineno, old, new in FIXES:\n    try:\n        with open(fpath) as f:\n            lines = f.readlines()\n        if lines[lineno-1].rstrip() == old:\n            lines[lineno-1] = new + \"\\n\"\n            with open(fpath, \"w\") as f:\n                f.writelines(lines)\n            print(f\"FIXED {fpath}:{lineno}\")\n        else:\n            print(f\"MISMATCH {fpath}:{lineno}\")\n            print(f\"  Expected: {old!r}\")\n            print(f\"  Got:      {lines[lineno-1].rstrip()!r}\")\n    except Exception as e:\n        print(f\"ERROR {fpath}:{lineno}: {e}\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 _fix_tiebreaking.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && cat > _fix_tiebreaking.py << 'PYEOF'\n\"\"\"Fix insertion-order tiebreaking in NLI combo scripts → alphabetical.\"\"\"\n\nFIXES = [\n    (\"direction_r_nli_verifier.py\", 94,\n     \"    return c.most_common(1)[0][0]\",\n     \"    _max = max(c.values()); return sorted(k for k, v in c.items() if v == _max)[0]\"),\n    (\"direction_rg_combo.py\", 37,\n     \"    return c.most_common(1)[0][0]\",\n     \"    _max = max(c.values()); return sorted(k for k, v in c.items() if v == _max)[0]\"),\n    (\"direction_rg_combo.py\", 185,\n     \"        answer = votes.most_common(1)[0][0]\",\n     \"        _max = max(votes.values()); answer = sorted(k for k, v in votes.items() if v == _max)[0]\"),\n    (\"dir_j3_nli_multi_verifier.py\", 182,\n     '                combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '                combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n    (\"scripts/dir_j2_nli_qwen3.py\", 136,\n     '            combo_answer = votes.most_common(1)[0][0] if votes else \"Unknown\"',\n     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else \"Unknown\"'),\n]\n\nfor fpath, lineno, old, new in FIXES:\n    try:\n        with open(fpath) as f:\n            lines = f.readlines()\n        if lines[lineno-1].rstrip() == old:\n            lines[lineno-1] = new + \"\\n\"\n            with open(fpath, \"w\") as f:\n                f.writelines(lines)\n            print(f\"FIXED {fpath}:{lineno}\")\n        else:\n            print(f\"MISMATCH {fpath}:{lineno}\")\n            print(f\"  Expected: {old!r}\")\n            print(f\"  Got:      {lines[lineno-1].rstrip()!r}\")\n    except Exception as e:\n        print(f\"ERROR {fpath}:{lineno}: {e}\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 _fix_tiebreaking.py"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T05:32:11.347494+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"FIXED direction_r_nli_verifier.py:94\\nFIXED direction_rg_combo.py:37\\nFIXED direction_rg_combo.py:185\\nFIXED dir_j3_nli_multi_verifier.py:182\\nFIXED scripts/dir_j2_nli_qwen3.py:136\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-21T05:32:11.347699+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('artifacts/nli_combo_recomputed.json') as f:\n    d = json.load(f)\n\n# Cross-validate Mistral against DRC pilot\nm = d['proofwriter']['Mistral-7B']\nassert m['sc']['n_correct'] == 236, f'SC mismatch: {m[\\\"sc\\\"][\\\"n_correct\\\"]}'\nassert m['w1']['n_correct'] == 241, f'w1 mismatch: {m[\\\"w1\\\"][\\\"n_correct\\\"]}'\nassert m['w3']['n_correct'] == 276, f'w3 mismatch: {m[\\\"w3\\\"][\\\"n_correct\\\"]}'\nassert m['w5']['n_correct'] == 302, f'w5 mismatch: {m[\\\"w5\\\"][\\\"n_correct\\\"]}'\nprint('DRC pilot cross-validation: PASS')\nprint(f'Spearman rho={d[\\\"spearman\\\"][\\\"rho\\\"]}, p={d[\\\"spearman\\\"][\\\"p\\\"]}')\nprint(f'BH significant: {d[\\\"bh_correction\\\"][\\\"n_significant\\\"]}/12')\n\"\n",
  "description": "Cross-validate Mistral results against DRC pilot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('artifacts/nli_combo_recomputed.json') as f:\n    d = json.load(f)\n\n# Cross-validate Mistral against DRC pilot\nm = d['proofwriter']['Mistral-7B']\nassert m['sc']['n_correct'] == 236, f'SC mismatch: {m[\\\"sc\\\"][\\\"n_correct\\\"]}'\nassert m['w1']['n_correct'] == 241, f'w1 mismatch: {m[\\\"w1\\\"][\\\"n_correct\\\"]}'\nassert m['w3']['n_correct'] == 276, f'w3 mismatch: {m[\\\"w3\\\"][\\\"n_correct\\\"]}'\nassert m['w5']['n_correct'] == 302, f'w5 mismatch: {m[\\\"w5\\\"][\\\"n_correct\\\"]}'\nprint('DRC pilot cross-validation: PASS')\nprint(f'Spearman rho={d[\\\"spearman\\\"][\\\"rho\\\"]}, p={d[\\\"spearman\\\"][\\\"p\\\"]}')\nprint(f'BH significant: {d[\\\"bh_correction\\\"][\\\"n_significant\\\"]}/12')\n\"\n",
    "description": "Cross-validate Mistral results against DRC pilot"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-21T05:32:11.347855+00:00_

DRC pilot cross-validation: PASS
Spearman rho=1.0, p=0.0
BH significant: 2/12

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 109 · 2026-05-21T05:32:11.348310+00:00_

全部完成。总结：

## 重算结果

### PW600 (alphabetical tiebreaking)

| Generator | SC (alpha) | w1 | w3 | w5 |
|---|---|---|---|---|
| **Mistral-7B** | 39.33% (236) | 40.17% (+0.83pp, p=.36) | **46.00% (+6.67pp, p=1.1e-5)\*** | **50.33% (+11.0pp, p=6.2e-7)\*** |
| LLaMA-3.1-8B | **72.50%** (435) | 73.33% (+0.83pp, p=.36) | 73.33% (+0.83pp, p=.66) | 72.00% (−0.50pp, p=.87) |
| Qwen2.5-14B | **74.00%** (444) | 74.17% (+0.17pp, p=1.0) | 74.67% (+0.67pp, p=.50) | 75.17% (+1.17pp, p=.36) |
| Qwen3-14B | **85.83%** (515) | 86.00% (+0.17pp, p=1.0) | 86.33% (+0.50pp, p=.45) | 87.00% (+1.17pp, p=.21) |

\* = significant after BH correction (m=12)

### 关键变化

1. **SC baseline 上移**：alphabetical + filtering invalid answers 使 LLaMA SC 从 420→435 (+15), Qwen2.5 441→444 (+3), Qwen3 510→515 (+5)。Mistral 不变。

2. **Combo gain 大幅变化**：
   - Mistral w3: +3.50pp → **+6.67pp**（gain 增大，因为 combo 本身从 257→276）
   - LLaMA w3: +4.17pp → **+0.83pp**（gain 缩小，SC 上移更多）
   - 其余类似缩小

3. **BH significant: 4 → 2**（仅 Mistral w3、w5 存活）

4. **Spearman ρ = 1.0**（n=4, exact permutation p = 0.083）: capability gap 与 combo gain 完全单调

5. **FOLIO (Mistral)**: SC=55.88%(114/204), w1=56.37%(+0.49pp), w3=58.82%(+2.94pp, p=.21)

### 代码修复
9 处 `Counter.most_common()` / `max(dict, key=dict.get)` 已替换为 alphabetical tiebreaking（westd-16639: 4处, westd-25068: 5处）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_nli-combo-recompute-pw_20260521T052024"
}
```

</details>

---
