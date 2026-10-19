# ops plan002 log and qwen3

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan002-log-and-qwen3_20260521T115444_result.json`
- **Structured JSON:** [`af2d159b21f76fce3cbd.json`](../../sessions/af/af2d159b21f76fce3cbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 任务 1: plan_002 — 已崩溃

- **PID 175859 已不存在**，进程已退出
- **日志末尾**显示 HuggingFace 模型下载失败：
  ```
  RuntimeError: Cannot send a request, as the client has been closed.
  EXIT_CODE=1
  ```
  模型还没开始加载就在下载阶段挂了，HTTP client 被关闭导致下载中断。
- **GPU 全部空闲**：4 张卡均 3 MiB / 0% 利用率

需要重新提交。崩溃原因是 HF Hub 网络问题——可能需要 `source /etc/network_turbo` 或设置 SSL 证书环境变量后再跑。

---

## 任务 2: Qwen3 — 仍在下载

- 已完成 shard：29/32（主目录中）
- `._____temp` 中还有 3 个 shard 正在下载：`00027`, `00029`, `00031`

剩余 3 个 shard，下载尚未完成。

---
