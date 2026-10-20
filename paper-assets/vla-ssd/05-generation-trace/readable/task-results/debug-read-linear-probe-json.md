# debug read linear probe json

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_read_linear_probe_json_20260518T040623_result.json`
- **Structured JSON:** [`de754a93d901c9ca4bfa.json`](../../sessions/de/de754a93d901c9ca4bfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整获取。图文件确认存在（PDF 18KB, PNG 114KB, 2026-05-18 11:42）。

---

## Summary

```json
{
  "trained_peak_layer": 14,
  "trained_peak_R2": 0.5655,
  "untrained_peak_layer": 0,
  "untrained_peak_R2": 0.5172,
  "inverted_U_trained": true,
  "trained_gt_untrained_at_peak": true
}
```

## Trained Linear Probe — mean R² by layer

| Layer | Trained Linear | Untrained Linear | Δ (T−U) | Trained MLP | Linear−MLP |
|-------|---------------|-----------------|----------|-------------|------------|
| 0 | 0.517 | 0.517 | 0.000 | 0.640 | −0.123 |
| 1 | 0.517 | 0.417 | +0.100 | 0.633 | −0.116 |
| 2 | 0.531 | 0.459 | +0.072 | 0.628 | −0.097 |
| 3 | 0.533 | 0.340 | +0.193 | 0.652 | −0.119 |
| 4 | 0.553 | 0.423 | +0.130 | 0.647 | −0.094 |
| 5 | 0.545 | 0.392 | +0.153 | 0.647 | −0.102 |
| 6 | 0.548 | 0.401 | +0.147 | 0.649 | −0.101 |
| 7 | 0.556 | 0.401 | +0.155 | 0.645 | −0.089 |
| 8 | 0.555 | 0.424 | +0.131 | 0.655 | −0.100 |
| 9 | 0.560 | 0.401 | +0.159 | 0.651 | −0.091 |
| 10 | 0.555 | 0.326 | +0.229 | 0.643 | −0.088 |
| 11 | 0.544 | 0.366 | +0.178 | 0.644 | −0.100 |
| 12 | 0.561 | 0.320 | +0.241 | 0.609 | −0.048 |
| 13 | 0.562 | 0.311 | +0.251 | 0.630 | −0.068 |
| **14** | **0.565** | **0.241** | **+0.324** | 0.621 | −0.055 |
| 15 | 0.561 | 0.223 | +0.338 | 0.628 | −0.067 |
| 16 | 0.549 | 0.188 | +0.361 | 0.619 | −0.070 |
| 17 | 0.546 | 0.084 | +0.462 | 0.635 | −0.089 |
| 18 | 0.544 | 0.165 | +0.379 | 0.635 | −0.091 |
| 19 | 0.543 | 0.120 | +0.423 | 0.599 | −0.055 |
| 20 | 0.556 | 0.090 | +0.466 | 0.579 | −0.023 |
| 21 | 0.549 | 0.117 | +0.432 | 0.574 | −0.024 |
| 22 | 0.547 | −0.200 | +0.747 | 0.583 | −0.037 |
| 23 | 0.544 | 0.068 | +0.476 | 0.436 | +0.107 |
| 24 | 0.536 | 0.033 | +0.503 | 0.554 | −0.018 |
| 25 | 0.531 | −0.298 | +0.829 | 0.548 | −0.017 |
| 26 | 0.514 | 0.136 | +0.378 | 0.506 | +0.008 |
| 27 | 0.514 | 0.100 | +0.414 | 0.426 | +0.088 |
| 28 | 0.506 | 0.147 | +0.359 | 0.418 | +0.087 |
| 29 | 0.522 | 0.150 | +0.372 | 0.529 | −0.006 |
| 30 | 0.479 | 0.095 | +0.384 | 0.523 | −0.045 |
| 31 | 0.470 | 0.037 | +0.433 | 0.388 | +0.082 |
| 32 | 0.481 | 0.505 | −0.024 | 0.578 | −0.097 |

---

## 定性结论

**1. Inverted-U pattern — linear probe 下同样存在**
- Trained linear: peak layer 14 (R²=0.565), 两端下降。曲线比 MLP 更平坦（range 0.47–0.57 vs MLP 0.39–0.66）。
- Untrained linear: **无 inverted-U**，从 layer 0 (0.517) 单调下降至深层近零/负值。

**2. Trained > Untrained — 方向完全一致，且 linear probe 下差距更大**
- Δ 从浅层 +0.1 逐步增长到深层 +0.4~0.8。
- Peak layer (14): trained 0.565 vs untrained 0.241, Δ=+0.324。
- 深层（17-25）untrained 崩塌至 <0.1 甚至负值，而 trained 仍维持 ~0.54。
- 解释：深层表征高度非线性，untrained 的 random features 无法线性解码动作；训练后信息被重组为更 linearly decodable 的形式。

**3. Linear vs MLP gap**
- 浅层（0-11）：MLP 优势约 0.09-0.12，说明浅层信息需要非线性变换才能充分解码。
- 中层（12-22）：gap 缩小至 0.02-0.07，说明训练将动作信息重组为更线性可分的形式。
- 深层（23-28）：linear 偶尔反超 MLP（layer 23, 27, 28），可能因 MLP 过拟合退化。
- MLP peak 更早（layer 8, R²=0.655）vs linear peak layer 14。

**4. Layer 32 异常**
- Untrained layer 32 突然回升至 0.505（高于 layer 1-31 的 untrained），trained 反而低（0.481）。这是 LM head 前的最终层，可能 LLaMA 预训练的 output projection 恰好保留了部分空间信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "trained_peak_layer": 14,
    "trained_peak_R2": 0.5655,
    "untrained_peak_layer": 0,
    "untrained_peak_R2": 0.5172,
    "inverted_U_trained": true,
    "trained_gt_untrained_at_peak": true
  }
}
```

</details>

---
