# code kill fix acdc

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kill-fix-acdc_20260512T150933_result.json`
- **Structured JSON:** [`c948a29a500d005c607e.json`](../../sessions/c9/c948a29a500d005c607e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. PID 98300 Kill 确认
已成功 kill（SIGTERM，无需 SIGKILL）。nvidia-smi 显示 GPU 5 上只剩 PID 98594（9302MiB）。

### 2. ACDC 多 threshold 问题：**否**

`circuit_discovery.py` 中 `run_acdc` 只传了 `tao_exps=[-2]`，即单个 threshold τ=0.01。没有多 threshold 扫描。

```python
prune_scores = acdc_prune_scores(
    model=ac_task.model,
    dataloader=ac_task.train_loader,
    official_edges=None,
    tao_exps=[-2],  # 只有一个
)
```

日志中的 τ=0.01 是 ACDC 算法逐边测试（Remove/Keep），总共 32491 条边，这是正常的 O(E) 行为。

### 3. 当前进度 & ETA

- 进度：**29690 / 32491**（91.4%），速度 3.29 it/s
- 剩余：~2801 edges ÷ 3.29 = **约 14 分钟** ACDC 完成
- 已移除 29504 边，保留 186 边
- ACDC 之后还有 CSS、Cross-Tabulation、Evaluation 阶段

### 4. Kill 后速度变化

Kill 前后 ACDC 速度都稳定在 ~3.3 it/s。PID 98300 可能之前已不活跃或在不同 GPU 上，对当前进程无明显影响。GPU 5 利用率 100%，正常。

### 5. 整体 ETA

- ACDC 完成：~14 分钟（约 23:24）
- 后续 Phase C/D（CSS + Eval）：预计 5-15 分钟
- **总计：约 20-30 分钟后出 mvp_results.json**

EAP-IG 和 Edge Pruning 均已有缓存（`cache_eap_ig.json`、`cache_edge_pruning.json`），不会重跑。

---
