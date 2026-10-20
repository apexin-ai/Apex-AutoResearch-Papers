# check 15pct grpo verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_15pct_grpo_verify_20260520T050807_result.json`
- **Structured JSON:** [`91aa7396b896aa13b034.json`](../../sessions/91/91aa7396b896aa13b034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## 状态确认

### 1. GRPO CKA-only 15%
- **状态**: 正在运行，正加载 ref_model（模型已上 GPU，cuda:2 占用 13193 MiB）
- **PID**: 204464，tmux session: `grpo_cka15`
- **当前阶段**: 数据集加载完成（7473 samples），正在加载 ref_model，尚未开始训练 step
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_cka_only_15.log`

### 2. GRPO Standard 15%
- **状态**: 正在运行，同样在加载 ref_model（cuda:3 占用 13169 MiB）
- **PID**: 204542，tmux session: `grpo_std15`
- **当前阶段**: 同上，数据集加载完成，ref_model 加载中
- **日志**: `/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_standard_15.log`

### 3. Pruning/SFT 阶段确认
| 产出 | 状态 | 大小 |
|------|------|------|
| `pruned_cka_only_15/` | 完整（含 model.safetensors + pruning_metadata.pt） | ~12.2GB |
| `pruned_standard_15/` | 完整（含 model.safetensors + pruning_metadata.pt） | ~12.1GB |
| `sft_cka_only_15/` | 完整（含 training_args.bin） | ~12.2GB |
| `sft_standard_15/` | 完整（含 training_args.bin） | ~12.1GB |

### 4. Registry 更新
- `pipeline_cka_only_15`: PREPARING → RUNNING（含完整 spec）
- `pipeline_standard_15`: PREPARING → RUNNING（含完整 spec）

两个 GRPO 训练刚启动约 2 分钟，正在加载 ref_model，预计很快开始第一个 step。100 steps 预计 8-12h 完成。

---
