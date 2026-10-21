# analysis edcr deduped with reranker

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_deduped_with_reranker_20260518T074117_result.json`
- **Structured JSON:** [`de82cec53745b6a1f3c4.json`](../../sessions/de/de82cec53745b6a1f3c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整输出：

```
去重全集 (n=7):
  Methods: ['SFT', 'RSFT_CED', 'RSFT_flatNLI', 'GRPO_QLoRA', 'GRPO_bf16_G8', 'DPO_1ep', 'CED_reranker']
  EDCR vs Rel-F1: rho=-0.8929, p=0.006807
  EDCR vs Evi-F1: rho=-0.7143, p=0.071344
  (Evi-F1 - Rel-F1) vs Rel-F1: rho=-0.7857, p=0.036238

无GRPO_QLoRA (n=6):
  Methods: ['SFT', 'RSFT_CED', 'RSFT_flatNLI', 'GRPO_bf16_G8', 'DPO_1ep', 'CED_reranker']
  EDCR vs Rel-F1: rho=-0.8286, p=0.041563
  EDCR vs Evi-F1: rho=-0.5429, p=0.265703
  (Evi-F1 - Rel-F1) vs Rel-F1: rho=-0.8286, p=0.041563

无QLoRA无DPO (n=5):
  Methods: ['SFT', 'RSFT_CED', 'RSFT_flatNLI', 'GRPO_bf16_G8', 'CED_reranker']
  EDCR vs Rel-F1: rho=-0.7000, p=0.188120
  EDCR vs Evi-F1: rho=-0.9000, p=0.037386
  (Evi-F1 - Rel-F1) vs Rel-F1: rho=-0.7000, p=0.188120
```

加入 CED_reranker 后，EDCR vs Rel-F1 在全集 n=7 上 ρ=-0.8929 (p=0.007)，相关性进一步增强且高度显著。去掉 GRPO_QLoRA 的 n=6 子集也保持显著 (ρ=-0.8286, p=0.042)。n=5 子集因样本量太小失去统计显著性 (p=0.188)。

---
