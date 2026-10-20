# diag baseline f1 discrepancy

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_baseline-f1-discrepancy_20260514T152624_result.json`
- **Structured JSON:** [`25869a2db612415698f8.json`](../../sessions/25/25869a2db612415698f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完美复现了两个数字。诊断报告如下：

---

## 诊断结果：probe_001 cross-eval F1 偏差

### 根因：索引空间错位

`lf_holdout_crosseval.py` 存在 bug：它把 `checkpoints/split_info.json` 中的 `test_indices` 直接用于索引全量 `embeddings.pt`（54809 windows），但这些索引实际上是 **conf≥2 过滤后数组**（15401 windows）的索引。

### 机制

1. **probe_001 训练**（`train_probe.py --min_confidence 2`）：先过滤出 conf≥2 的 15401 个 windows，然后在过滤后的数组上做 train/val/test split。`split_info.json` 中 `test_indices` 范围 [33, 15158]，是过滤后数组的索引。

2. **cross-eval 脚本**：加载全量 54809 windows，用 `test_indices` 直接索引 → 取到的是**完全不同的 windows**。

### 量化影响

| | 正确 test set | 错误 test set (cross-eval) |
|---|---|---|
| stagnation | 485 | 454 |
| progress | 1339 | 1370 |
| conf 分布 | conf≥2: 1780, conf=3: 44 | **conf=1: 1318**, conf≥2: 506 |
| **标签错配** | — | **711/1824 (39%)** |
| **macro_f1** | **0.9055** ✓ | **0.8136** ✗ |

### 结论

- **0.9055 是可信的**，是 probe_001 在其正确 test set（conf≥2）上的真实性能
- **0.8136 是错误的**，是因为 cross-eval 取错了 windows（72% 是 conf=1 的低置信度样本，模型从未见过这类数据）
- cross-eval 脚本需要修复：使用 `keep_indices` 先还原过滤，再用 `test_indices` 索引

---
