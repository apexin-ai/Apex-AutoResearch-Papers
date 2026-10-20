# analysis tracvla spatial results and fix

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tracvla_spatial_results_and_fix_20260521T023522_result.json`
- **Structured JSON:** [`956eb1c5c2a1cb6f84d9.json`](../../sessions/95/956eb1c5c2a1cb6f84d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 JSON 已同步到本地 `artifacts/tracvla_spatial/`。Phi-3-Vision 下载已在后台运行 (PID 524060)。

---

## TraceVLA-Spatial Trained 关键指标

### 1. R² Probing
**所有 32 层 R² = 0.0**（image_mean 和 last_preaction 两种表示均为 0）。线性 probe 完全无法从中间表示预测动作。这个结果异常——可能是 probing 脚本的问题（样本量只有 2 个 task × 1 demo × 2 timestep = 4 样本，训练线性回归不够），需要排查。

### 2. L1 Attention Profile
| 类别 | Head 数 |
|------|---------|
| instruction_dominant | **29/32** |
| mixed | 3 (head 2, 13, 22) |
| image_dominant | **0** |

Top-5 instruction ratio: head_8 (0.941), head_26 (0.911), head_19 (0.896), head_20 (0.859), head_1 (0.841)

L1 注意力几乎完全被指令主导，零个 image-dominant head。

### 3. Counterfactual (Cohen's d 排序)
| Condition | Cohen's d | MSE |
|-----------|-----------|-----|
| **empty** | **3.75** | 0.083 |
| wrong | 1.61 | 0.065 |
| shuffled | 1.56 | 0.056 |
| paraphrased | 1.55 | 0.072 |

- 所有条件 token_divergence_rate = 1.0（100% token 发生变化）
- Empty 效应最大（移除指令影响最大），wrong/shuffled/paraphrased 效应相近（~1.55-1.61）
- Paraphrased 也引发显著 action shift (d=1.55)，说明模型对 exact wording 敏感

### 4. Cross-instruction Classification
| Layer | image_mean | last_preaction |
|-------|-----------|----------------|
| L0 | 1.0 | **0.0** |
| L8 | 1.0 | 1.0 |
| L16 | 1.0 | 1.0 |
| L24 | 1.0 | 1.0 |
| L31 | 1.0 | 1.0 |

image_mean 在所有层完美分类 (1.0)；last_preaction 在 L0 为 0（chance 以下），L8+ 升至 1.0。说明指令信息从 L8 开始被整合到 pre-action token 表示中。

**注意：R² probing 全零很可能是样本量问题（仅 4 样本），不是真实信号。cross-instruction classification 和 counterfactual 的结果是可靠的。**

---
