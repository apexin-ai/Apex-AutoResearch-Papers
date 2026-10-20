# analysis matched tax prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matched_tax_prep_20260521T090914_result.json`
- **Structured JSON:** [`5811e7c32bf1d1b9109c.json`](../../sessions/58/5811e7c32bf1d1b9109c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**实验进度（截至 17:15 server time）**

| 实验 | GPU | 进度 | 速度 | ETA |
|------|-----|------|------|-----|
| 1.7B no-evi fix | cuda:0 | 204/247 (83%) | ~30s/it | **~17:35** |
| 4B no-evi fix | cuda:1 | 174/247 (70%) | ~30s/it | **~17:50** |
| 8B no-evi fix | cuda:2 | 136/247 (55%) | ~50s/it | **~18:45** |
| 4B with-evi | cuda:3 | 10/247 (4%) | ~38s/it | **~19:35** |

**验证结果**
- 4 个 running 进程命令行已通过 `ps aux` 确认：所有 fix 版均使用正确 SFT adapter + `--no_evidence` flag
- 8B with-evi@2048 结果完整：ign_f1=0.5012, predictions.json 9.7MB, format_ok=984/985
- 无异常

**Fair tax 计算就绪情况**
- 脚本：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`
- 1.7B pair：with-evi ✅ + no-evi fix ETA 17:35 → **最早 17:35 可算**
- 8B pair：with-evi ✅ + no-evi fix ETA 18:45 → **最早 18:45 可算**
- 4B pair：with-evi ETA 19:35 (瓶颈) + no-evi fix ETA 17:50 → **最早 19:35 可算**

具体命令已写入 memory.md。

---
