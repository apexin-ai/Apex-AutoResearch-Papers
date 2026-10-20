# analysis carc mvp seed42

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carc_mvp_seed42_20260512T112044_result.json`
- **Structured JSON:** [`ae4ea53be0dd41e3d9ef.json`](../../sessions/ae/ae4ea53be0dd41e3d9ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## carc_mvp_seed42 实验结果

### 全局指标

| 指标 | seed42 | seed1337 (参考) |
|------|--------|----------------|
| pearson_r_ema_perturbation | **-0.1176** | -0.113 |
| spearman_r_ema_perturbation | -0.1087 | — |
| perturbation_diff_pct | **5.69%** | 5.26% |
| pearson_r_ema_surprisal | +0.1162 | — |
| ppl_twotier | 1.34 | — |
| ppl_uniform40 | 1.34 | — |
| near_zero_ratio (red/novel) | 0.4992/0.4536 = 1.10x | — |
| partial_r(EMA,pert\|pos) | -0.1151 | — |
| partial_r(EMA,surp\|pos) | +0.1344 | — |
| chain_level_r(EMA,pert) | -0.3570 | — |
| chain_level_r(EMA,surp) | +0.3195 | — |
| n_redundant / n_novel | 19,158 / 2,312,874 | — |

### 2×2 判定

| 条件 | 阈值 | 实际值 | 通过? |
|------|------|--------|-------|
| \|r\| >= 0.4 | 0.4 | 0.1176 | NO |
| diff >= 10% | 10% | 5.69% | NO |

**Verdict: FAIL** (两条都不满足，与 seed1337 一致)

### Per-layer 分析

**3 层达到 PASS 标准** (\|r\|>=0.4 AND diff>=10%):

| Layer | r | diff% | n_redundant |
|-------|---|-------|-------------|
| L30 | -0.4412 | +13.0% | 2465 |
| L31 | -0.4150 | +12.7% | 1098 |
| L33 | -0.4156 | +10.7% | 719 |

**仅 \|r\|>=0.4 但 diff<10% 的层**: 无 (即所有 \|r\|>=0.4 的层都同时满足 diff>=10%)

**diff>=10% 但 \|r\|<0.4 的层 (DISCORDANT-A)**: L03-L07, L09-L17, L21, L23, L25-L26, L28-L29, L36-L37, L39-L46 — 共 30 层有 diff>=10% 但相关性不够

**表现最差的层** (\|r\|<0.1 且 diff<5%): L01 (r=-0.067, +0.1%), L02 (r=-0.001, +3.2%), L47 (r=+0.071, +2.8%)

### 结论

seed42 与 seed1337 高度一致：全局 Pearson r ≈ -0.12，perturbation diff ≈ 5.7%，均远未达到 PASS 阈值。虽然中深层 (L30-L33) 在 per-layer 粒度上表现出显著信号（\|r\|>0.4 且 diff>10%），但这些信号聚集在少数层且被大量弱信号层稀释，全局聚合后不足以通过。两个 seed 的复现性很好，说明 FAIL 结论稳健。

---
