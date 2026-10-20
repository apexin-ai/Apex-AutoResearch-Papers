# experiment v3b check results

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_v3b_check_results_20260513T171803_result.json`
- **Structured JSON:** [`db182930e14c3421368e.json`](../../sessions/db/db182930e14c3421368e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

---

## MVP v3b 实验报告

### 1. 实验状态

| 实验 | 状态 | 退出码 | 运行时间 |
|------|------|--------|----------|
| mvp_v3b_cr70 (cuda:0) | **已完成** | 0 | ~14m26s |
| mvp_v3b_cr85 (cuda:1) | **已完成** | 0 | ~15m42s |

⚠️ **数据问题**：两个实验写入同一 `eval/results.csv`，CR85 覆盖了 CR70 的结果文件。CR70 日志确认也输出 `MVP Verdict: KILL`。

### 2. CR 0.85 三方对比（overall, 65 traces）

| Method | KIRR | PPL |
|--------|------|-----|
| Full (无压缩) | **100.0%** | 19.99 |
| Uniform EA (baseline) | **40.3%** | 24.72 |
| Pure Structural | **0.0%** | 41.72 |
| **TurnKV** (ea + 0.1×offset) | **35.8%** | 25.58 |

| 指标 | 值 | Pass 标准 | 结果 |
|------|----|-----------|------|
| KIRR diff (TurnKV - EA) | **-4.5 pp** | ≥ 10pp | ❌ |
| TurnKV KIRR | **35.8%** | ≥ 90% | ❌ |
| PPL ratio | **1.035** | ≤ 1.02 | ❌ |

分 case type：
- **Standard traces**: KIRR diff = -4.2pp, PPL ratio = 1.031
- **Adversarial traces**: KIRR diff = -5.0pp, PPL ratio = 1.045

### 3. MVP Verdict: **KILL**

TurnKV 在所有维度上**劣于** Uniform EA baseline：
- KIRR 更低（-4.5pp），说明加法偏置不仅没帮助，反而干扰了 EA score 的排序
- PPL 更高（1.035×），质量也更差
- Pure structural 得到 0% KIRR，说明结构先验本身完全无效，加上去只会添噪声

两个 CR 的日志都输出 `MVP Verdict: KILL`。D007 additive bias 方向 definitive KILL。

### 4. Registry 更新

- `mvp_v3b_cr85`: DONE, negative, metrics 已写入
- `mvp_v3b_cr70`: DONE, negative, 标注 results 被覆盖

---
