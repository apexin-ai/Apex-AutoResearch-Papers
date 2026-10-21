# analysis deepseek exception only seed123 v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_exception_only_seed123_v2_20260520T064922_result.json`
- **Structured JSON:** [`a23f4f5509d00c15658d.json`](../../sessions/a2/a23f4f5509d00c15658d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 实验结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **99.50%** (95% CI: [99.08%, 99.83%]) |
| Train Loss | 0.1234 |
| Eval Loss (epoch 3) | 0.478 |
| 训练时长 | ~1h 45min (3 epochs, 444 steps) |

## 对比

| 实验 | Accuracy | 结论 |
|------|----------|------|
| seed42 (current code) | 99.33% | baseline |
| **seed123 v2 (current code)** | **99.50%** | seed 一致 (+0.17pp) |
| seed123 old (5/15, old code) | 91.09% | **确认是代码 bug** |

**结论: SUCCESS** — seed123 在当前代码下达到 99.50%，与 seed42 基本一致，旧版 91.09% 确认为代码问题导致。Registry 已更新为 DONE/success，报告已注册。

---
