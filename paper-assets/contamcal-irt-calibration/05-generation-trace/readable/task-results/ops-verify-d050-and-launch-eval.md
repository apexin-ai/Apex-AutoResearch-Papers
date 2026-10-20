# ops verify d050 and launch eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-d050-and-launch-eval_20260521T051702_result.json`
- **Structured JSON:** [`054a8ae9547068531256.json`](../../sessions/05/054a8ae9547068531256.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### retrain_qwen14b_d050_s0 — 训练成功 ✓
- exit_code=0, epoch=1.0, train_loss=0.9421
- Adapter: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s0/lora_adapter/adapter_model.safetensors` (275MB)
- lora_alpha=32 ✓ (C006 pass)
- Registry → DONE/success

### eval_qwen14b_d050_mmlu_s0 — 已启动 ✓
- PID 479118, cuda:1, 32726 MiB 已占用
- Registry → RUNNING

### ARC eval — 暂无可用 GPU
- cuda:0/2/3 全部占满（各 32726 MiB, 93-94% utilization）
- ARC 需等其中一张 GPU 释放后再提交

### 当前 GPU 状态
| GPU | Memory | Util | 状态 |
|-----|--------|------|------|
| 0 | 32735/97887 MiB | 94% | 占用 (PID 474588) |
| 1 | 32726/97887 MiB | — | MMLU eval (PID 479118) |
| 2 | 32735/97887 MiB | 94% | 占用 (PID 474594) |
| 3 | 32735/97887 MiB | 93% | 占用 (PID 474597) |

---
