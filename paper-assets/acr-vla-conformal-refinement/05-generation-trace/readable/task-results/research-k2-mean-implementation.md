# research k2 mean implementation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_k2-mean-implementation_20260523T064126_result.json`
- **Structured JSON:** [`ee6ac7bf1a83779b6f47.json`](../../sessions/ee/ee6ac7bf1a83779b6f47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息完整，给出报告。

---

## 报告

### 1. K=2 mean 是否已支持？

**已支持。** 用 `vla_only` mode + `--baseline_mode mean` 即可。

但当前实现有一个问题：`--baseline_mode mean` 会强制 K=10（见 `main()` 第 815 行）：

```python
if args.mode == "vla_only":
    if args.baseline_mode == "single":
        args.K = 1
    elif args.baseline_mode == "mean":
        args.K = 10
```

所以 **K=2 mean 不是开箱即用的**——`--baseline_mode mean` 会覆盖用户传的 `--K 2`。

**调用方式（需要微调）：**

当前想跑 K=2 mean，`--mode vla_only --baseline_mode mean --K 2` 不行，因为 K 会被覆盖成 10。

### 2. 最小改动方案

改 `main()` 中那 4 行，让 `--baseline_mode mean` 不覆盖用户显式指定的 K：

```python
# 改前：
if args.mode == "vla_only":
    if args.baseline_mode == "single":
        args.K = 1
    elif args.baseline_mode == "mean":
        args.K = 10

# 改后：
if args.mode == "vla_only":
    if args.baseline_mode == "single":
        args.K = 1
    # baseline_mode == "mean" 时保留用户指定的 --K 值
```

改完后调用：
```bash
python evaluate.py --benchmark object --mode vla_only --baseline_mode mean --K 2 --n_rollouts 20
```

`select_action_vla_only` 的逻辑已经是正确的——它对 K 个 sample 取 mean（第 202-204 行），K=2 时就是 2 个 sample 取均值。

### 3. reconvla --K 2 的实际行为

`reconvla_select` 逻辑：
1. 计算 K 个 sample 的 mean（centroid）
2. 计算每个 sample 到 centroid 的 L2 距离
3. 选距离最小的那个

**K=2 时**：两个 sample 到它们均值的距离是**对称的**（距离相等），所以 `argmin()` 总是返回 index 0（PyTorch tie-breaking 行为）。这意味着 **reconvla K=2 等价于总是选第一个 sample，不具备有意义的选择能力**。这不是 bug，是 K=2 下 argmin-to-centroid 的数学必然。

---
