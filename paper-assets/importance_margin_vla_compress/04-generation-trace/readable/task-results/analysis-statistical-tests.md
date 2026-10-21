# analysis statistical tests

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_statistical_tests_20260519T200645_result.json`
- **Structured JSON:** [`831f9dd04c77483eecab.json`](../../sessions/83/831f9dd04c77483eecab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

统计检验完成，已注册为 `art_20260519_cd7566`。

核心结论：
- **仅 2/10 对显著 (p<0.05)**：M=64 VTC > M=96 VTC (p=0.034)，M=32 MLP > M=96 VTC (p=0.022)
- **VTC vs MLP (M=32)：p=0.150，不显著** — MLP 领先 3.3pp 但 n=3 power 不足以确认
- M=32/64/128 VTC 形成不可区分的性能平台（所有 p>0.25）
- M=96 是确认的低点，Bonferroni 校正后 (α=0.005) 所有对均不显著
- 论文措辞建议：VTC vs MLP 用 "comparable" / "no significant difference"，M=96 dip 可直接 claim

---
