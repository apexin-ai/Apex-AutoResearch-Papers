# check d134 pipeline status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-pipeline-status_20260518T104813_result.json`
- **Structured JSON:** [`bc9cbc8c724817b26218.json`](../../sessions/bc/bc9cbc8c724817b26218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pipeline 状态汇报

**整体状态：0/10 完成，pipeline 崩溃**

Pipeline 在第一个 run（ISR seed=47）的 step 21/500 处 OOM 崩溃，后续 9 个 run 均未启动。

**崩溃原因：** `torch.OutOfMemoryError` — 4B 模型 + 当前 batch 配置在 95GB GPU 上放不下。
- 错误时 GPU 已用 94.54 GiB / 94.97 GiB，尝试额外分配 1.16 GiB 失败
- OOM 发生在 backward pass（`accelerator.backward(loss)`）
- `set -eo pipefail` 导致整个 pipeline 脚本退出

**根因分析：** 配置沿用了 1.7B 模型的 batch 参数（`per_device_batch_size=4, gradient_accumulation_steps=2, num_generations=4, max_completion_length=512`），对 4B 模型 (Qwen3-4B) 内存不够。GRPO 需要 policy + reference model（~16GB weights）+ optimizer states（~16GB）+ gradients（~8GB）+ activations，总计超过 95GB。

**各 run 状态：**
- `d134_4b_isr_b01_s47`: 训练崩溃于 step 21，仅有 `reward_log.jsonl`（21行）和 `train.log`，无 checkpoint/eval/classify
- 其余 9 个 run: 未启动，目录不存在

**s47 weights 保留状态：** 无 weights（训练未完成，无 `.safetensors` 文件）

**磁盘：** 193G/250G (77%)

**修复建议：** 需要降低 batch 配置重跑。选项：
1. `per_device_batch_size` 4→2（最保守，有效 batch 减半）
2. `num_generations` 4→2（减少 GRPO 采样数）
3. 两者都减

pipeline 脚本中也需要加 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`（已在脚本中 export 了但 OOM 错误提示说没生效，可能因为 env var 在子进程中未继承或是在 allocator 初始化之后才设置）。

---
