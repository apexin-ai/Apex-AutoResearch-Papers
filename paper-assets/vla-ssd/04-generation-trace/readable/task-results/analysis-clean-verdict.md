# analysis clean verdict

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_clean-verdict_20260515T135244_result.json`
- **Structured JSON:** [`4b1faf26a189564c824a.json`](../../sessions/4b/4b1faf26a189564c824a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 正式 MVP Verdict 结果

### Overall Judgment: **FAIL**

失败原因：`delta-rho = 0.0427 ≤ 0.1` — trained vs untrained 的差异不足以通过 Gate 2。

---

### Gate 判定

| Gate | 条件 | 值 | 结果 |
|------|------|----|------|
| **Gate 1: rho_pass** | best_layer rho 足够高 | best_rho = **0.9550** (layer 4) | **PASS** |
| **Gate 2: delta_pass** | trained−untrained Δρ > 0.1 | Δρ = **0.0427**, CI [0.0359, 0.0502], p=0.0 | **FAIL** |
| **Gate 3: DINO gate** | VLA mean_rho ≥ DINO threshold (0.901) | VLA = **0.9562** ≥ 0.901 | **PASS** |

---

### 关键数值

| 指标 | 值 |
|------|----|
| best_layer (healthy) | **4** |
| best_pooled_rho (trained) | 0.9556 |
| best_per_task_mean_rho (trained) | 0.9562 |
| best_rho (untrained, layer 1) | 0.9334 |
| **Δρ at best layer** | **+0.0427** |
| Δρ 95% CI | [0.0359, 0.0502] |
| permutation p-value | 0.0 (CI excludes zero) |
| DINO mean_rho | 0.9008 |
| DINO gate threshold | 0.901 |

---

### 完整 33 层 Layer Profile

| Layer | Trained ρ | Untrained ρ | Δρ | Status |
|-------|-----------|-------------|--------|--------|
| 0 | 0.0000 | 0.0000 | +0.0000 | COLLAPSED |
| 1 | 0.9485 | 0.9334 | +0.0151 | healthy |
| 2 | 0.9547 | 0.9278 | +0.0269 | healthy |
| 3 | 0.9562 | 0.0000 | +0.9562 | COLLAPSED |
| **4** | **0.9550** | **0.9123** | **+0.0427** | **healthy (best)** |
| 5 | 0.9502 | 0.9310 | +0.0192 | healthy |
| 6 | 0.9495 | 0.9250 | +0.0245 | healthy |
| 7 | 0.9438 | 0.9036 | +0.0402 | healthy |
| 8 | 0.9336 | 0.9278 | +0.0058 | healthy |
| 9 | 0.9404 | 0.0000 | +0.9404 | COLLAPSED |
| 10 | 0.9394 | 0.9120 | +0.0274 | healthy |
| 11 | 0.9247 | 0.8878 | +0.0369 | healthy |
| 12 | 0.9012 | 0.8938 | +0.0075 | healthy |
| 13 | 0.9028 | 0.9321 | −0.0292 | healthy |
| 14 | 0.9058 | 0.9031 | +0.0027 | healthy |
| 15 | 0.9049 | 0.0000 | +0.9049 | COLLAPSED |
| 16 | 0.0000 | 0.8729 | −0.8729 | COLLAPSED |
| 17 | 0.9047 | 0.8839 | +0.0207 | healthy |
| 18 | 0.0000 | 0.8826 | −0.8826 | COLLAPSED |
| 19 | 0.9102 | 0.8752 | +0.0350 | healthy |
| 20 | 0.9203 | 0.0000 | +0.9203 | COLLAPSED |
| 21 | 0.8940 | 0.8883 | +0.0057 | healthy |
| 22 | 0.0000 | 0.7699 | −0.7699 | COLLAPSED |
| 23 | 0.0000 | 0.9024 | −0.9024 | COLLAPSED |
| 24 | 0.0000 | 0.9078 | −0.9078 | COLLAPSED |
| 25 | 0.9046 | 0.8899 | +0.0147 | healthy |
| 26 | 0.0000 | 0.0000 | +0.0000 | COLLAPSED |
| 27 | 0.8874 | 0.0000 | +0.8874 | COLLAPSED |
| 28 | 0.0000 | 0.8799 | −0.8799 | COLLAPSED |
| 29 | 0.8845 | 0.8498 | +0.0346 | healthy |
| 30 | 0.0000 | 0.8587 | −0.8587 | COLLAPSED |
| 31 | 0.8785 | 0.0000 | +0.8785 | COLLAPSED |
| 32 | 0.0000 | 0.0000 | +0.0000 | COLLAPSED |

---

### 坍塌层统计

- **16/33 层坍塌**（trained 或 untrained 的 per_task_mean_ρ < 0.1）
- 坍塌层：`[0, 3, 9, 15, 16, 18, 20, 22, 23, 24, 26, 27, 28, 30, 31, 32]`
- 健康层：`[1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 17, 19, 21, 25, 29]` (17 层)

---

### 解读

在 17 个健康层中，trained 模型在 best layer (4) 的 Δρ = +0.0427，CI 完全排除零（p=0.0），说明 trained 确实优于 untrained。但 **效应量不足**：Δρ = 0.043 远低于 0.1 阈值，Gate 2 未通过。同时 Gate 3 勉强通过（VLA 0.956 vs DINO 0.901，阈值 0.901）。

产出文件已保存至 `/root/autodl-tmp/vla-ssd/results/analysis/`（summary.json + 3 组图表 PDF/PNG）。

---
