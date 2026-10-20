# analysis ngram dryrun

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ngram_dryrun_20260513T164246_result.json`
- **Structured JSON:** [`7dc1d111fd032b27fd73.json`](../../sessions/7d/7dc1d111fd032b27fd73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Leading Indicator Ranking（6 个 post-G0 checkpoints）

| Rank | Metric | Detected | Gen | Step | Baseline | Value | Change |
|------|--------|----------|-----|------|----------|-------|--------|
| 1 | unigram_ent | YES | G1 | 152 | 6.933 | 3.916 | **-43.5%** |
| 2 | bigram_ent | YES | G1 | 152 | 10.201 | 5.416 | **-46.9%** |
| 3 | trigram_ent | YES | G1 | 152 | 11.410 | 5.931 | **-48.0%** |
| 4 | vocab_cov | YES | G1 | 152 | 0.469 | 0.350 | **-25.3%** |
| — | eff_rank | NO | — | — | 676.957 | 678.296 | 无显著变化 |
| — | ppl | NO | — | — | 13.267 | 13.414 | 无显著变化 |
| — | tok_ent_mean | NO | — | — | 2.576 | 2.564 | 无显著变化 |
| — | spec_entropy | NO | — | — | 6.518 | 6.520 | 无显著变化 |

### 关键发现

- **最快信号**: unigram_entropy，在 G1 step 152（~10M tokens）即触发，下降 43.5%
- 所有 4 个 n-gram/coverage 指标在**同一个 checkpoint**（G1 step 152）同时触发，说明 collapse 在 G1 第 2 个 checkpoint 时已经发生剧烈恶化
- G1 第 1 个 checkpoint（step 76）时这些指标尚未触发阈值，说明 collapse 发生在 step 76→152 之间

### eff_rank 对比

- **eff_rank 未被检测到**：G0 final 676.96 → G1 final 678.30，变化仅 +0.2%
- 与已知数据一致：eff_rank 变化 +1.34（稳定），而 vocab_coverage -71%、unigram_entropy -86%
- **结论：eff_rank 不是 collapse 的 leading indicator**，n-gram entropy 指标远比 spectral effective rank 更敏感

### 注意

4 个检测到的指标在同一 checkpoint 同时触发，无法区分谁"更 leading"。需要更细粒度的 checkpoint 间隔（如每 20 steps 采样）才能分离它们的时序差异。当前检测到的 checkpoint 是 G1 第 2 个 eval 点。

---
