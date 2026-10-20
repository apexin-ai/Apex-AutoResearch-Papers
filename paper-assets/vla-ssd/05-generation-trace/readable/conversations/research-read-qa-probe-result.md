# research read qa probe result

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_research_read_qa_probe_result_20260516T223757.jsonl`
- **Structured JSON:** [`38ab01d124f7d78a92eb.json`](../../sessions/38/38ab01d124f7d78a92eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-16T22:38:36.408324+00:00_

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
  "session": "worker_research_read_qa_probe_result_20260516T223757",
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

_source line 2 · 2026-05-16T22:38:36.408641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_read_qa_probe_result_20260516T223757",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T22:38:36.408820+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "\n# 1. 检查结果文件\necho \"=== FILE CHECK ===\"\nls -la /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json 2>/dev/null && echo \"FILE_EXISTS\" || echo \"NO_FILE\"\n\n# 2. 检查 tmux/进程\necho \"=== TMUX ===\"\ntmux ls 2>/dev/null | grep qa_probe\necho \"=== PROCESS ===\"\nps aux | grep qa_probe | grep -v grep\n\n# 3. 如果结果存在，读取完整内容\necho \"=== FULL RESULT ===\"\npython3 -c \"\nimport json\nwith open('/root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json') as f:\n    d = json.load(f)\n\n# Progress 4-class\nprint('=== PROGRESS (4-CLASS) ===')\nprog = d['tasks']['progress_4class']\nfor cond in ['dino_cls', 'projector']:\n    if cond in prog:\n        print(f'{cond}: acc={prog[cond][\\\"acc\\\"]:.4f}, f1={prog[cond][\\\"f1\\\"]:.4f}')\n\nfor model in ['trained', 'untrained']:\n    if model in prog:\n        print(f'{model}:')\n        for layer, vals in sorted(prog[model].items(), key=lambda x: int(x[0].replace(\\\"L\\\",\\\"\\\"))):\n            print(f'  {layer}: acc={vals[\\\"acc\\\"]:.4f}, f1={vals[\\\"f1\\\"]:.4f}')\n\n# Subtask binary\nprint()\nprint('=== SUBTASK (BINARY) ===')\nsub = d['tasks']['subtask_binary']\nfor cond in ['dino_cls', 'projector']:\n    if cond in sub:\n        print(f'{cond}: acc={sub[cond][\\\"acc\\\"]:.4f}, f1={sub[cond][\\\"f1\\\"]:.4f}')\n\nfor model in ['trained', 'untrained']:\n    if model in sub:\n        print(f'{model}:')\n        for layer, vals in sorted(sub[model].items(), key=lambda x: int(x[0].replace(\\\"L\\\",\\\"\\\"))):\n            print(f'  {layer}: acc={vals[\\\"acc\\\"]:.4f}, f1={vals[\\\"f1\\\"]:.4f}')\n\n# Summary\nprint()\nprint('=== SUMMARY ===')\ns = d.get('summary', {})\nfor k, v in s.items():\n    print(f'{k}: {v}')\n\" 2>/dev/null || echo \"PARSE_FAILED\"\n\n# 4. 如果文件不存在，查看 log\nif [ ! -f /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json ]; then\n    echo \"=== LOG ===\"\n    tail -30 ~/runs/vla-ssd/qa_probe_classification.log\nfi\n",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_read_qa_probe_result_20260516T223757",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "\n# 1. 检查结果文件\necho \"=== FILE CHECK ===\"\nls -la /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json 2>/dev/null && echo \"FILE_EXISTS\" || echo \"NO_FILE\"\n\n# 2. 检查 tmux/进程\necho \"=== TMUX ===\"\ntmux ls 2>/dev/null | grep qa_probe\necho \"=== PROCESS ===\"\nps aux | grep qa_probe | grep -v grep\n\n# 3. 如果结果存在，读取完整内容\necho \"=== FULL RESULT ===\"\npython3 -c \"\nimport json\nwith open('/root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json') as f:\n    d = json.load(f)\n\n# Progress 4-class\nprint('=== PROGRESS (4-CLASS) ===')\nprog = d['tasks']['progress_4class']\nfor cond in ['dino_cls', 'projector']:\n    if cond in prog:\n        print(f'{cond}: acc={prog[cond][\\\"acc\\\"]:.4f}, f1={prog[cond][\\\"f1\\\"]:.4f}')\n\nfor model in ['trained', 'untrained']:\n    if model in prog:\n        print(f'{model}:')\n        for layer, vals in sorted(prog[model].items(), key=lambda x: int(x[0].replace(\\\"L\\\",\\\"\\\"))):\n            print(f'  {layer}: acc={vals[\\\"acc\\\"]:.4f}, f1={vals[\\\"f1\\\"]:.4f}')\n\n# Subtask binary\nprint()\nprint('=== SUBTASK (BINARY) ===')\nsub = d['tasks']['subtask_binary']\nfor cond in ['dino_cls', 'projector']:\n    if cond in sub:\n        print(f'{cond}: acc={sub[cond][\\\"acc\\\"]:.4f}, f1={sub[cond][\\\"f1\\\"]:.4f}')\n\nfor model in ['trained', 'untrained']:\n    if model in sub:\n        print(f'{model}:')\n        for layer, vals in sorted(sub[model].items(), key=lambda x: int(x[0].replace(\\\"L\\\",\\\"\\\"))):\n            print(f'  {layer}: acc={vals[\\\"acc\\\"]:.4f}, f1={vals[\\\"f1\\\"]:.4f}')\n\n# Summary\nprint()\nprint('=== SUMMARY ===')\ns = d.get('summary', {})\nfor k, v in s.items():\n    print(f'{k}: {v}')\n\" 2>/dev/null || echo \"PARSE_FAILED\"\n\n# 4. 如果文件不存在，查看 log\nif [ ! -f /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json ]; then\n    echo \"=== LOG ===\"\n    tail -30 ~/runs/vla-ssd/qa_probe_classification.log\nfi\n",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T22:38:36.409081+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== FILE CHECK ===\\n-rw-r--r-- 1 root root 1548 May 17 06:01 /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json\\nFILE_EXISTS\\n=== TMUX ===\\nqa_probe_classification: 1 windows (created Sun May 17 06:02:45 2026)\\n=== PROCESS ===\\nroot     744972  0.0  0.0   6084  3792 ?        Ss   06:02   0:00 tmux new-session -d -s qa_probe_classification rm -f /tmp/agent-ml-exit/qa_probe_classification.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/vla-ssd/qa_probe_classification.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/qa_probe_classification.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/vla-ssd && export CUDA_VISIBLE_DEVICES=0 && timeout 7200 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/qa_probe_classification.py --condition all\\\"'; } > ~/runs/vla-ssd/qa_probe_classification.log 2>&1\\nroot     744973  0.0  0.0   4496  3460 pts/0    Ss+  06:02   0:00 bash -c rm -f /tmp/agent-ml-exit/qa_probe_classification.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/vla-ssd/qa_probe_classification.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/qa_probe_classification.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/vla-ssd && export CUDA_VISIBLE_DEVICES=0 && timeout 7200 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/qa_probe_classification.py --condition all\\\"'; } > ~/runs/vla-ssd/qa_probe_classification.log 2>&1\\nroot     744977  0.0  0.0   2800  1028 pts/0    S    06:02   0:00 timeout 7200 env bash -c bash -c \\\"source /roo
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_read_qa_probe_result_20260516T223757",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T22:38:36.409289+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "echo \"=== RAW JSON ===\" && cat /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json && echo && echo \"=== LOG TAIL ===\" && tail -50 ~/runs/vla-ssd/qa_probe_classification.log",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_read_qa_probe_result_20260516T223757",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "echo \"=== RAW JSON ===\" && cat /root/autodl-tmp/vla-ssd/results/qa_probe/classification_results.json && echo && echo \"=== LOG TAIL ===\" && tail -50 ~/runs/vla-ssd/qa_probe_classification.log",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T22:38:36.409519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== RAW JSON ===\\n{\\n  \\\"method\\\": \\\"Classification probe (LogisticRegression)\\\",\\n  \\\"tasks\\\": {\\n    \\\"progress_4class\\\": {\\n      \\\"trained\\\": {\\n        \\\"L0\\\": {\\n          \\\"acc\\\": 0.9474,\\n          \\\"f1\\\": 0.9476\\n        }\\n      },\\n      \\\"untrained\\\": {\\n        \\\"L0\\\": {\\n          \\\"acc\\\": 0.9474,\\n          \\\"f1\\\": 0.9476\\n        }\\n      },\\n      \\\"dino_cls\\\": {\\n        \\\"acc\\\": 0.9545,\\n        \\\"f1\\\": 0.9544\\n      },\\n      \\\"projector\\\": {\\n        \\\"acc\\\": 0.9474,\\n        \\\"f1\\\": 0.9476\\n      }\\n    },\\n    \\\"subtask_binary\\\": {\\n      \\\"trained\\\": {\\n        \\\"L0\\\": {\\n          \\\"acc\\\": 0.9829,\\n          \\\"f1\\\": 0.9829\\n        }\\n      },\\n      \\\"untrained\\\": {\\n        \\\"L0\\\": {\\n          \\\"acc\\\": 0.9829,\\n          \\\"f1\\\": 0.9829\\n        }\\n      },\\n      \\\"dino_cls\\\": {\\n        \\\"acc\\\": 0.9836,\\n        \\\"f1\\\": 0.9836\\n      },\\n      \\\"projector\\\": {\\n        \\\"acc\\\": 0.9829,\\n        \\\"f1\\\": 0.9829\\n      }\\n    }\\n  },\\n  \\\"summary\\\": {\\n    \\\"progress_best_trained\\\": {\\n      \\\"layer\\\": \\\"L0\\\",\\n      \\\"acc\\\": 0.9474,\\n      \\\"f1\\\": 0.9476\\n    },\\n    \\\"progress_best_untrained\\\": {\\n      \\\"layer\\\": \\\"L0\\\",\\n      \\\"acc\\\": 0.9474,\\n      \\\"f1\\\": 0.9476\\n    },\\n    \\\"progress_dino\\\": {\\n      \\\"acc\\\": 0.9545,\\n      \\\"f1\\\": 0.9544\\n    },\\n    \\\"progress_projector\\\": {\\n      \\\"acc\\\": 0.9474,\\n      \\\"f1\\\": 0.9476\\n    },\\n    \\\"subtask_best_trained\\\": {\\n      \\\"layer\\\": \\\"L0\\\",\\n      \\\"acc\\\": 0.9829,\\n      \\\"f1\\\": 0.9829\\n    },\\n    \\\"subtask_best_untrained\\\": {\\n      \\\"layer\\\": \\\"L0\\\",\\n      \\\"acc\\\": 0.9829,\\n      \\\"f1\\\": 0.9829\\n    },\\n    \\\"su
…[truncated 3685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_read_qa_probe_result_20260516T223757",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-16T22:38:36.409750+00:00_

完整结果如下。文件已写入，但进程仍在运行（可能在跑更多层，当前只有 L0）。

---

## QA Probe Classification Results

**Method**: Classification probe (LogisticRegression)

### Progress 4-class

| Condition | Acc | F1 |
|-----------|------|------|
| **trained L0** | 0.9474 | 0.9476 |
| **untrained L0** | 0.9474 | 0.9476 |
| **dino_cls** | 0.9545 | 0.9544 |
| **projector** | 0.9474 | 0.9476 |

### Subtask Binary

| Condition | Acc | F1 |
|-----------|------|------|
| **trained L0** | 0.9829 | 0.9829 |
| **untrained L0** | 0.9829 | 0.9829 |
| **dino_cls** | 0.9836 | 0.9836 |
| **projector** | 0.9829 | 0.9829 |

---

**状态**: 进程仍在运行（tmux session `qa_probe_classification` 活跃，python 进程占 CPU 3877%）。当前结果只有 L0 层，后续层正在计算中。Log 显示大量 LogisticRegression convergence warnings（lbfgs 达到 max_iter=1000 上限）。

**初步观察**（仅 L0，不下结论）：trained 与 untrained 在 L0 上数值完全相同，dino_cls 略高。需等全部层跑完再看趋势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_read_qa_probe_result_20260516T223757"
}
```

</details>

---
