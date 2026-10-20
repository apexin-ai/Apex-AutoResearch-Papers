# diagnose server status 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_server_status_21461_20260520T033143_result.json`
- **Structured JSON:** [`e6744e684a6e4e0d9f78.json`](../../sessions/e6/e6744e684a6e4e0d9f78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态汇报

### 1. d066_beam_sweep k=8 con (SciERC)

| 项目 | 值 |
|------|-----|
| PID | 165391 |
| GPU | **GPU1** — 18912MiB, 82% util |
| 进度 | **355/551** (64.4%) |
| 速率 | ~5.2s/doc |
| 剩余 | ~17 min |
| 预计完成 | **~11:49** |
| 输出文件 | `/root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam8_full_s1.jsonl` (724KB, 369行) |

当前是 beam sweep 的**最后一个配置** (beam8_full_s1)。beam1/2/4 的 con+unc 和 beam8_unc 均已完成，eval 文件已生成。整个脚本从 07:23 开始运行。

### 2. d065_qwen_greedy_4096 unc (DocRED)

| 项目 | 值 |
|------|-----|
| PID | 167691 |
| GPU | **GPU0** — 18910MiB, 87% util |
| 进度 | **55/998** (5.5%) |
| 速率 | ~16.4s/doc |
| 剩余 | ~4.3 hours |
| 预计完成 | **~15:50** |
| 输出文件 | `/root/autodl-tmp/schema_outputs/d065_qwen_docred_greedy_unc_4096.jsonl` (564KB, 55行) |

DocRED 文档长、token 多 (max_new_tokens=4096)，推理慢是正常的。

### 额外发现

**d065_block_con** (PID 169446) 在 pts/2 上以 `sleep 30` 循环等待，运行脚本 `d065_block_con_21461.sh`，可能在排队等 GPU 空闲。

---
