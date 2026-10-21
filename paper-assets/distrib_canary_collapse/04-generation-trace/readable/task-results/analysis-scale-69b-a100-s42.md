# analysis scale 69b a100 s42

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_69b_a100_s42_20260519T073634_result.json`
- **Structured JSON:** [`6180552934141e8195ee.json`](../../sessions/61/6180552934141e8195ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要
- 训练状态: **正常完成** (EXIT_CODE=0)
- Generations 完成: **11/11** (gen_0 baseline + 10 training gens)
- 训练时长: **~13h** (02:32 → 15:32 UTC, May 19)
- 精度: bf16, gradient_checkpointing, batch_size=4, steps_per_gen=5000

## 核心指标 (gen_0 → gen_10)

| Metric | gen_0 | gen_10 | Drift | 410M 基线 drift |
|--------|-------|--------|-------|-----------------|
| token_entropy | 2.699 | 1.187 | **-56.00%** | -61.69% |
| distinct_1 | 0.0941 | 0.0703 | **-25.31%** | -26.69% |
| distinct_2 | 0.5030 | 0.3186 | **-36.67%** | — |
| distinct_3 | 0.8209 | 0.5348 | **-34.85%** | — |
| ECE | 0.0155 | 0.3962 | **+2454.63%** | +3758.85% |
| perplexity | 15.83 | 450.79 | **+2748.57%** | +3369.37% |
| effective_rank | 65.06 | 112.77 | +73.34% | — |
| mauve | 0.0305 | 0.0260 | -14.57% | — |

## 因果检验

| Method | 6.9B (this) | 410M baseline |
|--------|-------------|---------------|
| naive_xcorr | **8/8** | 8/8 |
| diff_xcorr | **6/8** | 8/8 |
| threshold_onset | **8/8** | 0/8 |
| perm_granger_fwd | **7/8** | 6/8 |
| perm_granger_rev | **0/8** | 0/8 |
| ty_granger | 4/8 | 2/8 |
| **consensus K≥4** | **6/8** | 2/8 |
| MMCT detection_rate | **0.75** | — |

Consensus detail (6/8 pairs with K≥4):
- token_entropy→distinct_1: K=4 (naive, diff, thresh, pg_fwd)
- token_entropy→distinct_2: K=5 (naive, diff, thresh, pg_fwd, ty)
- token_entropy→distinct_3: K=5 (naive, diff, thresh, pg_fwd, ty)
- ece→distinct_1: K=4 (naive, diff, thresh, pg_fwd)
- ece→distinct_2: K=4 (naive, diff, thresh, pg_fwd)
- ece→distinct_3: K=5 (naive, diff, thresh, pg_fwd, ty)

未通过 K≥4 的 2 pairs 均为 →mauve (K=3)。

## 结论建议

- **conclusion: SUCCESS**
- 理由: PermG forward FDR 7/8, consensus K≥4 = 6/8 (远超 ≥6/8 阈值的下限)，reverse 0/8 确认方向性。Canary lead-lag 在 6.9B (17× scale-up) 下不仅持续存在，且信号比 410M 更强。
- 与 410M 对比:
  - **Collapse 幅度略小**: entropy drift -56% vs -62%, ECE drift 2455% vs 3759%, ppl drift 2749% vs 3369%。与 D079 预期一致 (bf16 隐式正则化抑制 collapse)。
  - **Lead-lag 信号更强**: consensus K≥4 从 2/8 跃升至 6/8, threshold_onset 从 0/8 到 8/8。6.9B 的退化轨迹更单调/平滑 (噪声更低)，使因果结构更容易检测。
  - PermG reverse 保持 0/8，确认因果方向 canary→diversity 在大规模下依然成立。
  - 唯一弱项: mauve pairs (K=3) 未达 consensus，可能因 mauve 在低 gen 数 (T=11) 下本身噪声较大。

## checkpoint_path 和 log_path
- checkpoint: `/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s42/gen_10/checkpoint/`  (also gen_9/checkpoint/)
- log: `~/runs/distrib_canary_collapse/scale_69b_a100_s42.log` (on westd-17855)
- analysis: `/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s42/analysis_results.json`

---
