# code classifier volatility fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classifier-volatility-fix_20260519T194558_result.json`
- **Structured JSON:** [`70130f75130a11fa1960.json`](../../sessions/70/70130f75130a11fa1960.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6/6 通过。验证结果：

| Family | Seed | Pattern | Conf | Key Signal |
|--------|------|---------|------|-----------|
| Phi-4 | 42 | Immune | 0.915 | max_dev=0.34pp ≤ τ |
| Qwen-14B | 42 | U-collapse | 0.937 | delta=-9.37pp |
| Qwen-7B | 42 | V-recovery | 0.618 | trough 63.15%, partial recovery |
| Gemma-2 | 42 | Benefit | 1.000 | +3.76pp monotonic |
| OLMo-2 | 42 | Benefit-sat | 0.515 | late gain 0.47pp < 0.5pp floor |
| Qwen-7B | 123 | **V-recovery-full** | 1.000 | delta=0.00pp but max_dev=3.22pp, V-dip to 63.37% |

Qwen-7B s123 现在正确分类为 V-recovery-full 而非 Immune。核心改动：在 `|Δ| ≤ τ` 分支内先算 `max_deviation = max(|a_i - a_0|)`，超过 τ 且有 V-dip 则判定为 V-recovery-full。三个文件（Python / TeX / YAML）已同步更新。

---
