# diag k07 long failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_k07_long_failures_20260525T170601_result.json`
- **Structured JSON:** [`dbb9301c3d7a341420d9.json`](../../sessions/db/dbb9301c3d7a341420d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验都是误判，实际仍在正常运行。** Cron reconcile 错误标记了它们。

### 实验状态

| 实验 | GPU | PID | 已运行 | 当前进度 | 状态 |
|------|-----|-----|--------|----------|------|
| eval_openvla_attn_k07_long_seed42 | 0 | 214260 | 2h27m | Task 3/10, Ep 30/50 | 正常运行 |
| eval_openvla_l2norm_k07_long_seed42 | 1 | 214795 | 2h26m | Task 3/10, Ep 30/50 | 正常运行 |

- 两个日志各仅 41 行（输出被 Python buffer，虽然用了 `-u` 但 shell redirect 可能仍在缓冲）
- 无结果 JSON 文件——尚未完成
- 速度 ~0.9 eps/min，500 episodes 总计约 9 小时，预计还需 ~6-7 小时

### 早期数据（仅供参考，实验未完成）

| 实验 | Task 1 SR | Task 2 SR |
|------|-----------|-----------|
| Attn k=0.7 | 38.0% (19/50) | 24.0% (12/50) |
| L2norm k=0.7 | 42.0% (21/50) | 34.0% (17/50) |

### GPU 2 & 3 使用情况

| GPU | PID | 命令 | 已运行 |
|-----|-----|------|--------|
| 2 | 215329 | random_prune k=0.7, libero_10, seed42 | 2h26m |
| 3 | 215965 | l2norm_prune k=0.85, libero_10, seed42 | 2h25m |

4 卡全满载（15.8GB/98GB，利用率 67-80%），全在跑 k=0.7/0.85 的 Long suite eval。

### Registry 问题

Registry 状态已被 cron 设为 DONE(failed)，状态机不允许 DONE → RUNNING 回退。需要手动修复 registry 或等实验完成后直接更新为正确的 conclusion + metrics。

---
