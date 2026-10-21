# analysis gradient conflict and attention

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_conflict_and_attention_20260519T131756_result.json`
- **Structured JSON:** [`b9b25595251f882b5a69.json`](../../sessions/b9/b9b25595251f882b5a69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## Gradient Conflict Analysis (3 epochs)

| Epoch | cos_sim | 负向层 | 强冲突层 | NTP/GAR 幅值比 |
|-------|---------|--------|----------|----------------|
| 0 | -0.089 | 22/28 (78.6%) | 3/28 | 7.5x |
| 1 | -0.054 | 20/28 (71.4%) | 0/28 | 13.7x |
| 2 | -0.042 | 19/28 (67.9%) | 0/28 | 14.7x |

## Attention Heatmap (4-way comparison)

| Model | Mean Goal Attn | T1→T10 Decay |
|-------|---------------|--------------|
| Base | 0.0136 | 87.5% |
| TG v7 | 0.0232 | 77.7% |
| UG | 0.0216 | 80.3% |
| LoRA-only | 0.0216 | 81.0% |

## 关键发现

1. **NTP-GAR 梯度冲突普遍存在**：67-79% 的层梯度方向相反，且随 epoch 增加 NTP 幅值主导越来越大（7.5→14.7x），GAR 信号被淹没
2. **四模型 attention 衰减几乎一致**：TG 77.7% vs LoRA-only 81.0%，gating 机制零增量
3. **根本原因**：gate 参数无法同时服务 NTP（push gate→1.0）和 GAR（要求重新分配 attention），训练中 NTP 梯度碾压 GAR

产出文件位于 `westd-20861:/root/turn_residual_gating/runs/analysis/`，已注册 3 个 artifact。

---
