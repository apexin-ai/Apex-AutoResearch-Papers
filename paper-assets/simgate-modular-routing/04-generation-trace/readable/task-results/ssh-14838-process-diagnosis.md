# ssh 14838 process diagnosis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14838-process-diagnosis_20260517T215256_result.json`
- **Structured JSON:** [`0a1be1667c291161a75d.json`](../../sessions/0a/0a1be1667c291161a75d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，结果已写入 `artifacts/14838_diagnosis.md`。

**摘要：**

| GPU | 状态 | 说明 |
|-----|------|------|
| 0 | DEAD | vLLM EngineDeadError 崩溃（engine core 内部异常） |
| 1 | ALIVE | PID 69734 正常运行，正在跑最后一个 task (measure-melting-point)，即将完成 |
| 2 | DEAD | PID 540229 不存在 |
| 3 | — | 空闲 |

**GPU 0, 2, 3 三卡空闲可用。** cuda:1 预计短期内完成全部 7 个 task 的收集。

---
