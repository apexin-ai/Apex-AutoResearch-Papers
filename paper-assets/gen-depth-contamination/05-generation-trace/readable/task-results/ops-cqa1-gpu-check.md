# ops cqa1 gpu check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-gpu-check_20260518T092601_result.json`
- **Structured JSON:** [`1e0ca61e910e79cb795b.json`](../../sessions/1e/1e0ca61e910e79cb795b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| GPU | 利用率 | 显存占用 | 进程 PID | 归属 |
|-----|--------|----------|----------|------|
| cuda:0 | **80%** | 5399MiB / 24564MiB | **22969** | exp025 ✅ |
| cuda:1 | 0% | 0MiB | 无 | — |
| cuda:2 | 0% | 0MiB | 无 | — |
| cuda:3 | 0% | 0MiB | 无 | — |

**cuda:0 进程详情：**
- PID 22969：`python scripts/exp025_pythia_filtering.py --strategy graduated_a09 --seed 456 --device cuda:0`
- 启动时间：17:20（约 6 分钟前）
- 附带 32 个 torch inductor compile worker 子进程

**exp025 主进程 (PID 15687)：**
- 存活 ✅：`bash scripts/run_exp025.sh`，启动于 16:26

**异常：exp025 只在 cuda:0 单卡运行，cuda:1/2/3 完全空闲。** 预期是 4 卡并行，但实际命令行显式指定了 `--device cuda:0`，且没有其他 GPU 上有进程。这可能是 `run_exp025.sh` 正在串行跑多个 seed/strategy（当前跑的是 `graduated_a09 --seed 456`），而非 4 卡并行。

---
