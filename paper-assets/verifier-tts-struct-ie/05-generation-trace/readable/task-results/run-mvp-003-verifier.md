# run mvp 003 verifier

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_mvp-003-verifier_20260511T192340_result.json`
- **Structured JSON:** [`68b78b60915dd53b8ad5.json`](../../sessions/68/68b78b60915dd53b8ad5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

=== Verifier Selection F1 矩阵 ===

| N | greedy | exact_sc | verify_selected | oracle | random |
|---|--------|----------|-----------------|--------|--------|
| 1 | 42.05 | — | — | — | — |
| 4 | — | 41.88±0.37 | 41.56±0.13 | 45.92±0.42 | 41.29±0.72 |
| 8 | — | 42.22±0.63 | 41.98±0.14 | 47.45±0.25 | 41.79±0.58 |
| 16 | — | 41.34±0.32 | 42.00±0.33 | 48.54±0.36 | 41.83±0.86 |

**Verify parse 成功率**: 100% (8400/8400)

**同分文档比例** (verifier 给所有候选同分):
- N=4: 56-65% 的 docs 所有候选同分
- N=8: 50-52%
- N=16: 40-43%

**Verify score 与实际 F1 相关性**:
- Pearson: 0.088~0.101 (极弱)
- Spearman: 0.129~0.149 (极弱)

**Pass: verify-selected@N≥8 > greedy ≥ 1.0pt? NO**

### 关键发现

1. **Verifier 几乎无法区分好坏候选。** Pearson/Spearman 相关系数均 <0.15，说明 verify score 和实际 F1 基本无关。

2. **同分问题严重。** N=4 时 56-65% 的文档所有候选获得相同分数，verifier 在这些 docs 上退化为随机选择。N=16 时好一些（40-43%），因为候选差异更大。

3. **verify_selected 性能和 random baseline 接近**，都在 41-42 范围内，未能超过 greedy baseline。这与低相关性一致——verifier 本质上是在随机选择。

4. **根本原因**: 同一个 Qwen3-8B 模型既做 NER 又做 verify，它无法识别自己的错误。需要更强的 verifier 模型或不同的验证策略（如 pairwise comparison 而非 pointwise scoring）。

---
