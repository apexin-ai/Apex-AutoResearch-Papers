# ops check 80pool status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_80pool_status_20260516T021312_result.json`
- **Structured JSON:** [`9504e7283a798c9e0d4e.json`](../../sessions/95/9504e7283a798c9e0d4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：**已完成** (completed)

100/100 batches 全部跑完，extract + analyze 两阶段均正常结束。完成时间 2026-05-16 10:06:21 UTC。

### 输出文件
`/root/schema-dag-extraction/artifacts/fewrel_80pool_16sub/`
- `bootstrap_ci.json` — 主结果
- `results_incremental.jsonl` — 100 batches 逐条结果
- `predictions_incremental.jsonl` — 原始预测
- `preprocess.json` / `batch_config.json` — 配置

### 关键 Metrics

| 指标 | 值 |
|------|-----|
| **Overall accuracy** | 80.77% (std=0.0797) |
| **Δ(Q4-Q1)** | **-3.92pp**, 95% CI [-7.79, +0.42] |
| Q1 (low BCS=0.504) | acc=82.83% [79.92, 85.42] |
| Q2 (BCS=0.541) | acc=79.42% [76.00, 82.58] |
| Q3 (BCS=0.569) | acc=81.92% [79.00, 84.67] |
| Q4 (high BCS=0.614) | acc=78.92% [75.87, 82.25] |
| **Pearson r(BCS, acc)** | -0.2206 |
| **Regression slope** | -0.4010, 95% CI [-0.684, -0.063], **p=0.027** |

趋势方向一致（高 BCS → 低 accuracy），回归斜率显著 (p<0.05)，但 Δ(Q4-Q1) 的 bootstrap CI 跨零 [-7.79, +0.42]，quartile 对比未达显著。

---
