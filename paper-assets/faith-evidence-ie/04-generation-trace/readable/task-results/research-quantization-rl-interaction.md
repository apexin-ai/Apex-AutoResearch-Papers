# research quantization rl interaction

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_quantization-rl-interaction_20260515T174945_result.json`
- **Structured JSON:** [`405d60d8543ba6539b71.json`](../../sessions/40/405d60d8543ba6539b71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献综述已写入 `artifacts/literature_quantization_rl.md`，覆盖 4 个方向共 18 篇论文。

核心发现：

**有直接先例的部分：**
- Kumar et al. (NeurIPS 2025) 和 QuRL (ICLR 2026) 已报告 quantization 损害 RL training，QuRL 发现 RL 的 weight update 极小、被 quantization noise 淹没
- FP4 论文提出理论阈值：gradient < √3 × quantization noise → 训练停滞
- GTPO/DAPO 已识别 GRPO 的 entropy collapse 和 token-level gradient conflict

**我们的 unique contribution：**
- QLoRA 4-bit + GRPO 导致 structured output 的 **subtask decoupling**（relation↔evidence 分离）——文献中无直接先例
- 现有 quantization+RL 研究全部集中在 math reasoning，structured IE 的 multi-component output 更脆弱
- 同一配置下 4-bit vs bf16 的干净消融是独特的实验证据

**Claim 2 reframing** 建议已附在文档末尾，论据链从 QLoRA SFT 正常 → RL weight update 微小 → 4-bit noise 超过理论阈值 → gradient conflict 放大 → subtask decoupling。

---
