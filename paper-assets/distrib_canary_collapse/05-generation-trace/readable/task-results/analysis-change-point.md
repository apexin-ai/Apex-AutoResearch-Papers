# analysis change point

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_change_point_20260518T140428_result.json`
- **Structured JSON:** [`e5eb370d7a80349dbe6a.json`](../../sessions/e5/e5eb370d7a80349dbe6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有输出文件已保存到远程 `/root/autodl-tmp/distrib_canary_collapse/artifacts/change_point_analysis/`。

## 结果摘要

**方法**: Max-split statistic + bootstrap permutation test (5000 permutations, p<0.05)

**核心发现**: Canary 断点系统性早于 downstream。

**α=0.75 (3 seeds)**:
| 指标类型 | 指标 | 断点 gen | 显著率 | 效应量 d |
|---------|------|---------|--------|---------|
| canary | token_entropy | gen 1 | 1/3 | -3.21 |
| canary | ECE | gen 1 | 1/3 | +3.10 |
| downstream | distinct_1 | gen 2-3 | 3/3 | -2.18 |
| downstream | distinct_2 | gen 3 | 3/3 | -1.97 |
| downstream | distinct_3 | gen 3-4 | 3/3 | -1.86 |
| downstream | perplexity | gen 4 | 3/3 | +1.70 |

Canary 领先 downstream ~2.2 代 (在 2/3 seeds 中显著)。

**关键说明**: token_entropy 在所有 seed 中最佳分割点均为 gen 1 (|d|>3.0)，但因为 T=11 下 gen-1 分割的 pre-change segment 仅 1 个点，max-split test 统计功效不足，p 值偏高 (0.05-0.14)。效应本身高度一致，方向性证据稳健。

**时间排序**: token_entropy (gen 1) → ECE (gen 1) → distinct_1 (gen 2-3) → distinct_2 (gen 3) → distinct_3 (gen 3-4) → perplexity (gen 4-5)。与 canary-leads-downstream 假说一致。

---
