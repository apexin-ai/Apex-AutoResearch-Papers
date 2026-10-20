# fetch gold canonical results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fetch_gold-canonical-results_20260515T091822_result.json`
- **Structured JSON:** [`866f68edef2563fab500.json`](../../sessions/86/866f68edef2563fab500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 files written locally. `model_consistency_report.md` not found on server.

## 关键确认

### 1. Shared window 数量：**确认为 195**

`gb_vs_mv` 测试的 `n_samples = 195`。199 个 gold windows 中有 4 个不在 `non_abstain`（即这 4 个 gold window 的 MV label 是 abstain/-1，无法匹配到 windows_labeled.jsonl 的非弃权子集），所以 shared = 195。没有 gold window 被"丢失"——这 4 个是因为原始数据中三名标注者无多数一致而被排除。

### 2. GB 训练集大小（gold exclusion 后）

| 指标 | 值 |
|------|-----|
| 原始 train_indices | 10,634 |
| gold windows 在 train 中 | 39 |
| 排除后训练集 | **10,595** |
| keep_indices (非弃权子集) | 15,401 |

GB 模型在 bootstrap 脚本中重新训练时排除了 39 个 gold window（`[leakage-fix]`），用 10,595 个样本训练，然后在全部 195 个 shared gold window 上预测。

---
