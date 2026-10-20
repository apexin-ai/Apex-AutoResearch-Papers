# infra kill vllm cuda2

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-vllm-cuda2_20260512T161023_result.json`
- **Structured JSON:** [`30f42f851ab552fab8eb.json`](../../sessions/30/30f42f851ab552fab8eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**
- PID 110596 已终止（进程不存在）
- GPU 2 显存已释放：22105 MiB → **0 MiB**
- GPU 3 DPO 训练（PID 170853）未受影响：23105 MiB 不变

**6卡 GPU 状态：**

| GPU | 占用 | 总量 | 说明 |
|-----|------|------|------|
| 0 | 9669 MiB | 24564 MiB | |
| 1 | 0 MiB | 24564 MiB | 空闲 |
| 2 | **0 MiB** | 24564 MiB | **已释放** |
| 3 | 23105 MiB | 24564 MiB | DPO 训练运行中 |
| 4 | 8093 MiB | 24564 MiB | |
| 5 | 9311 MiB | 24564 MiB | |

---
