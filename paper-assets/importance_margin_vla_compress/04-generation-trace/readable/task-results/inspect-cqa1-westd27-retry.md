# inspect cqa1 westd27 retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_cqa1_westd27_retry_20260526T022222_result.json`
- **Structured JSON:** [`0f24925e40e512c71ae9.json`](../../sessions/0f/0f24925e40e512c71ae9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台都连接失败：

```
cqa1-33015 | 失败 | Unable to connect to port 33015 on 58.144.141.28 (connection refused/端口不通)
westd-27271 | 失败 | Unable to connect to port 27271 on 36.103.198.204 (connection refused/端口不通)
```

两台都是 AutoDL 实例，端口连不上说明实例已关机或重启导致端口变更。需要去 AutoDL 控制台确认：
1. 实例是否还在运行
2. 如果重启过，获取新的 SSH 端口并更新 `~/.ssh/config`

---
