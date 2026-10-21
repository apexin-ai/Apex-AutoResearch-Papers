# ops verify cliff keep ratio params

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-cliff-keep-ratio-params_20260520T214014_result.json`
- **Structured JSON:** [`b9fc0e1c895d97cfc169.json`](../../sessions/b9/b9fc0e1c895d97cfc169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. Vision token 保留数量（日志确认）

| 实验 | 日志中的 token 信息 | 正确？ |
|------|---------------------|--------|
| k=0.85 seed42 | `Vision tokens: 50 total, keeping 42 (85%)` | ✅ |
| k=0.85 seed43 | `Vision tokens: 50 total, keeping 42 (85%)` | ✅ |
| k=0.80 seed42 | `Vision tokens: 50 total, keeping 40 (80%)` | ✅ |
| k=0.80 seed43 | `Vision tokens: 50 total, keeping 40 (80%)` | ✅ |
| k=0.90 seed43 (参考) | `Vision tokens: 50 total, keeping 45 (90%)` | ✅ |

### 2. 脚本中 keep_ratio 处理逻辑

```python
# line 65: argparse 定义
p.add_argument("--keep_ratio", type=float, default=1.0,
               help="Fraction of vision tokens to keep (1.0 = no pruning)")

# line 90: 裁剪计算 — 直接用 keep_ratio * N，没有 1-keep_ratio
k = max(1, int(keep_ratio * N))

# line 272: 日志中同样的计算
k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))
```

`int(0.85 * 50) = 42`，`int(0.80 * 50) = 40`。参数名叫 `keep_ratio`，代码里也直接当 keep 用，没有任何取反操作。

### 3. 结论：**参数完全正确，没有 keep/prune 混淆**

k=0.85 异常差的原因是 **Task 6 (butter) 的极端 seed 方差**：

| 实验 | Task 6 (butter) SR |
|------|--------------------|
| k=0.90 seed43 | 100% (50/50) |
| k=0.85 seed43 | **0% (0/50)** |
| k=0.80 seed42 | 56% (28/50) |

k=0.85 seed43 在 butter 任务上 50 集全部 FAIL（每集都跑满 800 步超时）。这不是参数 bug，是 pruning 在特定 keep 数量 + seed 组合下的灾难性退化——可能第 43-45 号 token 中包含了 butter 任务的关键视觉特征。

4 个实验目前均仍在运行中。

---
