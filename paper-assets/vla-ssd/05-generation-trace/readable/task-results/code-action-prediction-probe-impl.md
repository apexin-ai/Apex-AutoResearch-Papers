# code action prediction probe impl

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action-prediction-probe-impl_20260515T141150_result.json`
- **Structured JSON:** [`323a410dd76769f61173.json`](../../sessions/32/323a410dd76769f61173.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。实现完成，结果如下：

**Layer 4 (trained) 测试结果：**
- Overall R² = 0.536, Per-task mean R² = 0.543
- Gripper accuracy = 85.5%
- Per-dim R²: dx=0.47, dy=0.61, dz=0.35, drx=0.37, dry=0.18, drz=0.63, gripper=0.55
- Raw MSE = 0.090

**代码修改（`/root/vla-ssd/scripts/train_probes.py`）：**
1. `ActionMLPProbe` class — 7-dim 输出的 MLP
2. `load_actions()` — 从 LIBERO HDF5 加载 action，自动处理 `demo_X`/`traj_X` key 映射
3. `run_action_prediction()` — 完整 runner：shifted pairs (h_t→a_{t+1})、per-dim z-score standardization、训练+early stopping、per-dim R²/overall R²/per-task R²/gripper accuracy/raw MSE
4. `parse_args` 加了 `action_prediction` choice 和 `--data_dir` 参数
5. `save_results` 加了 action_prediction 的 CSV fields 和 summary best_layer 选择
6. `main` runners dict 加了 `action_prediction`

备份在 `train_probes.py.bak3`。

---
