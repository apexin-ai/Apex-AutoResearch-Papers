# infra status check and act

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_status-check-and-act_20260514T133359_result.json`
- **Structured JSON:** [`0512a20e185880caba50.json`](../../sessions/05/0512a20e185880caba50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## MVP 实验状态报告

### 状态：rep_42, rep_43 均已完成 | rep_44 正在训练

- **rep_42**: 11 代完成, EXIT_CODE=0 (May 14 20:15)
- **rep_43**: 11 代完成, EXIT_CODE=0 (May 14 20:13)  
- **rep_44**: PID 30672, CUDA:0, 正在 gen_0 初始化阶段（生成合成数据中）
- **GPU**: 双卡 97GB (A100-80G×2), rep44 启动前两卡空闲

---

### 每代关键指标

#### rep_42

| gen | token_entropy | ECE | self_bleu | distinct_2 | perplexity | eff_rank | mauve |
|-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 3.234 | 0.011 | 0.010 | 0.518 | 26.9 | 46.6 | 0.034 |
| 1 | 1.908 | 0.204 | 0.010 | 0.514 | 55.9 | 79.6 | 0.032 |
| 2 | 1.480 | 0.323 | 0.011 | 0.428 | 160.4 | 95.4 | 0.031 |
| 3 | 1.380 | 0.358 | 0.012 | 0.390 | 281.6 | 90.0 | 0.036 |
| 4 | 1.331 | 0.377 | 0.013 | 0.366 | 394.1 | 88.3 | 0.031 |
| 5 | 1.306 | 0.390 | 0.013 | 0.356 | 486.5 | 88.8 | 0.031 |
| 6 | 1.302 | 0.397 | 0.013 | 0.349 | 586.8 | 91.1 | 0.028 |
| 7 | 1.296 | 0.402 | 0.013 | 0.340 | 694.6 | 91.7 | 0.031 |
| 8 | 1.319 | 0.403 | 0.014 | 0.339 | 786.3 | 90.8 | 0.029 |
| 9 | 1.264 | 0.416 | 0.013 | 0.337 | 917.6 | 88.4 | 0.031 |
| 10 | 1.276 | 0.417 | 0.013 | 0.335 | 1003.7 | 96.2 | 0.030 |

#### rep_43

| gen | token_entropy | ECE | self_bleu | distinct_2 | perplexity | eff_rank | mauve |
|-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 3.234 | 0.011 | 0.011 | 0.513 | 26.9 | 46.6 | 0.034 |
| 1 | 1.909 | 0.205 | 0.011 | 0.518 | 55.5 | 78.4 | 0.030 |
| 2 | 1.466 | 0.322 | 0.012 | 0.428 | 158.7 | 94.3 | 0.034 |
| 3 | 1.325 | 0.361 | 0.012 | 0.385 | 279.7 | 99.3 | 0.033 |
| 4 | 1.280 | 0.382 | 0.012 | 0.365 | 395.1 | 102.1 | 0.031 |
| 5 | 1.269 | 0.394 | 0.012 | 0.354 | 502.0 | 81.1 | 0.030 |
| 6 | 1.252 | 0.402 | 0.013 | 0.346 | 608.7 | 80.1 | 0.032 |
| 7 | 1.255 | 0.407 | 0.014 | 0.339 | 696.0 | 87.8 | 0.031 |
| 8 | 1.257 | 0.412 | 0.013 | 0.334 | 815.9 | 84.3 | 0.029 |
| 9 | 1.250 | 0.418 | 0.013 | 0.332 | 909.4 | 82.1 | 0.028 |
| 10 | 1.260 | 0.420 | 0.014 | 0.330 | 1014.7 | 82.2 | 0.032 |

---

### analyze_mvp.py 完整结果

**Verdict: STRONG PASS**

> 2 canary families (ece, token_entropy) each have >= 1 SIGNIFICANT LEAD pair.

**前处理结果**:
- MAUVE: demoted to supplementary (floor_effect — Gen 0 < 0.10)
- effective_rank: inconclusive (slopes 方向不一致: seed 42: +0.81, seed 43: -1.90)

**Significant Lead Pairs (6 对)**:

| canary | downstream | mean_lag | lag_std | seed 42 (|r|, p) | seed 43 (|r|, p) |
|--------|-----------|:---:|:---:|:---:|:---:|
| token_entropy | distinct_1 | -1.0 | 0.0 | 0.993, p=0.0036 | 0.994, p=0.0028 |
| token_entropy | distinct_2 | -1.0 | 0.0 | 0.968, p=0.0231 | 0.970, p=0.0197 |
| token_entropy | distinct_3 | -3.0 | 2.0 | 0.953, p=0.0224 | 0.941, p=0.0392 |
| ece | distinct_1 | -2.0 | 0.0 | 0.998, p=0.0000 | 0.995, p=0.0000 |
| ece | distinct_2 | -1.0 | 0.0 | 0.996, p=0.0005 | 0.997, p=0.0001 |
| ece | distinct_3 | -3.0 | 2.0 | 0.991, p=0.0008 | 0.987, p=0.0013 |

**Weak Lead Pairs (1 对)**:
- token_entropy → perplexity: mean_lag=-5.0, lag_std=0.0 (p=0.12/0.08, 未过 0.05 阈值)

**No Lead Pairs (9 对)**: self_bleu 全部 NO LEAD（lag 方向不一致），effective_rank 全部 NO LEAD/WEAK（相关性弱且方向不一致）

**产出文件**: `results/mvp/analysis/` 下的 `metric_trends.png`, `cross_correlation.png`, `lead_time_table.csv`, `analysis_summary.json`

---

### rep_44 训练状态

- PID: **30672**
- GPU: CUDA:0
- 当前阶段: gen_0 数据生成（padding_side warning 是正常的）
- 日志: `~/runs/distrib_canary_collapse/mvp_v4_rep44.log`

---
