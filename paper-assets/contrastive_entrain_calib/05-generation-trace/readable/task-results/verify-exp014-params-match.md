# verify exp014 params match

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp014-params-match_20260518T165423_result.json`
- **Structured JSON:** [`14d3e9483006ed961e40.json`](../../sessions/14/14d3e9483006ed961e40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 超参对比结果

| 参数 | exp-002 | exp-014 | 匹配? |
|------|---------|---------|-------|
| **LoRA r** | 64 | 64 | ✓ |
| **lora_alpha** | 64 | 64 | ✓ |
| **target_modules** | q/v/k/o_proj | q/v/k/o_proj | ✓ |
| **bias** | "none" | "none" | ✓ |
| **task_type** | "CAUSAL_LM" | "CAUSAL_LM" | ✓ |
| **dropout** | 未设置(默认) | 未设置(默认) | ✓ |
| **learning_rate** | 5e-5 | 5e-5 | ✓ |
| **warmup_steps** | 200 | 200 | ✓ |
| **per_device_train_batch_size** | 1 | 1 | ✓ |
| **gradient_accumulation_steps** | 16 | 16 | ✓ |
| **gradient_checkpointing** | True | True | ✓ |
| **max_steps** | 8000 | 8000 | ✓ |
| **num_train_epochs** | 10 | 10 | ✓ |
| **bf16** | True | True | ✓ |
| **seed** | 42 | 42 | ✓ |
| **num_generations** | 2 | 2 | ✓ |
| **max_completion_length** | 256 | 256 | ✓ |
| **r1_weight** | 0.25 | 0.25 | ✓ |
| **r2_weight** | 0.0 | 0.0 | ✓ |
| **r3_weight** | 0.75 | 0.75 | ✓ |
| **reward_layers** | [19,20,24,27,32,33,35] | [19,20,24,27,32,33,35] | ✓ |
| **reward_position** | "asst_first" | "asst_first" | ✓ |
| **r3_model_name** | cross-encoder/nli-deberta-v3-base | cross-encoder/nli-deberta-v3-base | ✓ |
| **logging_steps** | 10 | 10 | ✓ |
| **save_steps** | 500 | 500 | ✓ |
| **MODEL_PATH** | /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B | /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B | ✓ |
| **DATA_PATH** | calibration_v2_1_expanded.jsonl | calibration_v2_1_expanded.jsonl | ✓ |
| **DIRECTION_PATH** | exp001/directions.pt | exp001/directions.pt | ✓ |
| **R1 计算方式** | 方向投影 (direction projection) | 探针概率 (1-P(syc)) | ✓ 预期差异 |

**所有训练超参完全一致。**

---

## 需要注意的非超参差异

**exp-002 包含 per-strength R1 adaptive gating，exp-014 没有。**

exp-002 的 `Exp002Trainer` 有以下机制：
- 前 10 步收集 weak-strength 样本的 R1 值统计量
- 如果 weak R1 噪声过大（|mean|<0.05 或 std>|mean|），在 step 100 后将 weak 样本的 R1 贡献置零

exp-014 的 `ProbeTrainer` 没有这个 gating 逻辑。

**判断：** 这属于 R1 信号质量控制机制，与 R1 计算方式紧密耦合。direction-based R1 在 weak pair 上信号可能不稳定所以需要 gating；probe-based R1 直接输出概率，信号特性不同，不一定需要同样的 gating。但如果你想严格控制变量，有两个选择：

1. **保持现状**（推荐）：gating 是 direction-based R1 的配套机制，probe R1 不需要，去掉是合理的设计决策。在论文中说明即可。
2. **移植 gating**：在 `ProbeTrainer` 中也加入同样的 adaptive gating 逻辑，对 probe R1 的 weak pair 做同样的噪声检测和置零。

除此之外，exp-014 多了 `HF_ENDPOINT` 环境变量设置（第 22-23 行），仅影响模型下载镜像，对训练无影响。

---
