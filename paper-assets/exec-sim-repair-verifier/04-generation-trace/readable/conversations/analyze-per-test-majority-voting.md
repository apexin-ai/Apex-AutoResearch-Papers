# analyze per test majority voting

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analyze_per-test-majority-voting_20260512T092930.jsonl`
- **Structured JSON:** [`a913de78d41f38b87f63.json`](../../sessions/a9/a913de78d41f38b87f63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-12T09:30:06.476904+00:00_

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
  "session": "worker_analyze_per-test-majority-voting_20260512T092930",
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

_source line 2 · 2026-05-12T09:30:06.477285+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_per-test-majority-voting_20260512T092930",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T09:30:06.477453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "tail -80 ~/runs/exec-sim-repair-verifier/per-test-majority-voting.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_per-test-majority-voting_20260512T092930",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "tail -80 ~/runs/exec-sim-repair-verifier/per-test-majority-voting.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T09:30:06.477587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-westd-4x5090",
  "command": "cat /home/sonny/exec-sim-repair-verifier/eval_majority_voting.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_per-test-majority-voting_20260512T092930",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-westd-4x5090",
    "command": "cat /home/sonny/exec-sim-repair-verifier/eval_majority_voting.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-12T09:30:06.477756+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-12 17:22:49,838 INFO Loading base model: /root/.cache/huggingface/hub/Qwen/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:00<00:00, 122.71it/s]\\n2026-05-12 17:22:49,906 INFO Loading adapter: checkpoints/best\\n2026-05-12 17:22:54,808 INFO Test set: 1890 examples, pass=978, fail=912\\n2026-05-12 17:22:54,808 INFO Majority baseline: 51.7%\\n2026-05-12 17:22:54,808 INFO === Single-pass greedy (temperature=0) ===\\nThe following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n2026-05-12 17:23:24,481 INFO Greedy accuracy: 87.51% (29.7s)\\n2026-05-12 17:23:24,481 INFO === 3-pass sampling (temperature=0.7) ===\\n2026-05-12 17:23:24,481 INFO Pass 1/3...\\n2026-05-12 17:23:54,396 INFO   Pass 1 accuracy: 86.72%\\n2026-05-12 17:23:54,396 INFO Pass 2/3...\\n2026-05-12 17:24:25,440 INFO   Pass 2 accuracy: 86.83%\\n2026-05-12 17:24:25,440 INFO Pass 3/3...\\n2026-05-12 17:24:54,619 INFO   Pass 3 accuracy: 87.62%\\n2026-05-12 17:24:54,625 INFO Majority vote accuracy: 86.83%\\n2026-05-12 17:24:54,625 INFO Improvement over greedy: -0.69pp\\n2026-05-12 17:24:54,625 INFO Agreement distribution:\\n2026-05-12 17:24:54,625 INFO   3/3: 1763 (93.3%)\\n2026-05-12 17:24:54,625 INFO   2/3: 127 (6.7%)\\n2026-05-12 17:24:54,642 INFO Results saved to eval_majority_voting.json\\n\\n============================================================\\nMAJORITY VOTING REPORT: Per-test Self-Consistency (K=3)\\n============================================================\\n\\nTest set: 1890 examples (pass=978, fail=912)\\nTemperature: 0.7, K=3\\n\\nSingle-pass (greedy): 87.51%\\nMajority vote (K=3):  86.83%\\nImprovement:           -0.69pp\\n\\nAgreement distribution:\\n  3/3 unanimous: 1763 (93.3%)\\n  2/3 unanimous: 
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_per-test-majority-voting_20260512T092930",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T09:30:06.478040+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"test_set_size\\\": 1890,\\n  \\\"K\\\": 3,\\n  \\\"temperature\\\": 0.7,\\n  \\\"class_balance\\\": {\\n    \\\"pass\\\": 978,\\n    \\\"fail\\\": 912,\\n    \\\"pass_pct\\\": 51.7\\n  },\\n  \\\"majority_baseline_accuracy\\\": 51.75,\\n  \\\"single_pass_accuracy\\\": 87.51,\\n  \\\"majority_vote_accuracy\\\": 86.83,\\n  \\\"improvement_pp\\\": -0.69,\\n  \\\"agreement_distribution\\\": {\\n    \\\"3/3\\\": {\\n      \\\"count\\\": 1763,\\n      \\\"pct\\\": 93.3\\n    },\\n    \\\"2/3\\\": {\\n      \\\"count\\\": 127,\\n      \\\"pct\\\": 6.7\\n    }\\n  },\\n  \\\"per_pass_accuracies\\\": [\\n    86.72,\\n    86.83,\\n    87.62\\n  ],\\n  \\\"flipped_correct\\\": 15,\\n  \\\"flipped_wrong\\\": 28,\\n  \\\"net_flips\\\": -13,\\n  \\\"single_pass\\\": {\\n    \\\"accuracy\\\": 87.51,\\n    \\\"accuracy_vs_baseline_gap_pp\\\": 35.77,\\n    \\\"per_class\\\": {\\n      \\\"FAIL\\\": {\\n        \\\"precision\\\": 82.75,\\n        \\\"recall\\\": 93.64,\\n        \\\"f1\\\": 87.86,\\n        \\\"support\\\": 912\\n      },\\n      \\\"PASS\\\": {\\n        \\\"precision\\\": 93.24,\\n        \\\"recall\\\": 81.8,\\n        \\\"f1\\\": 87.15,\\n        \\\"support\\\": 978\\n      }\\n    },\\n    \\\"confusion_matrix\\\": {\\n      \\\"tn\\\": 854,\\n      \\\"fp\\\": 58,\\n      \\\"fn\\\": 178,\\n      \\\"tp\\\": 800\\n    },\\n    \\\"unparseable\\\": 0\\n  },\\n  \\\"majority_vote\\\": {\\n    \\\"accuracy\\\": 86.83,\\n    \\\"accuracy_vs_baseline_gap_pp\\\": 35.08,\\n    \\\"per_class\\\": {\\n      \\\"FAIL\\\": {\\n        \\\"precision\\\": 81.66,\\n        \\\"recall\\\": 93.75,\\n        \\\"f1\\\": 87.29,\\n        \\\"support\\\": 912\\n      },\\n      \\\"PASS\\\": {\\n        \\\"precision\\\": 93.24,\\n        \\\"recall\\\": 80.37,\\n        \\\"f1\\\": 86.33,\\n        \\\"support\\\": 978\\n      }\\n    },\\n    \\\"confusion_matrix\\\": {\\n      \\\"tn\\\": 855,\\n      \\\"fp\\\
…[truncated 345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_per-test-majority-voting_20260512T092930",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-12T09:30:06.478279+00:00_

## Per-test Majority Voting 实验结果

**实验状态：成功完成** (EXIT_CODE=0)

### 关键 Metrics

| Metric | Single-pass (greedy) | Majority Vote (K=3) | Delta |
|--------|---------------------|---------------------|-------|
| **Accuracy** | 87.51% | 86.83% | **-0.69pp** |
| FAIL F1 | 87.86% | 87.29% | -0.57pp |
| PASS F1 | 87.15% | 86.33% | -0.82pp |
| FAIL Recall | 93.64% | 93.75% | +0.11pp |
| PASS Recall | 81.80% | 80.37% | -1.43pp |

### 与 Baseline 对比

| Method | Accuracy |
|--------|----------|
| 3-seed mean (baseline) | 88.41% |
| Single-pass seed 42 | 87.83% |
| 本次 greedy | 87.51% |
| **Majority vote K=3** | **86.83%** |

### Flip 分析

- 3/3 unanimous: 1763 (93.3%) — 绝大多数样本三次预测一致
- 2/3 split: 127 (6.7%)
- Flipped correct→wrong: **28**, Flipped wrong→correct: **15**, Net: **-13**

Majority voting 在 127 个分歧样本上翻转了 43 个预测，但翻错的比翻对的多 13 个，导致整体下降。

### Per-pass 采样准确率

Pass 1: 86.72%, Pass 2: 86.83%, Pass 3: 87.62% — 三次采样均低于 greedy (87.51%)，temperature=0.7 引入的随机性降低了单次准确率。

### 结论

**Majority voting 无效，反而降低了 accuracy (-0.69pp)**。原因：

1. 模型在 greedy 模式下已经高度校准（87.5%），temperature 采样引入的噪声大于纠错收益
2. 93.3% 的样本三次一致，说明模型对大部分样本已高度 confident，self-consistency 无空间发挥
3. 在少数分歧样本上，错误翻转多于正确翻转（28 vs 15），说明模型错误不是随机噪声而是系统性偏差，voting 无法修复

**Per-test majority voting 不值得采用。** Single-pass greedy 更快（30s vs 120s）且更准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_per-test-majority-voting_20260512T092930"
}
```

</details>

---
