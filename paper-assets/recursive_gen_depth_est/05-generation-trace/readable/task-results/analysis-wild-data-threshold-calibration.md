# analysis wild data threshold calibration

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wild_data_threshold_calibration_20260518T182225_result.json`
- **Structured JSON:** [`141806de836a4d7aafa8.json`](../../sessions/14/141806de836a4d7aafa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有产出已保存。总结结果：

## 校准分析结果

**核心发现：wild-data FPR 是 decision-threshold 问题，不是概率校准问题。**

### 1. Platt/Isotonic 校准无效
| Model | C4 FPR | FW FPR | Wiki FPR | BalAcc | ECE |
|-------|--------|--------|----------|--------|-----|
| Uncalibrated | 33.41% | 16.90% | 0% | 0.780 | 0.052 |
| Platt | 36.51% | 19.48% | 0% | 0.781 | 0.051 |
| Isotonic | 38.62% | 21.05% | 0% | 0.776 | 0.051 |

ECE 已经很低（~0.05），RF 在 in-dist 上概率校准良好。Platt/Isotonic 反而略微增加 FPR。

### 2. P(d0) 分布是双峰的
- C4: ~33% 样本 P(d0) 集中在 0.15-0.30（moderate uncertainty），~67% 在 P(d0)>0.95
- 0.15-0.20 之间有 sharp transition（FPR 从 2.78% 跳到 19.63%）

### 3. 低阈值可有效缓解 FPR
| Threshold | C4 FPR | FW FPR | d0 recall | d1+ recall | BalAcc |
|-----------|--------|--------|-----------|------------|--------|
| argmax (default) | 33.41% | 16.90% | 0.996 | 0.998 | 0.780 |
| **0.15** | **2.78%** | **0.71%** | 0.999 | 0.990 | 0.777 |
| 0.10 | 0.69% | 0.15% | 0.999 | 0.986 | 0.775 |

**推荐操作点：P(d0) < 0.15 才标记为 d1+**。C4 FPR 从 33% 降到 2.78%，BalAcc 仅降 0.3%。

### 4. 对论文叙事的意义
- 回应审稿人"FPR without calibration mitigation"：可以说明 simple threshold adjustment 即可将 FPR 控制在 <3%
- 但需要注意 C004 约束：这不改变 C4 d1+ 预测是 OOD 假阳性的本质，只是展示 mitigation 方案

### 产出文件
`/root/autodl-tmp/recursive_gen_depth_est/results/wild_data_calibration/`:
- `threshold_calibration_results.json` (完整数据)
- 8 张分析图（reliability diagram, FPR curves, P(d0) distributions, PR curve, tradeoff plot）

---
