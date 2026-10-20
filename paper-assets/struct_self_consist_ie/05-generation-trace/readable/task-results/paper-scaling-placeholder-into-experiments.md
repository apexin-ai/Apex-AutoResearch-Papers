# paper scaling placeholder into experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_scaling-placeholder-into-experiments_20260519T220841_result.json`
- **Structured JSON:** [`20db9883f64ea90328a5.json`](../../sessions/20/20db9883f64ea90328a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。experiments.tex 中新增内容位于 §5.5 Scaling Behavior：

**插入位置和内容：**
- **L183–195**: 12 个 `\newcommand` placeholder（7B/14B/32B 的 degen、greedy、constr、LP）
- **L225–234**: Version A 叙事段落 — "Degeneracy rises with scale within a model family"，含三维证据收敛（scale/epoch/family）
- **L236–251**: Table `tab:scaling_ft` — 7B/14B/32B/8B 对比表，8B 行填入已知值
- **L253–258**: Figure `fig:scaling_curve` placeholder（`\includegraphics` 已注释）
- **L260**: Version B 备选注释

**待填 placeholder 清单（12 个）：**

| 命令 | 含义 |
|------|------|
| `\scaleSevenDegen` | 7B degeneracy % |
| `\scaleFourteenDegen` | 14B degeneracy % |
| `\scaleThirtytwoDegen` | 32B degeneracy % |
| `\scaleSevenGreedy` | 7B greedy F1 |
| `\scaleFourteenGreedy` | 14B greedy F1 |
| `\scaleThirtytwoGreedy` | 32B greedy F1 |
| `\scaleSevenConstr` | 7B construction Δ (pp) |
| `\scaleFourteenConstr` | 14B construction Δ (pp) |
| `\scaleThirtytwoConstr` | 32B construction Δ (pp) |
| `\scaleSevenLP` | 7B LP ρ |
| `\scaleFourteenLP` | 14B LP ρ |
| `\scaleThirtytwoLP` | 32B LP ρ |

Table 中 SJ ρ 列 7B/14B/32B 也为 `---`，待实验数据补充。Figure 的 `scaling_curve.pdf` 待生成。

---
