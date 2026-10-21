# analysis s43 1000 n components investigation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s43-1000-n_components-investigation_20260515T164625_result.json`
- **Structured JSON:** [`4ba3e9404436c0e79eed.json`](../../sessions/4b/4ba3e9404436c0e79eed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。让我整理下发现的完整内容。

---

## 调查结论：s43-1000-r2 的 n_components=3 是 parsing artifact

### n_components=3 的来源

`decompose_fol()` 将每个 proved 样本分解为 3 个组件：
1. **premise** — 唯一的一条前提
2. **conclusion_quantifier** — 从 conclusion 剥离的 `∃x` 或 `∀x`
3. **conclusion_whole** — 去掉量词后的 body

s43-1000-r2 的 **全部 90 个 proved 样本都是 H7 tautological**（单条 premise == conclusion）。模型只生成 1 条 premise 就是 conclusion 的复制。

### ISR 被抬高的机制

ISR = n_necessary / n_components。对于 H7 + 单 premise + `∃x(P(x))` 结构：

| 组件 | Ablation 操作 | 结果 | 原因 |
|------|-------------|------|------|
| premise | 删除唯一前提 | **necessary** (58) 或 not (2) | 2 个 `∃x(x=Jack)` 恰好是 FOL 等式 tautology |
| conclusion_quantifier `∃x` | 剥离量词 | **necessary** (63) 或 not (26) | 取决于 x 是否在 body 中出现及量词类型 |
| conclusion_whole | 替换为 `$T` | **not necessary** (84) 或 necessary (5) | 5 个含 `¬` 的 body 疑似 `$T` Prover9 兼容问题 |

关键 artifact：**剥离 `∃x` 后 body 中的自由变量 x 被 Prover9 默认全称量化**（`∃x` → `∀x`），使得从 `∃x(P(x))` 的 premise 无法证明 `∀x(P(x))` 的 conclusion，于是量词被判为 necessary。这不是推理能力，是 Prover9 的自由变量约定。

### ISR 分布

| ISR | 数量 | 原因 |
|-----|------|------|
| 0.667 | 58 | `∃x` + x 在 body 中使用 → 量词 necessary, 2/3 |
| 0.333 | 26 | `∀x`（5个）或 `∃x` 中 x 未使用（19个）或等式 tautology（2个）→ 1/3 |
| 1.000 | 5 | `∃x` + 含 `¬` 的 body → `$T` 替换疑似 Prover9 不兼容 → 3/3 |
| 0.750 | 1 | n_components=4 的特殊情况 |

### s42 vs s43 对比

两者都是 H7 主导，ISR 差异完全由生成的 premise 数量决定：

| | s42 | s43 |
|--|-----|-----|
| H7 占比 | 81/93 (87%) | **90/90 (100%)** |
| n_components | 3~16（中位~7） | **几乎全是 3** |
| 典型 ISR | 1/7 ≈ 0.14 | **2/3 ≈ 0.67** |
| 报告 mean ISR | 0.123 | **0.531** |

s42 生成 6-7 条冗余 premise（拉大分母），s43 只生成 1 条（分母小 + conclusion 拆分占 2/3）。

### 影响与修正

- **修正后 ISR = 0.0**：全部 90 proved 均为 H7，按 C013 taxonomy 应被分类为 H7 并排除。无 genuine 推理样本。
- **论文影响**：如果论文中引用了 s43 ISR=0.531，必须修正。s43 与 s42/s44 一样本质上 ISR=0（纯 H7），表观差异完全是 n_components parsing artifact。
- **额外 bug**：5 个 ISR=1.0 样本是 `$T` 在 Prover9 中的兼容性问题（conclusion_whole ablation 应该总返回 proved，但对含 `¬` 的 body 失败了）。

---
