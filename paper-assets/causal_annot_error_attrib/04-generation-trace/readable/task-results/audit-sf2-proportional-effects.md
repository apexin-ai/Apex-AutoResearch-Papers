# audit sf2 proportional effects

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_sf2_proportional_effects_20260523T175614_result.json`
- **Structured JSON:** [`3c5c57f1d5ea8495336b.json`](../../sessions/3c/3c5c57f1d5ea8495336b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 97.3% 精确来源

**文件**: `artifacts/exp_proportional_real_matrices_results.json`  
**JSON path**: `.non_proportional.sign_preservation_rate`  
**精确值**: `0.9730434782608696` (= 1119/1150)

### 性质判定：**半 empirical，半 synthetic**

实验设计（见 `exp_proportional_real_matrices.py`）：
- **Confusion matrices**: 23 个**真实** LLM 混淆矩阵（civil_comments/humaid/vast × deepseek/qwen/llama4），✓ empirical
- **DGP 参数 (f, g)**: `f ~ N(0,1)` 独立于 `g`（`non_proportional` 组），✗ synthetic
- 50 seeds × 23 matrices = 1150 samples

### 关键问题：措辞与数据不匹配

method.tex L97 写的是：
> "97.3% of empirical LLM configurations **satisfy the condition**"

实际测的是 `sign_preservation_rate`（`sign(τ_direct) == sign(τ_total)`），即**即使 f≠λg（non-proportional），monotonicity 仍以 97.3% 概率保持 sign preservation**。

这是一个 **robustness 指标**，不是"满足 proportional effects 条件"。纸面含义 vs 实际含义有两层错位：

1. **"satisfy the condition"** 暗示 proportional effects (f=λg) 成立 → 实际测的是 sign preservation（不需要 f=λg）
2. **"empirical LLM configurations"** 暗示 f 和 g 来自真实 LLM 任务 → 实际上只有 C 是 empirical，f/g 是随机生成的

### 建议修正文本

当前（method.tex L97）：
```
but 97.3\% of empirical LLM configurations satisfy the condition
```

建议改为（选一）：

**方案 A**（准确描述 sign preservation robustness）：
```
but sign preservation holds in 97.3\% of non-proportional configurations 
tested with 23 empirical LLM confusion matrices
```

**方案 B**（更简洁）：
```
but monotonicity is empirically robust: 97.3\% sign preservation rate 
even under non-proportional effects across 23 LLM confusion matrices
```

---
