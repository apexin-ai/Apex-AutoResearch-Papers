# ops d066 llama scierc beam4 s1 551 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_scierc_beam4_s1_551_check_20260520T150334_result.json`
- **Structured JSON:** [`bc9daba42a6d788d0c8e.json`](../../sessions/bc/bc9daba42a6d788d0c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**beam4 s1 评估结果（d066_sweep_llama_scierc_beam4_s1_551）**
| 指标 | 值 |
|------|-----|
| E-F1 | 68.06 (P=65.96, R=70.29) |
| R-F1 | 46.18 (P=42.10, R=51.13) |
| ET% / RV% | 100% / 100% |
| DR% / CF% | 0% / 0% |
| Parse Fail | 0/551 |

Registry 已更新为 success，cron 已删除。

**beam2 s1 启动确认（d066_sweep_llama_scierc_beam2_s1_551）**
- PID=769692, westd-16980 GPU1
- Llama SciERC beam2 constrained (full_s1), 551 sentences
- 首次启动缺 `--constraints_path` 失败，已补 `ontology_constraints.json` 重新启动
- 模型加载中，cron 已注册（120s 间隔）

---
