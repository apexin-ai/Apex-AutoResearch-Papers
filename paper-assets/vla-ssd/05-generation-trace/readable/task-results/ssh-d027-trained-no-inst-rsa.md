# ssh d027 trained no inst rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d027-trained-no-inst-rsa_20260515T221225_result.json`
- **Structured JSON:** [`4a714aa43267dbbdb1c8.json`](../../sessions/4a/4a714aa43267dbbdb1c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_trained_no_inst.json`。

## 2×2 RSA Matrix (peak RSA across layers)

|           | with-inst | no-inst |
|-----------|-----------|---------|
| **trained**   | 0.4876    | **0.489** |
| **untrained** | 0.4846    | 0.4802  |
| **DINO**      | 0.388     | —       |

## Effect sizes

| Effect | Delta |
|--------|-------|
| Training effect (with-inst) | +0.003 |
| Training effect (no-inst) | +0.0088 |
| Instruction effect (trained) | **-0.0014** |
| Instruction effect (untrained) | +0.0044 |

## 关键发现

- Trained no-inst peak RSA = **0.489**（layer 30），略高于 trained with-inst 的 0.4876
- 所有 4 个条件的 peak RSA 都在 **0.48–0.49** 的窄带内，差异 < 0.01
- Bootstrap delta CI [-0.058, 0.072] 包含 0，trained vs untrained 无显著差异
- G1 和 G2 gates 均 FAIL：training 对 action-aligned representation 无显著影响
- Instruction 对 trained model 的效果为 **-0.0014**（几乎为零，甚至略负）

遵循 C001 约束，这里不做因果结论，仅报告数字。4 格数据现在齐全。

---
