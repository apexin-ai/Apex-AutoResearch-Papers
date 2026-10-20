# ssh plan003 perlayer degradation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan003-perlayer-degradation_20260515T223128_result.json`
- **Structured JSON:** [`e65f4515ebe08abea93d.json`](../../sessions/e6/e65f4515ebe08abea93d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。结果保存在 `/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json`。

关键发现：

| 条件 | Peak LLM RSA | Peak Layer | Proj→L1 Drop | L1后模式 |
|------|-------------|------------|--------------|---------|
| with-inst trained | 0.4876 | L9 | 0.2036 | non_monotonic |
| with-inst untrained | 0.4846 | L12 | 0.1512 | non_monotonic |
| no-inst trained | 0.489 | L30 | 0.2526 | predominantly_increasing |
| no-inst untrained | 0.4802 | L6 | 0.1374 | non_monotonic |

核心结论：
- **SigLIP+projector RSA (0.6153) → LLM Layer 1 是最大 drop**，所有条件都损失 0.13–0.25（~20–40%）
- Layer 0 (embedding) 是异常值（trained 模型 RSA=0.0），实际结构从 L1 开始恢复
- **总降解幅度在 0.126–0.135 之间**，即 LLM 最好层仍比 projector 输出低 ~0.13
- No-inst trained 是唯一呈"持续上升"模式的条件（L1→L30 递增），其余三个都是 non-monotonic
- 所有条件的 LLM 层 RSA 都远高于 DINO (0.388)

---
