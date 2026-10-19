# deploy pi05 crm training bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-crm-training-bjb1-18228_20260524T083322_result.json`
- **Structured JSON:** [`815502cd42f8740fd350.json`](../../sessions/81/815502cd42f8740fd350.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1 — Kill 旧进程** ✓
- PID 278846 (GPU 1) 和 279117 (GPU 2) 已 force kill
- bjb1-18228 和 cqa1-32758 的 tmux sessions 已清理

**Step 2 — 代码兼容性** ✓
- `train_crm_k1.py` 已有 `--reuse_merged_cache` 路径，直接加载 `obs_features.pt/k_samples.pt/expert_actions.pt`
- `MultiScaleCRM` 的 `set_normalization_stats` 正确处理 1D obs_mean（单尺度 fallback）
- 无需代码修改，只需传 `--obs_dim 2048 --reuse_merged_cache`

**Cache 维度确认**:
- Spatial: 60,250 samples, obs [60250, 2048], k_samples [60250, 10, 5, 6]
- Goal: 61,728 samples, obs [61728, 2048], k_samples [61728, 10, 5, 6]
- h_eff=5, action_dim=6, K=10 → K=1 取 sample[0]

**Step 4 — 训练已启动** ✓
- GPU 1 (525MB): `crm-pi05-spatial` — epoch 13/50, val_loss=0.004967, 持续下降
- GPU 2 (525MB): `crm-pi05-goal` — epoch 15/50, val_loss=0.004808, 持续下降
- 模型 536,418 params (vs SmolVLA 960D 时 ~327K，因 obs_dim=2048 增大)

**Step 6 — Registry** ✓
- `train-crm-pi05-spatial-k1`: RUNNING
- `train-crm-pi05-goal-k1`: RUNNING

---
