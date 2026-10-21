# ops ssh retry status check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ssh_retry_status_check_20260524T124323_result.json`
- **Structured JSON:** [`7c04fd8a01e7065e7b1c.json`](../../sessions/7c/7c04fd8a01e7065e7b1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器均 **SSH 认证失败**：

| 服务器 | 状态 | 错误 | 耗时 |
|--------|------|------|------|
| **westd-45947** | ❌ 失败 | Authentication failed | 3.13s |
| **westd-35807** | ❌ 失败 | Authentication failed | 2.69s |

连接未超时（2-3秒响应），说明服务器可达、端口正常，问题在**认证**（密钥或端口变更）。

可能原因：
1. **实例重启导致 SSH 端口变更**（AutoDL 常见问题）— 需要去控制台查新端口并更新 `~/.ssh/config`
2. **SSH 密钥被重置** — 需要重新配置

请去 AutoDL 控制台确认两台实例的当前 SSH 端口，并更新 `~/.ssh/config` 中对应的端口配置。

---
