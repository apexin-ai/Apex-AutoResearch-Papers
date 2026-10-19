# diagnose qwen dual process

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen_dual_process_20260513T163829_result.json`
- **Structured JSON:** [`8017936f84b252c3b736.json`](../../sessions/80/8017936f84b252c3b736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完毕，结论如下：

## 排查结果

### PID 状态

| PID | 状态 | 说明 |
|-----|------|------|
| **61362** | **已死亡** | 不存在 |
| **62033** | **已死亡** | 不存在 |
| **67518** | 存活，运行 5m50s | agent-ml 启动的 wrapper bash 进程 |
| **67530** | 存活，运行 5m50s，RSS ~4GB | 主 train.py 进程，**唯一占用 GPU 的进程**（cuda:0，49372 MiB） |
| **67870-67873** | 存活，RSS 各 ~2.9GB | 67530 的 4 个子进程 |

### 进程树

```
67518 (bash wrapper)
 └─ 67522 (timeout)
     └─ 67523 (bash run_m2_full_qwen.sh)
         └─ 67530 (python train.py)  ← 主进程，占 GPU
             ├─ 67870 (python train.py)  ← DataLoader worker
             ├─ 67871 (python train.py)
             ├─ 67872 (python train.py)
             └─ 67873 (python train.py)
```

### train.py 多进程分析

- **无** DDP / DataParallel / mp.spawn / torch.multiprocessing
- **有** `num_workers=4`（训练 DataLoader）和 `num_workers=2`（验证 DataLoader）
- 4 个子进程（67870-67873）正是训练 DataLoader 的 4 个 worker，由 PyTorch 自动 fork 产生

### 结论

**预期行为，无异常。**

原来的 PID 61362 和 62033 已经不存在（可能是之前的训练已结束或被终止）。当前只有一个训练实例在跑（PID 67530），它的 4 个子进程是 DataLoader worker，不是重复启动。tmux session `m2_full_qwen` 只有 1 个窗口，一切正常。无需任何操作。

---
