# ops feat ablation v1 check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feat_ablation_v1_check_20260515T193449_result.json`
- **Structured JSON:** [`4d4708f2dc5399e6c203.json`](../../sessions/4d/4d4708f2dc5399e6c203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中已清理）。

---

## feat_ablation_v1 结果汇报

**状态：成功完成，9/9 cells 全部跑完**，总耗时 7822s (~2.2h)。

### 关键 Metrics

| 指标 | 值 |
|------|-----|
| Full 19 features mean acc | **0.7847** ± 0.0494 |
| Top-5 features mean acc | **0.7678** ± 0.0527 (97.8% of full) |
| Top-2 features mean acc | **0.7152** ± 0.0581 (91.1% of full) |
| 达到 95% full acc 所需特征数 | mean **4.2**, max **5** |

### Forward Selection 首选特征

- **p90_ppl**: 6/9 cells（gpt2xl 全部 + olmo 全部）
- **var_surprisal**: 3/9 cells（pythia 全部）

### 特征类别排名（单类别 accuracy）

1. **perplexity**: 0.767 — 全部 9/9 cells 的最佳单类别
2. **surprisal**: 0.733
3. **lexical_diversity**: 0.462
4. **repetition**: 0.437
5. **ngram_entropy**: 0.395

### 核心发现

- Perplexity 类特征主导，单类别就能达到 ~98% of full accuracy
- 只需 ~4 个特征即可达到 full 的 95%，19 个特征中大量冗余（VIF>10 的有 14-16 个）
- Registry 已更新为 DONE/success，metrics 已写入

---
