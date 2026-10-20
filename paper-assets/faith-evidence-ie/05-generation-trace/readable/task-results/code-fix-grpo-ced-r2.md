# code fix grpo ced r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_grpo_ced_r2_20260514T102736_result.json`
- **Structured JSON:** [`7540e1170fa0456e54d5.json`](../../sessions/75/7540e1170fa0456e54d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 诊断修复报告

### 1. GPU 释放状态
r1 训练进程（PID 24291-24294）kill 时仍在运行，手动 kill 后 4x RTX 5090 全部释放（0 MiB）。

### 2. 三个问题诊断与修复

| 问题 | 之前配置 | 修改后 |
|------|---------|--------|
| **(A) 无 checkpoint** | `save_strategy="epoch"`, `save_total_limit=2` 硬编码 | 新增 `--save_steps`, `--save_total_limit`, `--save_strategy` CLI 参数；传 `--save_steps N` 时自动切换为 steps 策略 |
| **(B) reward 权重失衡** | `reward_fns = [format, f1, ced]` 等权求和 | 新增 `WeightedRewardFn` wrapper + `--format_reward_weight`/`--f1_reward_weight`/`--ced_reward_weight` CLI 参数 |
| **(C) clip_ratio=0** | `num_iterations` 未设（默认 1），无 KL 控制 | 新增 `--num_iterations`（建议 2）、`--kl_coef`（映射到 GRPOConfig beta）、`--max_steps` CLI 参数 |

### 3. Dry-run 结果 (max_steps=2, num_iterations=2)

| 指标 | 值 |
|------|-----|
| format_reward (weighted) | 0.03 (raw=0.1 × w=0.3) |
| f1_reward | 0.0 |
| ced_reward | 0.0 |
| total reward | 0.03 |
| reward_std | 0.0 |
| clip_ratio | 0.0 (zero advantage → no clip) |
| completions/clipped_ratio | 1.0 (全部触达 1024 max length) |
| checkpoint 保存 | checkpoint-1, checkpoint-2 ✅ |
| OOM | 无 ✅ |

> clip_ratio=0 在 dry-run 中是预期的：所有 4 个 generation 得到相同 reward → advantage=0 → 无梯度 → ratio=1。正式训练中模型已经过 SFT 微调，输出质量更高且有差异，clip_ratio 将非零。

### 4. 两方案配置对比

| 参数 | 保守方案 | 激进方案 |
|------|---------|---------|
| learning_rate | 2e-5 | 5e-5 |
| num_iterations | 2 | 2 |
| kl_coef | 0 (不用) | 0.05 |
| cliprange | 0.2 (TRL 默认) | 0.2 |
| save_steps | 10 | 10 |
| save_total_limit | 5 | 5 |
| format_reward_weight | 0.3 | 0.3 |
| f1_reward_weight | 2.0 | 2.0 |
| ced_reward_weight | 0.5 | 0.5 |
| gradient_accumulation_steps | 16 | 16 |

---
