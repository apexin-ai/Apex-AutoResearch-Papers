# code exp004 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004_bootstrap_ci_20260515T231700_result.json`
- **Structured JSON:** [`5ea30e9b4b9735c138c2.json`](../../sessions/5e/5ea30e9b4b9735c138c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `artifacts/bootstrap_ci_7b.json`。

## Bootstrap CI + Permutation Test (Qwen-7B, exp-004)

| Pair | AUC | CI Lower | CI Upper | CI Width | Perm p |
|------|-----|----------|----------|----------|--------|
| 0v1 | 0.9638 | 0.9607 | 0.9665 | 0.0059 | <0.0001 |
| 1v2 | 0.6168 | 0.6079 | 0.6261 | 0.0182 | <0.0001 |
| 2v3 | 0.5492 | 0.5388 | 0.5594 | 0.0205 | <0.0001 |
| 3v4 | 0.5276 | 0.5170 | 0.5375 | 0.0204 | <0.0001 |
| 4v5 | 0.5085 | 0.4988 | 0.5191 | 0.0202 | 0.0676 |

**关键发现**:
- **1v2 CI lower = 0.6079 > 0.60** → K*=2 结论 robust，整个 CI 在 0.60 以上
- **2v3 CI lower = 0.5388 < 0.56** → depth 2→3 区分力显著低于 1→2，符合 K*=2 的断点
- **4v5 是唯一 p>0.05 的 pair**（p=0.0676），CI 跨过 0.50 → 该 pair 不显著区别于 chance
- **0v1 CI 极窄（0.006）**，AUC ~0.96，depth 0→1 区分几乎完美
- OOF AUC 与之前报告的轻微差异（如 0.9644→0.9638）是 GroupKFold 随机性导致的，在 CI 内

---
