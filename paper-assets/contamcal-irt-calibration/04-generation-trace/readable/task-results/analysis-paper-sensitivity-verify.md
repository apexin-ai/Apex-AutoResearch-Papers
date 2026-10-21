# analysis paper sensitivity verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-sensitivity-verify_20260519T223917_result.json`
- **Structured JSON:** [`083f115a618bac281157.json`](../../sessions/08/083f115a618bac281157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

### Sensitivity 描述（30→180）

| 位置 | 内容 | 状态 |
|------|------|------|
| method.tex:59 | "30-combination grid sweep … (180/180 model--seed--threshold pairs" | ✅ |
| results.tex:11 (Table 1 caption) | "180/180 model--seed--combination pairs across 30 $(\tau,\sigma)$ combinations" | ✅ |
| results.tex:27 | "stable across 30 $(\tau,\sigma)$ threshold combinations (six model--seed configurations" | ✅ |
| appendix.tex:154 (Table 7) | "grid sweep over 30 $(\tau, \sigma)$ combinations", 表内 6 行各 30/30 | ✅ |

所有 "30" 均指 grid size（6τ×5σ=30），无遗留错误。"180" 正确出现在 method.tex 和 results.tex Table 1 caption 中（30 combos × 6 model-seed = 180 pairs）。

### V-recovery 修改

| 位置 | 内容 | 状态 |
|------|------|------|
| method.tex:59 | "recovery extent varies by seed (partial at seed$=$42, full at seed$=$123)" | ✅ |
| results.tex:30 | "recovery extent varies from partial to full" | ✅ |
| limitations.tex:10 | "recovery extent varies (partial at s42, full at s123)" | ✅ |

### 其他修改

| 位置 | 内容 | 状态 |
|------|------|------|
| limitations.tex:9 | `\paragraph{Seed coverage.}` | ✅ |
| abstract.tex:1 | "partial-to-full rebound" | ✅ |

全部 6 处 sensitivity + 3 处 V-recovery + 2 处其他修改均已到位，无遗漏。

---
