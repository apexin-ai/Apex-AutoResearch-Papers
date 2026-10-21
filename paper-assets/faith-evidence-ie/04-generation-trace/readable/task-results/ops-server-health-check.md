# ops server health check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-health-check_20260514T224531_result.json`
- **Structured JSON:** [`9edb0b46eff8cf3e76e5.json`](../../sessions/9e/9edb0b46eff8cf3e76e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程存活

| PID | 任务 | 状态 | GPU | 显存 |
|-----|------|------|-----|------|
| 90080 | 训练 grpo_ced_lr5e6_r1 | **ALIVE** | GPU 0 | 13.6 GB |
| 108025 | ckpt-60 eval 原版 | **DEAD** | — | — |
| 108185 | ckpt-60 eval r2 | **ALIVE** | GPU 1 | 9.7 GB |
| 101842 | ckpt-40 eval r2 | **ALIVE** | GPU 2 | 10.6 GB |
| 104979 | SFT baseline eval | **ALIVE** | GPU 3 | 9.7 GB |

### GPU 占用（4× RTX 5090 32GB each）

- **GPU 0**: 训练进程 (13.6/32 GB)
- **GPU 1**: ckpt-60 eval r2 (9.7/32 GB)
- **GPU 2**: ckpt-40 eval r2 (10.6/32 GB)
- **GPU 3**: SFT baseline eval (9.7/32 GB)

### 训练进度

- **Step 101/200** (50.5%)，已运行 3h06m
- 速度 ~100-110 s/step，剩余 99 步 → 预计还需 **~2h45m**（约 UTC 09:30 完成）
- 最新 checkpoint: **checkpoint-100**（06:43 UTC 保存）
- KL divergence 警告：step 5 时爆到 2.4B，step 30 到 70T，step 85 到 14M，step 90 回落到 685。当前 KL 在 0.007 左右，正常范围
- Reward 趋势：format_reward ~0.25, f1_reward ~0.016, ced_reward ~0.018, total ~0.28

### ckpt-60 eval

- **PID 108025（原版）**：已死，exit -15（被 SIGTERM 杀掉），inference 还没开始就挂了
- **PID 108185（r2）**：存活，运行 16min，当前 **10/62 batches (16%)**，~92s/batch → 剩余 52 batch ≈ **~80min**（约 UTC 08:00 完成）
- 输出目录 `grpo_ced_lr5e6_ckpt60/` 为空（还在跑）
- 注意：r2 的 output_dir 和原版不同：原版写到 `lr5e6_r1_ckpt60/checkpoint-60`，r2 直接写到 `grpo_ced_lr5e6_ckpt60/`

### ckpt-40 eval r2

- 运行 1h21m，output_dir `lr5e6_r1_ckpt40/checkpoint-40/` 仍为空（结果在完成时写入）
- 根据运行时间估算（~93-100s/batch），大约已完成 **~48/62 batches (77%)**
- 预计还需 **~23min**（约 UTC 07:10 完成）

### SFT baseline eval

- 运行 53min，output_dir `sft_baseline_eval_results/` 仍为空
- 估算已完成 **~34/62 batches (55%)**
- 预计还需 **~43min**（约 UTC 07:30 完成）

### 关键发现

1. ckpt-60 原版 eval (PID 108025) 被 SIGTERM 杀了，r2 (PID 108185) 正在正常跑，不需要修复
2. ckpt-40 原版 eval 也曾被 SIGTERM 杀过（日志显示 `exit -15`），r2 重试正在正常运行
3. 所有 4 张 GPU 都在工作，没有闲置
4. 训练的 KL 曾经爆炸过但已恢复，reward 在缓慢提升

---
