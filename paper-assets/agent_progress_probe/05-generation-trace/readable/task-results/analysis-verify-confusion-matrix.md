# analysis verify confusion matrix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-confusion-matrix_20260514T192003_result.json`
- **Structured JSON:** [`5923f55945796ed148ed.json`](../../sessions/59/5923f55945796ed148ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完全确认。以下是最终结论：

---

## 验证结果

### 1. 混淆矩阵

**probe_001 (N=1824, registry 模型)**:
```
              pred=stag  pred=prog
  actual=stag     400        85
  actual=prog      46      1293
```

**checkpoints_full on conf>=2 (N=2206, breakdown 报告的数据)**:
```
              pred=stag  pred=prog
  actual=stag     562       166
  actual=prog      29      1449
```

### 2. precision/recall 正确值

| 指标 | probe_001 (N=1824) | full on conf≥2 (N=2206) |
|---|---|---|
| **precision_stag** | **0.8969** | **0.9509** |
| **recall_stag** | **0.8247** | **0.7720** |
| f1_stag | 0.8593 ✓ (= registry) | 0.8522 |

**Worker 报告 precision_stag=0.95, recall_stag=0.77 是正确的**（对应 N=2206 的 full model）。

### 3. 166 个错误的性质

**166 = FN_stag（missed stagnation）**：实际是 stagnation 但模型预测为 progress。

Reviewer 的错误：JSON 中的 `TN=562, FP=166, FN=29, TP=1449` 是 **progress-centric**（`cm.ravel()` 默认以 label=1 为正类）。Reviewer 直接拿 `562/(562+166)=0.772` 当 precision_stag，实际上这算的是 recall_stag。precision 和 recall 恰好被互换了。

### 4. 结论

**瓶颈是 recall（漏检）**，不是 precision。模型预测 stagnation 时准确率极高（95%），但会漏掉 22.8% 的 stagnation 窗口（错判为 progress）。

### 5. 两个 test set 的区别
- **N=1824**：probe_001 自己的 test split（conf≥2 过滤后再 split），f1_stag=0.8593 = registry 值
- **N=2206**：checkpoints_full 的 test split（全数据 split 后再过滤 conf≥2），f1_stag=0.8522

---
