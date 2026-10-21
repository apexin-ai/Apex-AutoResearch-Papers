# ops status check westd16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd16980_20260516T053804_result.json`
- **Structured JSON:** [`c833bf27a2c49dffdd3e.json`](../../sessions/c8/c833bf27a2c49dffdd3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均在运行中，状态正常。

## 状态汇总

| 实验 | PID | 状态 | 输出行数 | 进度 | 预计剩余 |
|------|-----|------|---------|------|---------|
| **w6_mistral_scierc_constrained** | 334606→334612 | 运行中, CPU=101%, 1.9GB RSS | 128/551 | 23.2% | ~9 min runtime, 刚启动不久，日志只有 pad_token_id 消息，还在前期 |
| **w5_qwen_docred_lora_constrained_eval** | 321568 | 运行中, CPU=100%, 1.9GB RSS | 604/998 | 60.5% | ~394 samples × ~17s ≈ **1.8h** |

**GPU:**
- GPU 0: 87% util, 14.7/97.9 GB (Mistral scierc)
- GPU 1: 85% util, 17.4/97.9 GB (Qwen DocRED)

**细节:**
- PID 334606 是 bash wrapper，实际 python 进程是子进程 334612（已运行 ~9 min，活跃）
- w5 Qwen DocRED 日志最后一行: `[486/998] Bill Warner (writer): FAIL E=0 R=0 76.1s`（输出文件比日志略快，正常的 buffer 延迟）
- 无 exit 文件，两个实验均未完成

无已完成实验，暂不需要提取 metrics。

---
