# code action prediction probe prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action-prediction-probe-prep_20260515T140041_result.json`
- **Structured JSON:** [`7dede223a98ab03431f9.json`](../../sessions/7d/7dede223a98ab03431f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/action_probe_design.md`。

**调研结果摘要**：

- Actions 是连续 7-dim float64：dims 0-2 position delta, dims 3-5 orientation delta, dim 6 gripper binary {-1, 1}
- Feature T 与 action T 完全对齐，50 demos/task，10 tasks
- Feature HDF5 不含 action，需从 LIBERO 原始 hdf5 加载，文件名映射 `{TASK}.h5` → `{TASK}_demo.hdf5`
- DINO 用 `traj_X` key vs VLA 用 `demo_X`，index 一一对应

**设计要点**：

- 预测 a_{t+1}（next action），比 a_t 更需要策略理解
- MLP regression probe (in→256→7)，MSE loss on per-dim standardized actions
- 核心指标：per-task mean R² 的 Δ(trained − untrained)
- 代码改动 ~170 行新增 + ~20 行修改，大量复用现有基础设施
- 三组对比运行（trained/untrained/dinov2），每组 ~5-10 分钟

---
