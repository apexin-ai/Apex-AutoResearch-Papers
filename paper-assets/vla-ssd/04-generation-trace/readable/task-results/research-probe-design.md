# research probe design

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_probe-design_20260515T045705_result.json`
- **Structured JSON:** [`d743c3f7d3d3c81dc9ef.json`](../../sessions/d7/d743c3f7d3d3c81dc9ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入。核心要点总结：

**关键发现**: OpenVLA 对每个 trajectory timestep 做独立 forward pass，RoPE 编码的是 sequence 内 token position（固定不变），**不是** trajectory timestep。因此 RoPE 实际上不构成 temporal distance probing 的混淆因素。

**设计要点**:
- **Probe 输入**: |h(t_j) − h(t_i)| 绝对差值（对称、紧凑）
- **Token 聚合**: last pre-action token（模型决策汇聚点）
- **输出**: 回归预测 |t_j − t_i|/T，用 Spearman ρ 评估
- **核心控制实验是 Control C（untrained model）**, 而非 timestep fraction baseline——因为后者恒等于目标（ρ ≈ 1.0），VLA 不可能超越

**需 Director 确认的关键修改**: Roadmap 中 "VLA > timestep-baseline (Δρ > 0.1)" 在当前目标定义下不成立。建议改为 **VLA > untrained-model (Δρ > 0.1)**，这能真正分离 VLA 训练贡献 vs 架构偏差。

文件位置: `artifacts/probe_design_plan.md`

---
