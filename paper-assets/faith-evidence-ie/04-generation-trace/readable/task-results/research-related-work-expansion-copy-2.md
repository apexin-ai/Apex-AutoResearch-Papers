# research related work expansion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-expansion_20260515T230258_result.json`
- **Structured JSON:** [`90772f2dc07661560ce9.json`](../../sessions/90/90772f2dc07661560ce9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`literature_map.yaml` 更新为 25 个类别共 53 篇论文，新增 15 篇覆盖 5 个调研方向：

| 方向 | 新增论文 | 关键文献 |
|------|---------|---------|
| **1. Evidence-based DocRE** | 4 篇 | DREEAM (EACL'23), DocGNRE (EMNLP'23), CDER (2025), Evidence-aware DocRE (CIKM'22) |
| **2. Faithfulness cost** | 3 篇 | "Faithfulness vs Plausibility" (2024), "Does Faithfulness Conflict..." (2024), "Measuring CoT Faithfulness" (EMNLP'25) |
| **3. LoRA/QLoRA artifacts** | 4 篇 | "Illusion of Equivalence" (2024), LoRA phase transition (2024), QeRL (NVIDIA'25), Quantization impact on RL (NeurIPS'25 WS) |
| **4. GRPO beyond RLHF** | 2 篇 | ReasoningNER (2025), Posterior-GRPO (2025) |
| **5. RSFT / Offline RL** | 4 篇 (新增2已有3) | OREO (2024), PCL-Reasoner (2026), RS-DPO (NAACL'24), RAFT (TMLR'24) |

核心发现对论文 positioning 的影响：
- **C2 (QLoRA decoupling)** 现在有"Illusion of Equivalence"的 intruder dimensions 和 LoRA phase transition 理论支撑
- **C1 (evidence tax)** 有 DREEAM/EIDER 作为 DocRE evidence 先驱 + faithfulness cost 量化文献
- **RSFT 优于 GRPO** 有 PCL-Reasoner (math) 和 OREO 作为跨领域 converging evidence

---
