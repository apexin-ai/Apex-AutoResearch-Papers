# ops d066 llama scierc beam4 s1 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_scierc_beam4_s1_16980_20260520T142718_result.json`
- **Structured JSON:** [`068f520b3210f01097db.json`](../../sessions/06/068f520b3210f01097db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动并注册完毕。

**汇报：**

| 项目 | 值 |
|------|-----|
| **PID** | 766045 (python) / 766040 (bash wrapper) |
| **服务器** | westd-16980 GPU1 |
| **数据路径** | `data/processed_data/test.json` — 100 行（100 docs, 551 sentences）✓ |
| **GPU 状态** | 83% 利用率，18.3GB / 97.9GB 显存，模型已加载完毕正在推理 |
| **输出路径** | `/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_551_beam4_full_s1.jsonl` |
| **日志** | `/root/autodl-tmp/schema_outputs/d066_beam_sweep/llama_scierc_beam4_s1_551.log` |
| **Registry** | `d066_sweep_llama_scierc_beam4_s1_551` → RUNNING |
| **Cron** | 已注册，120s 轮询 |

注意：首次尝试失败因为系统 python3 没有 torch（miniconda3 未激活）。已用 conda base 环境重新启动成功。

---
