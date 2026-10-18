# fix register unregistered exps

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_register_unregistered_exps_20260526T081227_result.json`
- **Structured JSON:** [`f793e8cfef58b3c89d6f.json`](../../sessions/f7/f793e8cfef58b3c89d6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| exp_id | 操作 | 最终状态 |
|--------|------|---------|
| `eval_pi05_random_k075_long_seed42_v2` | 状态修正 PREPARING→DONE | **DONE** (SR=62.4%) |
| `eval_pi05_attention_k075_long_seed42` | 状态修正 ALLOCATED→RUNNING, PID更新 | **RUNNING** |
| `eval_pi05_l2norm_k05_long_seed42_v4` | 新建条目（原条目 DONE 锁死） | **RUNNING** |
| `eval_pi05_random_k05_long_seed42_v3` | 新建条目（原条目 DONE 锁死） | **RUNNING** |
| `eval_openvla_random_k085_long_seed42_v3` | 状态修正 PREPARING→RUNNING, PID更新 | **RUNNING** |
| `eval_openvla_random_k085_object_seed42_v2` | 状态修正 PREPARING→RUNNING, PID更新 | **RUNNING** |
| `eval_openvla_random_k05_long_seed42_v2` | 状态修正 PREPARING→RUNNING, PID更新 | **RUNNING** |
| `eval_openvla_l2norm_k07_object_seed42_v3` | 新建条目（原条目 DEPLOYED 锁死） | **RUNNING** |

所有 9 个实验中，8 个已注册（PID 3728 的进程已完成直接标 DONE），1 个（westd-38929 GPU3）按要求跳过。原条目状态锁死的 3 个创建了新版本条目。

---
