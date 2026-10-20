# research c5b literature linkage

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_c5b_literature_linkage_20260514T184841_result.json`
- **Structured JSON:** [`a2fdbe98e7c9e6e3ace2.json`](../../sessions/a2/a2fdbe98e7c9e6e3ace2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。总结如下：

---

## 文献联动结论

**Map 中已有 5 篇论文提供 prior evidence**，其中 SLiM (ICML 2025) 最直接——证明 compound compression error 需要 low-rank compensation 而非 simple redistribution。新增的 Physics of KV Cache Compression (arXiv 2603.01426) 提供了机制层面的解释：**representational rigidity** 导致即使 token 存活、budget 分配最优，attention routing flexibility 仍然崩溃。

**诊断：方法问题，非方向错误。** Phase-awareness 本身有效（ThinKV、PagedEviction 已验证），但 simple redistribution 只解决了 "where to allocate"，没有解决 "how to compensate the interaction term"。Oracle +18% 的天花板反映的是 redistribution 作为工具类的固有局限，而非 phase-gated hypothesis 的失败。

**§8 Future Work 建议引用**：

> Oracle phase-aware redistribution 的有限 recovery（+18%）与 prior work 一致：SLiM [Mozaffari et al., ICML 2025] 证明 compound Q+S 误差非加性且需显式 low-rank 补偿；[arXiv 2603.01426] 发现 "representational rigidity"——head consensus 过度时 routing flexibility 崩溃，与 budget 分配无关。这表明 future compound sparsity mitigation 应从 compensation-based approaches（如建模 cross-axis interaction term 的轻量 adapter）或 learned joint controllers（cf. LKV [arXiv 2605.06676]）入手，而非更精细的 budget redistribution。

已将 Physics of KV Cache Compression 和 R-KV 追加至 literature_map.yaml。

Sources:
- [Physics of KV Cache Compression (arXiv 2603.01426)](https://arxiv.org/abs/2603.01426)
- [R-KV: Redundancy-aware KV Cache Compression (NeurIPS 2025)](https://arxiv.org/abs/2505.24133)

---
