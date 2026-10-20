# verify d005 s42 hyperparams

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d005_s42_hyperparams_20260515T200838_result.json`
- **Structured JSON:** [`c5391c80348a104ef6f4.json`](../../sessions/c5/c5391c80348a104ef6f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已充分。

## 验证结果

### d005_s42 (Qwen2.5-3B) 超参配置

| 参数 | 实际值 | 标准值 | 状态 |
|------|--------|--------|------|
| **lora_alpha** | **32** | 16 | **不一致** |
| **learning_rate** | **2e-4** (peak) | 5e-5 | **不一致** |
| r | 16 | 16 | OK |
| lora_dropout | 0.05 | - | - |
| target_modules | 全部 7 个 proj | - | - |

### 结论：**非标准配置，不能用**

d005_s42 与 d000_s42（D071 发现的问题）完全一致：lr=2e-4, lora_alpha=32，均偏离标准配置（lr=5e-5, lora_alpha=16）。**不可加入 signals_3B_v6。**

### Checkpoint 路径

- adapter: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/`
- checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/checkpoint-3177/`

同批次的 0.5B 和 1.5B d005_s42 checkpoint 也在同目录下，大概率也是同样的非标准配置。

---
