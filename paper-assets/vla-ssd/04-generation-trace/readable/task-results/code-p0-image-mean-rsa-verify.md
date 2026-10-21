# code p0 image mean rsa verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0_image_mean_rsa_verify_20260515T223349_result.json`
- **Structured JSON:** [`15f2bbfd31f5d33a265d.json`](../../sessions/15/15f2bbfd31f5d33a265d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Condition | last_preaction | image_mean | SigLIP projector |
|-----------|---------------|------------|------------------|
| **Trained** (peak, L23) | 0.4876 | **0.5014** | 0.6153 |
| **Untrained** (peak, L23) | 0.4846 | **0.4847** | — |

**结论: Claim 2 HOLDS**

image_mean RSA = 0.5014，与 last_preaction (0.4876) 在同一量级，远低于 SigLIP projector (0.6153)。gap = 0.1139。

即使使用与 SigLIP 完全相同的 mean pooling 聚合方式，VLA 的 action alignment 仍然显著低于 SigLIP —— 排除了 Reviewer 提出的"聚合伪影"假说。LLM 确实降解了 action alignment。

- 脚本: `/root/vla-ssd/rsa_image_mean.py`（已有，直接运行）
- 结果 JSON: `/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json`
- Artifact 已注册: `art_20260515_bd66b6`

---
