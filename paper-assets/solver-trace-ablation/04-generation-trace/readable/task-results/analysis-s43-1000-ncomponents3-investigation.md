# analysis s43 1000 ncomponents3 investigation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s43-1000-ncomponents3-investigation_20260515T170724_result.json`
- **Structured JSON:** [`86c76cbddbd0a075b854.json`](../../sessions/86/86c76cbddbd0a075b854.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。现在写调查报告到 artifacts 目录。

## 调查结论

### n_components=3 的含义和来源

`n_components` 是 `decompose_fol()` (`src/sta/components.py`) 对 proof 问题分解出的可消融组件数。s43-1000 中 n_components=3 的构成：

| 组件 | 类型 | 示例 |
|------|------|------|
| 1 | `premise` | `∃x (x = mary ∧ isAdvocate(x))` |
| 2 | `conclusion_quantifier` | `∃x` |
| 3 | `conclusion_whole` | `x = mary ∧ isAdvocate(x)` |

原因：`decompose_fol` 将 conclusion 中的量词 `∃x` 拆分为独立可消融组件。s43-1000 模型的 90 个 proved 全部生成 `∃x (...)` 格式的 tautological formalization（premise = conclusion），所以 conclusion 一律被拆成 quantifier + body = 3 组件。

### 三个 seed 对比

| Seed | n_components | ISR | H7 rate | Component pattern |
|------|-------------|------|---------|-------------------|
| s42 | 3-16（中位数~8） | 0.123 | 0% | 多 premise + conclusion_whole，**无 quantifier 拆分** |
| s43-1000 | **3**（89/90） | **0.531** | **100%** | 1 premise + conclusion_quantifier + conclusion_whole |
| s44-1000 | 6-24（中位数~13） | 0.002 | 0% | 多 premise + conclusion_whole，**无 quantifier 拆分** |

s43-1000 是唯一被 quantifier 拆分影响的 seed — 因为只有它的模型学会了用 `∃x (...)` 格式。s42/s44 的 conclusion 都是 atomic（如 `A(a)`），不触发拆分。

### 确认：n_components=3 IS a parsing artifact

**ISR 分布（90 proved）**：
- ISR=1/3（26 个）：`∃x` 中 x 不在 body 中出现（vacuous quantifier），quantifier 不 necessary → 只有 premise necessary
- ISR=2/3（58 个）：x 出现在 body 中，移除 `∃x` 改变语义 → premise + quantifier 都 necessary
- ISR=1.0（5 个）：`$T` 替换 conclusion_whole 后 Prover9 仍无法证明（solver 对 `$T` 的处理 bug）
- ISR=3/4（1 个）：4 组件的 implication 结构

**反事实计算（去除 quantifier 拆分）**：

| 指标 | 当前值（有 artifact） | 修正值（无 artifact） | 差异 |
|------|---------------------|---------------------|------|
| Overall mean ISR | 0.5308 | **0.4650** | -0.066 (-12%) |
| Proved-only mean ISR | 0.5898 | **0.5167** | -0.073 (-12%) |
| ISR 分布 | 1/3:26, 2/3:58, 3/4:1, 1:5 | **0:2, 0.5:83, 1.0:5** | 大幅简化 |

### 根因分析

ISR=0.531 虚高有两层原因：

1. **根本原因（H7a tautology）**：90/90 proved 全部是 premise=conclusion 的平凡证明，保证 ISR ≥ 0.5（premise 在 `{P} ⊢ P` 中总是 "necessary"，但这种 necessity 毫无推理含义）。

2. **Quantifier 拆分 artifact**：将 `∃x` 作为独立组件多算一个 necessary component（当 x 在 body 中出现时），从 ISR=0.5 拉高到 ISR=0.667，贡献额外 ~0.066 points。

3. **`$T` solver bug**：5 个样本中 Prover9 无法证明 `$T`（可能不是 Prover9 原生常量），false-positive ISR=1.0，贡献额外 ~0.025 points。

### 建议修正方案

1. **论文中**：s43-1000 ISR=0.531 应标注为 "entirely H7a tautological + quantifier decomposition artifact"。真实 ISR（去除 artifact）为 0.465，但即使 0.465 也完全来自 H7a tautology 的 trivial necessity，不代表任何推理质量。

2. **代码修复**（如果需要统一标准）：
   - `decompose_fol()` 中不拆分 conclusion quantifier（将 conclusion 整体作为 `conclusion_whole`），所有 seed 统一 n_components 计算
   - 或者：检测 vacuous quantifier（bound variable 不在 body 中出现），不为其创建 component
   - 修复 `$T` 在 Prover9 中的处理

3. **Explanation 文本 parsing**：98/100 的 formalization 包含 `### Explanation:` 段落。parser 在 98 个中正确处理（regex 在换行处截断），但 folio_149 因 model 在 Premises/Conclusion 之前输出大量 Explanation 文本导致 parsing 失败（该样本 execution_reward=0，未影响 ISR 计算）。

---
