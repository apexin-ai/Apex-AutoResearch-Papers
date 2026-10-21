# knowledge scaling section placeholder audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_scaling-section-placeholder-audit_20260520T003309_result.json`
- **Structured JSON:** [`b3a5335c87ee0f785b9c.json`](../../sessions/b3/b3a5335c87ee0f785b9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整的 placeholder 清单。

---

## Placeholder 审计报告

### 1. `docs/paper/sections/experiments.tex` — §5.5 Scaling (L174-210)

**当前状态：§5.5 已基本写完，使用硬编码数值，无 \newcommand placeholder。**

**Table `tab:scale_comparison` (L185-198) 中的 "---" 数据缺口：**

| 行 | 位置 | 缺失值 | 对应实验 |
|----|------|--------|----------|
| L192 | Few-NERD 8B FT | VC, SJ, FK（3个信号相关性） | 8B FT signal 计算 |
| L193 | Few-NERD 72B ZS | Hdr（headroom）, FK（1个信号相关性） | 72B ZS signal 计算 |

**注释掉的元素：**
- L209: `fig:scaling_curve` — 整个图被注释掉（`% Figure: scaling_curve (pending data)`）
- L210: 指向 Version B narrative 的注释

**重要发现：within-family scaling（7B/14B/32B）实验的内容完全不在编译版本中。** §5.5 当前只包含 8B FT vs 72B ZS 对比 + few-shot 分析，没有使用任何 scaling narrative。

---

### 2. `artifacts/scaling_narrative_A_monotonic.tex` — 12 个 placeholder

全部未填（XX.X 格式），依赖 **Qwen2.5 7B/14B/32B FT on Few-NERD** 实验：

| 行 | 命令 | 含义 | 当前值 |
|----|------|------|--------|
| 6 | `\scaleSevenDegen` | 7B degeneracy % | XX.X |
| 7 | `\scaleFourteenDegen` | 14B degeneracy % | XX.X |
| 8 | `\scaleThirtytwoDegen` | 32B degeneracy % | XX.X |
| 9 | `\scaleSevenGreedy` | 7B greedy F1 | .XXX |
| 10 | `\scaleFourteenGreedy` | 14B greedy F1 | .XXX |
| 11 | `\scaleThirtytwoGreedy` | 32B greedy F1 | .XXX |
| 12 | `\scaleSevenConstr` | 7B construction Δ pp | X.XX |
| 13 | `\scaleFourteenConstr` | 14B construction Δ pp | X.XX |
| 14 | `\scaleThirtytwoConstr` | 32B construction Δ pp | X.XX |
| 15 | `\scaleSevenLP` | 7B LP ρ | .XXX |
| 16 | `\scaleFourteenLP` | 14B LP ρ | .XXX |
| 17 | `\scaleThirtytwoLP` | 32B LP ρ | .XXX |

Narrative（L21-30）引用全部 12 个命令。

---

### 3. `artifacts/scaling_narrative_B_nonmonotonic.tex` — 12 个 placeholder

与 Version A 完全相同的 12 个 `\newcommand`，不同的叙事框架（非单调趋势）。实验结果决定选 A 还是 B。

---

### 4. `artifacts/zs_vs_fs_comparison_draft.tex` — 5 个 placeholder

依赖 **72B few-shot on Few-NERD** 实验：

| 行 | 命令 | 含义 | 当前值 |
|----|------|------|--------|
| 6 | `\fsFewnerdLP` | Few-NERD FS LP ρ | --- (gray) |
| 7 | `\fsFewnerdDegen` | Few-NERD FS degeneracy | --- (gray) |
| 8 | `\fsFewnerdConstr` | Few-NERD FS construction Δ | --- (gray) |
| 9 | `\fsFewnerdGreedy` | Few-NERD FS greedy F1 | --- (gray) |
| 10 | `\fsFewnerdOracle` | Few-NERD FS oracle F1 | --- (gray) |

Table L28 的 Few-NERD Few-shot 行使用这 5 个命令。

---

### 写入完成路径

| 实验 | 完成后可填 | 文件 |
|------|-----------|------|
| **Qwen2.5 7B/14B/32B FT on Few-NERD** | 12 个 scale* 命令 + 选择 narrative A or B + 启用 fig:scaling_curve + 将 narrative 插入 experiments.tex §5.5 | `scaling_narrative_A/B.tex` → `experiments.tex` |
| **72B few-shot on Few-NERD** | 5 个 fsFewnerd* 命令 | `zs_vs_fs_comparison_draft.tex` |
| **Few-NERD 8B FT signal 补算** | tab:scale_comparison 中 VC, SJ, FK 三个 "---" | `experiments.tex` L192 |
| **Few-NERD 72B ZS signal 补算** | tab:scale_comparison 中 Hdr, FK 两个 "---" | `experiments.tex` L193 |

**关键路径：** within-family scaling 实验（7B/14B/32B）是最大的缺口——12 个 placeholder + 1 个图 + 1 段 narrative 全部等它的结果。这个实验同时决定用 Version A（单调）还是 Version B（非单调）叙事。ZS vs FS 的 Few-NERD 缺口是次要的（5 个值）。tab:scale_comparison 的 "---" 可能是有意省略（信号未计算），优先级最低。

---
