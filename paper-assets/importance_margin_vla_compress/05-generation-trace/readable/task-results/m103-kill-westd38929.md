# m103 kill westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_m103_kill_westd38929_20260525T005915_result.json`
- **Structured JSON:** [`7c02d21e9bf603627e4d.json`](../../sessions/7c/7c02d21e9bf603627e4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-38929 清理完毕。

**Killed 的 sessions（4 个）：**
| Session | GPU | Suite |
|---------|-----|-------|
| `eval_openvla_random_k09_goal_seed42_v2` | cuda:0 | goal |
| `eval_openvla_random_k09_spatial_seed42_v2` | cuda:1 | spatial |
| `eval_openvla_attn_k085_goal_seed42_v2` | cuda:2 | goal |
| `eval_openvla_attn_k085_spatial_seed42_v2` | cuda:3 | spatial |

**GPU 状态（全部释放）：**
| GPU | Utilization | Memory |
|-----|-------------|--------|
| 0 | 0% | 0 MiB / 97887 MiB |
| 1 | 0% | 0 MiB / 97887 MiB |
| 2 | 0% | 0 MiB / 97887 MiB |
| 3 | 0% | 0 MiB / 97887 MiB |

**Registry 更新：** 6 个实验标记为 `conclusion=killed, status=DONE`（4 个 v2 + 2 个原始版本）。原始的 `eval_openvla_attn_k085_goal_seed42` 和 `eval_openvla_attn_k085_spatial_seed42` 不在 RUNNING 列表中，未做修改。

**未动的 session：** `eval_xvla_random_k05_spatial_seed43`（非 OpenVLA，保留）。

---
