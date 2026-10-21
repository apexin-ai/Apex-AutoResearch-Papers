# diag plan 002 v6 crash

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan-002-v6-crash_20260514T070357_result.json`
- **Structured JSON:** [`1603246fd834fae9132d.json`](../../sessions/16/1603246fd834fae9132d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因

**CUDA OOM，GPU 0 内存争抢。** v6 训练首次启动时（~14:59），GPU 0 上已有另一个进程占用大量显存。Qwen3-1.7B LoRA 训练单独运行需要 ~30GB（当前重启后使用 29848/32607 MiB），两个进程共存必然 OOM。

### 完整错误信息

日志因 stderr/stdout 交错而混乱，实际致命错误是：
```
Terminated
[...] iB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large 
try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation.
EXIT_CODE=1
EXIT_CODE=129
```

训练跑了 30/153 步（~2:54）后被 OOM 杀死。日志中看到的 `WeightedCETrainer` traceback 是 stderr 与 stdout 进度条交错的产物，不是独立的代码错误。

### 当前状态

**训练已被重新启动**（PID 240633，15:03 启动），目前正常运行在 GPU 0，进度 73/153 步（48%，epoch 2）。

epoch 1 eval 结果：
- accuracy=0.929, f1_macro=0.481
- **f1_internal=0.0**（recall_internal=0.0）— 模型把所有样本都预测为 deterministic

### 修复方案

**不需要改代码。** 崩溃是 GPU 资源争抢问题，不是代码 bug。

但 epoch 1 的 f1_internal=0.0 值得注意：去掉 `--class_weights` 后，模型在 89.7%/10.3% 的不平衡数据上完全忽略了 minority class。这正是 v6 实验的预期对照——验证 class_weights 的必要性。

---
