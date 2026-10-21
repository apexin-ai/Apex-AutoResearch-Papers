# ops d066 llama beam8 unc check relay

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_beam8_unc_check_relay_20260520T132000_result.json`
- **Structured JSON:** [`ebf16a8ab9ed2babbfa6.json`](../../sessions/eb/ebf16a8ab9ed2babbfa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常启动，模型已加载到 GPU1。

## 报告

| 项目 | 状态 |
|------|------|
| **Llama beam8 unc** | 完成 — 200行 JSONL, 199成功/1失败 |
| **新启动配置** | `llama_docred_200_beam4_unconstrained` — PID 761033, GPU1 |
| **GPU0** | PID 756540 (beam8 s1), 64570 MiB |
| **GPU1** | PID 761033 (beam4 unc), 18270 MiB（模型加载中） |
| **磁盘** | `/root/autodl-tmp` 250G 用 171G, 余 80G (69%) |

注：首次用了 `--output_file`（不存在），已修正为 `--output_path` 重新启动。

---
