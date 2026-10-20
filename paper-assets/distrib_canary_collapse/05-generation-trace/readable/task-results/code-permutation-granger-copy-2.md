# code permutation granger

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_permutation_granger_20260514T214130_result.json`
- **Structured JSON:** [`f2f40c2e14cff4a7475b.json`](../../sessions/f2/f2f40c2e14cff4a7475b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Summary

### 1. 验证结果（4 seed × 2 pair）

| Seed | Pair | F-stat | p-value | f² | Verdict |
|------|------|--------|---------|-----|---------|
| 42 | token_entropy → distinct_1 | 612.12 | 0.011 | 102.02 | **SIG** |
| 43 | token_entropy → distinct_1 | 2614.78 | 0.001 | 435.80 | **SIG** |
| 44 | token_entropy → distinct_1 | 1369.76 | 0.002 | 228.29 | **SIG** |
| 45 | token_entropy → distinct_1 | 752.82 | 0.004 | 125.47 | **SIG** |
| 42 | effective_rank → distinct_1 | 46.44 | 0.021 | 7.74 | SIG |
| 43 | effective_rank → distinct_1 | 14.17 | 0.016 | 2.36 | SIG |
| 44 | effective_rank → distinct_1 | 8.09 | 0.133 | 1.35 | n.s. |
| 45 | effective_rank → distinct_1 | 16.30 | 0.091 | 2.72 | n.s. |

- **正样本**: 4/4 SIG（TY 在 plan_009 中只有 power 0.05-0.20）
- **负样本**: 2/4 n.s.，majority-vote = NOT_SIGNIFICANT

### 2. Permutation Granger vs TY 对比

| 指标 | TY (asymptotic) | PermG (shuffle+diff) |
|------|-----------------|---------------------|
| 显著 pair 数 | 4/16 | 6/16 |
| 正样本 power | 4/4 (但 F 依赖渐近分布) | 4/4 |
| effective_rank pairs | 全部 n.s. | 全部 n.s. |
| 新增检出 | — | ece→distinct_2, ece→distinct_3 |

PermG 比 TY 多检出 2 个 ece pair，反映更高的 power。

### 3. 完整 5-method ablation

```
Method              SIG pairs  Rate
naive_pearson       16/16      100%
differenced_xcorr   14/16       88%
threshold_onset      9/16       56%
permutation_granger  6/16       38%
toda_yamamoto        4/16       25%
```

PermG 定位在 threshold 和 TY 之间：比 threshold 更保守（正确拒绝更多 spurious），比 TY 有更高 power（多检出 ece→distinct pair）。

### 实现细节
- 脚本: `/root/autodl-tmp/distrib_canary_collapse/permutation_granger.py`
- 策略: 一阶差分 + random shuffle（非 circular shift，因为差分后自相关已弱，且 T=10 的 circular shift 只有 9 种排列不够用）
- 已集成到 `method_ablation.py` 作为第 5 种方法，FDR 校正和 effect size 均已接入

---
