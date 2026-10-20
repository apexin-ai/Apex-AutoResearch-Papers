# exp sf1 padding status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sf1_padding_status_check_20260521T205638_result.json`
- **Structured JSON:** [`562dd1d3fd0ad99bf069.json`](../../sessions/56/562dd1d3fd0ad99bf069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`exception_only_padded2048_seed42` ✓ 已完成

| 指标 | 值 |
|------|-----|
| **Accuracy** | **99.83%** (CI: 99.6%–100%) |
| Majority baseline | 71.5% |
| Lift | +28.3pp |
| Pass F1 | 0.999 (P=1.00, R=1.00) |
| **Fail F1** | **0.997** (P=0.99, R=1.00) |
| 测试样本 | 1190 |
| 训练耗时 | ~2.46 GPU-hours |

训练正常完成，cuda:1 已释放。Registry 已更新为 DONE/success。Padding 到 2048 tokens 对 exception-only 条件下的 verdict 分类几乎无损——仅 2 个 pass 样本被误判为 fail（1190 中错 2 个）。

---
