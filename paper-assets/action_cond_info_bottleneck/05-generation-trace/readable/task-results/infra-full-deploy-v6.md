# infra full deploy v6

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-deploy-v6_20260515T141603_result.json`
- **Structured JSON:** [`617e01c00ee9c61af233.json`](../../sessions/61/617e01c00ee9c61af233.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 连接两次均超时，按指示停止重试并报告。

---

## 部署报告（第 6 次尝试）

### 1. SSH 连接: **失败**
- 服务器: `westb-13953` (`connect.westb.seetacloud.com:13953`)
- 错误: `timed out` (10.09s)
- `detect_image` 同样返回 `SSH error: timed out`
- 两次尝试（`ssh_read_only` + `detect_image`）均超时

### 2-9. 后续阶段: **未执行**（SSH 不可达）

### 可能原因
- AutoDL 实例重启后 **SSH 端口可能已变更**（AutoDL 已知行为）
- 请到 AutoDL 控制台确认：
  1. 实例状态是否为"运行中"
  2. 当前 SSH 端口号是否仍为 `13953`
  3. 如端口已变，更新 `~/.ssh/config` 和项目配置后重新执行

---
