# code offline singlestep action error

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_offline_singlestep_action_error_20260517T113724_result.json`
- **Structured JSON:** [`eb893fb4b03f8bed39be.json`](../../sessions/eb/eb893fb4b03f8bed39be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

**ACIS k=0.5 true_removal pruning 的离线单步 action 误差分析** (200 步, LIBERO demo data)

| 指标 | 值 |
|------|------|
| Bypass vs Pruned mean L2 | **1.284** |
| Bypass vs GT mean L2 | 0.414 |
| Pruned vs GT mean L2 | 1.391 |
| 相对误差 (L2/action_norm) | **111.5%** |

**Per-dimension 分解**:
- 位置 (xyz): 0.20-0.30
- 旋转 (xyz): 0.01-0.02 (很小)
- **Gripper: 1.02** (主要误差来源，相当于在 [-1,1] 上直接翻转)

**结论**: `large_per_step_error` — pruning 在每一步都直接破坏 action prediction，不是"小误差 compounding 到灾难"的情况。相对误差 >100% 意味着 pruning 引入的偏差超过了 action 本身的幅度。gripper 维度是主要贡献者，token 移除导致了离散 gripper 决策的翻转。

脚本保存在 `offline_singlestep_error.py`，JSON 结果在 `eval_results/offline_singlestep_error.json`，实验已注册为 `offline_singlestep_error_k05`。

---
