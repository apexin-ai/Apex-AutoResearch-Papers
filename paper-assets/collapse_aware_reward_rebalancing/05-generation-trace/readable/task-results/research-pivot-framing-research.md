# research pivot framing research

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pivot_framing_research_20260516T210031_result.json`
- **Structured JSON:** [`407d78a7c00dcedf5fe7.json`](../../sessions/40/407d78a7c00dcedf5fe7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，已写入 memory.md。核心结论：

---

**评级：B-（可行但有显著风险）**

**关键发现：**

1. **"Stagnation" 精确观察无人提出**，但相邻空间已很拥挤——DIVE（iterative self-improvement diversity loss）、DARLING（Facebook，quality-diversity co-optimization via RL）、CD-RLHF（ACL 2025，curiosity-driven diversity）都在打这个方向。

2. **"Stagnation" 比 "collapse" 弱**，但有先例：DARLING/GEM 都用 positive framing（"jointly improve" / "preserve"），不需要 claim failure mode。建议 framing：**"unlocks diversity-quality co-improvement under iterative reward curation"**。

3. **现有数据只证明问题存在，不证明 CARR 有效**。必须跑 CARR 实验并且 diversity growth ≥ baseline 的 +3%。如果 CARR 只补回 1-2pp，effect size 太小。

4. **时间风险**：DDL 9 天，CARR 效果实验 + 论文撰写压力极大。

**最直接竞争者需仔细区分：**
- vs DIVE：我们是 external reward signal curation，他们是 self-play
- vs DARLING：我们是 curation-time 权重调节（lightweight），他们是 training objective 修改
- vs CD-RLHF：我们是 iterative multi-round，他们是 single-round intrinsic reward

Sources:
- [DIVE: Diversified Iterative Self-Improvement](https://arxiv.org/abs/2501.00747)
- [DARLING: Jointly Reinforcing Diversity and Quality](https://arxiv.org/abs/2509.02534)
- [CD-RLHF: Curiosity-Driven RLHF](https://arxiv.org/abs/2501.11463)
- [GEM: Preserving Diversity in Supervised Fine-Tuning](https://arxiv.org/abs/2408.16673)
- [Kirk et al.: Understanding Effects of RLHF on Diversity](https://arxiv.org/abs/2310.06452)

---
