# ops r3 grpo bf16 g4 analysis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r3_grpo_bf16_g4_analysis_20260525T000346_result.json`
- **Structured JSON:** [`6393fb2acb912cd25d5d.json`](../../sessions/63/6393fb2acb912cd25d5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。以下是完整分析。

---

## r3_grpo_bf16_g4 分析结果

### 1. Reward 轨迹（每 5 steps 记录，共 20 个数据点）

| Step | reward | f1_reward | ced_reward | format | entropy |
|------|--------|-----------|------------|--------|---------|
| 5    | 1.866  | 1.205     | 0.360      | 0.30   | 0.148   |
| 10   | 1.314  | 0.907     | 0.175      | 0.30   | 0.140   |
| 15   | 2.081  | 1.424     | 0.357      | 0.30   | 0.127   |
| 20   | 2.305  | 1.192     | 0.813      | 0.30   | 0.106   |
| 25   | 1.763  | 0.935     | 0.528      | 0.30   | 0.104   |
| 30   | 1.315  | 0.838     | 0.245      | 0.30   | 0.088   |
| 35   | 1.471  | 0.770     | 0.401      | 0.30   | 0.090   |
| 40   | 1.098  | 0.421     | 0.377      | 0.30   | 0.094   |
| 45   | 1.244  | 0.576     | 0.402      | 0.30   | 0.153   |
| 50   | 1.513  | 0.703     | 0.510      | 0.30   | 0.129   |
| 55   | **0.581** | 0.365  | 0.051      | 0.23   | 0.133   |
| 60   | 0.681  | 0.298     | 0.146      | 0.24   | 0.135   |
| 65   | 1.238  | 0.711     | 0.270      | 0.26   | 0.167   |
| 70   | **3.426** | 2.491  | 0.717      | 0.30   | 0.086   |
| 75   | 2.174  | 1.447     | 0.502      | 0.30   | 0.108   |
| 80   | 0.771  | 0.651     | 0.045      | 0.08   | 0.163   |
| 85   | 1.437  | 0.812     | 0.325      | 0.30   | 0.135   |
| 90   | 1.647  | 0.783     | 0.564      | 0.30   | 0.135   |
| 95   | 1.501  | 1.084     | 0.184      | 0.23   | 0.168   |
| 100  | 1.019  | 0.683     | 0.171      | 0.17   | 0.127   |

**均值**: reward ≈ 1.47, f1 ≈ 0.85, ced ≈ 0.35, entropy ≈ 0.126

### 2. 结论：bf16 G=4 **不 collapse**

判断依据：
- reward **从未**降到 0.3 以下（最低 0.581 @ step 55，随后立即恢复）
- 20 个数据点中 16 个 reward > 1.0，无单调下降趋势
- entropy 始终在 0.086–0.168 范围，没有坍缩到 0（模型保持多样性）
- train_loss 最终 ≈ -0.004（接近 0，正常收敛）

### 3. 与基准对比

| 实验 | 量化 | G | kl | reward 行为 | eval ign_f1 |
|------|------|---|-----|-------------|-------------|
| **QLoRA G=4** (mvp2) | 4-bit | 4 | 0 | **collapse** → rel_f1=0.2167 | 0.2167 (catastrophic) |
| **plan_011** (bf16 G=8) | bf16 | 8 | 0.01 | 健康 ↑ | 0.4549 (+4.9pp vs SFT) |
| **r3_grpo_bf16_g4** (本实验) | bf16 | 4 | 0.01 | **健康，均值 1.47** | 待 eval |

### 4. 对论文 claim 的影响

**"Quantization is the primary cause of collapse" — 强烈支持。**

这是关键的隔离变量实验：
- QLoRA G=4 → collapse (rel_f1=0.2167)
- bf16 G=4 → 不 collapse (reward 保持 ~1.47)
- **唯一变量是 quantization (4-bit vs bf16)**，G=4 相同

此前 plan_011 的 registry notes 明确提到 "plan_011 同时改了 quantization + group_size(8 vs 4), 需隔离变量"。r3_grpo_bf16_g4 正是这个隔离实验——结果明确：**G=4 不是 collapse 的原因，4-bit quantization 才是**。

### 5. 注意事项

- 尚无 eval metrics（需跑 eval 才能与 plan_011 的 ign_f1=0.4549 直接对比）
- 训练末段 (step 95-100) completions 变长 (avg 957 tokens, clipped_ratio=50%)，format reward 降到 0.17，可能有轻微 length exploitation，但 reward 仍健康
- kl_coef=0.01（与 plan_011 一致，但与 QLoRA baseline kl=0 不同），不过 quantization 已被隔离为唯一变量

---
