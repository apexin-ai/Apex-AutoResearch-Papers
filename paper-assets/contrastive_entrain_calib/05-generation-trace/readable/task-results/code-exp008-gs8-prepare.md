# code exp008 gs8 prepare

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-gs8-prepare_20260522T130720_result.json`
- **Structured JSON:** [`fe9101201f0c0e8f1ed2.json`](../../sessions/fe/fe9101201f0c0e8f1ed2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。最终核对：

## 新脚本 `run_exp008_gs8_ablation.py` 关键配置对比

| 参数 | exp-008 原值 | gs8 ablation |
|------|-------------|-------------|
| `batch_size` | 1 | **8** |
| `grad_accum` | 16 | **2** |
| effective batch size | 16 | 16 (不变) |
| `max_steps` | 8000 | **800** |
| `save_steps` | 500 | **200** (checkpoint at 200/400/600/800) |
| `output_dir` | `.../checkpoints/exp008_binary_probe_penalty` | **`/root/autodl-tmp/.../exp008_gs8_ablation/`** |
| `lr` | 5e-5 | 5e-5 (不变) |
| `lora_rank/alpha` | 64/128 | 64/128 (不变) |
| `lambda_reward/probe` | 0.1/1.0 | 0.1/1.0 (不变) |
| `seed` | 42 | 42 (不变) |
| `retrain_interval` | 500 | 500 (不变) |
| `warmup_steps` | 200 | 200 (不变) |

## 说明

**关于 group_size 的实现**：exp-008 是纯 SFT 脚本，没有 GRPO 的 `num_generations` 参数。在 SFT 上下文中，"group_size" 映射到 `batch_size`——每次前向传播中 probe penalty S(t) 基于多少个样本的均值计算。原来 batch_size=1 (每个 probe 分数只看一个样本)，现在 batch_size=8 (S(t) 是 8 个样本的均值，信号更平滑)。`grad_accum` 从 16 降到 2，保持有效 batch size = 16 不变。

## Dry run 状态

GPU 0 被占用（PID 237437, 38GB/98GB, 95% util），**跳过 dry run**。GPU 0 有 ~60GB 空闲，Qwen3-8B (bf16 ~16GB) + batch_size=8 + `output_hidden_states=True` (所有层 hidden states) 估算需要 35-45GB，应该能放下，但需要等当前任务完成后验证。

## 需要注意

`warmup_steps=200` 在 `max_steps=800` 下占比 25%（原来在 8000 步中只占 2.5%）。如果你认为这会影响实验公平性，需要按比例缩小为 `warmup_steps=20`。

---
