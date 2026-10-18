# registry cleanup phantom running

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_cleanup_phantom_running_20260522T200606_result.json`
- **Structured JSON:** [`716c2189e14f85f5ade3.json`](../../sessions/71/716c2189e14f85f5ade3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 汇报

**RUNNING 数变化：31 → 10**

### 标为 DONE (negative) — 20 条

**>24h 无 metrics（2 条）：**
- `train_openvla_sc_m64_seed42_v6` — stale >24h
- `train_openvla_sc_m96_seed42_v3` — stale >24h

**短名重复（5 条）：**
| 短名（已清理） | 对应长名 |
|---|---|
| `pi05_l2norm_k085_goal_s42` | `eval_pi05_l2norm_k085_goal_seed42_w38929` |
| `pi05_random_k09_goal_s42` | `eval_pi05_random_k09_goal_seed42` |
| `pi05_l2norm_k095_long_s42` | `eval_pi05_l2norm_k095_long_seed42` |
| `random_k095_long_seed42` | `eval_pi05_random_k095_long_seed42` |
| `l2norm_k095_goal_seed42` | `eval_pi05_l2norm_k095_goal_seed42` |

**版本替代（1 条）：**
- `eval_pi05_random_k085_goal_seed42_v2` — superseded by v3

**4-24h 无 metrics（12 条）：**
- `eval_pi05_l2norm_k07_goal_seed42` (6h)
- `eval_pi05_l2norm_k085_goal_seed42_w38929` (6h)
- `eval_pi05_random_k09_goal_seed42` (8h)
- `eval_pi05_l2norm_k095_long_seed42` (8h)
- `pi05_l2norm_k09_goal_s42` (9h, 50-ep)
- `random_k095_goal_seed42` (10h, 50-ep)
- `eval_pi05_baseline_long_seed42` (10h, 50-ep)
- `eval_pi05_l2norm_k0925_object_seed43_v2` (10h)
- `eval_pi05_l2norm_k095_object_seed43_v2` (10h)
- `eval_pi05_l2norm_k09_object_seed43` (11h)
- `eval_pi05_random_k05_spatial_seed43` (14h)
- `eval_pi05_l2norm_k0925_spatial_seed43` (14h)

### 保留 RUNNING — 10 条
全部为最近 4h 内启动的 eval 任务（Long/Goal suite）。

### Metrics 格式问题
被清理的 20 条均无 metrics 记录，无需格式修正。

### 注意
Registry 不支持 `FAILED` 状态（合法值：ALLOCATED/ANALYZING/DEPLOYED/DEPLOYING/DONE/PENDING/PREPARING/QUEUED/RUNNING），所有需要标记失败的条目统一用 `DONE(negative)` + `failure_reason` 字段记录原因。

---
