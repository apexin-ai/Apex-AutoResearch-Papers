# analysis exp 033 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_analysis_exp-033-results_20260518T191648.jsonl`
- **Structured JSON:** [`e8426eaa727a5a5e92d0.json`](../../sessions/e8/e8426eaa727a5a5e92d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-18T19:20:25.967975+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T19:20:25.968323+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:20:25.968507+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T19:20:25.968640+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "tail -200 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "tail -200 /root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033.log"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:20:25.968763+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "tail -200 ~/runs/symb_invariant_consensus/exp-033.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "tail -200 ~/runs/symb_invariant_consensus/exp-033.log"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:20:25.969107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.5931372549019608,\\n    \\\"sc_accuracy\\\": 0.5441176470588235,\\n    \\\"sica_correct\\\": 121,\\n    \\\"sc_correct\\\": 111,\\n    \\\"extraction_rate\\\": 0.9714052287581699,\\n    \\\"total_constraints_extracted\\\": 14042,\\n    \\\"total_unique_constraints\\\": 8021,\\n    \\\"contradiction_rate\\\": 0.03503303827452936,\\n    \\\"problems_with_contradictions\\\": 128,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.5931372549019608,\\n        \\\"sc\\\": 0.5441176470588235,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 4881.8\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion
…[truncated 7762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T19:20:25.969302+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": "{'exp_id': 'exp-033'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "filters": "{'exp_id': 'exp-033'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T19:20:25.969546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 03:08:09,554 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:09,870 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:10,093 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:10,468 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:10,469 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:10,573 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:10,690 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:11,561 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:13,473 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:16,148 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:17,947 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:18,071 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:19,326 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:19,950 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:20,227 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:21,054 INFO HTTP Request: POST http://localhost:8000/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 03:08:22,395 INFO HTTP Request: POST http://localhost:8000/v1/chat/completion
…[truncated 6749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T19:20:25.969708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\nbash: line 1: python: command not found\\nEXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T19:20:25.969839+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2008}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T19:20:25.970028+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')); rs=d['results']; sats=[r['maxsat_stats']['satisfied']/max(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'],1) for r in rs]; print(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}'); print(f'avg_unique_constraints={sum(r[\\\"constraints_stats\\\"][\\\"unique_after_dedup\\\"] for r in rs)/len(rs):.1f}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')); rs=d['results']; sats=[r['maxsat_stats']['satisfied']/max(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'],1) for r in rs]; print(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}'); print(f'avg_unique_constraints={sum(r[\\\"constraints_stats\\\"][\\\"unique_after_dedup\\\"] for r in rs)/len(rs):.1f}')\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:20:25.970169+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T19:20:25.970293+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": "5",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "limit": "5",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T19:20:25.970547+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-042b-premise-formal\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:13:55.356Z\", \"updated_at\": \"2026-05-18T19:16:38.233Z\", \"hypothesis\": \"Premise-Only Formalization (重启): 绕过 CoT trace extraction，直接让 LLM 将 FOLIO premises + conclusion 形式化为 FOL，用 Z3 验证逻辑蕴含。K=12 独立 formalization + majority vote。如果 extraction quality 是 capability trap 的瓶颈，直接 formalization 应能产生更准确的约束，使 Premise-FOL > vanilla SICA。exp-042 因 vLLM 未启动失败，本次重启。\", \"parent\": \"exp-042-premise-formalization\", \"server\": \"westd-25068\", \"gpu\": \"cuda:2\", \"reproduce\": {\"server\": \"westd-25068\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-18T19:16:36.261Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && bash scripts/run_premise_formalization.sh 2 8002\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && bash scripts/run_premise_formalization.sh 2 8002\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:2\"], \"pid\": \"83150\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-042b-premise-formal.log\", \"submitted_at\": \"2026-05-18T19:16:37.520Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"83150\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-042b-premise-formal.log\"}, \"exp-045-backward-verification\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:01:40.541Z\", \"updated_at\": \"2026-05-18T19:16:34.740Z\", \"hypothesis\": \"Backward Verification: 翻转验证方向，对每个候选答案反向推理需要哪些 premises 成立/矛盾，用 Z3 检查哪个答案与 premises 最一致（矛盾最少）。如果 forward extraction 质量是瓶颈，backward verification 绕过 extraction 直接用 solver 判断一致性，可能打破 capability trap。\", \"server\": \"westd-25068\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"wes
…[truncated 7135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T19:20:25.970727+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": "{'status': 'QUEUED'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "filters": "{'status': 'QUEUED'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T19:20:25.970916+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-033\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:02:16.294Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2192}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T19:20:25.971086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json,sys; d=json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')); rs=d['results']; sats=[r['maxsat_stats']['satisfied']/(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded']) if (r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'])>0 else 0 for r in rs]; print(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}'); print(f'avg_unique={sum(r[chr(99)+chr(111)+chr(110)+chr(115)+chr(116)+chr(114)+chr(97)+chr(105)+chr(110)+chr(116)+chr(115)+chr(95)+chr(115)+chr(116)+chr(97)+chr(116)+chr(115)][chr(117)+chr(110)+chr(105)+chr(113)+chr(117)+chr(101)+chr(95)+chr(97)+chr(102)+chr(116)+chr(101)+chr(114)+chr(95)+chr(100)+chr(101)+chr(100)+chr(117)+chr(112)] for r in rs)/len(rs):.1f}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json,sys; d=json.load(open('/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json')); rs=d['results']; sats=[r['maxsat_stats']['satisfied']/(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded']) if (r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'])>0 else 0 for r in rs]; print(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}'); print(f'avg_unique={sum(r[chr(99)+chr(111)+chr(110)+chr(115)+chr(116)+chr(114)+chr(97)+chr(105)+chr(110)+chr(116)+chr(115)+chr(95)+chr(115)+chr(116)+chr(97)+chr(116)+chr(115)][chr(117)+chr(110)+chr(105)+chr(113)+chr(117)+chr(101)+chr(95)+chr(97)+chr(102)+chr(116)+chr(101)+chr(114)+chr(95)+chr(100)+chr(101)+chr(100)+chr(117)+chr(112)] for r in rs)/len(rs):.1f}')\""
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T19:20:25.971222+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T19:20:25.971369+00:00_

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
  "session": "worker_analysis_exp-033-results_20260518T191648",
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

_source line 20 · 2026-05-18T19:20:25.971497+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T19:20:25.971618+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nd=json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nrs=d['results']\nsats=[r['maxsat_stats']['satisfied']/(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded']) if (r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'])>0 else 0 for r in rs]\nuniq=[r['constraints_stats']['unique_after_dedup'] for r in rs]\nprint(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}')\nprint(f'avg_unique_constraints={sum(uniq)/len(uniq):.1f}')\n# SICA wins / SC wins / ties\nsica_only=sum(1 for r in rs if r['sica_correct'] and not r['sc_correct'])\nsc_only=sum(1 for r in rs if r['sc_correct'] and not r['sica_correct'])\nboth=sum(1 for r in rs if r['sica_correct'] and r['sc_correct'])\nneither=sum(1 for r in rs if not r['sica_correct'] and not r['sc_correct'])\nprint(f'sica_only_wins={sica_only}, sc_only_wins={sc_only}, both_correct={both}, neither={neither}')\n# non-unanimous SC rate (C0 proxy)\nnon_unan=sum(1 for r in rs if max(r['sc_vote_distribution'].values()) < r['sc_vote_count'])\nprint(f'c0_non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "cd /root/symb_invariant_consensus && python3 -c \"\nimport json\nd=json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nrs=d['results']\nsats=[r['maxsat_stats']['satisfied']/(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded']) if (r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'])>0 else 0 for r in rs]\nuniq=[r['constraints_stats']['unique_after_dedup'] for r in rs]\nprint(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}')\nprint(f'avg_unique_constraints={sum(uniq)/len(uniq):.1f}')\n# SICA wins / SC wins / ties\nsica_only=sum(1 for r in rs if r['sica_correct'] and not r['sc_correct'])\nsc_only=sum(1 for r in rs if r['sc_correct'] and not r['sica_correct'])\nboth=sum(1 for r in rs if r['sica_correct'] and r['sc_correct'])\nneither=sum(1 for r in rs if not r['sica_correct'] and not r['sc_correct'])\nprint(f'sica_only_wins={sica_only}, sc_only_wins={sc_only}, both_correct={both}, neither={neither}')\n# non-unanimous SC rate (C0 proxy)\nnon_unan=sum(1 for r in rs if max(r['sc_vote_distribution'].values()) < r['sc_vote_count'])\nprint(f'c0_non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T19:20:25.971776+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/symb_invariant_consensus && python3 -c \\\"\\\\nimport json\\\\nd=json.load(open(\\\\'results/exp033_mistral_7b_folio204/exp033_results.json\\\\'))\\\\nrs=d[\\\\'results\\\\']\\\\nsats=[r[\\\\'maxsat_stats\\\\'][\\\\'satisfied\\\\']/(r[\\\\'maxsat_stats\\\\'][\\\\'satisfied\\\\']+r[\\\\'maxsat_stats\\\\'][\\\\'excluded\\\\']) if (r[\\\\'maxsat_stats\\\\'][\\\\'satisfied\\\\']+r[\\\\'maxsat_stats\\\\'][\\\\'excluded\\\\'])>0 else 0 for r in rs]\\\\nuniq=[r[\\\\'constraints_stats\\\\'][\\\\'unique_after_dedup\\\\'] for r in rs]\\\\nprint(f\\\\'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}\\\\')\\\\nprint(f\\\\'avg_unique_constraints={sum(uniq)/len(uniq):.1f}\\\\')\\\\n# SICA wins / SC wins / ties\\\\nsica_only=sum(1 for r in rs if r[\\\\'sica_correct\\\\'] and not r[\\\\'sc_correct\\\\'])\\\\nsc_only=sum(1 for r in rs if r[\\\\'sc_correct\\\\'] and not r[\\\\'sica_correct\\\\'])\\\\nboth=sum(1 for r in rs if r[\\\\'sica_correct\\\\'] and r[\\\\'sc_correct\\\\'])\\\\nneither=sum(1 for r in rs if not r[\\\\'sica_correct\\\\'] and not r[\\\\'sc_correct\\\\'])\\\\nprint(f\\\\'sica_only_wins={sica_only}, sc_only_wins={sc_only}, both_correct={both}, neither={neither}\\\\')\\\\n# non-unanimous SC rate (C0 proxy)\\\\nnon_unan=sum(1 for r in rs if max(r[\\\\'sc_vote_distribution\\\\'].values()) < r[\\\\'sc_vote_count\\\\'])\\\\nprint(f\\\\'c0_non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T19:20:25.971949+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \"\nimport json\nd=json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nrs=d['results']\nsats=[r['maxsat_stats']['satisfied']/(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded']) if (r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'])>0 else 0 for r in rs]\nuniq=[r['constraints_stats']['unique_after_dedup'] for r in rs]\nprint(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}')\nprint(f'avg_unique_constraints={sum(uniq)/len(uniq):.1f}')\nsica_only=sum(1 for r in rs if r['sica_correct'] and not r['sc_correct'])\nsc_only=sum(1 for r in rs if r['sc_correct'] and not r['sica_correct'])\nboth=sum(1 for r in rs if r['sica_correct'] and r['sc_correct'])\nneither=sum(1 for r in rs if not r['sica_correct'] and not r['sc_correct'])\nprint(f'sica_only_wins={sica_only}, sc_only_wins={sc_only}, both_correct={both}, neither={neither}')\nnon_unan=sum(1 for r in rs if max(r['sc_vote_distribution'].values()) < r['sc_vote_count'])\nprint(f'c0_non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \"\nimport json\nd=json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nrs=d['results']\nsats=[r['maxsat_stats']['satisfied']/(r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded']) if (r['maxsat_stats']['satisfied']+r['maxsat_stats']['excluded'])>0 else 0 for r in rs]\nuniq=[r['constraints_stats']['unique_after_dedup'] for r in rs]\nprint(f'maxsat_mean_sat_ratio={sum(sats)/len(sats):.4f}')\nprint(f'avg_unique_constraints={sum(uniq)/len(uniq):.1f}')\nsica_only=sum(1 for r in rs if r['sica_correct'] and not r['sc_correct'])\nsc_only=sum(1 for r in rs if r['sc_correct'] and not r['sica_correct'])\nboth=sum(1 for r in rs if r['sica_correct'] and r['sc_correct'])\nneither=sum(1 for r in rs if not r['sica_correct'] and not r['sc_correct'])\nprint(f'sica_only_wins={sica_only}, sc_only_wins={sc_only}, both_correct={both}, neither={neither}')\nnon_unan=sum(1 for r in rs if max(r['sc_vote_distribution'].values()) < r['sc_vote_count'])\nprint(f'c0_non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T19:20:25.972093+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"maxsat_mean_sat_ratio=0.9609\\navg_unique_constraints=39.3\\nsica_only_wins=12, sc_only_wins=2, both_correct=109, neither=81\\nc0_non_unanimous=0/204 = 0.0000\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T19:20:25.972264+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \"\nimport json\nd=json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nrs=d['results']\nnon_unan=sum(1 for r in rs if len(r['sc_vote_distribution'])>1)\ntotal_traces=[sum(r['sc_vote_distribution'].values()) for r in rs]\nmaj_fracs=[max(r['sc_vote_distribution'].values())/sum(r['sc_vote_distribution'].values()) for r in rs]\nprint(f'non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}')\nprint(f'avg_total_votes={sum(total_traces)/len(total_traces):.1f}')\nprint(f'avg_majority_frac={sum(maj_fracs)/len(maj_fracs):.4f}')\nprint(f'c0_rate={non_unan/len(rs):.4f}')\nfrom scipy.stats import binom_test\nb=2\nc=12\np=binom_test(min(b,c), b+c, 0.5)\nprint(f'mcnemar: b(sc_only)={b}, c(sica_only)={c}, p={p:.4f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \"\nimport json\nd=json.load(open('results/exp033_mistral_7b_folio204/exp033_results.json'))\nrs=d['results']\nnon_unan=sum(1 for r in rs if len(r['sc_vote_distribution'])>1)\ntotal_traces=[sum(r['sc_vote_distribution'].values()) for r in rs]\nmaj_fracs=[max(r['sc_vote_distribution'].values())/sum(r['sc_vote_distribution'].values()) for r in rs]\nprint(f'non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}')\nprint(f'avg_total_votes={sum(total_traces)/len(total_traces):.1f}')\nprint(f'avg_majority_frac={sum(maj_fracs)/len(maj_fracs):.4f}')\nprint(f'c0_rate={non_unan/len(rs):.4f}')\nfrom scipy.stats import binom_test\nb=2\nc=12\np=binom_test(min(b,c), b+c, 0.5)\nprint(f'mcnemar: b(sc_only)={b}, c(sica_only)={c}, p={p:.4f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T19:20:25.972418+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python -c \\\"\\\\nimport json\\\\nd=json.load(open(\\\\'results/exp033_mistral_7b_folio204/exp033_results.json\\\\'))\\\\nrs=d[\\\\'results\\\\']\\\\nnon_unan=sum(1 for r in rs if len(r[\\\\'sc_vote_distribution\\\\'])>1)\\\\ntotal_traces=[sum(r[\\\\'sc_vote_distribution\\\\'].values()) for r in rs]\\\\nmaj_fracs=[max(r[\\\\'sc_vote_distribution\\\\'].values())/sum(r[\\\\'sc_vote_distribution\\\\'].values()) for r in rs]\\\\nprint(f\\\\'non_unanimous={non_unan}/{len(rs)} = {non_unan/len(rs):.4f}\\\\')\\\\nprint(f\\\\'avg_total_votes={sum(total_traces)/len(total_traces):.1f}\\\\')\\\\nprint(f\\\\'avg_majority_frac={sum(maj_fracs)/len(maj_fracs):.4f}\\\\')\\\\nprint(f\\\\'c0_rate={non_unan/len(rs):.4f}\\\\')\\\\nfrom scipy.stats import binom_test\\\\nb=2\\\\nc=12\\\\np=binom_test(min(b,c), b+c, 0.5)\\\\nprint(f\\\\'mcnemar: b(sc_only)={b}, c(sica_only)={c}, p={p:.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 1\\n\\nStdout:\\n\\nnon_unanimous=166/204 = 0.8137\\navg_total_votes=10.5\\navg_majority_frac=0.7515\\nc0_rate=0.8137\\n\\nStderr:\\n\\nError while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\nTraceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 12, in &lt;module>\\nImportError: cannot import name 'binom_test' from 'scipy.stats' (/root/miniconda3/lib/python3.12/site-packages/scipy/stats/__init__.py). Did you mean: 'binomtest'?\\n\\n\", \"metadata\": {\"elapsed_seconds\": 1.22}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T19:20:25.972616+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-25068",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom scipy.stats import binomtest\nr=binomtest(2, 14, 0.5)\nprint(f'mcnemar_p={r.pvalue:.6f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-25068",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom scipy.stats import binomtest\nr=binomtest(2, 14, 0.5)\nprint(f'mcnemar_p={r.pvalue:.6f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T19:20:25.972790+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"mcnemar_p=0.012939\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T19:20:25.973003+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "status",
  "value": "ALLOCATED",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "status",
    "value": "ALLOCATED",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T19:20:25.973181+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"ALLOCATED\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:19:15.613Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3343}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T19:20:25.973337+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "status",
  "value": "RUNNING",
  "project": "symb_invariant_consensus",
  "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\"', 'server': 'westd-25068', 'data_path': 'data/folio_full.json', 'data_count': 204, 'model_name': 'Mistral-7B-Instruct-v0.3', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "status",
    "value": "RUNNING",
    "project": "symb_invariant_consensus",
    "spec": "{'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\"', 'server': 'westd-25068', 'data_path': 'data/folio_full.json', 'data_count': 204, 'model_name': 'Mistral-7B-Instruct-v0.3', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T19:20:25.973516+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:19:25.429Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7539}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T19:20:25.973681+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "checkpoint_path",
  "value": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "checkpoint_path",
    "value": "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T19:20:25.973849+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:19:31.514Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37
…[truncated 6 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T19:20:25.974020+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "log_path",
  "value": "~/runs/symb_invariant_consensus/exp-033.log",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "log_path",
    "value": "~/runs/symb_invariant_consensus/exp-033.log",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T19:20:25.974238+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:19:32.383Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T19:20:25.974520+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "metrics",
  "value": "{'n_problems': 204, 'sica_accuracy': 59.31, 'sc_accuracy': 54.41, 'delta_pp': 4.9, 'sica_correct': 121, 'sc_correct': 111, 'mcnemar_discordant_b': 2, 'mcnemar_discordant_c': 12, 'mcnemar_p_value': 0.0129, 'c0_non_unanimous_rate': 0.8137, 'avg_majority_frac': 0.7515, 'extraction_rate': 97.14, 'contradiction_rate': 3.5, 'problems_with_contradictions': 128, 'avg_unique_constraints': 39.3, 'maxsat_mean_sat_ratio': 0.9609, 'total_constraints': 14042, 'unique_constraints': 8021, 'wall_time_min': 81.4, 'k': 12}",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "metrics",
    "value": "{'n_problems': 204, 'sica_accuracy': 59.31, 'sc_accuracy': 54.41, 'delta_pp': 4.9, 'sica_correct': 121, 'sc_correct': 111, 'mcnemar_discordant_b': 2, 'mcnemar_discordant_c': 12, 'mcnemar_p_value': 0.0129, 'c0_non_unanimous_rate': 0.8137, 'avg_majority_frac': 0.7515, 'extraction_rate': 97.14, 'contradiction_rate': 3.5, 'problems_with_contradictions': 128, 'avg_unique_constraints': 39.3, 'maxsat_mean_sat_ratio': 0.9609, 'total_constraints': 14042, 'unique_constraints': 8021, 'wall_time_min': 81.4, 'k': 12}",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T19:20:25.974841+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:19:41.246Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log
…[truncated 633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T19:20:25.975133+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "conclusion",
  "value": "success",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "conclusion",
    "value": "success",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T19:20:25.975412+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:19:45.260Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log
…[truncated 662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T19:20:25.975657+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "notes",
  "value": "Mistral-7B FOLIO-204: SICA 59.31% vs SC 54.41%, delta=+4.90pp (McNemar p=0.013, significant). 首次 SICA 显著超越 SC。关键因素：C0=81.37%（远高于 Qwen-7B 的 55%），高 diversity 使 SC majority vote 退化，而 SICA MaxSAT 仍能从 noisy traces 中提取信号。Discordant: SICA-only=12, SC-only=2, 高度不对称。但绝对准确率低（59% vs Qwen-7B 77%），说明 Mistral-7B 基础推理能力弱。结论：capability trap 非普遍现象，依赖 diversity/quality 平衡——高 diversity + 低 quality 时 SICA 有优势。",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "notes",
    "value": "Mistral-7B FOLIO-204: SICA 59.31% vs SC 54.41%, delta=+4.90pp (McNemar p=0.013, significant). 首次 SICA 显著超越 SC。关键因素：C0=81.37%（远高于 Qwen-7B 的 55%），高 diversity 使 SC majority vote 退化，而 SICA MaxSAT 仍能从 noisy traces 中提取信号。Discordant: SICA-only=12, SC-only=2, 高度不对称。但绝对准确率低（59% vs Qwen-7B 77%），说明 Mistral-7B 基础推理能力弱。结论：capability trap 非普遍现象，依赖 diversity/quality 平衡——高 diversity + 低 quality 时 SICA 有优势。",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T19:20:25.975954+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:20:01.816Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log
…[truncated 1072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T19:20:25.976189+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-033",
  "field": "status",
  "value": "DONE",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-033",
    "field": "status",
    "value": "DONE",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T19:20:25.976496+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-033\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:42:09.819Z\", \"updated_at\": \"2026-05-18T19:20:05.477Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3 --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8000 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp033.log 2>&1 & sleep 120 && python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8000/v1 --model auto --seed 42 --math-data data/empty.json --pw-data data/empty.json --folio-data data/folio_full.json --output results/exp033_mistral_7b_folio204/exp033_results.json --save-intermediates 2>&1 | tee results/exp033_mistral_7b_folio204/exp033.log\\\"\", \"server\": \"westd-25068\", \"gpu\": [\"cuda:0\"], \"pid\": \"65773\", \"log_path\": \"~/runs/symb_invariant_consensus/exp-033.log\", \"submitted_at\": \"2026-05-18T17:42:09.638Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Mistral-7B-Instruct-v0.3\", \"seed\": 42, \"wall_clock_seconds\": 5875.8, \"gpu_hours\": 1.63}, \"hypothesis\": \"Cross-family validation: Mistral-7B-Instruct-v0.3 在 FOLIO-204 全量上 SICA vs SC。验证 capability trap 跨模型家族在 full dataset 上是否持续（D012 pilot exp-010 已确认 delta=0, n=60）。\", \"reproduce\": {\"finished_at\": \"2026-05-18T19:02:16.294Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:02:18.863472+00:00\"}]}, \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/exp033_results.json\", \"log_pat
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-033-results_20260518T191648",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-18T19:20:25.976809+00:00_

Registry 已更新为 DONE/success。

---

## exp-033 分析报告：Mistral-7B-Instruct-v0.3 FOLIO-204

### 核心结果

| 指标 | 值 |
|------|-----|
| **SICA accuracy** | **59.31%** (121/204) |
| **SC accuracy** | **54.41%** (111/204) |
| **delta (SICA - SC)** | **+4.90pp** |
| **McNemar p-value** | **0.013** (显著, α=0.05) |
| n | 204 |
| k | 12 |

### 诊断指标

| 指标 | 值 |
|------|-----|
| extraction_rate | 97.14% |
| contradiction_rate | 3.50% (128/204 problems) |
| avg_unique_constraints | 39.3 |
| maxsat_mean_sat_ratio | 0.9609 |
| C0 (non-unanimous rate) | **81.37%** |
| avg_majority_frac | 0.7515 |
| Discordant: SICA-only wins | **12** |
| Discordant: SC-only wins | **2** |
| wall_time | 81.4 min |

### Baseline 对比

| 实验 | 模型 | 数据集 | SICA | SC | Delta | C0 |
|------|------|--------|------|-----|-------|-----|
| exp-026 | Qwen2.5-14B | FOLIO-204 | 74.51% | 75.00% | -0.49pp | ~45% |
| exp-035 | Qwen2.5-7B | FOLIO-204 | 76.85% | 77.34% | -0.49pp | 55.17% |
| exp-010-v3 | Mistral-7B | D012 (n=60) | 48.33% | 48.33% | 0pp | — |
| **exp-033** | **Mistral-7B** | **FOLIO-204** | **59.31%** | **54.41%** | **+4.90pp** | **81.37%** |

### 关键发现

1. **首次 SICA 显著超越 SC** — delta=+4.90pp, McNemar p=0.013, discordant pairs 高度不对称 (12:2)。

2. **Capability trap 非普遍现象** — Qwen 家族 (7B/14B) 上 delta≈-0.49pp (capability trap 成立)，但 Mistral-7B 上 SICA 反而大幅胜出。关键区别在于 **diversity**：
   - Mistral-7B C0=81.37%，Qwen-7B C0=55.17%
   - 高 diversity 导致 SC majority vote 退化（avg majority fraction 仅 75.15%）
   - SICA 的 MaxSAT 在 noisy 但 diverse 的 traces 中仍能提取有用信号

3. **绝对性能低** — Mistral-7B 59.31% 远低于 Qwen-7B 77%，说明基础推理能力弱，但 SICA 在这种条件下反而比 SC 更能容忍 noise。

4. **D012 pilot 有误导性** — n=60 的小样本掩盖了 +4.90pp 的效应。

5. **理论解释** — SICA 的优势区间是 "高 diversity + 中等 quality"：traces 足够多样使 SC 失效，但 constraint extraction 质量仍足以让 MaxSAT 找到一致解。Qwen 模型 diversity 不够高（SC 的 majority vote 仍然 robust），所以 SICA 无法胜出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp-033-results_20260518T191648"
}
```

</details>

---
