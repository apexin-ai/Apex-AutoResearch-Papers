# urgent westd38929 verify registry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd38929_verify_registry_20260525T042205_result.json`
- **Structured JSON:** [`4291ff61ae570a7729f1.json`](../../sessions/42/4291ff61ae570a7729f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：westd-38929 不可达。**

连接 `36.103.198.204:38929` 失败 — AutoDL 实例很可能已重启，SSH 端口已变更。

**Registry 状态：** 4 个 v3 实验均不存在。当前 RUNNING 的 7 个实验全在 westd-41074 和 westd-27271 上，且都是 v2 版本（Long/Object suite），无 Goal/Spatial v3 记录：

| Registry 中的 RUNNING 实验 | 服务器 |
|---|---|
| eval_openvla_attn_k09_long_seed42_v2 | westd-41074 |
| eval_openvla_attn_k085_long_seed42_v2 | westd-41074 |
| eval_openvla_random_k09_long_seed42_v2 | westd-41074 |
| eval_openvla_l2norm_k09_long_seed42_v2 | westd-41074 |
| eval_openvla_baseline_object_seed42_v2 | westd-27271 |
| eval_openvla_l2norm_k09_long_seed42 (killed) | westd-41074 |
| eval_openvla_random_k09_long_seed42 (killed) | westd-41074 |

**需要你做的：**
1. 去 AutoDL 控制台查 westd-38929 实例的新 SSH 端口，更新 `~/.ssh/config`
2. 确认实例是否还在运行（如果实例关机了，4 个 v3 实验已丢失，需要重新提交）

---
