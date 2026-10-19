# test westd28034 lora vram

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_test_westd28034_lora_vram_20260518T134538_result.json`
- **Structured JSON:** [`f65818e58c7f1fe2c9a3.json`](../../sessions/f6/f65818e58c7f1fe2c9a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试完成。结果：

## Qwen3-8B LoRA VRAM 测试结果（RTX 5090 32GB）

| 配置 | Peak VRAM | 状态 |
|------|-----------|------|
| 模型加载 (bf16) | 16.4GB | OK |
| LoRA 挂载后 | 16.4GB | OK |
| batch=1, seq=2048 | **21.4GB** | OK |
| batch=2, seq=2048 | **26.4GB** | OK |
| batch=4, seq=2048 | **OOM** (27.9GB时崩) | 失败 |
| batch=8, seq=2048 | OOM | 失败 |

**结论**：
- 32GB RTX 5090 **可以跑** Qwen3-8B LoRA 训练
- 单卡最大 batch_size = **2**（peak 26.4GB，剩余约 6GB 余量）
- batch=4 OOM，不可用
- **不需要** multi-GPU DDP 就能训练

**建议训练配置**：
- `per_device_train_batch_size=2`
- `gradient_accumulation_steps=8`（有效 batch=16）
- `gradient_checkpointing=True`
- `bf16=True`
- 单卡即可，4 卡 DDP 可 4x 加速

---
