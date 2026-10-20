# analysis exp 084 085 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_exp-084-085-status-check_20260519T230800.jsonl`
- **Structured JSON:** [`2e8376933b2954f54a92.json`](../../sessions/2e/2e8376933b2954f54a92.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-19T23:09:07.663035+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T23:09:07.663343+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T23:09:07.663501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ps aux | grep -E \"run_debate|run_contrastive\" | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ps aux | grep -E \"run_debate|run_contrastive\" | grep -v grep"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T23:09:07.663631+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T23:09:07.663753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "tmux ls 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "tmux ls 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T23:09:07.663890+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T23:09:07.664038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls -la /root/symb_invariant_consensus/results/exp084_debate_mistral_logiqa_seed123/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls -la /root/symb_invariant_consensus/results/exp084_debate_mistral_logiqa_seed123/"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T23:09:07.664159+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ls -la /root/symb_invariant_consensus/results/exp085_contrastive_mistral_logiqa_seed123/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ls -la /root/symb_invariant_consensus/results/exp085_contrastive_mistral_logiqa_seed123/"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T23:09:07.664271+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "ps aux | grep vllm | grep -v grep | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "ps aux | grep vllm | grep -v grep | head -5"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T23:09:07.664392+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 132\\ndrwxr-xr-x  3 root root    82 May 20 06:38 .\\ndrwxr-xr-x 51 root root  4096 May 20 06:37 ..\\n-rw-r--r--  1 root root 65336 May 20 07:07 dryrun.json\\ndrwxr-xr-x  2 root root  4096 May 20 07:07 intermediates\\n-rw-r--r--  1 root root 60164 May 20 07:07 results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T23:09:07.664513+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 248\\ndrwxr-xr-x  3 root root     82 May 20 06:39 .\\ndrwxr-xr-x 51 root root   4096 May 20 06:37 ..\\n-rw-r--r--  1 root root 121941 May 20 07:07 dryrun.json\\ndrwxr-xr-x  2 root root   4096 May 20 07:07 intermediates\\n-rw-r--r--  1 root root 122715 May 20 07:07 results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T23:09:07.664634+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T23:09:07.664765+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp084_debate_mistral_logiqa_seed123/results.json')); s=d.get('summary',{}); print(f'total={len(d.get(\\\"results\\\",[]))}, debate_acc={s.get(\\\"debate_accuracy\\\",\\\"N/A\\\")}, sc_acc={s.get(\\\"sc_accuracy\\\",\\\"N/A\\\")}, delta={s.get(\\\"delta\\\",\\\"N/A\\\")}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp084_debate_mistral_logiqa_seed123/results.json')); s=d.get('summary',{}); print(f'total={len(d.get(\\\"results\\\",[]))}, debate_acc={s.get(\\\"debate_accuracy\\\",\\\"N/A\\\")}, sc_acc={s.get(\\\"sc_accuracy\\\",\\\"N/A\\\")}, delta={s.get(\\\"delta\\\",\\\"N/A\\\")}')\""
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T23:09:07.664902+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T23:09:07.665034+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp085_contrastive_mistral_logiqa_seed123/results.json')); s=d.get('summary',{}); print(f'total={len(d.get(\\\"results\\\",[]))}, contrastive_acc={s.get(\\\"contrastive_accuracy\\\",\\\"N/A\\\")}, sc_acc={s.get(\\\"sc_accuracy\\\",\\\"N/A\\\")}, delta={s.get(\\\"delta\\\",\\\"N/A\\\")}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "python3 -c \"import json; d=json.load(open('/root/symb_invariant_consensus/results/exp085_contrastive_mistral_logiqa_seed123/results.json')); s=d.get('summary',{}); print(f'total={len(d.get(\\\"results\\\",[]))}, contrastive_acc={s.get(\\\"contrastive_accuracy\\\",\\\"N/A\\\")}, sc_acc={s.get(\\\"sc_accuracy\\\",\\\"N/A\\\")}, delta={s.get(\\\"delta\\\",\\\"N/A\\\")}')\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T23:09:07.665152+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T23:09:07.665290+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/exp084_debate_mistral_logiqa_seed123/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/exp084_debate_mistral_logiqa_seed123/results.json"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T23:09:07.665402+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/results/exp085_contrastive_mistral_logiqa_seed123/results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-25068",
    "command": "cat /root/symb_invariant_consensus/results/exp085_contrastive_mistral_logiqa_seed123/results.json"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T23:09:07.665740+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n\\\": 27,\\n    \\\"debate_accuracy\\\": 0.1852,\\n    \\\"sc_accuracy\\\": 0.4444,\\n    \\\"delta\\\": -0.2593,\\n    \\\"k\\\": 12,\\n    \\\"n_debates\\\": 4,\\n    \\\"temperature\\\": 0.7,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"seed\\\": 123,\\n    \\\"total_wall_time_s\\\": 1851.7,\\n    \\\"total_debate_constraints\\\": 448,\\n    \\\"fallback_count\\\": 1\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"logiqa_000\\\",\\n      \\\"problem\\\": \\\"Context: One seminar had 18 participants. It is known that :(1) At least 5 young teachers are female; (2) At least 6 female teachers are over middle age; (3) At least seven young women are teachers;\\\\n\\\\nQuestion: According to the above information, which of the following can be concluded about the participants?\\\\n\\\\nA. Some young teachers are not women\\\\nB. Some young women are not teachers\\\\nC. There are at least 11 young teachers\\\\nD. There are at least 13 female teachers\\\",\\n      \\\"dataset\\\": \\\"logiqa\\\",\\n      \\\"ground_truth\\\": \\\"D\\\",\\n      \\\"debate_answer\\\": \\\"D\\\",\\n      \\\"debate_correct\\\": true,\\n      \\\"sc_answer\\\": \\\"None of the above\\\",\\n      \\\"sc_correct\\\": false,\\n      \\\"candidates\\\": [\\n        \\\"A\\\",\\n        \\\"A (with a note of caution)\\\",\\n        \\\"B\\\",\\n        \\\"B. Some young women are not teachers\\\",\\n        \\\"C\\\",\\n        \\\"C \\\\\\\\ and \\\\\\\\ D\\\",\\n        \\\"D\\\",\\n        \\\"None of the above\\\"\\n      ],\\n      \\\"sc_vote_distribution\\\": {\\n        \\\"A\\\": 3,\\n        \\\"None of the above\\\": 5,\\n        \\\"D\\\": 2,\\n        \\\"A (with a note of caution)\\\": 1,\\n        \\\"B. Some young women are not teachers\\\": 1\\n      },\\n      \\\"debate_scores\\\": {\\n        \\\"A\\\": 0.0,\\n        \\\"A (with a no
…[truncated 7902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T23:09:07.666191+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n\\\": 52,\\n    \\\"contrastive_accuracy\\\": 0.5385,\\n    \\\"sc_accuracy\\\": 0.5,\\n    \\\"delta\\\": 0.0385,\\n    \\\"k\\\": 12,\\n    \\\"k_contrast\\\": 3,\\n    \\\"temperature\\\": 0.7,\\n    \\\"mode\\\": \\\"vllm\\\",\\n    \\\"seed\\\": 123,\\n    \\\"total_wall_time_s\\\": 1770.5,\\n    \\\"total_pro_constraints\\\": 213,\\n    \\\"total_con_constraints\\\": 275,\\n    \\\"degenerate_count\\\": 9\\n  },\\n  \\\"results\\\": [\\n    {\\n      \\\"problem_idx\\\": 0,\\n      \\\"problem_id\\\": \\\"logiqa_000\\\",\\n      \\\"problem\\\": \\\"Context: One seminar had 18 participants. It is known that :(1) At least 5 young teachers are female; (2) At least 6 female teachers are over middle age; (3) At least seven young women are teachers;\\\\n\\\\nQuestion: According to the above information, which of the following can be concluded about the participants?\\\\n\\\\nA. Some young teachers are not women\\\\nB. Some young women are not teachers\\\\nC. There are at least 11 young teachers\\\\nD. There are at least 13 female teachers\\\",\\n      \\\"dataset\\\": \\\"logiqa\\\",\\n      \\\"ground_truth\\\": \\\"D\\\",\\n      \\\"contrastive_answer\\\": \\\"C\\\",\\n      \\\"contrastive_correct\\\": false,\\n      \\\"sc_answer\\\": \\\"B\\\",\\n      \\\"sc_correct\\\": false,\\n      \\\"candidates\\\": [\\n        \\\"A\\\",\\n        \\\"B\\\",\\n        \\\"C\\\",\\n        \\\"D\\\"\\n      ],\\n      \\\"answer_counts\\\": {\\n        \\\"C\\\": 2,\\n        \\\"B\\\": 3,\\n        \\\"D\\\": 1,\\n        \\\"A\\\": 1\\n      },\\n      \\\"contrastive_scores\\\": {\\n        \\\"A\\\": 0.0,\\n        \\\"B\\\": 0.0,\\n        \\\"C\\\": 3.0,\\n        \\\"D\\\": 0.0\\n      },\\n      \\\"pro_constraints_count\\\": 4,\\n      \\\"con_constraints_count\\\": 1,\\n      \\\"per_candidate_details\\\": {\\n        \\\"A\\\": {\\n          \\\"score\\\": 0.0,\\n    
…[truncated 8114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T23:09:07.666422+00:00_

两个实验都已**完成**，CRON 误判。结果如下：

## exp-084 (Debate × LogiQA s123)

| 指标 | 值 |
|------|-----|
| n | 27 |
| debate_accuracy | **18.52%** |
| sc_accuracy | 44.44% |
| delta | **-25.93%** (debate 大幅劣于 SC) |
| wall_time | 1851.7s (~30.9 min) |
| fallback_count | 1 |

## exp-085 (Contrastive × LogiQA s123)

| 指标 | 值 |
|------|-----|
| n | 52 |
| contrastive_accuracy | **53.85%** |
| sc_accuracy | 50.00% |
| delta | **+3.85%** (contrastive 略优于 SC) |
| wall_time | 1770.5s (~29.5 min) |
| degenerate_count | 9 (17.3%) |

## 注意事项

1. **样本量异常**：exp-084 只跑了 27 题，exp-085 跑了 52 题，都远低于预期的 200 题。需要检查是 dry-run 模式还是数据集截断。
2. **exp-084 结果很差**：debate 准确率仅 18.52%，远低于 SC baseline 的 44.44%，delta=-25.93%。
3. **vLLM 状态**：因 ssh_read_only 不支持管道，未能检查 vLLM 进程；但两个实验都正常跑完并产出结果，说明 vLLM 在实验期间是正常的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp-084-085-status-check_20260519T230800"
}
```

</details>

---
