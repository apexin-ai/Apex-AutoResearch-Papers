# debug trajectory level d check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_trajectory_level_d_check_20260519T024110_result.json`
- **Structured JSON:** [`daf395537b1c6b71ba20.json`](../../sessions/da/daf395537b1c6b71ba20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注册表已由之前的 Worker 完整填写（status=DONE, conclusion=success）。

## 结果

| Experiment | Condition | Token-level d | Trajectory-level d | 95% CI | N demos | Ratio (token/traj) |
|---|---|---|---|---|---|---|
| head_ablation | top24 | 0.651 | 2.943 | [2.469, 3.707] | 50 | 0.22x |
| specificity | bottom24 | 0.565 | 2.347 | [1.854, 3.221] | 30 | 0.24x |
| counterfactual | empty | 0.968 | 3.438 | [2.921, 4.448] | 30 | 0.28x |
| counterfactual | wrong | 0.844 | 3.798 | [3.194, 4.938] | 30 | 0.22x |
| counterfactual | shuffled | 0.625 | 2.595 | [2.028, 3.791] | 30 | 0.24x |
| counterfactual | paraphrased | 0.697 | 2.131 | [1.740, 2.819] | 30 | 0.33x |
| dose_response | top4 | 0.482 | 2.623 | [2.106, 3.575] | 30 | 0.18x |
| dose_response | top8 | 0.508 | 2.186 | [1.764, 2.931] | 30 | 0.23x |
| dose_response | top12 | 0.560 | 2.286 | [1.876, 3.043] | 30 | 0.24x |
| dose_response | top16 | 0.592 | 2.400 | [1.895, 3.327] | 30 | 0.25x |
| dose_response | top20 | 0.617 | 2.529 | [1.960, 3.639] | 30 | 0.24x |
| dose_response | top24 | 0.637 | 2.601 | [2.127, 3.444] | 30 | 0.24x |
| dose_response | top28 | 0.654 | 2.470 | [2.027, 3.268] | 30 | 0.26x |
| dose_response | top32 | 0.639 | 2.695 | [2.226, 3.559] | 30 | 0.24x |

**Inflation factor (token/trajectory)**: mean = 0.245, range [0.184, 0.327]

### 核心发现

与原始假设（autocorrelation 导致 token-level d 高估）相反：trajectory-level d **远大于** token-level d（约 3-5 倍）。原因：demo 内 50 个 timestep 取平均后噪声被平滑掉，std 大幅缩小，d = mean/std 随之增大。

Token-level d 实际上是**保守估计**。所有条件在 trajectory level 下 d > 2.0（CI 下界均 > 1.7），效应非常强。

注册表已完整：status=DONE, conclusion=success, 含全部 14 个条件的 metrics。

---
