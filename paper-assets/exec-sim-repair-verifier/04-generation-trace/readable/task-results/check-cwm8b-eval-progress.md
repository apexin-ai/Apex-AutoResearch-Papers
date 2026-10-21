# check cwm8b eval progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cwm8b-eval-progress_20260516T042708_result.json`
- **Structured JSON:** [`12ad5dc81b3040d7be82.json`](../../sessions/12/12ad5dc81b3040d7be82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM 8B Eval 进度汇总

| Shard | PID | GPU | 状态 | 已完成/总数 | 进度 | 预计剩余 |
|-------|-----|-----|------|-------------|------|----------|
| **v3** (全量) | 443221 | cuda:3 | 运行中 | 7176 / 9784 | 73.3% | ~5h |
| **shard2** | 448100 | cuda:1 | 运行中 | 1568 / 2104 | 74.5% | ~1h |
| **shard3** | 453335 | cuda:0 | 运行中 | 928 / 1480 | 62.7% | ~1h |
| **shard4** | — | cuda:2 | **已完成** | 688 / 684 | 100% | — |

### GPU 利用率
| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 21133 / 32607 MiB | 88% |
| 1 | 21133 / 32607 MiB | 84% |
| 2 | 0 / 32607 MiB | **0% (空闲)** |
| 3 | 21133 / 32607 MiB | 83% |

### 关键信息
- **shard4 已完成**，进程已退出，GPU 2 空闲可复用
- **v3** 的 running_acc = 64.4%（12:27 时刻），output_dir = `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test/`
- **v3 与 shard2/3/4 有大量重叠**：v3 跑全量 0-9784，shard2 跑 7680-9784，shard3 跑 6200-7680，shard4 跑 9100-9783。shard2/3/4 先跑完的部分可以直接用，v3 作为完整备份
- shard2 的 bash 包装进程 CPU=0%，但实际 python 子进程 (pid 448100) 在 100% CPU 正常运行
- 无 OOM 或异常

---
