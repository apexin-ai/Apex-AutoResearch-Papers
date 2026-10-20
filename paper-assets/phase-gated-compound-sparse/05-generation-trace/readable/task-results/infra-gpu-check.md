# infra gpu check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check_20260514T061923_result.json`
- **Structured JSON:** [`c42c5c72b0703c5af86a.json`](../../sessions/c4/c42c5c72b0703c5af86a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 占用报告

### GPU 状态

| GPU | 显存占用 | 总显存 | 利用率 | 占用进程 |
|-----|---------|--------|--------|---------|
| cuda:0 | 60,178 MiB | 97,887 MiB | 90% | PID 79817 (31,438 MiB) + PID 80500 (28,726 MiB) |
| cuda:1 | 0 MiB | 97,887 MiB | 0% | 空闲 |
| cuda:2 | 0 MiB | 97,887 MiB | 0% | 空闲 |
| cuda:3 | 0 MiB | 97,887 MiB | 0% | 空闲 |

### 进程映射

- **bf16_importance_s020**: bash wrapper PID 79812 → 实际 Python 进程 PID **79817**，在 **GPU 0**，占 31,438 MiB
- **bf16_importance_s030**: bash wrapper PID 80495 → 实际 Python 进程 PID **80500**，在 **GPU 0**，占 28,726 MiB
- **bf16_importance_s025 (PID 80207)**: **不存在**，ps 输出中未找到该进程

### 结论

1. **冲突确认**：两个实验（s020 和 s030）都设置了 `CUDA_VISIBLE_DEVICES=0`，共享 GPU 0。显存未溢出（60/98 GB），但 GPU 利用率 90%，存在计算资源争抢，会互相拖慢。
2. **GPU 1/2/3 完全空闲**，白白浪费了 3 张卡。
3. **s025 进程已不存在**，需要检查其日志确认是正常结束还是异常退出。

---
