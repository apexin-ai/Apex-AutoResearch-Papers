# analysis trajectory level cohens d collect

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_trajectory_level_cohens_d_collect_20260519T021948_result.json`
- **Structured JSON:** [`97f0c45bbe4b59eab042.json`](../../sessions/97/97f0c45bbe4b59eab042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

## Trajectory-level Cohen's d 结果

| Experiment | Condition | Token-level d | Traj-level d | 95% CI | N | Ratio (token/traj) |
|---|---|---|---|---|---|---|
| Head ablation | top24 | 0.651 | **2.943** | [2.469, 3.707] | 50 | 0.221 |
| Specificity | bottom24 | 0.565 | **2.347** | [1.854, 3.221] | 30 | 0.241 |
| Dose-response | top4 | 0.482 | **2.623** | [2.106, 3.575] | 30 | 0.184 |
| Dose-response | top8 | 0.508 | **2.186** | [1.764, 2.931] | 30 | 0.232 |
| Dose-response | top12 | 0.560 | **2.286** | [1.876, 3.043] | 30 | 0.245 |
| Dose-response | top16 | 0.592 | **2.400** | [1.895, 3.327] | 30 | 0.247 |
| Dose-response | top20 | 0.617 | **2.529** | [1.960, 3.639] | 30 | 0.244 |
| Dose-response | top24 | 0.637 | **2.601** | [2.127, 3.444] | 30 | 0.245 |
| Dose-response | top28 | 0.654 | **2.470** | [2.027, 3.268] | 30 | 0.265 |
| Dose-response | top32 | 0.639 | **2.695** | [2.226, 3.559] | 30 | 0.237 |
| Counterfactual | shuffled | 0.625 | **2.595** | [2.028, 3.791] | 30 | 0.241 |
| Counterfactual | paraphrased | 0.697 | **2.131** | [1.740, 2.819] | 30 | 0.327 |
| Counterfactual | wrong | 0.844 | **3.798** | [3.194, 4.938] | 30 | 0.222 |
| Counterfactual | empty | 0.968 | **3.438** | [2.921, 4.448] | 30 | 0.282 |

**Inflation factor (token/traj):** mean = 0.245, range [0.184, 0.327]

### 关键发现

原假设方向相反：token-level d 并非高估效应，而是**低估**了约 4 倍。Trajectory-level 聚合后，每个 demo 内 50 个 timestep 的噪声被平均掉，信噪比大幅提升，所有 trajectory-level d 均 > 2.0（"very large" effect）。所有 95% CI 下界 > 1.7，效应极其稳健。

---
