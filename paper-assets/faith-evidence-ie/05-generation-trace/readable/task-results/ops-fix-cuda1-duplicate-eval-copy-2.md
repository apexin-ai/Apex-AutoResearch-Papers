# ops fix cuda1 duplicate eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-cuda1-duplicate-eval_20260514T204307_result.json`
- **Structured JSON:** [`b3d066aeaf57a26addb6.json`](../../sessions/b3/b3d066aeaf57a26addb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**报告：**

| 项目 | 状态 |
|------|------|
| **PID 97333 (含子进程树)** | ✅ ALL KILLED（97333/97334/97339/97340 全部清除） |
| **PID 96500** | ✅ ALIVE，已运行 21 分钟，状态 Rl+（正在执行） |
| **ckpt-20 eval 结果** | 未完成，metrics.json 尚不存在 |
| **eval 进度** | 4/62 batches（~6%），每 batch 约 160s，预计还需 ~2.5 小时 |
| **cuda:1** | 仅 PID 96500 占用 9710 MiB，重复进程已清除干净 |

---
