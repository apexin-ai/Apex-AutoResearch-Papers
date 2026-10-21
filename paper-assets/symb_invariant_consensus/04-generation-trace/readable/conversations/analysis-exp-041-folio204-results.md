# analysis exp 041 folio204 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_analysis_exp-041-folio204-results_20260518T202043.jsonl`
- **Structured JSON:** [`1b61a7ee8ccf2e116f47.json`](../../sessions/1b/1b61a7ee8ccf2e116f47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-18T20:23:40.726221+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__delete_cron,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T20:23:40.726606+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T20:23:40.726783+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp-041-14b-folio204-16639'}",
  "project": "symb_invariant_consensus",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp-041-14b-folio204-16639'}",
    "project": "symb_invariant_consensus",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T20:23:40.726977+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2954}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T20:23:40.727486+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "tail -80 /root/runs/symb_invariant_consensus/exp-041-14b-folio204-16639.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "tail -80 /root/runs/symb_invariant_consensus/exp-041-14b-folio204-16639.log"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T20:23:40.727681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls -la /root/symb_invariant_consensus/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls -la /root/symb_invariant_consensus/results/"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T20:23:40.727821+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/root/runs/symb_invariant_consensus/exp-041-14b-folio204-16639.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T20:23:40.728030+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x  7 root root 4096 May 19 01:50 .\\ndrwxr-xr-x 10 root root 4096 May 19 01:43 ..\\ndrwxr-xr-x  3 root root   81 May 19 01:46 exp032_qwen25_14b_pw600\\ndrwxr-xr-x  3 root root   81 May 19 01:48 exp033_qwen3_14b_pw600_nonthinking\\ndrwxr-xr-x  3 root root   81 May 19 01:48 exp036_qwen25_14b_folio204\\ndrwxr-xr-x  2 root root   10 May 19 01:43 exp037_mistral7b_folio204\\ndrwxr-xr-x  3 root root   81 May 19 01:51 exp038_qwen25_14b_logiqa200\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T20:23:40.728305+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root -name \"*exp041*\" -o -name \"*exp-041*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root -name \"*exp041*\" -o -name \"*exp-041*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T20:23:40.728449+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T20:23:40.728592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls -la /root/runs/symb_invariant_consensus/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls -la /root/runs/symb_invariant_consensus/"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T20:23:40.728719+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/runs/symb_invariant_consensus/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T20:23:40.728862+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root/symb_invariant_consensus/results/ -name \"*.json\" -newer /root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root/symb_invariant_consensus/results/ -name \"*.json\" -newer /root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T20:23:40.729126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-270_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-487_Q19.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-971_Q5.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-804_Q16.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-572_Q18.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-285_Q16.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNoneg-OWA-D5-686_Q18.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-735_Q9.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_RelNeg-OWA-D5-966_Q7.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-145_Q9.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-401_Q15.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-352_Q8.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-842_Q7.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNoneg-OWA-D5-296_Q13.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-203_Q21.json\\n/root/symb_invariant_consensus/results/exp032_qwen25_14b_pw600/intermediates/ProofWriter_AttNeg-OWA-D5-1119_Q6.json\\n/root/symb_invariant_consensus/results/exp032_qwe
…[truncated 6354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T20:23:40.729319+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root -maxdepth 3 -name \"*exp041*\" -o -name \"*exp-041*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root -maxdepth 3 -name \"*exp041*\" -o -name \"*exp-041*\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T20:23:40.729483+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T20:23:40.729623+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/.bash_history"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/.bash_history"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T20:23:40.729763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\nhf download google/gemma-3-27b-it --local-dir /root/autodl-tmp/models/gemma-3-27b-it > /tmp/dl_gemma.log 2>&1 &\\nhf download deepseek-ai/DeepSeek-R1-0528-Qwen3-8B --local-dir /root/autodl-tmp/models/deepseek-r1-0528-qwen3-8b > /tmp/dl_deepseek_r1_0528.log 2>&1 &\\nhf download microsoft/Phi-4-reasoning --local-dir /root/autodl-tmp/models/phi-4-reasoning > /tmp/dl_phi4.log 2>&1 &\\nhf download meta-llama/Llama-4-Scout-17B-16E-Instruct --local-dir /root/autodl-tmp/models/llama-4-scout > /tmp/dl_llama4.log 2>&1 &\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_ENDPOINT=https://hf-mirror.com\\nHF_ENDPOINT=https://hf-mirror.com hf download google/gemma-3-27b-it --local-dir /root/autodl-tmp/models/gemma-3-27b-it > /tmp/dl_gemma.log 2>&1 &\\nHF_ENDPOINT=https://hf-mirror.com hf download deepseek-ai/DeepSeek-R1-0528-Qwen3-8B --local-dir /root/autodl-tmp/models/deepseek-r1-0528-qwen3-8b > /tmp/dl_deepseek_r1_0528.log 2>&1 &\\nHF_ENDPOINT=https://hf-mirror.com hf download microsoft/Phi-4-reasoning --local-dir /root/autodl-tmp/models/phi-4-reasoning > /tmp/dl_phi4.log 2>&1 &\\nHF_ENDPOINT=https://hf-mirror.com hf download meta-llama/Llama-4-Scout-17B-16E-Instruct --local-dir /root/autodl-tmp/models/llama-4-scout > /tmp/dl_llama4.log 2>&1 &\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T20:23:40.729915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /root -maxdepth 2 -name \"*.log\" -newer /root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /root -maxdepth 2 -name \"*.log\" -newer /root/symb_invariant_consensus/results/exp038_qwen25_14b_logiqa200"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T20:23:40.730049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T20:23:40.730191+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "cat /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T20:23:40.730310+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp-041'}",
  "project": "symb_invariant_consensus",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp-041'}",
    "project": "symb_invariant_consensus",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T20:23:40.730675+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_problems\\\": 204,\\n    \\\"sica_accuracy\\\": 0.7549019607843137,\\n    \\\"sc_accuracy\\\": 0.7745098039215687,\\n    \\\"sica_correct\\\": 154,\\n    \\\"sc_correct\\\": 158,\\n    \\\"extraction_rate\\\": 0.9799836601307189,\\n    \\\"total_constraints_extracted\\\": 13588,\\n    \\\"total_unique_constraints\\\": 5999,\\n    \\\"contradiction_rate\\\": 0.009668278046341057,\\n    \\\"problems_with_contradictions\\\": 36,\\n    \\\"per_level_accuracy\\\": {\\n      \\\"validation\\\": {\\n        \\\"sica\\\": 0.7549019607843137,\\n        \\\"sc\\\": 0.7745098039215687,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"per_dataset_accuracy\\\": {\\n      \\\"folio\\\": {\\n        \\\"sica\\\": 0.7549019607843137,\\n        \\\"sc\\\": 0.7745098039215687,\\n        \\\"n\\\": 204\\n      }\\n    },\\n    \\\"k\\\": 12,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"total_wall_time_s\\\": 8413.4\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"folio_0\\\",\\n      \\\"problem\\\": \\\"Given the following premises:\\\\nIf people perform in school talent shows often, then they attend and are very engaged with school events. People either perform in school talent shows often or are inactive and disinterested members of their community. If people chaperone high school dances, then they are not students who attend the school. All people who are inactive and disinterested members of their community chaperone high school dances. All young children and teenagers who wish to further their academic careers and educational opportunities are students who attend the school. Bonnie either both attends and is very engaged with school events and is a student who attends the school, or she neither attends and is very engaged with school events nor is a student who attends the school.\\\\n\\\\nDetermine whether the following conclusion
…[truncated 7788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T20:23:40.730958+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2972}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T20:23:40.731192+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "stat /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "stat /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T20:23:40.731353+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  File: /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json\\n  Size: 294637    \\tBlocks: 576        IO Block: 4096   regular file\\nDevice: 34h/52d\\tInode: 13978747597  Links: 1\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\nAccess: 2026-05-19 04:08:05.458506048 +0800\\nModify: 2026-05-19 04:07:48.438405483 +0800\\nChange: 2026-05-19 04:07:48.438405483 +0800\\n Birth: 2026-05-19 01:48:34.169359827 +0800\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T20:23:40.731501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "ls -la /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "ls -la /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T20:23:40.731634+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 952\\ndrwxr-xr-x 3 root root     81 May 19 01:48 .\\ndrwxr-xr-x 7 root root   4096 May 19 01:50 ..\\n-rw-r--r-- 1 root root 656570 May 19 04:07 exp036.log\\ndrwxr-xr-x 2 root root   8192 May 19 04:07 intermediates\\n-rw-r--r-- 1 root root 294637 May 19 04:07 results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T20:23:40.731760+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "find /tmp -name \"*.log\" -maxdepth 1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "find /tmp -name \"*.log\" -maxdepth 1"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T20:23:40.731911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/vllm_exp038.log\\n/tmp/autodl.sh.log\\n/tmp/pip_install.log\\n/tmp/model_download.log\\n/tmp/pip_small.log\\n/tmp/dl_phi4.log\\n/tmp/model_download2.log\\n/tmp/pip_vllm.log\\n/tmp/dl_llama4.log\\n/tmp/model_download3.log\\n/tmp/model_download4.log\\n/tmp/model_ms.log\\n/tmp/model_hfmirror.log\\n/tmp/exp032_screen.log\\n/tmp/vllm_exp032.log\\n/tmp/vllm_test.log\\n/tmp/vllm_exp036.log\\n/tmp/model_hf2.log\\n/tmp/dl_gemma.log\\n/tmp/vllm_exp037.log\\n/tmp/model_noxet.log\\n/tmp/dl_deepseek_r1_0528.log\\n/tmp/wget_model.log\\n/tmp/prep_strategyqa.log\\n/tmp/vllm_exp034.log\\n/tmp/vllm_exp033.log\\n/tmp/dl_mistral_redownload.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T20:23:40.732047+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T20:23:40.732303+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-045b-backward-verify\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:16:45.453Z\", \"updated_at\": \"2026-05-18T20:17:48.323Z\", \"hypothesis\": \"Backward Verification v2 (正确模型 Qwen2.5-14B): 翻转验证方向，对每个候选答案反向推理 premises，用 Z3 检查一致性。v1 使用错误模型 (Qwen-7B) 得到 -21pp，需确认 Qwen-14B 上是否仍为强 negative（预期是，因为根因是 FOL quality 而非 model capacity）。\", \"server\": \"westd-25068\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"westd-25068\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-18T20:17:45.787Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && mkdir -p results/exp045b_backward_qwen14b && CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8003 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp045b.log 2>&1 & sleep 120 && python -u backward_verification.py --api-base http://localhost:8003/v1 --model auto --k 12 --data data/folio_full.json --output results/exp045b_backward_qwen14b/results.json --seed 42 --temperature 0.7 2>&1 | tee results/exp045b_backward_qwen14b/exp045b.log\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && mkdir -p results/exp045b_backward_qwen14b && CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/models/Qwen2.5-14B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.90 --port 8003 --dtype auto --trust-remote-code --enforce-eager > /tmp/vllm_exp045b.log 2>&1 & sleep 120 && python -u backward_verification.py --api-base http://localhost:8003/v1 --model auto --k 12 --data data/folio_full.json --output results/exp045b_backwa
…[truncated 7700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T20:23:40.732499+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "symb_invariant_consensus",
  "limit": "50",
  "fields": "['status', 'conclusion', 'server', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "limit": "50",
    "fields": "['status', 'conclusion', 'server', 'hypothesis']"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T20:23:40.732632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "tail -30 /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/exp036.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "tail -30 /root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/exp036.log"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T20:23:40.732992+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-038-14b-logiqa200-16639\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 LogiQA 2.0 (200题) 上 SICA vs SC：跨数据集验证 capability trap。LogiQA 是多选逻辑推理（非二元分类），constraint extraction 和 Z3 formalization 需要适配不同推理类型。\", \"conclusion\": \"negative\"}, \"exp-045b-backward-verify\": {\"status\": \"RUNNING\", \"hypothesis\": \"Backward Verification v2 (正确模型 Qwen2.5-14B): 翻转验证方向，对每个候选答案反向推理 premises，用 Z3 检查一致性。v1 使用错误模型 (Qwen-7B) 得到 -21pp，需确认 Qwen-14B 上是否仍为强 negative（预期是，因为根因是 FOL quality 而非 model capacity）。\", \"server\": \"westd-25068\"}, \"exp-046-mistral-pw600\": {\"status\": \"RUNNING\", \"hypothesis\": \"Mistral-7B-Instruct-v0.3 在 ProofWriter-600 上 SICA vs SC：验证 regime boundary 跨域泛化。exp-033 (Mistral FOLIO-204) 显示 +4.90pp (p=0.013)，如果 PW-600 也显示正向 delta，则 regime-dependent capability trap 不是 FOLIO-specific artifact。\", \"server\": \"westd-25068\"}, \"exp-044b-icl-oracle\": {\"status\": \"RUNNING\", \"hypothesis\": \"ICL with Oracle Examples (v2, 正确模型 Qwen2.5-14B): 用 5 个 gold FOL annotations 作为 few-shot examples 教 LLM 提取高质量约束。如果 extraction quality 是 capability trap 瓶颈，oracle-guided extraction 应能产生更 discriminative 的约束，使 ICL-SICA > vanilla SICA (74.51%)。评测 199 题。v1 因使用错误模型 (Mistral-7B) 被 kill。\", \"server\": \"westd-25068\"}, \"exp-041-14b-folio204-16639\": {\"status\": \"DONE\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"conclusion\": \"failed\"}, \"exp-045-backward-verification\": {\"status\": \"ANALYZING\", \"hypothesis\": \"Backward Verification: 翻转验证方向，对每个候选答案反向推理需要哪些 premises 成立/矛盾，用 Z3 检查哪个答案与 premises 最一致（矛盾最少）。如果 forward extraction 质量是瓶颈，backward verification 绕过 extraction 直接用 solver 判断一致性，可能打破 capability trap。\", \"server\": \"westd-25068\", \"conclusion\": \"killed\"}, \"exp-042b-premise-formal\": {\"status\": \"DONE\", \"hypothesis\": \"Premise-Only Formalization (重启): 绕过 CoT trace extra
…[truncated 13167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T20:23:40.733199+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-19 04:07:45,212 INFO HTTP Request: POST http://localhost:8002/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 04:07:48,151 INFO HTTP Request: POST http://localhost:8002/v1/chat/completions \\\"HTTP/1.1 200 OK\\\"\\n2026-05-19 04:07:48,428 INFO Scorer mode=NORMAL  satisfied_ratio=1.000 (25/25)  alpha=0.50  threshold=0.20\\nSICA: True (X)\\n  Constraints: 60 extracted -> 25 unique\\n  MaxSAT: 25 sat, 0 excl, solve=0.7250048220157623ms\\n  Timing: trace=8.2s extract=24.6s total=33.1s\\nSC:   True (X) -- votes: 12/12\\nTime: 33.1s\\n\\n================================================================================\\nFULL MVP EXPERIMENT RESULTS\\n================================================================================\\nProblems: 204\\nSICA accuracy: 75.5% (154/204)\\nSC accuracy:   77.5% (158/204)\\nExtraction rate: 98.0%\\nContradiction rate: 1.0%\\nProblems with contradictions: 36/204\\n\\n--- By Dataset ---\\n  folio       : SICA=75.5%  SC=77.5%  (n=204)\\n\\n--- By Level ---\\n  Level validation: SICA=75.5%  SC=77.5%  (n=204)\\n================================================================================\\n\\nTotal wall time: 140.2 min\\nResults saved to results/exp036_qwen25_14b_folio204/results.json\\nFULL_MVP_DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T20:23:40.733393+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-16639",
  "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json') as f:\n    data = json.load(f)\nresults = data['results']\na = sum(1 for r in results if r['sica_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['sica_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['sica_correct'] and r['sc_correct'])\nd = sum(1 for r in results if not r['sica_correct'] and not r['sc_correct'])\nn = len(results)\nprint(f'n={n}, both_correct={a}, sica_only={b}, sc_only={c}, both_wrong={d}')\nprint(f'SICA={a+b}/{n}={100*(a+b)/n:.2f}%, SC={a+c}/{n}={100*(a+c)/n:.2f}%')\nprint(f'delta={100*(a+b)/n - 100*(a+c)/n:.2f}pp')\ndisc = b + c\nif disc > 0:\n    chi2 = (b - c)**2 / (b + c)\n    from math import exp, sqrt, pi, erfc\n    p = erfc(sqrt(chi2/2)) if chi2 > 0 else 1.0\n    print(f'McNemar chi2={chi2:.4f}, p={p:.4f}')\nelse:\n    print('No discordant pairs')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-16639",
    "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json') as f:\n    data = json.load(f)\nresults = data['results']\na = sum(1 for r in results if r['sica_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['sica_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['sica_correct'] and r['sc_correct'])\nd = sum(1 for r in results if not r['sica_correct'] and not r['sc_correct'])\nn = len(results)\nprint(f'n={n}, both_correct={a}, sica_only={b}, sc_only={c}, both_wrong={d}')\nprint(f'SICA={a+b}/{n}={100*(a+b)/n:.2f}%, SC={a+c}/{n}={100*(a+c)/n:.2f}%')\nprint(f'delta={100*(a+b)/n - 100*(a+c)/n:.2f}pp')\ndisc = b + c\nif disc > 0:\n    chi2 = (b - c)**2 / (b + c)\n    from math import exp, sqrt, pi, erfc\n    p = erfc(sqrt(chi2/2)) if chi2 > 0 else 1.0\n    print(f'McNemar chi2={chi2:.4f}, p={p:.4f}')\nelse:\n    print('No discordant pairs')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T20:23:40.733544+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T20:23:40.733689+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-16639",
  "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json') as f:\n    data = json.load(f)\nresults = data['results']\na = sum(1 for r in results if r['sica_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['sica_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['sica_correct'] and r['sc_correct'])\nd = sum(1 for r in results if not r['sica_correct'] and not r['sc_correct'])\nn = len(results)\nprint(f'n={n}, both_correct={a}, sica_only={b}, sc_only={c}, both_wrong={d}')\nprint(f'SICA={a+b}/{n}={100*(a+b)/n:.2f}%, SC={a+c}/{n}={100*(a+c)/n:.2f}%')\nprint(f'delta={100*(a+b)/n - 100*(a+c)/n:.2f}pp')\ndisc = b + c\nif disc > 0:\n    chi2 = (b - c)**2 / (b + c)\n    from math import erfc, sqrt\n    p = erfc(sqrt(chi2/2)) if chi2 > 0 else 1.0\n    print(f'McNemar chi2={chi2:.4f}, p={p:.4f}')\n    print(f'extraction_rate={data[\\\"summary\\\"][\\\"extraction_rate\\\"]:.4f}')\n    print(f'contradiction_rate={data[\\\"summary\\\"][\\\"contradiction_rate\\\"]:.4f}')\nelse:\n    print('No discordant pairs')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-16639",
    "command": "python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json') as f:\n    data = json.load(f)\nresults = data['results']\na = sum(1 for r in results if r['sica_correct'] and r['sc_correct'])\nb = sum(1 for r in results if r['sica_correct'] and not r['sc_correct'])\nc = sum(1 for r in results if not r['sica_correct'] and r['sc_correct'])\nd = sum(1 for r in results if not r['sica_correct'] and not r['sc_correct'])\nn = len(results)\nprint(f'n={n}, both_correct={a}, sica_only={b}, sc_only={c}, both_wrong={d}')\nprint(f'SICA={a+b}/{n}={100*(a+b)/n:.2f}%, SC={a+c}/{n}={100*(a+c)/n:.2f}%')\nprint(f'delta={100*(a+b)/n - 100*(a+c)/n:.2f}pp')\ndisc = b + c\nif disc > 0:\n    chi2 = (b - c)**2 / (b + c)\n    from math import erfc, sqrt\n    p = erfc(sqrt(chi2/2)) if chi2 > 0 else 1.0\n    print(f'McNemar chi2={chi2:.4f}, p={p:.4f}')\n    print(f'extraction_rate={data[\\\"summary\\\"][\\\"extraction_rate\\\"]:.4f}')\n    print(f'contradiction_rate={data[\\\"summary\\\"][\\\"contradiction_rate\\\"]:.4f}')\nelse:\n    print('No discordant pairs')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T20:23:40.733827+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"n=204, both_correct=154, sica_only=0, sc_only=4, both_wrong=46\\nSICA=154/204=75.49%, SC=158/204=77.45%\\ndelta=-1.96pp\\nMcNemar chi2=4.0000, p=0.0455\\nextraction_rate=0.9800\\ncontradiction_rate=0.0097\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T20:23:40.734018+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-041-14b-folio204-16639",
  "field": "conclusion",
  "value": "negative",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-041-14b-folio204-16639",
    "field": "conclusion",
    "value": "negative",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T20:23:40.734178+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-041-14b-folio204-16639\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:01:33.016Z\", \"updated_at\": \"2026-05-18T20:23:21.892Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"spec\": {\"command\": \"run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8002/v1 --model auto --seed 42 --pw-data data/empty.json --folio-data data/folio_full.json --math-data data/empty.json\", \"server\": \"westd-16639\", \"data_path\": \"/root/symb_invariant_consensus/data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen2.5-14B-Instruct (cached)\", \"eval_data\": \"FOLIO-204\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T20:15:00.713Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T20:15:02.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:15:05.317649+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5919}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T20:23:40.734332+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-041-14b-folio204-16639",
  "field": "metrics",
  "value": "{'n': 204, 'sica_accuracy': 0.7549, 'sc_accuracy': 0.7745, 'sica_correct': 154, 'sc_correct': 158, 'delta_pp': -1.96, 'mcnemar_chi2': 4, 'mcnemar_p': 0.0455, 'extraction_rate': 0.98, 'contradiction_rate': 0.0097, 'discordant_sica_only': 0, 'discordant_sc_only': 4, 'both_correct': 154, 'both_wrong': 46, 'wall_time_min': 140.2}",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-041-14b-folio204-16639",
    "field": "metrics",
    "value": "{'n': 204, 'sica_accuracy': 0.7549, 'sc_accuracy': 0.7745, 'sica_correct': 154, 'sc_correct': 158, 'delta_pp': -1.96, 'mcnemar_chi2': 4, 'mcnemar_p': 0.0455, 'extraction_rate': 0.98, 'contradiction_rate': 0.0097, 'discordant_sica_only': 0, 'discordant_sc_only': 4, 'both_correct': 154, 'both_wrong': 46, 'wall_time_min': 140.2}",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T20:23:40.734658+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-041-14b-folio204-16639\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:01:33.016Z\", \"updated_at\": \"2026-05-18T20:23:23.996Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"spec\": {\"command\": \"run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8002/v1 --model auto --seed 42 --pw-data data/empty.json --folio-data data/folio_full.json --math-data data/empty.json\", \"server\": \"westd-16639\", \"data_path\": \"/root/symb_invariant_consensus/data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen2.5-14B-Instruct (cached)\", \"eval_data\": \"FOLIO-204\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T20:15:00.713Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T20:15:02.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:15:05.317649+00:00\"}]}, \"metrics\": {\"n\": 204, \"sica_accuracy\": 0.7549, \"sc_accuracy\": 0.7745, \"sica_correct\": 154, \"sc_correct\": 158, \"delta_pp\": -1.96, \"mcnemar_chi2\": 4, \"mcnemar_p\": 0.0455, \"extraction_rate\": 0.98, \"contradiction_rate\": 0.0097, \"discordant_sica_only\": 0, \"discordant_sc_only\": 4, \"both_correct\": 154, \"both_wrong\": 46, \"wall_time_min\": 140.2}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.397}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T20:23:40.734978+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-041-14b-folio204-16639",
  "field": "log_path",
  "value": "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/exp036.log",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-041-14b-folio204-16639",
    "field": "log_path",
    "value": "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/exp036.log",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T20:23:40.735237+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-041-14b-folio204-16639\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:01:33.016Z\", \"updated_at\": \"2026-05-18T20:23:29.636Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"spec\": {\"command\": \"run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8002/v1 --model auto --seed 42 --pw-data data/empty.json --folio-data data/folio_full.json --math-data data/empty.json\", \"server\": \"westd-16639\", \"data_path\": \"/root/symb_invariant_consensus/data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen2.5-14B-Instruct (cached)\", \"eval_data\": \"FOLIO-204\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T20:15:00.713Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T20:15:02.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:15:05.317649+00:00\"}]}, \"metrics\": {\"n\": 204, \"sica_accuracy\": 0.7549, \"sc_accuracy\": 0.7745, \"sica_correct\": 154, \"sc_correct\": 158, \"delta_pp\": -1.96, \"mcnemar_chi2\": 4, \"mcnemar_p\": 0.0455, \"extraction_rate\": 0.98, \"contradiction_rate\": 0.0097, \"discordant_sica_only\": 0, \"discordant_sc_only\": 4, \"both_correct\": 154, \"both_wrong\": 46, \"wall_time_min\": 140.2}, \"log_path\": \"/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/exp036.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4802}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T20:23:40.735394+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp-041-14b-folio204-16639",
  "field": "checkpoint_path",
  "value": "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp-041-14b-folio204-16639",
    "field": "checkpoint_path",
    "value": "/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json",
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T20:23:40.735520+00:00_

called mcp__agent-ml-research__delete_cron

<details open><summary>🔧 Tool call — mcp__agent-ml-research__delete_cron</summary>

```json
{
  "exp_id": "exp-041-14b-folio204-16639"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__delete_cron",
  "tool_args": {
    "exp_id": "exp-041-14b-folio204-16639"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T20:23:40.735677+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp-041-14b-folio204-16639\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:01:33.016Z\", \"updated_at\": \"2026-05-18T20:23:30.526Z\", \"hypothesis\": \"Qwen2.5-14B-Instruct 在 FOLIO-204 上 SICA vs SC（westd-16639 独立重跑）：在不同服务器上复现 exp-001/026 结果，验证 capability trap 的可复现性和排除服务器环境差异。\", \"spec\": {\"command\": \"run_full_mvp.py --mode vllm --k 12 --temperature 0.7 --max-tokens 4096 --api-base http://localhost:8002/v1 --model auto --seed 42 --pw-data data/empty.json --folio-data data/folio_full.json --math-data data/empty.json\", \"server\": \"westd-16639\", \"data_path\": \"/root/symb_invariant_consensus/data/folio_full.json\", \"data_count\": 204, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen2.5-14B-Instruct (cached)\", \"eval_data\": \"FOLIO-204\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T20:15:00.713Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T20:15:02.129Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:15:05.317649+00:00\"}]}, \"metrics\": {\"n\": 204, \"sica_accuracy\": 0.7549, \"sc_accuracy\": 0.7745, \"sica_correct\": 154, \"sc_correct\": 158, \"delta_pp\": -1.96, \"mcnemar_chi2\": 4, \"mcnemar_p\": 0.0455, \"extraction_rate\": 0.98, \"contradiction_rate\": 0.0097, \"discordant_sica_only\": 0, \"discordant_sc_only\": 4, \"both_correct\": 154, \"both_wrong\": 46, \"wall_time_min\": 140.2}, \"log_path\": \"/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/exp036.log\", \"checkpoint_path\": \"/root/symb_invariant_consensus/results/exp036_qwen25_14b_folio204/results.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4127}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T20:23:40.735831+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No cron found for 'exp-041-14b-folio204-16639'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043",
  "tool": "mcp__agent-ml-research__delete_cron",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-18T20:23:40.736022+00:00_

Registry updated, cron already cleared.

## exp-041 结果

实验实际完成，结果存于 `exp036_qwen25_14b_folio204/` 目录（之前被 auto-monitor 误判为 failed）。

| 指标 | exp-041 (westd-16639) | exp-026 (westd-25068) |
|---|---|---|
| SICA | 75.49% (154/204) | 74.51% |
| SC | 77.45% (158/204) | 75.00% |
| delta | **-1.96pp** | -0.49pp |
| McNemar p | **0.0455** (显著) | — |
| extraction_rate | 0.9800 | — |
| contradiction_rate | 0.0097 | — |
| discordant | sica_only=0, sc_only=4 | — |

**结论：negative。** Capability trap 方向一致（SC > SICA），且在 westd-16639 上 delta 更大、McNemar 达到显著（p=0.0455）。SC baseline 更高 (+2.45pp)，说明不同服务器环境存在 variance，但 SICA 始终未能超越 SC。不支持可复现性中的"数值一致"，但支持"结论一致"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp-041-folio204-results_20260518T202043"
}
```

</details>

---
