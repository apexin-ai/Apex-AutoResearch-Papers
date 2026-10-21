# infra ssh debug 4090x4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_ssh-debug-4090x4_20260513T094353_result.json`
- **Structured JSON:** [`e2df6fb64aee08791752.json`](../../sessions/e2/e2df6fb64aee08791752.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已修复，`autodl-4090x4` 连接成功。**

## 排查结论

| 项目 | 结果 |
|------|------|
| **根因** | `resources.yaml` 中 `autodl-4090x4` 条目缺少 `password_encrypted` 字段 |
| **修复** | 从 `bjb1-18228`（同一台服务器）复制 `password_encrypted` 到 `autodl-4090x4` 的 accounts 下 |
| **验证** | 连接成功，4×RTX 4090 全部可用 |

两个条目 `autodl-4090x4` 和 `bjb1-18228` 指向同一台机器（`connect.bjb1.seetacloud.com:18228`），区别在于 `bjb1-18228` 有完整配置（密码、GPU 分配、项目名），而 `autodl-4090x4` 是一个不完整的条目。后续建议统一使用 `bjb1-18228` 或确保两个条目配置同步。

---
