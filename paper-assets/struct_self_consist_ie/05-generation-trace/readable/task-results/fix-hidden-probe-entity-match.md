# fix hidden probe entity match

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hidden_probe_entity_match_20260518T111519_result.json`
- **Structured JSON:** [`bde455c2d9f48b7a3ff1.json`](../../sessions/bd/bde455c2d9f48b7a3ff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Probe 完成。汇总结果：

---

## 调查结果

### 1. entity_set 修复状态
- `hidden_state_probe.py` (v1) **已经是** `(text, type)` — 无需修改
- `hidden_state_probe_v2.py` **仍用** `(start, end, type)` — **已修复**
- `labels.pt` **是用旧 `(start, end, type)` 生成的**，但当前脚本内部已自动用 `(text, type)` 重算 labels

### 2. Greedy F1 ≠ 0.644 的原因
**不是 entity matching 问题。** Probe 数据 (`exp_012_logprob`) 和论文主表 (`exp_012_rerun_1024`) 是**不同的 sample set**：
- 2547/4408 sample pairs 的 entities 不同
- 46/551 instances 的 greedy 输出不同
- `exp_012_rerun_1024` gold-filtered greedy F1 = **0.6441**（与论文一致）
- `exp_012_logprob` gold-filtered greedy F1 = **0.6099**

要得到 greedy=0.644 的 probe 结果，需要用 `exp_012_rerun_1024` 数据**重新提取 hidden states**（需要 GPU）。

### 3. Probe 结果（text,type matching）

```
SciERC (gold-filtered 529 instances, 5-fold CV × 3 seeds, (text,type) matching):
| Method        | Spearman ρ    | Selection F1  | Gap Closure |
|---------------|---------------|---------------|-------------|
| LP            | 0.221         | 0.609         | -0.7%       |
| Hidden Linear | 0.233±0.021   | 0.620±0.004   | 6.3%        |
| Hidden MLP    | 0.454±0.008   | 0.635±0.004   | 15.6%       |
| Greedy        | —             | 0.610         | —           |
| Oracle        | —             | 0.769         | 100%        |
```

MLP 架构: `4096 → 256 (ReLU, Dropout=0.1) → 64 (ReLU, Dropout=0.1) → 1`
- Adam, lr=1e-3, weight_decay=1e-4, batch=256
- 100 epochs max, early stopping patience=15

Hidden states 来源: `Qwen3-8B + SciERC LoRA (merged-v2)`, mean-pool, 4096-dim

### 对比旧结果（start,end,type labels）

| | ρ (MLP) | Sel F1 (MLP) | Gap Closure (MLP) |
|---|---------|-------------|-------------------|
| 旧 (start,end,type) | 0.461±0.020 | 0.632±0.004 | 13.9% |
| **新 (text,type)** | **0.454±0.008** | **0.635±0.004** | **15.6%** |

MLP gap closure 从 13.9% → 15.6%，std 从 0.020 → 0.008（更稳定）。

---
