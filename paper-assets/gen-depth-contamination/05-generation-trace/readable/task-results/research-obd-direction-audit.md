# research obd direction audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_obd_direction_audit_20260513T193011_result.json`
- **Structured JSON:** [`124b5d8ee18cc42e6450.json`](../../sessions/12/124b5d8ee18cc42e6450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有了完整的对比信息。

---

## 核对结果

### 1. 代码中子分类器 label 的方向

**两处 OBD 实现方向一致，均为 `P(Y > k)`：**

- `scripts/run_exp010_ordinal_comparison.py` **第99行**：
  ```python
  y_bin = (y > k).astype(int)
  ```
  注释（第3行、第90行）也写明：`K-1 binary classifiers for P(Y>k)`

- `scripts/exp006_filtering_strategies.py` **第147行**（`Graduated.fit`）：
  ```python
  labels = (depths > k).astype(int)
  ```
  docstring（第132行）：`K-1 binary classifiers for P(depth>k)`

### 2. 预测概率计算公式

两个文件的公式完全一致（以 exp010 为例，第108-114行）：

```python
# P(Y=0) = 1 - P(Y>0)
class_probs[:, 0] = 1.0 - cum_probs[:, 0]
# P(Y=k) = P(Y>k-1) - P(Y>k)   for 0 < k < K
for k in range(1, max_depth):
    class_probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
# P(Y=K) = P(Y>K-1)
class_probs[:, max_depth] = cum_probs[:, max_depth - 1]
```

这是标准的 **P(Y > k) 方向**的 OBD 分解。

### 3. 论文 method.tex 写的方向

`docs/paper/method.tex` 第95-98行：

> The $k$-th sub-classifier estimates:  
> $P(\text{depth} \leq k \mid \mathbf{x}), \quad k = 0, 1, \ldots, K{-}1$

预测公式（第101-103行）：

> $\hat{d}(\mathbf{x}) = \min\{k : P(\text{depth} \leq k \mid \mathbf{x}) > 0.5\}$

### 4. 结论：**论文和代码方向不一致**

| | 论文 method.tex | 代码实际实现 |
|---|---|---|
| 子分类器建模 | $P(\text{depth} \leq k \mid \mathbf{x})$ | `(y > k)` → $P(\text{depth} > k \mid \mathbf{x})$ |
| 概率分解 | 未写明 | $P(Y=k) = P(Y>k{-}1) - P(Y>k)$ |

**差异本质**：$P(\text{depth} \leq k) = 1 - P(\text{depth} > k)$，两者是互补关系。数学上等价——OBD 用哪个方向都能正确分解概率。但论文写的是 $\leq$ 方向，代码实现的是 $>$ 方向，**描述与实现不匹配**。

代码中的概率分解公式 `P(Y=0) = 1 - P(Y>0)` 与 $>$ 方向自洽。如果按论文的 $\leq$ 方向，公式应为 `P(Y=0) = P(Y≤0)`、`P(Y=k) = P(Y≤k) - P(Y≤k-1)`。两套公式数值结果相同，但论文需要改成与代码一致的 $>$ 方向，或者反过来改代码。

---
