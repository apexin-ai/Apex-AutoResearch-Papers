# code control b label permutation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_control-b-label-permutation_20260515T121501_result.json`
- **Structured JSON:** [`7203f68cb4dbecfcbaae.json`](../../sessions/72/7203f68cb4dbecfcbaae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。`--shuffle_labels` 结果符合预期：

**Global ρ = 0.039, mean per-task ρ = 0.039, R² = -0.052**

Per-task ρ 值：

| Task | ρ |
|------|---|
| KITCHEN_SCENE3 (stove + moka pot) | 0.074 |
| KITCHEN_SCENE4 (bowl in drawer) | 0.046 |
| KITCHEN_SCENE6 (mug in microwave) | 0.071 |
| KITCHEN_SCENE8 (both moka pots) | 0.014 |
| LIVING_ROOM_1 (soup + cheese in basket) | 0.062 |
| LIVING_ROOM_2 (soup + sauce) | 0.018 |
| LIVING_ROOM_2 (cheese + butter) | 0.051 |
| LIVING_ROOM_5 (mugs on plates) | 0.093 |
| LIVING_ROOM_6 (mug + pudding) | 0.050 |
| STUDY_SCENE1 (book in caddy) | -0.091 |

所有 per-task ρ 都在 [-0.1, +0.1] 范围内，全局 ρ ≈ 0.04（p=0.049，本质上与随机一致）。R² 为负值表明模型预测不如直接用均值。这正是 label permutation negative control 的预期行为——打乱标签后 probe 无法学到有意义的映射。

代码修改完成并通过验证。三处改动：
1. **argparse**：新增 `--shuffle_labels` flag（line 63）
2. **模式检测**：运行时打印 mode 标识（line 430-431）
3. **标签置换**：训练前用 `torch.randperm` 独立打乱 y_tr 和 y_val（line 467-468）

原有 cross-trajectory shuffle 代码保持不变。

---
