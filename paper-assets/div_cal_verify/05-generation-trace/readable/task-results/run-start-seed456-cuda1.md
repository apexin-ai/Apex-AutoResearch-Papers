# run start seed456 cuda1

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_start_seed456_cuda1_20260514T065135_result.json`
- **Structured JSON:** [`a29d1730193ff62fbba5.json`](../../sessions/a2/a29d1730193ff62fbba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## RGDS seed=123 完整 Metrics (gen 0→7)

| Gen | PPL | RankMe | KNN | Rare Ngram | Rank Corr |
|-----|-----|--------|-----|------------|-----------|
| 0 | 26.32 | 365.65 | 0.988 | 0.0343 | 0.0301 |
| 1 | 33.72 | 396.58 | 0.988 | 0.0285 | 0.0135 |
| 2 | 43.58 | 416.12 | 0.988 | 0.0224 | 0.0148 |
| 3 | 51.80 | 422.63 | 0.988 | 0.0194 | -0.0004 |
| 4 | 57.08 | 422.85 | 0.988 | 0.0183 | -0.0109 |
| 5 | 69.28 | 426.34 | 0.988 | 0.0171 | -0.0089 |
| 6 | 77.57 | 428.93 | 0.988 | 0.0162 | -0.0274 |
| 7 | 90.25 | 431.19 | 0.988 | 0.0149 | -0.0170 |

PPL 从 26.3→90.3 持续退化，rankme 单调上升（365→431），rare ngram 持续下降，rank corr 基本为 0（无显著相关）。KNN 恒定 0.988。Registry 已更新为 DONE。

## external_seed456 启动状态

- **已成功启动** — tmux session `medium_external_seed456`
- PID 462871, cuda:1, **19250MiB** 显存, **98% util**, 551W, 65C
- 正在 gen_0 合成数据生成阶段
- Registry 已更新为 RUNNING

## random50_seed123 (cuda:0) 当前进度

- PID 453372, cuda:0, 22460MiB, 67% util
- **正在 gen 2/7** — 训练阶段 (step 3/5)
- gen 1 已完成：PPL=33.54, RankMe=399.19, KNN=0.988, Rare=0.0298

---
