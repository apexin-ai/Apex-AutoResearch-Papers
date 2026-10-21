# paper fix numerical consistency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_numerical_consistency_20260524T074540_result.json`
- **Structured JSON:** [`7b7a374b35cccfad3f0c.json`](../../sessions/7b/7b7a374b35cccfad3f0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All residual "n=29" references are only in the intentional LaTeX comments. No stale "26/29", "Walker n=13", or "ten factorial" remain.

---

## 修改汇总

### 确定性更新

| 文件 | 行 | 旧值 | 新值 |
|------|-----|------|------|
| abstract_body.tex | 1 | `26/29` | `27/30` |
| introduction.tex | 6 | `26/29 classification ($n{=}29$` | `27/30 classification ($n{=}30$` |
| methodology.tex | 38 | `26/29 accuracy` | `27/30 accuracy` |
| results.tex | 72 | `26 of 29 experimental` | `27 of 30 experimental` |
| results.tex | 102 | `($n{=}29$)` | `($n{=}30$)` |
| conclusion.tex | 4 | `(26/29` | `(27/30` |
| appendix.tex | 123 | `ten factorial experiments` | `eleven factorial experiments` |
| appendix.tex | 134 | *(new row added)* | `059 & 4.72 & self-correcting CIVO & $-$ & $+$` |
| appendix.tex | 154 | `n_neg=7, n=10` | `n_neg=8, n=11` (B1: s5 is B1-negative) |
| appendix.tex | 176 | `n_pos=4, n=10` | `n_pos=5, n=11` (B2: s5 is B2-positive) |
| appendix.tex | 197 | `n_pos=8, n=16, Walker 14` | `n_pos=9, n=17, Walker 15` |
| appendix.tex | 231 | `n{=}29` | `n{=}30` |
| appendix.tex | 236 | `n{=}29` | `n{=}30` |
| appendix.tex | 272 | `n{=}29` (×2) | `n{=}30` (×2) |
| appendix.tex | 277 | `Walker ($n{=}13$)` | `Walker ($n{=}14$)` |
| appendix.tex | 290 | `PickCube & 18` | `PickCube & 19` |
| appendix.tex | 291 | `Cheetah & 15` | `Cheetah & 16` |
| appendix.tex | 292 | `Walker & 7 & 13 & 12/13 (0.923)` | `Walker & 7 & 14 & 13/14 (0.929)` |
| appendix.tex | 294 | Mean accuracy `0.974` | `0.976` |
| appendix.tex | 309 | Mean accuracy `0.974` (prose) | `0.976` |

### AUROC 注释

| 文件 | 位置 | 内容 |
|------|------|------|
| methodology.tex | 39 | `% Note: AUROC computed on original n=29 validation set; exp_059 (s5) correctly classified under same threshold` |
| appendix.tex | 150 | 同上 (B2 AUROC=0.958 prose) |
| appendix.tex | 179 | 同上 (B2 AUROC=0.958 caption) |
| appendix.tex | 244 | 同上 (ROC curve caption) |

### TODO 标记 (9处)

| 文件 | 行 | 内容 |
|------|-----|------|
| methodology.tex | 40 | `TODO: Recalculate LOEO mean AUROC with n=30` |
| conclusion.tex | 11 | `TODO: Recalculate LOEO mean AUROC with n=30` |
| appendix.tex | 157 | `TODO: Recalculate Clopper-Pearson CIs with n=11 (B1)` |
| appendix.tex | 181 | `TODO: Recalculate AUROC and CIs with n=11 (B2)` |
| appendix.tex | 203 | `TODO: Recalculate AUROC and CIs with n=17 (B2 full)` |
| appendix.tex | 238 | `TODO: Regenerate ROC curve figure and bootstrap CI with n=30` |
| appendix.tex | 301 | `TODO: Recalculate Walker fold AUROC and θ_opt ranges` |
| appendix.tex | 304 | `TODO: Recalculate LOEO mean AUROC` |
| appendix.tex | 310 | `TODO: Recalculate LOEO mean AUROC` (prose) |

---
