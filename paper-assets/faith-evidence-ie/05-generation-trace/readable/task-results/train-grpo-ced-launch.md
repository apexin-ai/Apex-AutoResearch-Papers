# train grpo ced launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_grpo-ced-launch_20260514T071113_result.json`
- **Structured JSON:** [`a6a730691188215193d4.json`](../../sessions/a6/a6a730691188215193d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 卡全部在工作：

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 56% | 20.6 GB |
| 1 | 47% | 7.1 GB |
| 2 | 50% | 7.0 GB |
| 3 | 50% | 7.6 GB |

GRPO+CED Stage 3 训练已成功启动，总计 189 步（注意这里显示 189 而非之前预估的 48，因为 GRPOTrainer 内部按 `num_generations` 和 `num_mini_batches` 进一步分割了 batch）。

总结修复的两个 bug：
1. **accelerate + deepspeed 冲突**：移除 `accelerate_4gpu.yaml` 中的 `mixed_precision: bf16`，改为在 yaml 中用 `deepspeed_config_file` 引用 deepspeed json，从训练命令中移除 `--deepspeed` 参数
2. **CEDRewardWrapper 缺少 `__name__`**：TRL GRPOTrainer 对 reward function 调用 `.__name__`，callable 类需要显式设置 `self.__name__`

---
