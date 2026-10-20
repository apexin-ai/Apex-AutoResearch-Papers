# ssh d027 perlayer rsa analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d027-perlayer-rsa-analysis_20260515T221250_result.json`
- **Structured JSON:** [`796ecd2645dee03176c2.json`](../../sessions/79/796ecd2645dee03176c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。以下是逐层 RSA 对比：

### Per-Layer RSA: With-Inst vs No-Inst (untrained VLA)

| Layer | With-Inst | No-Inst | Delta |
|------:|----------:|--------:|------:|
| 0 | 0.0000 | 0.2025 | **-0.2025** |
| 1 | 0.4641 | 0.4779 | -0.0138 |
| 2 | 0.4659 | 0.4755 | -0.0096 |
| 3-11 | ~0.475-0.484 | ~0.470-0.480 | < 0.01 |
| 12 | 0.4846 | 0.4727 | +0.0119 |
| 13 | 0.4844 | 0.4703 | **+0.0141** |
| 14 | 0.4845 | 0.4710 | +0.0135 |
| 15 | 0.4841 | 0.4722 | +0.0119 |
| 16 | 0.4845 | 0.4741 | +0.0104 |
| 17-32 | ~0.481-0.484 | ~0.476-0.480 | < 0.01 |

### 关键数字
- **Mean delta (excl. layer 0)**: ~+0.005（with-inst 略高）
- **Max delta (excl. layer 0)**: +0.0141 at layer 13
- **DINO RSA reference**: 0.388（两个条件的所有层都远高于 DINO）

### 分析

**Layer 0 是特殊情况**：with-inst 的 layer 0 RSA=0.0（embedding 层，所有 demo 特征完全相同），no-inst=0.2025（去掉 instruction 后 embedding 层有了些许变异）。这反映的是 embedding 输入差异，不是模型表征差异。

**Layer 1-32 的 instruction 效应可以忽略**：
- 除 layer 0 外，所有层的 |delta| 均 < 0.015
- Layers 12-16 有微弱的正 delta（with-inst 比 no-inst 高 ~0.01），但幅度太小，不具有实质意义
- 两个条件下 RSA 曲线几乎完全重叠（~0.47-0.48 全层）

**结论**：Instruction 对 untrained VLA 的逐层 action-alignment 没有实质影响。无论有无 instruction，untrained VLA 在所有层都表现出相同水平的 RSA (~0.48)，且均远高于 DINO (0.388)。这进一步支持高 RSA 来自模型架构/预训练权重，而非 instruction grounding。

---
