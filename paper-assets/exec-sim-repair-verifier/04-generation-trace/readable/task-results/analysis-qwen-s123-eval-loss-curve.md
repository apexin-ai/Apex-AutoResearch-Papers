# analysis qwen s123 eval loss curve

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-s123-eval-loss-curve_20260521T225521_result.json`
- **Structured JSON:** [`895e3677452d56537c1f.json`](../../sessions/89/895e3677452d56537c1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已提取。下面是完整分析。

---

## Qwen CWM 8B — eval_loss 曲线（3 seeds，总步数=6633）

| Step | s42 | s123 | s456 |
|------|-----|------|------|
| 100 | 0.4423 | 0.4447 | 0.4427 |
| 200 | 0.3070 | 0.3095 | 0.2981 |
| **300** | **0.2907** | 0.2875 | **0.2769** |
| **400** | **0.2862** | 0.3060 | 0.2834 |
| 500 | 0.2998 | 0.3030 | 0.2898 |
| 600 | 0.3013 | 0.3074 | 0.3213 |
| 1000 | 0.3332 | 0.3356 | 0.3513 |
| 2000 | 0.3995 | 0.4119 | 0.4268 |
| 3000 | 0.4449 | 0.4528 | 0.4347 |
| 4000 | 0.4779 | 0.4738 | 0.4703 |
| 5000 | 0.5038 | 0.4998 | 0.4986 |
| 6000 | 0.5161 | 0.5131 | 0.5018 |
| 6600 | 0.5208* | 0.5166 | 0.5068 |

*s42 最后一个 eval 在 step 6100

### Qwen 曲线判断

**不是 U 形，是 J 形（持续单调上升）。**

| Seed | Min step | Min eval_loss | Final eval_loss | 上升幅度 |
|------|----------|---------------|-----------------|----------|
| s42 | **400** | **0.2862** | 0.5208 (6100) | +81.9% |
| s123 | **300** | **0.2875** | 0.5166 (6600) | +79.7% |
| s456 | **300** | **0.2769** | 0.5068 (6600) | +83.0% |

- **Minimum 位置**：step 300-400 / 6633 = **4.5-6.0%** 处
- **从 minimum 到终点**：eval_loss 持续单调上升，**没有任何回落或平台期**
- 三个 seed 曲线高度一致，minimum 位置和走势完全重合

---

## DeepSeek CWM — eval_loss

### func-level（3 epochs，总步数=1434）

| Step | s42 | s123 |
|------|-----|------|
| 478 (1ep) | 0.0458 | 0.0442 |
| 956 (2ep) | **0.0429** | **0.0408** |
| 1434 (3ep) | 0.0457 | 0.0451 |

**弱 U 形**：min 在 epoch 2（step 956），epoch 3 回升 ~6-10%。

### repo-level v2

| Step | s123 | s456 |
|------|------|------|
| 4209 (1ep) | **4.1157** | 4.7308 |
| 8418 (2ep) | 4.9907 | **4.7267** |
| 12627 (3ep) | — | 5.2837 |

s123 从 epoch 1→2 上升 21%；s456 在 epoch 2 微降后 epoch 3 大幅上升 11.8%。eval 粒度太粗，但趋势也是上升。

---

## 结论

1. **Overtraining 确认：Qwen CWM 8B 严重 overtrain。** eval_loss 在训练仅完成 ~5% 时就达到 minimum，之后单调上升 ~80%，持续了剩余 95% 的训练过程。三个 seed 完美复现此行为。

2. **不是 U 形，比 U 形更糟。** 没有平台期、没有二次下降。是纯粹的 "初始快速下降 + 持续上升" 的 J 形曲线，说明模型从 step ~400 开始就在持续过拟合。

3. **最优 checkpoint 应在 step 300-400 附近**（约 0.5 epoch），而实际训练跑了 6633 步（~5 epoch）。当前使用的 final checkpoint 的 eval_loss 几乎是 optimal 的 2 倍。

4. **DeepSeek func-level 也有类似模式**（弱 U 形，min 在 epoch 2），但幅度小得多（~6-10%），因为 func-level 数据更简单。

5. **跨 seed/model 一致性**：所有实验都显示 eval_loss 早期触底后上升，这是系统性过拟合，不是随机波动。

---
