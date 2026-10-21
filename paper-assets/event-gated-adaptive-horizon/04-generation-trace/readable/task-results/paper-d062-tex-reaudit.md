# paper d062 tex reaudit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d062-tex-reaudit_20260516T071236_result.json`
- **Structured JSON:** [`13958b748da7a2d1065f.json`](../../sessions/13/13958b748da7a2d1065f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

"untrained" 已完全清除。所有 "causal factor/trigger" 均已修正为组合表述。

---

## 检查结果清单

### 1. `introduction.tex` — 已修复
| 问题 | 修复 |
|------|------|
| L6: "we isolate the *trained* $\dt$-embedding as the causal factor" | → "we isolate the combination of a *trained* $\dt$-embedding and multi-rate data exposure as the causal trigger. This trained-and-exposed embedding enables..." |
| 无 "untrained"/"utr" | ✓ 无需修改 |
| 无 006/007 Sub OFF 错误 | ✓ 无需修改 |

### 2. `abstract.tex` — 已修复
| 问题 | 修复 |
|------|------|
| L2: "we identify trained temporal embedding as the causal factor" | → "we identify the combination of trained temporal embedding and multi-rate data exposure as the causal trigger" |
| 无 "untrained"/"utr" | ✓ 无需修改 |

### 3. `conclusion.tex` — 已修复（2处）
| 问题 | 修复 |
|------|------|
| L4: "identifying trained $\dt$-embedding as the causal factor" | → "identifying the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor" |
| L8: "Trained $\dt$-embedding is the causal factor; **untrained** or removed embeddings prevent overestimation" | → "The combination of trained $\dt$-embedding and multi-rate data exposure is the causal factor; **unexposed, frozen, or removed** embeddings prevent overestimation" |

### 4. `analysis.tex` — 已修复（1处）
| 问题 | 修复 |
|------|------|
| L4: "trained $\dt$-embedding is the causal factor behind pathological value dynamics" | → "the combination of trained $\dt$-embedding and multi-rate data exposure is the causal factor behind..." |
| 其余内容（CIVO 机制、seed divergence、MPC immunity、embedding dilemma）| ✓ 无问题，正确使用 "no-embedding (008f)"、"trained embedding" 等 |

### 5. `related_work.tex` — 无需修改
✓ 无 "untrained"、"utr"、旧因果叙事。全文仅讨论他人工作的方法论对比。

### 6. `appendix.tex` — 无需修改
✓ 纯数值表格和阈值分析，无 D062 相关术语问题。

### 7. `main.tex` — 无需修改
✓ 仅框架文件（documentclass、usepackage、\input），无文本内容。

### 8. `methodology.tex` — 已修复（2处回退）
| 问题 | 修复 |
|------|------|
| L19: `\textbf{Untrained}` 标题（旧术语，应为 Frozen） | → `\textbf{Frozen}: a fixed random projection... (\texttt{requires\_grad=False})` |
| L32: "trained / untrained / none" | → "trained / frozen / none" |
| 表格（trn/exp/frz/---）、脚注、四分类表述 | ✓ 均正确，006/007 Sub=ON，005 Sub=OFF Emb=adaptive，008a/008c 标注为 exp |

### 9. `results.tex` — 已修复（1处）
| 问题 | 修复 |
|------|------|
| L229: "trained $\dt$-embedding as the causal factor" | → "the combination of trained $\dt$-embedding and multi-rate data exposure as the causal factor" |
| 表格 Tab1: 006 trn/ON, 007 trn/ON, 005 adaptive/OFF, 008a exp/OFF, 008c exp/OFF, 015b frz/ON | ✓ 均正确 |
| 无 "untrained"/"utr" | ✓ |

---

**总计修改 8 处**，涉及 6 个文件。"untrained" 已完全清除（0 残留），所有因果叙事均已修正为 "trained embedding + multi-rate data exposure" 的组合表述。

---
