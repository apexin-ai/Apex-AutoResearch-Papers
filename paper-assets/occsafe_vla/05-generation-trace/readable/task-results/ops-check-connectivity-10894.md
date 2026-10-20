# ops check connectivity 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_connectivity_10894_20260529T114955_result.json`
- **Structured JSON:** [`6ff9d4ecb6aa23855870.json`](../../sessions/6f/6ff9d4ecb6aa23855870.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器都连不上。

### 汇报

**westd-10894:**
- SSH 连通性：**FAIL** — `Unable to connect to port 10894 on 36.103.198.204`
- 训练状态：无法检查
- Eval：未启动（SSH 不通）

**westd-34685:**
- SSH 连通性：**FAIL** — `Unable to connect to port 34685 on 36.103.198.204`
- 训练状态：无法检查
- Eval：未启动（SSH 不通）

两台都是 AutoDL 实例，端口连接失败通常意味着实例已关机或重启导致端口变更。需要到 AutoDL 控制台确认实例状态，如果实例重启了则更新 SSH 端口配置。

---
