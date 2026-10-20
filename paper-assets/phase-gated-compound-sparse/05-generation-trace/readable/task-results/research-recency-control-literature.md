# research recency control literature

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_recency_control_literature_20260516T231504_result.json`
- **Structured JSON:** [`d485205a2c8f0ab2a578.json`](../../sessions/d4/d485205a2c8f0ab2a578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 文献调研结果

### Q1: Recency/position-based eviction 作为 control condition 的先例

**无直接先例。** 现有文献中，recency/window eviction 均作为 **performance baseline**（比较方法优劣），而非作为 **methodological control**（排除 scoring mechanism 作为 confound）。

具体角色：
- **H2O** (NeurIPS 2023, 2306.14048): 比较 "local only" vs "H2 only" vs "H2O"，但目的是展示两种 signal 的互补性，不是排除 scoring circularity
- **StreamingLLM** (ICLR 2024, 2309.17453): sink + recent window 作为其方法本身，不作为 control
- **Scissorhands** (2305.17118): 使用 sliding window 作为 baseline 之一

### Q2: FIFO/recency eviction 的已知性质

| 论文 | 关键发现 |
|------|---------|
| StreamingLLM | 纯 window attention 丢失 attention sink 后 perplexity 崩塌 |
| H2O | local-only 比 H2-only 表现更差（2.85%–22.75% 性能退化），说明 recency ≠ importance |
| Hold Onto That Thought (NeurIPS 2025, 2512.12008) | 在 reasoning task 上，heavy-hitter 方法显著优于 StreamingLLM 的 recency 策略 |
| DefensiveKV (ICLR 2026, 2510.13334) | 将 StreamingLLM 归类为 "early method that loses valuable information" |

### Q3: Attention-based vs Position-based 在 reasoning task 上的行为差异

- **"Hold Onto That Thought"** 是最直接的比较：在 GSM8K/MATH500 等 reasoning benchmark 上，H2O/SnapKV-D（attention-based）显著优于 StreamingLLM（position-based），甚至偶尔超越 full-cache
- **ForesightKV** (2602.03203): 针对 reasoning model，学习 long-term contribution，隐含说明 position 信号不足
- **LazyEviction** (2506.15969): 发现 recurring tokens（间歇性重要）被 position-based 方法错误驱逐，导致 reasoning 性能崩塌

### 判断

**我们的 recency control 用法是方法论创新。** 现有文献将 recency eviction 视为一种（次优的）方法或 baseline，但无人将其作为 scoring-independent control 来检验 "观察到的 phase gradient 是否源于 attention scoring mechanism 本身"。

**论文中可以这样 claim：**
> While prior work (H2O, StreamingLLM) has established that recency-based eviction underperforms attention-based methods, we repurpose it as a scoring-independent control to isolate whether observed phase-dependent behavior arises from the eviction mechanism itself or specifically from attention-score-based token selection.

可引用 H2O 和 "Hold Onto That Thought" 作为 recency eviction 性质的支撑文献，同时指出我们的 control design 用法是新的。

Sources:
- [H2O: Heavy-Hitter Oracle (NeurIPS 2023)](https://arxiv.org/abs/2306.14048)
- [StreamingLLM (ICLR 2024)](https://arxiv.org/abs/2309.17453)
- [Hold Onto That Thought (NeurIPS 2025)](https://arxiv.org/abs/2512.12008)
- [DefensiveKV (ICLR 2026)](https://arxiv.org/abs/2510.13334)
- [Scissorhands](https://arxiv.org/abs/2305.17118)
- [ForesightKV](https://arxiv.org/html/2602.03203v1)
- [LazyEviction](https://arxiv.org/html/2506.15969)

---
