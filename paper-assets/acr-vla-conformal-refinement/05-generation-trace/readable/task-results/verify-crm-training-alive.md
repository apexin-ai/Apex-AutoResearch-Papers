# verify crm training alive

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_crm-training-alive_20260524T105805_result.json`
- **Structured JSON:** [`7acc0e336cce9809c839.json`](../../sessions/7a/7acc0e336cce9809c839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

| 项目 | 状态 |
|------|------|
| **GPU 0 显存** | 558 MiB（训练进程 `CUDA_VISIBLE_DEVICES=0`，但显存占用偏低） |
| **tmux session** | `train-crm-pi05-unified-3suite-r2` 存在 ✅ |
| **PID 326310** | 存活 ✅（bash wrapper），实际 python 训练进程 PID 326315 + 2 个 worker（328645, 328646） |
| **当前进度** | **Epoch 1, batch 300/684** |
| **Batches/epoch** | **684**（194,485 samples / 256 batch_size ≈ 760 理论值，实际 684 因 val_split=0.1 分出验证集：~175K train / 256 ≈ 684）✅ 符合预期 |
| **Loss** | ~0.014–0.018（epoch 1 前半段） |

**关键验证通过**：batches/epoch = 684（非旧的 ~5470），确认 batch_size=256 生效。训练刚启动约 20 分钟（18:38 启动），正在 epoch 1 前半段正常推进。

注意：GPU 0 显存仅 558 MiB 看起来偏低，可能是因为 `nvidia-smi` 查询时刻刚好在 batch 间隙，或者 CRM 模型本身很小（仅 615,966 参数）所以实际显存需求不大。

---
