# ops verify libero proprio dims

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-libero-proprio-dims_20260518T101631_result.json`
- **Structured JSON:** [`4fd61063c6541ccd7839.json`](../../sessions/4f/4fd61063c6541ccd7839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 维度 | 值 | 组成 |
|---|---|---|
| **LIBERO 原始 proprio state** | **8D** | eef_pos(3) + eef_axisangle(3) + gripper_qpos(2) |
| **SmolVLA 输入 state** | **8D → pad 32D** | 8D 经 MEAN_STD 归一化后 zero-pad 到 max_state_dim=32 |
| **VLA 单步 action 输出** | **7D** | 6D pose + 1D gripper (`FULL_ACTION_DIM=7`) |
| **CRM 用的 action_dim** | **6D** | `CORRECTION_DIM=6`，仅修正 pose，不修正 gripper |
| **H_eff** | **5** | 从 chunk_size=50 截断 |
| **CRM correction 维度** | **30D** | = CORRECTION_DIM(6) × H_EFF(5) |
| **Uncertainty dim** (Gated CRM) | **40D** | = 6×5 + 5 + 5 (pose_var + entropy + norms) |

关键细节：
- Gripper 不经过 CRM 修正，evaluate.py 中取 K 个 sample 的 gripper 均值直接拼接
- `obs_dim=960` 是 VLM hidden_size，不是 proprio
- 论文 Method 写 `d=6` 对应的是 `CORRECTION_DIM`（仅 pose），论文 Experiments 写 "8D proprioceptive state" 是 SmolVLA 的输入 state，两者不矛盾

---
