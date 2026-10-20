# paper round3 p0 text fixes

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round3_p0_text_fixes_20260524T080553_result.json`
- **Structured JSON:** [`74d18325df75b89607e1.json`](../../sessions/74/74d18325df75b89607e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。修改清单：

### Task 1: ManiSkill sparse→dense
| 文件:行 | 旧 | 新 |
|---|---|---|
| `analysis.tex:11` | "manipulation rewards are sparse and contact-gated" + reward density hypothesis | "Both domains use dense shaped rewards..." + 新 mediator 讨论（periodicity, observation structure, contact-gated dynamics）+ "remain an open question" |
| `appendix.tex:725` | "sparse-reward failure" / "sparse-reward manipulation tasks" / "sparse rewards" | "manipulation failure" / "manipulation tasks" / "contact-gated dynamics" |
| `appendix.tex:863` | "a manipulation task with sparse rewards" | "a dense-reward manipulation task" |

### Task 2: structural factor → hypothesized
| 文件:行 | 旧 | 新 |
|---|---|---|
| `abstract_body.tex:1` | "as the structural factor" | "as a hypothesized structural factor" |
| `conclusion.tex:4` | "is the structural factor." | "is the hypothesized structural factor. Empirical validation on MPC-based architectures (e.g., TD-MPC2) remains future work." |

### Task 3: exp_045 extended run
| 文件 | 变更 |
|---|---|
| `analysis.tex` (Practitioner guidelines 后) | 新增 `\paragraph{Training horizon and extended dynamics.}` — 105K rationale + exp\_045 505K 自恢复数据（NVE 4.91× → 0.05×, eval 867.6 = 94.7% baseline, 170K extra steps）|

### Task 5: Detector 降级
| 文件:行 | 旧 | 新 |
|---|---|---|
| `introduction.tex:14` | "**Online detection.** A lightweight NVE-based detector achieves 100% sensitivity (5/5)" | "**Preliminary diagnostic.** A proof-of-concept NVE-based detector achieves TPR 95% CI [47.8%, 100%] (n=5/5), FPR 22% (2/9)" |
| `results.tex:177` | "it achieves TPR=5/5, FPR=2/9" | "it achieves TPR=5/5 (95% Clopper-Pearson CI [47.8%, 100%]), FPR=2/9 (22%)" + 新增 "The detector requires larger-sample validation..." |

### Task 6: irreversible → sustained
| 文件:行 | 旧 | 新 |
|---|---|---|
| `results.tex:80` | "6/7 suffering irreversible policy collapse" | "6/7 suffering sustained policy collapse within the observation window" |
| `appendix.tex:627` | "may be irreversible even when" | "persists even when" |
| `appendix.tex:720` | "is irreversible even when the critic" | "persists within the observation window even when the critic" |

### Task 7: Abstract 精简
- 删除 "2.78×"（保留 "reward prediction gap"）
- 删除 "ρ>0.999"（保留 "dual critics converge in pure imagination"）
- 删除 "A lightweight NVE detector achieves 100% sensitivity"（已移至 contribution）
- "isolate" → "identify"

### Task 8: Dual-critic nuance
| 文件 | 变更 |
|---|---|
| `results.tex:165` (critic convergence 段落后) | 新增 "While critic convergence renders pessimistic value estimation ineffective as a standard mechanism, the min operation in wide dual-critic may provide regularization through alternative mechanisms such as gradient diversity or implicit capacity constraints." |

### Task 9: Table 1 baseline
| 文件 | 变更 |
|---|---|
| `results.tex` Table 1 脚注 | 新增 vanilla DreamerV3 baseline 行：Walker 915.7, Cheetah ~320, PickCube via exp\_019a\_v2, StackCube/PegInsertion "---" |

### Task 10: Figure 6
- 主体 10 页，超 8 页限制 → Figure 6 留 Appendix
- `results.tex:103` 加显式引用 "see Figure~\ref{fig:multiple_pathways} in Appendix"

### 验证
- `grep sparse.*reward` → 0 matches
- `grep irreversible` → 0 matches
- `grep structural factor` → 3 matches，全部含 "hypothesized" 或 "open question" 语境
- `pdflatex` 编译通过，无 Error

---
