# ops eval prep code sync

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-prep-code-sync_20260521T191028_result.json`
- **Structured JSON:** [`a3fd8ba4f433864beb23.json`](../../sessions/a3/a3fd8ba4f433864beb23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。汇总：

**Training (bjb1-18228)**
- Epoch 7/50, batch 1350/1950，运行 52 min
- Best val_loss = 0.005511 (epoch 6)，约 5.5h 后完成
- 输出目录: `crm_pi05_full/object/`，已有 crm_best.pt

**代码同步**
- 两台 eval 服务器 evaluate.py 均为 33058 bytes，版本正确
- 三台服务器都没有有效 git remote，代码是直接拷贝的

**Eval 环境 (bjb1-32546 / bjb2-28827)**
- torch 2.10.0+cu128, CUDA OK, 6 GPUs each
- evaluate.py --help 正常
- pi05 模型 (7.5GB) 已就位
- **环境就绪**

**Checkpoint**
- `crm_pi05_full/object/`: 当前 run，epoch 2-6 + crm_best.pt ✅
- `crm_pi05/spatial/`: epoch 2-6 + crm_best.pt ✅
- `crm_pi05/object/`: 旧 run 残留 (epoch 1-3)

可立即用现有 best checkpoint 做早期 eval 测试，无需等训练完成。

---
