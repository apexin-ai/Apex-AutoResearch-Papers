# analyze alpha sweep a025 s44 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_alpha_sweep_a025_s44_fp32_20260519T114354_result.json`
- **Structured JSON:** [`ea76940f70f45ce5e4af.json`](../../sessions/ea/ea76940f70f45ce5e4af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，尚未完成。**

## 当前状态

- **进度**: gen_4/10 训练中，step ~960/5000
- **已完成**: gen_0 ~ gen_3（4/10 generations）
- **启动时间**: 2026-05-19 17:53 (CST)
- **W&B**: 无（未集成）
- **ETA**: 约 90 min（gen_4 剩余 ~9 min + gen_5-9 各 ~15 min + 最终分析）

## 已完成 generation 的逐代指标

| Gen | token_entropy | distinct_1 | perplexity | eff_rank | mauve |
|-----|:---:|:---:|:---:|:---:|:---:|
| 0 (baseline) | 3.2342 | 0.0974 | 26.95 | 46.6 | 0.0324 |
| 1 | 2.9831 | 0.0980 | 19.24 | 48.7 | 0.0341 |
| 2 | 3.0307 | 0.0817 | 20.23 | 50.7 | 0.0332 |
| 3 | 3.0265 | 0.0730 | 20.80 | 51.2 | 0.0325 |

## 初步观察

- **d1_drift (gen0→gen3)**: -25.1%（0.0974 → 0.0730），已有明显下降趋势
- **token_entropy**: gen0→gen1 下降 7.8%（3.234→2.983），之后回升并稳定在 ~3.03
- **perplexity**: gen0 到 gen1 大幅下降（26.95→19.24），之后缓慢上升
- **eff_rank**: 持续上升（46.6→51.2），与其他 α=0.25 seed 趋势一致

## PermG / K≥4 / MMCT

**尚不可用**。这些分析指标需要 10 个 generation 全部完成后才计算。结果目录中无 `all_metrics.json` 或分析文件。

---

需要等实验跑完再提取完整指标。预计约 21:15 CST 完成。

---
