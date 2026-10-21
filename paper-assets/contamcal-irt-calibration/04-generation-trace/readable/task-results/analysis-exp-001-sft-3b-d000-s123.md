# analysis exp 001 sft 3B d000 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_3B_d000_s123_20260515T000542_result.json`
- **Structured JSON:** [`2658fba80d3fda49190d.json`](../../sessions/26/2658fba80d3fda49190d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇报如下：

## exp_001_sft_3B_d000_s123 训练结果

**1. 状态：SUCCESS** — 训练正常完成，EXIT_CODE=0，无 error/traceback。

**2. 最终指标：**
| 指标 | 值 |
|------|-----|
| train_loss | **1.1361** |
| mean_token_accuracy | 0.7480 |
| entropy | 1.1108 |
| num_tokens | 19,555,717 |

**3. 训练规模：** 3125 steps, 1 epoch, 耗时 13141.8s（~3.65h）

**4. Checkpoint：完整**
- `adapter_model.safetensors` — 119.8 MB
- `adapter_config.json`, tokenizer 文件, `training_args.bin` 均存在
- 路径: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/`

**5. 与同配置 baseline 对比：**

| 运行 | train_loss | token_acc | 耗时 |
|------|-----------|-----------|------|
| 3B d000 seed=42 (exp_001_sft_0pct_3B) | 1.1306 | 0.7344 | 3.58h |
| 3B d000 seed=42 v2 (exp_001_sft_3B_d000_v2) | 1.1357 | 0.7316 | 3.47h |
| **3B d000 seed=123 (本次)** | **1.1361** | **0.7480** | **3.65h** |

三次 d000 训练的 final loss 在 1.130–1.136 范围内，差异 <0.5%，seed 间一致性良好。

**6. 异常：** 无。bitsandbytes 的 `libnvJitLink.so.13` 加载警告是已知的非致命错误，不影响训练（未使用 bnb 量化）。

---
