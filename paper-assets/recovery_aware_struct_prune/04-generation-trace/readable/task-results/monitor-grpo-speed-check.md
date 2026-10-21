# monitor grpo speed check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo_speed_check_20260516T125158_result.json`
- **Structured JSON:** [`8035f8029d6493778171.json`](../../sessions/80/8035f8029d6493778171.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 20% GRPO 实验（已修复，重启为 v2）

注意：这两个是**重启后的 v2 runs**，wandb ID 已变更。

| 实验 | GPU | 当前 step | 步速 | GPU 利用率 | 显存占用 |
|------|-----|----------|------|-----------|---------|
| grpo_rasp_qwen_math_v2 | cuda:0 | 9/100 | **~27s/step** | 99% | 57.7/95.6 GB |
| grpo_standard_qwen_math_v2 | cuda:1 | 8/100 | **~27s/step** | 93% | 58.6/95.6 GB |

**EOS 修复生效确认**：日志显示 `generation_config.eos_token_id: [151643, 151645]`，步速从 ~7min/step 降到 **~27s/step**，提速 **15x**。

Step 5 有 checkpoint 保存，导致 step 6 耗时偏高（~36-40s），之后逐步恢复。正常步速稳定在 26-28s。

新 wandb:
- rasp: `2sgy2m1a` (run name: grpo_rasp_qwen_math_v2)
- standard: `iq8nkk1p` (run name: grpo_standard_qwen_math_v2)

### 25% GRPO 实验

| 实验 | GPU | 状态 | GPU 利用率 | 显存占用 |
|------|-----|------|-----------|---------|
| grpo_rasp_25_qwen_math | cuda:2 | **仍在加载模型** | 0% | 3 MiB |
| grpo_standard_25_qwen_math | cuda:3 | **仍在加载模型** | 0% | 3 MiB |

25% 实验日志各只有 2 行（模型加载开始于 20:51:37），GPU 显存几乎为零。模型还在 CPU 加载阶段，尚未传到 GPU。这两个刚启动不久，需要等几分钟让模型加载完成后再确认是否正常训练。

### 异常

无 OOM、无 collapse 迹象、无报错。20% 实验运行健康。25% 实验需要再过几分钟确认是否成功进入训练。

---
