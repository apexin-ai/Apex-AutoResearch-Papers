# code fix code analysis script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-code-analysis-script_20260519T025536_result.json`
- **Structured JSON:** [`b977254b475e8aca05e2.json`](../../sessions/b9/b977254b475e8aca05e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

| 检查项 | 结果 |
|--------|------|
| Qwen-1.5B: K\*=2, 0v1 AUC | K\*=2, AUC=0.9388 |
| Pythia-1.4B: K\*=1, 0v1 AUC | K\*=1, AUC=0.9592 |
| 其他 3 模型 | TBD |
| Caption 含 "CodeSearchNet Python" | 有 |
| Caption 含 "TheStack" | 无 |
| 表格列数 | `l cc cc cc cc cc` = 11 列 |
| cmidrule 分组 | `{2-3} {4-5} {6-7} {8-9} {10-11}` |

Pythia-1.4B 的 K\*=1 与预期一致，但 0v1 AUC 实际值为 0.9592（高于预估的 0.8952）。这是从 `exp_code_pythia1b4/pairwise_auc.json` 读出的真实数据。

---
