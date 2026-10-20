# check batch1 completion

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_batch1-completion_20260515T144515_result.json`
- **Structured JSON:** [`a101c073a69ef36c5629.json`](../../sessions/a1/a101c073a69ef36c5629.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Batch 1 训练状态

| 训练 | PID | GPU | 状态 | 进度 | 最新指标 |
|------|-----|-----|------|------|----------|
| **vanilla-seed7** | 154666 | cuda:1 | **已完成** ✓ | 1635/1635 (100%) | loss=0.295, token_acc=0.898 |
| **taxei-seed1** | 154937 | cuda:2 | 运行中 | 2017/3387 (59%) | loss=0.28, token_acc=0.90 |
| **taxei-seed7** | 155145 | cuda:3 | 运行中 | 2001/3387 (59%) | loss=0.27, token_acc=0.90 |

### vanilla-seed7（已完成）
- EXIT_CODE=0，正常结束
- 总耗时 59m 24s，1635 steps，3 epochs
- 最终 loss=0.295，token_acc=0.898，train_loss=0.415
- Checkpoints: checkpoint-545 / checkpoint-1090 / **checkpoint-1635**（final）

### taxei-seed1（运行中）
- 当前 step 2017/3387，~1.93s/it
- 已有 checkpoint-1129（epoch 1 结束时保存）
- **ETA: ~44 分钟**

### taxei-seed7（运行中）
- 当前 step 2001/3387，~1.95s/it
- 已有 checkpoint-1129（epoch 1 结束时保存）
- **ETA: ~45 分钟**

### GPU 空闲情况
- **cuda:0**: 空闲
- **cuda:1**: 空闲（vanilla-seed7 已完成释放）
- cuda:2, cuda:3: 被 taxei-seed1/seed7 占用（各 ~19.5GB / 32GB）

---
