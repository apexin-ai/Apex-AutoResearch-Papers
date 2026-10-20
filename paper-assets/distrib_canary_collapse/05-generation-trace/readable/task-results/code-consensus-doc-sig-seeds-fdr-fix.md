# code consensus doc sig seeds fdr fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_consensus_doc_sig_seeds_fdr_fix_20260515T111624_result.json`
- **Structured JSON:** [`414744e8571623398e96.json`](../../sessions/41/414744e8571623398e96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§5.2 sig_seeds 矩阵已修正完毕。两个本地副本均已更新，服务器端无同名文件。

变更汇总（9 个 cell）：

| Cell | 旧值 | FDR 修正值 |
|------|:---:|:---:|
| entropy→d3 perm | 4 | 3 |
| self_bleu→ppl perm | 1 | 0 |
| ece→d1 TY | 3 | 2 |
| eff_rank→d1 perm | 2 | 1 |
| eff_rank→d2 diff | 3 | 2 |
| eff_rank→d2 perm | 2 | 0 |
| eff_rank→d3 diff | 3 | 2 |
| eff_rank→d3 TY | 2 | 1 |
| eff_rank→d3 perm | 2 | 0 |

列总和验证：TY=24 ✓, perm=27 ✓, naive=63 不变 ✓, threshold=35 不变 ✓, diff 55→53（2 cell 微调）✓。§5.3/5.4 数据已一致。

---
