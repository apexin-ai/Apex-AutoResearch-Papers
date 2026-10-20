# analysis qwen3 pw kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen3-pw-kappa_20260524T105840_result.json`
- **Structured JSON:** [`f2ff07d7f6d078a2336d.json`](../../sessions/f2/f2ff07d7f6d078a2336d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
Qwen3-14B ProofWriter — Fleiss' κ
============================================================

--- exp033 (seed42) ---
  N = 599,  K = 12,  κ = 0.7872,  K_eff = 1.24

--- seed123 ---
  N = 583,  K = 12,  κ = 0.7849,  K_eff = 1.25

--- seed456 ---
  N = 582,  K = 12,  κ = 0.7820,  K_eff = 1.25

--- seed789 ---
  N = 584,  K = 12,  κ = 0.7779,  K_eff = 1.26

Cross-seed:
  Mean κ  = 0.7830
  Std κ   = 0.0035
```

**答案类别分布**（三大类占比，其余为极少量提取错误）：
- Unknown: ~44%
- True: ~28%
- False: ~28%

κ ≈ 0.78 属于 "substantial agreement"（Landis & Koch 标准），12 条 traces 之间一致性很高。K_eff ≈ 1.25 表明 12 条 traces 的有效独立样本数约为 1.25——traces 之间高度冗余。

---
