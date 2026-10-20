# analysis generalize pythia1b c4 a100 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_generalize_pythia1b_c4_a100_s43_20260518T001906_result.json`
- **Structured JSON:** [`daca5f53c9226a9c89a4.json`](../../sessions/da/daca5f53c9226a9c89a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，实验标记为 **DONE (success)**。

## 结果摘要

**8-pair 分析** ({token_entropy, ece} × {d1, d2, d3, mauve}):

| Method | s43 | s42 (parent) |
|--------|-----|------|
| naive_xcorr | 8/8 | 8/8 |
| diff_xcorr_fdr | 8/8 | 8/8 |
| threshold_onset | 8/8 | 8/8 |
| permg_fwd_fdr | 8/8 | 8/8 |
| permg_rev_fdr | **0/8** | 3/8 |
| ty_granger | 5/8 | — |
| consensus_ge4 | **8/8** | 8/8 |
| token_entropy rev | **0/4** | 0/4 |

**s43 比 s42 更强**：permg_rev 从 3/8 降至 0/8（s42 中 ECE→diversity 的 reverse 显著性在 s43 中消失），单向因果信号更纯净。

drift 幅度高度一致：token_entropy -56.9% vs -57.5%，perplexity +7624% vs +8069%。

C4 域 multi-seed 验证通过，domain robustness 确认非单种子偶然。

---
