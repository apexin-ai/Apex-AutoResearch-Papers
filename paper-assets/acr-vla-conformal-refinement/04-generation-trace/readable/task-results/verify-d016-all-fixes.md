# verify d016 all fixes

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d016-all-fixes_20260514T074650_result.json`
- **Structured JSON:** [`b1554ab5a0b1865c2cc0.json`](../../sessions/b1/b1554ab5a0b1865c2cc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the verification report:

---

```
Fix C1: ✅ — 6D→8D state 正确
```
- `utils.py:81-84`: `ee_states` 拼接 `demo["obs/ee_states"]` (T,6) 和 `demo["obs/gripper_states"]` (T,2)，axis=-1，输出 (T,8)。docstring 也更新为 `(T, 8)`。
- `smolvla_wrapper.py:72`: `state_mean` shape 为 (8,)。
- `smolvla_wrapper.py:90-93`: `_normalize_state` 用 `D = state_raw.shape[-1]`，然后 `self.state_mean[:D]`、`self.state_std[:D]`，可处理任意 D≤8。
- `evaluate.py:80-84`: `get_robot_state` 拼接 `eef_pos(3) + eef_axisangle(3) + gripper_qpos(2)` = 8D。与训练一致。

```
Fix W3: ✅ — alpha 0.1→0.5 正确
```
- `cgs.py:26`: `alpha=0.5`，注释标注 BugFix W3。
- `cgs.py:101`: `q_idx = ceil((1-0.5)*(10+1)) - 1 = ceil(5.5) - 1 = 6 - 1 = 5`。K=10 时 index=5 是排序后第 6 个值（0-indexed），即中位数。正确。

```
Fix W2: ✅ — argmin base action 逻辑正确
```
- `crm.py:44`: 参数名为 `base_action`（非 mean_action）。`crm.py:62`: `return base_action + delta`，残差结构正确。
- `evaluate.py:172-179`: `select_action_crm` 中 argmin 逻辑——`k_pose_flat` (K,30)，计算到 mean 的 L2 距离，`best_idx = distances.argmin()`，取 `k_pose_flat[best_idx]` 作为 base_action。
- `train_crm.py:285-292`: `_argmin_base_action` 辅助函数——batch 版本，`k_flat` (B,K,30)，`mean_a` (B,1,30)，`dists = ((k_flat - mean_a)**2).sum(dim=-1)` (B,K)，`best_idx = dists.argmin(dim=1)` (B,)，fancy indexing取 (B,30)。
- 训练循环 (line 401) 和验证循环 (line 447) 均调用 `_argmin_base_action(k_samp)`。
- gripper 维度：`evaluate.py:181` 用 `k_full[:, :, CORRECTION_DIM:].mean(dim=0)` 作为 gripper，不受 argmin 影响。

```
Fix W4: ✅ — L2 norm clipping 正确
```
- `crm.py:18`: `max_correction_norm=1.42`。
- `crm.py:58-61`: `delta = self.net(x)` 后：
  - `delta_norm = delta.norm(dim=-1, keepdim=True)`
  - `delta = delta * torch.clamp(self.max_correction_norm / (delta_norm + 1e-8), max=1.0)`
  - `max=1.0` 确保只缩小不放大（当 norm ≤ max_correction_norm 时 ratio ≥ 1，被 clamp 到 1.0）。

```
Train/Eval 一致性: ✅
```
两处 argmin 逻辑完全一致：都是 L2 距离到 mean，取 argmin。`evaluate.py` 是单样本版 (K,30)→scalar idx，`train_crm.py` 是 batch 版 (B,K,30)→(B,) idx，数学等价。

---
