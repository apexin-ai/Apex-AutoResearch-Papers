# analysis r mcnemar seed verify

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_analysis_r-mcnemar-seed-verify_20260520T105518.jsonl`
- **Structured JSON:** [`cc205abcedcb15b143a4.json`](../../sessions/cc/cc205abcedcb15b143a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-20T10:58:35.705017+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T10:58:35.705406+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T10:58:35.705610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -80 /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -80 /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T10:58:35.705755+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/exp033_mistral_folio204/"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T10:58:35.705901+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/direction_r_nli_small/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/direction_r_nli_small/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T10:58:35.706099+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Direction R: External NLI Verifier for FOLIO logical reasoning.\\n\\nUses an encoder-only NLI model (architecturally independent from decoder-only LLMs)\\nas an external verifier to break confirmation bias in self-consistency.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom pathlib import Path\\n\\nimport torch\\nfrom transformers import AutoModelForSequenceClassification, AutoTokenizer\\n\\n\\ndef parse_problem(problem_text):\\n    \\\"\\\"\\\"Extract premises and hypothesis from FOLIO problem text.\\\"\\\"\\\"\\n    m = re.search(\\n        r\\\"Given the following premises:\\\\n(.+?)\\\\n\\\\nDetermine whether the following conclusion is true, false, or uncertain:\\\\n(.+)\\\",\\n        problem_text,\\n        re.DOTALL,\\n    )\\n    if m:\\n        return m.group(1).strip(), m.group(2).strip()\\n    parts = problem_text.split(\\\"Determine whether the following conclusion is true, false, or uncertain:\\\")\\n    if len(parts) == 2:\\n        premises = parts[0].replace(\\\"Given the following premises:\\\", \\\"\\\").strip()\\n        hypothesis = parts[1].strip()\\n        return premises, hypothesis\\n    return problem_text, \\\"\\\"\\n\\n\\ndef load_nli_model(model_name, device):\\n    \\\"\\\"\\\"Load NLI model and tokenizer.\\\"\\\"\\\"\\n    print(f\\\"Loading NLI model: {model_name}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n    model = AutoModelForSequenceClassification.from_pretrained(model_name)\\n    model.to(device)\\n    model.eval()\\n    id2label = model.config.id2label\\n    print(f\\\"  Labels: {id2label}\\\")\\n    return model, tokenizer, id2label\\n\\n\\ndef nli_predict(model, tokenizer, id2label, premise, hypothesis, device):\\n    \\\"\\\"\\\"Run NLI inference, return (label, probs_dict).\\\"\\\"\\\"\\n    inputs = tokenizer(\\n        premise
…[truncated 1020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T10:58:35.706334+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/symb_invariant_consensus/results/exp033_mistral_folio204/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T10:58:35.706494+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T10:58:35.706661+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T10:58:35.706839+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"adaptive_sica_validation.json\\ncase_study_constraints.json\\ncase_study_normalized.json\\ncondorcet_independence_analysis.json\\nconfirmation_bias\\ncross_model_experiment\\ncross_model_kappa\\ncross_model_mistral_folio\\ndirection_a_prove\\ndirection_b_deepconf\\ndirection_e_abstention\\ndirection_f_blind_fol\\ndirection_g_decoupling\\ndirection_g_dryrun.log\\ndirection_g_vllm.log\\ndirection_i_z3_filter\\ndirection_r_deberta\\ndirection_r_nli_large\\ndirection_r_nli_small\\ndisc_filter_full.log\\ndisc_filter_test.log\\ndiscriminative_filter_exp033.json\\ndiscriminative_filter_exp033_test.json\\ndiscriminative_filter_exp044b.json\\ndiscriminative_filter_exp046.json\\ndiscriminative_filter_exp054.json\\nexp-007-qwen72b-awq\\nexp-029-contrastive-folio204\\nexp004_qwen7b_rerun\\nexp013_constraint_ablation\\nexp027_qwen3_14b_nonthinking\\nexp028_qwen3_14b_thinking\\nexp028b_discordant_tracking.json\\nexp028b_qwen3_thinking_folio204\\nexp033_mistral_7b_folio204\\nexp033_per_problem_analysis.json\\nexp033_per_problem_analysis_v2.json\\nexp034_llama31_8b_folio204\\nexp034_qwen25_14b_proofwriter\\nexp035_qwen25_7b_folio204\\nexp036_z3_feedback\\nexp036b_cross_trace_unsat.json\\nexp044b_icl_oracle_qwen14b\\nexp045b_backward_qwen14b\\nexp046_mistral_7b_pw600\\nexp047_qwen3_thinking_folio204\\nexp051_mistral_k_sensitivity\\nexp054_mistral_folio204_t10\\nexp057_mistral_folio204_t03\\nexp058_mistral_folio204_t05\\nexp059_cross_qwen3_extractor\\nexp05_backward_verification\\nexp060_cross_qwen25_14b_extractor\\nexp061_qwen25_7b_folio204\\nexp062_gemma27b_folio204\\nexp065_qwen7b_pw600\\nexp066_qwen14b_folio_seed123\\nexp066_vllm.log\\nexp067_mistral_folio_seed789\\nexp069_mistral_logiqa200\\nexp070_qwen7b_logiqa200\\nexp071_qwen7b_logiqa200_seed123\\nexp073_qwen7b_logiqa200_seed456\\nexp073b_qwen7b_logiqa200_seed456\\nexp074_icg_dryrun\\nexp074_icg_mistral_folio\\nexp074_icg_v2_dryrun\\nexp074c_icg_mistral_folio_seed123\\ne
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:58:35.707022+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"traces\\|load\\|path\\|json\\|exp0\\|seed\\|baseline\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"traces\\|load\\|path\\|json\\|exp0\\|seed\\|baseline\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T10:58:35.707160+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T10:58:35.707298+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -200 /root/symb_invariant_consensus/results/direction_r_nli_small/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -200 /root/symb_invariant_consensus/results/direction_r_nli_small/results.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T10:58:35.707567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"model\\\": \\\"/root/models/deberta-large-mnli\\\",\\n    \\\"n_problems\\\": 204,\\n    \\\"elapsed_seconds\\\": 4.3,\\n    \\\"sc_baseline\\\": {\\n      \\\"accuracy\\\": 0.5441,\\n      \\\"correct\\\": 111\\n    },\\n    \\\"nli_standalone\\\": {\\n      \\\"accuracy\\\": 0.4951,\\n      \\\"correct\\\": 101,\\n      \\\"delta_vs_sc\\\": -0.049\\n    },\\n    \\\"nli_as_verifier\\\": {\\n      \\\"accuracy\\\": 0.4951,\\n      \\\"correct\\\": 101,\\n      \\\"delta_vs_sc\\\": -0.049,\\n      \\\"strategy\\\": \\\"agree->keep_SC, disagree->use_NLI\\\"\\n    },\\n    \\\"nli_sica_combo\\\": {\\n      \\\"accuracy\\\": 0.5784,\\n      \\\"correct\\\": 118,\\n      \\\"delta_vs_sc\\\": 0.0343,\\n      \\\"strategy\\\": \\\"NLI_as_extra_vote_in_SC\\\"\\n    },\\n    \\\"per_label\\\": {\\n      \\\"True\\\": {\\n        \\\"total\\\": 72,\\n        \\\"nli_acc\\\": 0.5972,\\n        \\\"sc_acc\\\": 0.5556,\\n        \\\"nli_correct\\\": 43,\\n        \\\"sc_correct\\\": 40\\n      },\\n      \\\"False\\\": {\\n        \\\"total\\\": 63,\\n        \\\"nli_acc\\\": 0.7143,\\n        \\\"sc_acc\\\": 0.381,\\n        \\\"nli_correct\\\": 45,\\n        \\\"sc_correct\\\": 24\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"total\\\": 69,\\n        \\\"nli_acc\\\": 0.1884,\\n        \\\"sc_acc\\\": 0.6812,\\n        \\\"nli_correct\\\": 13,\\n        \\\"sc_correct\\\": 47\\n      }\\n    },\\n    \\\"disagreement_analysis\\\": {\\n      \\\"agree\\\": 92,\\n      \\\"disagree\\\": 112,\\n      \\\"disagree_nli_right\\\": 38,\\n      \\\"disagree_sc_right\\\": 48,\\n      \\\"disagree_both_wrong\\\": 26\\n    }\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"id\\\": \\\"folio_0\\\",\\n      \\\"ground_truth\\\": \\\"Unknown\\\",\\n      \\\"premises_len\\\": 763,\\n      \\\"hypothesis_len\\\": 45,\\n      \\\"nli_raw_label\\\": \\\"ENTAILMENT\\\",\\n      \\\"nli_probs\\\": {
…[truncated 4653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T10:58:35.707778+00:00_

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
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
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

_source line 16 · 2026-05-20T10:58:35.707946+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"constraint_cache\\nexp033.log\\nexp033_results.json\\nintermediates\\nsc_answer_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T10:58:35.708096+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"traces\\|load\\|path\\|exp033\\|seed\\|baseline\\|sc_traces\\|input\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"traces\\|load\\|path\\|exp033\\|seed\\|baseline\\|sc_traces\\|input\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T10:58:35.708231+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T10:58:35.708358+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"traces\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"traces\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T10:58:35.708489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"101:    parser.add_argument(\\\"--traces-dir\\\", default=\\\"results/exp033_mistral_7b_folio204/\\\")\\n112:    sc_matrix_path = os.path.join(args.traces_dir, \\\"sc_answer_matrix.json\\\")\\n115:    print(f\\\"Loaded SC traces for {len(sc_matrix)} problems\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T10:58:35.708613+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"exp033\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"exp033\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T10:58:35.708737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"101:    parser.add_argument(\\\"--traces-dir\\\", default=\\\"results/exp033_mistral_7b_folio204/\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T10:58:35.708856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"seed\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"seed\" /root/symb_invariant_consensus/direction_r_nli_verifier.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T10:58:35.709014+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T10:58:35.709150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T10:58:35.709362+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.5931372549019608,\\n    \\\"sc_accuracy\\\": 0.5441176470588235,\\n    \\\"sica_correct\\\": 121,\\n    \\\"sc_correct\\\": 111,\\n    \\\"extraction_rate\\\": 0.9714052287581699,\\n    \\\"total_constraints_extracted\\\": 14042,\\n    \\\"total_unique_constraints\\\": 8021,\\n    \\\"contradiction_rate\\\": 0.03503303827452936,\\n    \\\"problems_with_contradictions\\\": 128,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4881.8\\n  },\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T10:58:35.709552+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T10:58:35.709715+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T10:58:35.709841+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -5 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -5 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T10:58:35.710035+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 01:48:33,970 INFO SICA Full MVP | mode=vllm k=12 resume=False temperature=0.70 max_tokens=4096\\n2026-05-19 01:48:33,970 INFO Loaded 0 MATH problems\\n2026-05-19 01:48:33,970 INFO Loaded 0 ProofWriter problems\\n2026-05-19 01:48:33,971 INFO Loaded 204 FOLIO problems\\n2026-05-19 01:48:33,971 INFO Total: 204 problems\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T10:58:35.710185+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nfrom scipy.stats import binom_test\n\nwith open('results/direction_r_nli_small/results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\n# Verify summary numbers\nsc_cor = sum(1 for r in results if r['sc_correct'])\ncombo_cor = sum(1 for r in results if r['combo_correct'])\nprint(f'SC correct: {sc_cor}/{n} = {sc_cor/n:.4f}')\nprint(f'Combo correct: {combo_cor}/{n} = {combo_cor/n:.4f}')\nprint(f'Delta: {(combo_cor-sc_cor)/n:.4f} ({combo_cor-sc_cor} problems)')\nprint()\n\n# McNemar 2x2 table\nb = 0  # SC correct, combo wrong\nc = 0  # SC wrong, combo correct\nboth_correct = 0\nboth_wrong = 0\n\nfor r in results:\n    sc = r['sc_correct']\n    co = r['combo_correct']\n    if sc and co:\n        both_correct += 1\n    elif sc and not co:\n        b += 1\n    elif not sc and co:\n        c += 1\n    else:\n        both_wrong += 1\n\nprint('=== McNemar 2x2 Contingency Table ===')\nprint(f'Both correct:              {both_correct}')\nprint(f'Both wrong:                {both_wrong}')\nprint(f'SC correct, combo wrong:   {b}')\nprint(f'SC wrong, combo correct:   {c}')\nprint(f'Discordant pairs:          {b+c}')\nprint()\n\n# McNemar exact test (two-sided binomial)\nif b + c > 0:\n    p = binom_test(min(b, c), b + c, 0.5)\n    print(f'McNemar exact p-value: {p:.6f}')\n    print(f'Significant (p<0.05): {p < 0.05}')\n    print(f'Significant (p<0.01): {p < 0.01}')\nprint()\n\n# Per-label McNemar\nprint('=== Per-label McNemar ===')\nfor label in ['True', 'False', 'Unknown']:\n    sub = [r for r in results if r['ground_truth'] == label]\n    b_l = sum(1 for r in sub if r['sc_correct'] and not r['combo_correct'])\n    c_l = sum(1 for r in sub if not r['sc_correct'] and r['combo_correct'])\n    bc_l = sum(1 for r in sub if r['sc_correct'] and r['combo_correct'])\n    bw_l = sum(1 for r in sub if not r['sc_correct'] and not r['combo_correct'])\n    print(f'{label} (n={len(sub)}): both_correct={bc_l}, both_wrong={bw_l}, b={b_l}, c={c_l}, discordant={b_l+c_l}', end='')\n    if b_l + c_l > 0:\n        p_l = binom_test(min(b_l, c_l), b_l + c_l, 0.5)\n        print(f', p={p_l:.6f}')\n    else:\n        print(', N/A')\nprint()\n\n# 95% CI for accuracy difference (normal approx for paired proportions)\nimport math\np_sc = sc_cor / n\np_co = combo_cor / n\ndiff = p_co - p_sc\n# Variance of difference for paired data\n# Var(p1-p2) = (1/n) * (b+c)/n - ((c-b)/n)^2\nvar_diff = (1/n) * ((b + c)/n - ((c - b)/n)**2)\nse_diff = math.sqrt(var_diff)\nci_low = diff - 1.96 * se_diff\nci_high = diff + 1.96 * se_diff\nprint(f'=== 95% CI for accuracy difference ===')\nprint(f'Diff = {diff:.4f} ({diff*100:.2f}pp)')\nprint(f'SE = {se_diff:.4f}')\nprint(f'95% CI: [{ci_low:.4f}, {ci_high:.4f}] = [{ci_low*100:.2f}pp, {ci_high*100:.2f}pp]')\nprint()\n\n# Bootstrap CI\nimport random\nrandom.seed(42)\nn_boot = 10000\nboot_diffs = []\nfor _ in range(n_boot):\n    idx = random.choices(range(n), k=n)\n    sc_b = sum(results[i]['sc_correct'] for i in idx)\n    co_b = sum(results[i]['combo_correct'] for i in idx)\n    boot_diffs.append((co_b - sc_b) / n)\nboot_diffs.sort()\nlo = boot_diffs[int(0.025 * n_boot)]\nhi = boot_diffs[int(0.975 * n_boot)]\nprint(f'Bootstrap 95% CI (10000 resamples): [{lo:.4f}, {hi:.4f}] = [{lo*100:.2f}pp, {hi*100:.2f}pp]')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nfrom scipy.stats import binom_test\n\nwith open('results/direction_r_nli_small/results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\n# Verify summary numbers\nsc_cor = sum(1 for r in results if r['sc_correct'])\ncombo_cor = sum(1 for r in results if r['combo_correct'])\nprint(f'SC correct: {sc_cor}/{n} = {sc_cor/n:.4f}')\nprint(f'Combo correct: {combo_cor}/{n} = {combo_cor/n:.4f}')\nprint(f'Delta: {(combo_cor-sc_cor)/n:.4f} ({combo_cor-sc_cor} problems)')\nprint()\n\n# McNemar 2x2 table\nb = 0  # SC correct, combo wrong\nc = 0  # SC wrong, combo correct\nboth_correct = 0\nboth_wrong = 0\n\nfor r in results:\n    sc = r['sc_correct']\n    co = r['combo_correct']\n    if sc and co:\n        both_correct += 1\n    elif sc and not co:\n        b += 1\n    elif not sc and co:\n        c += 1\n    else:\n        both_wrong += 1\n\nprint('=== McNemar 2x2 Contingency Table ===')\nprint(f'Both correct:              {both_correct}')\nprint(f'Both wrong:                {both_wrong}')\nprint(f'SC correct, combo wrong:   {b}')\nprint(f'SC wrong, combo correct:   {c}')\nprint(f'Discordant pairs:          {b+c}')\nprint()\n\n# McNemar exact test (two-sided binomial)\nif b + c > 0:\n    p = binom_test(min(b, c), b + c, 0.5)\n    print(f'McNemar exact p-value: {p:.6f}')\n    print(f'Significant (p<0.05): {p < 0.05}')\n    print(f'Significant (p<0.01): {p < 0.01}')\nprint()\n\n# Per-label McNemar\nprint('=== Per-label McNemar ===')\nfor label in ['True', 'False', 'Unknown']:\n    sub = [r for r in results if r['ground_truth'] == label]\n    b_l = sum(1 for r in sub if r['sc_correct'] and not r['combo_correct'])\n    c_l = sum(1 for r in sub if not r['sc_correct'] and r['combo_correct'])\n    bc_l = sum(1 for r in sub if r['sc_correct'] and r['combo_correct'])\n    bw_l = sum(1 for r in sub if not r['sc_correct'] and not r['combo_correct'])\n    print(f'{label} (n={len(sub)}): both_correct={bc_l}, both_wrong={bw_l}, b={b_l}, c={c_l}, discordant={b_l+c_l}', end='')\n    if b_l + c_l > 0:\n        p_l = binom_test(min(b_l, c_l), b_l + c_l, 0.5)\n        print(f', p={p_l:.6f}')\n    else:\n        print(', N/A')\nprint()\n\n# 95% CI for accuracy difference (normal approx for paired proportions)\nimport math\np_sc = sc_cor / n\np_co = combo_cor / n\ndiff = p_co - p_sc\n# Variance of difference for paired data\n# Var(p1-p2) = (1/n) * (b+c)/n - ((c-b)/n)^2\nvar_diff = (1/n) * ((b + c)/n - ((c - b)/n)**2)\nse_diff = math.sqrt(var_diff)\nci_low = diff - 1.96 * se_diff\nci_high = diff + 1.96 * se_diff\nprint(f'=== 95% CI for accuracy difference ===')\nprint(f'Diff = {diff:.4f} ({diff*100:.2f}pp)')\nprint(f'SE = {se_diff:.4f}')\nprint(f'95% CI: [{ci_low:.4f}, {ci_high:.4f}] = [{ci_low*100:.2f}pp, {ci_high*100:.2f}pp]')\nprint()\n\n# Bootstrap CI\nimport random\nrandom.seed(42)\nn_boot = 10000\nboot_diffs = []\nfor _ in range(n_boot):\n    idx = random.choices(range(n), k=n)\n    sc_b = sum(results[i]['sc_correct'] for i in idx)\n    co_b = sum(results[i]['combo_correct'] for i in idx)\n    boot_diffs.append((co_b - sc_b) / n)\nboot_diffs.sort()\nlo = boot_diffs[int(0.025 * n_boot)]\nhi = boot_diffs[int(0.975 * n_boot)]\nprint(f'Bootstrap 95% CI (10000 resamples): [{lo:.4f}, {hi:.4f}] = [{lo*100:.2f}pp, {hi*100:.2f}pp]')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T10:58:35.710447+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python3 -c \\\"\\\\nimport json\\\\nfrom scipy.stats import binom_test\\\\n\\\\nwith open(\\\\'results/direction_r_nli_small/results.json\\\\') as f:\\\\n    data = json.load(f)\\\\n\\\\nresults = data[\\\\'results\\\\']\\\\nn = len(results)\\\\nprint(f\\\\'Total problems: {n}\\\\')\\\\n\\\\n# Verify summary numbers\\\\nsc_cor = sum(1 for r in results if r[\\\\'sc_correct\\\\'])\\\\ncombo_cor = sum(1 for r in results if r[\\\\'combo_correct\\\\'])\\\\nprint(f\\\\'SC correct: {sc_cor}/{n} = {sc_cor/n:.4f}\\\\')\\\\nprint(f\\\\'Combo correct: {combo_cor}/{n} = {combo_cor/n:.4f}\\\\')\\\\nprint(f\\\\'Delta: {(combo_cor-sc_cor)/n:.4f} ({combo_cor-sc_cor} problems)\\\\')\\\\nprint()\\\\n\\\\n# McNemar 2x2 table\\\\nb = 0  # SC correct, combo wrong\\\\nc = 0  # SC wrong, combo correct\\\\nboth_correct = 0\\\\nboth_wrong = 0\\\\n\\\\nfor r in results:\\\\n    sc = r[\\\\'sc_correct\\\\']\\\\n    co = r[\\\\'combo_correct\\\\']\\\\n    if sc and co:\\\\n        both_correct += 1\\\\n    elif sc and not co:\\\\n        b += 1\\\\n    elif not sc and co:\\\\n        c += 1\\\\n    else:\\\\n        both_wrong += 1\\\\n\\\\nprint(\\\\'=== McNemar 2x2 Contingency Table ===\\\\')\\\\nprint(f\\\\'Both correct:              {both_correct}\\\\')\\\\nprint(f\\\\'Both wrong:                {both_wrong}\\\\')\\\\nprint(f\\\\'SC correct, combo wrong:   {b}\\\\')\\\\nprint(f\\\\'SC wrong, combo correct:   {c}\\\\')\\\\nprint(f\\\\'Discordant pairs:          {b+c}\\\\')\\\\nprint()\\\\n\\\\n# McNemar exact test (two-sided binomial)\\\\nif b + c > 0:\\\\n    p = binom_test(min(b, c), b + c, 0.5)\\\\n    print(f\\\\'McNemar exact p-value: {p:.6f}\\\\')\\\\n    print(f\\\\'Significant (p<0.05): {p < 0.05}\\\\')\\\\n    print(f\\\\'Significant (p<0.01): {p < 0.01}\\\\')\\\\n
…[truncated 2703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T10:58:35.710653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -rn \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -rn \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T10:58:35.710792+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"seed\" /root/symb_invariant_consensus/run_sica.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"seed\" /root/symb_invariant_consensus/run_sica.py"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T10:58:35.710975+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T10:58:35.711121+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/symb_invariant_consensus/run_sica.py: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T10:58:35.711258+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cat > /tmp/mcnemar_r.py << 'PYEOF'\nimport json, math, random\nfrom scipy.stats import binomtest\n\nwith open('/root/symb_invariant_consensus/results/direction_r_nli_small/results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\nsc_cor = sum(1 for r in results if r['sc_correct'])\ncombo_cor = sum(1 for r in results if r['combo_correct'])\nprint(f'SC correct: {sc_cor}/{n} = {sc_cor/n:.4f}')\nprint(f'Combo correct: {combo_cor}/{n} = {combo_cor/n:.4f}')\nprint(f'Delta: {(combo_cor-sc_cor)/n:.4f} ({combo_cor-sc_cor} problems)')\nprint()\n\nb = 0\nc = 0\nboth_correct = 0\nboth_wrong = 0\n\nfor r in results:\n    sc = r['sc_correct']\n    co = r['combo_correct']\n    if sc and co:\n        both_correct += 1\n    elif sc and not co:\n        b += 1\n    elif not sc and co:\n        c += 1\n    else:\n        both_wrong += 1\n\nprint('=== McNemar 2x2 Contingency Table ===')\nprint(f'Both correct:              {both_correct}')\nprint(f'Both wrong:                {both_wrong}')\nprint(f'SC correct, combo wrong:   {b}')\nprint(f'SC wrong, combo correct:   {c}')\nprint(f'Discordant pairs:          {b+c}')\nprint()\n\nif b + c > 0:\n    res = binomtest(min(b, c), b + c, 0.5, alternative='two-sided')\n    print(f'McNemar exact p-value: {res.pvalue:.6f}')\n    print(f'Significant (p<0.05): {res.pvalue < 0.05}')\n    print(f'Significant (p<0.01): {res.pvalue < 0.01}')\nprint()\n\nprint('=== Per-label McNemar ===')\nfor label in ['True', 'False', 'Unknown']:\n    sub = [r for r in results if r['ground_truth'] == label]\n    b_l = sum(1 for r in sub if r['sc_correct'] and not r['combo_correct'])\n    c_l = sum(1 for r in sub if not r['sc_correct'] and r['combo_correct'])\n    bc_l = sum(1 for r in sub if r['sc_correct'] and r['combo_correct'])\n    bw_l = sum(1 for r in sub if not r['sc_correct'] and not r['combo_correct'])\n    print(f'{label} (n={len(sub)}): both_correct={bc_l}, both_wrong={bw_l}, b={b_l}, c={c_l}, discordant={b_l+c_l}', end='')\n    if b_l + c_l > 0:\n        res_l = binomtest(min(b_l, c_l), b_l + c_l, 0.5, alternative='two-sided')\n        print(f', p={res_l.pvalue:.6f}')\n    else:\n        print(', N/A')\nprint()\n\np_sc = sc_cor / n\np_co = combo_cor / n\ndiff = p_co - p_sc\nvar_diff = (1/n) * ((b + c)/n - ((c - b)/n)**2)\nse_diff = math.sqrt(var_diff)\nci_low = diff - 1.96 * se_diff\nci_high = diff + 1.96 * se_diff\nprint('=== 95% CI for accuracy difference (normal approx) ===')\nprint(f'Diff = {diff:.4f} ({diff*100:.2f}pp)')\nprint(f'SE = {se_diff:.4f}')\nprint(f'95% CI: [{ci_low:.4f}, {ci_high:.4f}] = [{ci_low*100:.2f}pp, {ci_high*100:.2f}pp]')\nprint()\n\nrandom.seed(42)\nn_boot = 10000\nboot_diffs = []\nfor _ in range(n_boot):\n    idx = random.choices(range(n), k=n)\n    sc_b = sum(results[i]['sc_correct'] for i in idx)\n    co_b = sum(results[i]['combo_correct'] for i in idx)\n    boot_diffs.append((co_b - sc_b) / n)\nboot_diffs.sort()\nlo = boot_diffs[int(0.025 * n_boot)]\nhi = boot_diffs[int(0.975 * n_boot)]\nprint(f'Bootstrap 95% CI (10000 resamples): [{lo:.4f}, {hi:.4f}] = [{lo*100:.2f}pp, {hi*100:.2f}pp]')\nPYEOF\necho \"Script written\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat > /tmp/mcnemar_r.py << 'PYEOF'\nimport json, math, random\nfrom scipy.stats import binomtest\n\nwith open('/root/symb_invariant_consensus/results/direction_r_nli_small/results.json') as f:\n    data = json.load(f)\n\nresults = data['results']\nn = len(results)\nprint(f'Total problems: {n}')\n\nsc_cor = sum(1 for r in results if r['sc_correct'])\ncombo_cor = sum(1 for r in results if r['combo_correct'])\nprint(f'SC correct: {sc_cor}/{n} = {sc_cor/n:.4f}')\nprint(f'Combo correct: {combo_cor}/{n} = {combo_cor/n:.4f}')\nprint(f'Delta: {(combo_cor-sc_cor)/n:.4f} ({combo_cor-sc_cor} problems)')\nprint()\n\nb = 0\nc = 0\nboth_correct = 0\nboth_wrong = 0\n\nfor r in results:\n    sc = r['sc_correct']\n    co = r['combo_correct']\n    if sc and co:\n        both_correct += 1\n    elif sc and not co:\n        b += 1\n    elif not sc and co:\n        c += 1\n    else:\n        both_wrong += 1\n\nprint('=== McNemar 2x2 Contingency Table ===')\nprint(f'Both correct:              {both_correct}')\nprint(f'Both wrong:                {both_wrong}')\nprint(f'SC correct, combo wrong:   {b}')\nprint(f'SC wrong, combo correct:   {c}')\nprint(f'Discordant pairs:          {b+c}')\nprint()\n\nif b + c > 0:\n    res = binomtest(min(b, c), b + c, 0.5, alternative='two-sided')\n    print(f'McNemar exact p-value: {res.pvalue:.6f}')\n    print(f'Significant (p<0.05): {res.pvalue < 0.05}')\n    print(f'Significant (p<0.01): {res.pvalue < 0.01}')\nprint()\n\nprint('=== Per-label McNemar ===')\nfor label in ['True', 'False', 'Unknown']:\n    sub = [r for r in results if r['ground_truth'] == label]\n    b_l = sum(1 for r in sub if r['sc_correct'] and not r['combo_correct'])\n    c_l = sum(1 for r in sub if not r['sc_correct'] and r['combo_correct'])\n    bc_l = sum(1 for r in sub if r['sc_correct'] and r['combo_correct'])\n    bw_l = sum(1 for r in sub if not r['sc_correct'] and not r['combo_correct'])\n    print(f'{label} (n={len(sub)}): both_correct={bc_l}, both_wrong={bw_l}, b={b_l}, c={c_l}, discordant={b_l+c_l}', end='')\n    if b_l + c_l > 0:\n        res_l = binomtest(min(b_l, c_l), b_l + c_l, 0.5, alternative='two-sided')\n        print(f', p={res_l.pvalue:.6f}')\n    else:\n        print(', N/A')\nprint()\n\np_sc = sc_cor / n\np_co = combo_cor / n\ndiff = p_co - p_sc\nvar_diff = (1/n) * ((b + c)/n - ((c - b)/n)**2)\nse_diff = math.sqrt(var_diff)\nci_low = diff - 1.96 * se_diff\nci_high = diff + 1.96 * se_diff\nprint('=== 95% CI for accuracy difference (normal approx) ===')\nprint(f'Diff = {diff:.4f} ({diff*100:.2f}pp)')\nprint(f'SE = {se_diff:.4f}')\nprint(f'95% CI: [{ci_low:.4f}, {ci_high:.4f}] = [{ci_low*100:.2f}pp, {ci_high*100:.2f}pp]')\nprint()\n\nrandom.seed(42)\nn_boot = 10000\nboot_diffs = []\nfor _ in range(n_boot):\n    idx = random.choices(range(n), k=n)\n    sc_b = sum(results[i]['sc_correct'] for i in idx)\n    co_b = sum(results[i]['combo_correct'] for i in idx)\n    boot_diffs.append((co_b - sc_b) / n)\nboot_diffs.sort()\nlo = boot_diffs[int(0.025 * n_boot)]\nhi = boot_diffs[int(0.975 * n_boot)]\nprint(f'Bootstrap 95% CI (10000 resamples): [{lo:.4f}, {hi:.4f}] = [{lo*100:.2f}pp, {hi*100:.2f}pp]')\nPYEOF\necho \"Script written\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T10:58:35.711421+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T10:58:35.711656+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/mcnemar_r.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/mcnemar_r.py"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T10:58:35.711819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -rn \"seed\" /root/symb_invariant_consensus/sica_full_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -rn \"seed\" /root/symb_invariant_consensus/sica_full_mvp.py"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T10:58:35.712002+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204 -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204 -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T10:58:35.712154+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Total problems: 204\\nSC correct: 111/204 = 0.5441\\nCombo correct: 118/204 = 0.5784\\nDelta: 0.0343 (7 problems)\\n\\n=== McNemar 2x2 Contingency Table ===\\nBoth correct:              110\\nBoth wrong:                85\\nSC correct, combo wrong:   1\\nSC wrong, combo correct:   8\\nDiscordant pairs:          9\\n\\nMcNemar exact p-value: 0.039062\\nSignificant (p<0.05): True\\nSignificant (p<0.01): False\\n\\n=== Per-label McNemar ===\\nTrue (n=72): both_correct=39, both_wrong=29, b=1, c=3, discordant=4, p=0.625000\\nFalse (n=63): both_correct=24, both_wrong=35, b=0, c=4, discordant=4, p=0.125000\\nUnknown (n=69): both_correct=47, both_wrong=21, b=0, c=1, discordant=1, p=1.000000\\n\\n=== 95% CI for accuracy difference (normal approx) ===\\nDiff = 0.0343 (3.43pp)\\nSE = 0.0145\\n95% CI: [0.0059, 0.0628] = [0.59pp, 6.28pp]\\n\\nBootstrap 95% CI (10000 resamples): [0.0098, 0.0637] = [0.98pp, 6.37pp]\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T10:58:35.712288+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"grep: /root/symb_invariant_consensus/sica_full_mvp.py: No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T10:58:35.712489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_0.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_1.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_2.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_3.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_4.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_5.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_6.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_7.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_8.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_9.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_10.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_11.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_12.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_13.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_14.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_15.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_16.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_17.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_18.json\\n/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates/folio_19.json\\n/root/symb_invariant_consensus/res
…[truncated 6370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T10:58:35.712678+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -rn \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -rn \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T10:58:35.712816+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T10:58:35.712964+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "find /root/symb_invariant_consensus -maxdepth 1 -name \"*.py\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "find /root/symb_invariant_consensus -maxdepth 1 -name \"*.py\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T10:58:35.713124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/prepare_proofwriter.py\\n/root/symb_invariant_consensus/run_mvp.py\\n/root/symb_invariant_consensus/run_full_mvp.py\\n/root/symb_invariant_consensus/prepare_data.py\\n/root/symb_invariant_consensus/run_case_study.py\\n/root/symb_invariant_consensus/run_contrastive_folio.py\\n/root/symb_invariant_consensus/analysis_k_ablation_folio204.py\\n/root/symb_invariant_consensus/analysis_constraint_ablation_folio204.py\\n/root/symb_invariant_consensus/extract_constraints.py\\n/root/symb_invariant_consensus/extract_constraints_parallel.py\\n/root/symb_invariant_consensus/extract_fast.py\\n/root/symb_invariant_consensus/run_ablation_analysis.py\\n/root/symb_invariant_consensus/reextract_failed.py\\n/root/symb_invariant_consensus/reextract_v2.py\\n/root/symb_invariant_consensus/reextract_v3.py\\n/root/symb_invariant_consensus/run_logiqa.py\\n/root/symb_invariant_consensus/run_z3_feedback_folio.py\\n/root/symb_invariant_consensus/run_consistency_filtering.py\\n/root/symb_invariant_consensus/premise_formalization.py\\n/root/symb_invariant_consensus/run_icl_oracle.py\\n/root/symb_invariant_consensus/backward_verification.py\\n/root/symb_invariant_consensus/diff_scorers.py\\n/root/symb_invariant_consensus/cross_trace_unsat.py\\n/root/symb_invariant_consensus/analysis_constraint_precision.py\\n/root/symb_invariant_consensus/run_multi_temp.py\\n/root/symb_invariant_consensus/compute_fleiss_kappa.py\\n/root/symb_invariant_consensus/sc_tiebreak_revalidation.py\\n/root/symb_invariant_consensus/mcnemar_recompute.py\\n/root/symb_invariant_consensus/run_icg.py\\n/root/symb_invariant_consensus/run_contrastive.py\\n/root/symb_invariant_consensus/run_debate.py\\n/root/symb_invariant_consensus/run_kappa_generalization.py\\n/root/symb_invariant_consensus/constraint_ablation.py\\n/root/symb_invariant_consensus/error_categorization.py\\n/root/symb_invariant_consensus/run_cross_model.py\\n/root/symb_invariant_con
…[truncated 956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T10:58:35.713273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -3 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -3 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T10:58:35.713405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"folio_0\\\": {\\n    \\\"answers\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T10:58:35.713527+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep -n \"seed\" /root/symb_invariant_consensus/run_full_mvp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep -n \"seed\" /root/symb_invariant_consensus/run_full_mvp.py"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T10:58:35.713650+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"213:    parser.add_argument(\\\"--seed\\\", type=int, default=None)\\n219:    if args.seed is not None:\\n221:        random.seed(args.seed)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T10:58:35.713772+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "grep \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "grep \"seed\" /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T10:58:35.713911+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T10:58:35.714082+00:00_

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
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
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

_source line 56 · 2026-05-20T10:58:35.714403+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Direction R: External NLI Verifier for FOLIO logical reasoning.\\n\\nUses an encoder-only NLI model (architecturally independent from decoder-only LLMs)\\nas an external verifier to break confirmation bias in self-consistency.\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport re\\nimport time\\nfrom collections import Counter\\nfrom pathlib import Path\\n\\nimport torch\\nfrom transformers import AutoModelForSequenceClassification, AutoTokenizer\\n\\n\\ndef parse_problem(problem_text):\\n    \\\"\\\"\\\"Extract premises and hypothesis from FOLIO problem text.\\\"\\\"\\\"\\n    m = re.search(\\n        r\\\"Given the following premises:\\\\n(.+?)\\\\n\\\\nDetermine whether the following conclusion is true, false, or uncertain:\\\\n(.+)\\\",\\n        problem_text,\\n        re.DOTALL,\\n    )\\n    if m:\\n        return m.group(1).strip(), m.group(2).strip()\\n    parts = problem_text.split(\\\"Determine whether the following conclusion is true, false, or uncertain:\\\")\\n    if len(parts) == 2:\\n        premises = parts[0].replace(\\\"Given the following premises:\\\", \\\"\\\").strip()\\n        hypothesis = parts[1].strip()\\n        return premises, hypothesis\\n    return problem_text, \\\"\\\"\\n\\n\\ndef load_nli_model(model_name, device):\\n    \\\"\\\"\\\"Load NLI model and tokenizer.\\\"\\\"\\\"\\n    print(f\\\"Loading NLI model: {model_name}\\\")\\n    tokenizer = AutoTokenizer.from_pretrained(model_name)\\n    model = AutoModelForSequenceClassification.from_pretrained(model_name)\\n    model.to(device)\\n    model.eval()\\n    id2label = model.config.id2label\\n    print(f\\\"  Labels: {id2label}\\\")\\n    return model, tokenizer, id2label\\n\\n\\ndef nli_predict(model, tokenizer, id2label, premise, hypothesis, device):\\n    \\\"\\\"\\\"Run NLI inference, return (label, probs_dict).\\\"\\\"\\\"\\n    inputs = tokenizer(\\n        premise
…[truncated 7589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T10:58:35.714636+00:00_

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
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
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

_source line 58 · 2026-05-20T10:58:35.714781+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T10:58:35.714931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls /root/symb_invariant_consensus/results/direction_r_deberta/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls /root/symb_invariant_consensus/results/direction_r_deberta/"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T10:58:35.715062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T10:58:35.715181+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "head -30 /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "head -30 /root/symb_invariant_consensus/results/direction_r_nli_large/results.json"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T10:58:35.715323+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_r1_deberta_standalone\\\": {\\n    \\\"accuracy\\\": 0.4951,\\n    \\\"correct\\\": 101,\\n    \\\"total\\\": 204,\\n    \\\"per_class\\\": {\\n      \\\"True\\\": {\\n        \\\"n\\\": 72,\\n        \\\"correct\\\": 43,\\n        \\\"accuracy\\\": 0.5972,\\n        \\\"precision\\\": 0.5181,\\n        \\\"recall\\\": 0.5972,\\n        \\\"f1\\\": 0.5548\\n      },\\n      \\\"False\\\": {\\n        \\\"n\\\": 63,\\n        \\\"correct\\\": 45,\\n        \\\"accuracy\\\": 0.7143,\\n        \\\"precision\\\": 0.4545,\\n        \\\"recall\\\": 0.7143,\\n        \\\"f1\\\": 0.5556\\n      },\\n      \\\"Unknown\\\": {\\n        \\\"n\\\": 69,\\n        \\\"correct\\\": 13,\\n        \\\"accuracy\\\": 0.1884,\\n        \\\"precision\\\": 0.5909,\\n        \\\"recall\\\": 0.1884,\\n        \\\"f1\\\": 0.2857\\n      }\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-20T10:58:35.715537+00:00_

全部分析完成。以下是完整报告。

---

## Direction R: McNemar Exact Test 报告

### 1. Seed 一致性

**确认：SC traces 一致。** R脚本直接从 `results/exp033_mistral_7b_folio204/sc_answer_matrix.json` 加载已有的12条SC traces，不重新生成。combo策略是将NLI预测作为第13票加入。

- R结果中SC baseline = 111/204 = 54.41%，与exp033完全吻合
- **修正**：exp033未使用显式seed（`run_full_mvp.py --seed`默认`None`，日志无seed记录）。用户所述"seed=42"未在代码/日志中找到证据。但这不影响一致性——R直接复用exp033的traces文件。

### 2. 模型注意

结果JSON记录的实际模型是 **`/root/models/deberta-large-mnli`**（`microsoft/deberta-large-mnli`），非任务描述中的 `cross-encoder/nli-deberta-v3-base`。请确认论文中引用正确的模型名。

### 3. 核心数字

| 指标 | 值 |
|------|-----|
| SC baseline | 111/204 = **54.41%** |
| NLI-SICA-combo | 118/204 = **57.84%** |
| Delta | **+3.43pp** (+7 problems) |

### 4. McNemar 2x2 Contingency Table

|  | Combo Correct | Combo Wrong |
|--|:---:|:---:|
| **SC Correct** | 110 | 1 |
| **SC Wrong** | 8 | 85 |

- b (SC correct, combo wrong) = **1**
- c (SC wrong, combo correct) = **8**
- Discordant pairs = **9**

### 5. McNemar Exact p-value

**p = 0.0391** (two-sided binomial test, min(1,8) out of 9 trials)

- **Significant at α=0.05**: Yes
- **Significant at α=0.01**: No

### 6. Per-label McNemar

| Label | n | b | c | discordant | p |
|-------|---|---|---|------------|---|
| True | 72 | 1 | 3 | 4 | 0.625 |
| False | 63 | 0 | 4 | 4 | 0.125 |
| Unknown | 69 | 0 | 1 | 1 | 1.000 |

per-label均不显著（样本太小，discordant pairs仅1-4对）。

### 7. 95% CI for Accuracy Difference

| 方法 | 95% CI |
|------|--------|
| Normal approximation | [0.59pp, 6.28pp] |
| Bootstrap (10000 resamples) | [0.98pp, 6.37pp] |

两种方法CI均不包含0，与p<0.05一致。

### 结论

NLI-SICA-combo相比SC baseline的+3.43pp提升**统计显著**（McNemar exact p=0.039, α=0.05），但效应量较小——9对discordant pairs中combo赢8对、输1对。CI上界约6pp，说明真实效应可能在0.6-6.4pp之间。如果论文需要report，建议同时给出p值和discordant pair counts，因为n=9的discordant pairs使得结果对单题翻转非常敏感。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r-mcnemar-seed-verify_20260520T105518"
}
```

</details>

---
