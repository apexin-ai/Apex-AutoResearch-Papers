# analysis fix ve calibration

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fix-ve-calibration_20260514T095646_result.json`
- **Structured JSON:** [`9ae9363ac5bff3a6fd8b.json`](../../sessions/9a/9ae9363ac5bff3a6fd8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是汇总报告：

---

## 修正结果

### JSON 更新摘要
- **95 个 v/R 数据点**全部改用 `eval_return` 重算，每个点新增 `eval_return` 字段
- 分析文本描述已同步更新
- `"100% classification accuracy"` → `"cleanly separates"`
- metadata 增加 `v_over_return_note` 说明修正

### 关键 v/R 变化（late-stage）

| 实验 | 旧 v/R (train) | 新 v/R (eval) | 变化 |
|------|----------------|---------------|------|
| **exp_008d@55K** (collapsed) | 1.87 | **1.67** | ↓ 但仍远超 1.0 |
| **exp_006@65K** (collapsed) | 2.43 | **2.72** | ↑ 更极端 |
| exp_008a@105K (healthy) | 0.47 | 0.39 | ↓ |
| exp_008c@65K (healthy) | 0.32 | 0.33 | ≈ |
| exp_008e_v3@105K (healthy) | 0.60 | 0.53 | ↓ |
| exp_008f@105K (healthy) | 0.21 | 0.20 | ≈ |
| baseline@505K | 0.67 | 0.69 | ≈ |

结论不变：collapsed 的 v/R 远超 1.0，healthy 从未超过 1.0，分离性依然明确。

### 新发现的数据点

```
008d@55K: eval_return=82.75, value_mean=137.88
006@65K: eval_return=132.86, value_mean=361.69
007@45K: eval_return=144.41, value_mean=18.26
007@55K: eval_return=152.49, value_mean=9.28
```

---
