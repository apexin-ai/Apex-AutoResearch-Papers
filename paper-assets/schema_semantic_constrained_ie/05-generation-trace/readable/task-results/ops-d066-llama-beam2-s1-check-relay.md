# ops d066 llama beam2 s1 check relay

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_beam2_s1_check_relay_20260520T120336_result.json`
- **Structured JSON:** [`4143f25d9ecfa89c7d80.json`](../../sessions/41/4143f25d9ecfa89c7d80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，模型已加载到 GPU1。

**汇报：**

| 项目 | 状态 |
|------|------|
| **Llama beam2 s1** | 完成。`llama_docred_200_beam2_full_s1.jsonl`，200行，199成功/1失败 |
| **Llama beam8 unc** | 已启动，PID 755444 |
| **GPU0** | Qwen beam8 s1 运行中（PID 748197，68134 MiB） |
| **GPU1** | Llama beam8 unc 运行中（PID 755449，18270 MiB，模型加载中） |

注：首次启动缺少 `--data_path` 和 `--constraints_path` 参数导致报错，已补全重新启动。

---
