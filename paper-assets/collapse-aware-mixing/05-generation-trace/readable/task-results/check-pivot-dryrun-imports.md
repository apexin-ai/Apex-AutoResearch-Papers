# check pivot dryrun imports

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pivot_dryrun_imports_20260513T184424_result.json`
- **Structured JSON:** [`adaf9b6639f7046e6e8a.json`](../../sessions/ad/adaf9b6639f7046e6e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

```
=== IMPORT CHECK ===
1. analyze_generated_eff_rank: OK
2. compare_eff_rank_vs_ngram: OK
3. analyze_layer_eff_rank: OK (加载慢 ~23s，torch 初始化)
4. analyze_ngram_leading: OK

=== PATH CHECK ===
G2 checkpoints: checkpoint-76, checkpoint-152, checkpoint-228, checkpoint-304, checkpoint-305
G1 synth data: /root/autodl-tmp/output_v7/G1/synth_data/ (data-00000-of-00001.arrow, 52.5MB)
pivot_b_analysis dir: ready

=== G2 EVAL ===
Status: DONE (进程 93514 已退出)
Progress: pipeline 完成，VERDICT = EXTEND
  - G0 baseline: rank=677.6 ±1.01, ppl=13.27
  - First rank drop (≥1σ): NOT DETECTED
  - First PPL rise (significant): NOT DETECTED
  - KL divergence: 0.6182 (95% CI [0.607, 0.832]), threshold 0.1: PASS
  - 结论: neither spectral rank nor PPL moved in 2 generations

=== G2 METRICS ===
6 条记录 (5 checkpoints + final_model)，关键趋势：

| checkpoint | step | eff_rank | ppl    | KL_unigram |
|------------|------|----------|--------|------------|
| ckpt-76    | 76   | 680.09   | 13.521 | 0.618      |
| ckpt-152   | 152  | 682.81   | 13.576 | 0.618      |
| ckpt-228   | 228  | 683.38   | 13.589 | 0.618      |
| ckpt-304   | 304  | 683.38   | 13.589 | 0.618      |
| ckpt-305   | 305  | 683.44   | 13.590 | 0.618      |
| final      | 305  | 683.44   | 13.590 | 0.618      |

⚠️ 注意：所有 checkpoint 的 n-gram 指标完全退化 — `unique_tokens=1`, `vocab_coverage≈2e-5`, 所有 n-gram entropy=0。合成数据生成可能只产生了单一 token 的重复序列（total_tokens=3968, unique=1）。KL 值在所有 checkpoint 间完全相同，说明 n-gram 指标是在同一份合成数据上计算的，没有 per-checkpoint 重新生成。

---
