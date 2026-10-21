# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260516T025122_result.json`
- **Structured JSON:** [`7d095caa3eca6b13451e.json`](../../sessions/7d/7d095caa3eca6b13451e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discussion section 已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex`。

7 段结构：
1. **Synthesis** — source-router-policy 三角叙事，projector 提供 96.6% readout 容量
2. **VL pretraining generalization** — CLIP 0.557 确认 VL pretraining 是通用 source，非 SigLIP 特有
3. **Geometric-functional dissociation** — DINO ≈ Proj in R² but << in RSA，VL pretraining 提供 alignment 而非额外 information
4. **RSA vs CKA** — linear CKA 排序反转，RDM kernel CKA 恢复一致，metric choice determines narrative
5. **Design implications** — 四条实践建议（encoder quality、projector output、readout concentration、instruction role）
6. **Behavioral connection** — 与 Grant et al. 2026 behavioral findings 的 representational account 对应
7. **Limitations** — 单架构/单 benchmark、RSA 非因果、跨实验 R² 超参差异、post-hoc 分析局限

所有数字严格来自 registry，R² 对比仅在同一 probe 设置内进行，未混用 50ep/100ep 数字。

---
