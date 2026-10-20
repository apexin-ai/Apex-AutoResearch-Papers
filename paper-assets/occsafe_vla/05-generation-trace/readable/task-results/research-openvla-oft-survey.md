# research openvla oft survey

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_openvla-oft-survey_20260520T040517_result.json`
- **Structured JSON:** [`cfae4eb196116b47087f.json`](../../sessions/cf/cfae4eb196116b47087f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/openvla_oft_survey.md`。

核心发现：

- **OpenVLA-OFT** (MIT, ~1200 stars, RSS 2025) 是 Stanford 出的 Optimized Fine-Tuning 方案，在 LIBERO 上 97.1% SOTA，推理速度 26× 提升
- **原生支持 LIBERO**：有完整的数据转换、训练脚本、预训练 checkpoint (HuggingFace)
- **A100 80GB 单卡可训练** (batch_size=8, ~62GB)，依赖自定义 transformers fork（bidirectional attention）
- **SafeLIBERO 是纯评估 benchmark**，不含训练数据和 occupancy 标注——数据生成是最大工程瓶颈
- **辅助头最佳位置**：SigLIP+DINOv2 fused features 输出后（16×16 空间分辨率），QDepth-VLA 已验证此位置加 geometric auxiliary head 可行
- **预估总工期 3-4 周**，关键路径在 occupancy GT 数据生成 (Phase 3)

---
