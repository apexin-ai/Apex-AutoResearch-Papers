# code fix multiseed add seed123

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-multiseed-add-seed123_20260515T005257_result.json`
- **Structured JSON:** [`c992be6de35c8e4ee4f8.json`](../../sessions/c9/c992be6de35c8e4ee4f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个脚本已修改并重跑成功。

## 结果汇总

| Method | Seeds | Mean | SD |
|--------|-------|------|-----|
| Vanilla | 3 | **65.3%** | 3.3% |
| TaxEI | 3 | **56.7%** | 8.6% |
| Random | 3 | **63.1%** | 6.9% |

与预期完全一致。

### 关键变化（vs 之前 2-seed 分析）

| 指标 | 之前 (2-seed) | 现在 (3-seed) |
|------|------|------|
| TaxEI vs Vanilla pooled Δ | -10.6% (p=0.0483) | **-8.5% (p=0.0756)** |
| TaxEI vs Random pooled Δ | -6.4% (p=0.1786) | -6.4% (p=0.1790) |
| Variance ratio TaxEI/Vanilla | 3.3x | **7.0x** |

Permutation test p 值变化：加入 seed=123 后 TaxEI vs Vanilla 的 pooled 比较从 p=0.0483（刚好显著）变为 p=0.0756（不显著），因为 seed=123 的 TaxEI (61.7%) 接近 Vanilla (66.0%)，拉高了 TaxEI 均值。方差比从 3.3x 升至 7.0x，因为 TaxEI 在 seed=0 的异常低值(46.8%)在 3 个数据点中更突出。

---
