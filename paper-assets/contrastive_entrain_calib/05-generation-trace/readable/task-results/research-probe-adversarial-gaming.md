# research probe adversarial gaming

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_probe-adversarial-gaming_20260518T215222_result.json`
- **Structured JSON:** [`087c7535f010faad71b2.json`](../../sessions/08/087c7535f010faad71b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/research/probe_gaming_literature.md` 并注册。

覆盖内容：
- **6 个主题区块**：reward hacking 理论与实证（Gao, Skalse, Wen, Denison 等 12 篇）、sycophancy 问题与缓解（Sharma, Shapira, Wang, Wei 等 8 篇）、RepE/activation steering（Zou, Li/ITI, Turner/ActAdd, Rimsky/CAA, Burns/CCS 等 7 篇）、REINFORCE/非可微 reward 信号（GRPO, GRADE, ZO-PG 等 4 篇）、probe 作为训练信号的脆弱性分析
- **分级引用建议**：Tier 1 必引 8 篇、Tier 2 强烈推荐 10 篇、Tier 3 可选 10 篇
- **叙事定位建议**：从 sycophancy 是 RLHF 基础缺陷 → reward hacking 是底层机制 → RepE 提供新范式 → DC-GRPO 将 RepE 从推理时扩展到训练时 → probe gaming (exp-008) 提供实证支撑

关键发现：**没有先前工作明确记录 linear probe 作为可微 reward signal 时被 adversarial gaming 的现象**。这是论文的原创实证贡献。最接近的相关工作是 Latent-GRPO（Zhang et al. 2026），同样用表示空间几何作 GRPO reward，但针对推理正确性而非行为属性，且使用聚类而非方向投影。

---
