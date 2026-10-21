# ssh full experiment check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-experiment-check_20260515T010123_result.json`
- **Structured JSON:** [`3b9da467cb31903e0e82.json`](../../sessions/3b/3b9da467cb31903e0e82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. ckpt-100 eval (pid=117635, cuda:3)
- **状态**: 运行中，已运行 1h22m
- **进度**: 51/62 batches (**82%**)，~95s/batch
- **预计剩余**: ~17 分钟完成

### 2. GRPO 训练 (pid=90080, cuda:0)
- **状态**: 运行中，已运行 5h22m
- **进度**: **186/200 steps (93%)**，~95s/step
- **最新指标** (step ~185):
  - reward: 0.281, format_reward: 0.252, f1_reward: 0.014, ced_reward: 0.015
  - clipped_ratio: 0.088, kl: 0.036
  - lr: 1.275e-6 (衰减阶段)
- **预计剩余**: ~22 分钟完成

### 3. RSFT generation (pid=122144, cuda:1)
- **状态**: 运行中，已运行 52m
- **进度**: 97/1514 batches (**6.4%**)，完成约 186/3027 docs
- **diversity 监控** (最近 100 样本):
  - format_ok_rate: **99.6%**
  - truncation_rate: **9.2%**
  - **mean_diversity: 0.9/8** — 仍然是危机级别，没有改善
- **预计剩余**: ~12-13 小时

### 4. GPU 使用情况

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | 60% | 13.6/32.6 GB | GRPO 训练 |
| 1 | 79% | 23.2/32.6 GB | RSFT 生成 |
| 2 | **0%** | **0 GB** | 空闲 |
| 3 | 79% | 11.2/32.6 GB | ckpt-100 eval |

**关键问题**: RSFT diversity 仍然是 0.9/8，8 个 generation 中平均只有 0.9 个不同输出，基本上都是重复的。这个问题从上次检查到现在没有改善，生成的数据质量堪忧。

---
