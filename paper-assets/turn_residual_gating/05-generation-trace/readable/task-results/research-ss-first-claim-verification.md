# research ss first claim verification

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ss_first_claim_verification_20260523T213643_result.json`
- **Structured JSON:** [`0115207a8a86c983cf86.json`](../../sessions/01/0115207a8a86c983cf86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SS "首次" Claim 文献核实报告

### 搜索覆盖

| 搜索词 | 相关论文数 |
|--------|-----------|
| `"scheduled sampling" "attention loss" transformer` | 2 (Mihaylova 2019, Dou & Gales 2022) |
| `"exposure bias" "auxiliary attention objective"` | 0 |
| `"scheduled sampling" "attention steering"` | 0 |
| `"curriculum learning" "attention distribution" transformer` | 1 (graph domain, 不相关) |
| `"scheduled sampling" multi-turn dialogue attention` | 2 (TA&AT 2024, Bilevel SS 2023 — 均不涉及 attention objective) |
| `"teacher forcing" "attention" "scheduled sampling" NLP` | 0 新发现 |
| `scheduled sampling auxiliary loss attention allocation` | 0 新发现 |
| + 5 条补充搜索 | 见下文 |

### 直接先例

**未找到。** 没有论文同时满足：
- 使用经典 scheduled sampling（基于时间的课程学习，从 teacher-forcing 线性过渡到 model-generation）
- 应用于 attention distribution 作为训练目标
- 在 multi-turn transformer 场景

### 相关工作（需评估是否引用）

#### 1. Attention Forcing (Zheng et al., 2019) — **建议引用**
- **Venue:** arXiv 1909.12289 / OpenReview (ICLR 2020 提交)
- **做法:** 用 reference attention 引导训练，输入 generated output history + reference attention（非 teacher forcing 的 reference output）
- **与我们的区别:** (a) 不是 scheduled sampling 机制 — 没有时间课程从 TF→AR 过渡；(b) 应用于 cross-attention（encoder-decoder），不是 self-attention；(c) 仅 TTS + 单轮 NMT
- **判断:** 相关但不同。它用 attention 作为引导信号，但不涉及 SS 或 multi-turn

#### 2. Parallel Attention Forcing + Scheduled Attention Forcing (Dou & Gales, 2022) — **强烈建议引用**
- **Venue:** arXiv 2211.03237
- **做法:** 引入 "Scheduled Attention Forcing"：基于 KL(α_t||α̂_t) 与 KL(α_t||α̌_t) 的比较，数据依赖地在两种训练模式间切换；attention KL loss 作为辅助目标
- **与我们的关键区别:**
  - **不是经典 SS:** 论文明确说 "For scheduled sampling, the selection is random. For scheduled attention forcing, the selection depends on the data." 是数据依赖的二元选择，不是时间课程
  - **单轮 NMT:** 不涉及 multi-turn
  - **Cross-attention:** 作用于 encoder-decoder cross-attention，不是 self-attention
- **判断:** 最接近的相关工作。虽然名字含 "scheduled"，但机制不同于经典 SS。论文中 **当前未引用** 此工作

#### 3. TA&AT (2024) — 已间接覆盖
- SS 用于 action/policy sampling（task-oriented dialogue），不涉及 attention objective

#### 4. Mihaylova & Martins (2019) — 已引用 ✓
- SS 扩展到 transformer（两遍解码），但仅用于单轮 NMT 的标准 token prediction

### 结论

- [x] **无直接先例** → "first" claim 可保留
- [ ] 找到直接先例 → 必须修改 claim

"First transfer of scheduled sampling to multi-turn transformer attention objectives" 这个 claim 的三个限定词（scheduled sampling / multi-turn / attention objectives）的交集中，没有找到先例。

### 建议

**1. 必须引用 Parallel Attention Forcing (Dou & Gales, 2022)**

这是最接近的相关工作，reviewer 很可能会找到它。Related work 中应增加讨论，明确区分：

> Dou & Gales (2022) introduced *scheduled attention forcing*, which uses KL-divergence on cross-attention as a data-dependent switch between training modes in single-turn NMT. Our work differs in three respects: (i) we apply classic time-scheduled sampling (linearly increasing $\rho$), not data-dependent selection; (ii) our target is self-attention allocation in multi-turn dialogue; (iii) the scheduled component addresses auxiliary attention objectives rather than the primary translation loss.

**2. 也建议引用 Attention Forcing (Zheng et al., 2019)**

作为使用 attention 作为训练信号的先驱工作。

**3. 建议微调措辞**

当前 claim 用 "first evidence" 已经比 "first" 更审慎。可进一步加强精确度：

当前：
> first evidence that scheduled sampling transfers to multi-turn transformer attention objectives

建议：
> first evidence that *time-scheduled* sampling---linearly mixing model-generated context---transfers to *auxiliary* attention objectives in multi-turn transformers

增加 "time-scheduled" 和 "auxiliary" 两个限定词，进一步与 Dou & Gales 的 data-dependent scheduled attention forcing 区分开。

Sources:
- [Attention Forcing for Sequence-to-sequence Model Training](https://arxiv.org/abs/1909.12289)
- [Parallel Attention Forcing for Machine Translation](https://arxiv.org/abs/2211.03237)
- [Scheduled Sampling for Transformers](https://arxiv.org/abs/1906.07651)
- [TA&AT: Enhancing Task-Oriented Dialog with Turn-Level Auxiliary Tasks and Action-Tree Based Scheduled Sampling](https://arxiv.org/abs/2401.15626)
- [Beyond Self-learned Attention: Mitigating Attention Bias](https://arxiv.org/abs/2402.16790)
- [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120)

---
