# ops cuda2 cascade grpo cka only 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda2_cascade_grpo_cka_only_2048_20260518T232246_result.json`
- **Structured JSON:** [`0fde22fce91d9ddf7ca9.json`](../../sessions/0f/0fde22fce91d9ddf7ca9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部状态汇总：

### 1. SFT 重训完成
- **train_loss**: 0.758, **mean_token_accuracy**: 0.8252, **epoch**: 2, **runtime**: 1688s
- 模型已保存到 `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/` (12.3GB)
- Registry 已更新为 success

### 2. GRPO CKA-only MATH-500 @2048 已启动
- **PID 36703**, cuda:2, 12488MiB 已加载
- tmux session: `eval_math500_grpo_cka_only_20_2048`
- 正在加载 MATH 数据集，即将开始推理

### 3. 其他 GPU 进度
| GPU | 任务 | 进度 | 当前 Acc |
|-----|------|------|----------|
| cuda:0 | Dense @2048 | 187/500 (37%) | 55.3% |
| cuda:1 | Standard GRPO v2 | 355/500 (71%) | 25.1% |
| cuda:3 | RASP GRPO | 470/500 (94%) | 24.0% |

cuda:3 RASP GRPO 快跑完了，约 8 分钟后结束。

---
