# fix register 10894 crons

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_register_10894_crons_20260528T004414_result.json`
- **Structured JSON:** [`ca8c82a1f6546eed2041.json`](../../sessions/ca/ca8c82a1f6546eed2041.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 实验 | GPU | 确认 PID | 预期 PID | Cron ID | 状态 |
|------|-----|---------|---------|---------|------|
| vanilla_object_s1 | cuda:0 | **798980** | 798900 | `8d41dadc` | ✅ 存活，cron 已注册 |
| detach_ln_v2_s4 | cuda:1 | **822480** | 822402 | `289b2a51` | ✅ 存活，cron 已注册 |
| full_occ_bn_object_s0 | cuda:2 | **930834** | 930752 | `1c9dee3d` | ✅ 存活，cron 已注册 |
| detach_bn_object_s0 | cuda:3 | **931057** | 930908 | `64427350` | ✅ 存活，cron 已注册 |

**PID 偏差说明**：实际 PID 与预期差 78-149，均为同一实验的 GPU 子进程（通过 `/proc/&lt;pid>/cmdline` 中的 `--run_id_note` 确认身份匹配）。4 张 GPU 各占 ~62GB 显存，均在正常训练中。

**Cron 监控**：每 17 分钟检查一次各实验的进程存活状态和日志进度，进程异常终止时立即报告。Session-only，7 天后自动过期。

---
