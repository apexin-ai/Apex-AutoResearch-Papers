# diagnose westd connectivity

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_connectivity_20260517T054259_result.json`
- **Structured JSON:** [`d074c109eef014ba5e17.json`](../../sessions/d0/d074c109eef014ba5e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-11672 不可达。**

错误信息：`[Errno None] Unable to connect to port 11672 on 36.103.198.204`

连接在 0.41 秒内被拒绝，说明端口完全不响应（服务器关机、实例被释放、或网络层阻断）。

### 汇报

| 项目 | 状态 |
|------|------|
| SSH 连接 | **失败** — port 11672 unreachable |
| 实验进程 | 无法确认，大概率已中断 |
| GPU/磁盘 | 无法检查 |

4 个实验（eval_sft_rasp_20_seed123、eval_sft_standard_20_seed123、eval_sft_rasp_20_seed456、eval_sft_standard_20_seed456）均应视为中断/失败。需要等服务器恢复后重新提交，或转移到 westb-23072 执行。

---
