# eval 1 7b isr b01 eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_eval_1_7b-isr-b01-eval_20260516T221533.jsonl`
- **Structured JSON:** [`544008f7f306fcc02735.json`](../../sessions/54/544008f7f306fcc02735.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-16T22:18:26.688680+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T22:18:26.689055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T22:18:26.689238+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --help 2>&1 | head -40",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --help 2>&1 | head -40",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T22:18:26.689395+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: eval_sta.py [-h] --model_path MODEL_PATH --data_path DATA_PATH\\n                   --output_path OUTPUT_PATH [--logic_type {fol,prolog}]\\n                   [--solver SOLVER] [--max_new_tokens MAX_NEW_TOKENS]\\n                   [--timeout TIMEOUT] [--max_samples MAX_SAMPLES]\\n                   [--do_sample] [--temperature TEMPERATURE]\\n\\nFull STA evaluation of a checkpoint\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --model_path MODEL_PATH\\n  --data_path DATA_PATH\\n  --output_path OUTPUT_PATH\\n  --logic_type {fol,prolog}\\n                        Logic type: fol (Prover9) or prolog (swipl)\\n  --solver SOLVER       Solver name (default: auto based on logic_type)\\n  --max_new_tokens MAX_NEW_TOKENS\\n  --timeout TIMEOUT\\n  --max_samples MAX_SAMPLES\\n                        Max number of samples to evaluate (default: all)\\n  --do_sample           Use sampling instead of greedy decoding\\n  --temperature TEMPERATURE\\n                        Sampling temperature\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T22:18:26.689552+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --model_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42 --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --model_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42 --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T22:18:26.689723+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --model_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42 --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1'\\n\\nStdout:\\n\\n[21/100] id=folio_669 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[22/100] id=folio_393 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[23/100] id=folio_1331 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[24/100] id=folio_699 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[25/100] id=folio_529 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[26/100] id=folio_233 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[27/100] id=folio_1076 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[28/100] id=folio_14 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[29/100] id=folio_215 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[30/100] id=folio_1203 ... \\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T22:18:26.689923+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && tmux new-session -d -s eval_1.7b_isr_b01 \"CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --model_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42 --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1 | tee /tmp/eval_1.7b_isr_b01.log\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && tmux new-session -d -s eval_1.7b_isr_b01 \"CUDA_VISIBLE_DEVICES=0 python scripts/eval_sta.py --model_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42 --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1 | tee /tmp/eval_1.7b_isr_b01.log\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T22:18:26.690060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T22:18:26.690209+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "sleep 90 && tail -20 /tmp/eval_1.7b_isr_b01.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "sleep 90 && tail -20 /tmp/eval_1.7b_isr_b01.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T22:18:26.690333+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'sleep 90 && tail -20 /tmp/eval_1.7b_isr_b01.log'\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T22:18:26.690452+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -20 /tmp/eval_1.7b_isr_b01.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -20 /tmp/eval_1.7b_isr_b01.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T22:18:26.690584+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[28/100] id=folio_14 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[29/100] id=folio_215 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[30/100] id=folio_1203 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[31/100] id=folio_769 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[32/100] id=folio_491 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[33/100] id=folio_267 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[34/100] id=folio_574 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[35/100] id=folio_149 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[36/100] id=folio_1364 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[37/100] id=folio_1223 ... proved  ISR=0.600  gen=0.8s  eval=0.0s\\n[38/100] id=folio_1329 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[39/100] id=folio_953 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[40/100] id=folio_558 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[41/100] id=folio_1254 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[42/100] id=folio_924 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[43/100] id=folio_693 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[44/100] id=folio_1086 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[45/100] id=folio_960 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[46/100] id=folio_1371 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[47/100] id=folio_1323 ... \", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.01}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T22:18:26.690768+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "sleep 25 && tail -5 /tmp/eval_1.7b_isr_b01.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "sleep 25 && tail -5 /tmp/eval_1.7b_isr_b01.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T22:18:26.690906+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[82/100] id=folio_1289 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[83/100] id=folio_1051 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[84/100] id=folio_1381 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[85/100] id=folio_847 ... proved  ISR=0.600  gen=0.7s  eval=0.0s\\n[86/100] id=folio_832 ... \", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 25.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T22:18:26.691048+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "sleep 15 && tail -10 /tmp/eval_1.7b_isr_b01.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "sleep 15 && tail -10 /tmp/eval_1.7b_isr_b01.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T22:18:26.691169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Proved:       100/100 (100.0%)\\n  Mean ISR:     0.6000 +/- 0.0000\\n  Median ISR:   0.6000\\n  ISR/PR ratio: 0.6000\\n  Proved-only ISR: 0.6000\\n  By answer type:\\n    false: n=25, proved=25, ISR=0.6000\\n    unknown: n=41, proved=41, ISR=0.6000\\n    true: n=34, proved=34, ISR=0.6000\\n  Time: 76.3s (0.8s/sample)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 15.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T22:18:26.691329+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/classify_h7.py /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/classify_h7.py /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T22:18:26.691471+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"usage: classify_h7.py [-h] [--eval_path EVAL_PATH] [--batch BATCH [BATCH ...]]\\n                      [--out OUT] [--json_out JSON_OUT] [--scan]\\n                      [--scan_dirs SCAN_DIRS [SCAN_DIRS ...]]\\nclassify_h7.py: error: unrecognized arguments: /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json\\n\", \"stderr\": \"\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T22:18:26.691617+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/classify_h7.py --eval_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cd /root/solver-trace-ablation && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python scripts/classify_h7.py --eval_path /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T22:18:26.691796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\n  eval_results\\n============================================================\\nTotal samples: 100, Proved: 100\\nH7a (text-match tautology):                 0/100 = 0.0%\\nH7b (obfuscated tautology):                 0/100 = 0.0%\\nH7 total (H7a + H7b):                       0/100 = 0.0%\\nH1 strict  (multi-prem, concl in premises): 100/100 = 100.0%\\nH8 conj-collapse (concl = P1∧P2∧...):      0/100 = 0.0%\\nAny conclusion-in-premise (H7a+H1):         100/100 = 100.0%\\nContent-independent predicates:              100/100 = 100.0%\\nGenuine (proved - H7 - H1 - H8):           0/100 = 0.0%\\n---\\nH7 relaxed (single_premise + ISR>=0.5):     0/100 = 0.0%\\nSingle premise: 0/100 = 0.0%\\nISR = 1.0:      0/100 = 0.0%\\n\\n  H1 examples (first 3):\\n    folio_765: 2 premises, isr=0.6\\n    folio_1179: 2 premises, isr=0.6\\n    folio_66: 2 premises, isr=0.6\\n\\n\\n===================================================================================================================\\n  SUMMARY TABLE\\n===================================================================================================================\\nRun                                      Proved    H7a    H7b     H7     H1     H8  Genuine    Gen% CntIndep\\n-------------------------------------------------------------------------------------------------------------------\\neval_results                                100      0      0      0    100      0        0    0.0%      100\\n-------------------------------------------------------------------------------------------------------------------\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T22:18:26.692019+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('summary',d), indent=2))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42/eval_results.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('summary',d), indent=2))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T22:18:26.692186+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"n_problems\\\": 100,\\n  \\\"n_proved\\\": 100,\\n  \\\"prove_rate\\\": 1.0,\\n  \\\"mean_isr\\\": 0.6,\\n  \\\"isr_std\\\": 0.0,\\n  \\\"median_isr\\\": 0.6,\\n  \\\"isr_pr_ratio\\\": 0.6,\\n  \\\"proved_only_mean_isr\\\": 0.6,\\n  \\\"min_isr\\\": 0.6,\\n  \\\"max_isr\\\": 0.6,\\n  \\\"by_answer_type\\\": {\\n    \\\"false\\\": {\\n      \\\"count\\\": 25,\\n      \\\"proved\\\": 25,\\n      \\\"prove_rate\\\": 1.0,\\n      \\\"mean_isr\\\": 0.6\\n    },\\n    \\\"unknown\\\": {\\n      \\\"count\\\": 41,\\n      \\\"proved\\\": 41,\\n      \\\"prove_rate\\\": 1.0,\\n      \\\"mean_isr\\\": 0.6\\n    },\\n    \\\"true\\\": {\\n      \\\"count\\\": 34,\\n      \\\"proved\\\": 34,\\n      \\\"prove_rate\\\": 1.0,\\n      \\\"mean_isr\\\": 0.6\\n    }\\n  },\\n  \\\"elapsed_seconds\\\": 76.3,\\n  \\\"avg_time_per_sample\\\": 0.8,\\n  \\\"solver\\\": \\\"Prover9Solver\\\",\\n  \\\"logic_type\\\": \\\"fol\\\",\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/outputs/w2_1.7b_isr_b01_s42\\\"\\n}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T22:18:26.692366+00:00_

## 1.7B ISR β=0.1 Eval

- n_proved / n_problems: 100/100
- prove_rate: 100%
- mean_isr: 0.600 (σ=0.000)
- H7%: 0%
- H1%: 100%
- H8%: 0%
- Genuine%: **0.0%**

完全 H1 collapse：模型学会了每次都把结论放进 premises（2 premises, ISR=0.6 uniformly）。β=0.1 的 ISR reward 过弱，未能抑制 shortcut hacking，反而 100% 收敛到 conclusion-in-premise 策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_1_7b-isr-b01-eval_20260516T221533"
}
```

</details>

---
