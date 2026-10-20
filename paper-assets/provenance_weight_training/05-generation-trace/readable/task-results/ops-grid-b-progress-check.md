# ops grid b progress check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grid-b-progress-check_20260514T082947_result.json`
- **Structured JSON:** [`9c7a25681d42c79e2cbe.json`](../../sessions/9c/9c7a25681d42c79e2cbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Grid-b seed42 batch (GPU 0)
当前 b 值: **b=1.5**
已完成:
- b=0.5: PPL=**17.651**, loss=2.8708
- b=1.0: PPL=**17.692**, loss=2.8731

当前进度: step **2432/6103 (40%)**, ETA ~2h10m, 速度 2.13s/it
- grid_b1_5_seed42 目录有 checkpoint-1500, checkpoint-2000，无 final

## Grid-b seed123 round 1 (GPU 1/2/3)
| 配置 | GPU | Step | 进度 | 速度 | ETA |
|------|-----|------|------|------|-----|
| b=0.5 | 1 | 2656/6103 | **43%** | 2.12s/it | ~2h02m |
| b=1.0 | 2 | 2564/6103 | **42%** | 4.52s/it | ~4h27m |
| b=1.5 | 3 | 2141/6103 | **35%** | 4.51s/it | ~4h58m |

注意：GPU 1 上的 b=0.5 速度 (~2.12s/it) 是 GPU 2/3 (~4.5s/it) 的 2 倍。GPU 2/3 可能共享显存导致变慢（均占用 93GB/98GB）。

## Auto-eval watcher
状态: **running** (PID 74145)
已产出 eval:
- `grid_b0_5_seed42_eval.json` — PPL=17.651
- `grid_b1_0_seed42_eval.json` — PPL=17.692

Watcher 每 60s 轮询一次，检测到有 final 目录自动触发 eval。

## GPU 状态
| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 46.5/97.9 GB | 99% |
| 1 | 46.5/97.9 GB | 99% |
| 2 | 93.0/97.9 GB | 100% |
| 3 | 93.0/97.9 GB | 99% |

GPU 2/3 显存几乎打满（93/98GB），GPU 0/1 正常（46.5GB）。这解释了 GPU 2/3 上训练速度慢一倍的现象——可能 auto_eval_watcher 指定了 GPU 3 做 eval 但此时 GPU 3 同时在训练 b=1.5_seed123。

---
