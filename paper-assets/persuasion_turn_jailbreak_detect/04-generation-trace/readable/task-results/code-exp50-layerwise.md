# code exp50 layerwise

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp50_layerwise_20260522T085939_result.json`
- **Structured JSON:** [`9a22b00a37ef00f23387.json`](../../sessions/9a/9a22b00a37ef00f23387.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp50 完成。**结果为 Positive**——discriminative compression 集中在后期层。

关键发现（Fisher Ratio，越高 = 类间区分越强）：

| Layer | vanilla | 9-class | scrambled | JB-MLM |
|-------|---------|---------|-----------|--------|
| 1-5   | 0.3-0.8 | 0.3-0.8 | 0.3-0.8   | 0.3-0.8 |
| 6     | 1.52    | 2.05    | 1.70      | 1.53   |
| 8     | 1.47    | **3.20** | 2.50     | 1.40   |
| 9     | 1.04    | **4.03** | **3.76** | 1.07   |
| 10    | 0.73    | **10.92** | **5.93** | 0.93  |
| 11    | 2.28    | **9.10** | **7.37** | 3.33   |
| 12    | 2.83    | **6.53** | **7.91** | 2.61   |

- **Layers 1-5**：4 个变体的 Fisher 几乎无差异（~0.3-0.8），与 Maennel 2020 "早期层标签无关"一致
- **Layers 8-12**：9-class 和 scrambled 的 Fisher 显著 diverge（5-11x），而 JB-MLM 和 vanilla 保持平坦——说明 classification-supervised DAPT 的 discriminative compression 集中在后期层
- 9-class 在 layer 10 达峰值（10.92），scrambled 在 layer 12 达峰值（7.91）

输出文件：
- 数据：`results/exp50_layerwise_results.json`
- 图表：`figures/paper/fig_layerwise_representation.{pdf,png}`
- 脚本：`scripts/exp50_layerwise_representation.py`

---
