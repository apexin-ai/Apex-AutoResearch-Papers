# analysis r5 sigmoid steepness

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r5_sigmoid_steepness_20260520T204852_result.json`
- **Structured JSON:** [`55c2ea106aadc3d7376c.json`](../../sessions/55/55c2ea106aadc3d7376c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已注册。总结：

**数据验证**：T=10 和 T=20 的 s42 数据与任务表完全一致。多 seed 有偏差（α=0.10 s43=3/8; α=0.75 s44=0/8 可能是 19828 未 re-analyze）。

**拟合结果（Binomial MLE）**：

| 参数 | Sigmoid T=10 | Sigmoid Combined | 变化 |
|---|---|---|---|
| **k** | 478.0 ± 474.5 | 279.3 ± 527.6 | **-41.6%** |
| **α_c** | 0.4826 | 0.4512 | **-0.031 左移** |
| **y_max** | 0.750 | 0.750 | 不变 |
| **90% 过渡宽度** | 0.009 | 0.016 | **+72%** |

**模型比较**：
- Sigmoid ≈ Probit（AIC 完全一致：T=10 = 32.99，combined = 79.86），三个模型的 NLL 相同（13.496 / 36.929）
- Gen logistic 多 1 参数无改善，AIC 被惩罚 +2
- **所有模型不可区分**——数据本质上是阶跃函数，k 的 SE ≈ k 本身

**关键解读**：
- T=10 数据是 α≈0.48 处的近完美阶跃函数
- T=20 α=0.45=5/8 是唯一的亚平台非零点，迫使过渡变缓、α_c 左移
- 但即使加入 T=20，过渡仍然很陡（宽度仅 0.016），需要更多中间 α 数据点才能约束过渡形状

---
