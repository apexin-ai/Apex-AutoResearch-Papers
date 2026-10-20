# ssh gpu gen2 status check

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_gen2_status_check_20260516T015929_result.json`
- **Structured JSON:** [`aab2e379b7ad77902bae.json`](../../sessions/aa/aab2e379b7ad77902bae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | **0%** | 7951 / 97887 MiB |
| cuda:1 | **0%** | 7951 / 97887 MiB |

GPU 利用率为 0%，但两张卡各有 ~8GB 显存占用。

### gen2 当前阶段：信号计算（compute_signals），进行中

两个 `compute_signals.py` 进程正在跑：
- **seed42**: `per-example signals` 进度 ~36% (112/313)，速度 ~11s/it
- **seed137**: `per-example signals` 进度 ~31% (98/313)，速度 ~13s/it

这两个进程是 CPU-bound 的信号计算阶段（GPU 利用率 0% 印证了这点），由 `run_pipeline.py --seeds 42,137 --start_gen 1` 在 tmux session `mvp_collapse_decoupling` 中调度。

### 已完成的阶段
按时间线：
1. gen0 信号计算 ✅ (02:18 / 02:39)
2. gen1 训练 ✅ (checkpoints gen1_seed42, gen1_seed137 @ 05:27)
3. gen1 信号计算 ✅ (06:41 / 06:42)
4. gen1 可视化 ✅ (07:21)
5. gen1 统计分析 ✅ (09:20 / 09:21)
6. gen2 训练 ✅ (checkpoints gen2_seed42, gen2_seed137 @ 09:40)
7. **gen2 信号计算 🔄 进行中** (~30-36%，两个 seed 并行)

### 预计剩余时间
- seed42: ~(313-112) × 11s ≈ **37 分钟**
- seed137: ~(313-98) × 13s ≈ **47 分钟**

信号计算完成后，pipeline 应会继续 gen2 的可视化和分析步骤。

---
