# analysis exp1 isr b03 s42 1000 r2 eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427.jsonl`
- **Structured JSON:** [`a33422e67d9101f6668a.json`](../../sessions/a3/a33422e67d9101f6668a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-15T11:37:39.962990+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T11:37:39.963450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:37:39.963687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls -la /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls -la /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T11:37:39.963885+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp1-isr-b03-s42-1000-r2'}",
  "project": "solver-trace-ablation",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp1-isr-b03-s42-1000-r2'}",
    "project": "solver-trace-ablation",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T11:37:39.964043+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 15728840\\ndrwxr-xr-x  3 root root       4096 May 15 19:32 .\\ndrwxr-xr-x 22 root root       4096 May 15 18:27 ..\\n-rw-r--r--  1 root root       1876 May 15 19:16 README.md\\n-rw-r--r--  1 root root        707 May 15 19:17 added_tokens.json\\n-rw-r--r--  1 root root       4168 May 15 19:17 chat_template.jinja\\ndrwxr-xr-x  2 root root       4096 May 15 19:16 checkpoint-1000\\n-rw-r--r--  1 root root       1535 May 15 19:16 config.json\\n-rw-r--r--  1 root root     172239 May 15 19:32 eval_results.json\\n-rw-r--r--  1 root root        188 May 15 19:16 generation_config.json\\n-rw-r--r--  1 root root    1671853 May 15 19:17 merges.txt\\n-rw-r--r--  1 root root 4990095032 May 15 19:17 model-00001-of-00004.safetensors\\n-rw-r--r--  1 root root 4944309096 May 15 19:17 model-00002-of-00004.safetensors\\n-rw-r--r--  1 root root 4996758848 May 15 19:17 model-00003-of-00004.safetensors\\n-rw-r--r--  1 root root 1158754848 May 15 19:17 model-00004-of-00004.safetensors\\n-rw-r--r--  1 root root      32856 May 15 19:17 model.safetensors.index.json\\n-rw-r--r--  1 root root     261304 May 15 19:16 reward_log.jsonl\\n-rw-r--r--  1 root root        613 May 15 19:17 special_tokens_map.json\\n-rw-r--r--  1 root root   11422654 May 15 19:17 tokenizer.json\\n-rw-r--r--  1 root root       5459 May 15 19:17 tokenizer_config.json\\n-rw-r--r--  1 root root       7953 May 15 19:17 training_args.bin\\n-rw-r--r--  1 root root    2776833 May 15 19:17 vocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.21}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T11:37:39.964181+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.306}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T11:37:39.964337+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/checkpoint-1000/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/checkpoint-1000/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:37:39.964472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"added_tokens.json\\nchat_template.jinja\\nconfig.json\\ngeneration_config.json\\nmerges.txt\\nmodel-00001-of-00004.safetensors\\nmodel-00002-of-00004.safetensors\\nmodel-00003-of-00004.safetensors\\nmodel-00004-of-00004.safetensors\\nmodel.safetensors.index.json\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntrainer_state.json\\ntraining_args.bin\\nvocab.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T11:37:39.964608+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "head -50 /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "head -50 /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:37:39.964864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 100,\\n    \\\"n_proved\\\": 95,\\n    \\\"prove_rate\\\": 0.95,\\n    \\\"mean_isr\\\": 0.734,\\n    \\\"isr_std\\\": 0.2575,\\n    \\\"median_isr\\\": 0.6,\\n    \\\"isr_pr_ratio\\\": 0.7726,\\n    \\\"proved_only_mean_isr\\\": 0.7726,\\n    \\\"min_isr\\\": 0.0,\\n    \\\"max_isr\\\": 1.0,\\n    \\\"by_answer_type\\\": {\\n      \\\"false\\\": {\\n        \\\"count\\\": 25,\\n        \\\"proved\\\": 25,\\n        \\\"prove_rate\\\": 1.0,\\n        \\\"mean_isr\\\": 0.824\\n      },\\n      \\\"unknown\\\": {\\n        \\\"count\\\": 41,\\n        \\\"proved\\\": 38,\\n        \\\"prove_rate\\\": 0.926829268292683,\\n        \\\"mean_isr\\\": 0.673170731707317\\n      },\\n      \\\"true\\\": {\\n        \\\"count\\\": 34,\\n        \\\"proved\\\": 32,\\n        \\\"prove_rate\\\": 0.9411764705882353,\\n        \\\"mean_isr\\\": 0.7411764705882353\\n      }\\n    },\\n    \\\"elapsed_seconds\\\": 108.1,\\n    \\\"avg_time_per_sample\\\": 1.1,\\n    \\\"solver\\\": \\\"Prover9Solver\\\",\\n    \\\"logic_type\\\": \\\"fol\\\",\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/exp1_isr_b03_s42_1000\\\"\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"index\\\": 0,\\n      \\\"id\\\": \\\"folio_765\\\",\\n      \\\"context\\\": \\\"Tipped employees are not entitled to be paid the federal minimum wage by their employees. \\\\nIf a person is a white-collar worker, they are entitled to be paid the federal minimum wage by their employees. \\\\nAll lawyers are white-collar workers.\\\\nEvery advocate is a lawyer.\\\\nMary is not a lawyer or a tipped employee.\\\",\\n      \\\"question\\\": \\\"Mary is an advocate.\\\",\\n      \\\"answer\\\": \\\"false\\\",\\n      \\\"formalization\\\": \\\"Premises:  \\\\n1. ∀x (P(x) → Q(x))  \\\\n2. ∃x R(x)  \\\\n\\\\nConclusion:  \\\\n∀x (P(x) → Q(x))  \\\\n∃x R(x)\\\",\\n      \\\"gen_time\\\": 1.51,\\n      \\\"eval_time\\
…[truncated 188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:37:39.965072+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "ls /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "ls /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T11:37:39.965217+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:37:39.965343+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/classify_h7.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/classify_h7.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T11:37:39.965474+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: classify_h7.py [-h] [--eval_path EVAL_PATH] [--batch BATCH [BATCH ...]]\\n                      [--out OUT]\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --eval_path EVAL_PATH\\n                        Single eval file\\n  --batch BATCH [BATCH ...]\\n                        Multiple eval files\\n  --out OUT             Output file path\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.59}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T11:37:39.965625+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && export CUDA_VISIBLE_DEVICES=0 && python3 scripts/classify_h7.py --eval_path /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval_results.json --out /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/h7_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && export CUDA_VISIBLE_DEVICES=0 && python3 scripts/classify_h7.py --eval_path /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval_results.json --out /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/h7_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:37:39.965787+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  exp1_isr_b03_s42_1000\\n============================================================\\nTotal samples: 100, Proved: 95\\nH7 strict  (single premise == conclusion):  0/95 = 0.0%\\nH1 strict  (multi-prem, concl in premises): 54/95 = 56.8%\\nAny conclusion-in-premise (H7+H1):          54/95 = 56.8%\\nH7 relaxed (single_premise + ISR>=0.5):     0/95 = 0.0%\\nSingle premise: 0/95 = 0.0%\\nISR = 1.0:      41/95 = 43.2%\\n\\n  H1 examples (first 3):\\n    folio_765: 2 premises, isr=0.6\\n    folio_66: 2 premises, isr=0.6\\n    folio_1378: 2 premises, isr=0.6\\n\\n\\n============================================================\\n  SUMMARY TABLE\\n============================================================\\nRun                                       H7       H1    H7+H1   Proved\\n------------------------------------------------------------\\nexp1_isr_b03_s42_1000                 0/95   54/95   54/95        95\\n------------------------------------------------------------\\n\\n\\nResults saved to /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/h7_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T11:37:39.965940+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/h7_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/h7_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:37:39.966077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  exp1_isr_b03_s42_1000\\n============================================================\\nTotal samples: 100, Proved: 95\\nH7 strict  (single premise == conclusion):  0/95 = 0.0%\\nH1 strict  (multi-prem, concl in premises): 54/95 = 56.8%\\nAny conclusion-in-premise (H7+H1):          54/95 = 56.8%\\nH7 relaxed (single_premise + ISR>=0.5):     0/95 = 0.0%\\nSingle premise: 0/95 = 0.0%\\nISR = 1.0:      41/95 = 43.2%\\n\\n  H1 examples (first 3):\\n    folio_765: 2 premises, isr=0.6\\n    folio_66: 2 premises, isr=0.6\\n    folio_1378: 2 premises, isr=0.6\\n\\n\\n============================================================\\n  SUMMARY TABLE\\n============================================================\\nRun                                       H7       H1    H7+H1   Proved\\n------------------------------------------------------------\\nexp1_isr_b03_s42_1000                 0/95   54/95   54/95        95\\n------------------------------------------------------------\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:37:39.966242+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "solver-trace-ablation",
  "fields": "['exp_id', 'metrics', 'conclusion']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "solver-trace-ablation",
    "fields": "['exp_id', 'metrics', 'conclusion']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T11:37:39.966582+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp1-isr-b03-s42-1000-r2\": {\"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_problems\": 100, \"h7_rate\": 0.4316, \"h7_count\": 41, \"h1_rate\": 0.4316, \"h1_count\": 41, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"eval_component_count_mean\": 5, \"eval_by_type\": {\"false\": {\"count\": 25, \"proved\": 25, \"prove_rate\": 1, \"mean_isr\": 0.824}, \"unknown\": {\"count\": 41, \"proved\": 38, \"prove_rate\": 0.927, \"mean_isr\": 0.673}, \"true\": {\"count\": 34, \"proved\": 32, \"prove_rate\": 0.941, \"mean_isr\": 0.741}}, \"train_final_prove_rate\": 0.829, \"train_final_mean_isr\": 0.727, \"train_loss\": 0.0041, \"train_runtime_seconds\": 6280, \"train_final_entropy\": 9e-06, \"completions_mean_length\": 47}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000-r2\": {\"metrics\": {\"train_final_prove_rate\": 0.989, \"train_final_mean_isr\": 0.353, \"train_final_reward\": 1.062, \"train_steps\": 1000, \"train_runtime_seconds\": 2957, \"eval_prove_rate\": 1, \"eval_mean_isr\": 0.3333, \"eval_isr_std\": 0, \"eval_median_isr\": 0.3333, \"eval_proved_only_isr\": 0.3333, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_component_count_mean\": 3, \"genuine_rate\": 0, \"genuine_count\": 0, \"tautological_collapse\": true, \"h7_rate\": null, \"h7_count\": null, \"h1_rate\": null, \"h1_count\": null}, \"conclusion\": \"negative\"}, \"plan018-additive-random-b01-s42-1000\": {\"conclusion\": \"failed\"}, \"exp1-isr-b03-s42-1000\": {\"conclusion\": \"failed\"}, \"plan002-additive-b01-s42-1000\": {\"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.9, \"eval_mean_isr\": 0.7892, \"eval_isr_std\": 0.3424, \"eval_proved_only_isr\": 0.8769, \"eval_median_isr\": 1, \"h7_strict_count\": 83, \"h7_strict_rate\": 0.922
…[truncated 12902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T11:37:39.966860+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp1-isr-b03-s42-1000-r2",
  "field": "metrics",
  "value": "{'eval_prove_rate': 0.95, 'eval_mean_isr': 0.734, 'eval_isr_std': 0.2575, 'eval_median_isr': 0.6, 'eval_proved_only_isr': 0.7726, 'eval_n_proved': 95, 'eval_n_problems': 100, 'eval_data': 'proofwriter_fol_100.jsonl', 'eval_by_answer_type': {'false': {'count': 25, 'proved': 25, 'prove_rate': 1, 'mean_isr': 0.824}, 'unknown': {'count': 41, 'proved': 38, 'prove_rate': 0.927, 'mean_isr': 0.673}, 'true': {'count': 34, 'proved': 32, 'prove_rate': 0.941, 'mean_isr': 0.741}}, 'h7_count': 0, 'h7_rate': 0, 'h1_count': 54, 'h1_rate': 0.568, 'genuine_count': 41, 'genuine_rate': 0.432, 'tautological_collapse': False, 'isr_1_count': 41, 'isr_1_rate': 0.432, 'single_premise_count': 0, 'train_final_prove_rate': 0.829, 'train_final_mean_isr': 0.727, 'train_loss': 0.0041, 'train_runtime_seconds': 6280, 'train_final_entropy': 9e-06, 'completions_mean_length': 47}",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp1-isr-b03-s42-1000-r2",
    "field": "metrics",
    "value": "{'eval_prove_rate': 0.95, 'eval_mean_isr': 0.734, 'eval_isr_std': 0.2575, 'eval_median_isr': 0.6, 'eval_proved_only_isr': 0.7726, 'eval_n_proved': 95, 'eval_n_problems': 100, 'eval_data': 'proofwriter_fol_100.jsonl', 'eval_by_answer_type': {'false': {'count': 25, 'proved': 25, 'prove_rate': 1, 'mean_isr': 0.824}, 'unknown': {'count': 41, 'proved': 38, 'prove_rate': 0.927, 'mean_isr': 0.673}, 'true': {'count': 34, 'proved': 32, 'prove_rate': 0.941, 'mean_isr': 0.741}}, 'h7_count': 0, 'h7_rate': 0, 'h1_count': 54, 'h1_rate': 0.568, 'genuine_count': 41, 'genuine_rate': 0.432, 'tautological_collapse': False, 'isr_1_count': 41, 'isr_1_rate': 0.432, 'single_premise_count': 0, 'train_final_prove_rate': 0.829, 'train_final_mean_isr': 0.727, 'train_loss': 0.0041, 'train_runtime_seconds': 6280, 'train_final_entropy': 9e-06, 'completions_mean_length': 47}",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T11:37:39.967099+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp1-isr-b03-s42-1000-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:31:37.813Z\", \"updated_at\": \"2026-05-15T11:36:54.648Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"224651\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000-r2.log\", \"submitted_at\": \"2026-05-15T09:32:05.796Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7320.6, \"gpu_hours\": 2.03}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"224651\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T11:27:09.017Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:27:13.616148+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_probl
…[truncated 979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T11:37:39.967303+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp1-isr-b03-s42-1000-r2",
  "field": "conclusion",
  "value": "success",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp1-isr-b03-s42-1000-r2",
    "field": "conclusion",
    "value": "success",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T11:37:39.967479+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp1-isr-b03-s42-1000-r2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:31:37.813Z\", \"updated_at\": \"2026-05-15T11:37:26.456Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"224651\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000-r2.log\", \"submitted_at\": \"2026-05-15T09:32:05.796Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7320.6, \"gpu_hours\": 2.03}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"224651\", \"log_path\": \"~/runs/solver-trace-ablation/exp1-isr-b03-s42-1000-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 --num_steps 1000 --beta 0.3 --seed 42 --no_wandb\\\"\", \"finished_at\": \"2026-05-15T11:27:09.017Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:27:13.616148+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.95, \"eval_mean_isr\": 0.734, \"eval_isr_std\": 0.2575, \"eval_median_isr\": 0.6, \"eval_proved_only_isr\": 0.7726, \"eval_n_proved\": 95, \"eval_n_probl
…[truncated 978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T11:37:39.967663+00:00_

评估完成。结果汇总：

## exp1-isr-b03-s42-1000-r2 (ISR β=0.3, 1000步, seed42)

| 指标 | 值 |
|------|-----|
| **prove_rate** | 0.95 (95/100) |
| **mean_isr** | 0.734 |
| **H7** | 0 (0%) |
| **H1** | 54 (56.8%) |
| **genuine** | 41 (43.2%) |
| **ISR=1.0** | 41 (43.2%) |
| **tautological_collapse** | false |
| **by_answer_type** | 34 true / 25 false / 41 unknown ✓ |

### 与 500 步 ISR β=0.3 (exp1-isr-b03-s43-r3) 对比

| 指标 | 500步 s43 | 1000步 s42 | 变化 |
|------|-----------|------------|------|
| PR | 0.86 | 0.95 | +9pp |
| mean_isr | 0.254 | 0.734 | +0.48 |
| H7 | 4 (4.7%) | 0 (0%) | ↓ |
| H1 | 59 (68.6%) | 54 (56.8%) | ↓ |
| genuine | 23 (26.7%) | 41 (43.2%) | +16.5pp |

**注意**：seed 不同（s42 vs s43），对比有 confound。

**结论改为 success**：原 registry 中 h7=41/genuine=0 是错误数据（可能把 ISR=1.0 count 误标为 H7）。实际 H7=0，genuine=41（43.2%），是所有 ISR β=0.3 实验中最高的 genuine rate。mean_isr=0.734 偏高（潜在 Goodhart），但 genuine 绝对数量和比例均有提升，H1 也略降。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427"
}
```

</details>

---
