# paper theory critical fixes v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_theory_critical_fixes_v2_20260517T193930_result.json`
- **Structured JSON:** [`a63160e0ce3a71db9d64.json`](../../sessions/a6/a63160e0ce3a71db9d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary:

---

## 变更日志

### theory_draft.tex

| 位置 | 修改内容 |
|------|----------|
| Line 82 | `\begin{theorem}[EDD Upper Bound]` → `\begin{proposition}[EDD Upper Bound (Conditional)]` |
| Line 84 | 添加 `($\gamma$-contraction)` 说明条件依赖 |
| Line 90 | `\end{theorem}` → `\end{proposition}` |
| Line 100 | `Theorem~\ref{thm:edd} reveals` → `Proposition~\ref{thm:edd}, conditional on Assumption~\ref{asm:contraction}, reveals` |
| Line 110 | AUC 值: 0.922→0.953, 0.802→0.862, 0.712→0.766, 0.653→0.683 |
| Line 110 | 删除 "γ≈0.75 in KL-divergence space" 和 "AUC decay ratio ≈0.87" |
| Line 110 | 替换为 "geometric decay in AUC-excess (AUC - 0.5) with contraction factor γ ≈ 0.74" |
| Line 110 | `Theorem~\ref{thm:edd}` → `Proposition~\ref{thm:edd}` |

### theory_section_draft.md

| 位置 | 修改内容 |
|------|----------|
| Line 28 | AUC 值: 0.922→0.953, 0.802→0.862, 0.712→0.766 |
| Line 49 | "lower-bounded by their total variation distance" → "as KL divergence decreases, TV decreases (Pinsker: TV ≤ √(KL/2)), which in turn implies AUC approaches 0.5 (since AUC ≤ 0.5 + TV)" |
| Line 59 | AUC 序列: 0.922���0.953, 0.802→0.862, 0.712→0.766, 0.653→0.683 |
| Line 59 | 删除 "γ≈0.75 in KL-divergence space" 和 "AUC decay ratio ≈0.87" |
| Line 59 | 替换为 "geometric decay in AUC-excess (AUC - 0.5) with contraction factor γ ≈ 0.74" |

### 验证清单结果
1. 0.922, 0.802, 0.712, 0.653 → 全部消失 ✓
2. 0.75.*KL → 消失 ✓
3. 0.87 ��� 消失 ✓
4. "theorem" for EDD → 已变为 Proposition（Tail Contraction theorem 保留，非修改目标） ✓
5. "lower-bound" → 消失 ✓
6. d3v4 mean 0.766 与 range [0.750, 0.784] 一致 ✓
7. d4v5 range [0.681, 0.684] 与 mean 0.683 一致 ✓

### d0v1 Mean AUC

来源: `pairwise_auc.json` (random_forest classifier, depth_extension experiments)
- Pythia: **0.9962**
- GPT2-XL: **0.9951**
- OLMo: **0.9946**
- **3-model mean: 0.995**

注: binary_pairwise_results.json 中未��含 d0v1 pair（可能因为近乎完美而未单独跑），数据取自同一实验框架的 pairwise_auc.json random_forest 结果。

---
