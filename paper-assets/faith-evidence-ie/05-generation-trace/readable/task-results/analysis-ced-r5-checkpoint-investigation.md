# analysis ced r5 checkpoint investigation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ced-r5-checkpoint-investigation_20260514T150138_result.json`
- **Structured JSON:** [`2c62247db1d7d64d3376.json`](../../sessions/2c/2c62247db1d7d64d3376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，汇报如下。

---

## ced_r5 调查结果

### 现存 checkpoint
| checkpoint | step |
|---|---|
| checkpoint-440 | 440 |
| checkpoint-460 | 460 |
| checkpoint-480 | 480 |
| checkpoint-500 | 500 |
| checkpoint-520 | 520 |

`save_steps=20`, `save_total_limit=5`（从存活 checkpoint 数量推断）。

### f1_reward 时间线（关键转折）

| step | f1_reward | 备注 |
|---|---|---|
| 5 | 0.0681 | 初始 |
| 20 | **0.2453** | 早期峰值 |
| 30 | 0.0577 | 最后一个 > 0.01 的 step |
| **35** | **0.0000** | **首次归零** |
| 40 | 0.0039 | 短暂微弱回升 |
| **45** | **0.0000** | **永久归零起点** |
| 45–520 | 0.0000 | 全部为零，无例外 |

**Collapse 时间线**：
- **step 35**：f1 首次 = 0
- **step 45**：f1 永久归零
- **step 170**：completion 长度坍缩到 ~34 tokens 并锁死
- **step 220+**：entropy 降至 < 0.001，grad_norm 几乎全为 0，模型完全停止学习

### "最后正常" checkpoint 是否存在

**不存在。** f1 最后 > 0 在 step 40，而现存最早的 checkpoint 是 step 440 — 已经在 collapse 后 400 步了。save_total_limit=5 导致早期 checkpoint 全部被覆盖。无法恢复到 collapse 前的状态。

---

## extract_r3 健康状况

**未发生 mode collapse。** 具体指标：

| 指标 | 状态 |
|---|---|
| f1_reward | 正常波动，0.02–0.49 范围，最近 step 505=0.47, step 520=0.35 |
| completion length | 稳定 ~43 tokens，未坍缩 |
| entropy | 低但非零（0.005–0.025） |
| grad_norm | **大部分 step 为 0**，偶尔脉冲式出现（step 265=2.15, step 415=1.69） |

**grad_norm 多数为 0 的解释**：模型已经收敛到一个较稳定的策略，大部分 batch 的梯度被 clip 或接近零，但偶尔遇到 informative 样本时仍能产生梯度更新。f1 在 step 300+ 有上升趋势（多次达到 0.3+），说明模型仍在缓慢学习。**不需要干预，但值得持续监控。**

---
