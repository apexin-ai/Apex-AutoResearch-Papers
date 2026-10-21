# ops 009e completion analysis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_009e-completion-analysis_20260515T112448_result.json`
- **Structured JSON:** [`b53919ec5ed2965778df.json`](../../sessions/b5/b53919ec5ed2965778df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## Part 1: 009e 最终分析

**exp_009e_008d_walker_s1 — DONE / negative (collapse confirmed)**

| Step | eval_return | value_mean | NVE | actor_loss | actor_entropy |
|------|------------|------------|-----|------------|--------------|
| 5K | 31.00 | 0.00 | 0.000 | -0.1091 | 8.158 |
| 15K | 153.67 | 3.37 | 0.022 | -0.3367 | 0.481 |
| 25K | 167.22 | 25.86 | 0.155 | -0.1951 | -1.862 |
| 35K | 146.34 | 60.20 | 0.411 | -0.1697 | -3.465 |
| 45K | 140.76 | 97.53 | 0.693 | -0.1057 | -4.575 |
| **55K** | **82.75** | **137.88** | **1.666** | -0.0726 | -4.879 |
| 65K | 250.00 | 173.81 | 0.695 | -0.0567 | -4.492 |
| 75K | 178.06 | 189.87 | 1.066 | -0.0087 | -4.983 |
| 85K | 201.93 | 163.08 | 0.808 | 0.0109 | -4.937 |
| 95K | 132.79 | 144.82 | 1.091 | 0.0037 | -4.275 |
| **105K** | **131.08** | **135.37** | **1.033** | 0.0024 | -4.255 |

**结论**: 经典 CIVO collapse 复现。NVE@55K=1.666x 触发后，actor_loss 翻正、entropy 坍缩，性能无法恢复。最终 eval=131 vs baseline~700+。C2 collapse rate = **2/3 seeds** (008d s0 ✗, 009e s1 ✗, 009b s2 ✓自修复)，强力支持 trainable dt_emb 是 CIVO 根因。

## Part 2: plan_015B 已提交

- **exp_id**: exp_015b_frozen_dt_emb
- **PID**: 142033
- **tmux session**: exp_015b_frozen_dt_emb
- **GPU**: cuda:1 @ bjb1-45299
- **关键参数**: `--dt_emb_freeze True`（其余同 008d config）
- **预期**: 如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在

---
