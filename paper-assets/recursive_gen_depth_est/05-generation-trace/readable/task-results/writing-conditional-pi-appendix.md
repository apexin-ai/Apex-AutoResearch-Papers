# writing conditional pi appendix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_conditional_pi_appendix_20260522T045550_result.json`
- **Structured JSON:** [`880dd43c2c88193801bc.json`](../../sessions/88/880dd43c2c88193801bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三项改动：

1. **Appendix** (`section_appendix.tex`): 在 §A.2 Permutation Importance 后新增 `\subsection{Conditional Permutation Importance under Multicollinearity}` (`\label{app:conditional_pi}`)，含动机、方法、结果表（top-5 + family-level CPI）、gpt2xl_temp09 排名反转例外、与 Gini 一致性段落。

2. **主文 §4.2** (`atlas.tex`): 在 VIF/group-ablation 脚注后、Table 引用前加入交叉引用句，引用 `\citep{strobl2008_conditional}` 和 `Appendix~\ref{app:conditional_pi}`。

3. **references.bib**: `strobl2008_conditional` 已存在，无需修改。

---
