# code r8 bge indexing bug audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r8_bge_indexing_bug_audit_20260518T072917_result.json`
- **Structured JSON:** [`0095555c43045cb54c91.json`](../../sessions/00/0095555c43045cb54c91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete audit:

---

## 审计结果

### 1. `hs` 的实际 data structure 和 shape

所有 tensor 均为 `(steps, layers, hidden_dim)` 格式：

| Model | Shape (示例) | 含义 |
|-------|-------------|------|
| r1_8b | `(46, 13, 4096)` | 46 steps, 13 layers (L12-24), 4096d |
| ot_7b | `(59, 28, 3584)` | 59 steps, 28 layers, 3584d |
| qwq_32b | `(48, 64, 5120)` | 48 steps, 64 layers, 5120d |
| r1_32b | `(36, 64, 5120)` | 36 steps, 64 layers, 5120d |

### 2. 原脚本的 indexing 方式

`stronger_text_encoder_comparison.py` 第 135 行：
```python
hs = d["hidden_states"][:n_steps, layer_idx, :].float().numpy()
```
**已经是正确的 `[:, layer_idx, :]` 语义**（第一维 steps，第二维选 layer，第三维 hidden_dim）。

### 3. E3 新脚本的 indexing 方式

`bge_bootstrap_bal_acc_fpr.py` 第 94 行：
```python
hs = hs[:, layer_idx, :]
```
与原脚本语义完全相同。

### 4. `hs[layer_idx]` 模式是否存在？

**不存在。** 对 `scripts/` 目录全文 grep `hs[layer_idx]`，返回零结果。所有脚本一致使用 `[:, layer_idx, :]` 或 `[:n_steps, layer_idx, :]`。服务器无 git 历史，无法追溯是否曾经存在过。

### 5. 结果逐项对比

| Model | Metric | 原始结果 | E3 结果 | 一致？ |
|-------|--------|---------|---------|--------|
| r1_8b | HS prec | 0.4971 | 0.4971 | ✓ |
| r1_8b | BGE prec | 0.4358 | 0.4358 | ✓ |
| ot_7b | HS prec | 0.4460 | 0.4460 | ✓ |
| ot_7b | BGE prec | 0.2629 | 0.2629 | ✓ |
| qwq_32b | HS prec | 0.5455 | 0.5455 | ✓ |
| qwq_32b | BGE prec | 0.4540 | 0.4540 | ✓ |
| r1_32b | HS prec | 0.5882 | 0.5882 | ✓ |
| r1_32b | BGE prec | 0.4750 | 0.4750 | ✓ |

所有 point estimates 精确到 6 位小数完全一致。

### 6. 结论

**没有 bug。** E3 worker 声称修复了 `hs[layer_idx]` → `hs[:, layer_idx, :]`，但原脚本 `stronger_text_encoder_comparison.py` 在第 135 行已经使用了正确的 `[:n_steps, layer_idx, :]` indexing。E3 的 "修复" 是一个 no-op，这正好解释了为什么结果完全一致。

**论文 Table 2 的 BGE precision 数字可信。** 原始实验就使用了正确的 layer indexing，E3 独立复现了相同结果。影响范围为零。

---
