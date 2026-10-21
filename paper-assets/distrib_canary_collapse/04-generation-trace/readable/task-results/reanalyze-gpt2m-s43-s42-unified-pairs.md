# reanalyze gpt2m s43 s42 unified pairs

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_reanalyze_gpt2m_s43_s42_unified_pairs_20260519T153238_result.json`
- **Structured JSON:** [`af2975afea948ef8b0f6.json`](../../sessions/af/af2975afea948ef8b0f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总报告：

---

## D101 结果：GPT-2m 统一 Downstream Pair 重分析

### Pair 配置变更
- **旧**: ent/ece → d1, d2, d3, **perplexity** (8 pairs)
- **新**: ent/ece → d1, d2, d3, **mauve** (8 pairs)

### GPT-2m s43 新旧对比

| 指标 | 旧 (含 ppl) | 新 (含 mauve) | 变化原因 |
|------|-----------|-------------|---------|
| PermG fwd | 8/8 | **6/8** | mauve 2 pairs 不显著 (p=0.33, 0.49) |
| PermG rev | 5/8 | **4/8** | mauve→ece 丢失 |
| Diff XCorr fwd | 8/8 | **6/8** | mauve pairs DiffFDR=0.24 |
| TY fwd | 4/8 | 4/8 | 不变 |
| Threshold | 0/8 | 0/8 | 不变 |
| K≥3 | 4/8 | 4/8 | 不变 |
| K≥4 | 1/8 | 1/8 | 不变 |
| MMCT uniform | — | 4/8 (50%) | |
| MMCT wpair | — | 6/8 (75%) | |

### GPT-2m s42 新旧对比

| 指标 | 旧 (含 ppl) | 新 (含 mauve) | 变化原因 |
|------|-----------|-------------|---------|
| PermG fwd | 6/8 | 6/8 | 不变 (ppl/mauve 都不 sig) |
| PermG rev | 3/8 | 3/8 | 不变 |
| TY fwd | 5/8 | **2/8** | ppl 的 TY 显著被 mauve 的不显著取代 |
| K≥3 (5method) | — | 2/8 | 保守 consensus |
| K≥4 (5method) | — | 0/8 | |
| MMCT uniform | — | 2/8 (25%) | |
| MMCT wpair | — | 6/8 (75%) | |

### 跨 Seed 一致性

| 指标 | s43 | s42 |
|------|-----|-----|
| PermG fwd | 6/8 | 6/8 | **一致** |
| PermG rev | 4/8 | 3/8 | 近似 |
| K≥3 | 4/8 | 2/8 | s42 较弱（ece→d2/d3 在 s42 中 TY 不显著） |
| MMCT wpair | 75% | 75% | **一致** |

### 关键发现

1. **Mauve 作为 downstream 在 T=11 下信号极弱**：所有 mauve pair 的 PermG p>0.10，DiffXCorr FDR>0.07。mauve 变化幅度仅 +7.9% (s43) / +7.9% (s42)，相比 distinct 指标 -12~-14% 的 drift，信噪比不足。

2. **Core distinct pairs 不受影响**：K≥3 和 K≥4 的 robust pairs 完全由 distinct 指标驱动，不含 ppl 或 mauve。统一 pair 后这些核心结论不变。

3. **PermG fwd 从 8/8 降到 6/8（s43）**：纯粹因为去掉了 ppl pairs（ppl drift +50527% 信号极强），换成 mauve（drift 仅 ~8%）。这是 apples-to-apples 对比的正确代价。

4. **MMCT wpair 跨 seed 稳定在 75%**：FPR 逆加权后，distinct pairs 的强信号补偿了 mauve 的弱信号。

---
