# code read layer scan results

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_read-layer-scan-results_20260519T211524_result.json`
- **Structured JSON:** [`1c3b1d67ca27eab2c099.json`](../../sessions/1c/1c3b1d67ca27eab2c099.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部读取。汇总如下：

## OpenVLA 多层 Real-Image Divergence 扫描结果

| Layer | Attn KL Real (mean) | Attn KL Dummy (mean) | Real/Dummy Ratio | Cos Dist Image Tokens | Cos Dist All Tokens |
|------:|--------------------:|---------------------:|-----------------:|----------------------:|--------------------:|
| 4     | 2.46e-05            | 4.32e-06             | **5.70x**        | 1.45e-06              | 1.84e-02            |
| 8     | 8.02e-05            | 2.33e-05             | 3.44x            | 8.95e-06              | 2.21e-02            |
| 12    | 1.58e-04            | 6.57e-05             | 2.41x            | 2.11e-05              | 2.45e-02            |
| **18**| **1.91e-04**        | 6.97e-05             | 2.74x            | 3.54e-05              | 2.77e-02            |
| **24**| **2.02e-04**        | 7.07e-05             | 2.85x            | 6.29e-05              | 2.79e-02            |
| 30    | 1.17e-04            | 8.43e-05             | 1.39x            | **1.17e-04**          | 2.67e-02            |

## 关键发现

1. **Attention KL divergence 峰值在 Layer 24**（2.02e-4），Layer 18 紧随其后（1.91e-4）。两者远高于其他层。

2. **Image token cosine distance 随深度单调递增**：Layer 4 仅 1.45e-6，Layer 30 达到 1.17e-4（约 81 倍增长）。说明越深的层，text paraphrase 对 image token hidden state 的扰动越大。

3. **Signal-to-noise（Real/Dummy KL ratio）在浅层最优**：Layer 4 的 real KL 是 dummy 的 5.7 倍，而 Layer 30 仅 1.39 倍。Layer 30 的 attention KL 实际上低于 Layer 18/24，且 dummy 噪声几乎追平 real signal。

4. **Text-image coupling 最强层：Layer 24**。它同时具备最高的 attention KL absolute value（2.02e-4）和较高的 real/dummy ratio（2.85x），且 image token cosine distance（6.29e-5）已显著高于 Layer 18（3.54e-5）。

5. **Layer 30 的高 image cosine distance 但低 KL ratio 的矛盾**暗示：最后几层的 hidden state 对 text 变化更敏感（image token 表征被 text 拉扯），但 attention pattern 本身已趋于稳定（text-image attention coupling 反而减弱）。这可能意味着 Layer 24 附近是 text→image 信息交互的关键瓶颈层，而 Layer 30 的变化更多是上游扰动的被动传播。

---
