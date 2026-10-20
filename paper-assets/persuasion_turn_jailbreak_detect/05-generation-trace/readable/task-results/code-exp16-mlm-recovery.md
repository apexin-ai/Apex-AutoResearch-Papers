# code exp16 mlm recovery

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-mlm-recovery_20260519T204746_result.json`
- **Structured JSON:** [`ebce64649cc35d0534ff.json`](../../sessions/eb/ebce64649cc35d0534ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**脚本内容**：

- `scripts/exp16_mlm_gpu0.sh` — GPU 0 跑 seed 42 Stage 2 → seed 123 Stage 1 → seed 123 Stage 2
- `scripts/exp16_mlm_gpu1.sh` — GPU 1 跑 seed 456 Stage 1 → seed 456 Stage 2
- 均已设置 `WANDB_MODE=disabled`, `TRANSFORMERS_OFFLINE=1`, `HF_HUB_OFFLINE=1`

**当前状态**：

| GPU | tmux session | 当前任务 | 进度 |
|-----|-------------|---------|------|
| 0 | exp16_mlm_gpu0 | seed 123 Stage 1 (DAPT) | Epoch 3/4, loss 5.61 |
| 1 | exp16_mlm_gpu1 | seed 456 Stage 1 (DAPT) | Epoch 2/4, loss 6.10 |

- seed 42 Stage 2 (GRU) 已完成，最佳 Val Loss 0.3608, Val Acc 0.8243
- GPU 显存各占用 ~20GB/98GB，利用率 72-76%
- 模型缓存 `microsoft/deberta-v3-base` 已在本地，`TRANSFORMERS_OFFLINE=1` 生效无网络请求

---
