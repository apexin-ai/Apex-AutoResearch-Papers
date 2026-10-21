# analysis 008e v3 s2 model metrics confirmation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_008e_v3_s2_model_metrics_confirmation_20260515T173647_result.json`
- **Structured JSON:** [`310da29d1b0aa56ff19d.json`](../../sessions/31/310da29d1b0aa56ff19d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。汇总分析如下：

---

## 008e_v3_s2 指标轨迹（35K → 105K）

| Step | eval_return | value_mean | target_mean | value−target | value_std | actor_entropy | actor_loss | reward_loss |
|------|------------|------------|-------------|-------------|-----------|---------------|------------|-------------|
| 35K  | 320 | 79.8 | 82.0 | −2.3 | 3.9 | −3.50 | −0.167 | 0.619 |
| 45K  | 357 | 125.3 | 127.2 | −2.0 | 4.7 | −4.91 | −0.112 | 0.620 |
| 55K  | 418 | 172.9 | 174.8 | −1.9 | 5.7 | −5.12 | −0.092 | 0.610 |
| 65K  | 435 | 220.5 | 222.2 | −1.7 | 6.2 | −5.14 | −0.075 | 0.604 |
| 75K  | 577 | 272.6 | 274.7 | −2.1 | 5.7 | −5.22 | −0.098 | 0.598 |
| **85K** | **715** | 339.3 | 341.8 | −2.5 | **7.4** | −5.21 | −0.098 | 0.582 |
| **95K** | **452** | 384.4 | 385.0 | −0.6 | **9.2** | **−4.53** | −0.027 | 0.561 |
| **105K** | **137** | 339.8 | 338.8 | **+1.1** | **18.3** | **−3.83** | **+0.016** | 0.557 |

## Non-CIVO 签名确认

**85K-105K 崩溃期间的 5 项 non-CIVO 诊断指标全部成立：**

| 诊断维度 | CIVO 预期 | Non-CIVO (IRD) 预期 | 85K→105K 实测 | 判定 |
|----------|----------|-------------------|-------------|------|
| value vs target | value >> target | value ≈ target | 差值 −2.5 → +1.1（始终 ~0） | **Non-CIVO** |
| value_std | 稳定/下降 | explosion | 7.4 → 9.2 → **18.3**（2.5x） | **Non-CIVO** |
| actor_entropy | 下降（过度确信） | 上升（de-specialization） | −5.21 → −4.53 → **−3.83**（+1.4） | **Non-CIVO** |
| actor_loss | 极负（overexploitation） | → 0 或正 | −0.098 → −0.027 → **+0.016** | **Non-CIVO** |
| reward_loss | 无特定模式 | 稳定（world model本身不崩） | 0.582 → 0.561 → 0.557（缓降） | 一致 |

## 结论

**Non-CIVO (Imagination-Reality Divergence) 签名在 85K-105K 崩溃期间持续且加剧。** 与 35K-65K 分析完全一致：

1. **Value 始终 tracking target**——value−target 差值在 ±2.5 范围内，105K 甚至轻微高估仅 +1.1。不存在 CIVO 的 value >> target 特征。
2. **value_std 从 85K 的 7.4 爆炸到 105K 的 18.3**（与之前分析的数字完全吻合），确认 noisy value estimates。
3. **actor_entropy 从 −5.21 上升到 −3.83**，actor 持续 de-specialize，与 CIVO 的 entropy 下降（过度确信）完全相反。
4. **actor_loss 从 −0.098 转正到 +0.016**，actor 不再能从 imagination rollout 中获得改进信号。
5. **reward_loss 持续缓降**（0.582→0.557），说明 world model 的 reward prediction 本身没有退化——问题出在 value estimation 的 variance，不是 model accuracy。

机制链条完整：world model accuracy ceiling → value_std explosion → noisy actor gradients → policy de-specialization → eval collapse。这是 IRD 而非 CIVO。

---
