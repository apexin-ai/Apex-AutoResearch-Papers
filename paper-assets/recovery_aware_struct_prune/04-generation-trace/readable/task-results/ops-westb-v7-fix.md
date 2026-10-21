# ops westb v7 fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-v7-fix_20260515T142306_result.json`
- **Structured JSON:** [`c024df413c092a0301f8.json`](../../sessions/c0/c024df413c092a0301f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Standard v7 正在训练中。GPU 1 已升至 39GB / 100% / 590W / 65°C。

---

## 最终报告

### Standard v7 (GPU 1) — 已成功启动
| 字段 | 值 |
|------|-----|
| PID | 532557 |
| GPU | cuda:1 (CUDA_VISIBLE_DEVICES=1, --gpu 0) |
| model_path | `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20` (无 final 子目录) |
| output_dir | `grpo_stage2_standard_20_v7` |
| 训练样本 | 7473 (完整 GSM8K) |
| 总 steps | 5604 |
| 当前进度 | Step 0/5604 (刚启动，第一个 step 正在跑) |
| WandB | `grpo_stage2_standard_20_v7`, run ID `45u85way` |
| 超参 | beta=0.01, loss_type=dapo, format_reward=0.1, temp=0.4, rep_penalty=1.15, optim=adamw_8bit, lr=1e-6 |
| 显存 | 39.3GB / 97.9GB |
| GPU util | 100%, 590W, 65°C |

### RASP v7 (GPU 0) — 未在运行
- 原始在 GPU 0 上的两个进程是 **dryrun**（`--max_steps 1 --output_dir /tmp/grpo_v7_dryrun`），不是真正的 RASP v7。
- 另一个 agent 曾短暂启动 RASP v7（PID 530945），但被 SIGHUP 终止（EXIT_CODE=129）。
- 目前 GPU 0 上跑的是另一个 agent 启动的 **RASP v8**（PID 532861, `grpo_rasp_20_v8`），仍在加载阶段（12.5GB, 0% util）。

### nvidia-smi 最终状态
```
GPU 0: 12,497MiB / 97,887MiB  |  0% util  |  RASP v8 (PID 532861, 另一个 agent)
GPU 1: 39,331MiB / 97,887MiB  | 100% util  |  Standard v7 (PID 532557, 本次启动)
```

### 遇到的问题
1. **sft_standard_20/final 不存在** — 模型直接在 `sft_standard_20/` 下
2. **首次启动 ENOSPC 崩溃** — HF 锁文件写根分区失败，改为 `HF_HOME=/root/autodl-tmp/.hf_cache` 后解决
3. **SIGHUP 批量杀进程** — 另一个 agent 启动的 v7 进程（RASP + Standard）均被 SIGHUP 终止

---
