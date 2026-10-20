# code d064 beam sweep prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d064_beam_sweep_prep_20260519T151214_result.json`
- **Structured JSON:** [`1fecf818d98339e3062a.json`](../../sessions/1f/1fecf818d98339e3062a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已部署 3 个脚本到两台服务器**，dry-run 全部通过：

| 服务器 | 脚本 | 任务 | 预估耗时 |
|--------|------|------|---------|
| westd-21461 | `d066_beam_sweep_scierc.sh` | Llama+Qwen × SciERC × beam 1,2,4,8 × unc/con | ~1h |
| westd-16980 | `d066_beam_sweep_docred.sh` | Llama+Qwen × DocRED × beam 1,2,4,8 × unc/con | ~45h |
| 两台 | `d066_analyze_beam_sweep.py` | 汇总 latency + violation rates + F1 | <1min |

**关键设计**：
- 推理脚本已内置 per-sample `inference_time_seconds`，无需额外计时
- Violation checker 集成在 sweep 脚本末尾自动运行
- 支持 resume（检查已完成输出，跳过）
- 两 GPU 并行（GPU0=Llama, GPU1=Qwen）

**启动方式**：d064 GPU 释放后直接 `nohup bash scripts/d066_beam_sweep_*.sh &`

报告已写入 `artifacts/_project/report/d066_beam_sweep_prep.md`。

---
