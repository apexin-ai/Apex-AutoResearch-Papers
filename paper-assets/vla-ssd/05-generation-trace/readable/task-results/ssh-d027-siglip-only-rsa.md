# ssh d027 siglip only rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d027-siglip-only-rsa_20260515T221202_result.json`
- **Structured JSON:** [`ca5d1b7847fbd432cc8a.json`](../../sessions/ca/ca5d1b7847fbd432cc8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### SigLIP+Projector RSA = **0.6153** [0.5257, 0.6954]

| 模型 | RSA |
|------|-----|
| **SigLIP+Projector (no LLM)** | **0.6153** |
| Trained VLA (full, with inst) | 0.4876 |
| Untrained VLA (with inst) | 0.4846 |
| Untrained VLA (no inst) | 0.4802 |
| DINO standalone | 0.388 |

**关键发现**：SigLIP+projector 的 RSA 不仅 ≥ 0.48（LLM full model），反而显著更高（0.615 vs 0.488）。这说明：

1. Vision encoder + projector 本身已经编码了强 action-relevant 结构
2. LLM 不仅没有增强 action alignment，反而在某种程度上**降低**了它（从 0.615 降到 0.488）
3. Trained 和 untrained LLM 的 RSA 几乎一致（0.488 vs 0.485），说明 LLM 训练对 action alignment 几乎无贡献——action-relevant 信息完全来自 vision encoder

Gate: **PASS** — vision encoder+projector 是 action-relevant 表征的来源，LLM 是 near-passthrough（甚至有信息损失）。

---
