# analysis s43 1000 n components investigation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s43-1000-n-components-investigation_20260515T171142_result.json`
- **Structured JSON:** [`948745a7ee76f90818eb.json`](../../sessions/94/948745a7ee76f90818eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是根因分析。

---

## n_components=3 根因分析

### 结论：Explanation 文本**没有**被计入 STA 组件

`_parse_formalization()` 用 `re.search(r"(?:Conclusion|Goal)\s*:\s*(.+)", ...)` 提取 conclusion，只取 "Conclusion:" 后第一行内容。Explanation 在 `---` 分隔线之后，完全不会被解析。

### n_components=3 的真正原因：existential quantifier 拆分

`decompose_fol()` (`components.py:78-96`) 在 conclusion 上执行：
1. `_strip_outer_quantifier()` 检测前导量词 (`∃x`, `∀x` 等) → 拆为独立 `conclusion_quantifier` 组件
2. 剩余 body 作为 `conclusion_whole` 组件

**s43 模型**生成的 FOL 带显式 `∃x (...)` 包装：
```
Premises: ∃x (x = mary ∧ isAdvocate(x))
Conclusion: ∃x (x = mary ∧ isAdvocate(x))
```
→ 3 components: `premise` + `conclusion_quantifier(∃x)` + `conclusion_whole(body)`

**s44 模型**生成简洁格式：
```
Premises: P(a)
Conclusion: P(a)
```
→ 2 components: `premise` + `conclusion_whole`

### ISR 膨胀机制

对于 H7 tautological (premise = conclusion)：

| 格式 | n_components | necessary | ISR |
|------|-------------|-----------|-----|
| s44: `P(a)` | 2 | premise=1 | **1/2 = 0.50** |
| s43: `∃x(...)` | 3 | premise + quantifier = 2 | **2/3 = 0.67** |

`conclusion_quantifier` 被判定 necessary 的原因：ablation 时删除 `∃x` 后，Prover9 将自由变量 `x` 隐式当作全称量化（`∀x`），语义从"存在一个 x"变成"所有 x 都满足"，更强，证明失败。

### s43 的 ISR 分布验证

90 个 proved 样本中：
- **89 个** n_components=3, **1 个** n_components=4
- ISR 值只出现 1/3, 2/3, 3/4, 1.0（全是 /3 或 /4 分数）
- 0 个 n_components=2

对比 s42: n_components 范围 3-16（中位数 ~7），反映真实多前提形式化。

### 对论文的影响

**n_components=3 不是独立 bug，而是 H7 + `∃x` 格式的复合效应。** 修正策略取决于论文如何处理 H7：

1. **如果 H7 已按 C013 从 genuine 中排除**：n_components=3 问题自动消失（s43 的 90/90 proved 全是 H7，排除后 genuine=0，ISR 不参与跨条件比较）

2. **如果需要报告 H7 内部的 ISR 对比**：
   - 不改 `decompose_fol`（conclusion 拆分对 genuine proof 是正确的设计）
   - 报告时标注 s43 的 ISR 受 `∃x` 格式膨胀 +0.17 相对于 s44 同为 H7 的 ISR=0.50
   - 或使用 `premise-only ISR`（仅计算 premise 组件的 necessary 比率），消除 conclusion 拆分差异

3. **不需要修改 eval_sta.py 或 components.py**。

### 修正后 ISR 估算

如果强制 s43 的 conclusion 不拆分（n_components=2）：
- 当前 ISR=0.667 的样本 → 0.50
- 当前 ISR=0.333 的样本 → 0.50
- mean ISR ≈ 0.50（接近 s44 的 0.55）

这证实 s43 vs s44 的 ISR 差异（0.531 vs 0.55）主要由 H7 主导，n_components=3 只是造成了小幅偏差而非根本原因。

---
