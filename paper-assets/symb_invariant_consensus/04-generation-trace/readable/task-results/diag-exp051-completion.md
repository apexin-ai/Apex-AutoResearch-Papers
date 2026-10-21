# diag exp051 completion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp051-completion_20260519T043523_result.json`
- **Structured JSON:** [`83309db0fc5665021165.json`](../../sessions/83/83309db0fc5665021165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整 K sensitivity 数据表：

## Mistral-7B K Sensitivity on FOLIO-204 (T=0.7)

| K | SC% | SICA% | Delta (pp) | b | c | McNemar p |
|---|-----|-------|------------|---|---|-----------|
| 4 | 54.41 | 52.94 | **-1.47** | 7 | 10 | 0.629 |
| 8 | 57.35 | 56.37 | **-0.98** | 4 | 6 | 0.754 |
| **12** | **54.41** | **59.31** | **+4.90** | **12** | **2** | **0.013** |
| 16 | 55.88 | 57.35 | **+1.47** | 10 | 7 | 0.629 |
| 20 | 57.35 | 59.31 | **+1.96** | 5 | 1 | 0.219 |

### K=20 分析

K=20 delta = +1.96pp，高于 K=16 的 +1.47pp 但远低于 K=12 的 +4.90pp。曲线不是严格倒 U 型（K=20 略高于 K=16），但整体呈 **peaked 曲线**：
- K<12：SICA 负效果（constraints 不足以纠正投票）
- **K=12：唯一显著正效果**（p=0.013，b=12 vs c=2）
- K>12：正效果但不显著，且大幅衰减（可能因 contradiction_rate 上升稀释信号）

K=20 的 b=5, c=1 比例很倾斜但样本太小无法达到显著性。contradiction_rate 从 K=12 的 3.5% 升至 K=20 的 3.9%，符合预期。

### 完成清单
- Registry: `exp-051-mistral-k-sensitivity` → DONE (success)
- Cron: 已删除
- 五点数据齐全，可直接用于论文 K ablation 图表

---
