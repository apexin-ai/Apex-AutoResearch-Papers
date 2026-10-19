# infra steering monitor L24 v4

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_steering-monitor-L24-v4_20260523T105419_result.json`
- **Structured JSON:** [`699596e4b19e768ac04d.json`](../../sessions/69/699596e4b19e768ac04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma L24 (121)

**状态:** 完成

**Probe accuracy:** 76.27%

**Baseline distribution:** both=32, neither=55, parametric=26, contextual=45 (n=158 conflict samples)

### 结果表（alpha × contextual 方向）

| alpha | steering flips | control flips | p→c | c→p | Fisher p |
|-------|---------------|---------------|-----|-----|----------|
| +5.0  | 1/158 (0.6%)  | 1/158 (0.6%)  | 0   | 0   | 1.0000   |
| +10.0 | 3/158 (1.9%)  | 2/158 (1.3%)  | 0   | 0   | 1.0000   |
| +20.0 | 5/158 (3.2%)  | 4/158 (2.5%)  | 0   | 0   | 1.0000   |

**Bonferroni 显著 (k=6, p < 0.0083):** 无。所有条件 Fisher p = 1.0，steering flips 与 control flips 无显著差异，且 p→c / c→p 定向翻转均为 0。

**路径:**
- Log: `/root/clkc_mech_interp/logs/steering_gemma_L24.log`
- JSON: `/root/clkc_mech_interp/data/gemma2/steering_results_L24_last.json`

L24 steering 完全无效——flip rate 极低且与 control 无差异，方向性翻转为零。

---
