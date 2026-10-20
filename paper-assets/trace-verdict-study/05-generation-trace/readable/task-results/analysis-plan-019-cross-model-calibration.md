# analysis plan 019 cross model calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_019_cross_model_calibration_20260521T151825_result.json`
- **Structured JSON:** [`4aecfc05022c302cb260.json`](../../sessions/4a/4aecfc05022c302cb260.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_019 完成。产出汇总：

**服务器 artifacts**:
- `/root/trace-verdict-study/artifacts/cross_model_calibration_plan019.json` — 完整数据（含 per-bin reliability 数据）
- `/root/trace-verdict-study/artifacts/cross_model_calibration_plan019.md` — 分析报告
- `/root/trace-verdict-study/artifacts/cross_model_calibration_plan019.png` — Reliability diagram

**核心结论**：Exception-only calibration 跨模型一致，4 个架构（1.5B–13B）ECE 均 < 0.005：

| Model | Acc | ECE | Brier |
|-------|-----|-----|-------|
| Qwen2.5-7B | 99.83% | 0.0027 | 0.0013 |
| DeepSeek-6.7B | 99.33% | 0.0049 | 0.0059 |
| CodeLlama-13B | 99.83% | 0.0020 | 0.0013 |
| Qwen2.5-1.5B | 99.83% | 0.0020 | 0.0013 |

MCE 数值偏高但均由 1–2 个样本的稀疏 bin 造成，不反映系统性 miscalibration。99.2%+ 样本落在 [0.95, 1.0] 置信区间且正确率 100%。

---
