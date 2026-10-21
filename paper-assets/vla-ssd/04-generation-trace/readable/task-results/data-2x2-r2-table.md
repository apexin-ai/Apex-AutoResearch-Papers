# data 2x2 r2 table

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_2x2_r2_table_20260520T103233_result.json`
- **Structured JSON:** [`2f95b94dfefe1a27a3f9.json`](../../sessions/2f/2f95b94dfefe1a27a3f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 四个条件的 R² Profile

| 条件 | Seeds | Peak Layer | Peak R² | Profile Shape |
|------|-------|------------|---------|---------------|
| OpenVLA Untrained | 15 | L0 | 0.629 | L0 最高后急剧崩塌，中后层均值降至 0.1-0.3，方差极大（std ~0.25），L32 回弹至 0.584 |
| OpenVLA Trained | 15 | L9 | 0.637 | 全层平坦（0.61-0.64），从 L21 起缓慢下降至 0.49，L32 小幅回弹 |
| Phi3V Untrained | 5 | L4 | 0.583 | L0 负值 → 快速爬升至 L4 peak，此后稳步下降至 ~0.45，方差适中 |
| Phi3V Trained | 15 | L11 | 0.634 | L0 负值 → 爬升至 L11 plateau（0.63），持续到 L20，缓降至 0.55 |

### 关键 Pattern

**1. Training effect 远大于 architecture effect**
- OpenVLA 中层（L15-L25）的 trained-untrained Δ 平均 **+0.313**，untrained 中层 R² 接近 0（部分 seed 为负）
- Phi3V 同区间 Δ 为 **+0.103**，untrained 仍保持 ~0.5 的基础 R²
- Training 在 OpenVLA 上的效应是 Phi3V 的 **3 倍**

**2. Untrained baseline 的架构差异**
- OpenVLA untrained 在 L0 即达 peak（0.629），因为 Llama-2 embedding 层直接继承了预训练的 token 表征，但中深层表征对 action 无解码能力
- Phi3V untrained 的 peak 在 L4（0.583），表明 Phi-3 预训练表征在浅层就具备一定的 action-relevant 结构

**3. Late-layer stability**
- OpenVLA untrained late-layer std = **0.277**（极不稳定，近半数 seed 产生负 R²）
- Phi3V untrained late-layer std = **0.047**（相对稳定）
- Training 将 OpenVLA late-layer std 从 0.277 降至 0.040，Phi3V 从 0.047 降至 0.011

**4. L32（输出层）anomaly**
- OpenVLA untrained L32 R² = 0.584，显著高于 L31（0.069）—— 预训练 LM head 自带 action-correlated 信号
- OpenVLA trained L32 = 0.535，反而低于 untrained L32 —— 训练后 LM head 被 repurposed，不再保留这个 shortcut

---
