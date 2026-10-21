# analysis nperm5000 rerun batch1

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nperm5000_rerun_batch1_20260518T105511_result.json`
- **Structured JSON:** [`50e2718cc6256c9c557a.json`](../../sessions/50/50e2718cc6256c9c557a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

n_perm=5000 confirmed in the new runs. The analysis structure changed: now 16 pairs (4 canaries × 4 downstreams) with 5 methods, vs old 8 pairs with 6 methods (PG split into fwd/rev). Here are the results:

## 条件 1: Baseline Pythia-410M s42
```
旧 (8 pairs):  Naive=8/8,  Diff=8/8,  Thresh=8/8,  PG_fwd=6/8, PG_rev=3/8, TY=4/8, K≥4=6/8
新 (16 pairs): Naive=16/16, Diff=16/16, Thresh=10/16, TY=5/16,   PG=10/16,   K≥4=7/16
               Total sig: 57/80
```
**n_perm confirmed: 5000**

## 条件 2: OPT-1.3B s42
```
旧 (8 pairs):  Naive=8/8,  Diff=8/8,  Thresh=8/8,  PG_fwd=6/8, PG_rev=2/8, TY=6/8, K≥4=6/8
新 (16 pairs): Naive=15/16, Diff=11/16, Thresh=8/16, TY=9/16,   PG=9/16,    K≥4=9/16
               Total sig: 52/80
```
**n_perm confirmed: 5000**

## 条件 3: Scale Pythia-1.4B s42
```
旧 (8 pairs):  Naive=7/8,  Diff=6/8,  Thresh=8/8,  PG_fwd=5/8, PG_rev=0/8, TY=0/8, K≥4=5/8
新 (16 pairs): Naive=15/16, Diff=10/16, Thresh=9/16, TY=3/16,   PG=8/16,    K≥4=8/16
               Total sig: 45/80
```
**n_perm confirmed: 5000**

## 关键变化说明

**格式不可直接对比**: 新分析从 8 pairs 扩展到 16 pairs（加入了 ece 和 effective_rank 作为 canary），且 PG 不再分 fwd/rev。所以新旧 sig counts 的分母不同，逐 method 直接比较没有意义。

**如需 apples-to-apples 对比**，需要从 16 pairs 中筛选出与旧 8 pairs 相同的子集（可能是 token_entropy + self_bleu → 4 downstreams = 8 pairs）。要我做这个子集提取吗？

---
