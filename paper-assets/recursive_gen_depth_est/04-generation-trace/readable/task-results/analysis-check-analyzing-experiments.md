# analysis check analyzing experiments

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_analyzing_experiments_20260522T033036_result.json`
- **Structured JSON:** [`07be72bfb6ae0724f529.json`](../../sessions/07/07be72bfb6ae0724f529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the results:

---

## 1. accum_pythia_nuc_mix50

**Status: STILL RUNNING** (PID 907272, ~1h20m elapsed)

当前进度：Phase 2c — 生成 d2 文本中 (2479/5000 samples written)

已完成的阶段：
- Phase 1: d1 生成完成 (5000 samples, 51.7min)
- Phase 2a: 混合数据完成 (2500 human + 2500 synthetic)
- Phase 2b: LoRA d2 训练完成 (train_loss=1.668, 3 epochs, 7m42s)
- Phase 2c: d2 生成进行中 (~50%)

**无 summary.json**。后续还需完成 d2 生成、可能的 d3/d4 phases、特征提取和分类。**不可更新 registry。**

---

## 2. conditional_pi_001 + conditional_pi_002

**Status: 8/9 cells 完成, 最后 1 cell 运行中**

### conditional_pi_001 (May 21, 已完成 7/9 cells)
已完成: pythia_nucleus, pythia_temp09, pythia_topk50, olmo_nucleus, olmo_temp09, olmo_topk50, gpt2xl_nucleus

### conditional_pi_002 (May 22, 补跑剩余 2 cells)
- **gpt2xl_temp09**: 完成 (3861s)。6 个 inf 值被 clip 到 float32 范围。
- **gpt2xl_topk50**: 运行中，bootstrap 100/1000 (截至 11:27)。预计 ~12:30 完成。

### 关键结果 — Top Features (跨 cell 一致)

| Rank | Feature | Importance (range) | Bootstrap stability |
|------|---------|-------------------|---------------------|
| 1 | **var_surprisal** | 0.28–0.38 | rank_std=0.0 (locked) |
| 2 | **p90_ppl** | 0.07–0.17 | rank_std≈0 |
| 3 | **p75_ppl** | 0.02–0.07 | rank_std<1.0 |
| 4 | **p50_ppl** | 0.01–0.04 | rank_std<1.0 |
| 5 | varies (p25_ppl/mean_ppl/trigram_entropy) | — | — |

**例外**: gpt2xl_temp09 中 p90_ppl (imp=0.419) 超过 var_surprisal (imp=0.093)，排名反转。

### 缺失
- gpt2xl_topk50 的 PI 和 bootstrap 结果（运行中）
- per_cell_pi.json / bootstrap_ranks.json 目前只含 7 cells，需要 conditional_pi_002 完成后 merge 9 cells 的完整结果

---

**结论**: 两个实验均未完成。accum_pythia_nuc_mix50 大约还需 1-2 小时；conditional_pi 的最后一个 cell (gpt2xl_topk50) 约 1 小时后完成。建议 ~12:30 后复查。

---
