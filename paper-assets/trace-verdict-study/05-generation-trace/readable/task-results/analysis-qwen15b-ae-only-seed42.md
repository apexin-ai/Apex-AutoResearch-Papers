# analysis qwen15b ae only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_ae_only_seed42_20260520T074850_result.json`
- **Structured JSON:** [`7e4081f7e6ed5d7465e5.json`](../../sessions/7e/7e4081f7e6ed5d7465e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：SUCCESS — Qwen-1.5B ae_only 达 99.08% accuracy**

| 指标 | 值 |
|------|-----|
| Accuracy | 99.08% [98.49%, 99.58%] |
| Pass | P=1.000 R=0.987 F1=0.994 |
| Fail | P=0.969 R=1.000 F1=0.984 |

关键发现：
- 1.5B 模型与 13B CodeLlama (99.08%) 持平，仅比 7B Qwen (99.92%) 低 0.84pp
- ae_only 信号在 1.5B–13B 范围内 scale-invariant
- fail recall = 1.000（零漏检），符合 CI 场景偏好
- 同模型 ae_only (99.08%) vs exception_only (99.83%) 差距 0.75pp，均在 ceiling 区域

Registry 已更新为 DONE/success，分析报告已注册 (`art_20260520_dd2394`)。

---
