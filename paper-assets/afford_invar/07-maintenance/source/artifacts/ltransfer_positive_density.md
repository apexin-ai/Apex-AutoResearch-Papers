# L_transfer 正对密度验证报告

**日期**: 2026-05-19
**数据**: 130 tasks × 6 instructions/task = 780 条指令（5 suites: libero_spatial, libero_object, libero_goal, libero_10, libero_90）
**Encoder**: SigLIP-base（mean pooling → cosine similarity）

## 1. 相似度矩阵统计

| 指标 | 全部对 | 跨任务对 |
|------|--------|----------|
| Total pairs | 303,810 | 301,860 |
| Min | 0.0771 | 0.0771 |
| Max | 1.0000 | 1.0000 |
| Mean | 0.5115 | 0.5103 |
| Std | 0.1657 | 0.1651 |

**分位数（全部对）**: P25=0.38, P50=0.53, P75=0.64, P90=0.71, P95=0.76, P99=0.84

## 2. 不同阈值下的正对密度

| Threshold | #Positive Pairs | Density | Avg Pos/Anchor |
|-----------|----------------|---------|----------------|
| 0.70 | 36,077 | 11.95% | 92.5 |
| 0.75 | 16,529 | 5.48% | 42.4 |
| **0.80** | **5,986** | **1.98%** | **15.3** |
| **0.85** | **1,867** | **0.62%** | **4.8** |
| 0.90 | 485 | 0.16% | 1.2 |
| 0.95 | 167 | 0.06% | 0.4 |

## 3. Top-20 最相似跨任务对

Top-20 全部为 sim=1.0000，均来自 libero_90 内不同任务但指令文本完全相同的情况（如 libero_90_74 vs libero_90_82 都有 "pick up the book and place it in the left compartment of the caddy"）。这说明 libero_90 中存在大量重复指令分布在不同 task_id 下。

## 4. 孤立任务（threshold=0.85 下无正对）

12 / 130 个任务孤立（9.2%）：

- libero_object_0: pick up the alphabet soup and place it in the basket
- libero_10_0: turn on the stove and put the moka pot on it
- libero_10_2: put the yellow and white mug in the microwave and close it
- libero_10_3: put both moka pots on the stove
- libero_10_6: put both the cream cheese box and the butter in the basket
- libero_10_9: pick up the book and place it in the back compartment of the caddy
- libero_90_5: put the chocolate pudding in the top drawer of the cabinet and close it
- libero_90_23: close the bottom drawer of the cabinet and open the top drawer
- libero_90_27: put the wine bottle on the wine rack
- libero_90_28: close the top drawer of the cabinet
- libero_90_68: put the yellow and white mug on the right plate
- libero_90_86: pick up the book in the middle and place it on the cabinet shelf

## 5. 按 Suite 分布（threshold=0.85）

| Suite 对 | #Positive Pairs |
|----------|----------------|
| libero_90 × libero_90 | 815 (43.6%) |
| libero_spatial × libero_spatial | 140 (7.5%) |
| libero_goal × libero_goal | 129 (6.9%) |
| libero_object × libero_object | 75 (4.0%) |
| libero_10 × libero_90 | 8 (0.4%) |
| libero_10 × libero_10 | 7 (0.4%) |
| **跨 suite（spatial/object/goal 之间）** | **0** |

**关键发现**: 正对几乎全部集中在 suite 内部，跨 suite 的正对极少。L_transfer 实际上只在同一 suite 内部起作用。

## 6. 判定

**MARGINAL** — 阈值 0.85 下 avg_pos/anchor=4.8，刚好在边界。

### 建议

1. **降阈值到 0.80**：avg_pos/anchor 从 4.8 增到 15.3，density 从 0.62% 增到 1.98%，进入 SUFFICIENT 区间
2. **注意 libero_90 的指令重叠**：大量 sim=1.0 的正对来自 libero_90 中不同 task_id 使用完全相同的指令文本，这些正对的训练信号可能过强，需要考虑是否去重
3. **跨 suite 迁移有限**：spatial/object/goal 之间零正对，L_transfer 无法提供跨 suite 的语义对齐信号。如果跨 suite 迁移是目标，需要补充其他机制
