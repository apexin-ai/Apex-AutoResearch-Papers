# diag olmo2 arc s0 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-arc-s0-completion_20260520T182352_result.json`
- **Structured JSON:** [`935ae0977415845727ae.json`](../../sessions/93/935ae0977415845727ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 不存在（已被清理）。

**OLMo-2 ARC 三种子均值计算：**

| seed | d000 | d005 | d025 | d050 | d100 | Δ(d100-d000) |
|------|-------|-------|-------|-------|-------|-------------|
| s0 | 75.85 | 76.79 | 78.58 | 78.50 | 79.35 | **+3.50** |
| s42 | 76.11 | 76.62 | 78.16 | 79.61 | 80.03 | **+3.92** |
| s123 | 76.88 | 77.22 | 76.62 | 79.18 | 79.78 | **+2.90** |
| **mean** | **76.28** | **76.88** | **77.79** | **79.10** | **79.72** | **+3.44** |

**三种子均值 Δ = (+3.50 + 3.92 + 2.90) / 3 = +3.44pp**

对比 MMLU 三种子均值 +1.35pp，ARC contamination effect 约为 MMLU 的 **2.5 倍**。这与预期一致——ARC 题目量少（1172 vs MMLU ~14k），contamination 在小 benchmark 上效应更显著。

OLMo-2 现在是第二个 n=3 seeds × 双 benchmark（ARC + MMLU）完整的模型家族。

---
