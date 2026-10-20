# ops check disk qwen3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-disk-qwen3_20260518T125856_result.json`
- **Structured JSON:** [`2e089fc2a171a2a2b1d5.json`](../../sessions/2e/2e089fc2a171a2a2b1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## 磁盘空间

| 分区 | 挂载点 | 总量 | 已用 | 可用 | 用量 |
|------|--------|------|------|------|------|
| overlay | / (含 /root) | 30G | 12G | 19G | 38% |
| /dev/md0 | /root/autodl-tmp | **250G** | 151G | **100G** | 61% |
| /dev/sda2 | (系统盘) | 879G | 407G | 427G | 49% |

**`/root/autodl-tmp` 是独立分区，250G 总量，100G 可用。空间充足，继续下载没问题。**

## Qwen3-14B 下载状态

- **PID 29779 运行中**，20:48 启动，已运行约 11 分钟，CPU 28.6%
- 已下载：**16G**（完整约 28G，进度约 57%）
- 下载完成后 autodl-tmp 预计剩余约 88G，完全够用

## autodl-tmp/models/ 已有模型

| 模型 | 占用 |
|------|------|
| Qwen2.5-72B-Instruct | 75G |
| Qwen2.5-14B-Instruct | 28G |
| Qwen3-14B (下载中) | 16G |
| Llama-3.1-8B-Instruct | 存在 |
| Mistral-7B-Instruct-v0.3 | 存在 |

## exp-026 状态

- **PID 27245 运行中**，20:11 启动，正常执行
- vLLM 服务端 (Qwen2.5-14B) PID 23182 正常
- 最新日志 20:59:25 仍在持续发送推理请求，HTTP 200 OK，一切正常

---
