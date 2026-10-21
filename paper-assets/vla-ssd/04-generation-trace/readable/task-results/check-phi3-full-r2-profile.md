# check phi3 full r2 profile

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phi3_full_r2_profile_20260523T235913_result.json`
- **Structured JSON:** [`b3d1273b4974f844d6e6.json`](../../sessions/b3/b3d1273b4974f844d6e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Llama-2-chat 也有 NLP control 数据（在 `llama2chat_action_probe/` 目录下，note 同样标注 "text-only model"）。

## Phi-3-mini-instruct (L0–L31)

| Layer | R² |
|-------|------|
| L0 | 0.1555 |
| L1 | 0.1552 |
| L2 | 0.1555 |
| L3 | 0.1553 |
| L4 | 0.1554 |
| L5 | 0.1555 |
| L6 | 0.1554 |
| L7 | 0.1554 |
| L8 | 0.1555 |
| L9 | 0.1555 |
| L10 | 0.1552 |
| L11 | 0.1552 |
| L12 | 0.1554 |
| L13 | 0.1555 |
| L14 | 0.1555 |
| L15 | 0.1555 |
| L16 | 0.1555 |
| L17 | 0.1555 |
| L18 | 0.1555 |
| L19 | 0.1555 |
| L20 | 0.1555 |
| L21 | 0.1555 |
| L22 | 0.1555 |
| L23 | 0.1555 |
| L24 | 0.1555 |
| L25 | 0.1555 |
| L26 | 0.1555 |
| L27 | 0.1555 |
| L28 | 0.1555 |
| L29 | 0.1555 |
| L30 | 0.1555 |
| L31 | 0.1555 |

- **Peak**: L0 (R²=0.1555) — 多层并列
- **Exit**: L31 (R²=0.1555)
- **ΔR² (peak–exit)**: 0.0000
- **ΔR² (max–min)**: 0.0003 (0.1555 − 0.1552)
- **Mean R²**: 0.1555

## Llama-2-7b-chat (L0–L31)

| Layer | R² |
|-------|------|
| L0 | 0.1553 |
| L1 | 0.1554 |
| L2 | 0.1551 |
| L3 | 0.1554 |
| L4 | 0.1552 |
| L5 | 0.1554 |
| L6 | 0.1547 |
| L7 | 0.1551 |
| L8 | 0.1552 |
| L9 | 0.1553 |
| L10 | 0.1553 |
| L11 | 0.1553 |
| L12 | 0.1554 |
| L13 | 0.1554 |
| L14 | 0.1554 |
| L15 | 0.1555 |
| L16 | 0.1551 |
| L17 | 0.1552 |
| L18 | 0.1553 |
| L19 | 0.1553 |
| L20 | 0.1554 |
| L21–L31 | 0.1555 |

- **Peak**: L15 (R²=0.1555) — L21+ 并列
- **Exit**: L31 (R²=0.1555)
- **ΔR² (peak–exit)**: 0.0000
- **ΔR² (max–min)**: 0.0008 (0.1555 − 0.1547)
- **Mean R²**: 0.1553

## 对比

两个 backbone 的 NLP control R² profile 完全一致：

1. **所有层 R² ≈ 0.1555**，波动在 ±0.0003（Phi-3）和 ±0.0008（Llama-2）范围内，本质上是噪声。
2. **无 layer-wise 变化趋势**：没有 peak、没有 exit collapse、没有单调递增/递减。R² 完全 flat。
3. **std = 0.0**（action_r2_probing.json），说明单次 seed 运行，数值波动来自 Ridge 回归的数值精度而非实质性差异。
4. **n_unique_hidden_states = 10**：text-only model 对同一 task instruction 每个 timestep 产生相同 hidden state，hidden state 只有 10 个唯一值（对应 10 个 task），线性 probe 无法从中预测 action → R² ≈ baseline 水平，符合预期。

结论：NLP control 验证通过——纯文本 LLM 的 hidden states 不包含 action-predictive 信息，R² 在所有层均为 chance level (~0.155)，跨两个 backbone 结果一致。

---
