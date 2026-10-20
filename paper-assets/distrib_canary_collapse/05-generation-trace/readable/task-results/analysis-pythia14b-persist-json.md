# analysis pythia14b persist json

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia14b_persist_json_20260517T235150_result.json`
- **Structured JSON:** [`7f4602fddc15764d1511.json`](../../sessions/7f/7f4602fddc15764d1511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存，格式与 C4 版本一致（相同 top-level keys、8 pairs、6 methods）。

结果与任务中的预期值有差异：

| 方法 | 实际 | 预期 |
|------|------|------|
| Naive | 6/8 | 7/8 |
| Diff | 6/8 | 6/8 |
| Thresh | 8/8 | 8/8 |
| PG_fwd | 2/8 | 5/8 |
| PG_rev | 0/8 | 0/8 |
| TY | 0/8 | 0/8 |
| Consensus>=4 | 1/8 | 5/8 |

Naive 差异原因：`ece->distinct_2` 和 `ece->distinct_3` 的 best lag 为 -3（downstream leads canary），naive_pearson 要求 `lag > 0` 才算显著，但 FDR 校正后的 `sig_fdr` 只看 p 值不看 lag 方向。显示逻辑优先使用 `sig_fdr`，导致 lag=-3 的 pair 被标为 SIG（output 显示 6/8），但底层 `significant` 字段为 False。

PG_fwd 差异可能源于 FDR 校正后 p_fdr 超过 0.05 阈值（如 `token_entropy->distinct_1` raw p=0.041 → p_fdr=0.084）。预期值可能来自 raw p 而非 FDR 校正。

JSON 文件路径：`results/generalize/pythia14b_wiki_a100_s42/analysis/pythia14b_8pair_6method_analysis.json`

---
