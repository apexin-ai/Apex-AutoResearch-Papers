# diag exp008v3 single gpu feasibility

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp008v3-single-gpu-feasibility_20260519T061025_result.json`
- **Structured JSON:** [`ec54cf68d1fbc26a3a78.json`](../../sessions/ec/ec54cf68d1fbc26a3a78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，给出评估。

## 评估结果

### 1. GPU 状态确认

4× RTX 5090 (32GB)，当前：
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 21.8/32.6 GB | exp-004 运行中 |
| 1 | 31.4/32.6 GB | 满载运行中 |
| 2 | 30.6/32.6 GB | 满载运行中 |
| **3** | **4 MB / 32.6 GB** | **空闲** |

### 2. 单卡 GRPO 可行性：**不可行**

脚本关键参数：
- `per_device_train_batch_size=1`, `gradient_checkpointing=True`, `num_generations=2`, `max_completion_length=256`
- LoRA r=64, target = q/k/v/o_proj
- 额外：DeBERTa NLI (~400MB) + Binary Probe + 7 层 activation cache

**显存估算**：
- Qwen3-8B bf16 = ~16 GB
- LoRA 参数 + optimizer states = ~1-2 GB
- GRPO num_gen=2: 需要同时 forward 2 条生成序列的 KV cache + logprobs = ~6-8 GB
- Gradient checkpointing backward pass = ~4-6 GB
- DeBERTa + probe + activation cache = ~1.5 GB
- **总计 ~29-34 GB**

即使最乐观估计也会卡在 32GB 边界。exp-002v2 在 96GB 卡上用了 52GB（那个是完整 DC-GRPO，此处虽然 R1 更轻但整体框架一样）。

**可能的 workaround**：
- **QLoRA 4-bit**：模型从 16GB 降到 ~5GB，总体可降至 ~18-22GB，**理论上可行**。但需要修改脚本（加 `BitsAndBytesConfig`），且 probe retrain 逻辑中 `unwrap_model` 提取 activations 在 4-bit 模型上需要验证兼容性。**风险较大，不建议在 exp-004 完成前折腾。**
- 降 `num_generations=1`：GRPO 至少需要 2 条生成做对比，降到 1 无意义。
- `max_completion_length` 从 256 降到 128：省 ~1-2GB，不够。

**结论：等双卡 DeepSpeed ZeRO-2 是正确策略。** ds_config_zero2.json 已就绪，双卡各分担一半 optimizer states，显存充裕。

### 3. GPU 3 空闲期间建议

按价值排序：

**推荐：(b) Eval dry-run**
- 用 exp-004 的中间 checkpoint 跑一次完整 eval pipeline
- 好处：提前验证 eval 脚本无 bug，exp-004 完成后可以立即出结果而不用 debug eval
- 只需单卡推理，32GB 绑绑有余
- 如果 eval 包含 NLI scoring，也可以一并验证 DeBERTa 在 28034 上加载正常

**次选：其他推理型预检**
- 验证 Qwen3-8B 在 28034 上 tokenizer / chat template 正常
- 预跑 probe_module 的 `train_probe` 确保 exp-001 activations 读取无误

**不推荐 (a)**：Direction stability 不需要 GPU，浪费。

是否需要我准备 eval dry-run 的命令？

---
