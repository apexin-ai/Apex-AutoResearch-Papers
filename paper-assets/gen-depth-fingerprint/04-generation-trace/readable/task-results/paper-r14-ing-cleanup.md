# paper r14 ing cleanup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r14-ing-cleanup_20260517T195130_result.json`
- **Structured JSON:** [`2984284e5ef16ff57897.json`](../../sessions/29/2984284e5ef16ff57897.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清零。共修改 47 处，涉及 18 个 .tex 文件。修改清单：

### 正文（8 文件，27 处）

| 文件 | 行 | 原文 | 新文 | 手法 |
|---|---|---|---|---|
| **abstract.tex** | 3 | `, producing recursive chains whose outputs…` | `, and the resulting recursive chains…` | 拆为并列 |
| | 7 | `, restricting current applicability…` | `, which restricts current applicability…` | which 从句 |
| **method.tex** | 7 | `, revealing differential depth response:` | `and reveal differential depth response:` | 并列动词 |
| | 17 | `, enabling finer-grained provenance…` | `, which enables finer-grained provenance…` | which 从句 |
| | 24 | `, enabling evaluation of cross-generator…` | `, which enables evaluation of cross-generator…` | which 从句 |
| | 28 | `, isolating the effect…` | `, which isolates the effect…` | which 从句 |
| | 42 | `, confirming that both feature groups…` | `, which confirms that both feature groups…` | which 从句 |
| | 52 | `NLL, capturing the average…` | `NLL, which captures the average…` | which 从句 |
| | 53 | `NLL, measuring the spread…` | `NLL, which measures the spread…` | which 从句 |
| | 54 | `NLL, capturing the most surprising…` | `NLL, which captures the most surprising…` | which 从句 |
| | 55 | `capturing…reflecting…` | `which captures…; this reflects…` | which + 拆句 |
| | 56 | `, ensuring the classifier…` | `, which ensures the classifier…` | which 从句 |
| | 59 | `, characterizing the shape…` | `and characterizes the shape…` | 并列动词 |
| | 86 | `, confirming that discriminative power…` | `, which confirms that discriminative power…` | which 从句 |
| | 96 | `, ensuring a controlled comparison.` | `to ensure a controlled comparison.` | 目的不定式 |
| **results.tex** | 15 | `, confirming that depth signal persists…` | `, which confirms that depth signal persists…` | which 从句 |
| | 16 | `, making each recursive step…` | `and makes each recursive step…` | 并列动词 |
| | 19 | `, confirming transfer across…` | `, which confirms transfer across…` | which 从句 |
| | 70 | `, supporting "approximately preserves"…` | `, which supports "approximately preserves"…` | which 从句 |
| | 78 | `, confirming DDR is…` | `; this confirms DDR is…` | 分号拆句 |
| | 82 | `, indicating that high-temperature…` | `. This collapse indicates that…` | 拆句 |
| | 113 | `, yielding slightly higher scores…` | `, which yields slightly higher scores…` | which 从句 |
| **discussion.tex** | 12 | `, suggesting that the gen-1/gen-2+…` | `. These results suggest that…` | 拆句 |
| | 13 | `, suggesting compression within…` | `. This pattern suggests compression…` | 拆句 |
| **related_work.tex** | 26 | `, showing progressive information loss.` | `and show progressive information loss.` | 并列动词 |
| | 28 | `, enabling the DDR decomposition…` | `, which enables the DDR decomposition…` | which 从句 |
| | 33 | `, providing an empirical signature…` | `and provides an empirical signature…` | 并列动词 |
| | 39 | `, showing monotonic diversity decline…` | `; these features show monotonic diversity decline…` | 分号拆句 |
| | 46 | `, motivating passive post-hoc methods…` | `, which motivates passive post-hoc methods…` | which 从句 |
| **limitations.tex** | 5 | `, enabling controlled study…` | `and enables controlled study…` | 并列动词 |
| | 24 | `, suggesting that reference model…` | `, which suggests that reference model…` | which 从句 |
| | 28 | `, indicating that depth fingerprinting…` | `, which indicates that depth fingerprinting…` | which 从句 |
| **conclusion.tex** | 6 | `, defining the current scope boundaries.` | `; these limitations define the current scope boundaries.` | 分号拆句 |

### 附录（10 文件，20 处）

| 文件 | 行 | 原文 → 新文 | 手法 |
|---|---|---|---|
| **appendix_prompt_type** | 7 | `, confirming that…` → `, which confirms that…` | which |
| **appendix_qlora** | 30 | `, confirming stability…` → `, which confirms stability…` | which |
| **appendix_cross_temp** | 7 | `, indicating the temperature mismatch…` → `. The temperature mismatch…` | 拆句 |
| | 20 | `, suggesting the coarser…` → `. The coarser…appears…` | 拆句 |
| **appendix_confusion_matrix** | 17 | `, indicating that gen-1 text…` → `. Gen-1 text already…` | 拆句 |
| **appendix_downstream** | 25 | `, confirming the robustness…` → `, which confirms the robustness…` | which |
| | 32 | `, indicating the two…` → `; the two curation strategies…` | 分号 |
| | 35 | `, confirming that data quantity…` → `, which confirms that data quantity…` | which |
| **appendix_human_edit** | 23 | `, indicating that depth signal…` → `, which indicates that depth signal…` | which |
| | 32 | `, making entropy features…` → `and makes entropy features…` | 并列 |
| **appendix_lofo** | 28 | `, confirming that the 7-feature…` → `, which confirms that the 7-feature…` | which |
| **appendix_length** | 10 | `, indicating that depth…` → `; depth does not…` | 分号 |
| | 21 | `, confirming that the 0.046 drop…` → `, which confirms that the 0.046 drop…` | which |
| **appendix_error_analysis** | 10 | `, making the gen-1→gen-2…` → `; the gen-1→gen-2 transition is therefore…` | 分号 |
| | 13 | `, making depth discrimination harder.` → `, which makes depth discrimination harder.` | which |
| | 39 | `, indicating they retain…` → `; these samples retain…` | 分号 |
| **appendix_classifier** | 31 | `, confirming that 3-class…` → `, which confirms that 3-class…` | which |
| **appendix_domain** | 21 | `, demonstrating that depth signal…` → `, which demonstrates that depth signal…` | which |
| | 31 | `, compressing the feature distance…` → `and compresses the feature distance…` | 并列 |
| **appendix_finer_depth** | 52 | `, establishing 3-class granularity…` → `. This establishes 3-class granularity…` | 拆句 |
| | 53 | `, confirming that the bottleneck…` → `, which confirms that the bottleneck…` | which |
| **appendix_feature_distributions** | 18 | `, explaining the classification difficulty…` → `, which explains the classification difficulty…` | which |

---
