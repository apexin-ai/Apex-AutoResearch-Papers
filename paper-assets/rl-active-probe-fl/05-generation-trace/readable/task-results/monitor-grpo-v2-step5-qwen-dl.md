# monitor grpo v2 step5 qwen dl

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo-v2-step5-qwen-dl_20260514T120059_result.json`
- **Structured JSON:** [`2f3e82568243362e1e86.json`](../../sessions/2f/2f3e82568243362e1e86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 任务 1: GRPO v2 训练

| 项目 | 值 |
|------|-----|
| PID 30171 | **存活**, 运行 1h03m, 状态 R |
| 进度 | **step 6/73** (~10min/step, 预计还需 ~11h) |
| GPU 0 | 93% 利用率, 28.7GB / 97.9GB |
| trainer_state.json | 不存在 |
| 输出目录 grpo_v2/ | **空**（save_steps=50, 未到） |
| tensorboard events | 无 |

**关键问题：step 5 已过但日志中无任何 reward/loss 指标。** grep "reward" 和 "loss" 均无匹配。日志中 step 5 进度条有一次清屏重置（TRL 在 logging_steps 打印指标时的行为），但指标本身没有出现在日志文件中。这可能是：
- TRL 的 logging callback 没有正确配置，指标没写到 stdout/stderr
- 或者 report_to 设为了某个不可用的后端

**暂无法判断 reward_mean 是否 > 0**，需要检查代码中 `report_to` 参数设置，或等 trainer_state.json 在首次 save 时出现。

---

### 任务 2: Qwen3-30B-A3B 下载

| 项目 | 值 |
|------|-----|
| safetensors 文件 | **16/16, 全部完成** |
| 总大小 | ~57GB |
| 最后更新 | model-00015 @ 19:54 |
| 下载进程 | **无**（正常，已完成） |

**下载已完成。** 上次检查是 14/16 @ 18:39，此后又下载了 model-00013 (19:50) 和 model-00015 (19:54)。所有 16 个 shard + tokenizer + config 均已就位。

---

### 任务 3: eval-sft-v2-ckpt

| 项目 | 值 |
|------|-----|
| PID 32728 | **存活**, 运行 42min, 状态 R |
| 进度 | **200/202** (~10s/sample) |
| GPU 1 | 67% 利用率, 17.2GB / 97.9GB |
| 输出文件 | 尚未生成（写入在评估完成后） |
| 最后日志 | 20:01:16 |

**即将完成**，剩余 2 个样本，预计 ~20s 内结束。

---
