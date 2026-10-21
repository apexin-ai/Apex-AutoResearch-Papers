# diagnose gpu process check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-process-check_20260516T035023_result.json`
- **Structured JSON:** [`17f9c4a2cb5c271d067a.json`](../../sessions/17/17f9c4a2cb5c271d067a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### sweep-isr-b005-s42 — 已完成，无需恢复

- **实际状态**: 正常完成 (EXIT_CODE=0)，于 `2026-05-16T03:50:36Z` 退出
- **训练进度**: 500/500 steps (100%)
- **最终指标**: prove_rate=0.888, mean_isr=0.577
- **输出**: `/root/autodl-tmp/outputs/sweep_isr_b005_s42/` — 完整模型已保存 (~15GB, 4 shards) + checkpoint-500
- **tmux**: 已退出，无残留进程
- **结论**: Registry 标记 killed 是错误的。实验已成功完成，建议更新 registry 为 `conclusion=success`

---

### sweep-isr-b01-s45 — 正在运行，有效训练

| 项目 | 值 |
|------|-----|
| PID | 604569 |
| 启动时间 | 11:21 (今天，约30分钟前) |
| 当前 step | 177/500 (35%) |
| GPU | GPU 0, 79.5GB/97.9GB, 93% 利用率 |
| CUDA_VISIBLE_DEVICES | 0 |
| 最近 reward | step 176=0.379, step 177=0.257 |
| prove_rate | ~0.25-0.375 (正在学习中) |
| step time | ~7-12s/step |
| 预计剩余 | ~40-50 min |
| wandb run | sweep-isr-b01-s45-r3 |
| config | grpo_additive_bonus_b01.yaml, β=0.1, seed=45, num_gen=4 |
| checkpoint | checkpoint-150 已保存 (15GB) |

- **结论**: 有效运行，step 在增长，reward/loss 在变化。建议恢复 registry 为 `RUNNING`

---

### 环境概况
- 磁盘: 152G/250G (61%)，99G 可用 — 充足
- GPU 1: 空闲 (0MiB, 0%)

---
