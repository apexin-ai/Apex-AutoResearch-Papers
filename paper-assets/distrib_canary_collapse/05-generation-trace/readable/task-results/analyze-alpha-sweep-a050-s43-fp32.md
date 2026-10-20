# analyze alpha sweep a050 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_alpha_sweep_a050_s43_fp32_20260519T094232_result.json`
- **Structured JSON:** [`40065ba0ed268c098a2f.json`](../../sessions/40/40065ba0ed268c098a2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要
- **conclusion**: success
- **PermG**: 6/8 (75%)
- **MMCT wpair**: 6/8 (75%)
- **d1 drift**: -29.00%
- **perplexity_gen0**: 26.95
- **perplexity_gen9**: 31.38
- **token_entropy_gen0**: 3.2342
- **token_entropy_gen9**: 2.6849
- **checkpoint_path**: `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43_fp32/gen_10/checkpoint/`
- **log_path**: `~/runs/distrib_canary_collapse/alpha_sweep_a050_s43_fp32.log`
- **wandb_run_id**: 无（日志中未找到 W&B 链接）

## 详细分析

### Per-generation metrics

| Gen | token_entropy | perplexity | distinct_1 | ece | mauve |
|-----|--------------|-----------|-----------|-------|-------|
| 0 | 3.2342 | 26.95 | 0.09290 | 0.0108 | 0.0304 |
| 1 | 2.5186 | 23.48 | 0.09157 | 0.0702 | 0.0282 |
| 2 | 2.5474 | 26.29 | 0.07470 | 0.0776 | 0.0265 |
| 3 | 2.6089 | 27.44 | 0.07090 | 0.0766 | 0.0234 |
| 4 | 2.6246 | 28.89 | 0.07121 | 0.0821 | 0.0208 |
| 5 | 2.6185 | 29.21 | 0.07014 | 0.0838 | 0.0227 |
| 6 | 2.6600 | 29.72 | 0.06980 | 0.0842 | 0.0238 |
| 7 | 2.6724 | 30.44 | 0.06874 | 0.0835 | 0.0222 |
| 8 | 2.6564 | 31.50 | 0.06770 | 0.0890 | 0.0265 |
| 9 | 2.6849 | 31.38 | 0.06638 | 0.0871 | 0.0245 |
| 10 | 2.7227 | 31.58 | 0.06596 | 0.0842 | 0.0232 |

### Lead-lag pattern

token_entropy 在 gen 0→1 急剧下降（3.234→2.519，-22.1%），之后 gen 2-10 缓慢回升但始终远低于 baseline。distinct_1 的下降从 gen 1→2 开始明显（0.0916→0.0747），滞后 1 generation，经典的 canary lead 模式。

### Per-pair consensus detail (K≥4 threshold)

| Pair | Votes | K≥4? | Methods |
|------|-------|------|---------|
| token_entropy→d1 | 5 | **Yes** | naive, diff, thresh, pg_fwd, ty |
| token_entropy→d2 | 5 | **Yes** | naive, diff, thresh, pg_fwd, ty |
| token_entropy→d3 | 4 | **Yes** | naive, diff, thresh, pg_fwd |
| token_entropy→mauve | 2 | No | naive, thresh |
| ece→d1 | 5 | **Yes** | naive, diff, thresh, pg_fwd, ty |
| ece→d2 | 5 | **Yes** | naive, diff, thresh, pg_fwd, ty |
| ece→d3 | 5 | **Yes** | naive, diff, thresh, pg_fwd, ty |
| ece→mauve | 2 | No | naive, thresh |

mauve pairs 均未通过 K≥4，因 mauve 噪声大（整个序列在 0.020-0.030 波动，无单调趋势）。

### PermG directionality

- Forward: 6/8 sig（p < 0.05 after FDR）
- Reverse: 0/8 sig

单向因果关系干净，无逆向 Granger 显著。

## Regime 判断

**α=0.50 明确处于 active regime，不是 boundary。**

| Metric | α=0.25 (ref) | α=0.50 s43 (本次) | α=0.60 s42 (d080 ref) |
|--------|-------------|-------------------|----------------------|
| PermG fwd | ≈0/8 | **6/8** | 3/8 |
| Consensus K≥4 | ≈0/8 | **6/8** | 7/8 |
| d1 drift | ~low | **-29.0%** | -28.2% |
| ppl drift | ~low | **+17.2%** | +68.5% |

关键发现：
1. α=0.50 s43 的 PermG (6/8) **高于** α=0.60 s42 (3/8)。但 α=0.60 的 consensus K≥4 更高 (7/8)，因为 α=0.60 的 TY 显著率更高 (8/8 vs 5/8)，这与 C003 一致（TY 在较低 α 时 seed 不稳定）。
2. d1 drift 几乎相同（-29.0% vs -28.2%），说明 diversity 退化程度在 α=0.50-0.60 已经饱和。
3. perplexity drift 差异大（+17.2% vs +68.5%），α=0.60 的模型退化更严重。
4. step function 转折点在 **α=0.25 到 α=0.50 之间**，不在 0.50 处。α=0.50 已经充分激活了 lead-lag 信号。

等 s42/s44 完成后做 3-seed pooled 分析可进一步确认。s44 已完成（有 all_metrics.json），s42 尚未产出 all_metrics.json。

---
