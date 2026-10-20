# fix d132 cascade items 2to5 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d132_cascade_items_2to5_v2_20260518T052720_result.json`
- **Structured JSON:** [`16919282c0c0adc84f7a.json`](../../sessions/16/16919282c0c0adc84f7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed: N=8 CoNLL gives 59.0% (~59.1%), while N=16 gives 48.3%. The table has the wrong value. All data is now collected.

## #2 tab:degeneracy N=16 CoNLL
- N=16 实验: `output/exp_002_conll_n16/`
- N=16 F1-based degeneracy (gf): **48.3%**
- N=8 验证: 59.0% (与论文 59.1% 一致，确认论文误用了 N=8 值)
- 论文当前值: 59.1%
- 需要更新: **YES** (59.1% → 48.3%)

## #3 N-scaling LP Δ
- 论文当前值: +0.42pp (appendix L978, tab:n_scaling_selection, N=8 行)
- 来自旧 full-set: **YES** (脚注明确 "full 551-instance test set"，gold-filtered 为 529)
- 正确 gf max_LP N=8 值 (exp_012_rerun_1024): **+0.61pp**
- 需要更新: **YES** (整个 N-scaling 表需用 gold-filtered 重算；N=8 LP 行从 +0.42 → ~+0.61pp)

## #4 LLaMA degeneracy
- 论文当前值: 89.2% (discussion.tex L11)
- 当前定义: 不确定来源，但与 F1-based 和 keyset-based 均不完全匹配
- F1-based gf 值: **86.4%** (2380/2756)
- Keyset-based gf 值: 84.9% (2340/2756)
- 89.2% 可能来自 non-gold-filtered 或 N=8 实验
- 需要更新: **YES** (89.2% → 86.4% F1-based gf)

## #5 p-value
- 实验: exp_012_rerun_1024, gold-filtered n=529
- LP selection mean delta: +0.61pp
- Permutation test (10000 permutations, two-sided): **p = 0.3860**
- +0.61pp p=0.386

---
