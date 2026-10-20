# ops check and submit exp026

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-submit-exp026_20260525T231603_result.json`
- **Structured JSON:** [`b29b8bbe71dc2b4bddcd.json`](../../sessions/b2/b29b8bbe71dc2b4bddcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇报如下：

---

## 汇报

### 1. PID 3923 状态
**已完成。** 脚本 `fast_r02_regen_and_ews.py` 运行了约 80 分钟（10 代 × ~450-700s/代），正常退出。

### 2. EWS r=0.2 结果文件

输出文件：`/root/spectral_collapse_ews/results/alternative_ews_v2_r02.json`（完整 11 代数据）

| Gen | RankMe | tok_ent | iso | PPL | ppl_growth | stable_rank(attn) | stable_rank(ffn) | slv_log_det |
|-----|--------|---------|-----|-----|------------|-------------------|------------------|-------------|
| 0 | 734.3 | 6.764 | 0.314 | 9.55 | 0.00 | 69.39 | 90.31 | 2366.7 |
| 1 | 746.6 | 6.775 | 0.159 | 10.28 | 0.73 | 69.44 | 90.38 | 2367.5 |
| 2 | 753.6 | 6.792 | 0.121 | 10.74 | 0.46 | 69.47 | 90.42 | 2358.3 |
| 3 | 759.1 | 6.771 | 0.104 | 11.14 | 0.40 | 69.49 | 90.47 | 2362.5 |
| 4 | 764.1 | 6.770 | 0.080 | 11.51 | 0.37 | 69.52 | 90.51 | 2379.2 |
| 5 | 762.6 | 6.723 | 0.074 | 11.83 | 0.32 | 69.53 | 90.55 | 2398.9 |
| 6 | 760.0 | 6.730 | 0.075 | 12.19 | 0.36 | 69.56 | 90.60 | 2429.8 |
| 7 | 759.1 | 6.709 | 0.069 | 12.54 | 0.35 | 69.59 | 90.66 | 2436.3 |
| 8 | 759.3 | 6.752 | 0.057 | 12.96 | 0.42 | 69.63 | 90.71 | 2454.3 |
| 9 | 758.9 | 6.725 | 0.058 | 13.39 | 0.43 | 69.66 | 90.75 | 2463.1 |
| 10 | 756.4 | 6.713 | 0.058 | 13.83 | 0.44 | 69.70 | 90.81 | 2479.7 |

### 3. GPU 状态
| GPU | Memory Used | Utilization |
|-----|-------------|-------------|
| cuda:0 | 19349 MiB | 70% |
| **cuda:1** | **0 MiB** | **0%** |

**cuda:1 完全可用**（0 MiB 占用，0% 利用率）。

### 4. 关键观察
- PPL 从 9.55 → 13.83，稳定增长（符合 model collapse 预期但增速较慢，r=0.2 有 20% 真实数据缓冲）
- isotropy 从 0.314 → 0.058 大幅下降（early warning 信号）
- RankMe 先升后降（734 → 764 → 756），在 Gen 4 达峰后缓慢下降
- stable_rank 单调缓增，sigma1 单调缓降
- slv_log_det 从 2366 → 2479 持续增长

---
