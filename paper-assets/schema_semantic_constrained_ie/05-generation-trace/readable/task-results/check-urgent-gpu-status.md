# check urgent gpu status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_urgent-gpu-status_20260523T054339_result.json`
- **Structured JSON:** [`098141548639d7187e5a.json`](../../sessions/09/098141548639d7187e5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

### westd-21461（2× RTX PRO 6000 Blackwell, 各 96GB）

| GPU | 显存占用 | GPU利用率 | 温度 | 进程 |
|-----|---------|----------|------|------|
| GPU 0 | 39,254 / 97,887 MiB (40%) | 83% | 55°C | PID 106695 — `run_constrained_extraction.py`（刚启动约1分钟，13:42） |
| GPU 1 | 41,598 / 97,887 MiB (43%) | 87% | 52°C | PID 88995 — `run_constrained_extraction.py`（运行约5小时，08:40启动） |

**GPU 0 任务详情**：PID 106695，刚启动，具体参数输出被截断，但从 torch compile worker 的 parent PID 可确认是推理任务。

**GPU 1 任务详情**：70B LoRA DocRED full_s2 推理，模型 `Meta-Llama-3.1-70B-Instruct-AWQ-INT4`，checkpoint-1146，200 samples，输出到 `outputs/70b_lora_docred_200_full_s2.jsonl`。

---

### westd-16980（2× RTX PRO 6000 Blackwell, 各 96GB）

| GPU | 显存占用 | GPU利用率 | 温度 | 进程 |
|-----|---------|----------|------|------|
| GPU 0 | 0 / 97,887 MiB (0%) | 0% | 34°C | 无 |
| GPU 1 | 0 / 97,887 MiB (0%) | 0% | 34°C | 无 |

**两张卡完全空闲。** 服务器上有一些残留 Python 进程（http.server、download_wiki.py），但都不占 GPU。

---
