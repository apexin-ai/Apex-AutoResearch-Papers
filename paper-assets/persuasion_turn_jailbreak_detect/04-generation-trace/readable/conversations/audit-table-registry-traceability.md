# audit table registry traceability

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_audit_table-registry-traceability_20260523T191641.jsonl`
- **Structured JSON:** [`9b77f22f60c1397bfc4e.json`](../../sessions/9b/9b77f22f60c1397bfc4e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-23T19:31:19.283688+00:00_

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
  "session": "worker_audit_table-registry-traceability_20260523T191641",
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

_source line 2 · 2026-05-23T19:31:19.284035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:31:19.284213+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "persuasion_turn_jailbreak_detect",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:31:19.285264+00:00_

Error: result (205,256 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:31:19.285492+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T19:31:19.285651+00:00_

docs/paper/checklist.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:31:19.285779+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:31:19.285966+00:00_

total 1672
drwxr-xr-x 86 ubuntu ubuntu  12288 May 23 15:08 .
drwxr-xr-x 12 ubuntu ubuntu   4096 May 23 18:48 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 12:19 EXP-2
drwxr-xr-x  7 ubuntu ubuntu   4096 May 18 04:24 _project
-rw-r--r--  1 ubuntu ubuntu  12939 May 23 10:50 audit_appendix.md
-rw-r--r--  1 ubuntu ubuntu  18868 May 23 10:40 audit_experiments.md
-rw-r--r--  1 ubuntu ubuntu   9723 May 23 10:28 audit_main_text.md
drwxr-xr-x  4 ubuntu ubuntu   4096 May 17 07:59 data
drwxr-xr-x  4 ubuntu ubuntu   4096 May 18 04:17 dream_reports
drwxr-xr-x  2 ubuntu ubuntu   4096 May 19 00:01 embedding_tsne
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 10:40 exp1
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 17:10 exp10_fewshot_llm_judge
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 23:44 exp11_tost_equivalence
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 23:42 exp12_toxicchat_bootstrap
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 23:43 exp13_meanpool_multiseed
-rw-r--r--  1 ubuntu ubuntu   5006 May 19 23:52 exp17_diagnosis.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 12:35 exp18_e2e_finetune
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 12:43 exp19_wildchat_fpr
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 10:23 exp1_roberta_9class
-rw-r--r--  1 ubuntu ubuntu   2088 May 18 10:23 exp1_roberta_9class_results.json
-rw-r--r--  1 ubuntu ubuntu   1064 May 18 10:40 exp1_roberta_mlm_results.json
-rw-r--r--  1 ubuntu ubuntu   1041 May 18 10:40 exp1_roberta_vanilla_results.json
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 13:51 exp20_deepcontext_proxy
-rw-r--r--  1 ubuntu ubuntu  12228 May 20 13:50 exp20_deepcontext_proxy.py
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 14:14 exp21_cross_checkpoint
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 14:29 exp22_aa_early_detection
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 14:29 exp24_calibration_ece
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 14:29 exp25_fitd_early_detection
drwxr-xr-x  3 ubuntu ubuntu   4096 May 20 14:51 exp26_frozen_probing
-rw-r--r--  1 ubuntu ubuntu  13602 May 
…[truncated 7388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:31:19.286146+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T19:31:19.286394+00:00_

1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method})
…[truncated 16188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:31:19.286613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\n# The result is likely a JSON string itself\nexps = json.loads(result) if isinstance(result, str) else result\nprint(f'Type: {type(exps).__name__}')\nif isinstance(exps, list):\n    print(f'Count: {len(exps)}')\n    if exps:\n        print(f'Keys: {list(exps[0].keys())}')\n        # Print all exp_ids\n        for e in exps:\n            eid = e.get('exp_id', 'N/A')\n            status = e.get('status', 'N/A')\n            metrics = e.get('metrics', {})\n            print(f'{eid} | {status} | metrics_keys={list(metrics.keys()) if metrics else \\\"none\\\"}')\nelif isinstance(exps, dict):\n    print(f'Keys: {list(exps.keys())}')\n\" 2>&1 | head -200",
  "description": "Probe registry structure and list all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\n# The result is likely a JSON string itself\nexps = json.loads(result) if isinstance(result, str) else result\nprint(f'Type: {type(exps).__name__}')\nif isinstance(exps, list):\n    print(f'Count: {len(exps)}')\n    if exps:\n        print(f'Keys: {list(exps[0].keys())}')\n        # Print all exp_ids\n        for e in exps:\n            eid = e.get('exp_id', 'N/A')\n            status = e.get('status', 'N/A')\n            metrics = e.get('metrics', {})\n            print(f'{eid} | {status} | metrics_keys={list(metrics.keys()) if metrics else \\\"none\\\"}')\nelif isinstance(exps, dict):\n    print(f'Keys: {list(exps.keys())}')\n\" 2>&1 | head -200",
    "description": "Probe registry structure and list all experiments"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:31:19.286761+00:00_

Type: dict
Keys: ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:31:19.286902+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed.get('data', parsed)\nprint(f'Type of data: {type(experiments).__name__}')\nif isinstance(experiments, list):\n    print(f'Count: {len(experiments)}')\n    for e in experiments:\n        eid = e.get('exp_id', 'N/A')\n        status = e.get('status', 'N/A')\n        metrics = e.get('metrics', {})\n        conclusion = e.get('conclusion', '')[:80] if e.get('conclusion') else ''\n        mkeys = list(metrics.keys()) if metrics else []\n        print(f'  {eid} | {status} | conclusion={conclusion} | metrics_keys={mkeys}')\nelif isinstance(experiments, dict):\n    print(f'Keys: {list(experiments.keys())[:20]}')\n    # Maybe it's keyed by exp_id\n    for k, v in list(experiments.items())[:3]:\n        print(f'  {k}: {type(v).__name__}')\n\" 2>&1",
  "description": "Explore registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed.get('data', parsed)\nprint(f'Type of data: {type(experiments).__name__}')\nif isinstance(experiments, list):\n    print(f'Count: {len(experiments)}')\n    for e in experiments:\n        eid = e.get('exp_id', 'N/A')\n        status = e.get('status', 'N/A')\n        metrics = e.get('metrics', {})\n        conclusion = e.get('conclusion', '')[:80] if e.get('conclusion') else ''\n        mkeys = list(metrics.keys()) if metrics else []\n        print(f'  {eid} | {status} | conclusion={conclusion} | metrics_keys={mkeys}')\nelif isinstance(experiments, dict):\n    print(f'Keys: {list(experiments.keys())[:20]}')\n    # Maybe it's keyed by exp_id\n    for k, v in list(experiments.items())[:3]:\n        print(f'  {k}: {type(v).__name__}')\n\" 2>&1",
    "description": "Explore registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T19:31:19.287033+00:00_

Type of data: dict
Keys: ['experiments', 'count', 'total', 'baseline']
  experiments: dict
  count: int
  total: int

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:31:19.287154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nprint()\nfor eid, exp in experiments.items():\n    status = exp.get('status', 'N/A')\n    metrics = exp.get('metrics', {})\n    conclusion = (exp.get('conclusion') or '')[:120]\n    mkeys = list(metrics.keys()) if metrics else []\n    print(f'{eid} | {status} | metrics={mkeys}')\n    if conclusion:\n        print(f'  conclusion: {conclusion}')\n\" 2>&1",
  "description": "List all experiment IDs and their metrics keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed['data']['experiments']\nprint(f'Total experiments: {len(experiments)}')\nprint()\nfor eid, exp in experiments.items():\n    status = exp.get('status', 'N/A')\n    metrics = exp.get('metrics', {})\n    conclusion = (exp.get('conclusion') or '')[:120]\n    mkeys = list(metrics.keys()) if metrics else []\n    print(f'{eid} | {status} | metrics={mkeys}')\n    if conclusion:\n        print(f'  conclusion: {conclusion}')\n\" 2>&1",
    "description": "List all experiment IDs and their metrics keys"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T19:31:19.287390+00:00_

Total experiments: 136

exp67_length_matching | DONE | metrics=['dd_ood', 'aa_ood']
  conclusion: success
exp66_sharegpt_benign_adaptation | DONE | metrics=['baseline_fpr', 'baseline_n', 'data_source', 'adaptation_curve', 'comparison']
  conclusion: negative
exp65_svd_necessity_ablation | DONE | metrics=['original', 'remove_top3_svd', 'remove_random3']
  conclusion: success
exp64_toxicchat_confidence_analysis | DONE | metrics=['9class_majority', 'jb_mlm_majority', '9class_per_seed_high_conf_ratio', 'jb_mlm_per_seed_high_conf_ratio']
  conclusion: success
exp11_tost_equivalence | DONE | metrics=['dd_ood_full', 'actorattack_full', 'note']
  conclusion: success
exp46_inference_efficiency | DONE | metrics=['disped_latency_ms', 'disped_latency_std', 'disped_throughput_conv_s', 'disped_gpu_mem_MB', 'disped_params_M', 'qwen3_latency_ms', 'qwen3_latency_std', 'qwen3_throughput_conv_s', 'qwen3_gpu_mem_MB', 'qwen3_params_B', 'speedup_factor', 'memory_ratio', 'test_conversations', 'gpu']
  conclusion: success
exp63_toxicchat_fpfn | DONE | metrics=['9class_mv_f1', '9class_mv_fpr', '9class_mv_precision', '9class_mv_recall', 'mlm_mv_f1', 'mlm_mv_fpr', 'mlm_mv_precision', 'mlm_mv_recall', 'mlm_correct_9class_wrong_total', 'mlm_wins_fp_fraction', 'mlm_wins_fn_fraction', '9class_correct_mlm_wrong_total']
  conclusion: negative
exp62_topic_diagnosis | DONE | metrics=['vanilla_iid_fisher', 'vanilla_dd_fisher', 'vanilla_aa_fisher', '9class_iid_fisher', '9class_dd_fisher', '9class_aa_fisher', 'topic_iid_fisher', 'topic_dd_fisher', 'topic_aa_fisher', 'finding']
  conclusion: negative
exp61_random_binary_partition | DONE | metrics=['iid_f1', 'dd_ood_f1', 'aa_ood_f1', 'n_partitions', 'n_perfect', 'outlier_seed', 'outlier_aa_f1', 'wall_clock_min']
  conclusion: success
exp60_turncount_baseline | DONE | metrics=['tc_full', 'tc_k1', 'disped_full']
  conclusion: success
exp59_resample_350 | DONE | metrics=['dd_ood_f1', 'aa_ood_f1', 'iid_f1', 'dd_seeds', 'aa_seeds', 'iid_seeds']
  conclusion: s
…[truncated 22011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:31:19.287606+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tab:mixed_llm|tab:ood_perturbation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tab:mixed_llm|tab:ood_perturbation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T19:31:19.287766+00:00_

docs/paper/appendix.tex:143:\label{tab:ood_perturbation}
docs/paper/appendix.tex:243:[Omitted long matching line]
docs/paper/appendix.tex:252:\label{tab:mixed_llm}
docs/paper/appendix.tex:264:[Omitted long matching line]
docs/paper/experiments.tex:174:All preceding experiments use single-source (Qwen3-8B) data. To test whether the evidence hierarchy transfers when training data mixes LLM sources, we train on 250 Qwen + 250 Llama-3.1-8B conversations (Table~\ref{tab:mixed_llm}).
docs/paper/experiments.tex:211:[Omitted long matching line]
docs/paper/main.aux:1357:\newlabel{tab:ood_perturbation}{{10}{14}{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta $: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm $std where available}{table.caption.32}{}}
docs/paper/main.aux:1454:\newlabel{tab:mixed_llm}{{13}{15}{Mixed-LLM training (250 Qwen + 250 Llama conversations, 3-seed mean$\pm $std where available). ToxicChat evaluated on balanced set (408 conversations)}{table.caption.38}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:31:19.287915+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\n\n# Extract detailed metrics for key experiments\npython3 -c \"\nimport json, sys\n\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed['data']['experiments']\n\n# Key experiments for Table 2 (main_results): 9-class, MLM, vanilla on IID and DD OOD\n# Key experiments for Table 3 (evidence_hierarchy): all variants on DD, AA\n# Key experiments for Table 4 (cross_encoder): RoBERTa variants\n# Key experiments for Table 5 (mixed_llm): exp16 or exp44\n# Key experiments for Table 6 (human_data): exp8_mhj_human_data\n# Key experiments for Table 7 (ood_perturbation): exp4, exp6\n\nimportant_ids = [\n    # Main results / evidence hierarchy\n    'plan_002_clean_training', 'plan_002_seed123', 'plan_002_seed456',\n    'plan_006_cross_attack_clean', 'phase_b_full',\n    'vanilla_multiseed_dd_ood',\n    'plan_017_mlm_control', 'plan_017_mlm_perturbation',\n    'plan_018_wiki_mlm_control', 'plan_018_wiki_perturbation',\n    'plan_016v2_topic_control', 'plan_016v2_topic_perturbation',\n    'plan_013_none_collapse', 'plan_013_binary_perturbation',\n    'mf1_binary_seed123', 'mf1_binary_seed456',\n    'mf1_scrambled_seed123', 'mf1_scrambled_seed456',\n    'plan_003_scrambled_ablation',\n    # ActorAttack\n    'exp2_actorattack_ood', 'exp2_actorattack_mcnemar',\n    # Perturbation\n    'exp4_dd_ood_perturbation', 'exp6_actorattack_perturbation',\n    # Cross-encoder\n    'exp1_roberta_9class', 'exp1_roberta_mlm', 'exp1_roberta_vanilla',\n    'exp15_roberta_large', 'exp15b_roberta_large_lr', 'exp15c_roberta_large_mlm',\n    # Mixed LLM\n    'exp16_multi_llm', 'exp44_multi_llm_mixed',\n    # Human data\n    'exp8_mhj_human_data',\n    # TF-IDF\n    'exp7_tfidf_perprefix_actorattack',\n    # Bootstrap CI\n    'exp9_bootstrap_ci',\n    # TOST\n    'exp11_tost_equivalence', 'exp41_tost_10seed',\n    # Mean pooling\n    'exp27_mean_pooling', 'exp13_meanpool_multiseed',\n    # LLM judge\n    'exp5_llm_judge_ood', 'exp10_fewshot_llm_judge',\n    # Llama Guard\n    'exp40_llama_guard_baseline',\n    # Wildchat FPR\n    'exp19_wildchat_fpr',\n    # Benign adaptation\n    'exp45_benign_adaptation_curve',\n    'exp52_oasst2_n25_multiseed',\n    # ToxicChat bootstrap\n    'exp12_toxicchat_bootstrap',\n    # 5-seed expansion\n    'exp55_5seed_mlm_vs_9class_aa',\n    # Deep context proxy\n    'exp20_deepcontext_proxy',\n    # Frozen probing\n    'exp26_frozen_probing',\n    # Data efficiency\n    'exp28_data_efficiency', 'exp28b_data_efficiency_supplement', 'exp28c_vanilla_supplement',\n    # Inference efficiency\n    'exp29_inference_efficiency', 'exp46_inference_efficiency',\n    # TOST 10-seed\n    'exp41_tost_10seed',\n    # Dual-OOD\n    'exp42_ood_benign_mixed', 'exp42b_balanced_ratio_ablation',\n    'exp51_lmsys_benign_ood',\n    # Random binary partition\n    'exp61_random_binary_partition',\n    # 9class per-prefix\n    'exp22_aa_early_detection', 'exp25_fitd_early_detection',\n    # Strategy prediction\n    'exp32_strategy_prediction', 'exp33_strategy_prediction_plan002',\n    # Exp59\n    'exp59_resample_350',\n]\n\nfor eid in important_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics', {})\n        conclusion = exp.get('conclusion', '')\n        print(f'=== {eid} (conclusion={conclusion}) ===')\n        print(json.dumps(metrics, indent=2, default=str))\n        print()\n    else:\n        print(f'=== {eid}: NOT FOUND ===')\n        print()\n\" 2>&1",
  "description": "Extract detailed metrics for all key experiments",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\n\n# Extract detailed metrics for key experiments\npython3 -c \"\nimport json, sys\n\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed['data']['experiments']\n\n# Key experiments for Table 2 (main_results): 9-class, MLM, vanilla on IID and DD OOD\n# Key experiments for Table 3 (evidence_hierarchy): all variants on DD, AA\n# Key experiments for Table 4 (cross_encoder): RoBERTa variants\n# Key experiments for Table 5 (mixed_llm): exp16 or exp44\n# Key experiments for Table 6 (human_data): exp8_mhj_human_data\n# Key experiments for Table 7 (ood_perturbation): exp4, exp6\n\nimportant_ids = [\n    # Main results / evidence hierarchy\n    'plan_002_clean_training', 'plan_002_seed123', 'plan_002_seed456',\n    'plan_006_cross_attack_clean', 'phase_b_full',\n    'vanilla_multiseed_dd_ood',\n    'plan_017_mlm_control', 'plan_017_mlm_perturbation',\n    'plan_018_wiki_mlm_control', 'plan_018_wiki_perturbation',\n    'plan_016v2_topic_control', 'plan_016v2_topic_perturbation',\n    'plan_013_none_collapse', 'plan_013_binary_perturbation',\n    'mf1_binary_seed123', 'mf1_binary_seed456',\n    'mf1_scrambled_seed123', 'mf1_scrambled_seed456',\n    'plan_003_scrambled_ablation',\n    # ActorAttack\n    'exp2_actorattack_ood', 'exp2_actorattack_mcnemar',\n    # Perturbation\n    'exp4_dd_ood_perturbation', 'exp6_actorattack_perturbation',\n    # Cross-encoder\n    'exp1_roberta_9class', 'exp1_roberta_mlm', 'exp1_roberta_vanilla',\n    'exp15_roberta_large', 'exp15b_roberta_large_lr', 'exp15c_roberta_large_mlm',\n    # Mixed LLM\n    'exp16_multi_llm', 'exp44_multi_llm_mixed',\n    # Human data\n    'exp8_mhj_human_data',\n    # TF-IDF\n    'exp7_tfidf_perprefix_actorattack',\n    # Bootstrap CI\n    'exp9_bootstrap_ci',\n    # TOST\n    'exp11_tost_equivalence', 'exp41_tost_10seed',\n    # Mean pooling\n    'exp27_mean_pooling', 'exp13_meanpool_multiseed',\n    # LLM judge\n    'exp5_llm_judge_ood', 'exp10_fewshot_llm_judge',\n    # Llama Guard\n    'exp40_llama_guard_baseline',\n    # Wildchat FPR\n    'exp19_wildchat_fpr',\n    # Benign adaptation\n    'exp45_benign_adaptation_curve',\n    'exp52_oasst2_n25_multiseed',\n    # ToxicChat bootstrap\n    'exp12_toxicchat_bootstrap',\n    # 5-seed expansion\n    'exp55_5seed_mlm_vs_9class_aa',\n    # Deep context proxy\n    'exp20_deepcontext_proxy',\n    # Frozen probing\n    'exp26_frozen_probing',\n    # Data efficiency\n    'exp28_data_efficiency', 'exp28b_data_efficiency_supplement', 'exp28c_vanilla_supplement',\n    # Inference efficiency\n    'exp29_inference_efficiency', 'exp46_inference_efficiency',\n    # TOST 10-seed\n    'exp41_tost_10seed',\n    # Dual-OOD\n    'exp42_ood_benign_mixed', 'exp42b_balanced_ratio_ablation',\n    'exp51_lmsys_benign_ood',\n    # Random binary partition\n    'exp61_random_binary_partition',\n    # 9class per-prefix\n    'exp22_aa_early_detection', 'exp25_fitd_early_detection',\n    # Strategy prediction\n    'exp32_strategy_prediction', 'exp33_strategy_prediction_plan002',\n    # Exp59\n    'exp59_resample_350',\n]\n\nfor eid in important_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics', {})\n        conclusion = exp.get('conclusion', '')\n        print(f'=== {eid} (conclusion={conclusion}) ===')\n        print(json.dumps(metrics, indent=2, default=str))\n        print()\n    else:\n        print(f'=== {eid}: NOT FOUND ===')\n        print()\n\" 2>&1",
    "description": "Extract detailed metrics for all key experiments",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T19:31:19.288267+00:00_

&lt;persisted-output>
Output too large (50.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt

Preview (first 2KB):
=== plan_002_clean_training (conclusion=negative) ===
{
  "treatment_k1_f1": 1,
  "baseline_k1_f1": 0.987,
  "treatment_k2_f1": 1,
  "baseline_k2_f1": 0.9867,
  "treatment_k3_f1": 1,
  "baseline_k3_f1": 0.9867,
  "treatment_k5_f1": 1,
  "baseline_k5_f1": 1,
  "treatment_full_f1": 1,
  "baseline_full_f1": 1,
  "tfidf_all_k_f1": 1,
  "max_delta_pp": 1.3,
  "pass_criteria_5pp": false
}

=== plan_002_seed123 (conclusion=success) ===
{
  "treatment_k1_f1": 1,
  "treatment_k2_f1": 1,
  "treatment_k3_f1": 1,
  "treatment_k5_f1": 1,
  "treatment_full_f1": 1,
  "baseline_k1_f1": 0.987,
  "baseline_k2_f1": 0.987,
  "baseline_k3_f1": 0.987,
  "baseline_full_f1": 1,
  "tfidf_all_k_f1": 1,
  "dd_ood_k1_f1": 1,
  "dd_ood_k2_f1": 0.9904,
  "dd_ood_k3_f1": 0.9904,
  "dd_ood_k5_f1": 1,
  "dd_ood_full_f1": 1
}

=== plan_002_seed456 (conclusion=success) ===
{
  "treatment_k1_f1": 1,
  "treatment_k2_f1": 1,
  "treatment_k3_f1": 1,
  "treatment_k5_f1": 1,
  "treatment_full_f1": 1,
  "baseline_k1_f1": 0.9296,
  "baseline_k2_f1": 0.9589,
  "baseline_k3_f1": 0.9867,
  "baseline_k5_f1": 0.9867,
  "baseline_full_f1": 1,
  "tfidf_all_k_f1": 1,
  "deberta_best_epoch": 2,
  "deberta_persuasion_acc": 0.8593,
  "deberta_intent_acc": 1,
  "dd_ood_k1_f1": 0.9715,
  "dd_ood_k2_f1": 0.9622,
  "dd_ood_k3_f1": 0.935,
  "dd_ood_k5_f1": 0.9904,
  "dd_ood_full_f1": 0.9904
}

=== plan_006_cross_attack_clean (conclusion=success) ===
{
  "dd_treatment_full_f1": 1,
  "dd_baseline_full_f1": 0.2845,
  "dd_treatment_k1_f1": 1,
  "dd_baseline_k1_f1": 0.5752,
  "dd_treatment_k2_f1": 0.9904,
  "dd_baseline_k2_f1": 0.4381,
  "dd_treatment_k3_f1": 0.9904,
  "dd_baseline_k3_f1": 0.3596,
  "dd_treatment_k5_f1": 1,
  "dd_baseline_k5_f1": 0.3
…[truncated 291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:31:19.288452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "offset": "125",
  "limit": "160"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "offset": "125",
    "limit": "160"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:31:19.288687+00:00_

125	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
126	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
127	\midrule
128	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
129	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	Table~\ref{tab:perturbation} shows perturbation behavior on IID data.
135	Classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.
136	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp.
137	McNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\leq$7 discordant pairs, statistical power is limited.
138	
139	\begin{table}[t]
140	\centering
141	\small
142	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
143	\label{tab:ood_perturbation}
144	\begin{tabular}{@{}lcccc@{}}
145	\toprule
146	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
147	\midrule
148	9-class & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & +0.6 \\
149	Binary & 1.000$\pm$.000 & 1.000$\pm$.000 & 0.0 & +0.6 \\
150	Scrambled & .994$\pm$.005 & 1.000$\pm$.000 & +0.6 & $-$0.3 \\
151	\midrule
152	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
153	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
154	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
155	\bottomrule
156	\end{tabular}
157	\vspace{-2pt}
158	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
159	\end{table}
160	
161	On OOD DD, the IID pattern replicates: classification-
…[truncated 9609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:31:19.288853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:31:19.288977+00:00_

File content (26464 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:31:19.289107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T19:31:19.289368+00:00_

1	=== plan_002_clean_training (conclusion=negative) ===
2	{
3	  "treatment_k1_f1": 1,
4	  "baseline_k1_f1": 0.987,
5	  "treatment_k2_f1": 1,
6	  "baseline_k2_f1": 0.9867,
7	  "treatment_k3_f1": 1,
8	  "baseline_k3_f1": 0.9867,
9	  "treatment_k5_f1": 1,
10	  "baseline_k5_f1": 1,
11	  "treatment_full_f1": 1,
12	  "baseline_full_f1": 1,
13	  "tfidf_all_k_f1": 1,
14	  "max_delta_pp": 1.3,
15	  "pass_criteria_5pp": false
16	}
17	
18	=== plan_002_seed123 (conclusion=success) ===
19	{
20	  "treatment_k1_f1": 1,
21	  "treatment_k2_f1": 1,
22	  "treatment_k3_f1": 1,
23	  "treatment_k5_f1": 1,
24	  "treatment_full_f1": 1,
25	  "baseline_k1_f1": 0.987,
26	  "baseline_k2_f1": 0.987,
27	  "baseline_k3_f1": 0.987,
28	  "baseline_full_f1": 1,
29	  "tfidf_all_k_f1": 1,
30	  "dd_ood_k1_f1": 1,
31	  "dd_ood_k2_f1": 0.9904,
32	  "dd_ood_k3_f1": 0.9904,
33	  "dd_ood_k5_f1": 1,
34	  "dd_ood_full_f1": 1
35	}
36	
37	=== plan_002_seed456 (conclusion=success) ===
38	{
39	  "treatment_k1_f1": 1,
40	  "treatment_k2_f1": 1,
41	  "treatment_k3_f1": 1,
42	  "treatment_k5_f1": 1,
43	  "treatment_full_f1": 1,
44	  "baseline_k1_f1": 0.9296,
45	  "baseline_k2_f1": 0.9589,
46	  "baseline_k3_f1": 0.9867,
47	  "baseline_k5_f1": 0.9867,
48	  "baseline_full_f1": 1,
49	  "tfidf_all_k_f1": 1,
50	  "deberta_best_epoch": 2,
51	  "deberta_persuasion_acc": 0.8593,
52	  "deberta_intent_acc": 1,
53	  "dd_ood_k1_f1": 0.9715,
54	  "dd_ood_k2_f1": 0.9622,
55	  "dd_ood_k3_f1": 0.935,
56	  "dd_ood_k5_f1": 0.9904,
57	  "dd_ood_full_f1": 0.9904
58	}
59	
60	=== plan_006_cross_attack_clean (conclusion=success) ===
61	{
62	  "dd_treatment_full_f1": 1,
63	  "dd_baseline_full_f1": 0.2845,
64	  "dd_treatment_k1_f1": 1,
65	  "dd_baseline_k1_f1": 0.5752,
66	  "dd_treatment_k2_f1": 0.9904,
67	  "dd_baseline_k2_f1": 0.4381,
68	  "dd_treatment_k3_f1": 0.9904,
69	  "dd_baseline_k3_f1": 0.3596,
70	  "dd_treatment_k5_f1": 1,
71	  "dd_baseline_k5_f1": 0.3105,
72	  "fitd_treatment_full_f1": 1,
73	  "fitd_baseline_full_f1": 1,
74	  "fi
…[truncated 10487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:31:19.289525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T19:31:19.289817+00:00_

500	  "iid_full_f1": 1,
501	  "iid_k1_f1": 1,
502	  "iid_k2_f1": 1,
503	  "iid_k3_f1": 1,
504	  "iid_k5_f1": 1,
505	  "deberta_val_persuasion_acc": 1,
506	  "deberta_val_intent_acc": 1,
507	  "seed": 123
508	}
509	
510	=== mf1_binary_seed456 (conclusion=success) ===
511	{
512	  "dd_ood_full_f1": 1,
513	  "dd_ood_k1_f1": 1,
514	  "dd_ood_k2_f1": 1,
515	  "dd_ood_k3_f1": 0.9904,
516	  "dd_ood_k5_f1": 1,
517	  "deberta_val_persuasion_acc": 1,
518	  "deberta_val_intent_acc": 1,
519	  "seed": 456
520	}
521	
522	=== mf1_scrambled_seed123 (conclusion=success) ===
523	{
524	  "val_persuasion_acc": 0.6724,
525	  "val_intent_acc": 1,
526	  "dd_ood_f1_k1": 1,
527	  "dd_ood_f1_k2": 1,
528	  "dd_ood_f1_k3": 1,
529	  "dd_ood_f1_k5": 1,
530	  "dd_ood_f1_full": 1
531	}
532	
533	=== mf1_scrambled_seed456 (conclusion=success) ===
534	{
535	  "dd_ood_full_f1": 1,
536	  "dd_ood_k1_f1": 1,
537	  "dd_ood_k2_f1": 1,
538	  "dd_ood_k3_f1": 0.99,
539	  "dd_ood_k5_f1": 1,
540	  "deberta_val_persuasion_acc": 0.698,
541	  "seed": 456
542	}
543	
544	=== plan_003_scrambled_ablation (conclusion=negative) ===
545	{
546	  "scrambled_k1_f1": 0.9744,
547	  "scrambled_k2_f1": 1,
548	  "scrambled_k3_f1": 1,
549	  "scrambled_k5_f1": 1,
550	  "scrambled_full_f1": 1,
551	  "proper_k2_f1": 0.9867,
552	  "proper_k3_f1": 0.9867,
553	  "baseline_k2_f1": 0.8788,
554	  "baseline_k3_f1": 0.9276,
555	  "scrambled_deberta_persuasion_acc": 0.6437,
556	  "proper_deberta_persuasion_acc": 0.7963,
557	  "data_version": "v4c (NOT plan_002 data)"
558	}
559	
560	=== exp2_actorattack_ood (conclusion=success) ===
561	{
562	  "deberta_9class": {
563	    "k1": 0.773,
564	    "k1_std": 0.041,
565	    "k2": 0.855,
566	    "k2_std": 0.048,
567	    "k3": 0.921,
568	    "k3_std": 0.046,
569	    "k5": 0.966,
570	    "k5_std": 0.028,
571	    "full": 0.972,
572	    "full_std": 0.026
573	  },
574	  "deberta_binary": {
575	    "k1": 0.737,
576	    "k1_std": 0.074,
577	    "k2": 0.89,
578	    "k2_std": 0.065,
579	    "k3": 0.951,
580	   
…[truncated 10530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:31:19.289971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
  "offset": "1000",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
    "offset": "1000",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T19:31:19.290261+00:00_

1000	    }
1001	  },
1002	  "mcnemar_clean_full": {
1003	    "9class_vs_vanilla": {
1004	      "seed42": {
1005	        "p": 0,
1006	        "b": 78,
1007	        "c": 0
1008	      },
1009	      "seed123": {
1010	        "p": 0,
1011	        "b": 72,
1012	        "c": 0
1013	      },
1014	      "seed456": {
1015	        "p": 0,
1016	        "b": 78,
1017	        "c": 0
1018	      }
1019	    }
1020	  },
1021	  "note": "CORRECTED 2026-05-18: vanilla seed123/456 GRU checkpoints and binary seed42 DeBERTa+GRU checkpoints were wrong (used different models than exp2). Fixed to match exp2 checkpoints. Clean baselines now consistent with exp2. All variants still degrade under perturbation except topic at K=1. 9class significantly outperforms vanilla on both clean and perturbed (McNemar all p<0.001)."
1022	}
1023	
1024	=== exp1_roberta_9class (conclusion=success) ===
1025	{
1026	  "dd_ood_full_f1_mean": 0.9936,
1027	  "dd_ood_full_f1_std": 0.0045,
1028	  "dd_ood_k1_mean": 0.9873,
1029	  "dd_ood_k1_std": 0.0119,
1030	  "dd_ood_k2_mean": 0.9505,
1031	  "dd_ood_k2_std": 0.0284,
1032	  "dd_ood_k3_mean": 0.9563,
1033	  "dd_ood_k3_std": 0.0189,
1034	  "dd_ood_k5_mean": 0.9872,
1035	  "dd_ood_k5_std": 0.009,
1036	  "iid_full_f1": 1,
1037	  "n_seeds": 3,
1038	  "encoder": "roberta-base"
1039	}
1040	
1041	=== exp1_roberta_mlm (conclusion=success) ===
1042	{
1043	  "dd_ood_full_f1_mean": 0.9874,
1044	  "dd_ood_full_f1_std": 0.0178,
1045	  "dd_ood_k1_mean": 0.9428,
1046	  "dd_ood_k1_std": 0.0184,
1047	  "dd_ood_k2_mean": 0.9747,
1048	  "dd_ood_k2_std": 0.0232,
1049	  "dd_ood_k3_mean": 0.9747,
1050	  "dd_ood_k3_std": 0.0232,
1051	  "dd_ood_k5_mean": 0.9841,
1052	  "dd_ood_k5_std": 0.016,
1053	  "n_seeds": 3,
1054	  "encoder": "roberta-base"
1055	}
1056	
1057	=== exp1_roberta_vanilla (conclusion=success) ===
1058	{
1059	  "dd_ood_full_f1_mean": 0.9813,
1060	  "dd_ood_full_f1_std": 0.0264,
1061	  "dd_ood_k1_mean": 0.9127,
1062	  "dd_ood_k1_std": 0.1028,
1063	  "dd_ood_k2_mean": 0.9003,
106
…[truncated 11618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T19:31:19.290419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
  "offset": "1500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
    "offset": "1500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T19:31:19.290701+00:00_

1500	    "std": 0
1501	  },
1502	  "dd_ood_k5": {
1503	    "mean": 1,
1504	    "std": 0
1505	  },
1506	  "dd_ood_full": {
1507	    "mean": 1,
1508	    "std": 0
1509	  },
1510	  "aa_ood_full": {
1511	    "mean": 1,
1512	    "std": 0
1513	  },
1514	  "fitd_ood_full": {
1515	    "mean": 1,
1516	    "std": 0
1517	  },
1518	  "metric": "f1_macro",
1519	  "seeds": 3,
1520	  "early_stop_epoch": 4
1521	}
1522	
1523	=== exp13_meanpool_multiseed (conclusion=success) ===
1524	{
1525	  "dd_ood": {
1526	    "k1": {
1527	      "mean": 0.9905,
1528	      "std": 0.0134
1529	    },
1530	    "k2": {
1531	      "mean": 0.9936,
1532	      "std": 0.009
1533	    },
1534	    "k3": {
1535	      "mean": 0.9842,
1536	      "std": 0.016
1537	    },
1538	    "k5": {
1539	      "mean": 0.9968,
1540	      "std": 0.0045
1541	    },
1542	    "full": {
1543	      "mean": 0.9905,
1544	      "std": 0.0134
1545	    }
1546	  },
1547	  "actorattack": {
1548	    "k1": {
1549	      "mean": 0.8301,
1550	      "std": 0.0272
1551	    },
1552	    "k2": {
1553	      "mean": 0.903,
1554	      "std": 0.0229
1555	    },
1556	    "k3": {
1557	      "mean": 0.9622,
1558	      "std": 0.0076
1559	    },
1560	    "k5": {
1561	      "mean": 0.9716,
1562	      "std": 0.0153
1563	    },
1564	    "full": {
1565	      "mean": 0.9623,
1566	      "std": 0.0151
1567	    }
1568	  },
1569	  "metric": "f1_macro",
1570	  "classifier": "mean_pooling + linear",
1571	  "encoder": "9-class DeBERTa-v3-base",
1572	  "note": "Mean pooling matches BiGRU on DD OOD (all K \u22650.98). ActorAttack K\u22653 also \u22650.96. Confirms temporal modeling not necessary."
1573	}
1574	
1575	=== exp5_llm_judge_ood (conclusion=success) ===
1576	{
1577	  "dd_ood": {
1578	    "k1_binary_f1": 0,
1579	    "k2_binary_f1": 0,
1580	    "k3_binary_f1": 0,
1581	    "k5_binary_f1": 0,
1582	    "full_binary_f1": 0,
1583	    "k1_macro_f1": 0.2436,
1584	    "k2_macro_f1": 0.2436,
1585	    "k3_macro_f1": 0.2436,
1586	    "k5_macro_f1": 0.2436,
1587	    "full_macro
…[truncated 10256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:31:19.290900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
  "offset": "2000",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/b1rll3za1.txt",
    "offset": "2000",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T19:31:19.291182+00:00_

2000	  },
2001	  "vanilla": {
2002	    "125": {
2003	      "iid": 0.53,
2004	      "dd_ood": 0.24,
2005	      "aa_ood": 0.24
2006	    },
2007	    "350": {
2008	      "iid": 1,
2009	      "dd_ood": 0.36,
2010	      "aa_ood": 0.49
2011	    }
2012	  },
2013	  "note": "9-class at 14% data (50 samples) already achieves DD=1.0, AA=0.99 \u2014 outperforming vanilla at 100% by 64pp (DD) and 50pp (AA). Sample efficiency entirely driven by DAPT representation quality."
2014	}
2015	
2016	=== exp28b_data_efficiency_supplement (conclusion=success) ===
2017	{
2018	  "9class_3seed_N50_aa_ood": "0.969\u00b10.037",
2019	  "9class_3seed_N125_aa_ood": "0.975\u00b10.019",
2020	  "9class_3seed_N250_aa_ood": "0.975\u00b10.035",
2021	  "9class_3seed_N350_aa_ood": "0.972\u00b10.033",
2022	  "note": "9-class 3-seed complete. Vanilla N=50/250 missing (script crashed float16 dtype in GRU eval). exp28b added seed123+456 for 9-class only."
2023	}
2024	
2025	=== exp28c_vanilla_supplement (conclusion=success) ===
2026	{
2027	  "9class_3seed": {
2028	    "N50": {
2029	      "iid": "1.000\u00b10.000",
2030	      "dd_ood": "1.000\u00b10.000",
2031	      "aa_ood": "0.969\u00b10.030"
2032	    },
2033	    "N125": {
2034	      "iid": "1.000\u00b10.000",
2035	      "dd_ood": "1.000\u00b10.000",
2036	      "aa_ood": "0.975\u00b10.016"
2037	    },
2038	    "N250": {
2039	      "iid": "1.000\u00b10.000",
2040	      "dd_ood": "1.000\u00b10.000",
2041	      "aa_ood": "0.975\u00b10.029"
2042	    },
2043	    "N350": {
2044	      "iid": "1.000\u00b10.000",
2045	      "dd_ood": "0.978\u00b10.024",
2046	      "aa_ood": "0.972\u00b10.027"
2047	    }
2048	  },
2049	  "vanilla_seed42": {
2050	    "N50": {
2051	      "iid": 0.646,
2052	      "dd_ood": 0.529,
2053	      "aa_ood": 0.234
2054	    },
2055	    "N125": {
2056	      "iid": 0.532,
2057	      "dd_ood": 0.244,
2058	      "aa_ood": 0.244
2059	    },
2060	    "N250": {
2061	      "iid": 0.987,
2062	      "dd_ood": 0.365,
2063	      "aa_ood": 0.502
2064	    },
206
…[truncated 10246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T19:31:19.291565+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\n\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed['data']['experiments']\n\n# Search for any roberta_large 3-seed or multiseed experiments\nfor eid, exp in experiments.items():\n    if 'roberta' in eid.lower() and 'large' in eid.lower():\n        print(f'=== {eid} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2, default=str))\n        print()\n    # Also check for dual_ood\n    if 'dual' in eid.lower() or ('ood' in eid.lower() and 'benign' in eid.lower()):\n        print(f'=== {eid} ===')\n        m = exp.get('metrics', {})\n        print(json.dumps(m, indent=2, default=str))\n        print()\n\" 2>&1",
  "description": "Search for RoBERTa-large multiseed and dual-OOD experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\n\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexperiments = parsed['data']['experiments']\n\n# Search for any roberta_large 3-seed or multiseed experiments\nfor eid, exp in experiments.items():\n    if 'roberta' in eid.lower() and 'large' in eid.lower():\n        print(f'=== {eid} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2, default=str))\n        print()\n    # Also check for dual_ood\n    if 'dual' in eid.lower() or ('ood' in eid.lower() and 'benign' in eid.lower()):\n        print(f'=== {eid} ===')\n        m = exp.get('metrics', {})\n        print(json.dumps(m, indent=2, default=str))\n        print()\n\" 2>&1",
    "description": "Search for RoBERTa-large multiseed and dual-OOD experiments"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T19:31:19.291775+00:00_

=== exp51_lmsys_benign_ood ===
{
  "baseline_fpr": 0.575,
  "baseline_n": 200,
  "data_source": "oasst2 (real crowdsourced human)",
  "adaptation_curve": {
    "n0": {
      "fpr": 0.575
    },
    "n10": {
      "fpr": 0.205,
      "dd_f1": 1,
      "aa_f1": 1,
      "fitd_f1": 1
    },
    "n25": {
      "fpr": 0.015,
      "dd_f1": 1,
      "aa_f1": 0.953,
      "fitd_f1": 1
    },
    "n50": {
      "fpr": 0.005,
      "dd_f1": 1,
      "aa_f1": 0.99,
      "fitd_f1": 1
    }
  },
  "comparison_wildchat": {
    "baseline_fpr": 0.681,
    "n10_fpr": 0,
    "n10_sufficient": true
  }
}

=== exp42_ood_benign_mixed ===
{
  "wildchat_fpr_mean": 0,
  "wildchat_fpr_std": 0,
  "iid_f1_mean": 1,
  "ood_dd_f1_mean": 1,
  "ood_aa_f1_mean": 0.956,
  "ood_fitd_f1_mean": 1,
  "wildchat_eval_n": 49,
  "data_filtered": "27/226 jailbreak patterns removed",
  "train_size": "500 (350 orig + 150 WildChat benign)"
}

=== exp15c_roberta_large_mlm ===
{
  "dd_ood": {
    "mlm": {
      "k1": 0.876,
      "k3": 0.902,
      "full": 0.884
    },
    "vanilla_exp15": {
      "k1": 0.878,
      "k3": 0.915,
      "full": 0.927
    },
    "9class_exp15": {
      "k1": 0.965,
      "k3": 0.96,
      "full": 0.987
    }
  },
  "actorattack": {
    "mlm": {
      "k1": 0.876,
      "k3": 0.881,
      "full": 0.874
    },
    "vanilla_exp15": {
      "k1": 0.977,
      "k3": 0.99,
      "full": 1
    },
    "9class_exp15": {
      "k1": 0.718,
      "k3": 0.881,
      "full": 0.946
    }
  },
  "key_finding": "MLM DAPT hurts both DD OOD and AA vs vanilla. AA: MLM 0.874 < 9class 0.946 < vanilla 1.000. Representation shift from continued pretraining itself conflicts with frozen-encoder GRU, not classification head interference."
}

=== exp15b_roberta_large_lr ===
{
  "dd_ood": {
    "9class_lr1e5": {
      "k1": 0.899,
      "k3": 0.851,
      "full": 0.948
    },
    "9class_lr2e5_exp15": {
      "k1": 0.965,
      "k3": 0.96,
      "full": 0.987
    }
  },
  "actorattack": {
    "9class_lr1e5"
…[truncated 975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:31:19.291932+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp15* 2>/dev/null\nls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ | grep -i 'roberta_large\\|dual_ood\\|roberta-large'",
  "description": "Search for RoBERTa-large artifact files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp15* 2>/dev/null\nls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ | grep -i 'roberta_large\\|dual_ood\\|roberta-large'",
    "description": "Search for RoBERTa-large artifact files"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T19:31:19.292076+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T19:31:19.292218+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ | grep -iE 'dual|wildchat|benign_adapt|adapt_curve|roberta.large'",
  "description": "Search for dual-OOD and RoBERTa-large artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ | grep -iE 'dual|wildchat|benign_adapt|adapt_curve|roberta.large'",
    "description": "Search for dual-OOD and RoBERTa-large artifacts"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T19:31:19.292339+00:00_

exp19_wildchat_fpr
exp45_benign_adaptation_curve
exp51_adapt_curve
exp66_sharegpt_benign_adaptation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T19:31:19.292459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexps = parsed['data']['experiments']\n\n# Search for exp with roberta large 3-seed or std values\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    ms = json.dumps(m)\n    # Find any experiment with 'roberta' and 'large' and 'std' or '3seed' or multiple seeds\n    if 'roberta' in eid.lower() and 'large' in eid.lower():\n        print(f'{eid}: {ms[:200]}')\n    # Or any exp with roberta_large in metrics\n    if 'roberta_large' in ms.lower() or 'roberta-large' in ms.lower():\n        print(f'{eid}: {ms[:200]}')\n\nprint('---')\n# Check exp40 for Llama Guard pooled recall\nexp40 = exps.get('exp40_llama_guard_baseline', {})\nm40 = exp40.get('metrics', {})\n# Calculate pooled recall\ndd_rec = m40.get('ood_dd', {}).get('full', {}).get('rec_jb', 0)\naa_rec = m40.get('ood_aa', {}).get('full', {}).get('rec_jb', 0)\nfitd_rec = m40.get('ood_fitd', {}).get('full', {}).get('rec_jb', 0)\niid_rec = m40.get('iid_crescendo', {}).get('full', {}).get('rec_jb', 0)\nprint(f'Llama Guard recalls: DD={dd_rec}, AA={aa_rec}, FITD={fitd_rec}, IID={iid_rec}')\n# Pooled: total correct / total jailbreak\ntotal_correct = int(dd_rec*80) + int(aa_rec*80) + int(fitd_rec*80) + int(iid_rec*38)\ntotal_jb = 80 + 80 + 80 + 38\nprint(f'Pooled recall: {total_correct}/{total_jb} = {total_correct/total_jb:.3f} ({total_correct/total_jb*100:.1f}%)')\n\" 2>&1",
  "description": "Search for RoBERTa-large 3-seed data and check Llama Guard pooled recall"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexps = parsed['data']['experiments']\n\n# Search for exp with roberta large 3-seed or std values\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    ms = json.dumps(m)\n    # Find any experiment with 'roberta' and 'large' and 'std' or '3seed' or multiple seeds\n    if 'roberta' in eid.lower() and 'large' in eid.lower():\n        print(f'{eid}: {ms[:200]}')\n    # Or any exp with roberta_large in metrics\n    if 'roberta_large' in ms.lower() or 'roberta-large' in ms.lower():\n        print(f'{eid}: {ms[:200]}')\n\nprint('---')\n# Check exp40 for Llama Guard pooled recall\nexp40 = exps.get('exp40_llama_guard_baseline', {})\nm40 = exp40.get('metrics', {})\n# Calculate pooled recall\ndd_rec = m40.get('ood_dd', {}).get('full', {}).get('rec_jb', 0)\naa_rec = m40.get('ood_aa', {}).get('full', {}).get('rec_jb', 0)\nfitd_rec = m40.get('ood_fitd', {}).get('full', {}).get('rec_jb', 0)\niid_rec = m40.get('iid_crescendo', {}).get('full', {}).get('rec_jb', 0)\nprint(f'Llama Guard recalls: DD={dd_rec}, AA={aa_rec}, FITD={fitd_rec}, IID={iid_rec}')\n# Pooled: total correct / total jailbreak\ntotal_correct = int(dd_rec*80) + int(aa_rec*80) + int(fitd_rec*80) + int(iid_rec*38)\ntotal_jb = 80 + 80 + 80 + 38\nprint(f'Pooled recall: {total_correct}/{total_jb} = {total_correct/total_jb:.3f} ({total_correct/total_jb*100:.1f}%)')\n\" 2>&1",
    "description": "Search for RoBERTa-large 3-seed data and check Llama Guard pooled recall"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T19:31:19.292624+00:00_

exp15c_roberta_large_mlm: {"dd_ood": {"mlm": {"k1": 0.876, "k3": 0.902, "full": 0.884}, "vanilla_exp15": {"k1": 0.878, "k3": 0.915, "full": 0.927}, "9class_exp15": {"k1": 0.965, "k3": 0.96, "full": 0.987}}, "actorattack": {"ml
exp15b_roberta_large_lr: {"dd_ood": {"9class_lr1e5": {"k1": 0.899, "k3": 0.851, "full": 0.948}, "9class_lr2e5_exp15": {"k1": 0.965, "k3": 0.96, "full": 0.987}}, "actorattack": {"9class_lr1e5": {"k1": 0.459, "k3": 0.676, "full
exp15_roberta_large: {"dd_ood": {"roberta_large_vanilla": {"k1": 0.878, "k3": 0.915, "full": 0.927}, "roberta_large_9class": {"k1": 0.965, "k3": 0.96, "full": 0.987}}, "actorattack": {"roberta_large_vanilla": {"k1": 0.977
exp15_roberta_large: {"dd_ood": {"roberta_large_vanilla": {"k1": 0.878, "k3": 0.915, "full": 0.927}, "roberta_large_9class": {"k1": 0.965, "k3": 0.96, "full": 0.987}}, "actorattack": {"roberta_large_vanilla": {"k1": 0.977
---
Llama Guard recalls: DD=0.0125, AA=0, FITD=0, IID=0.1053
Pooled recall: 5/278 = 0.018 (1.8%)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T19:31:19.292789+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexps = parsed['data']['experiments']\n\n# Check exp51_adapt_curve and exp56 for dual-OOD values\nfor eid in ['exp51_adapt_curve', 'exp56_crossllm_10shot', 'exp56_crossllm_10shot_adaptation', 'exp66_sharegpt_benign_adaptation', 'exp45', 'exp67_length_matching']:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'=== {eid} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2, default=str)[:800])\n        print()\n    else:\n        print(f'{eid}: NOT FOUND')\n\" 2>&1",
  "description": "Check adapt curve and dual-OOD experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "REGFILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect/a3b0276b-76a8-455b-9a2e-91310c9bfe46/tool-results/mcp-agent-ml-research-read_registry-1779563817327.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = data['result']\nparsed = json.loads(result) if isinstance(result, str) else result\nexps = parsed['data']['experiments']\n\n# Check exp51_adapt_curve and exp56 for dual-OOD values\nfor eid in ['exp51_adapt_curve', 'exp56_crossllm_10shot', 'exp56_crossllm_10shot_adaptation', 'exp66_sharegpt_benign_adaptation', 'exp45', 'exp67_length_matching']:\n    if eid in exps:\n        exp = exps[eid]\n        print(f'=== {eid} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2, default=str)[:800])\n        print()\n    else:\n        print(f'{eid}: NOT FOUND')\n\" 2>&1",
    "description": "Check adapt curve and dual-OOD experiments"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T19:31:19.292953+00:00_

exp51_adapt_curve: NOT FOUND
exp56_crossllm_10shot: NOT FOUND
=== exp56_crossllm_10shot_adaptation ===
{
  "baseline_fpr": 0.945,
  "baseline_aa_llama_recall": 0.74,
  "adaptation_curve": {
    "n0": {
      "fpr": 0.945,
      "dd_f1": 1,
      "aa_f1": 0.99,
      "fitd_f1": 1,
      "dd_llama_recall": 1,
      "aa_llama_recall": 0.74,
      "fitd_llama_recall": 1
    },
    "n5": {
      "fpr": 0.055,
      "dd_f1": 0.694,
      "aa_f1": 0.841,
      "fitd_f1": 0.99,
      "dd_llama_recall": 0.64,
      "aa_llama_recall": 0.04,
      "fitd_llama_recall": 0.76
    },
    "n10": {
      "fpr": 0.03,
      "dd_f1": 0.816,
      "aa_f1": 0.601,
      "fitd_f1": 1,
      "dd_llama_recall": 0.6,
      "aa_llama_recall": 0,
      "fitd_llama_recall": 0.8
    },
    "n25": {
      "fpr": 0.005,
      "dd_f1": 0.556,
      "aa_f1": 0.271,
      "fitd_f1": 0.99,
      "dd_llama_recall": 0.08,
    

=== exp66_sharegpt_benign_adaptation ===
{
  "baseline_fpr": 0.39,
  "baseline_n": 200,
  "data_source": "ShareGPT (real user-ChatGPT conversations)",
  "adaptation_curve": {
    "n0": {
      "fpr": 0.39
    },
    "n5": {
      "fpr": 0.21,
      "iid_f1": 1,
      "dd_f1": 0.953,
      "aa_f1": 0.891,
      "fitd_f1": 1
    },
    "n10": {
      "fpr_mean": 0.105,
      "fpr_seeds": [
        0.075,
        0.155,
        0.085
      ],
      "iid_f1": 0.987,
      "dd_f1_mean": 0.906,
      "aa_f1_mean": 0.852,
      "fitd_f1": 1
    },
    "n15": {
      "fpr": 0.095,
      "iid_f1": 1,
      "dd_f1": 0.917,
      "aa_f1": 0.874,
      "fitd_f1": 1
    },
    "n20": {
      "fpr": 0.1,
      "iid_f1": 1,
      "dd_f1": 0.926,
      "aa_f1": 0.858,
      "fitd_f1": 1
    },
    "n25": {
      "fpr_mean": 0.027,
      "fpr_see

exp45: NOT FOUND
=== exp67_length_matching ===
{
  "dd_ood": {
    "full_set_f1": 0.887,
    "full_set_std": 0.086,
    "range_matched_f1": 0.88,
    "range_matched_std": 0.094,
    "range_matched_delta": -0.008,
    "bucket_matched_f1": 0.913,
    "bu
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T19:31:19.293122+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ -name \"*.json\" | xargs grep -l \"0.855\\|dual.ood\\|no.adapt\" 2>/dev/null | head -5",
  "description": "Search for dual-OOD result files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ -name \"*.json\" | xargs grep -l \"0.855\\|dual.ood\\|no.adapt\" 2>/dev/null | head -5",
    "description": "Search for dual-OOD result files"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T19:31:19.293248+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp2_actorattack_ood.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp12_toxicchat_bootstrap/exp12_toxicchat_bootstrap.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/EXP-2/data/exp2_actorattack_ood.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T19:31:19.293367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ -name \"*.json\" -path \"*exp45*\" -o -name \"*.json\" -path \"*exp51*\" -o -name \"*.json\" -path \"*dual*\" -o -name \"*.json\" -path \"*wildchat*\" 2>/dev/null | head -10",
  "description": "Find wildchat/dual-OOD JSON files in artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/ -name \"*.json\" -path \"*exp45*\" -o -name \"*.json\" -path \"*exp51*\" -o -name \"*.json\" -path \"*dual*\" -o -name \"*.json\" -path \"*wildchat*\" 2>/dev/null | head -10",
    "description": "Find wildchat/dual-OOD JSON files in artifacts"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T19:31:19.293484+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp45/data/multiseed_n10_summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp45_benign_adaptation_curve/multiseed_n10_summary.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp51_adapt_curve/data/exp51_oasst2_adapt_curve.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T19:31:19.293623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp45_benign_adaptation_curve/multiseed_n10_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp45_benign_adaptation_curve/multiseed_n10_summary.json"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T19:31:19.293767+00:00_

1	{
2	  "experiment": "exp45_benign_adaptation_curve",
3	  "description": "Multi-seed robustness check for N=10 benign adaptation",
4	  "n": 10,
5	  "seeds": [42, 123, 456],
6	  "per_seed": {
7	    "42": {
8	      "wildchat_fpr": 0.0,
9	      "iid_f1_macro": 1.0,
10	      "ood_dd_f1": 1.0,
11	      "ood_aa_f1": 1.0,
12	      "ood_fitd_f1": 1.0,
13	      "ood_aa_recall": 1.0
14	    },
15	    "123": {
16	      "wildchat_fpr": 0.0,
17	      "iid_f1_macro": 1.0,
18	      "ood_dd_f1": 1.0,
19	      "ood_aa_f1": 0.9715,
20	      "ood_fitd_f1": 1.0,
21	      "ood_aa_recall": 0.9625
22	    },
23	    "456": {
24	      "wildchat_fpr": 0.0,
25	      "iid_f1_macro": 1.0,
26	      "ood_dd_f1": 1.0,
27	      "ood_aa_f1": 0.9715,
28	      "ood_fitd_f1": 1.0,
29	      "ood_aa_recall": 0.9625
30	    }
31	  },
32	  "aggregated_mean_std": {
33	    "wildchat_fpr": "0.000 ± 0.000",
34	    "iid_f1_macro": "1.000 ± 0.000",
35	    "ood_dd_f1": "1.000 ± 0.000",
36	    "ood_aa_f1": "0.981 ± 0.016",
37	    "ood_fitd_f1": "1.000 ± 0.000"
38	  }
39	}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_table-registry-traceability_20260523T191641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-23T19:31:19.294056+00:00_

I now have all the data needed. Let me write the comprehensive traceability report.

## Table 数据溯源报告

### Table 2 (main_results) — Cross-attack generalization, IID (Crescendo) / OOD (DD)

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class IID K=2 | 1.000±.000 | plan_002_* (treatment_k2_f1) | 1.000, 1.000, 1.000 → 1.000±.000 | ✅ |
| 9-class IID Full | 1.000±.000 | plan_002_* (treatment_full_f1) | 1.000, 1.000, 1.000 → 1.000±.000 | ✅ |
| 9-class OOD K=2 | .981±.013 | plan_006 + plan_002_{123,456} (dd_ood_k2) | 0.9904, 0.9904, 0.9622 → 0.981±.013 | ✅ |
| 9-class OOD Full | .997±.005 | plan_006 + plan_002_{123,456} (dd_ood_full) | 1.000, 1.000, 0.9904 → 0.997±.005 | ✅ |
| MLM IID K=2 | .974 | plan_017_mlm_control (iid_f1_k2 seed42) | 0.9737 → .974 | ✅ |
| MLM IID Full | 1.000 | plan_017_mlm_control (iid_f1_full seed42) | 1.000 | ✅ |
| MLM OOD K=2 | .993±.009 | plan_017_mlm_control (dd_ood_f1_k2) | mean=0.9934, std=0.0093 | ✅ |
| MLM OOD Full | .914±.115 | plan_017_mlm_control (dd_ood_f1_full) | mean=0.9138, std=0.115 | ✅ |
| Vanilla IID K=2 | .978±.016 | plan_002_* (baseline_k2) | 0.9867, 0.987, 0.9589 → mean=.978 | ⚠️ std |
| Vanilla IID Full | 1.000±.000 | plan_002_* (baseline_full) | 1.000, 1.000, 1.000 | ✅ |
| Vanilla OOD K=2 | .479±.038 | vanilla_multiseed_dd_ood (k2) | mean=0.479, std=0.038 | ✅ |
| Vanilla OOD Full | .312±.026 | vanilla_multiseed_dd_ood (full) | mean=0.312, std=0.026 | ✅ |
| TF-IDF IID K=2 | 1.000 | plan_002 (tfidf_all_k_f1) | 1.000 | ✅ |
| TF-IDF IID Full | 1.000 | plan_002 (tfidf_all_k_f1) | 1.000 | ✅ |
| TF-IDF OOD K=2 | 1.000 | exp7 (dd_ood k2) | 1.000 | ✅ |
| TF-IDF OOD Full | .961 | exp7 (dd_ood full) | 0.961 | ✅ |

---

### Table 3 (evidence_hierarchy) — DD-Full, AA-Full, DD-K=2

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class DD-Full | .997±.005 | plan_006/plan_002 | 1.000, 1.000, 0.990 → .997±.005 | ✅ |
| 9-class AA-Full | .972±.026 | exp2_actorattack_ood (deberta_9class) | full=0.972, std=0.026 | ✅ |
| 9-class DD-K=2 | .981±.013 | plan_006/plan_002 | 0.990, 0.990, 0.962 → .981±.013 | ✅ |
| Binary DD-Full | 1.000±.000 | mf1_binary_{123,456} + plan_013 (seed42) | seed123=1.000, seed456=1.000, seed42=0.990 → .997±.005 | ⚠️ 见下 |
| Binary AA-Full | .990±.008 | exp2_actorattack_ood (deberta_binary) | full=0.990, std=0.008 | ✅ |
| Binary DD-K=2 | .994±.009 | mf1_binary seeds k2 | seed123=1.000, seed456=1.000 | ⚠️ seed42缺失 |
| Scrambled DD-Full | .997±.005 | mf1_scrambled_{123,456} | seed123=1.000, seed456=1.000 | ⚠️ seed42缺失 |
| Scrambled AA-Full | .951±.043 | exp2_actorattack_ood (deberta_scrambled) | full=0.951, std=0.043 | ✅ |
| Scrambled DD-K=2 | .981±.026 | mf1_scrambled seeds k2 | seed123=1.000, seed456=1.000 | ⚠️ seed42缺失 |
| MLM DD-Full | .914±.115 | plan_017_mlm_control | mean=0.914, std=0.115 | ✅ |
| MLM AA-Full | .893±.080 | exp2_actorattack_ood (deberta_mlm) | full=0.893, std=0.080 | ✅ |
| MLM DD-K=2 | .993±.009 | plan_017_mlm_control | mean=0.993, std=0.009 | ✅ |
| Mean pooling DD-Full | .991±.013 | exp13_meanpool_multiseed (dd_ood.full) | mean=0.9905, std=0.0134 | ✅ |
| Mean pooling AA-Full | .962±.015 | exp13_meanpool_multiseed (actorattack.full) | mean=0.9623, std=0.0151 | ✅ |
| Mean pooling DD-K=2 | **1.000** | exp27_mean_pooling (dd_ood_k2) | 1.000±0 | ⚠️ 见下 |
| Topic DD-Full | .541±.207 | plan_016v2_topic_control | mean=0.5411, std=0.2069 | ✅ |
| Topic AA-Full | .625±.141 | exp2_actorattack_ood (deberta_topic) | full=0.625, std=0.141 | ✅ |
| Topic DD-K=2 | .593±.166 | plan_016v2_topic_control (k2) | mean=0.5926, std=0.1655 | ✅ |
| Wiki-MLM DD-Full | .904±.115 | plan_018_wiki_mlm_control | mean=0.904, std=0.115 | ✅ |
| Wiki-MLM AA-Full | .686±.297 | exp2_actorattack_ood (deberta_wiki_mlm) | full=0.686, std=0.297 | ✅ |
| Wiki-MLM DD-K=2 | .911±.073 | plan_018_wiki_mlm_control (k2) | mean=0.911, std=0.073 | ✅ |
| Vanilla DD-Full | .312±.026 | vanilla_multiseed_dd_ood | mean=0.312, std=0.026 | ✅ |
| Vanilla AA-Full | .258±.000 | exp2_actorattack_ood (deberta_vanilla) | full=0.258, std=0 | ✅ |
| Vanilla DD-K=2 | .479±.038 | vanilla_multiseed_dd_ood (k2) | mean=0.479, std=0.038 | ✅ |
| TF-IDF DD-Full | .961 | exp7 (dd_ood full) | 0.961 | ✅ |
| TF-IDF AA-Full | .261 | exp7 (actorattack full) | 0.2609 → .261 | ✅ |
| TF-IDF DD-K=2 | 1.000 | exp7 (dd_ood k2) | 1.000 | ✅ |
| Llama Guard DD-Full | .025 | exp40_llama_guard_baseline (ood_dd.full) | f1_jb=0.0244 → .025 | ⚠️ 指标不一致 |
| Llama Guard AA-Full | .000 | exp40_llama_guard_baseline (ood_aa.full) | f1_jb=0 | ⚠️ 指标不一致 |
| Dual-OOD no adapt DD | .855 | — | — | ❌ 无法溯源 |
| Dual-OOD no adapt AA | .842 | — | — | ❌ 无法溯源 |
| Dual-OOD +10-shot DD | .994 | — | — | ❌ 无法溯源 |
| Dual-OOD +10-shot AA | .981 | exp45 (aa_f1 n10 multiseed) | 0.981±0.016 | ⚠️ 部分匹配 |

---

### Table 4 (cross_encoder) — DD / AA Full, 3-seed

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| DeBERTa Vanilla DD | .312±.026 | vanilla_multiseed_dd_ood | mean=0.312, std=0.026 | ✅ |
| DeBERTa Vanilla AA | .258±.000 | exp2 (deberta_vanilla) | full=0.258, std=0 | ✅ |
| DeBERTa MLM DD | .914±.115 | plan_017_mlm_control | mean=0.914, std=0.115 | ✅ |
| DeBERTa MLM AA | .893±.080 | exp2 (deberta_mlm) | full=0.893, std=0.080 | ✅ |
| DeBERTa 9-class DD | .997±.005 | plan_006/plan_002 | mean=0.997, std=0.005 | ✅ |
| DeBERTa 9-class AA | .972±.026 | exp2 (deberta_9class) | full=0.972, std=0.026 | ✅ |
| RoBERTa-base Vanilla DD | .981±.026 | exp1_roberta_vanilla | mean=0.9813, std=0.0264 | ✅ |
| RoBERTa-base Vanilla AA | .466±.163 | exp2 (roberta_vanilla) | full=0.466, std=0.163 | ✅ |
| RoBERTa-base MLM DD | .987±.018 | exp1_roberta_mlm | mean=0.9874, std=0.0178 | ✅ |
| RoBERTa-base MLM AA | .730±.201 | exp2 (roberta_mlm) | full=0.730, std=0.201 | ✅ |
| RoBERTa-base 9-class DD | .994±.005 | exp1_roberta_9class | mean=0.9936, std=0.0045 | ✅ |
| RoBERTa-base 9-class AA | .939±.046 | exp2 (roberta_9class) | full=0.939, std=0.046 | ✅ |
| RoBERTa-large Vanilla DD | .927±.036 | exp15 (roberta_large_vanilla) | full=0.927 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large Vanilla AA | 1.000±.000 | exp15 (roberta_large_vanilla) | full=1.000 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large MLM DD | .884±.065 | exp15c (mlm) | full=0.884 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large MLM AA | .874±.014 | exp15c (mlm) | full=0.874 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large 9-class DD | .987±.004 | exp15 (roberta_large_9class) | full=0.987 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large 9-class AA | .946±.057 | exp15 (roberta_large_9class) | full=0.946 (single seed) | ⚠️ 无std来源 |

---

### Table 5 (mixed_llm) — 250 Qwen + 250 Llama

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class Mixed | .996±.006 | exp16 (9class_mean.mixed_test) | 0.996 | ⚠️ std无来源 |
| 9-class DD OOD | .818±.096 | exp16 (9class_mean.dd_ood) | 0.818, std=0.096 | ✅ |
| 9-class AA OOD | .504±.107 | exp16 (9class_mean.aa_ood) | 0.504, std=0.107 | ✅ |
| 9-class FITD OOD | .997±.005 | exp16 (9class_mean.fitd_ood) | 0.997, std=0.005 | ✅ |
| 9-class ToxicChat | .550±.052 | exp16 (9class_mean.toxicchat_balanced) | 0.55, std=0.052 | ✅ |
| MLM Mixed | .681±.226 | exp16 (mlm_mean.mixed_test) | **0.975** | ❌ 不一致 |
| MLM DD OOD | .289±.101 | exp16 (mlm_mean.dd_ood) | 0.289, std=0.101 | ✅ |
| MLM AA OOD | .258±.075 | exp16 (mlm_mean.aa_ood) | 0.258, std=0.075 | ✅ |
| MLM FITD OOD | .679±.188 | exp16 (mlm_mean.fitd_ood) | 0.679, std=0.188 | ✅ |
| MLM ToxicChat | .256±.053 | exp16 (mlm_mean.toxicchat_balanced) | 0.256, std=0.053 | ✅ |
| Vanilla Mixed | .802±.010 | exp16 (vanilla_mean.mixed_test) | 0.802 | ⚠️ std无来源 |
| Vanilla DD OOD | .291±.065 | exp16 (vanilla_mean.dd_ood) | 0.291, std=0.065 | ✅ |
| Vanilla AA OOD | .389±.073 | exp16 (vanilla_mean.aa_ood) | 0.389, std=0.073 | ✅ |
| Vanilla FITD OOD | .867±.022 | exp16 (vanilla_mean.fitd_ood) | 0.867, std=0.022 | ✅ |
| Vanilla ToxicChat | .356±.009 | exp16 (vanilla_mean.toxicchat_balanced) | 0.356, std=0.009 | ✅ |

---

### Table 6 (human_data) — ToxicChat macro F1

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| JB-MLM | .837±.013 | exp8 (jb_mlm_macro_f1) | 0.837, std=0.013 | ✅ |
| Wiki-MLM | .791±.093 | exp8 (wiki_mlm_macro_f1) | 0.791, std=0.093 | ✅ |
| Binary | .705±.072 | exp8 (binary_macro_f1) | 0.705, std=0.072 | ✅ |
| Scrambled | .616±.056 | exp8 (scrambled_macro_f1) | 0.616, std=0.056 | ✅ |
| 9-class | .596±.087 | exp8 (9class_macro_f1) | 0.596, std=0.087 | ✅ |
| Topic | .496±.042 | exp8 (topic_macro_f1) | 0.496, std=0.042 | ✅ |
| Vanilla | .413±.021 | exp8 (vanilla_macro_f1) | 0.413, std=0.021 | ✅ |

**Table 6 完全一致 ✅**

---

### Table 7 (ood_perturbation) — OOD DD, Clean/Perturbed Full, Δ

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class Clean Full | .994±.005 | exp4 (9class_3seed.clean_full) | 0.9968 (pooled) | ⚠️ .997 vs .994 |
| 9-class Pert Full | 1.000±.000 | exp4 (9class_3seed.perturbed_full) | 1.000 | ✅ |
| 9-class Δ Full | +0.6 | exp4 (delta_full) | +0.0032 → +0.3pp | ⚠️ +0.6 vs +0.3 |
| 9-class Δ K=1 | +0.6 | exp4 (delta_k1) | +0.0063 → +0.6pp | ✅ |
| Binary Clean Full | 1.000±.000 | exp4 (binary_3seed.clean_full) | 0.9968 | ⚠️ .997 vs 1.000 |
| Binary Pert Full | 1.000±.000 | exp4 (binary_3seed.perturbed_full) | 1.000 | ✅ |
| Binary Δ Full | 0.0 | exp4 | +0.0032 → +0.3pp | ⚠️ 0.0 vs +0.3 |
| Binary Δ K=1 | +0.6 | exp4 (delta_k1) | +0.0064 → +0.6pp | ✅ |
| Scrambled Clean Full | .994±.005 | exp4 (scrambled_3seed.clean_full) | 0.9968 | ⚠️ .997 vs .994 |
| Scrambled Pert Full | 1.000±.000 | exp4 (perturbed_full) | 1.000 | ✅ |
| JB MLM Clean Full | .914±.115 | exp4 (jb_mlm_3seed.clean_full) | 0.9138 | ✅ |
| JB MLM Pert Full | .941 | exp4 (jb_mlm_3seed.perturbed_full) | 0.9409 → .941 | ✅ |
| JB MLM Δ Full | +2.7 | exp4 (delta_full) | +0.0271 → +2.7pp | ✅ |
| Wiki MLM Clean Full | .904±.115 | exp4 (wiki_mlm_3seed.clean_full) | 0.9042 | ✅ |
| Wiki MLM Pert Full | .872 | exp4 (perturbed_full) | 0.8715 → .872 | ✅ |
| Wiki MLM Δ Full | −3.3 | exp4 (delta_full) | −0.0327 → −3.3pp | ✅ |
| Vanilla Clean Full | .312±.026 | exp4 (vanilla_3seed.clean_full) | 0.3123 → .312 | ✅ |
| Vanilla Pert Full | .339±.055 | exp4 (perturbed_full) | 0.3394 → .339 | ✅ |
| Vanilla Δ Full | +2.7 | exp4 (delta_full) | +0.0271 → +2.7pp | ✅ |
| Vanilla Δ K=1 | −6.8±1.1 | exp4 (delta_k1) | −0.0681 → −6.8pp | ✅ |

---

### ⚠️ 不一致（需修复或解释）

1. **Table 2 Vanilla IID K=2 std**: 论文 .016, 计算得 .013 (pop std, n=3). 论文声明使用 pop std (n divisor), 但 .016 匹配 Bessel-corrected std (n−1 divisor). 轻微不一致。

2. **Table 3 Binary DD-Full**: 论文 1.000±.000, 但 registry seed42 (plan_013_none_collapse) dd_binary_full_f1=0.9904. 如果 seed42 确实为 0.990, 则 3-seed mean=.997±.005, 不是 1.000±.000。

3. **Table 3 Mean pooling DD-K=2**: 论文 1.000, 但 exp13_meanpool_multiseed 报告 dd_ood.k2 mean=0.994±.009。论文使用了 exp27 (1.000±.000) 的值而非 exp13 的值, 两个实验结果不同 — 应统一使用同一组实验。

4. **Table 3 Llama Guard 指标不一致**: 论文显示 DD=.025 / AA=.000, 这是 **jailbreak-class F1** (f1_jb), 而其他所有行使用 **macro F1**。如果使用 macro F1, Llama Guard DD 应为 .253。虽然 Llama Guard 几乎不检测任何 jailbreak, 但表内指标不统一。

5. **Table 5 MLM Mixed**: 论文 .681±.226, registry exp16 mixed_test=0.975。差异巨大。可能原因: registry 存储的是 Qwen-only test 性能 (note 标注 "qwen_test INVALIDATED" 因 35.5% 数据泄漏), 而论文使用正确的 Qwen+Llama 混合测试集。但 registry 对应字段未更新。

6. **Table 7 Clean Full vs Table 2/3**: 9-class clean DD-Full 在 Table 7 为 .994, 在 Table 2/3 为 .997。两表应评估同一模型在同一数据上的结果, 差异 0.003 表明可能使用了不同的 checkpoint 或不同的评估代码。Binary 同理 (Table 7=1.000 vs 实际应为 .997)。

7. **Table 7 Δ Full 与 clean/pert 不一致**: 9-class clean=.994, pert=1.000, Δ 应为 +0.6pp; 但 exp4 pooled clean=0.9968 → per-seed 计算给出 Δ=+0.32pp, 不是 +0.6pp。Binary clean=1.000, pert=1.000, Δ 应为 0.0; exp4 pooled clean=0.9968 → Δ=+0.32pp。论文的 Δ 值基于四舍五入后的 .994 和 1.000 计算, 而非原始精度值。

---

### ❌ 无法溯源

1. **Table 3 Dual-OOD "no adapt" DD=.855, AA=.842** — 未找到对应 registry 实验。这些值来自将 WildChat benign 替换 IID benign 进行测试, 但该评估结果未注册。

2. **Table 3 Dual-OOD "+10-shot" DD=.994** — exp45 报告适配后 dd_f1=1.000 (使用 IID benign 测试), 与论文 .994 不符。.994 应来自以 WildChat benign 替换测试集的 dual-OOD 评估, 但该计算未注册。AA=.981 与 exp45 的 aa_f1=0.981 匹配, 但 DD 值不匹配。

3. **Table 4 RoBERTa-large 所有 std 值** — registry 仅有单 seed 值 (exp15/15b/15c), 无 3-seed 数据。论文标题声明 "3-seed mean±std", mean 值与 registry 单 seed 值完全吻合, 但 std 来源不明 (未注册为 registry 实验)。

4. **Table 3 Binary/Scrambled DD seed42** — mf1_binary 和 mf1_scrambled 系列仅有 seed123 和 seed456 数据。seed42 的 DD OOD 值需从 plan_013_none_collapse (binary) 推断, 但该实验可能使用不同数据版本 (v4c)。

5. **Table 5 Mixed/Vanilla Mixed 列 std 值** — registry exp16 仅存储 mean, 无 std。论文的 .006 (9-class) 和 .010 (vanilla) 无 registry 来源。

---

### 总结

- **完全一致**: Table 6 (human_data) 全部 7 行 ✅; Table 4 DeBERTa 和 RoBERTa-base 行 (12 cells) ✅; Table 2 大部分 cells ✅; Table 3 大部分 cells ✅
- **轻微不一致**: 主要是 pop std vs Bessel std (Table 2 vanilla IID K=2), 以及 Table 7 的 clean baseline 与 Table 2/3 相差 0.003 (可能来自不同评估 pipeline)
- **显著不一致**: Table 5 MLM Mixed (.681 vs registry 0.975); Table 3 Binary DD-Full (1.000 vs 计算应为 .997); Mean pooling DD-K=2 混用两组实验数据
- **无法溯源**: RoBERTa-large 的全部 std 值; Dual-OOD 的 4 个 cells; Table 5 Mixed 列的 std 值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_table-registry-traceability_20260523T191641"
}
```

</details>

---
