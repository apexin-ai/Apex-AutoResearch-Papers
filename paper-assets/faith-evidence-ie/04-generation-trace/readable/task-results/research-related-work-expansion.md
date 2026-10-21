# research related work expansion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-expansion_20260515T233120_result.json`
- **Structured JSON:** [`67b435838380baaa053d.json`](../../sessions/67/67b435838380baaa053d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**新增 17 篇论文**（68 → 85），覆盖 5 个方向：

| 方向 | 新增 | 代表论文 |
|------|------|---------|
| Evidence-based DocRE | 3 | EAAGRE, GEGA, KnowRA (IJCAI'25) |
| Faithfulness Structured Output | 4 | G&O, Structural Failures (2026), APIE (AAAI'26) |
| GRPO for Structured Tasks | 4 | E-GRPO (ICLR'26), GRPO-LEAD (EMNLP'25), SFT vs RL |
| QLoRA vs FFT | 2 | RandLoRA (ICLR'25), LoRA Rank Trade-offs |
| MTL Trade-offs in IE | 4 | C-LoRAE, Ortho-LoRA, Proactive Gradient Conflict + Survey |

**对 FREIGE novelty 的影响**：新文献巩固了三个核心贡献的独特性。E-GRPO (ICLR'26) 是 CED reward 最近的 prior work，但它用 entity match 而非 NLI-based evidence quality；Ortho-LoRA 和 RandLoRA 从理论层面支持 QLoRA task decoupling 发现；G&O 和 Structural Failures 独立佐证 faithfulness tax 现象。

**产出**：
- `literature_map.yaml` 已更新（85 papers）
- 调研报告已注册为 artifact `art_20260515_25a2d5`

---
