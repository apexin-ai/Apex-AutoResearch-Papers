# research inverted ema failure literature

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_inverted_ema_failure_literature_20260512T172021_result.json`
- **Structured JSON:** [`6c07f8c598a15981bef8.json`](../../sessions/6c/6c07f8c598a15981bef8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成文献搜索，在现有 `literature_map.yaml` 中新增了 **Failure Mode Analysis** 板块，包含 6 篇新论文和综合分析。

## 核心发现

**高相关 (high relevance) — 3 篇：**

| 论文 | 与我们的关系 |
|------|------------|
| [KeyDiff](https://arxiv.org/abs/2504.15364) | 最直接对比。同样用 centroid（cache mean）做 eviction，驱逐高相似度冗余 token，<0.04% 损失。关键差异：每步**精确重算** mean，而非 EMA 平滑 |
| [DefensiveKV](https://arxiv.org/abs/2510.13334) (ICLR'26) | 直接解释失败机制：mean aggregation 的 stability assumption 脆弱，importance 突变时 mean/EMA 聚合灾难性失败，损失是 defensive aggregation 的 2.3-4.3× |
| [Pitfalls of KV Cache Compression](https://arxiv.org/abs/2510.00231) | 系统性失效模式：selective amnesia，部分 instruction 被完全忽略，eviction bias 是关键因素 |

**中相关 (medium relevance) — 3 篇：** [Attention Sink](https://arxiv.org/abs/2410.10781) (ICLR'25 Spotlight)、[Lost in the Middle](https://arxiv.org/abs/2307.03172) (TACL'24)、[HashEvict](https://arxiv.org/abs/2412.16187) — 解释 recency 为何是强 baseline 以及 pre-attention query-aware scoring 的可行路径。

**已有文件中的相关方法：** [H2O](https://arxiv.org/abs/2306.14048)、[StreamingLLM](https://arxiv.org/abs/2309.17453)、[NACL](https://arxiv.org/abs/2408.03675) — 已在原有条目中。

## 结论

**"方法问题"，非"hypothesis 方向错"。** Centroid-based eviction 思路本身可行（KeyDiff 证明），但 EMA smoothing 导致 centroid 收敛到全局均值丧失区分度，mean aggregation 在 importance 突变时脆弱（DefensiveKV 证明），random eviction 通过多样性采样提供隐式 robustness 是任何确定性 scoring 的门槛（NACL 经验）。修正方向：精确 per-step centroid + diversity maximization，或 query-aware pre-attention scoring。

---
