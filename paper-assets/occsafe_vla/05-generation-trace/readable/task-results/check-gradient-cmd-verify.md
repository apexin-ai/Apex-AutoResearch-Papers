# check gradient cmd verify

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gradient-cmd-verify_20260527T033538_result.json`
- **Structured JSON:** [`eb114b2b33eb8b41522c.json`](../../sessions/eb/eb114b2b33eb8b41522c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，修正后的命令已写入 `gradient_commands_verified.md`（artifact `art_20260527_7a1aae`）。

**关键发现与修正：**

| # | 条件 | Checkpoint | 服务器 / GPU |
|---|------|-----------|-------------|
| 1 | Vanilla | `vanilla_v2_s1` | westd-34685 cuda:0 |
| 2 | Full OCC BN | `full_occ_bn_v2_s1` | westd-34685 cuda:1 |
| 3 | Full OCC LN | `full_occ_ln_s3_v2` | westd-10894 cuda:0 |
| 4 | Detach BN | `detach_bn_v2_s1` | westd-34685 cuda:2 |
| 5 | **Detach LN** (已修正) | `detach_ln_s3` | westd-34685 cuda:3 |

**修正内容**：条件5从错误的 Detach BN 重复改为 `detach_ln_s3`（在 westd-34685 上找到）。所有5个checkpoint路径均已验证存在，condition_name 全部唯一，5条命令可并行执行。

---
